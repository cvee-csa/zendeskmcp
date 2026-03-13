"""
Export ticket comments for all tickets from the last 30 days.
Reads ticket IDs from ../zendeskdata/tickets.csv (run export_tickets.py first).
Saves to ../zendeskdata/comments.csv

Includes: ticket_id, comment_id, author_id, public, created_at, body (truncated).
Also computes a per-ticket summary saved to ../zendeskdata/ticket_metrics.csv
with first_response_time, total_comments, and resolution_time.

Supports resuming — if comments.csv already exists, it skips tickets already processed.
"""

import os
import csv
import time
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

SUBDOMAIN = os.getenv("ZENDESK_SUBDOMAIN")
EMAIL = os.getenv("ZENDESK_EMAIL")
API_KEY = os.getenv("ZENDESK_API_KEY")
AUTH = (f"{EMAIL}/token", API_KEY)
BASE_URL = f"https://{SUBDOMAIN}.zendesk.com/api/v2"

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "zendeskdata")
TICKETS_FILE = os.path.join(OUTPUT_DIR, "tickets.csv")
COMMENTS_FILE = os.path.join(OUTPUT_DIR, "comments.csv")
METRICS_FILE = os.path.join(OUTPUT_DIR, "ticket_metrics.csv")
ERRORS_FILE = os.path.join(OUTPUT_DIR, "skipped_tickets.csv")

COMMENT_FIELDS = ["ticket_id", "comment_id", "author_id", "public", "created_at", "body_preview"]
METRIC_FIELDS = ["ticket_id", "created_at", "status", "first_reply_at", "first_response_minutes",
                 "total_comments", "public_comments", "internal_comments", "last_comment_at"]

MAX_BODY_LENGTH = 500  # Truncate comment bodies to keep CSV manageable
MAX_RETRIES = 3


