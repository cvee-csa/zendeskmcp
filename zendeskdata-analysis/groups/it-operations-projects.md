# IT-Operations-Projects

*Part of the [CSA Zendesk Group-by-Group Analysis](00_summary.md)*

---

**Severity: HIGH** | 28 tickets | 24 open (85.7%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | 6.5h | 3.2x |
| Resolution (median) | 44.1d | 2.2x |
| Zero-Reply Rate | 14.3% | Above org (3.3%) |
| Avg Comments/Ticket | 8.1 | — |
| Multi-Touch Rate | 89.3% | — |
| Automation Eligible | 2 (7.1%) | — |
| Unassigned | 9 | — |
| Stale (>7d no activity) | 9 | — |

### Status Breakdown

- **open**: 16 (57.1%)
- **hold**: 8 (28.6%)
- **solved**: 3 (10.7%)
- **closed**: 1 (3.6%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Nekoashi Wolf | 11 | 10 (90.9%) | 6.7 | 3 (27.3%) |
| Jacob Wicklund | 4 | 1 (25.0%) | 4.2 | 1 (25.0%) |
| Ryan Bergsma | 4 | 4 (100.0%) | 11.3 | 0 (0.0%) |

**Agent comment volume** (from comments.csv): 
Jacob Wicklund: 53, Kurt S: 49, Ryan Bergsma: 29, Nekoashi Wolf: 26, Kaitlin Morgan: 21, Joshua Buker: 11, Madison Hopkins: 6, Addison Young: 6, Hannah Rock: 4, Courtney Stiven: 4

### Top Tags

`skip_css` (25), `it` (22), `internal-requests` (18), `closed_by_merge` (1), `system_email_notification_failure` (1), `do_close` (1), `do_closed` (1), `edge_case` (1), `redacted_content` (1), `followup_today` (1)

### Top Subject Keywords

*cloudsecurityalliance* (6), *github* (4), *project* (3), *ops* (3), *csa* (3), *org* (3), *create* (3), *data* (2), *review* (2), *calendar* (2)

### Identified Patterns

- **Severe backlog**: 24 tickets remain open (85.7%), far above the org average. The queue is accumulating faster than it's being cleared.
- **Stale tickets**: 9 tickets have had no activity in over 7 days (0 over 30 days).
- **Slow response**: Median first response of 6.5h, which is 3.2x the org-wide median of 2.0h.
- **Weekend gap**: Weekend response is 27.7h vs. weekday 4.2h — a 6.6x penalty.
- **Above-average resolution time**: 44.1 days vs. org median of 20.0d.
- **High zero-reply rate**: 14.3% of tickets have no public response (4 tickets). Requesters are being ignored.
- **Agent bottleneck — Nekoashi Wolf**: 10 open out of 11 assigned (90.9% open rate).
- **High-touch queue**: 89.3% of tickets require more than 2 comments to resolve, indicating complex or multi-step issues.
- **Unassigned tickets**: 9 tickets have no agent assigned.

### Proposed Solutions

1. **Immediate triage**: Schedule a dedicated session to review all 24 open tickets. Close stale/resolved tickets, re-assign active ones, and escalate blocked tickets. Target: reduce open rate to under 25% within 2 weeks.
2. **Mandatory reply before close**: Add a Zendesk requirement that at least one public comment must exist before a ticket can be marked solved. This ensures every requester gets a response.
3. **Weekend coverage**: Include IT-Operations-Projects in weekend on-call rotation, or deploy the weekend auto-acknowledgment template to set expectations for Saturday/Sunday submissions.
4. **Process review**: Resolution time of 44.1d indicates process bottlenecks (approvals, external dependencies, unclear ownership). Map the end-to-end workflow, identify where tickets stall, and set internal checkpoints at 7-day and 14-day marks.
5. **Fix routing**: 9 tickets have no agent. Create a catch-all assignment rule: any ticket unassigned after 30 minutes auto-assigns to the group's on-duty agent.
6. **Redistribute Nekoashi Wolf's queue**: 10 open tickets cannot be cleared by one person. Redistribute across available agents in the group or pull in cross-trained agents from adjacent teams.
7. **Create macros for common topics**: The top tags (membership) indicate recurring question types. Build Zendesk macros with pre-written responses for these topics to reduce handling time.
8. **Improve first-contact resolution**: 89.3% of tickets need 3+ comments. Review the most common multi-touch tickets and update macros or help center articles to provide complete answers upfront.
