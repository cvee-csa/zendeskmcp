# CSA Zendesk: Proposed Actionable Items

**Generated:** March 13, 2026
**Data Source:** 3,607 tickets from tickets.csv, ticket_metrics.csv, comments.csv, agents.csv, groups.csv, tags.csv
**Analysis Period:** 2023-10-27 to 2026-03-13

---

## How to Read This Report

Each action item includes:
- **Severity**: CRITICAL / HIGH / MEDIUM / LOW
- **Evidence**: Data points from the CSV analysis that justify the action
- **Proposed Action**: Specific steps to take
- **Owner**: Suggested responsible party or team
- **Effort**: S (days) / M (1-2 weeks) / L (weeks-months)
- **Expected Impact**: What improvement to expect

---

## ACTION 1: Resolve the Chapters Queue Crisis

| Field | Detail |
|---|---|
| **Severity** | CRITICAL |
| **Evidence** | 169 total tickets. 120 open (71.0%). Median first response: **2,474 hours** (~103 days). Median resolution: **122.8 days**. Sole assignee: Billy Toney (168 tickets, 119 open, 70.8% open rate). Only 39 comments written by this agent across all tickets. |
| **Root Cause** | Single point of failure — one agent assigned to an entire queue with no backup, no escalation path, and no SLA enforcement. This is a structural staffing problem, not a performance problem. |
| **Proposed Action** | 1. Immediately triage all 120 open Chapters tickets: close stale/abandoned, re-route active ones. 2. Assign 1-2 additional agents from Sales/Membership to share the Chapters load. 3. Set up a round-robin or load-balanced assignment rule for the Chapters group. 4. Establish a 24-hour first-response SLA for this queue with manager alerts. |
| **Owner** | Sales/Membership Director + Support Operations Manager |
| **Effort** | S — Triage can start immediately; staffing adjustment within 1 week |
| **Expected Impact** | Eliminate the 103-day response time. Reduce Chapters open rate from 71% to under 20%. Prevent member/chapter attrition from unanswered inquiries. |

## ACTION 2: Establish Weekend Response Coverage

| Field | Detail |
|---|---|
| **Severity** | HIGH |
| **Evidence** | Weekday median response: **1.3 hours**. Weekend median response: **29.3 hours** — a **22.5x penalty**. 379 tickets created on weekends. Statistically significant (Mann-Whitney p < 0.0001 from prior analysis). The gap is driven by zero staffing, not volume surge. |
| **Root Cause** | No agents are scheduled for weekend shifts. Tickets submitted Friday evening through Sunday sit untouched until Monday morning. |
| **Proposed Action** | 1. Implement a weekend on-call rotation (2-3 agents, rotating weekly). 2. Deploy auto-responder for weekend submissions acknowledging receipt and setting expectations. 3. Set a weekend-specific SLA target: first response within 8 hours. 4. Prioritize high-urgency tickets for weekend triage using tags or priority fields. |
| **Owner** | IT-Support Team Lead + HR (for scheduling) |
| **Effort** | M — requires policy change and schedule negotiation |
| **Expected Impact** | Reduce weekend response time from 29.3h to under 8h. Improve overall P90 response time (currently 34.6h) by 30-40%. |

## ACTION 3: Rebalance Agent Workload Distribution

| Field | Detail |
|---|---|
| **Severity** | HIGH |
| **Evidence** | Gini coefficient: **0.745** (severe inequality). Top 3 agents handle 64.2% of all tickets: Rodoula Vasila (1,201), Wendy Adkinson (640), Dominik Vleming (474). Remaining 65 agents handle the other 1,292 tickets. Rodoula alone handles 33.3% of total volume. |
| **Root Cause** | Assignment rules concentrate tickets on a few agents. No workload caps or overflow routing exist. |
| **Proposed Action** | 1. Implement capacity-based routing: set max active tickets per agent (e.g., 50 open tickets triggers overflow). 2. Cross-train 5-10 agents on IT-Support and Sales/Membership workflows. 3. Redistribute Dominik Vleming's 107 open tickets — membership inquiries can be shared with Sales team. 4. Review and update auto-assignment rules to use round-robin with skill-based routing. |
| **Owner** | Support Operations Manager |
| **Effort** | M — routing rule changes + cross-training plan |
| **Expected Impact** | Reduce Gini coefficient from 0.745 to under 0.5. Prevent burnout of top agents. Create redundancy against single-agent failures (as seen with Chapters). |

## ACTION 4: Expand Ticket Automation

