# Support Tasks

*Part of the [CSA Zendesk Group-by-Group Analysis](00_summary.md)*

---

**Severity: MEDIUM** | 13 tickets | 8 open (61.5%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | No data | — |
| Resolution (median) | 168.2d | 8.4x |
| Zero-Reply Rate | 0.0% | Below org (3.3%) |
| Avg Comments/Ticket | 3.8 | — |
| Multi-Touch Rate | 46.2% | — |
| Automation Eligible | 0 (0.0%) | — |
| Unassigned | 0 | — |
| Stale (>7d no activity) | 5 | — |

### Status Breakdown

- **open**: 8 (61.5%)
- **closed**: 3 (23.1%)
- **solved**: 2 (15.4%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Rodoula Vasila | 11 | 6 (54.5%) | 862.6 | 0 (0.0%) |
| Morning Ellergrace | 1 | 1 (100.0%) | 0.0 | 0 (0.0%) |
| Wendy Adkinson | 1 | 1 (100.0%) | — | 0 (0.0%) |

**Agent comment volume** (from comments.csv): 
Rodoula Vasila: 27, Morning Ellergrace: 8, Wendy Adkinson: 4, Christina Lehman: 2, Madison Hopkins: 2, Dominik Vleming: 1, Katlyn Wright: 1, Rick Blue: 1, Tara Hanson: 1

### Top Tags

`skip_css` (12), `it` (6), `support_task` (6), `make_macro` (4), `make_documentation` (2), `yearly_task` (1), `update_macro` (1), `disconnect` (1), `invoiced` (1), `level2` (1)

### Top Subject Keywords

*update* (7), *macro* (5), *create* (4), *documentation* (4), *star* (3), *submission* (2), *invoice* (2), *api* (2), *key* (2), *coc* (1)

### Identified Patterns

- **Severe backlog**: 8 tickets remain open (61.5%), far above the org average. The queue is accumulating faster than it's being cleared.
- **Stale tickets**: 5 tickets have had no activity in over 7 days (0 over 30 days).
- **No response data**: First response time is null or zero, suggesting tickets may enter this queue without an initial reply being tracked.
- **Very slow resolution**: Median resolution of 168.2 days — 8.4x the org average of 20.0d. Tickets stall in this queue.
- **Workload concentration**: Rodoula Vasila handles 84.6% of tickets. The remaining 2 agent(s) handle the rest.
- **Agent bottleneck — Rodoula Vasila**: 6 open out of 11 assigned (54.5% open rate).

### Proposed Solutions

1. **Immediate triage**: Schedule a dedicated session to review all 8 open tickets. Close stale/resolved tickets, re-assign active ones, and escalate blocked tickets. Target: reduce open rate to under 25% within 2 weeks.
2. **Process review**: Resolution time of 168.2d indicates process bottlenecks (approvals, external dependencies, unclear ownership). Map the end-to-end workflow, identify where tickets stall, and set internal checkpoints at 7-day and 14-day marks.
3. **Create macros for common topics**: The top tags (disconnect, star) indicate recurring question types. Build Zendesk macros with pre-written responses for these topics to reduce handling time.
