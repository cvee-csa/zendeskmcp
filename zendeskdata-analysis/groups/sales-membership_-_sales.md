# Sales/Membership - Sales

*Part of the [CSA Zendesk Group-by-Group Analysis](00_summary.md)*

---

**Severity: MEDIUM** | 464 tickets | 102 open (22.0%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | 7.1h | 3.5x |
| Resolution (median) | 20.2d | 1.0x |
| Zero-Reply Rate | 0.2% | Below org (3.3%) |
| Avg Comments/Ticket | 2.4 | — |
| Multi-Touch Rate | 23.7% | — |
| Automation Eligible | 0 (0.0%) | — |
| Unassigned | 0 | — |
| Stale (>7d no activity) | 60 | — |

### Status Breakdown

- **closed**: 245 (52.8%)
- **solved**: 117 (25.2%)
- **open**: 91 (19.6%)
- **pending**: 10 (2.2%)
- **hold**: 1 (0.2%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Dominik Vleming | 458 | 100 (21.8%) | 7.1 | 1 (0.2%) |
| Eileen Sciarra | 6 | 2 (33.3%) | 12.4 | 0 (0.0%) |

**Agent comment volume** (from comments.csv): 
Dominik Vleming: 360, Eileen Sciarra: 120, Paige McKenna: 47, Addison Young: 8, Katlyn Wright: 8, Rodoula Vasila: 6, Megan Czaplinski: 4, Wendy Adkinson: 4, Morning Ellergrace: 3, Christina Lehman: 2

### Top Tags

`sales-membership` (454), `sales` (414), `membership` (395), `skip_css` (363), `pending_followup_1` (67), `pending_followup_solve` (60), `valid_ai_ted` (15), `system_email_notification_failure` (4), `web_widget` (3), `events` (2)

### Top Subject Keywords

*inquiry* (404), *membership* (395), *information* (258), *individual* (257), *contributor* (257), *valid* (16), *ted* (16), *thank* (15), *purchase* (15), *csa* (12)

### Satisfaction

- **Good**: 13 | **Bad**: 0 | **Offered (no response)**: 299
- Response rate: 4.2%

### Identified Patterns

- **Growing backlog**: 102 open tickets (22.0%). Without intervention, this queue will become a bottleneck.
- **Stale tickets**: 60 tickets have had no activity in over 7 days (0 over 30 days).
- **Slow response**: Median first response of 7.1h, which is 3.5x the org-wide median of 2.0h.
- **Weekend gap**: Weekend response is 34.4h vs. weekday 4.5h — a 7.6x penalty.
- **Workload concentration**: Dominik Vleming handles 98.7% of tickets. The remaining 1 agent(s) handle the rest.

### Proposed Solutions

1. **Backlog sprint**: Dedicate 2-3 hours per week specifically to clearing the 102 open tickets until the open rate drops below 15%.
2. **Weekend coverage**: Include Sales/Membership - Sales in weekend on-call rotation, or deploy the weekend auto-acknowledgment template to set expectations for Saturday/Sunday submissions.
3. **Create macros for common topics**: The top tags (membership) indicate recurring question types. Build Zendesk macros with pre-written responses for these topics to reduce handling time.