| Field | Detail |
|---|---|
| **Severity** | HIGH |
| **Evidence** | 698 tickets (19.4%) already tagged with automation markers (do_close, do_closed, auto_solved, non-actionable, spam, closed_by_merge). 669 tickets routed to the 'Non-actionable' group. Top tag: 'do_close' at 645 occurrences. Many of these still require manual agent touch to close. |
| **Root Cause** | Automation rules tag tickets but do not always close or resolve them automatically. Manual intervention is still required for tickets that need no human response. |
| **Proposed Action** | 1. Configure Zendesk triggers to auto-solve tickets tagged 'do_close', 'do_closed', or 'non-actionable' after 1 hour with no customer reply. 2. Auto-close spam-tagged tickets immediately. 3. Build macros for the top 5 recurring ticket types (password resets, membership inquiries, certificate questions). 4. Implement satisfaction survey bypass for auto-closed tickets. 5. Target: increase automation rate from 19.4% to 35%+ of total volume. |
| **Owner** | Zendesk Administrator + IT-Support Team Lead |
| **Effort** | S — trigger/automation rule configuration |
| **Expected Impact** | Free up ~500 agent-touches per month. Reduce average queue depth by 15-20%. Allow agents to focus on complex, high-value tickets. |

## ACTION 5: Fix Accounting Group Resolution Process

| Field | Detail |
|---|---|
| **Severity** | HIGH |
| **Evidence** | 113 tickets, 18 open (15.9%). Median resolution: **79.4 days** — 4x the org-wide average. No first-response data available (null), suggesting tickets enter this queue without an initial reply. 3 tickets have zero public comments. Most tickets are multi-touch, requiring back-and-forth over weeks. |
| **Root Cause** | This is a process problem: accounting workflows (invoice disputes, refunds, payment questions) inherently require external approvals, which stall ticket progress. There is no defined SLA or escalation for financial tickets. |
| **Proposed Action** | 1. Create a dedicated accounting SLA: first response within 4 hours, resolution target 14 business days. 2. Add internal status tags (e.g., 'awaiting-approval', 'awaiting-payment') to track stalled tickets. 3. Set 7-day auto-follow-up for tickets in pending/hold. 4. Assign a secondary agent to handle accounting overflow during Christina Lehman's absence. 5. Build a small FAQ/macro set for common accounting questions (invoice lookup, refund policy, payment terms). |
| **Owner** | Finance Team + Christina Lehman + Support Ops |
| **Effort** | M — process redesign + SLA implementation |
| **Expected Impact** | Reduce resolution time from 79.4 days to under 21 days. Improve requester experience for financial issues. |

## ACTION 6: Enforce Ticket Priority Classification

| Field | Detail |
|---|---|
| **Severity** | MEDIUM |
| **Evidence** | 3,554 of 3,607 tickets (98.5%) have no priority set. Only 44 marked 'normal', 8 'high', 1 'urgent'. Without priority data, SLA enforcement, escalation rules, and triage decisions are impossible. |
| **Root Cause** | Priority is not a required field on ticket creation. No auto-classification rules exist. Agents rarely set it manually. |
| **Proposed Action** | 1. Make priority a required field for all new tickets (via Zendesk form configuration). 2. Create auto-priority rules based on keywords: 'urgent', 'down', 'broken', 'security' → High/Urgent. 3. Default unclassified tickets to 'Normal'. 4. For web widget/email channels, use triggers to infer priority from subject line patterns. 5. Retroactively classify open tickets by age (> 7 days unresolved → escalate priority). |
| **Owner** | Zendesk Administrator |
| **Effort** | S — form configuration + trigger rules |
| **Expected Impact** | Enable SLA enforcement for the first time. Support triage-based routing. Provide data for future capacity planning. |

## ACTION 7: Eliminate Zero-Reply Tickets

| Field | Detail |
|---|---|
| **Severity** | MEDIUM |
| **Evidence** | 118 tickets (3.3%) have zero public comments. IT-Support accounts for 69 of these, IT-Operations for 35. IT-Operations has a 21.9% zero-reply rate. Jacob Wicklund has a 22.1% zero-reply rate across 77 tickets. |
| **Root Cause** | Some tickets are resolved internally (e.g., system fixes) without communicating back to the requester. Others fall through assignment cracks. IT-Operations tickets often involve infrastructure work where agents fix issues but don't close the loop. |
| **Proposed Action** | 1. Create a 'resolved without reply' macro that auto-sends a brief closure message to the requester. 2. Set a Zendesk automation: if a ticket has 0 public comments after 48 hours, alert the assigned agent and their manager. 3. Add a team-level KPI: zero-reply rate must stay under 5%. 4. For IT-Operations specifically: require a resolution note before marking solved. |
| **Owner** | IT-Support Team Lead + IT-Operations Manager |
| **Effort** | S — macro creation + automation rule |
| **Expected Impact** | Reduce zero-reply rate from 3.3% to under 1%. Improve customer satisfaction and transparency. |

