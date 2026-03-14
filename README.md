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

0. Modify the parameters in the `claude_desktop_config.json` JSON file to use the Zendesk MCP Server (example file in `zendeskmcp/claude`) and run the `uv` Python package manager command. Make sure the `"command"` JSON parameter is pointed to the path for the correct executable or bin file and the `"--directory"` parameter is configured to where the `zendesk-mcp-server` directory is.

1. Modify all three values in `.env.example`, this will handle the authentication piece for the Zendesk API.
