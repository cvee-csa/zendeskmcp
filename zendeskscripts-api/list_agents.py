"""
Export all Zendesk agents and admins to CSV.
Saves to ../zendeskdata/agents.csv
"""

import os
import csv
import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

SUBDOMAIN = os.getenv("ZENDESK_SUBDOMAIN")
EMAIL = os.getenv("ZENDESK_EMAIL")
API_KEY = os.getenv("ZENDESK_API_KEY")
AUTH = (f"{EMAIL}/token", API_KEY)
BASE_URL = f"https://{SUBDOMAIN}.zendesk.com/api/v2"

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "zendeskdata")
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "agents.csv")

FIELDS = ["id", "name", "email", "role", "default_group_id", "active", "created_at"]


def fetch_agents():
    """Fetch all agents and admins with pagination."""
    agents = []
    url = f"{BASE_URL}/users.json?role[]=agent&role[]=admin"

    while url:
        print(f"Fetching agents...")
        resp = requests.get(url, auth=AUTH)
        resp.raise_for_status()
        data = resp.json()
        agents.extend(data.get("users", []))
        url = data.get("next_page")

    return agents


def write_csv(agents):
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        for a in agents:
            row = {field: a.get(field, "") for field in FIELDS}
            writer.writerow(row)


if __name__ == "__main__":
    print("Exporting agents and admins...")
    agents = fetch_agents()
    write_csv(agents)
    print(f"\nDone! Exported {len(agents)} agents to {OUTPUT_FILE}")
