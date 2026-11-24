"""Self-tests for evals/run_evals.py (stdlib unittest): python3 -m unittest evals/test_harness.py"""

from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import run_evals as h


class Metrics(unittest.TestCase):
    def test_pass_k(self) -> None:
        self.assertAlmostEqual(h.pass_at_k(5, 3, 1), 0.6)
        self.assertAlmostEqual(h.pass_hat_k(5, 3, 3), 0.1)
        self.assertEqual(h.pass_hat_k(5, 5, 5), 1.0)
        self.assertEqual(h.pass_at_k(5, 0, 3), 0.0)

    def test_wilson(self) -> None:
        lo, hi = h.wilson(5, 5)
        self.assertTrue(0.56 < lo < 0.57 and hi == 1.0)


class Protected(unittest.TestCase):
    def test_reads_hook_regex(self) -> None:
        rx = h.protected_regex()
        self.assertTrue(rx.search("scripts/verify.sh"))
        self.assertTrue(rx.search(".github/workflows/ci.yml"))
        self.assertTrue(rx.search("evals/hidden/x"))


class TestInputs(unittest.TestCase):
    def test_string_literals(self) -> None:
        src = 'cases = ["", "1h ", "a\\"b"]'
        self.assertEqual(h.STRING_LITERAL.findall(src), ['""', '"1h "', '"a\\"b"'])


class Gate(unittest.TestCase):
    def results(self, reg: float, task_p1: float, violations: int = 0) -> dict:
        return {
            "summary": {
                "suites": {"regression": {"pass^3": reg, "tokens_mean": 100.0}},
                "trials_with_violations": violations,
            },
            "per_task": {"a": {"kind": "regression", "pass@1": task_p1, "violations": violations}},
        }

    def test_gate(self) -> None:
        base = self.results(1.0, 1.0)
        self.assertEqual(h.gate_problems(base, copy.deepcopy(base), 3, 0.02, 0.25), [])
        self.assertEqual(len(h.gate_problems(base, self.results(0.5, 0.6), 3, 0.02, 0.25)), 2)
        self.assertEqual(len(h.gate_problems(base, self.results(1.0, 1.0, 1), 3, 0.02, 0.25)), 1)


if __name__ == "__main__":
    unittest.main()
