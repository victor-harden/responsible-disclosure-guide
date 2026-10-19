import contextlib
import datetime as dt
import io
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import disclosure_timeline


class TimelineTests(unittest.TestCase):
    def test_default_policy_dates(self):
        reported = dt.date(2026, 1, 1)
        rows = disclosure_timeline.timeline(reported, disclosure_timeline.parse_policy("90,3,10"))
        by_name = {r["milestone"]: r for r in rows}
        self.assertEqual(by_name["acknowledgement"]["date"], "2026-01-04")
        self.assertEqual(by_name["triage"]["date"], "2026-01-11")
        self.assertEqual(by_name["fix target"]["date"], "2026-04-01")

    def test_custom_policy(self):
        policy = disclosure_timeline.parse_policy("30,1,5")
        rows = disclosure_timeline.timeline(dt.date(2026, 6, 1), policy)
        by_name = {r["milestone"]: r for r in rows}
        self.assertEqual(by_name["fix target"]["date"], "2026-07-01")

    def test_invalid_policy(self):
        with self.assertRaises(ValueError):
            disclosure_timeline.parse_policy("90,3")

    def test_invalid_date_exit_code(self):
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(disclosure_timeline.main(["--reported", "not-a-date"]), 2)

    def test_json_output(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = disclosure_timeline.main(["--reported", "2026-01-01", "--json"])
        self.assertEqual(code, 0)
        payload = json.loads(buf.getvalue())
        self.assertEqual(payload["milestones"][0]["day"], 0)

    def test_render_table(self):
        rows = disclosure_timeline.timeline(dt.date(2026, 1, 1),
                                            disclosure_timeline.parse_policy("90,3,10"))
        self.assertIn("| Milestone |", disclosure_timeline.render(rows))


if __name__ == "__main__":
    unittest.main()
