# CSA Zendesk: Group-by-Group Analysis

**Generated:** March 13, 2026
**Data Source:** Cross-referenced tickets.csv, ticket_metrics.csv, comments.csv, agents.csv, groups.csv, tags.csv
**Org Baselines:** Median response 2.0h | Median resolution 20.0d | Zero-reply rate 3.3%

---

## Summary

| Group | Tickets | Open (%) | Response (h) | Resolution (d) | Severity |
|---|---|---|---|---|---|
| IT-Support | 1,796 | 52 (2.9%) | 0.7 | 20.1 | **LOW** |
| Non-actionable | 669 | 0 (0.0%) | 0.0 | 0.0 | **LOW** |
| Sales/Membership - Sales | 464 | 102 (22.0%) | 7.1 | 20.2 | **MEDIUM** |
| Sales/Membership - Chapters | 169 | 120 (71.0%) | 2474.3 | 122.8 | **CRITICAL** |
| IT-Operations | 160 | 28 (17.5%) | 1.7 | 21.0 | **MEDIUM** |
| Accounting | 113 | 37 (32.7%) | 0.0 | 79.4 | **MEDIUM** |
| Membership Engagement | 72 | 15 (20.8%) | 7.9 | 30.2 | **MEDIUM** |
| Sales/Membership - Training | 29 | 2 (6.9%) | 21.0 | 20.7 | **MEDIUM** |
| IT-Development | 28 | 7 (25.0%) | 39.6 | 22.9 | **HIGH** |
| IT-Operations-Projects | 28 | 24 (85.7%) | 6.5 | 44.1 | **HIGH** |
| Sales/Membership - Partners and Instructors | 17 | 11 (64.7%) | 6.1 | 24.4 | **HIGH** |
| Sales/Membership | 15 | 7 (46.7%) | 18.7 | 27.1 | **HIGH** |
| IT-Security | 13 | 4 (30.8%) | 2.0 | 79.0 | **MEDIUM** |
| Support Tasks | 13 | 8 (61.5%) | 0.0 | 168.2 | **MEDIUM** |
| Kurt's Task List | 7 | 2 (28.6%) | — | 10.4 | **LOW** |
| Marketing - Events | 5 | 3 (60.0%) | 72.0 | 32.9 | **HIGH** |
| Operations Excellence | 4 | 2 (50.0%) | 18.9 | 55.5 | **MEDIUM** |
| Research and Development - STAR | 2 | 1 (50.0%) | — | 86.9 | **LOW** |
| IT-Operations-Tasks | 1 | 1 (100.0%) | 2.5 | — | **MEDIUM** |

---

## IT-Support

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

---

## Non-actionable

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

---

## Sales/Membership - Sales

