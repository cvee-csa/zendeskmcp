# IT-Operations

*Part of the [CSA Zendesk Group-by-Group Analysis](00_summary.md)*

---

**Severity: MEDIUM** | 160 tickets | 28 open (17.5%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | 1.7h | 0.8x (better) |
| Resolution (median) | 21.0d | 1.1x |
| Zero-Reply Rate | 21.9% | Above org (3.3%) |
| Avg Comments/Ticket | 6.7 | — |
| Multi-Touch Rate | 81.9% | — |
| Automation Eligible | 4 (2.5%) | — |
| Unassigned | 2 | — |
| Stale (>7d no activity) | 5 | — |

### Status Breakdown

- **closed**: 87 (54.4%)
- **solved**: 44 (27.5%)
- **hold**: 14 (8.8%)
- **open**: 14 (8.8%)
- **deleted**: 1 (0.6%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Jacob Wicklund | 70 | 13 (18.6%) | 1.9 | 16 (22.9%) |
| Kaitlin Morgan | 40 | 0 (0.0%) | 1.7 | 6 (15.0%) |
| Nekoashi Wolf | 31 | 11 (35.5%) | 1.2 | 4 (12.9%) |
| Ryan Bergsma | 17 | 3 (17.6%) | 1.5 | 9 (52.9%) |

**Agent comment volume** (from comments.csv): 
Jacob Wicklund: 282, Nekoashi Wolf: 190, Kurt S: 88, Ryan Bergsma: 85, Kaitlin Morgan: 69, Larry Hughes: 35, Joshua Buker: 28, Dominik Vleming: 27, Erik Johnson: 23, Marina Bregkou: 20

### Top Tags

`it` (157), `skip_css` (143), `internal-requests` (115), `system_email_notification_failure` (7), `followup_today` (7), `device` (3), `papertrail` (3), `rit` (3), `closed_by_merge` (3), `do_close` (1)

### Top Subject Keywords

*aas* (19), *access* (18), *csa* (16), *slack* (12), *rit* (12), *website* (12), *please* (11), *group* (11), *cloudsecurityalliance* (10), *new* (10)

### Identified Patterns

- **Stale tickets**: 5 tickets have had no activity in over 7 days (0 over 30 days).
- **Weekend gap**: Weekend response is 66.6h vs. weekday 1.7h — a 39.8x penalty.
- **High zero-reply rate**: 21.9% of tickets have no public response (35 tickets). Requesters are being ignored.
- **High-touch queue**: 81.9% of tickets require more than 2 comments to resolve, indicating complex or multi-step issues.
- **Unassigned tickets**: 2 tickets have no agent assigned.

### Proposed Solutions

1. **Mandatory reply before close**: Add a Zendesk requirement that at least one public comment must exist before a ticket can be marked solved. This ensures every requester gets a response.
2. **Weekend coverage**: Include IT-Operations in weekend on-call rotation, or deploy the weekend auto-acknowledgment template to set expectations for Saturday/Sunday submissions.
3. **Improve first-contact resolution**: 81.9% of tickets need 3+ comments. Review the most common multi-touch tickets and update macros or help center articles to provide complete answers upfront.
