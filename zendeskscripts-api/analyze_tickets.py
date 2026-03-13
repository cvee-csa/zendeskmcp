"""
Zendesk Ticket Analysis — Comprehensive Insights
Reads CSVs from ../zendeskdata/ and outputs:
  - Console summary
  - ../zendeskdata/insights_report.md (full markdown report)
  - ../zendeskdata/insights_data.json (structured data for further use)

Dependencies: pip install pandas
"""

import os
import csv
import json
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------
DATA_DIR = Path(__file__).resolve().parent.parent / "zendeskdata"
TICKETS_FILE = DATA_DIR / "tickets.csv"
METRICS_FILE = DATA_DIR / "ticket_metrics.csv"
COMMENTS_FILE = DATA_DIR / "comments.csv"
GROUPS_FILE = DATA_DIR / "groups.csv"
AGENTS_FILE = DATA_DIR / "agents.csv"
TAGS_FILE = DATA_DIR / "tags.csv"

REPORT_FILE = DATA_DIR / "insights_report.md"
JSON_FILE = DATA_DIR / "insights_data.json"

NOW = datetime.utcnow()
STALE_THRESHOLD_DAYS = 7

# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def load_csv(path):
    """Load a CSV into a list of dicts."""
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def safe_int(val, default=0):
    try:
        return int(val)
    except (ValueError, TypeError):
        return default


def safe_float(val, default=None):
    try:
        return float(val)
    except (ValueError, TypeError):
        return default


def parse_dt(val):
    """Parse ISO datetime string."""
    if not val:
        return None
    try:
        return datetime.fromisoformat(val.replace("Z", "+00:00")).replace(tzinfo=None)
    except (ValueError, TypeError):
        return None


def pct(count, total):
    return round(count / total * 100, 1) if total else 0


def fmt_minutes(minutes):
    """Format minutes as human-readable duration."""
    if minutes is None:
        return "N/A"
    if minutes < 60:
        return f"{minutes:.0f}m"
    if minutes < 1440:
        return f"{minutes/60:.1f}h"
    return f"{minutes/1440:.1f}d"


# ---------------------------------------------------------------------------
# DATA LOADING
# ---------------------------------------------------------------------------

print("Loading data...")
tickets = load_csv(TICKETS_FILE)
metrics = load_csv(METRICS_FILE)
groups = load_csv(GROUPS_FILE)
agents = load_csv(AGENTS_FILE)
tags = load_csv(TAGS_FILE)

group_map = {row["id"]: row["name"] for row in groups}
agent_map = {row["id"]: row["name"] for row in agents}

# Enrich tickets
for t in tickets:
    t["_created"] = parse_dt(t.get("created_at", ""))
    t["_updated"] = parse_dt(t.get("updated_at", ""))
    t["_group_name"] = group_map.get(t.get("group_id", ""), "(unassigned)")
    t["_agent_name"] = agent_map.get(t.get("assignee_id", ""), "(unassigned)")
    t["_tags_list"] = [x.strip() for x in t.get("tags", "").split(";") if x.strip()]
    t["_days_since_update"] = (NOW - t["_updated"]).days if t["_updated"] else None

# Enrich metrics
for m in metrics:
    m["_first_response_min"] = safe_float(m.get("first_response_minutes"))
    m["_total_comments"] = safe_int(m.get("total_comments"))
    m["_public_comments"] = safe_int(m.get("public_comments"))
    m["_internal_comments"] = safe_int(m.get("internal_comments"))

metrics_by_id = {m["ticket_id"]: m for m in metrics}

print(f"Loaded {len(tickets)} tickets, {len(metrics)} metrics, {len(groups)} groups, {len(agents)} agents, {len(tags)} tags\n")


# ---------------------------------------------------------------------------
# ANALYSIS FUNCTIONS
# ---------------------------------------------------------------------------

insights = {}  # Collect all insights for JSON export


def section(title):
    print(f"\n{'='*65}")
    print(f"  {title}")
    print(f"{'='*65}")


