"""
List all Zendesk groups.
Reads credentials from .env in the same directory.
"""

import os
import requests
from dotenv import load_dotenv

# Load .env from the same directory as this script
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

SUBDOMAIN = os.getenv("ZENDESK_SUBDOMAIN")
EMAIL = os.getenv("ZENDESK_EMAIL")
API_KEY = os.getenv("ZENDESK_API_KEY")

url = f"https://{SUBDOMAIN}.zendesk.com/api/v2/groups.json"
auth = (f"{EMAIL}/token", API_KEY)

response = requests.get(url, auth=auth)
response.raise_for_status()

groups = response.json().get("groups", [])

print(f"{'ID':<15} {'Name'}")
print("-" * 50)
for g in groups:
    print(f"{g['id']:<15} {g['name']}")

print(f"\nTotal groups: {len(groups)}")
