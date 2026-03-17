# IT Operations — New Team Member Onboarding Guide

**Cloud Security Alliance — Zendesk Support Environment**
**Last updated:** March 14, 2026

---

## Welcome

This guide gives you everything you need to get productive in CSA's Zendesk environment as an IT Operations team member. It covers how the support system is structured, who does what, what kinds of tickets you'll see, and the tools and workflows you'll use day to day.

---

## 1. How Zendesk Is Organized

CSA's Zendesk instance handles all internal and external support requests. Tickets come in through email, web forms, and API integrations, and are routed to **groups** (teams). Each group has **agents** (people) assigned to it.

### The Groups You Need to Know

There are 19 active groups. As IT-Ops, you'll work primarily in the first three and collaborate with the rest of the IT family:

**Your primary queues:**

| Group | What it handles | Current volume | Open tickets |
|---|---|---|---|
| IT-Operations | Internal IT requests — access provisioning, Slack, website changes, DNS, system tasks | 160 tickets | 28 (17.5%) |
| IT-Operations-Projects | Longer-running IT projects — GitHub org management, data reviews, infrastructure builds | 28 tickets | 24 (85.7%) |
| IT-Operations-Tasks | One-off operational tasks (e.g., reauthorize backups) | 1 ticket | 1 (100%) |

**Related IT queues you'll interact with:**

| Group | What it handles | Volume | Key contact |
|---|---|---|---|
| IT-Support | External-facing support — password resets, account access, exam/cert questions, membership help | 1,796 tickets | Rodoula Vasila, Wendy Adkinson, Katlyn Wright |
| IT-Development | Software development tasks — bug fixes, feature requests, CMS work | 28 tickets | Ryan Bergsma |
| IT-Security | Security reviews, access audits, compliance tasks | 13 tickets | Nekoashi Wolf, Kaitlin Morgan |

**Non-IT groups (for context when tickets get misrouted to you):**

| Group | What it handles | Volume |
|---|---|---|
| Sales/Membership - Sales | Membership inquiries, corporate sales, renewals | 464 tickets |
| Sales/Membership - Chapters | Chapter-specific membership and onboarding | 169 tickets |
| Accounting | Invoices, refunds, payment issues | 113 tickets |
| Membership Engagement | Member outreach and retention | 72 tickets |
| Non-actionable | Auto-closed system notifications, bounces, spam | 669 tickets |

If a ticket lands in your queue that's really a sales, membership, or accounting issue, reassign it to the correct group rather than trying to handle it yourself.

---

## 2. Your Team

These are the agents who work in the IT-Operations group family. You'll work alongside them daily.

| Agent | Email | Role | Primary Group | Tickets | Specialty |
|---|---|---|---|---|---|
| Jacob Wicklund | jwicklund@cloudsecurityalliance.org | Admin | IT-Operations | 77 | Infrastructure, internal requests — handles the most IT-Ops tickets by volume |
| Kaitlin Morgan | kmorgan@cloudsecurityalliance.org | Admin | IT-Operations | 44 | IT-Operations + IT-Security cross-functional |
| Nekoashi Wolf | nwolf@cloudsecurityalliance.org | Admin | IT-Support | 48 | IT-Ops projects, security, and cross-team support |
| Ryan Bergsma | rbergsma@cloudsecurityalliance.org | Admin | IT-Operations | 38 | Development + IT-Ops projects, GitHub and infrastructure |

**IT-Support agents you'll collaborate with frequently:**

| Agent | Email | Tickets | Note |
|---|---|---|---|
| Rodoula Vasila | rvasilas@cloudsecurityalliance.org | 1,201 | Highest-volume agent in the org — handles most IT-Support and non-actionable tickets |
| Wendy Adkinson | wadkinson@cloudsecurityalliance.org | 640 | Fastest median response (0.3h) — IT-Support frontline |
| Katlyn Wright | kwright@cloudsecurityalliance.org | 418 | IT-Support + non-actionable triage |
| Morning Ellergrace | mellergrace@cloudsecurityalliance.org | 158 | IT-Support backup |

---

## 3. What Tickets Look Like

### Common IT-Operations Ticket Types