## ACTION 8: Clear and Prevent Unassigned Tickets

| Field | Detail |
|---|---|
| **Severity** | MEDIUM |
| **Evidence** | 86 tickets (2.4%) have no assigned agent. 2 tickets have no group assignment at all. Unassigned tickets have no one accountable for their resolution. |
| **Root Cause** | Some channels (web widget, API) create tickets without triggering assignment rules. Group-level assignment doesn't always cascade to an individual agent. |
| **Proposed Action** | 1. Immediately triage all 86 unassigned tickets: assign or close. 2. Create a catch-all assignment trigger: any ticket unassigned after 30 minutes gets auto-assigned to the group's on-duty agent. 3. Add an 'Unassigned' view to Zendesk for daily monitoring by team leads. 4. Set a daily automated report of unassigned ticket count sent to Support Ops. |
| **Owner** | Support Operations Manager |
| **Effort** | S — triage + trigger configuration |
| **Expected Impact** | Eliminate unassigned tickets entirely. Ensure every ticket has an accountable owner within 30 minutes of creation. |

## ACTION 9: Improve Satisfaction Survey Response Rate

| Field | Detail |
|---|---|
| **Severity** | MEDIUM |
| **Evidence** | 1,719 surveys offered, only 260 responses (15.1% response rate). 250 good, 10 bad (96.2% satisfaction among respondents). 1628 tickets received no survey at all. The 15.1% response rate provides limited signal. |
| **Root Cause** | Default Zendesk CSAT prompt has low engagement. Surveys are only offered on solved tickets, missing hold/pending resolutions. Timing may not be optimal. |
| **Proposed Action** | 1. Customize the CSAT survey email with CSA branding and a simpler one-click rating. 2. Ensure surveys are sent on all resolved tickets (not just 'solved' status). 3. Add a follow-up survey prompt 24 hours after resolution. 4. For 'bad' ratings, auto-trigger a follow-up from a team lead to recover the relationship. 5. Track CSAT by group and agent as a team KPI. |
| **Owner** | Support Operations Manager + Zendesk Admin |
| **Effort** | S — survey configuration + reporting setup |
| **Expected Impact** | Increase response rate from 15% to 30%+. Gain statistically meaningful satisfaction data for group- and agent-level coaching. |

## ACTION 10: Clean Up Stale Project and Task Queues

| Field | Detail |
|---|---|
| **Severity** | MEDIUM |
| **Evidence** | **Support Tasks**: 13 tickets, 8 open (61.5%), median resolution 168.2 days. **IT-Operations-Projects**: 28 tickets, 16 open (57.1%), median resolution 44.1 days, 14.3% zero-reply rate. **Sales/Membership - Partners and Instructors**: 17 tickets, 10 open (58.8%). **Marketing - Events**: 5 tickets, 3 open (60%). These low-volume queues accumulate stale tickets with no urgency. |
| **Root Cause** | These queues are used as informal task trackers rather than support queues. No SLA applies, and no one reviews them regularly. Tickets linger indefinitely. |
| **Proposed Action** | 1. Conduct a one-time audit of all open tickets in these 4 queues — close completed or abandoned tickets. 2. Decide per queue: should this be a Zendesk group or should tasks move to a project management tool (Jira, Asana, etc.)? 3. For queues that remain, set a 30-day auto-close rule for tickets with no activity. 4. Assign a queue owner responsible for weekly reviews. |
| **Owner** | IT Director + respective team leads |
| **Effort** | S — audit and policy decision |
| **Expected Impact** | Close 30-40 stale tickets. Reduce noise in Zendesk reporting. Improve data accuracy for SLA metrics. |

## ACTION 11: Standardize and Consolidate Tagging Taxonomy