# --- 1. VOLUME OVERVIEW ---
section("1. TICKET VOLUME OVERVIEW")

recent = [t for t in tickets if t["_created"] and t["_created"] >= NOW - timedelta(days=30)]
open_statuses = {"open", "new", "pending", "hold"}
open_tickets = [t for t in tickets if t.get("status") in open_statuses]
closed_tickets = [t for t in tickets if t.get("status") in {"closed", "solved"}]

status_dist = Counter(t.get("status", "(unknown)") for t in tickets)
priority_dist = Counter(t.get("priority") or "(not set)" for t in tickets)
type_dist = Counter(t.get("type") or "(not set)" for t in tickets)

# Daily volume
daily_counts = Counter()
for t in recent:
    if t["_created"]:
        daily_counts[t["_created"].strftime("%Y-%m-%d")] += 1

avg_daily = sum(daily_counts.values()) / max(len(daily_counts), 1)
busiest_day = max(daily_counts, key=daily_counts.get) if daily_counts else "N/A"
quietest_day = min(daily_counts, key=daily_counts.get) if daily_counts else "N/A"

# Day-of-week pattern
dow_counts = Counter()
for t in recent:
    if t["_created"]:
        dow_counts[t["_created"].strftime("%A")] += 1

dow_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
dow_sorted = [(d, dow_counts.get(d, 0)) for d in dow_order]

print(f"Total tickets in dataset:    {len(tickets)}")
print(f"Created in last 30 days:     {len(recent)}")
print(f"Currently open/pending/hold: {len(open_tickets)}")
print(f"Average daily volume:        {avg_daily:.1f}")
print(f"Busiest day:                 {busiest_day} ({daily_counts.get(busiest_day, 0)} tickets)")
print(f"\nStatus distribution:")
for s in ["new", "open", "pending", "hold", "solved", "closed", "deleted"]:
    c = status_dist.get(s, 0)
    print(f"  {s:<12} {c:>5}  ({pct(c, len(tickets))}%)")

print(f"\nDay-of-week pattern (last 30 days):")
for day, count in dow_sorted:
    bar = "█" * int(count / max(1, max(dow_counts.values())) * 30)
    print(f"  {day:<10} {count:>4}  {bar}")

print(f"\nPriority usage:  {pct(priority_dist.get('(not set)', 0), len(tickets))}% unset")
print(f"Type usage:      {pct(type_dist.get('(not set)', 0), len(tickets))}% unset")

insights["volume"] = {
    "total": len(tickets),
    "last_30_days": len(recent),
    "open": len(open_tickets),
    "avg_daily": round(avg_daily, 1),
    "busiest_day": busiest_day,
    "status_distribution": dict(status_dist),
    "day_of_week": dict(dow_sorted),
    "priority_unset_pct": pct(priority_dist.get("(not set)", 0), len(tickets)),
    "type_unset_pct": pct(type_dist.get("(not set)", 0), len(tickets)),
}


# --- 2. RESPONSE TIME ANALYSIS ---
section("2. RESPONSE TIME ANALYSIS")

responded = [m for m in metrics if m["_first_response_min"] is not None]
not_responded = [m for m in metrics if m["_first_response_min"] is None]

resp_times = sorted([m["_first_response_min"] for m in responded])

def percentile(sorted_list, p):
    if not sorted_list:
        return None
    k = (len(sorted_list) - 1) * (p / 100)
    f = int(k)
    c = f + 1 if f + 1 < len(sorted_list) else f
    return sorted_list[f] + (k - f) * (sorted_list[c] - sorted_list[f])

median_resp = percentile(resp_times, 50)
p25_resp = percentile(resp_times, 25)
p75_resp = percentile(resp_times, 75)
p90_resp = percentile(resp_times, 90)
p95_resp = percentile(resp_times, 95)
mean_resp = sum(resp_times) / len(resp_times) if resp_times else 0

