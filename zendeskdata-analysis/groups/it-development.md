# IT-Development

*Part of the [CSA Zendesk Group-by-Group Analysis](00_summary.md)*

---

**Severity: HIGH** | 28 tickets | 7 open (25.0%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | 39.6h | 19.8x |
| Resolution (median) | 22.9d | 1.1x |
| Zero-Reply Rate | 0.0% | Below org (3.3%) |
| Avg Comments/Ticket | 3.2 | — |
| Multi-Touch Rate | 50.0% | — |
| Automation Eligible | 0 (0.0%) | — |
| Unassigned | 12 | — |
| Stale (>7d no activity) | 4 | — |

### Status Breakdown

- **closed**: 14 (50.0%)
- **solved**: 7 (25.0%)
- **open**: 5 (17.9%)
- **new**: 2 (7.1%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Ryan Bergsma | 16 | 2 (12.5%) | — | 0 (0.0%) |

**Agent comment volume** (from comments.csv): 
Lucas Moyle: 25, Rodoula Vasila: 15, Katlyn Wright: 9, Karamvir Rai: 8, Kurt S: 7, Alain Pannetrat: 4, Jacob Wicklund: 4, Morning Ellergrace: 3, Nekoashi Wolf: 2, Ryan Bergsma: 2

### Top Tags

`it` (28), `skip_css` (26), `internal-requests` (4), `development` (2), `credly` (2)

### Top Subject Keywords

*star* (6), *csa* (4), *cloudsecurityalliance* (4), *org* (4), *certificate* (3), *submission* (3), *auth* (3), *update* (3), *issue* (3), *name* (2)

### Identified Patterns

- **Growing backlog**: 7 open tickets (25.0%). Without intervention, this queue will become a bottleneck.
- **Stale tickets**: 4 tickets have had no activity in over 7 days (0 over 30 days).
- **Slow response**: Median first response of 39.6h, which is 19.8x the org-wide median of 2.0h.
- **Single point of failure**: Only one agent (Ryan Bergsma) handles this entire queue. Any absence means zero coverage.
- **Unassigned tickets**: 12 tickets have no agent assigned.

### Proposed Solutions

1. **Backlog sprint**: Dedicate 2-3 hours per week specifically to clearing the 7 open tickets until the open rate drops below 15%.
2. **Add backup agent**: Cross-train at least one additional agent on IT-Development workflows. Set up round-robin assignment so the queue doesn't depend on a single person.
3. **Set first-response SLA**: Configure a Zendesk SLA policy for IT-Development with a first-response target appropriate to severity (recommended: 4h for high priority, 8 business hours for normal). Enable breach notifications to the group lead.
4. **Fix routing**: 12 tickets have no agent. Create a catch-all assignment rule: any ticket unassigned after 30 minutes auto-assigns to the group's on-duty agent.
