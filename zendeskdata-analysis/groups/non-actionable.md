# Non-actionable

*Part of the [CSA Zendesk Group-by-Group Analysis](00_summary.md)*

---

**Severity: LOW** | 669 tickets | 0 open (0.0%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | No data | — |
| Resolution (median) | 0.0d | 0.0x (better) |
| Zero-Reply Rate | 0.1% | Below org (3.3%) |
| Avg Comments/Ticket | 2.0 | — |
| Multi-Touch Rate | 1.9% | — |
| Automation Eligible | 636 (95.1%) | — |
| Unassigned | 32 | — |
| Stale (>7d no activity) | 0 | — |

### Status Breakdown

- **closed**: 669 (100.0%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Rodoula Vasila | 346 | 0 (0.0%) | 0.0 | 1 (0.3%) |
| Katlyn Wright | 144 | 0 (0.0%) | — | 0 (0.0%) |
| Wendy Adkinson | 101 | 0 (0.0%) | 0.3 | 0 (0.0%) |
| Morning Ellergrace | 46 | 0 (0.0%) | 0.8 | 0 (0.0%) |

**Agent comment volume** (from comments.csv): 
Rodoula Vasila: 354, Katlyn Wright: 144, Wendy Adkinson: 108, Morning Ellergrace: 47, Kurt S: 3, Kaitlin Morgan: 1, Madison Hopkins: 1

### Top Tags

`skip_css` (637), `do_close` (636), `do_closed` (636), `edge_case` (636), `non-actionable` (636), `info-in` (185), `web_widget` (54), `it` (33), `valid_ai_ted` (32), `self_assessment` (12)

### Top Subject Keywords

*notification* (71), *registration* (70), *ccskv* (65), *sample* (65), *course* (65), *security* (59), *request* (48), *join* (48), *submission* (46), *rsa* (42)

### Identified Patterns

- **Healthy throughput**: Only 0.0% open rate indicates the queue is being actively managed and cleared.
- **No response data**: First response time is null or zero, suggesting tickets may enter this queue without an initial reply being tracked.
- **Fast resolution**: 0.0 days — well below the org median of 20.0d.
- **High automation potential**: 95.1% of tickets (636) are tagged with auto-close markers.
- **Unassigned tickets**: 32 tickets have no agent assigned.

### Proposed Solutions

1. **Deploy auto-close triggers**: 636 tickets are already tagged for automation. Configure Zendesk triggers to auto-solve these after 1 hour with no customer reply, using the auto-reply templates from `auto_reply_templates.md`.
2. **Fix routing**: 32 tickets have no agent. Create a catch-all assignment rule: any ticket unassigned after 30 minutes auto-assigns to the group's on-duty agent.
3. **Create macros for common topics**: The top tags (self_assessment, star) indicate recurring question types. Build Zendesk macros with pre-written responses for these topics to reduce handling time.