# Response time buckets
buckets = [
    ("< 1 hour", 0, 60),
    ("1–4 hours", 60, 240),
    ("4–8 hours", 240, 480),
    ("8–24 hours", 480, 1440),
    ("1–3 days", 1440, 4320),
    ("> 3 days", 4320, float("inf")),
]
bucket_counts = []
for label, lo, hi in buckets:
    c = sum(1 for r in resp_times if lo <= r < hi)
    bucket_counts.append((label, c))

print(f"Tickets with a reply:    {len(responded)} ({pct(len(responded), len(metrics))}%)")
print(f"Tickets with NO reply:   {len(not_responded)} ({pct(len(not_responded), len(metrics))}%)")
print(f"\nFirst response time:")
print(f"  Median:  {fmt_minutes(median_resp)}")
print(f"  Mean:    {fmt_minutes(mean_resp)}")
print(f"  P25:     {fmt_minutes(p25_resp)}")
print(f"  P75:     {fmt_minutes(p75_resp)}")
print(f"  P90:     {fmt_minutes(p90_resp)}")
print(f"  P95:     {fmt_minutes(p95_resp)}")
print(f"\nResponse time distribution:")
for label, c in bucket_counts:
    bar = "█" * int(c / max(1, max(x[1] for x in bucket_counts)) * 30)
    print(f"  {label:<14} {c:>5}  ({pct(c, len(responded))}%)  {bar}")

insights["response_times"] = {
    "responded_pct": pct(len(responded), len(metrics)),
    "no_reply_count": len(not_responded),
    "median_minutes": round(median_resp, 1) if median_resp else None,
    "mean_minutes": round(mean_resp, 1),
    "p90_minutes": round(p90_resp, 1) if p90_resp else None,
    "p95_minutes": round(p95_resp, 1) if p95_resp else None,
    "buckets": {label: c for label, c in bucket_counts},
}


# --- 3. CONVERSATION DEPTH ---
section("3. CONVERSATION DEPTH")

comment_counts = [m["_total_comments"] for m in metrics]
avg_comments = sum(comment_counts) / len(comment_counts) if comment_counts else 0
one_touch = sum(1 for c in comment_counts if c <= 2)
high_touch = [(m["ticket_id"], m["_total_comments"]) for m in metrics if m["_total_comments"] >= 10]
high_touch.sort(key=lambda x: x[1], reverse=True)

internal_only = [m for m in metrics if m["_public_comments"] <= 1 and m["_internal_comments"] >= 1]

print(f"Average comments/ticket:   {avg_comments:.1f}")
print(f"One-touch tickets (≤2):    {one_touch} ({pct(one_touch, len(metrics))}%)")
print(f"High-touch tickets (≥10):  {len(high_touch)} ({pct(len(high_touch), len(metrics))}%)")
print(f"Mostly internal notes:     {len(internal_only)} ({pct(len(internal_only), len(metrics))}%)")
if high_touch:
    print(f"\nMost commented tickets:")
    for tid, cc in high_touch[:10]:
        t = next((x for x in tickets if str(x["id"]) == str(tid)), None)
        subj = t.get("subject", "")[:45] if t else ""
        print(f"  #{tid:<8} {cc:>3} comments  {subj}")

insights["conversation_depth"] = {
    "avg_comments": round(avg_comments, 1),
    "one_touch_pct": pct(one_touch, len(metrics)),
    "high_touch_count": len(high_touch),
    "high_touch_top5": [(tid, cc) for tid, cc in high_touch[:5]],
}


# --- 4. GROUP WORKLOAD ---
section("4. GROUP WORKLOAD")

group_all = Counter(t["_group_name"] for t in tickets)
group_open = Counter(t["_group_name"] for t in open_tickets)
group_stale = Counter(t["_group_name"] for t in tickets
                      if t.get("status") in open_statuses
                      and t.get("_days_since_update") is not None
                      and t["_days_since_update"] >= STALE_THRESHOLD_DAYS)

