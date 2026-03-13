"""
List all Zendesk groups.
Reads credentials from .env in the same directory.
Saves to ../zendeskdata/groups.csv
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

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "zendeskdata")
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "groups.csv")

FIELDS = ["id", "name", "description", "created_at", "updated_at"]


def fetch_groups():
    url = f"https://{SUBDOMAIN}.zendesk.com/api/v2/groups.json"
    groups = []
    while url:
        resp = requests.get(url, auth=AUTH)
        resp.raise_for_status()
        data = resp.json()
        groups.extend(data.get("groups", []))
        url = data.get("next_page")
    return groups


if __name__ == "__main__":
    groups = fetch_groups()

    # Print to console
    print(f"{'ID':<15} {'Name'}")
    print("-" * 50)
    for g in groups:
        print(f"{g['id']:<15} {g['name']}")

    # Save to CSV
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        for g in groups:
            writer.writerow({field: g.get(field, "") for field in FIELDS})

    print(f"\nTotal groups: {len(groups)}")
    print(f"Saved to {OUTPUT_FILE}")