Based on subject line analysis, these are the recurring request categories you'll see:

**Access & Provisioning** — Requests like "AAS access for [person]", "Grant permission to [tool]", "Create [account/group]". These are the most frequent. Typical turnaround: same day.

**Slack Administration** — Adding people to Slack channels, managing invite URLs, Slack integrations. The "Public Slack Invite URL Checkup" is a recurring scheduled task.

**Website & DNS Changes** — DNS record updates, Cloudflare configurations, redirect setups, CMS access grants. These require care — verify the request with the requester before making changes.

**GitHub & Dev Tools** — Repository access, org ownership questions, CI/CD pipeline issues. Coordinate with Ryan Bergsma for anything involving the GitHub organization.

**Scheduled/Automated Tasks** — Tickets tagged `[AAS.Tasks.ScheduledTask]` are system-generated recurring checks (backup verification, subscription consolidation, URL checkups). These follow a known procedure — ask a teammate for the runbook if it's your first time.

**Internal Requests** — General IT asks from other CSA teams. Tagged with `internal-requests`. These are the bulk of the queue (115 out of 160 tickets carry this tag).

### Tags You'll See Constantly

| Tag | Meaning |
|---|---|
| `it` | General IT tag — on nearly every ticket in your queue |
| `skip_css` | Ticket should skip customer satisfaction survey (internal tickets don't need CSAT) |
| `internal-requests` | Request from a CSA employee, not an external customer |
| `system_email_notification_failure` | Automated alert about an email delivery failure |
| `followup_today` | Flagged for same-day follow-up |
| `closed_by_merge` | This ticket was merged into another — check the parent ticket |
| `do_close` / `do_closed` | Marked for auto-close — no action needed |
| `device` | Hardware-related request |

---

## 4. Key Metrics and What "Good" Looks Like

These are the current performance numbers for IT-Operations. Use them as your benchmark.

| Metric | IT-Operations | Org-wide Average | What to aim for |
|---|---|---|---|
| Median first response | 1.7 hours | 2.0 hours | Under 2 hours |
| Open rate | 17.5% | ~10% | Under 15% |
| Zero-reply rate | 21.9% | 3.3% | Under 5% — always reply before closing |
| Avg comments per ticket | ~2 | 3.6 | At least 1 public comment on every ticket |

**The zero-reply rate is the team's biggest area for improvement.** Currently 21.9% of IT-Ops tickets are closed without any public response to the requester. Even a one-line "This has been taken care of" before closing makes a difference.

---

## 5. Daily Workflow

Here's a recommended daily routine:

**Morning (first 15 minutes):**

1. Open the **IT-Operations** view in Zendesk. Sort by oldest-updated-first.
2. Check for any tickets assigned to you that are older than 2 days — these need attention first.
3. Check the **Unassigned** view — pick up anything that's sitting without an owner.
4. Scan IT-Operations-Projects for any open items that need a status update.

**Throughout the day:**

5. As new tickets come in, triage: can you resolve it in under 5 minutes? Do it now. Otherwise, reply acknowledging receipt and set a realistic timeline.
6. For every ticket you resolve, send a public reply explaining what you did before marking it solved. (This is how we get the zero-reply rate down.)
7. If a ticket belongs in another group (e.g., it's really a membership question or an accounting issue), reassign it immediately. Don't let it age in your queue.

**End of day (last 5 minutes):**

8. Check your open tickets — update any that are waiting on someone else with an internal note so you remember the status tomorrow.
9. Tag anything that needs follow-up tomorrow with `followup_today`.

---

## 6. When Tickets Arrive

Most IT-Operations tickets are created during business hours (US time zones), with a notable concentration in the late afternoon and evening:

| Time Block (UTC) | Volume | Note |
|---|---|---|
| 16:00–23:00 | Heavy | Peak hours — this is when most internal requests come in |
| 13:00–15:00 | Moderate | Post-lunch pickup |
| 00:00–05:00 | Light | Automated scheduled tasks and overnight stragglers |
| 06:00–12:00 | Very light | Quiet morning hours |

This means your queue will be fullest when you check in during the afternoon. Morning is a good time to clear backlog from the previous day.

---

## 7. Tools and Access You'll Need

Before your first day handling tickets, make sure you have:

- [ ] **Zendesk agent account** with access to IT-Operations, IT-Operations-Projects, and IT-Operations-Tasks groups
- [ ] **Slack** — CSA's primary internal communication tool (you'll get tickets about it, and you'll use it to coordinate with teammates)
- [ ] **Cloudflare** — For DNS and website infrastructure changes
- [ ] **GitHub** — CSA organization membership for repo and org management tasks
- [ ] **Google Workspace admin** — For account provisioning and group management
- [ ] **Claude** — CSA uses Claude with a Zendesk MCP integration for ticket analysis. See the [README](../README.md) for setup instructions.

---

## 8. Escalation Path

If you're stuck on a ticket, here's where to go:

| Situation | Escalate to |
|---|---|
| Infrastructure/DNS/Cloudflare issue | Jacob Wicklund or Ryan Bergsma |
| Security-related request | Nekoashi Wolf or Kaitlin Morgan → IT-Security group |
| Software bug or feature request | Ryan Bergsma → IT-Development group |
| Project-level work (multi-week) | Reassign to IT-Operations-Projects |
| External customer issue that landed in IT-Ops by mistake | Reassign to IT-Support |
| Membership/Sales question | Reassign to Sales/Membership - Sales |
| Accounting/billing question | Reassign to Accounting |
| Not sure where it goes | Ask in the team Slack channel before reassigning |

---

## 9. Things to Avoid

These are patterns from the data that have caused problems:

**Don't close tickets without a reply.** The team's 21.9% zero-reply rate is 6x the org average. Even for internal fixes where you resolved the issue behind the scenes, tell the requester what you did. A one-liner is fine.

**Don't let IT-Operations-Projects tickets sit.** This queue has an 85.7% open rate and a 44-day median resolution time. If a project ticket is assigned to you and you can't make progress, add an internal note explaining why and flag it for your lead.

**Don't hold tickets in your queue if you're not the right person.** Reassign quickly. A ticket sitting in the wrong queue for 3 days is worse than a 30-second reassignment.

**Don't skip internal notes.** When a ticket requires multiple steps over several days, leave internal notes on what you've done and what's left. Your teammates need to be able to pick up where you left off if you're out.

---

## 10. Using Claude with Your Zendesk Data

Claude is connected to CSA's Zendesk via an MCP server and has access to the exported ticket data. Here are things you can ask Claude to help with:

**Queue management:** "Show me all open IT-Operations tickets sorted by age" or "Which of my tickets haven't been updated in over 3 days?"

**Drafting replies:** "Draft a response for ticket #[number] — the user is asking about [topic]" — Claude will write a reply you can review and send.

**Research:** "What's the history on this requester? Have they submitted similar tickets before?" — Claude can search across the ticket data and comments.

**Pattern spotting:** "Are there any recurring ticket subjects in IT-Ops this month that might indicate a systemic issue?"

**Data lookups:** "Who is agent ID 12345?" or "What group is group_id 67890?" — Claude can cross-reference agents.csv and groups.csv instantly.

For more detail on the analysis Claude has already done on this data, see the files in `zendeskdata-analysis/`:

| File | What's in it |
|---|---|
| `proposed_actionable_items.md` | 12 prioritized action items for the entire Zendesk environment |
| `auto_reply_templates.md` | Ready-to-use auto-reply templates with real CSA URLs |
| `group_analysis_report.md` | Full metrics and patterns for every group |
| `groups/` | Individual per-group analysis files |

---

## Quick Reference Card

| What | Where |
|---|---|
| Your primary queue | Zendesk → IT-Operations view |
| Projects queue | Zendesk → IT-Operations-Projects view |
| Team Slack | Ask your lead for the channel name |
| Support contact page | https://cloudsecurityalliance.org/contact |
| CSA account portal | https://cloudsecurityalliance.org/account |
| Exam platform | https://exams.cloudsecurityalliance.org/en |
| Training platform | https://training.cloudsecurityalliance.org |
| STAR registry | https://cloudsecurityalliance.org/star/registry |
| Zendesk data & analysis | `zendeskdata/` and `zendeskdata-analysis/` in this repo |
