# Sales/Membership

*Part of the [CSA Zendesk Group-by-Group Analysis](00_summary.md)*

---

**Severity: HIGH** | 15 tickets | 7 open (46.7%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | 18.7h | 9.3x |
| Resolution (median) | 27.1d | 1.4x |
| Zero-Reply Rate | 0.0% | Below org (3.3%) |
| Avg Comments/Ticket | 5.2 | — |
| Multi-Touch Rate | 73.3% | — |
| Automation Eligible | 0 (0.0%) | — |
| Unassigned | 0 | — |
| Stale (>7d no activity) | 4 | — |

### Status Breakdown

- **open**: 6 (40.0%)
- **closed**: 6 (40.0%)
- **solved**: 2 (13.3%)
- **pending**: 1 (6.7%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Dominik Vleming | 6 | 4 (66.7%) | 42.4 | 0 (0.0%) |
| Eileen Sciarra | 4 | 2 (50.0%) | 16.7 | 0 (0.0%) |
| Megan Czaplinski | 4 | 1 (25.0%) | 23.3 | 0 (0.0%) |
| Tara Hanson | 1 | 0 (0.0%) | 21.9 | 0 (0.0%) |

**Agent comment volume** (from comments.csv): 
Megan Czaplinski: 13, Rodoula Vasila: 12, Dominik Vleming: 10, Eileen Sciarra: 6, Katlyn Wright: 6, Morning Ellergrace: 2, Paige McKenna: 2, Wendy Adkinson: 2, Andy Ruth: 1, Anna McKee (Schorr): 1

### Top Tags

`skip_css` (9), `pending_followup_1` (5), `pending_followup_solve` (5), `sales-membership` (4), `web_widget` (3), `training` (2), `star` (2), `it` (2), `sales` (1), `logo` (1)

### Top Subject Keywords

*training* (8), *inquiry* (5), *private* (4), *details* (3), *security* (3), *service* (2), *cloud* (2), *request* (1), *add* (1), *logo* (1)

### Satisfaction

- **Good**: 2 | **Bad**: 0 | **Offered (no response)**: 7
- Response rate: 22.2%

### Identified Patterns

- **Growing backlog**: 7 open tickets (46.7%). Without intervention, this queue will become a bottleneck.
- **Stale tickets**: 4 tickets have had no activity in over 7 days (0 over 30 days).
- **Slow response**: Median first response of 18.7h, which is 9.3x the org-wide median of 2.0h.
- **High-touch queue**: 73.3% of tickets require more than 2 comments to resolve, indicating complex or multi-step issues.

### Proposed Solutions

1. **Backlog sprint**: Dedicate 2-3 hours per week specifically to clearing the 7 open tickets until the open rate drops below 15%.
2. **Set first-response SLA**: Configure a Zendesk SLA policy for Sales/Membership with a first-response target appropriate to severity (recommended: 4h for high priority, 8 business hours for normal). Enable breach notifications to the group lead.
3. **Create macros for common topics**: The top tags (star, membership) indicate recurring question types. Build Zendesk macros with pre-written responses for these topics to reduce handling time.
4. **Improve first-contact resolution**: 73.3% of tickets need 3+ comments. Review the most common multi-touch tickets and update macros or help center articles to provide complete answers upfront.
