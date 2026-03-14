# IT-Security

*Part of the [CSA Zendesk Group-by-Group Analysis](00_summary.md)*

---

**Severity: MEDIUM** | 13 tickets | 4 open (30.8%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | 2.0h | 1.0x (better) |
| Resolution (median) | 79.0d | 4.0x |
| Zero-Reply Rate | 7.7% | Above org (3.3%) |
| Avg Comments/Ticket | 6.9 | — |
| Multi-Touch Rate | 61.5% | — |
| Automation Eligible | 0 (0.0%) | — |
| Unassigned | 0 | — |
| Stale (>7d no activity) | 1 | — |

### Status Breakdown

- **closed**: 5 (38.5%)
- **solved**: 4 (30.8%)
- **hold**: 2 (15.4%)
- **open**: 2 (15.4%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Kaitlin Morgan | 4 | 0 (0.0%) | 1873.0 | 0 (0.0%) |
| Nekoashi Wolf | 4 | 4 (100.0%) | 1.6 | 0 (0.0%) |
| Jacob Wicklund | 2 | 0 (0.0%) | 743.2 | 0 (0.0%) |
| Kurt S | 2 | 0 (0.0%) | — | 1 (50.0%) |
| Ryan Bergsma | 1 | 0 (0.0%) | — | 0 (0.0%) |

**Agent comment volume** (from comments.csv): 
Kurt S: 21, Jacob Wicklund: 19, Ryan Bergsma: 10, Kaitlin Morgan: 7, Morning Ellergrace: 6, Karamvir Rai: 3, Larry Hughes: 2, Nekoashi Wolf: 2, Courtney Stiven: 1, Dominik Vleming: 1

### Top Tags

`it` (11), `skip_css` (10), `internal-requests` (4), `ada` (1)

### Top Subject Keywords

*vulnerability* (3), *report* (3), *critical* (3), *security* (3), *anyone* (2), *weak* (2), *fwd* (1), *openai* (1), *teams* (1), *invite* (1)

### Identified Patterns

- **Growing backlog**: 4 open tickets (30.8%). Without intervention, this queue will become a bottleneck.
- **Stale tickets**: 1 tickets have had no activity in over 7 days (0 over 30 days).
- **Very slow resolution**: Median resolution of 79.0 days — 4.0x the org average of 20.0d. Tickets stall in this queue.
- **Elevated zero-reply rate**: 7.7% vs. org average of 3.3%.
- **High-touch queue**: 61.5% of tickets require more than 2 comments to resolve, indicating complex or multi-step issues.

### Proposed Solutions

1. **Backlog sprint**: Dedicate 2-3 hours per week specifically to clearing the 4 open tickets until the open rate drops below 15%.
2. **Mandatory reply before close**: Add a Zendesk requirement that at least one public comment must exist before a ticket can be marked solved. This ensures every requester gets a response.
3. **Process review**: Resolution time of 79.0d indicates process bottlenecks (approvals, external dependencies, unclear ownership). Map the end-to-end workflow, identify where tickets stall, and set internal checkpoints at 7-day and 14-day marks.
4. **Improve first-contact resolution**: 61.5% of tickets need 3+ comments. Review the most common multi-touch tickets and update macros or help center articles to provide complete answers upfront.
