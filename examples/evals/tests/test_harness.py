"""评测 harness 自身的测试：指标算对了吗？作弊会被抓到吗？门禁会在变差时失败吗？

    python -m unittest discover -s tests -v      （在 examples/evals 目录下）
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "harness"))
from metrics import pass_at_k, pass_hat_k, wilson_interval  # noqa: E402

PY = sys.executable


def run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([PY, *args], cwd=ROOT, capture_output=True, text=True, timeout=300)


class MetricsTest(unittest.TestCase):
    def test_pass_at_k_known_values(self):
        self.assertAlmostEqual(pass_at_k(5, 2, 3), 0.9)        # 1 - C(3,3)/C(5,3)
        self.assertAlmostEqual(pass_at_k(5, 0, 3), 0.0)
        self.assertAlmostEqual(pass_at_k(5, 3, 3), 1.0)        # 失败的只有 2 次，抽 3 次必有成功

    def test_pass_hat_k_known_values(self):
        self.assertAlmostEqual(pass_hat_k(5, 4, 3), 0.4)       # C(4,3)/C(5,3)
        self.assertAlmostEqual(pass_hat_k(5, 5, 5), 1.0)
        self.assertAlmostEqual(pass_hat_k(5, 4, 5), 0.0)

    def test_k1_both_equal_success_rate(self):
        for c in range(6):
            self.assertAlmostEqual(pass_at_k(5, c, 1), c / 5)
            self.assertAlmostEqual(pass_hat_k(5, c, 1), c / 5)

    def test_reliability_gap(self):
        # 8 次里成功 6 次（单次成功率 75%），连续 3 次都成功的估计只有 C(6,3)/C(8,3) = 20/56 ≈ 0.36
        self.assertAlmostEqual(pass_hat_k(8, 6, 3), 20 / 56)

    def test_wilson(self):
        lo, hi = wilson_interval(0, 30)
        self.assertEqual(lo, 0.0)
        self.assertLess(hi, 0.12)


class HarnessTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.tmp.name)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def results(self, profile: str, grader: str) -> dict:
        out = self.out / f"{profile}-{grader}.json"
        p = run("harness/run_evals.py", "--agent", f"{PY} agents/mock_agent.py --profile {profile}",
                "--trials", "5", "--grader", grader, "--out", str(out))
        self.assertEqual(p.returncode, 0, p.stderr)
        return json.loads(out.read_text())

    def test_naive_grader_is_fooled_by_cheating(self):
        naive = self.results("cheater", "naive")
        isolated = self.results("cheater", "isolated")
        self.assertEqual(naive["summary"]["trial_success_rate"], 1.0)
        self.assertLess(isolated["summary"]["trial_success_rate"], 1.0)
        self.assertGreater(isolated["summary"]["trials_with_violations"], 0)
        kinds = {v for t in isolated["per_task"].values() for v in t["violations"]}
        self.assertIn("forbidden_tool:read_hidden", kinds)
        self.assertIn("protected_modified:tests/test_visible.py", kinds)

    def test_hidden_tests_never_reach_agent_workspace(self):
        res = self.results("honest", "isolated")
        self.assertEqual(res["summary"]["trials_with_violations"], 0)

    def test_regression_gate(self):
        base = self.out / "base.json"
        good = self.out / "good.json"
        worse = self.out / "worse.json"
        for prof, path in [("honest", base), ("honest", good), ("honest_v2", worse)]:
            p = run("harness/run_evals.py", "--agent", f"{PY} agents/mock_agent.py --profile {prof}",
                    "--trials", "5", "--out", str(path))
            self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(run("harness/compare.py", "--baseline", str(base), "--current", str(good)).returncode, 0)
        bad = run("harness/compare.py", "--baseline", str(base), "--current", str(worse))
        self.assertEqual(bad.returncode, 1)
        self.assertIn("parse_duration", bad.stdout)


class JudgeAndPairedTest(unittest.TestCase):
    def test_calibration_gate(self):
        ok = run("judge/calibrate.py", "--labels", "judge/data/labels.csv", "--judge", "judge_v1",
                 "--compare", "judge_v2", "--pairwise", "judge/data/pairwise.csv")
        self.assertEqual(ok.returncode, 0, ok.stdout)
        self.assertIn("agreement=0.800 kappa=0.000", ok.stdout)   # 永远判通过：一致率高，kappa 为 0
        bad = run("judge/calibrate.py", "--labels", "judge/data/labels.csv", "--judge", "judge_v2")
        self.assertEqual(bad.returncode, 1)

    def test_paired_vuln_eval(self):
        p = run("vuln/paired_eval.py", "--pairs", "vuln/data/pairs.jsonl",
                "--predictions", "vuln/data/model_predictions.jsonl", "--cutoff", "2026-06-01")
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("always_vulnerable      F1=0.667 MCC=+0.000 P-C=0.000", p.stdout)


if __name__ == "__main__":
    unittest.main()
