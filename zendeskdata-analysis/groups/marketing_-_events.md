# Marketing - Events

*Part of the [CSA Zendesk Group-by-Group Analysis](00_summary.md)*

---

**Severity: HIGH** | 5 tickets | 3 open (60.0%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | 72.0h | 36.0x |
| Resolution (median) | 32.9d | 1.6x |
| Zero-Reply Rate | 0.0% | Below org (3.3%) |
| Avg Comments/Ticket | 4.8 | — |
| Multi-Touch Rate | 80.0% | — |
| Automation Eligible | 0 (0.0%) | — |
| Unassigned | 1 | — |
| Stale (>7d no activity) | 2 | — |

### Status Breakdown

- **closed**: 2 (40.0%)
- **open**: 2 (40.0%)
- **new**: 1 (20.0%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Morgan Belden | 3 | 1 (33.3%) | 72.0 | 0 (0.0%) |
| Addison Young | 1 | 1 (100.0%) | — | 0 (0.0%) |

**Agent comment volume** (from comments.csv): 
Morgan Belden: 7, Addison Young: 3, Rodoula Vasila: 3, Morning Ellergrace: 1

### Top Tags

`events` (3), `skip_css` (2), `cpe` (1), `marketing` (1), `info-in` (1), `pending_followup_1` (1), `pending_followup_solve` (1)

### Top Subject Keywords

*csa* (3), *summit* (2), *rsac* (2), *download* (1), *virtual* (1), *cloud* (1), *nhi* (1), *certificate* (1), *shipping* (1), *rsa* (1)

### Identified Patterns

- **Severe backlog**: 3 tickets remain open (60.0%), far above the org average. The queue is accumulating faster than it's being cleared.
- **Stale tickets**: 2 tickets have had no activity in over 7 days (0 over 30 days).
- **Critically slow response**: Median first response of 72.0 hours — requesters wait 3.0 days before hearing from anyone.
- **Above-average resolution time**: 32.9 days vs. org median of 20.0d.
- **High-touch queue**: 80.0% of tickets require more than 2 comments to resolve, indicating complex or multi-step issues.
- **Unassigned tickets**: 1 tickets have no agent assigned.

### Proposed Solutions

1. **Immediate triage**: Schedule a dedicated session to review all 3 open tickets. Close stale/resolved tickets, re-assign active ones, and escalate blocked tickets. Target: reduce open rate to under 25% within 2 weeks.
2. **Set first-response SLA**: Configure a Zendesk SLA policy for Marketing - Events with a first-response target appropriate to severity (recommended: 4h for high priority, 8 business hours for normal). Enable breach notifications to the group lead.
3. **Improve first-contact resolution**: 80.0% of tickets need 3+ comments. Review the most common multi-touch tickets and update macros or help center articles to provide complete answers upfront.
