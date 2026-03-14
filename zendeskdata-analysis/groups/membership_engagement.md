# Membership Engagement

*Part of the [CSA Zendesk Group-by-Group Analysis](00_summary.md)*

---

**Severity: MEDIUM** | 72 tickets | 15 open (20.8%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | 7.9h | 4.0x |
| Resolution (median) | 30.2d | 1.5x |
| Zero-Reply Rate | 1.4% | Below org (3.3%) |
| Avg Comments/Ticket | 5.3 | — |
| Multi-Touch Rate | 94.4% | — |
| Automation Eligible | 1 (1.4%) | — |
| Unassigned | 0 | — |
| Stale (>7d no activity) | 6 | — |

### Status Breakdown

- **closed**: 40 (55.6%)
- **solved**: 17 (23.6%)
- **pending**: 11 (15.3%)
- **open**: 4 (5.6%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Megan Czaplinski | 61 | 11 (18.0%) | 8.5 | 0 (0.0%) |
| Dominik Vleming | 8 | 3 (37.5%) | 1.0 | 1 (12.5%) |
| Eileen Sciarra | 3 | 1 (33.3%) | 4.6 | 0 (0.0%) |

**Agent comment volume** (from comments.csv): 
Megan Czaplinski: 170, Dominik Vleming: 70, Eileen Sciarra: 15, Morning Ellergrace: 9, Katlyn Wright: 8, Wendy Adkinson: 4, Jacob Wicklund: 2, Rodoula Vasila: 2, Addison Young: 1, Daniele Catteddu: 1

### Top Tags

`sales-membership` (63), `membership` (60), `skip_css` (59), `sales` (56), `pending_followup_1` (51), `pending_followup_solve` (42), `it` (6), `web_widget` (3), `system_email_notification_failure` (2), `internal-requests` (2)

### Top Subject Keywords

*inquiry* (59), *membership* (57), *individual* (6), *contributor* (6), *information* (6), *training* (4), *cloud* (3), *native* (2), *private* (2), *interested* (2)

### Identified Patterns

- **Growing backlog**: 15 open tickets (20.8%). Without intervention, this queue will become a bottleneck.
- **Stale tickets**: 6 tickets have had no activity in over 7 days (0 over 30 days).
- **Slow response**: Median first response of 7.9h, which is 4.0x the org-wide median of 2.0h.
- **Weekend gap**: Weekend response is 44.5h vs. weekday 7.2h — a 6.2x penalty.
- **Above-average resolution time**: 30.2 days vs. org median of 20.0d.
- **Workload concentration**: Megan Czaplinski handles 84.7% of tickets. The remaining 2 agent(s) handle the rest.
- **High-touch queue**: 94.4% of tickets require more than 2 comments to resolve, indicating complex or multi-step issues.

### Proposed Solutions

1. **Backlog sprint**: Dedicate 2-3 hours per week specifically to clearing the 15 open tickets until the open rate drops below 15%.
2. **Weekend coverage**: Include Membership Engagement in weekend on-call rotation, or deploy the weekend auto-acknowledgment template to set expectations for Saturday/Sunday submissions.
3. **Create macros for common topics**: The top tags (membership, star) indicate recurring question types. Build Zendesk macros with pre-written responses for these topics to reduce handling time.
4. **Improve first-contact resolution**: 94.4% of tickets need 3+ comments. Review the most common multi-touch tickets and update macros or help center articles to provide complete answers upfront.