print(f"{'Group':<45} {'Total':>6} {'Open':>6} {'Stale':>6}")
print("-" * 70)
for g, total in group_all.most_common(20):
    o = group_open.get(g, 0)
    s = group_stale.get(g, 0)
    flag = " ⚠" if s >= 10 else ""
    print(f"  {g:<43} {total:>6} {o:>6} {s:>6}{flag}")

insights["group_workload"] = {
    g: {"total": c, "open": group_open.get(g, 0), "stale": group_stale.get(g, 0)}
    for g, c in group_all.most_common(20)
}


# --- 5. AGENT WORKLOAD ---
section("5. AGENT WORKLOAD")

agent_all = Counter(t["_agent_name"] for t in tickets)
agent_open = Counter(t["_agent_name"] for t in open_tickets)

# Calculate avg response time per agent
agent_resp_times = {}
for m in responded:
    tid = m["ticket_id"]
    t = next((x for x in tickets if str(x["id"]) == str(tid)), None)
    if t:
        agent = t["_agent_name"]
        agent_resp_times.setdefault(agent, []).append(m["_first_response_min"])

print(f"{'Agent':<35} {'Total':>6} {'Open':>6} {'Avg Resp':>10}")
print("-" * 65)
for a, total in agent_all.most_common(15):
    o = agent_open.get(a, 0)
    resp_list = agent_resp_times.get(a, [])
    avg_r = fmt_minutes(sum(resp_list) / len(resp_list)) if resp_list else "N/A"
    flag = " ⚠" if o >= 50 else ""
    print(f"  {a:<33} {total:>6} {o:>6} {avg_r:>10}{flag}")

insights["agent_workload"] = {
    a: {
        "total": c,
        "open": agent_open.get(a, 0),
        "avg_response_min": round(sum(agent_resp_times.get(a, [0])) / max(len(agent_resp_times.get(a, [1])), 1), 1)
    }
    for a, c in agent_all.most_common(15)
}


# --- 6. TAG PATTERNS ---
section("6. TAG PATTERNS & CATEGORIZATION")

# Workflow tags (indicate process/automation)
workflow_tags = ["skip_css", "do_close", "do_closed", "pending_followup_1",
                 "pending_followup_solve", "disconnect"]
# Content tags (indicate topic)
content_tags = ["training", "membership", "sales", "accounting", "taise",
                "star", "ccsk", "self_assessment", "bundle"]
# Issue tags
issue_tags = ["edge_case", "non-actionable", "info-in", "internal-requests",
              "level1", "level2", "instructions"]

tag_data = {row["tag"]: safe_int(row["count"]) for row in tags}

print("Workflow/automation tags:")
for t in workflow_tags:
    c = tag_data.get(t, 0)
    if c:
        print(f"  {t:<30} {c:>5}  ({pct(c, len(tickets))}%)")

print(f"\nContent/topic tags:")
for t in content_tags:
    c = tag_data.get(t, 0)
    if c:
        print(f"  {t:<30} {c:>5}  ({pct(c, len(tickets))}%)")

print(f"\nIssue-type tags:")
for t in issue_tags:
    c = tag_data.get(t, 0)
    if c:
        print(f"  {t:<30} {c:>5}  ({pct(c, len(tickets))}%)")

# Non-actionable volume
non_actionable = sum(1 for t in tickets if "non-actionable" in t["_tags_list"]
                     or "do_close" in t["_tags_list"] or "edge_case" in t["_tags_list"])
print(f"\nNon-actionable ticket volume: {non_actionable} ({pct(non_actionable, len(tickets))}%)")

insights["tags"] = {
    "total_unique": len(tags),
    "non_actionable_pct": pct(non_actionable, len(tickets)),
    "top_content_tags": [(t, tag_data.get(t, 0)) for t in content_tags if tag_data.get(t, 0)],
}


# --- 7. STALE & UNRESPONDED TICKETS ---
section("7. STALE & UNRESPONDED TICKETS")