**Severity: MEDIUM** | 464 tickets | 102 open (22.0%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | 7.1h | 3.5x |
| Resolution (median) | 20.2d | 1.0x |
| Zero-Reply Rate | 0.2% | Below org (3.3%) |
| Avg Comments/Ticket | 2.4 | — |
| Multi-Touch Rate | 23.7% | — |
| Automation Eligible | 0 (0.0%) | — |
| Unassigned | 0 | — |
| Stale (>7d no activity) | 60 | — |

### Status Breakdown

- **closed**: 245 (52.8%)
- **solved**: 117 (25.2%)
- **open**: 91 (19.6%)
- **pending**: 10 (2.2%)
- **hold**: 1 (0.2%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Dominik Vleming | 458 | 100 (21.8%) | 7.1 | 1 (0.2%) |
| Eileen Sciarra | 6 | 2 (33.3%) | 12.4 | 0 (0.0%) |

**Agent comment volume** (from comments.csv): 
Dominik Vleming: 360, Eileen Sciarra: 120, Paige McKenna: 47, Addison Young: 8, Katlyn Wright: 8, Rodoula Vasila: 6, Megan Czaplinski: 4, Wendy Adkinson: 4, Morning Ellergrace: 3, Christina Lehman: 2

### Top Tags

`sales-membership` (454), `sales` (414), `membership` (395), `skip_css` (363), `pending_followup_1` (67), `pending_followup_solve` (60), `valid_ai_ted` (15), `system_email_notification_failure` (4), `web_widget` (3), `events` (2)

### Top Subject Keywords

*inquiry* (404), *membership* (395), *information* (258), *individual* (257), *contributor* (257), *valid* (16), *ted* (16), *thank* (15), *purchase* (15), *csa* (12)

### Satisfaction

- **Good**: 13 | **Bad**: 0 | **Offered (no response)**: 299
- Response rate: 4.2%

### Identified Patterns

- **Growing backlog**: 102 open tickets (22.0%). Without intervention, this queue will become a bottleneck.
- **Stale tickets**: 60 tickets have had no activity in over 7 days (0 over 30 days).
- **Slow response**: Median first response of 7.1h, which is 3.5x the org-wide median of 2.0h.
- **Weekend gap**: Weekend response is 34.4h vs. weekday 4.5h — a 7.6x penalty.
- **Workload concentration**: Dominik Vleming handles 98.7% of tickets. The remaining 1 agent(s) handle the rest.

### Proposed Solutions

1. **Backlog sprint**: Dedicate 2-3 hours per week specifically to clearing the 102 open tickets until the open rate drops below 15%.
2. **Weekend coverage**: Include Sales/Membership - Sales in weekend on-call rotation, or deploy the weekend auto-acknowledgment template to set expectations for Saturday/Sunday submissions.
3. **Create macros for common topics**: The top tags (membership) indicate recurring question types. Build Zendesk macros with pre-written responses for these topics to reduce handling time.

---

## Sales/Membership - Chapters

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

---

## IT-Operations

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

---

## Accounting

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

---

## Membership Engagement

**Severity: MEDIUM** | 72 tickets | 15 open (20.8%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | 7.9h | 4.0x |
| Resolution (median) | 30.2d | 1.5x |
| Zero-Reply Rate | 1.4% | Below org (3.3%) |
| Avg Comments/Ticket | 5.3 | — |
| Multi-Touch Rate | 94.4% | — |
| Automation Eligible | 1 (1.4%) | — |
| Unassigned | 0 | — |
| Stale (>7d no activity) | 6 | — |

### Status Breakdown

- **closed**: 40 (55.6%)
- **solved**: 17 (23.6%)
- **pending**: 11 (15.3%)
- **open**: 4 (5.6%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Megan Czaplinski | 61 | 11 (18.0%) | 8.5 | 0 (0.0%) |
| Dominik Vleming | 8 | 3 (37.5%) | 1.0 | 1 (12.5%) |
| Eileen Sciarra | 3 | 1 (33.3%) | 4.6 | 0 (0.0%) |

**Agent comment volume** (from comments.csv): 
Megan Czaplinski: 170, Dominik Vleming: 70, Eileen Sciarra: 15, Morning Ellergrace: 9, Katlyn Wright: 8, Wendy Adkinson: 4, Jacob Wicklund: 2, Rodoula Vasila: 2, Addison Young: 1, Daniele Catteddu: 1

### Top Tags

`sales-membership` (63), `membership` (60), `skip_css` (59), `sales` (56), `pending_followup_1` (51), `pending_followup_solve` (42), `it` (6), `web_widget` (3), `system_email_notification_failure` (2), `internal-requests` (2)

### Top Subject Keywords

*inquiry* (59), *membership* (57), *individual* (6), *contributor* (6), *information* (6), *training* (4), *cloud* (3), *native* (2), *private* (2), *interested* (2)

### Identified Patterns

- **Growing backlog**: 15 open tickets (20.8%). Without intervention, this queue will become a bottleneck.
- **Stale tickets**: 6 tickets have had no activity in over 7 days (0 over 30 days).
- **Slow response**: Median first response of 7.9h, which is 4.0x the org-wide median of 2.0h.
- **Weekend gap**: Weekend response is 44.5h vs. weekday 7.2h — a 6.2x penalty.
- **Above-average resolution time**: 30.2 days vs. org median of 20.0d.
- **Workload concentration**: Megan Czaplinski handles 84.7% of tickets. The remaining 2 agent(s) handle the rest.
- **High-touch queue**: 94.4% of tickets require more than 2 comments to resolve, indicating complex or multi-step issues.

### Proposed Solutions

1. **Backlog sprint**: Dedicate 2-3 hours per week specifically to clearing the 15 open tickets until the open rate drops below 15%.
2. **Weekend coverage**: Include Membership Engagement in weekend on-call rotation, or deploy the weekend auto-acknowledgment template to set expectations for Saturday/Sunday submissions.
3. **Create macros for common topics**: The top tags (membership, star) indicate recurring question types. Build Zendesk macros with pre-written responses for these topics to reduce handling time.
4. **Improve first-contact resolution**: 94.4% of tickets need 3+ comments. Review the most common multi-touch tickets and update macros or help center articles to provide complete answers upfront.

---

## Sales/Membership - Training

**Severity: MEDIUM** | 29 tickets | 2 open (6.9%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | 21.0h | 10.5x |
| Resolution (median) | 20.7d | 1.0x |
| Zero-Reply Rate | 0.0% | Below org (3.3%) |
| Avg Comments/Ticket | 4.3 | — |
| Multi-Touch Rate | 89.7% | — |
| Automation Eligible | 1 (3.4%) | — |
| Unassigned | 0 | — |
| Stale (>7d no activity) | 2 | — |

### Status Breakdown

- **closed**: 15 (51.7%)
- **solved**: 12 (41.4%)
- **hold**: 1 (3.4%)
- **open**: 1 (3.4%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Tara Hanson | 15 | 1 (6.7%) | 18.9 | 0 (0.0%) |
| Rick Blue | 14 | 1 (7.1%) | 41.9 | 0 (0.0%) |

**Agent comment volume** (from comments.csv): 
Tara Hanson: 23, Rick Blue: 21, Wendy Adkinson: 14, Rodoula Vasila: 12, Katlyn Wright: 8, Morning Ellergrace: 2

### Top Tags

`skip_css` (26), `sales-membership` (23), `credly` (8), `web_widget` (5), `pending_followup_1` (4), `pending_followup_solve` (4), `it` (2), `training` (1), `info-in` (1), `ccak` (1)

### Top Subject Keywords

*training* (13), *review* (12), *aicm* (12), *materials* (9), *invitation* (8), *contributors* (8), *needed* (8), *interested* (8), *trainer* (8), *course* (7)

### Satisfaction

- **Good**: 2 | **Bad**: 0 | **Offered (no response)**: 22
- Response rate: 8.3%

### Identified Patterns

- **Stale tickets**: 2 tickets have had no activity in over 7 days (0 over 30 days).
- **Slow response**: Median first response of 21.0h, which is 10.5x the org-wide median of 2.0h.
- **Weekend gap**: Weekend response is 68.5h vs. weekday 15.8h — a 4.3x penalty.
- **High-touch queue**: 89.7% of tickets require more than 2 comments to resolve, indicating complex or multi-step issues.

### Proposed Solutions

1. **Set first-response SLA**: Configure a Zendesk SLA policy for Sales/Membership - Training with a first-response target appropriate to severity (recommended: 4h for high priority, 8 business hours for normal). Enable breach notifications to the group lead.
2. **Improve first-contact resolution**: 89.7% of tickets need 3+ comments. Review the most common multi-touch tickets and update macros or help center articles to provide complete answers upfront.

---

## IT-Development

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

---

## IT-Operations-Projects

**Severity: HIGH** | 28 tickets | 24 open (85.7%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | 6.5h | 3.2x |
| Resolution (median) | 44.1d | 2.2x |
| Zero-Reply Rate | 14.3% | Above org (3.3%) |
| Avg Comments/Ticket | 8.1 | — |
| Multi-Touch Rate | 89.3% | — |
| Automation Eligible | 2 (7.1%) | — |
| Unassigned | 9 | — |
| Stale (>7d no activity) | 9 | — |

### Status Breakdown

- **open**: 16 (57.1%)
- **hold**: 8 (28.6%)
- **solved**: 3 (10.7%)
- **closed**: 1 (3.6%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Nekoashi Wolf | 11 | 10 (90.9%) | 6.7 | 3 (27.3%) |
| Jacob Wicklund | 4 | 1 (25.0%) | 4.2 | 1 (25.0%) |
| Ryan Bergsma | 4 | 4 (100.0%) | 11.3 | 0 (0.0%) |

**Agent comment volume** (from comments.csv): 
Jacob Wicklund: 53, Kurt S: 49, Ryan Bergsma: 29, Nekoashi Wolf: 26, Kaitlin Morgan: 21, Joshua Buker: 11, Madison Hopkins: 6, Addison Young: 6, Hannah Rock: 4, Courtney Stiven: 4

### Top Tags

`skip_css` (25), `it` (22), `internal-requests` (18), `closed_by_merge` (1), `system_email_notification_failure` (1), `do_close` (1), `do_closed` (1), `edge_case` (1), `redacted_content` (1), `followup_today` (1)

### Top Subject Keywords

*cloudsecurityalliance* (6), *github* (4), *project* (3), *ops* (3), *csa* (3), *org* (3), *create* (3), *data* (2), *review* (2), *calendar* (2)

### Identified Patterns

- **Severe backlog**: 24 tickets remain open (85.7%), far above the org average. The queue is accumulating faster than it's being cleared.
- **Stale tickets**: 9 tickets have had no activity in over 7 days (0 over 30 days).
- **Slow response**: Median first response of 6.5h, which is 3.2x the org-wide median of 2.0h.
- **Weekend gap**: Weekend response is 27.7h vs. weekday 4.2h — a 6.6x penalty.
- **Above-average resolution time**: 44.1 days vs. org median of 20.0d.
- **High zero-reply rate**: 14.3% of tickets have no public response (4 tickets). Requesters are being ignored.
- **Agent bottleneck — Nekoashi Wolf**: 10 open out of 11 assigned (90.9% open rate).
- **High-touch queue**: 89.3% of tickets require more than 2 comments to resolve, indicating complex or multi-step issues.
- **Unassigned tickets**: 9 tickets have no agent assigned.

### Proposed Solutions

1. **Immediate triage**: Schedule a dedicated session to review all 24 open tickets. Close stale/resolved tickets, re-assign active ones, and escalate blocked tickets. Target: reduce open rate to under 25% within 2 weeks.
2. **Mandatory reply before close**: Add a Zendesk requirement that at least one public comment must exist before a ticket can be marked solved. This ensures every requester gets a response.
3. **Weekend coverage**: Include IT-Operations-Projects in weekend on-call rotation, or deploy the weekend auto-acknowledgment template to set expectations for Saturday/Sunday submissions.
4. **Process review**: Resolution time of 44.1d indicates process bottlenecks (approvals, external dependencies, unclear ownership). Map the end-to-end workflow, identify where tickets stall, and set internal checkpoints at 7-day and 14-day marks.
5. **Fix routing**: 9 tickets have no agent. Create a catch-all assignment rule: any ticket unassigned after 30 minutes auto-assigns to the group's on-duty agent.
6. **Redistribute Nekoashi Wolf's queue**: 10 open tickets cannot be cleared by one person. Redistribute across available agents in the group or pull in cross-trained agents from adjacent teams.
7. **Create macros for common topics**: The top tags (membership) indicate recurring question types. Build Zendesk macros with pre-written responses for these topics to reduce handling time.
8. **Improve first-contact resolution**: 89.3% of tickets need 3+ comments. Review the most common multi-touch tickets and update macros or help center articles to provide complete answers upfront.

---

## Sales/Membership - Partners and Instructors

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

---

## Sales/Membership

**Severity: HIGH** | 15 tickets | 7 open (46.7%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | 18.7h | 9.3x |
| Resolution (median) | 27.1d | 1.4x |
| Zero-Reply Rate | 0.0% | Below org (3.3%) |
| Avg Comments/Ticket | 5.2 | — |
| Multi-Touch Rate | 73.3% | — |
| Automation Eligible | 0 (0.0%) | — |
| Unassigned | 0 | — |
| Stale (>7d no activity) | 4 | — |

### Status Breakdown

- **open**: 6 (40.0%)
- **closed**: 6 (40.0%)
- **solved**: 2 (13.3%)
- **pending**: 1 (6.7%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Dominik Vleming | 6 | 4 (66.7%) | 42.4 | 0 (0.0%) |
| Eileen Sciarra | 4 | 2 (50.0%) | 16.7 | 0 (0.0%) |
| Megan Czaplinski | 4 | 1 (25.0%) | 23.3 | 0 (0.0%) |
| Tara Hanson | 1 | 0 (0.0%) | 21.9 | 0 (0.0%) |

**Agent comment volume** (from comments.csv): 
Megan Czaplinski: 13, Rodoula Vasila: 12, Dominik Vleming: 10, Eileen Sciarra: 6, Katlyn Wright: 6, Morning Ellergrace: 2, Paige McKenna: 2, Wendy Adkinson: 2, Andy Ruth: 1, Anna McKee (Schorr): 1

### Top Tags

`skip_css` (9), `pending_followup_1` (5), `pending_followup_solve` (5), `sales-membership` (4), `web_widget` (3), `training` (2), `star` (2), `it` (2), `sales` (1), `logo` (1)

### Top Subject Keywords

*training* (8), *inquiry* (5), *private* (4), *details* (3), *security* (3), *service* (2), *cloud* (2), *request* (1), *add* (1), *logo* (1)

### Satisfaction

- **Good**: 2 | **Bad**: 0 | **Offered (no response)**: 7
- Response rate: 22.2%

### Identified Patterns

- **Growing backlog**: 7 open tickets (46.7%). Without intervention, this queue will become a bottleneck.
- **Stale tickets**: 4 tickets have had no activity in over 7 days (0 over 30 days).
- **Slow response**: Median first response of 18.7h, which is 9.3x the org-wide median of 2.0h.
- **High-touch queue**: 73.3% of tickets require more than 2 comments to resolve, indicating complex or multi-step issues.

### Proposed Solutions

1. **Backlog sprint**: Dedicate 2-3 hours per week specifically to clearing the 7 open tickets until the open rate drops below 15%.
2. **Set first-response SLA**: Configure a Zendesk SLA policy for Sales/Membership with a first-response target appropriate to severity (recommended: 4h for high priority, 8 business hours for normal). Enable breach notifications to the group lead.
3. **Create macros for common topics**: The top tags (star, membership) indicate recurring question types. Build Zendesk macros with pre-written responses for these topics to reduce handling time.
4. **Improve first-contact resolution**: 73.3% of tickets need 3+ comments. Review the most common multi-touch tickets and update macros or help center articles to provide complete answers upfront.

---

## IT-Security

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

---

## Support Tasks

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

---

## Kurt's Task List

**Severity: LOW** | 7 tickets | 2 open (28.6%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | No data | — |
| Resolution (median) | 10.4d | 0.5x (better) |
| Zero-Reply Rate | 0.0% | Below org (3.3%) |
| Avg Comments/Ticket | 2.7 | — |
| Multi-Touch Rate | 57.1% | — |
| Automation Eligible | 0 (0.0%) | — |
| Unassigned | 2 | — |
| Stale (>7d no activity) | 2 | — |

### Status Breakdown

- **solved**: 5 (71.4%)
- **new**: 2 (28.6%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Kurt S | 5 | 0 (0.0%) | — | 0 (0.0%) |

**Agent comment volume** (from comments.csv): 
Kurt S: 17, Nekoashi Wolf: 1

### Top Tags

`internal-requests` (7), `it` (7), `skip_css` (6)

### Top Subject Keywords

*org* (6), *cloudsecurityalliance* (5), *setup* (3), *dns* (2), *pod* (2), *admin* (2), *internal* (2), *csa* (2), *hive* (2), *mailgun* (1)

### Identified Patterns

- **Growing backlog**: 2 open tickets (28.6%). Without intervention, this queue will become a bottleneck.
- **Stale tickets**: 2 tickets have had no activity in over 7 days (0 over 30 days).
- **No response data**: First response time is null or zero, suggesting tickets may enter this queue without an initial reply being tracked.
- **High-touch queue**: 57.1% of tickets require more than 2 comments to resolve, indicating complex or multi-step issues.
- **Unassigned tickets**: 2 tickets have no agent assigned.

### Proposed Solutions

1. **Backlog sprint**: Dedicate 2-3 hours per week specifically to clearing the 2 open tickets until the open rate drops below 15%.

---

## Marketing - Events

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

---

## Operations Excellence

**Severity: MEDIUM** | 4 tickets | 2 open (50.0%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | 18.9h | 9.4x |
| Resolution (median) | 55.5d | 2.8x |
| Zero-Reply Rate | 0.0% | Below org (3.3%) |
| Avg Comments/Ticket | 9.8 | — |
| Multi-Touch Rate | 100.0% | — |
| Automation Eligible | 0 (0.0%) | — |
| Unassigned | 0 | — |
| Stale (>7d no activity) | 2 | — |

### Status Breakdown

- **open**: 2 (50.0%)
- **closed**: 1 (25.0%)
- **solved**: 1 (25.0%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Dominik Vleming | 2 | 1 (50.0%) | 18.9 | 0 (0.0%) |
| John DiMaria | 2 | 1 (50.0%) | — | 0 (0.0%) |

**Agent comment volume** (from comments.csv): 
Jacob Wicklund: 12, Dominik Vleming: 11, Madison Hopkins: 5, John DiMaria: 4, Ryan Bergsma: 4, Rodoula Vasila: 2, Hannah Rock: 1

### Top Tags

`skip_css` (4), `it` (3), `nc-reg_audit` (1), `not_applicable` (1), `qms` (1), `yes` (1), `internal-requests` (1)

### Top Subject Keywords

*automation* (1), *errors* (1), *marketing* (1), *airtable* (1), *base* (1), *finding* (1), *number* (1), *oct* (1), *bsi* (1), *audit* (1)

### Identified Patterns

- **Growing backlog**: 2 open tickets (50.0%). Without intervention, this queue will become a bottleneck.
- **Stale tickets**: 2 tickets have had no activity in over 7 days (0 over 30 days).
- **Slow response**: Median first response of 18.9h, which is 9.4x the org-wide median of 2.0h.
- **Above-average resolution time**: 55.5 days vs. org median of 20.0d.
- **High-touch queue**: 100.0% of tickets require more than 2 comments to resolve, indicating complex or multi-step issues.

### Proposed Solutions

1. **Backlog sprint**: Dedicate 2-3 hours per week specifically to clearing the 2 open tickets until the open rate drops below 15%.
2. **Set first-response SLA**: Configure a Zendesk SLA policy for Operations Excellence with a first-response target appropriate to severity (recommended: 4h for high priority, 8 business hours for normal). Enable breach notifications to the group lead.
3. **Process review**: Resolution time of 55.5d indicates process bottlenecks (approvals, external dependencies, unclear ownership). Map the end-to-end workflow, identify where tickets stall, and set internal checkpoints at 7-day and 14-day marks.
4. **Improve first-contact resolution**: 100.0% of tickets need 3+ comments. Review the most common multi-touch tickets and update macros or help center articles to provide complete answers upfront.

---

## Research and Development - STAR

**Severity: LOW** | 2 tickets | 1 open (50.0%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | No data | — |
| Resolution (median) | 86.9d | 4.3x |
| Zero-Reply Rate | 0.0% | Below org (3.3%) |
| Avg Comments/Ticket | 4.5 | — |
| Multi-Touch Rate | 50.0% | — |
| Automation Eligible | 0 (0.0%) | — |
| Unassigned | 0 | — |
| Stale (>7d no activity) | 1 | — |

### Status Breakdown

- **closed**: 1 (50.0%)
- **open**: 1 (50.0%)

### Agent Performance

| Agent | Tickets | Open (%) | Response (h) | Zero-Reply (%) |
|---|---|---|---|---|
| Andy Ruth | 2 | 1 (50.0%) | — | 0 (0.0%) |

**Agent comment volume** (from comments.csv): 
Morning Ellergrace: 3, Andy Ruth: 1, Katlyn Wright: 1, Lefteris Skoutaris: 1, Marina Bregkou: 1

### Top Tags

`cto` (1), `skip_css` (1), `it` (1)

### Top Subject Keywords

*star* (1), *submission* (1), *oqikcg* (1), *sustainableevolution* (1), *com* (1), *fwd* (1), *aicm* (1), *iso* (1), *mapping* (1)

### Identified Patterns

- **Growing backlog**: 1 open tickets (50.0%). Without intervention, this queue will become a bottleneck.
- **Stale tickets**: 1 tickets have had no activity in over 7 days (0 over 30 days).
- **No response data**: First response time is null or zero, suggesting tickets may enter this queue without an initial reply being tracked.
- **Very slow resolution**: Median resolution of 86.9 days — 4.3x the org average of 20.0d. Tickets stall in this queue.

### Proposed Solutions

1. **Backlog sprint**: Dedicate 2-3 hours per week specifically to clearing the 1 open tickets until the open rate drops below 15%.
2. **Process review**: Resolution time of 86.9d indicates process bottlenecks (approvals, external dependencies, unclear ownership). Map the end-to-end workflow, identify where tickets stall, and set internal checkpoints at 7-day and 14-day marks.

---

## IT-Operations-Tasks

**Severity: MEDIUM** | 1 tickets | 1 open (100.0%)

### Key Metrics

| Metric | Value | vs. Org Baseline |
|---|---|---|
| First Response (median) | 2.5h | 1.2x |
| Resolution (median) | No data | — |
| Zero-Reply Rate | 0.0% | Below org (3.3%) |
| Avg Comments/Ticket | 3.0 | — |
| Multi-Touch Rate | 100.0% | — |
| Automation Eligible | 0 (0.0%) | — |
| Unassigned | 1 | — |
| Stale (>7d no activity) | 1 | — |

### Status Breakdown

- **open**: 1 (100.0%)

### Top Tags

`internal-requests` (1), `it` (1)

### Top Subject Keywords

*action* (1), *required* (1), *reauthorize* (1), *probackup* (1), *airtable* (1)

### Identified Patterns

- **Severe backlog**: 1 tickets remain open (100.0%), far above the org average. The queue is accumulating faster than it's being cleared.
- **Stale tickets**: 1 tickets have had no activity in over 7 days (0 over 30 days).
- **High-touch queue**: 100.0% of tickets require more than 2 comments to resolve, indicating complex or multi-step issues.
- **Unassigned tickets**: 1 tickets have no agent assigned.

### Proposed Solutions

1. **Immediate triage**: Schedule a dedicated session to review all 1 open tickets. Close stale/resolved tickets, re-assign active ones, and escalate blocked tickets. Target: reduce open rate to under 25% within 2 weeks.
2. **Improve first-contact resolution**: 100.0% of tickets need 3+ comments. Review the most common multi-touch tickets and update macros or help center articles to provide complete answers upfront.

---
