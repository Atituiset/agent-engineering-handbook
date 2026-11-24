#!/usr/bin/env python3
"""回归门禁：把本次结果和基线比，掉得超过阈值就以非零状态退出，让 CI 失败。

    python harness/compare.py --baseline baseline.json --current results.json --max-drop 0.02

比较三类数字：
  1. 回归集的 pass^k（可靠性）：回归集本来就该一直过，看「每次都过」有没有变差；
  2. 能力集的 pass@k（能力上限）：能力集本来就难，只看「能不能做到」有没有变差；
  3. 回归集里每个任务的 pass@1：总分没掉、但某个任务掉了，也要报出来（总分会掩盖个别任务）。
另外，只要出现过程违规（改受保护文件、用禁用工具），直接失败。
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--current", required=True)
    ap.add_argument("--max-drop", type=float, default=0.02)
    ap.add_argument("--k", type=int, default=3, help="比较 pass^k / pass@k 用的 k")
    args = ap.parse_args()

    base = json.loads(Path(args.baseline).read_text(encoding="utf-8"))
    cur = json.loads(Path(args.current).read_text(encoding="utf-8"))
    k, tol = args.k, args.max_drop
    problems = []

    checks = [("regression", f"pass^{k}"), ("capability", f"pass@{k}")]
    for suite, metric in checks:
        b = base["summary"]["suites"].get(suite, {}).get(metric)
        c = cur["summary"]["suites"].get(suite, {}).get(metric)
        if b is None or c is None:
            continue
        status = "DROP" if c < b - tol else "ok"
        print(f"{suite:>10} {metric:>7}: baseline={b:.3f} current={c:.3f} [{status}]")
        if status == "DROP":
            problems.append(f"{suite} {metric} dropped {b:.3f} -> {c:.3f}")

    for tid, bt in base["per_task"].items():
        ct = cur["per_task"].get(tid)
        if bt["kind"] != "regression":
            continue
        if ct is None:
            problems.append(f"regression task {tid} missing from current run")
            continue
        if ct["pass@1"] < bt["pass@1"] - tol:
            problems.append(f"regression task {tid} pass@1 {bt['pass@1']:.3f} -> {ct['pass@1']:.3f}")

    if cur["summary"].get("trials_with_violations", 0) > 0:
        problems.append(f"{cur['summary']['trials_with_violations']} trial(s) violated process rules")

    if problems:
        print("\nREGRESSION GATE FAILED:")
        for p in problems:
            print("  -", p)
        return 1
    print("\nregression gate passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
