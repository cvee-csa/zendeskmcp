import base64
import json
import secrets
import time
import urllib.parse
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional

import requests as _requests
from zenpy import Zenpy
from zenpy.lib.api_objects import Comment
from zenpy.lib.api_objects import Ticket as ZenpyTicket


class ZendeskClient:
    TOKEN_REFRESH_BUFFER_SECONDS = 60

    # Allowed image MIME types. SVG is excluded because it can contain active content.
    _ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/gif", "image/webp"}
    _MAGIC_BYTES: Dict[str, List[bytes]] = {
        "image/jpeg": [b"\xff\xd8\xff"],
        "image/png": [b"\x89PNG\r\n\x1a\n"],
        "image/gif": [b"GIF87a", b"GIF89a"],
        "image/webp": [b"RIFF"],
    }
    _MAX_ATTACHMENT_BYTES = 10 * 1024 * 1024

    def __init__(
        self,
        subdomain: str,
        email: Optional[str] = None,
        token: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        redirect_uri: str = "https://localhost/callback",
        oauth_scopes: str = "read write",
        oauth_token_path: str | Path = ".zendesk_oauth_tokens.json",
        timeout: int = 30,
    ):
        self.subdomain = (subdomain or "").strip()
        self.email = (email or "").strip()
        self.token = (token or "").strip()
        self.client_id = (client_id or "").strip()
        self.client_secret = (client_secret or "").strip()
        self.redirect_uri = redirect_uri.strip()
        self.oauth_scopes = oauth_scopes.strip()
        self.oauth_token_path = Path(oauth_token_path)
        self.timeout = timeout
        self.base_url = f"https://{self.subdomain}.zendesk.com/api/v2"
        self._pending_oauth_state: Optional[str] = None
        self.client: Optional[Zenpy] = None
        self.auth_header = ""
        self._configure_client()

    def _has_oauth_config(self) -> bool:
        return bool(self.client_id and self.client_secret)

    def _has_api_token_config(self) -> bool:
        return bool(self.email and self.token)

    def auth_mode(self) -> Literal["oauth", "api_token"]:
        if self._has_oauth_config():
            return "oauth"
        if self._has_api_token_config():
            return "api_token"
        raise ValueError(
            "Missing Zendesk auth configuration. Set either "
            "ZENDESK_CLIENT_ID/ZENDESK_CLIENT_SECRET or ZENDESK_EMAIL/ZENDESK_API_KEY."
        )

    def _configure_client(self) -> None:
        if not self.subdomain:
            return
        if not self._has_oauth_config() and not self._has_api_token_config():
            return
        mode = self.auth_mode()
        if mode == "oauth":
            token_data = self._load_token_data()
            if not token_data:
                self.client = None
                self.auth_header = ""
                return
            access_token = self._get_access_token()
            self.client = Zenpy(subdomain=self.subdomain, oauth_token=access_token)
            self.auth_header = f"Bearer {access_token}"
        else:
            self.client = Zenpy(subdomain=self.subdomain, email=self.email, token=self.token)
            self.auth_header = self._legacy_auth_header()

    def _ensure_client(self) -> None:
        if self.client is None:
            self._configure_client()
        if self.client is None:
            raise ValueError(
                "Zendesk client is not authenticated. Configure either legacy API token auth "
                "or complete the OAuth flow first."
            )

    def _legacy_auth_header(self) -> str:
        credentials = f"{self.email}/token:{self.token}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode("ascii")
        return f"Basic {encoded_credentials}"

    def _oauth_token_url(self) -> str:
        return f"https://{self.subdomain}.zendesk.com/oauth/tokens"

    def _oauth_authorization_url(self, *, state: str, scope: Optional[str] = None) -> str:
        if not self._has_oauth_config():
            raise ValueError("OAuth authorization requires ZENDESK_CLIENT_ID and ZENDESK_CLIENT_SECRET.")
        query = urllib.parse.urlencode(
            {
                "response_type": "code",
                "client_id": self.client_id,
                "redirect_uri": self.redirect_uri,
                "scope": (scope or self.oauth_scopes).strip(),
                "state": state,
            }
        )
        return f"https://{self.subdomain}.zendesk.com/oauth/authorizations/new?{query}"

    def _load_token_data(self) -> Optional[Dict[str, Any]]:
        if not self.oauth_token_path.exists():
            return None
        try:
            return json.loads(self.oauth_token_path.read_text())
        except json.JSONDecodeError as exc:
            raise ValueError(f"OAuth token file is invalid JSON: {self.oauth_token_path}") from exc

    def _save_token_data(self, token_data: Dict[str, Any]) -> None:
        self.oauth_token_path.parent.mkdir(parents=True, exist_ok=True)
        self.oauth_token_path.write_text(json.dumps(token_data, indent=2))

    def _token_expired(self, token_data: Dict[str, Any]) -> bool:
        return int(token_data.get("expires_at", 0)) <= int(time.time())

    def _build_stored_token_data(
        self,
        token_response: Dict[str, Any],
        *,
        preserve_refresh_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        refresh_token = token_response.get("refresh_token") or preserve_refresh_token
        if not refresh_token:
            raise ValueError("Zendesk OAuth response did not include a refresh token.")
        expires_in = int(token_response["expires_in"])
        stored = {
            "access_token": token_response["access_token"],
            "refresh_token": refresh_token,
            "token_type": token_response.get("token_type", "bearer"),
            "scope": token_response.get("scope", self.oauth_scopes),
            "expires_in": expires_in,
            "expires_at": int(time.time()) + expires_in - self.TOKEN_REFRESH_BUFFER_SECONDS,
        }
        if "refresh_token_expires_in" in token_response:
            stored["refresh_token_expires_in"] = token_response["refresh_token_expires_in"]
        return stored

    def _exchange_authorization_code(self, code: str) -> Dict[str, Any]:
        response = _requests.post(
            self._oauth_token_url(),
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "authorization_code",
                "code": code,
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "redirect_uri": self.redirect_uri,
                "scope": self.oauth_scopes,
            },
            timeout=self.timeout,
        )
        response.raise_for_status()
        return self._build_stored_token_data(response.json())

    def _refresh_access_token(self) -> Dict[str, Any]:
        token_data = self._load_token_data()
        if not token_data or "refresh_token" not in token_data:
            raise ValueError(
                "No Zendesk OAuth refresh token is stored. Run begin_oauth_authorization and complete_oauth_authorization first."
            )
        response = _requests.post(
            self._oauth_token_url(),
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "refresh_token",
                "refresh_token": token_data["refresh_token"],
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            },
            timeout=self.timeout,
        )
        response.raise_for_status()
        refreshed = self._build_stored_token_data(
            response.json(),
            preserve_refresh_token=token_data["refresh_token"],
        )
        self._save_token_data(refreshed)
        return refreshed

    def _get_access_token(self, *, force_refresh: bool = False) -> str:
        if not self._has_oauth_config():
            raise ValueError("OAuth access tokens require ZENDESK_CLIENT_ID and ZENDESK_CLIENT_SECRET.")
        token_data = self._load_token_data()
        if not token_data:
            raise ValueError(
                f"No Zendesk OAuth token file found at {self.oauth_token_path}. "
                "Run begin_oauth_authorization and complete_oauth_authorization first."
            )
        if force_refresh or self._token_expired(token_data):
            token_data = self._refresh_access_token()
        return str(token_data["access_token"])

    def _request(self, method: str, url: str, **kwargs: Any) -> _requests.Response:
        self._ensure_client()
        headers = dict(kwargs.pop("headers", {}))
        headers["Authorization"] = self.auth_header
        response = _requests.request(method, url, headers=headers, timeout=self.timeout, **kwargs)
        if self.auth_mode() == "oauth" and response.status_code == 401:
            access_token = self._get_access_token(force_refresh=True)
            self.client = Zenpy(subdomain=self.subdomain, oauth_token=access_token)
            self.auth_header = f"Bearer {access_token}"
            headers["Authorization"] = self.auth_header
            response = _requests.request(method, url, headers=headers, timeout=self.timeout, **kwargs)
        response.raise_for_status()
        return response

    def begin_oauth_authorization(self, scope: Optional[str] = None) -> Dict[str, Any]:
        if not self._has_oauth_config():
            raise ValueError("begin_oauth_authorization requires ZENDESK_CLIENT_ID and ZENDESK_CLIENT_SECRET.")
        self._pending_oauth_state = secrets.token_urlsafe(24)
        selected_scope = (scope or self.oauth_scopes).strip()
        if not selected_scope:
            raise ValueError("scope must not be empty.")
        return {
            "authorization_url": self._oauth_authorization_url(
                state=self._pending_oauth_state,
                scope=selected_scope,
            ),
            "state": self._pending_oauth_state,
            "redirect_uri": self.redirect_uri,
            "scope": selected_scope,
        }

    def complete_oauth_authorization(self, code: str, state: str) -> Dict[str, Any]:
        clean_code = code.strip()
        clean_state = state.strip()
        if not clean_code:
            raise ValueError("code must not be empty.")
        if not clean_state:
            raise ValueError("state must not be empty.")
        if not self._pending_oauth_state:
            raise ValueError("No pending OAuth authorization exists. Run begin_oauth_authorization first.")
        if clean_state != self._pending_oauth_state:
            raise ValueError("OAuth state mismatch. Start the authorization flow again.")
        token_data = self._exchange_authorization_code(clean_code)
        self._save_token_data(token_data)
        self._pending_oauth_state = None
        self.client = Zenpy(subdomain=self.subdomain, oauth_token=token_data["access_token"])
        self.auth_header = f"Bearer {token_data['access_token']}"
        return {
            "success": True,
            "message": f"Zendesk OAuth tokens saved to {self.oauth_token_path}. Existing MCP tools will now use Bearer auth.",
            "expires_in": int(token_data["expires_in"]),
            "scope": token_data.get("scope"),
        }

    def get_ticket(self, ticket_id: int) -> Dict[str, Any]:
        try:
            self._ensure_client()
            ticket = self.client.tickets(id=ticket_id)
            return {
                "id": ticket.id,
                "subject": ticket.subject,
                "description": ticket.description,
                "status": ticket.status,
                "priority": ticket.priority,
                "created_at": str(ticket.created_at),
                "updated_at": str(ticket.updated_at),
                "requester_id": ticket.requester_id,
                "assignee_id": ticket.assignee_id,
                "organization_id": ticket.organization_id,
            }
        except Exception as e:
            raise Exception(f"Failed to get ticket {ticket_id}: {str(e)}")

    def get_ticket_comments(self, ticket_id: int) -> List[Dict[str, Any]]:
        try:
            self._ensure_client()
            comments = self.client.tickets.comments(ticket=ticket_id)
            result = []
            for comment in comments:
                attachments = []
                for attachment in getattr(comment, "attachments", []) or []:
                    attachments.append(
                        {
                            "id": attachment.id,
                            "file_name": attachment.file_name,
                            "content_url": attachment.content_url,
                            "content_type": attachment.content_type,
                            "size": attachment.size,
                        }
                    )
                result.append(
                    {
                        "id": comment.id,
                        "author_id": comment.author_id,
                        "body": comment.body,
                        "html_body": comment.html_body,
                        "public": comment.public,
                        "created_at": str(comment.created_at),
                        "attachments": attachments,
                    }
                )
            return result
        except Exception as e:
            raise Exception(f"Failed to get comments for ticket {ticket_id}: {str(e)}")

    def get_ticket_attachment(self, content_url: str) -> Dict[str, Any]:
        try:
            response = self._request("GET", content_url, stream=True)
            content_type = response.headers.get("Content-Type", "").split(";")[0].strip().lower()

            if content_type not in self._ALLOWED_IMAGE_TYPES:
                raise ValueError(
                    f"Attachment type '{content_type}' is not allowed. "
                    f"Supported types: {sorted(self._ALLOWED_IMAGE_TYPES)}"
                )

            chunks = []
            total = 0
            for chunk in response.iter_content(chunk_size=65536):
                total += len(chunk)
                if total > self._MAX_ATTACHMENT_BYTES:
                    raise ValueError(
                        f"Attachment exceeds the {self._MAX_ATTACHMENT_BYTES // (1024 * 1024)} MB size limit."
                    )
                chunks.append(chunk)
            content = b"".join(chunks)

            magic_signatures = self._MAGIC_BYTES.get(content_type, [])
            if magic_signatures and not any(content.startswith(sig) for sig in magic_signatures):
                raise ValueError(
                    f"File header does not match declared content type '{content_type}'. "
                    "The attachment may be spoofed."
                )
            if content_type == "image/webp" and content[8:12] != b"WEBP":
                raise ValueError("File header does not match declared content type 'image/webp'.")

            return {
                "data": base64.b64encode(content).decode("ascii"),
                "content_type": content_type,
            }
        except (ValueError, _requests.HTTPError):
            raise
        except Exception as e:
            raise Exception(f"Failed to fetch attachment from {content_url}: {str(e)}")

    def post_comment(self, ticket_id: int, comment: str, public: bool = True) -> str:
        try:
            self._ensure_client()
            ticket = self.client.tickets(id=ticket_id)
            ticket.comment = Comment(html_body=comment, public=public)
            self.client.tickets.update(ticket)
            return comment
        except Exception as e:
            raise Exception(f"Failed to post comment on ticket {ticket_id}: {str(e)}")

    def get_tickets(
        self,
        page: int = 1,
        per_page: int = 25,
        sort_by: str = "created_at",
        sort_order: str = "desc",
    ) -> Dict[str, Any]:
        try:
            per_page = min(per_page, 100)
            params = {
                "page": str(page),
                "per_page": str(per_page),
                "sort_by": sort_by,
                "sort_order": sort_order,
            }
            query_string = urllib.parse.urlencode(params)
            url = f"{self.base_url}/tickets.json?{query_string}"
            response = self._request("GET", url, headers={"Content-Type": "application/json"})
            data = response.json()

            ticket_list = []
            for ticket in data.get("tickets", []):
                ticket_list.append(
                    {
                        "id": ticket.get("id"),
                        "subject": ticket.get("subject"),
                        "status": ticket.get("status"),
                        "priority": ticket.get("priority"),
                        "description": ticket.get("description"),
                        "created_at": ticket.get("created_at"),
                        "updated_at": ticket.get("updated_at"),
                        "requester_id": ticket.get("requester_id"),
                        "assignee_id": ticket.get("assignee_id"),
                    }
                )

            return {
                "tickets": ticket_list,
                "page": page,
                "per_page": per_page,
                "count": len(ticket_list),
                "sort_by": sort_by,
                "sort_order": sort_order,
                "has_more": data.get("next_page") is not None,
                "next_page": page + 1 if data.get("next_page") else None,
                "previous_page": page - 1 if data.get("previous_page") and page > 1 else None,
            }
        except Exception as e:
            raise Exception(f"Failed to get latest tickets: {str(e)}")

    def get_all_articles(self) -> Dict[str, Any]:
        try:
            self._ensure_client()
            sections = self.client.help_center.sections()
            kb = {}
            for section in sections:
                articles = self.client.help_center.sections.articles(section.id)
                kb[section.name] = {
                    "section_id": section.id,
                    "description": section.description,
                    "articles": [
                        {
                            "id": article.id,
                            "title": article.title,
                            "body": article.body,
                            "updated_at": str(article.updated_at),
                            "url": article.html_url,
                        }
                        for article in articles
                    ],
                }
            return kb
        except Exception as e:
            raise Exception(f"Failed to fetch knowledge base: {str(e)}")

    def create_ticket(
        self,
        subject: str,
        description: str,
        requester_id: int | None = None,
        assignee_id: int | None = None,
        priority: str | None = None,
        type: str | None = None,
        tags: List[str] | None = None,
        custom_fields: List[Dict[str, Any]] | None = None,
    ) -> Dict[str, Any]:
        try:
            self._ensure_client()
            ticket = ZenpyTicket(
                subject=subject,
                description=description,
                requester_id=requester_id,
                assignee_id=assignee_id,
                priority=priority,
                type=type,
                tags=tags,
                custom_fields=custom_fields,
            )
            created_audit = self.client.tickets.create(ticket)
            created_ticket_id = getattr(getattr(created_audit, "ticket", None), "id", None)
            if created_ticket_id is None:
                created_ticket_id = getattr(created_audit, "id", None)

            created = self.client.tickets(id=created_ticket_id) if created_ticket_id else None
            return {
                "id": getattr(created, "id", created_ticket_id),
                "subject": getattr(created, "subject", subject),
                "description": getattr(created, "description", description),
                "status": getattr(created, "status", "new"),
                "priority": getattr(created, "priority", priority),
                "type": getattr(created, "type", type),
                "created_at": str(getattr(created, "created_at", "")),
                "updated_at": str(getattr(created, "updated_at", "")),
                "requester_id": getattr(created, "requester_id", requester_id),
                "assignee_id": getattr(created, "assignee_id", assignee_id),
                "organization_id": getattr(created, "organization_id", None),
                "tags": list(getattr(created, "tags", tags or []) or []),
            }
        except Exception as e:
            raise Exception(f"Failed to create ticket: {str(e)}")

    def update_ticket(self, ticket_id: int, **fields: Any) -> Dict[str, Any]:
        try:
            self._ensure_client()
            ticket = self.client.tickets(id=ticket_id)
            for key, value in fields.items():
                if value is None:
                    continue
                setattr(ticket, key, value)

            self.client.tickets.update(ticket)
            refreshed = self.client.tickets(id=ticket_id)
            return {
                "id": refreshed.id,
                "subject": refreshed.subject,
                "description": refreshed.description,
                "status": refreshed.status,
                "priority": refreshed.priority,
                "type": getattr(refreshed, "type", None),
                "created_at": str(refreshed.created_at),
                "updated_at": str(refreshed.updated_at),
                "requester_id": refreshed.requester_id,
                "assignee_id": refreshed.assignee_id,
                "organization_id": refreshed.organization_id,
                "tags": list(getattr(refreshed, "tags", []) or []),
            }
        except Exception as e:
            raise Exception(f"Failed to update ticket {ticket_id}: {str(e)}")
