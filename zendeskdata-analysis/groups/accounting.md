# Accounting

*Part of the [CSA Zendesk Group-by-Group Analysis](00_summary.md)*

---

**Severity: MEDIUM** | 113 tickets | 37 open (32.7%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | No data | — |
| Resolution (median) | 79.4d | 4.0x |
| Zero-Reply Rate | 2.7% | Below org (3.3%) |
| Avg Comments/Ticket | 7.8 | — |
| Multi-Touch Rate | 92.0% | — |
| Automation Eligible | 0 (0.0%) | — |
| Unassigned | 0 | — |
| Stale (>7d no activity) | 31 | — |

### Status Breakdown

- **solved**: 57 (50.4%)
- **closed**: 19 (16.8%)
- **hold**: 19 (16.8%)
- **open**: 18 (15.9%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Christina Lehman | 93 | 35 (37.6%) | 0.0 | 3 (3.2%) |
| Madison Hopkins | 20 | 2 (10.0%) | 4.3 | 0 (0.0%) |

**Agent comment volume** (from comments.csv): 
Rodoula Vasila: 191, Christina Lehman: 148, Madison Hopkins: 119, Katlyn Wright: 87, Morning Ellergrace: 52, Wendy Adkinson: 34, Nekoashi Wolf: 19, John DiMaria: 9, Rick Blue: 9, Paige McKenna: 2

### Top Tags

`accounting` (87), `skip_css` (77), `level2` (73), `star` (63), `star_certification` (59), `invoiced` (50), `roster` (20), `it` (18), `to_invoice` (17), `ccsk` (15)

### Top Subject Keywords

*invoice* (149), *requested* (82), *star* (73), *submission* (68), *com* (66), *sent* (55), *request* (13), *roster* (11), *cloud* (11), *security* (10)

### Satisfaction

- **Good**: 6 | **Bad**: 0 | **Offered (no response)**: 62
- Response rate: 8.8%

### Identified Patterns

- **Growing backlog**: 37 open tickets (32.7%). Without intervention, this queue will become a bottleneck.
- **Stale tickets**: 31 tickets have had no activity in over 7 days (0 over 30 days).
- **No response data**: First response time is null or zero, suggesting tickets may enter this queue without an initial reply being tracked.
- **Very slow resolution**: Median resolution of 79.4 days — 4.0x the org average of 20.0d. Tickets stall in this queue.
- **Workload concentration**: Christina Lehman handles 82.3% of tickets. The remaining 1 agent(s) handle the rest.
- **High-touch queue**: 92.0% of tickets require more than 2 comments to resolve, indicating complex or multi-step issues.

### Proposed Solutions

1. **Backlog sprint**: Dedicate 2-3 hours per week specifically to clearing the 37 open tickets until the open rate drops below 15%.
2. **Process review**: Resolution time of 79.4d indicates process bottlenecks (approvals, external dependencies, unclear ownership). Map the end-to-end workflow, identify where tickets stall, and set internal checkpoints at 7-day and 14-day marks.
3. **Create macros for common topics**: The top tags (accounting, star, ccsk, disconnect) indicate recurring question types. Build Zendesk macros with pre-written responses for these topics to reduce handling time.
4. **Improve first-contact resolution**: 92.0% of tickets need 3+ comments. Review the most common multi-touch tickets and update macros or help center articles to provide complete answers upfront.
