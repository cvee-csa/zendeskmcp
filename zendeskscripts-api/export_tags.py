"""
Export tag frequency counts from the tickets CSV.
Reads from ../zendeskdata/tickets.csv (run export_tickets.py first).
Saves to ../zendeskdata/tags.csv
"""

import os
import csv
from collections import Counter
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "zendeskdata")
TICKETS_FILE = os.path.join(OUTPUT_DIR, "tickets.csv")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "tags.csv")


if __name__ == "__main__":
    if not os.path.exists(TICKETS_FILE):
        print(f"Error: {TICKETS_FILE} not found. Run export_tickets.py first.")
        exit(1)

    tag_counter = Counter()
    ticket_count = 0

    with open(TICKETS_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ticket_count += 1
            tags_str = row.get("tags", "")
            if tags_str:
                tags = [t.strip() for t in tags_str.split(";") if t.strip()]
                tag_counter.update(tags)

    # Write sorted by frequency
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["tag", "count", "pct_of_tickets"])
        for tag, count in tag_counter.most_common():
            pct = round(count / ticket_count * 100, 1) if ticket_count else 0
            writer.writerow([tag, count, pct])

    print(f"Analyzed {ticket_count} tickets")
    print(f"Found {len(tag_counter)} unique tags")
    print(f"\nTop 20 tags:")
    for tag, count in tag_counter.most_common(20):
        pct = round(count / ticket_count * 100, 1)
        print(f"  {tag:<40} {count:>5}  ({pct}%)")
    print(f"\nSaved to {OUTPUT_FILE}")