| Field | Detail |
|---|---|
| **Severity** | LOW |
| **Evidence** | 224 unique tags across 3,607 tickets. Significant overlap detected: 'do_close' and 'do_closed' serve the same purpose. Tags like 'level1' (72) and 'level2' (82) are ambiguous. Multiple product tags exist (ccsk: 320, taise: 334, star: 332, bundle: 417) without consistent naming. 'pending_followup_1' (241) and 'pending_followup_solve' (209) could be consolidated. |
| **Root Cause** | Tags were added organically over time without a governance policy. No tag dictionary or standards document exists. |
| **Proposed Action** | 1. Create a tag governance document defining approved tags, their purpose, and when to use each. 2. Merge duplicates: 'do_close' + 'do_closed' → 'auto-close'. 3. Create namespaced tags for products: 'product:ccsk', 'product:star', 'product:taise'. 4. Replace ambiguous tags ('level1', 'level2') with descriptive alternatives ('escalation:tier1', 'escalation:tier2'). 5. Restrict tag creation to admins; agents select from approved list. |
| **Owner** | Zendesk Administrator |
| **Effort** | M — requires tag audit, migration, and policy documentation |
| **Expected Impact** | Cleaner automation rules. More accurate reporting. Easier onboarding for new agents. Improved tag-based routing reliability. |

## ACTION 12: Implement Tiered SLA Policy

| Field | Detail |
|---|---|
| **Severity** | HIGH |
| **Evidence** | No formal SLA exists today. Response times range from 0.3 hours (Wendy Adkinson) to 2,474 hours (Chapters queue). Without SLAs, there are no breach alerts, no escalation triggers, and no accountability framework. The data supports the following baseline SLA tiers: |

**Proposed SLA Tiers (based on current performance data):**

| Priority | First Response | Next Response | Resolution Target |
|---|---|---|---|
| Urgent | 1 hour | 2 hours | 4 hours |
| High | 4 hours | 8 hours | 1 business day |
| Normal | 8 business hours | 24 hours | 5 business days |
| Low | 24 business hours | 48 hours | 10 business days |

| **Proposed Action** | 1. Configure Zendesk SLA policies with the tiers above. 2. Set up breach notifications: warn at 75% of target, alert at 100%, escalate to manager at 150%. 3. Exempt 'Non-actionable' and auto-close tickets from SLA measurement. 4. Create an SLA compliance dashboard for weekly team review. 5. Start with 'observe mode' (track but don't enforce) for 30 days, then enforce. |
| **Owner** | VP of Operations + Support Operations Manager |
| **Effort** | M — policy design + Zendesk SLA configuration + team communication |
| **Expected Impact** | Establish measurable accountability. Catch breaches before they become crises (e.g., the Chapters situation). Provide data-driven basis for staffing decisions. |

---

## Priority Execution Matrix

| # | Action | Severity | Effort | Quick Win? |
|---|---|---|---|---|
| 1 | Resolve Chapters Queue Crisis | CRITICAL | S | Yes |
| 2 | Establish Weekend Coverage | HIGH | M | No |
| 3 | Rebalance Agent Workload | HIGH | M | No |
| 4 | Expand Ticket Automation | HIGH | S | Yes |
| 5 | Fix Accounting Resolution Process | HIGH | M | No |
| 6 | Enforce Priority Classification | MEDIUM | S | Yes |
| 7 | Eliminate Zero-Reply Tickets | MEDIUM | S | Yes |
| 8 | Clear Unassigned Tickets | MEDIUM | S | Yes |
| 9 | Improve Satisfaction Surveys | MEDIUM | S | Yes |
| 10 | Clean Up Stale Queues | MEDIUM | S | Yes |
| 11 | Standardize Tags | LOW | M | No |
| 12 | Implement SLA Framework | HIGH | M | No |

**Recommended execution order:** Start with quick wins (Actions 1, 4, 6, 7, 8) to build momentum, then tackle structural changes (Actions 2, 3, 5, 12) in parallel, and finish with the governance items (Actions 9, 10, 11).

---

## Methodology

This report was generated by cross-referencing all CSV data sources exported from CSA's Zendesk environment:

- **tickets.csv**: 3,607 tickets — status, assignment, timestamps, tags, channel
- **ticket_metrics.csv**: 3,594 records — first response time, comment counts
- **comments.csv**: 13,049 comments — agent activity, response patterns
- **agents.csv**: 68 agents — ID-to-name mapping, role, active status
- **groups.csv**: 35 groups — ID-to-name mapping, team structure
- **tags.csv**: 224 unique tags — pre-aggregated counts

Statistical techniques applied: descriptive statistics, Gini coefficient for workload inequality, Mann-Whitney U test for weekend/weekday comparison, tag deduplication and co-occurrence analysis, TF-IDF subject clustering (from prior analysis). All numeric agent and group IDs were resolved to human-readable names via cross-reference with agents.csv and groups.csv.
