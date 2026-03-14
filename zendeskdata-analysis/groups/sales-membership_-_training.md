# Sales/Membership - Training

*Part of the [CSA Zendesk Group-by-Group Analysis](00_summary.md)*

---

**Severity: MEDIUM** | 29 tickets | 2 open (6.9%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | 21.0h | 10.5x |
| Resolution (median) | 20.7d | 1.0x |
| Zero-Reply Rate | 0.0% | Below org (3.3%) |
| Avg Comments/Ticket | 4.3 | — |
| Multi-Touch Rate | 89.7% | — |
| Automation Eligible | 1 (3.4%) | — |
| Unassigned | 0 | — |
| Stale (>7d no activity) | 2 | — |

### Status Breakdown

- **closed**: 15 (51.7%)
- **solved**: 12 (41.4%)
- **hold**: 1 (3.4%)
- **open**: 1 (3.4%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Tara Hanson | 15 | 1 (6.7%) | 18.9 | 0 (0.0%) |
| Rick Blue | 14 | 1 (7.1%) | 41.9 | 0 (0.0%) |

**Agent comment volume** (from comments.csv): 
Tara Hanson: 23, Rick Blue: 21, Wendy Adkinson: 14, Rodoula Vasila: 12, Katlyn Wright: 8, Morning Ellergrace: 2

### Top Tags

`skip_css` (26), `sales-membership` (23), `credly` (8), `web_widget` (5), `pending_followup_1` (4), `pending_followup_solve` (4), `it` (2), `training` (1), `info-in` (1), `ccak` (1)

### Top Subject Keywords

*training* (13), *review* (12), *aicm* (12), *materials* (9), *invitation* (8), *contributors* (8), *needed* (8), *interested* (8), *trainer* (8), *course* (7)

### Satisfaction

- **Good**: 2 | **Bad**: 0 | **Offered (no response)**: 22
- Response rate: 8.3%

### Identified Patterns

- **Stale tickets**: 2 tickets have had no activity in over 7 days (0 over 30 days).
- **Slow response**: Median first response of 21.0h, which is 10.5x the org-wide median of 2.0h.
- **Weekend gap**: Weekend response is 68.5h vs. weekday 15.8h — a 4.3x penalty.
- **High-touch queue**: 89.7% of tickets require more than 2 comments to resolve, indicating complex or multi-step issues.

### Proposed Solutions

1. **Set first-response SLA**: Configure a Zendesk SLA policy for Sales/Membership - Training with a first-response target appropriate to severity (recommended: 4h for high priority, 8 business hours for normal). Enable breach notifications to the group lead.
2. **Improve first-contact resolution**: 89.7% of tickets need 3+ comments. Review the most common multi-touch tickets and update macros or help center articles to provide complete answers upfront.