stale_tickets = [t for t in open_tickets
                 if t.get("_days_since_update") is not None
                 and t["_days_since_update"] >= STALE_THRESHOLD_DAYS]
stale_tickets.sort(key=lambda x: x["_days_since_update"], reverse=True)

# Unresponded = open + no first reply
unresponded = []
for t in open_tickets:
    m = metrics_by_id.get(str(t["id"]))
    if m and (m["_first_response_min"] is None):
        unresponded.append(t)

print(f"Stale tickets (open, no update in {STALE_THRESHOLD_DAYS}+ days): {len(stale_tickets)}")
print(f"Unresponded tickets (open, no reply at all):     {len(unresponded)}")

# Age distribution of stale tickets
age_buckets_stale = [
    ("7-14 days", 7, 14),
    ("14-21 days", 14, 21),
    ("21-30 days", 21, 30),
    ("30-90 days", 30, 90),
    ("90+ days", 90, 9999),
]
print(f"\nStale ticket age distribution:")
for label, lo, hi in age_buckets_stale:
    c = sum(1 for t in stale_tickets if lo <= (t["_days_since_update"] or 0) < hi)
    if c:
        print(f"  {label:<14} {c:>5}")

print(f"\nStale by group (top 10):")
stale_by_group = Counter(t["_group_name"] for t in stale_tickets)
for g, c in stale_by_group.most_common(10):
    print(f"  {g:<40} {c:>5}")

print(f"\nUnresponded by group (top 10):")
unresponded_by_group = Counter(t["_group_name"] for t in unresponded)
for g, c in unresponded_by_group.most_common(10):
    print(f"  {g:<40} {c:>5}")

insights["stale"] = {
    "stale_count": len(stale_tickets),
    "unresponded_count": len(unresponded),
    "stale_by_group": dict(stale_by_group.most_common(10)),
    "unresponded_by_group": dict(unresponded_by_group.most_common(10)),
}


# --- 8. AUTOMATION OPPORTUNITIES ---
section("8. AUTOMATION & EFFICIENCY OPPORTUNITIES")

# Tickets that were auto-closed (have do_close + closed status)
auto_closeable = sum(1 for t in tickets if "do_close" in t["_tags_list"] or "do_closed" in t["_tags_list"])
already_closed_auto = sum(1 for t in tickets
                          if ("do_close" in t["_tags_list"] or "do_closed" in t["_tags_list"])
                          and t.get("status") in {"closed", "solved"})

# Purchase notifications (likely informational)
purchase_notif = sum(1 for t in tickets if "purchase_notification" in t["_tags_list"])

# Tickets with skip_css tag
skip_css = sum(1 for t in tickets if "skip_css" in t["_tags_list"])

# Chapter messages (formulaic pattern)
chapter_msgs = sum(1 for t in tickets if t.get("subject", "").startswith("Message for"))

print(f"Auto-close tagged (do_close/do_closed):  {auto_closeable} ({pct(auto_closeable, len(tickets))}%)")
print(f"  Already resolved:                      {already_closed_auto}")
print(f"  Still open:                            {auto_closeable - already_closed_auto}")
print(f"\nPurchase notifications:                  {purchase_notif} ({pct(purchase_notif, len(tickets))}%)")
print(f"Skip CSS tagged:                         {skip_css} ({pct(skip_css, len(tickets))}%)")
print(f"Chapter messages ('Message for ...'):     {chapter_msgs}")
print(f"\nEstimated automatable volume:             ~{auto_closeable + purchase_notif} tickets/month")
print(f"  ({pct(auto_closeable + purchase_notif, len(recent))}% of monthly volume)")

insights["automation"] = {
    "auto_closeable": auto_closeable,
    "purchase_notifications": purchase_notif,
    "chapter_messages": chapter_msgs,
    "estimated_automatable": auto_closeable + purchase_notif,
    "automatable_pct_monthly": pct(auto_closeable + purchase_notif, len(recent)),
}