def load_ticket_ids():
    """Read ticket IDs and metadata from the tickets CSV."""
    tickets = []
    with open(TICKETS_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tickets.append({
                "id": row["id"],
                "created_at": row["created_at"],
                "status": row["status"],
                "requester_id": row["requester_id"],
            })
    return tickets


def load_already_processed():
    """Load ticket IDs that have already been exported to comments.csv."""
    processed = set()
    if os.path.exists(COMMENTS_FILE):
        with open(COMMENTS_FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                processed.add(row["ticket_id"])
    # Also check metrics file for tickets that had 0 comments
    if os.path.exists(METRICS_FILE):
        with open(METRICS_FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                processed.add(row["ticket_id"])
    return processed


def fetch_comments(ticket_id):
    """Fetch all comments for a single ticket with error handling."""
    url = f"{BASE_URL}/tickets/{ticket_id}/comments.json"
    comments = []
    retries = 0

    while url:
        try:
            resp = requests.get(url, auth=AUTH)

            if resp.status_code == 429:
                retry_after = int(resp.headers.get("Retry-After", 60))
                print(f"    Rate limited. Waiting {retry_after}s...")
                time.sleep(retry_after)
                continue

            if resp.status_code == 429:
                # Handled above, but just in case
                continue

            if resp.status_code >= 500:
                retries += 1
                if retries >= MAX_RETRIES:
                    return None, f"{resp.status_code} Server Error (after {MAX_RETRIES} retries)"
                print(f"    Server error {resp.status_code}, retrying ({retries}/{MAX_RETRIES})...")
                time.sleep(5)
                continue

            if resp.status_code != 200:
                # Catch-all for any client error (400, 403, 404, 422, etc.)
                return None, f"{resp.status_code} {resp.reason}"
            data = resp.json()
            comments.extend(data.get("comments", []))
            url = data.get("next_page")
            retries = 0  # Reset retries on success

        except requests.exceptions.ConnectionError as e:
            retries += 1
            if retries >= MAX_RETRIES:
                return None, f"Connection error (after {MAX_RETRIES} retries): {e}"
            print(f"    Connection error, retrying ({retries}/{MAX_RETRIES})...")
            time.sleep(5)

    return comments, None


def compute_metrics(ticket, comments):
    """Compute response time metrics for a ticket."""
    requester_id = ticket["requester_id"]
    ticket_created = ticket["created_at"]

    public_comments = [c for c in comments if c.get("public")]
    internal_comments = [c for c in comments if not c.get("public")]

    # First non-requester public comment = first reply
    first_reply = None
    for c in comments:
        if str(c.get("author_id")) != str(requester_id) and c.get("public"):
            first_reply = c
            break

    first_reply_at = first_reply["created_at"] if first_reply else ""
    first_response_minutes = ""
    if first_reply and ticket_created:
        try:
            created = datetime.fromisoformat(ticket_created.replace("Z", "+00:00"))
            replied = datetime.fromisoformat(first_reply_at.replace("Z", "+00:00"))
            first_response_minutes = round((replied - created).total_seconds() / 60, 1)
        except (ValueError, TypeError):
            pass

    last_comment_at = comments[-1]["created_at"] if comments else ""

    return {
        "ticket_id": ticket["id"],
        "created_at": ticket_created,
        "status": ticket["status"],
        "first_reply_at": first_reply_at,
        "first_response_minutes": first_response_minutes,
        "total_comments": len(comments),
        "public_comments": len(public_comments),
        "internal_comments": len(internal_comments),
        "last_comment_at": last_comment_at,
    }


if __name__ == "__main__":
    if not os.path.exists(TICKETS_FILE):
        print(f"Error: {TICKETS_FILE} not found. Run export_tickets.py first.")
        exit(1)

    tickets = load_ticket_ids()
    already_processed = load_already_processed()

    # Filter out already-processed tickets for resume support
    remaining = [t for t in tickets if t["id"] not in already_processed]

    if already_processed:
        print(f"Resuming: {len(already_processed)} tickets already processed, {len(remaining)} remaining.")
    else:
        print(f"Processing comments for {len(tickets)} tickets...")

    # Open files in append mode if resuming, write mode if fresh
    is_resume = len(already_processed) > 0
    comment_mode = "a" if is_resume else "w"
    metric_mode = "a" if is_resume else "w"

    comments_f = open(COMMENTS_FILE, comment_mode, newline="", encoding="utf-8")
    metrics_f = open(METRICS_FILE, metric_mode, newline="", encoding="utf-8")
    errors_f = open(ERRORS_FILE, "a" if is_resume else "w", newline="", encoding="utf-8")

    comment_writer = csv.DictWriter(comments_f, fieldnames=COMMENT_FIELDS)
    metric_writer = csv.DictWriter(metrics_f, fieldnames=METRIC_FIELDS)
    error_writer = csv.writer(errors_f)

    # Write headers only for fresh runs
    if not is_resume:
        comment_writer.writeheader()
        metric_writer.writeheader()
        error_writer.writerow(["ticket_id", "error"])

    skipped = 0
    processed = 0

    try:
        for i, ticket in enumerate(remaining):
            tid = ticket["id"]
            print(f"  [{len(already_processed) + i + 1}/{len(tickets)}] Ticket #{tid}...", end="")

            comments, error = fetch_comments(tid)

            if error:
                print(f" SKIPPED ({error})")
                error_writer.writerow([tid, error])
                errors_f.flush()
                skipped += 1
                continue

            print(f" {len(comments)} comments")

            for c in comments:
                body = c.get("body", "") or ""
                comment_writer.writerow({
                    "ticket_id": tid,
                    "comment_id": c.get("id"),
                    "author_id": c.get("author_id"),
                    "public": c.get("public"),
                    "created_at": c.get("created_at"),
                    "body_preview": body[:MAX_BODY_LENGTH].replace("\n", " "),
                })

            metrics = compute_metrics(ticket, comments)
            metric_writer.writerow(metrics)

            processed += 1

            # Flush every 50 tickets so progress is saved
            if processed % 50 == 0:
                comments_f.flush()
                metrics_f.flush()

            # Be polite to the API
            if (i + 1) % 10 == 0:
                time.sleep(1)

    except KeyboardInterrupt:
        print(f"\n\nInterrupted! Progress saved. Run again to resume.")
    finally:
        comments_f.close()
        metrics_f.close()
        errors_f.close()

    print(f"\nDone!")
    print(f"  Processed: {processed}")
    print(f"  Skipped:   {skipped} (see {ERRORS_FILE})")
    print(f"  Comments → {COMMENTS_FILE}")
    print(f"  Metrics  → {METRICS_FILE}")
