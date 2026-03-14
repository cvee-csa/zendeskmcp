# Sales/Membership - Chapters

*Part of the [CSA Zendesk Group-by-Group Analysis](00_summary.md)*

---

**Severity: CRITICAL** | 169 tickets | 120 open (71.0%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | 2474.3h | 1237.2x |
| Resolution (median) | 122.8d | 6.1x |
| Zero-Reply Rate | 0.6% | Below org (3.3%) |
| Avg Comments/Ticket | 1.4 | — |
| Multi-Touch Rate | 3.6% | — |
| Automation Eligible | 0 (0.0%) | — |
| Unassigned | 1 | — |
| Stale (>7d no activity) | 93 | — |

### Status Breakdown

- **open**: 118 (69.8%)
- **closed**: 45 (26.6%)
- **solved**: 4 (2.4%)
- **new**: 1 (0.6%)
- **pending**: 1 (0.6%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Billy Toney | 168 | 119 (70.8%) | 2474.3 | 1 (0.6%) |

**Agent comment volume** (from comments.csv): 
Billy Toney: 39, Nekoashi Wolf: 7, Dominik Vleming: 4, Morning Ellergrace: 4, Rodoula Vasila: 3, Katlyn Wright: 2, Ryan Bergsma: 2, Wendy Adkinson: 2, Eileen Sciarra: 1, Jeffrey Westcott: 1

### Top Tags

`sales-membership` (49), `skip_css` (48), `membership` (5), `sales` (4), `it` (3), `web_widget` (2), `pending_followup_1` (2), `chapter_leader_cczt_bundle_request` (1), `chapters` (1), `amazon` (1)

### Top Subject Keywords

*chapter* (126), *message* (123), *metro* (14), *new* (13), *north* (13), *carolina* (12), *list* (12), *york* (10), *united* (8), *rsac* (7)

### Identified Patterns

- **Severe backlog**: 120 tickets remain open (71.0%), far above the org average. The queue is accumulating faster than it's being cleared.
- **Stale tickets**: 93 tickets have had no activity in over 7 days (0 over 30 days).
- **Critically slow response**: Median first response of 2474.3 hours — requesters wait 103.1 days before hearing from anyone.
- **Very slow resolution**: Median resolution of 122.8 days — 6.1x the org average of 20.0d. Tickets stall in this queue.
- **Single point of failure**: Only one agent (Billy Toney) handles this entire queue. Any absence means zero coverage.
- **Agent bottleneck — Billy Toney**: 119 open out of 168 assigned (70.8% open rate).
- **Unassigned tickets**: 1 tickets have no agent assigned.

### Proposed Solutions

1. **Immediate triage**: Schedule a dedicated session to review all 120 open tickets. Close stale/resolved tickets, re-assign active ones, and escalate blocked tickets. Target: reduce open rate to under 25% within 2 weeks.
2. **Add backup agent**: Cross-train at least one additional agent on Sales/Membership - Chapters workflows. Set up round-robin assignment so the queue doesn't depend on a single person.
3. **Set first-response SLA**: Configure a Zendesk SLA policy for Sales/Membership - Chapters with a first-response target appropriate to severity (recommended: 4h for high priority, 8 business hours for normal). Enable breach notifications to the group lead.
4. **Process review**: Resolution time of 122.8d indicates process bottlenecks (approvals, external dependencies, unclear ownership). Map the end-to-end workflow, identify where tickets stall, and set internal checkpoints at 7-day and 14-day marks.
5. **Redistribute Billy Toney's queue**: 119 open tickets cannot be cleared by one person. Redistribute across available agents in the group or pull in cross-trained agents from adjacent teams.
6. **Create macros for common topics**: The top tags (membership) indicate recurring question types. Build Zendesk macros with pre-written responses for these topics to reduce handling time.
