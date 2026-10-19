# responsible-disclosure-guide

How to report a vulnerability responsibly, plus a tool that lays out the
disclosure timeline from the report date: acknowledgement, triage, fix target and
public disclosure.

## Features

- `docs/guide.md`: preparation, contact, evidence, communication and escalation.
- `templates/report.md`: a report structure vendors can act on.
- `tools/disclosure_timeline.py`: computes the dates for a chosen policy
  (default: acknowledge in 3 days, triage in 10, fix target in 90, publish after
  the fix or at day 90).
- JSON output for trackers.

## Installation

```bash
git clone https://github.com/victor-harden/responsible-disclosure-guide.git
cd responsible-disclosure-guide
```

## Usage

```bash
python3 tools/disclosure_timeline.py --reported 2026-01-01
python3 tools/disclosure_timeline.py --reported 2026-01-01 --policy 120,7,14
python3 tools/disclosure_timeline.py --reported 2026-01-01 --json
```

`--policy` is `fix_days,ack_days,triage_days`.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## Ethics

Never test a system without authorization. This guide is about what to do when you
have found an issue in a system you were allowed to assess, or when a vendor
invites reports through a published channel.

## License

MIT — see [LICENSE](LICENSE).
