# Responsible disclosure in practice

## Before you report

- Confirm you were authorized, or that the vendor publishes a reporting channel.
- Reproduce the issue with the smallest possible impact and your own test data.
- Record timestamps, requests, responses and the affected version.

## Writing the report

Use [templates/report.md](../templates/report.md). Lead with impact, not with the
payload. Include a reproduction that a busy engineer can follow in five minutes.

## Sending it

- Use the vendor's security contact or `security.txt` if present.
- Encrypt sensitive details if the channel supports it.
- Keep a copy of the report and the date it was sent.

## While you wait

- Do not publish details before the agreed date.
- Answer clarifying questions promptly.
- Escalate politely after the acknowledgement window passes.

## Default windows used by the timeline tool

| Milestone | Default |
|---|---|
| Acknowledgement | 3 days |
| Triage | 10 days |
| Fix target | 90 days |
| Public disclosure | after fix, or day 90 with coordination |

These are defaults, not law. A vendor that is actively fixing the issue deserves
the agreed time; a vendor that ignores you does not get indefinite silence.
