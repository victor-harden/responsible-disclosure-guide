#!/usr/bin/env python3
"""Compute responsible-disclosure milestone dates."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys


def parse_policy(value: str):
    parts = [int(p) for p in value.split(",")]
    if len(parts) != 3 or any(p < 0 for p in parts):
        raise ValueError("policy must be 'fix_days,ack_days,triage_days'")
    fix_days, ack_days, triage_days = parts
    return {"fix_days": fix_days, "ack_days": ack_days, "triage_days": triage_days}


def timeline(reported: dt.date, policy: dict):
    ack = reported + dt.timedelta(days=policy["ack_days"])
    triage = reported + dt.timedelta(days=policy["triage_days"])
    fix = reported + dt.timedelta(days=policy["fix_days"])
    return [
        {"milestone": "reported", "date": reported.isoformat(), "day": 0},
        {"milestone": "acknowledgement", "date": ack.isoformat(), "day": policy["ack_days"]},
        {"milestone": "triage", "date": triage.isoformat(), "day": policy["triage_days"]},
        {"milestone": "fix target", "date": fix.isoformat(), "day": policy["fix_days"]},
        {"milestone": "public disclosure", "date": fix.isoformat(),
         "day": policy["fix_days"]},
    ]


def render(rows) -> str:
    lines = ["| Milestone | Day | Date |", "|---|---|---|"]
    for row in rows:
        lines.append(f"| {row['milestone']} | {row['day']} | {row['date']} |")
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Disclosure timeline calculator")
    parser.add_argument("--reported", required=True, help="report date YYYY-MM-DD")
    parser.add_argument("--policy", default="90,3,10")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    try:
        reported = dt.date.fromisoformat(args.reported)
        policy = parse_policy(args.policy)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    rows = timeline(reported, policy)
    if args.json:
        print(json.dumps({"reported": args.reported, "policy": policy, "milestones": rows},
                         indent=2))
    else:
        print(render(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
