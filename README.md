# Cloud Security Alliance

## Claude-Zendesk MCP Integration

**Start:** 03/13/2026

---

This Zendesk-Claude integration includes files from the [zendesk-mcp-server](https://github.com/reminia/zendesk-mcp-server) repository, including the MCP server and `zendesk_client` Python files.

---

## Python Pre-requisites

0. Set your user name and email address for Git to use when interacting with Github. This is important because every Git commit uses this information, and it's immutably baked into the commits you start creating:

   ```bash
   git config --global user.name "Catherine Vee"
   git config --global user.email catherineiscool@csa.com
   ```

1. Install the following:

   **Runtime & Package Managers:**

   - [Python 3.10+](https://www.python.org/downloads/)
   - [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer — included with most Python installations)
   - [uv](https://github.com/astral-sh/uv) (fast Python package manager, used by the MCP server)

   **Python Packages:**

   ```bash
   pip install python-dotenv requests
   ```

   | Package | Purpose |
   |---|---|
   | `python-dotenv` | Loads Zendesk API credentials from the `.env` file |
   | `requests` | Makes HTTP requests to the Zendesk REST API |

2. Run the export scripts in order:

   ```bash
   # Step A: Run these first (no dependencies)
   python3 export_tickets.py
   python3 list_groups.py
   python3 list_agents.py

   # Step B: These depend on tickets.csv existing
   python3 export_comments.py
   python3 export_tags.py
   ```

---

## Zendesk API Pre-requisites

0. Configure the MCP server by modifying `claude/claude_desktop_config.json`:

   ```json
   {
     "mcpServers": {
       "zendesk": {
         "command": "/path/to/uv",
         "args": ["--directory", "/path/to/zendesk-mcp-server", "run", "..."]
       }
     }
   }
   ```

   | Parameter | What to set |
   |---|---|
   | `"command"` | Full path to your `uv` executable (e.g., `/Users/yourname/.local/bin/uv`) |
   | `"--directory"` | Path to the `zendesk-mcp-server` directory on your machine |

   An example config file is provided in `zendeskmcp/claude/claude_desktop_config.json`.

1. Configure Zendesk API authentication by copying `.env.example` to `.env` and filling in all three values:

   ```bash
   cp .env.example .env
   ```

   | Variable | Value | Where to find it |
   |---|---|---|
   | `ZENDESK_SUBDOMAIN` | Your Zendesk subdomain (e.g., `cloudsecurityalliance`) | The part before `.zendesk.com` in your Zendesk URL |
   | `ZENDESK_EMAIL` | Agent email address (e.g., `you@yourorg.org`) | The email you use to log into Zendesk |
   | `ZENDESK_API_KEY` | Your Zendesk API token | Zendesk Admin → Apps and Integrations → Zendesk API → API token |
