# IT-Support

*Part of the [CSA Zendesk Group-by-Group Analysis](00_summary.md)*

---

**Severity: LOW** | 1,796 tickets | 52 open (2.9%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | 0.7h | 0.3x (better) |
| Resolution (median) | 20.1d | 1.0x |
| Zero-Reply Rate | 3.8% | Above org (3.3%) |
| Avg Comments/Ticket | 4.0 | — |
| Multi-Touch Rate | 65.3% | — |
| Automation Eligible | 54 (3.0%) | — |
| Unassigned | 24 | — |
| Stale (>7d no activity) | 5 | — |

### Status Breakdown

- **closed**: 1081 (60.2%)
- **solved**: 651 (36.2%)
- **pending**: 26 (1.4%)
- **open**: 20 (1.1%)
- **deleted**: 12 (0.7%)
- **hold**: 5 (0.3%)
- **new**: 1 (0.1%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Rodoula Vasila | 844 | 29 (3.4%) | 1.8 | 37 (4.4%) |
| Wendy Adkinson | 538 | 8 (1.5%) | 0.3 | 8 (1.5%) |
| Katlyn Wright | 274 | 8 (2.9%) | 0.3 | 4 (1.5%) |
| Morning Ellergrace | 111 | 4 (3.6%) | 2.5 | 3 (2.7%) |
| Nekoashi Wolf | 2 | 1 (50.0%) | 7.6 | 1 (50.0%) |
| Anna McKee (Schorr) | 1 | 1 (100.0%) | 8.9 | 0 (0.0%) |
| Jacob Wicklund | 1 | 0 (0.0%) | — | 0 (0.0%) |
| Matt Johnson | 1 | 0 (0.0%) | — | 1 (100.0%) |

**Agent comment volume** (from comments.csv): 
Rodoula Vasila: 1833, Wendy Adkinson: 1127, Katlyn Wright: 586, Morning Ellergrace: 430, Eileen Sciarra: 171, Megan Czaplinski: 43, Madison Hopkins: 40, Dominik Vleming: 37, Anna McKee (Schorr): 34, Paige McKenna: 30

### Top Tags

`skip_css` (1636), `it` (1628), `purchase_notification` (474), `training` (443), `bundle` (417), `web_widget` (347), `taise` (330), `ccsk` (300), `star` (257), `self_assessment` (194)

### Top Subject Keywords

*exam* (639), *bundle* (598), *purchase* (476), *notification* (472), *trusted* (327), *safety* (326), *expert* (325), *star* (291), *ccsk* (262), *submission* (211)

### Satisfaction

- **Good**: 225 | **Bad**: 10 | **Offered (no response)**: 1194
- Response rate: 16.4%

### Identified Patterns

- **Healthy throughput**: Only 2.9% open rate indicates the queue is being actively managed and cleared.
- **Stale tickets**: 5 tickets have had no activity in over 7 days (0 over 30 days).
- **Fast response**: Median first response of 0.7h — well under the org median of 2.0h.
- **Weekend gap**: Weekend response is 22.5h vs. weekday 0.4h — a 50.9x penalty.
- **Elevated zero-reply rate**: 3.8% vs. org average of 3.3%.
- **High-touch queue**: 65.3% of tickets require more than 2 comments to resolve, indicating complex or multi-step issues.
- **Unassigned tickets**: 24 tickets have no agent assigned.

### Proposed Solutions

1. **Weekend coverage**: Include IT-Support in weekend on-call rotation, or deploy the weekend auto-acknowledgment template to set expectations for Saturday/Sunday submissions.
2. **Fix routing**: 24 tickets have no agent. Create a catch-all assignment rule: any ticket unassigned after 30 minutes auto-assigns to the group's on-duty agent.
3. **Create macros for common topics**: The top tags (ccsk, star, self_assessment, disconnect, membership, instructions) indicate recurring question types. Build Zendesk macros with pre-written responses for these topics to reduce handling time.
4. **Improve first-contact resolution**: 65.3% of tickets need 3+ comments. Review the most common multi-touch tickets and update macros or help center articles to provide complete answers upfront.
