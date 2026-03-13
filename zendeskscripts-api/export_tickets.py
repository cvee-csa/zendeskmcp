"""
Export all Zendesk tickets from the last 30 days to CSV.
Uses the incremental ticket export API (cursor-based) to handle large volumes
without hitting the search API's 1,000 result limit.
Saves to ../zendeskdata/tickets.csv
"""

import os
import csv
import time
from datetime import datetime, timedelta
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
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "tickets.csv")

# Last 30 days as Unix timestamp
since_time = int((datetime.utcnow() - timedelta(days=30)).timestamp())
since_date_str = (datetime.utcnow() - timedelta(days=30)).strftime("%Y-%m-%d")

FIELDS = [
    "id", "subject", "description", "status", "priority", "type",
    "created_at", "updated_at", "group_id", "assignee_id", "requester_id",
    "organization_id", "tags", "satisfaction_rating", "channel",
    "is_public", "allow_channelback"
]


def fetch_tickets():
    """
    Fetch all tickets using the cursor-based incremental export API.
    This endpoint has no 1,000 result cap and returns up to 1,000 per page.
    """
    tickets = []
    url = f"{BASE_URL}/incremental/tickets/cursor.json?start_time={since_time}"

    batch = 1
    while url:
        print(f"Fetching batch {batch}...")
        resp = requests.get(url, auth=AUTH)

        if resp.status_code == 429:
            retry_after = int(resp.headers.get("Retry-After", 60))
            print(f"  Rate limited. Waiting {retry_after}s...")
            time.sleep(retry_after)
            continue

        resp.raise_for_status()
        data = resp.json()

        batch_tickets = data.get("tickets", [])
        tickets.extend(batch_tickets)
        print(f"  Got {len(batch_tickets)} tickets (total so far: {len(tickets)})")

        # Check if there are more results
        if data.get("end_of_stream", False):
            break

        after_url = data.get("after_url")
        if after_url and after_url != url:
            url = after_url
        else:
            break

        batch += 1
        time.sleep(1)  # Be polite to the API

    return tickets


def write_csv(tickets):
    """Write tickets to CSV."""
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        for t in tickets:
            row = {field: t.get(field, "") for field in FIELDS}
            # Convert tags list to semicolon-separated string
            if isinstance(row["tags"], list):
                row["tags"] = "; ".join(row["tags"])
            # Flatten satisfaction rating
            if isinstance(row.get("satisfaction_rating"), dict):
                row["satisfaction_rating"] = row["satisfaction_rating"].get("score", "")
            writer.writerow(row)


if __name__ == "__main__":
    print(f"Exporting tickets created since {since_date_str}...")
    tickets = fetch_tickets()
    write_csv(tickets)
    print(f"\nDone! Exported {len(tickets)} tickets to {OUTPUT_FILE}")
