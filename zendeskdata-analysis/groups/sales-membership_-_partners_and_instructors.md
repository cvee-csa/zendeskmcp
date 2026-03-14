# Sales/Membership - Partners and Instructors

*Part of the [CSA Zendesk Group-by-Group Analysis](00_summary.md)*

---

**Severity: HIGH** | 17 tickets | 11 open (64.7%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | 6.1h | 3.0x |
| Resolution (median) | 24.4d | 1.2x |
| Zero-Reply Rate | 5.9% | Above org (3.3%) |
| Avg Comments/Ticket | 4.4 | — |
| Multi-Touch Rate | 52.9% | — |
| Automation Eligible | 0 (0.0%) | — |
| Unassigned | 0 | — |
| Stale (>7d no activity) | 9 | — |

### Status Breakdown

- **open**: 9 (52.9%)
- **closed**: 4 (23.5%)
- **solved**: 2 (11.8%)
- **pending**: 1 (5.9%)
- **hold**: 1 (5.9%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Rick Blue | 17 | 11 (64.7%) | 6.1 | 1 (5.9%) |

**Agent comment volume** (from comments.csv): 
Rick Blue: 17, Katlyn Wright: 12, Nekoashi Wolf: 10, Rodoula Vasila: 8, Morning Ellergrace: 2, Eileen Sciarra: 1

### Top Tags

`sales-membership` (7), `skip_css` (5), `pending_followup_1` (2), `training_partner` (2), `ccsk` (2), `web_widget` (2), `cczt_bundle` (1), `complimentary` (1), `ttt` (1), `ttt_quiz` (1)

### Top Subject Keywords

*ccsk* (12), *train* (9), *trainer* (9), *student* (7), *submission* (7), *interested* (4), *being* (3), *training* (3), *partner* (3), *instructor* (2)

### Satisfaction

- **Good**: 2 | **Bad**: 0 | **Offered (no response)**: 2
- Response rate: 50.0%

### Identified Patterns

- **Severe backlog**: 11 tickets remain open (64.7%), far above the org average. The queue is accumulating faster than it's being cleared.
- **Stale tickets**: 9 tickets have had no activity in over 7 days (0 over 30 days).
- **Slow response**: Median first response of 6.1h, which is 3.0x the org-wide median of 2.0h.
- **Elevated zero-reply rate**: 5.9% vs. org average of 3.3%.
- **Single point of failure**: Only one agent (Rick Blue) handles this entire queue. Any absence means zero coverage.
- **Agent bottleneck — Rick Blue**: 11 open out of 17 assigned (64.7% open rate).
- **High-touch queue**: 52.9% of tickets require more than 2 comments to resolve, indicating complex or multi-step issues.

### Proposed Solutions

1. **Immediate triage**: Schedule a dedicated session to review all 11 open tickets. Close stale/resolved tickets, re-assign active ones, and escalate blocked tickets. Target: reduce open rate to under 25% within 2 weeks.
2. **Add backup agent**: Cross-train at least one additional agent on Sales/Membership - Partners and Instructors workflows. Set up round-robin assignment so the queue doesn't depend on a single person.
3. **Mandatory reply before close**: Add a Zendesk requirement that at least one public comment must exist before a ticket can be marked solved. This ensures every requester gets a response.
4. **Redistribute Rick Blue's queue**: 11 open tickets cannot be cleared by one person. Redistribute across available agents in the group or pull in cross-trained agents from adjacent teams.
5. **Create macros for common topics**: The top tags (ccsk) indicate recurring question types. Build Zendesk macros with pre-written responses for these topics to reduce handling time.