# --- 9. KEY FINDINGS & ACTION ITEMS ---
section("9. KEY FINDINGS & RECOMMENDED ACTIONS")

findings = []

if pct(priority_dist.get("(not set)", 0), len(tickets)) > 90:
    findings.append({
        "severity": "HIGH",
        "finding": f"{pct(priority_dist.get('(not set)', 0), len(tickets))}% of tickets have no priority set",
        "action": "Add required priority field or auto-classification triggers to improve triage",
    })

if len(unresponded) > 50:
    findings.append({
        "severity": "HIGH",
        "finding": f"{len(unresponded)} open tickets have never received a reply",
        "action": "Bulk-review unresponded tickets; set up alerts for tickets approaching SLA thresholds",
    })

if len(stale_tickets) > 100:
    findings.append({
        "severity": "HIGH",
        "finding": f"{len(stale_tickets)} tickets are stale (no activity in {STALE_THRESHOLD_DAYS}+ days)",
        "action": "Run a stale-ticket sweep; consider auto-solve after 14 days of inactivity on pending tickets",
    })

top_stale_group = stale_by_group.most_common(1)[0] if stale_by_group else None
if top_stale_group and top_stale_group[1] > 30:
    findings.append({
        "severity": "HIGH",
        "finding": f"{top_stale_group[0]} has {top_stale_group[1]} stale tickets — largest backlog",
        "action": f"Dedicate a triage session for {top_stale_group[0]} to clear the backlog",
    })

overloaded_agents = [(a, c) for a, c in agent_open.most_common(5) if c >= 50]
for a, c in overloaded_agents:
    findings.append({
        "severity": "MEDIUM",
        "finding": f"{a} has {c} open tickets — significantly above average",
        "action": f"Review {a}'s queue for tickets that can be reassigned or bulk-resolved",
    })

if insights["automation"]["automatable_pct_monthly"] > 20:
    findings.append({
        "severity": "MEDIUM",
        "finding": f"~{insights['automation']['estimated_automatable']} tickets/month ({insights['automation']['automatable_pct_monthly']}%) are potentially automatable",
        "action": "Implement auto-close triggers for do_close tagged tickets and purchase notifications",
    })

if pct(non_actionable, len(tickets)) > 15:
    findings.append({
        "severity": "MEDIUM",
        "finding": f"{pct(non_actionable, len(tickets))}% of tickets are non-actionable",
        "action": "Review intake channels to reduce non-actionable volume (spam filters, form validation)",
    })

if median_resp and median_resp > 120:
    findings.append({
        "severity": "LOW",
        "finding": f"Median first response time is {fmt_minutes(median_resp)}",
        "action": "Set up auto-responders for common ticket types to reduce perceived wait time",
    })

