CSA

 =============================
This Zendesk-Claude integration includes files from the zendesk-mcp-server (https://github.com/reminia/zendesk-mcp-server) repository, including the MCP server and zendesk_client Python files.

Python Pre-requisites:
 0. Set your user name and email address for Git to use when interacting with Github. This is important because every Git commit uses this information, and it’s immutably baked into the commits you start creating:

$ git config --global user.name "Catherine Vee"
$ git config --global user.email catherineiscool@csa.com

1. Install: Python, Python Installation Packager (PIP), uv

Zendesk API Pre-requisites:
0. Modify the parameters in the claude_desktop_config.json JSON file to use the Zendesk MCP Server (example file in zendeskmcp/claude) and run the "uv" Python package manager command. Make sure the "command" JSON parameter is pointed to the path for the correct executable or bin file and the "--directory" parameter is configured to where the zendesk-mcp-server directory is.

1. Modify all three values in .env.example, this will handle the authentication piece for the Zendesk API