for f in findings:
    sev_icon = {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🟢"}.get(f["severity"], "⚪")
    print(f"\n{sev_icon} [{f['severity']}] {f['finding']}")
    print(f"   → {f['action']}")

insights["findings"] = findings


# ---------------------------------------------------------------------------
# SAVE OUTPUTS
# ---------------------------------------------------------------------------

# JSON
with open(JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(insights, f, indent=2, default=str)
print(f"\n\nStructured data saved to: {JSON_FILE}")

# Markdown report
with open(REPORT_FILE, "w", encoding="utf-8") as f:
    f.write("# Zendesk Ticket Analysis — Insights Report\n\n")
    f.write(f"**Generated:** {NOW.strftime('%Y-%m-%d %H:%M UTC')}  \n")
    f.write(f"**Data range:** Last 30 days ({len(recent)} tickets created, {len(tickets)} total in dataset)\n\n")

    f.write("---\n\n## Executive Summary\n\n")
    f.write(f"The support team processed **{avg_daily:.0f} tickets/day** over the last 30 days. ")
    f.write(f"Resolution rate is healthy at **{pct(len(closed_tickets), len(tickets))}%**, ")
    f.write(f"but **{len(open_tickets)} tickets remain open**, with **{len(stale_tickets)} stale** ")
    f.write(f"and **{len(unresponded)} unresponded**. ")
    f.write(f"Median first response time is **{fmt_minutes(median_resp)}**, though the P90 is **{fmt_minutes(p90_resp)}**. ")
    f.write(f"An estimated **{insights['automation']['automatable_pct_monthly']}%** of monthly volume is potentially automatable.\n\n")

    f.write("---\n\n## Key Findings & Action Items\n\n")
    for fi in findings:
        sev = fi["severity"]
        f.write(f"- **[{sev}]** {fi['finding']}  \n  *Action:* {fi['action']}\n\n")

    f.write("---\n\n## Volume Overview\n\n")
    f.write(f"| Metric | Value |\n|---|---|\n")
    f.write(f"| Total tickets (dataset) | {len(tickets)} |\n")
    f.write(f"| Created last 30 days | {len(recent)} |\n")
    f.write(f"| Avg daily volume | {avg_daily:.1f} |\n")
    f.write(f"| Currently open | {len(open_tickets)} |\n")
    f.write(f"| Priority not set | {pct(priority_dist.get('(not set)', 0), len(tickets))}% |\n")
    f.write(f"| Type not set | {pct(type_dist.get('(not set)', 0), len(tickets))}% |\n\n")

    f.write("### Status Distribution\n\n")
    f.write("| Status | Count | % |\n|---|---|---|\n")
    for s in ["new", "open", "pending", "hold", "solved", "closed"]:
        c = status_dist.get(s, 0)
        f.write(f"| {s} | {c} | {pct(c, len(tickets))}% |\n")

    f.write("\n---\n\n## Response Times\n\n")
    f.write(f"| Metric | Value |\n|---|---|\n")
    f.write(f"| Tickets with reply | {len(responded)} ({pct(len(responded), len(metrics))}%) |\n")
    f.write(f"| Median response | {fmt_minutes(median_resp)} |\n")
    f.write(f"| P75 response | {fmt_minutes(p75_resp)} |\n")
    f.write(f"| P90 response | {fmt_minutes(p90_resp)} |\n")
    f.write(f"| P95 response | {fmt_minutes(p95_resp)} |\n\n")

    f.write("### Response Time Buckets\n\n")
    f.write("| Bucket | Count | % |\n|---|---|---|\n")
    for label, c in bucket_counts:
        f.write(f"| {label} | {c} | {pct(c, len(responded))}% |\n")

    f.write("\n---\n\n## Group Workload\n\n")
    f.write("| Group | Total | Open | Stale |\n|---|---|---|---|\n")
    for g, total in group_all.most_common(15):
        f.write(f"| {g} | {total} | {group_open.get(g, 0)} | {group_stale.get(g, 0)} |\n")

    f.write("\n---\n\n## Agent Workload (Top 15)\n\n")
    f.write("| Agent | Total | Open |\n|---|---|---|\n")
    for a, total in agent_all.most_common(15):
        f.write(f"| {a} | {total} | {agent_open.get(a, 0)} |\n")

    f.write("\n---\n\n## Automation Opportunities\n\n")
    f.write(f"| Category | Count | % of Monthly |\n|---|---|---|\n")
    f.write(f"| Auto-close tagged | {auto_closeable} | {pct(auto_closeable, len(recent))}% |\n")
    f.write(f"| Purchase notifications | {purchase_notif} | {pct(purchase_notif, len(recent))}% |\n")
    f.write(f"| Chapter messages | {chapter_msgs} | {pct(chapter_msgs, len(recent))}% |\n")
    f.write(f"| Non-actionable | {non_actionable} | {pct(non_actionable, len(recent))}% |\n")
    f.write(f"| **Estimated automatable** | **~{auto_closeable + purchase_notif}** | **{insights['automation']['automatable_pct_monthly']}%** |\n")

    f.write("\n---\n\n*Report generated by analyze_tickets.py*\n")

print(f"Markdown report saved to: {REPORT_FILE}")
