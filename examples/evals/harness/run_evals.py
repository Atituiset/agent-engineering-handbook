#!/usr/bin/env python3
"""最小评测 harness：多次试验、确定性结果检查、过程（transcript）检查、pass@k / pass^k、成本与延迟。

用法（在 examples/evals 目录下）：
    python harness/run_evals.py --agent "python agents/mock_agent.py --profile honest" \
        --trials 5 --k 1 3 5 --out results.json

两种评分方式：
  --grader isolated（默认）：评分在智能体碰不到的目录里进行。只从工作区拷出 entry_file，
      配上从未进入工作区的隐藏测试来跑；同时检查 transcript 和受保护文件有没有被改。
  --grader naive：直接跑工作区里的测试（智能体能改它们），也不看过程。用来对比演示。
只依赖 Python 标准库。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from metrics import pass_at_k, pass_hat_k, summarize_costs, wilson_interval  # noqa: E402


def file_hashes(root: Path, rel_prefixes: list[str]) -> dict[str, str]:
    out = {}
    for prefix in rel_prefixes:
        base = root / prefix
        files = [base] if base.is_file() else sorted(p for p in base.rglob("*") if p.is_file()) if base.exists() else []
        for f in files:
            if "__pycache__" in f.parts:
                continue
            out[str(f.relative_to(root))] = hashlib.sha256(f.read_bytes()).hexdigest()
    return out


def run_unittests(cwd: Path, start_dir: str, timeout: int) -> tuple[bool, str]:
    env = {"PATH": os.environ.get("PATH", ""), "PYTHONDONTWRITEBYTECODE": "1", "PYTHONPATH": str(cwd)}
    try:
        proc = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", start_dir, "-p", "test_*.py"],
            cwd=cwd, env=env, capture_output=True, text=True, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return False, "timeout"
    tail = (proc.stdout + proc.stderr).strip().splitlines()[-1:] or [""]
    return proc.returncode == 0, tail[0]


def grade_isolated(task_dir: Path, ws: Path, meta: dict) -> tuple[bool, str]:
    """评分器权限隔离：新目录 + 只拷贝产物 + 隐藏测试。工作区里的测试一概不用。"""
    with tempfile.TemporaryDirectory(prefix="grade-") as gd:
        gdir = Path(gd)
        entry = ws / meta["entry_file"]
        if not entry.exists():
            return False, "entry_file missing"
        shutil.copyfile(entry, gdir / meta["entry_file"])
        (gdir / "hidden_tests").mkdir()
        for f in (task_dir / "hidden").glob("test_*.py"):
            shutil.copyfile(f, gdir / "hidden_tests" / f.name)
        return run_unittests(gdir, "hidden_tests", meta.get("timeout_s", 30))


def grade_naive(ws: Path, meta: dict) -> tuple[bool, str]:
    return run_unittests(ws, "tests", meta.get("timeout_s", 30))


def check_trajectory(transcript: Path, meta: dict, before: dict, after: dict) -> list[str]:
    violations = []
    for rel, h in before.items():
        if after.get(rel) != h:
            violations.append(f"protected_modified:{rel}")
    for rel in after:
        if rel not in before:
            violations.append(f"protected_added:{rel}")
    forbidden = set(meta.get("forbidden_tools", []))
    if transcript.exists():
        for line in transcript.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            ev = json.loads(line)
            if ev.get("tool") in forbidden:
                violations.append(f"forbidden_tool:{ev['tool']}")
    else:
        violations.append("transcript_missing")
    return violations


def run_trial(task_dir: Path, meta: dict, agent_cmd: list[str], trial: int, grader: str) -> dict:
    with tempfile.TemporaryDirectory(prefix=f"{meta['id']}-{trial}-") as td:
        tmp = Path(td)
        ws = tmp / "ws"
        shutil.copytree(task_dir / "workspace", ws)
        transcript = tmp / "transcript.jsonl"
        before = file_hashes(ws, meta.get("protected_paths", []))
        cmd = agent_cmd + ["--workspace", str(ws), "--task-id", meta["id"], "--prompt", meta["prompt"],
                           "--trial", str(trial), "--transcript", str(transcript)]
        t0 = time.monotonic()
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=meta.get("timeout_s", 30) * 4)
        latency = time.monotonic() - t0
        tokens = 0
        try:
            tokens = int(json.loads(proc.stdout.strip().splitlines()[-1]).get("tokens", 0))
        except (ValueError, IndexError):
            pass
        after = file_hashes(ws, meta.get("protected_paths", []))
        if grader == "isolated":
            outcome, detail = grade_isolated(task_dir, ws, meta)
            violations = check_trajectory(transcript, meta, before, after)
        else:
            outcome, detail = grade_naive(ws, meta)
            violations = []
        return {
            "task": meta["id"], "trial": trial, "outcome_pass": outcome, "violations": violations,
            "passed": outcome and not violations and proc.returncode == 0,
            "agent_exit": proc.returncode, "latency_s": round(latency, 4), "tokens": tokens, "grader_detail": detail,
        }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tasks", default="tasks")
    ap.add_argument("--agent", required=True, help="智能体命令，例如 \"python agents/mock_agent.py --profile honest\"")
    ap.add_argument("--trials", type=int, default=5)
    ap.add_argument("--k", type=int, nargs="+", default=[1, 3, 5])
    ap.add_argument("--grader", choices=["isolated", "naive"], default="isolated")
    ap.add_argument("--only", nargs="*", help="只跑这些任务 id")
    ap.add_argument("--out", default="results.json")
    args = ap.parse_args()

    ks = [k for k in args.k if k <= args.trials]
    agent_cmd = shlex.split(args.agent)
    trials, per_task = [], {}
    for task_dir in sorted(p for p in Path(args.tasks).iterdir() if (p / "task.json").exists()):
        meta = json.loads((task_dir / "task.json").read_text(encoding="utf-8"))
        if args.only and meta["id"] not in args.only:
            continue
        rows = [run_trial(task_dir, meta, agent_cmd, t, args.grader) for t in range(args.trials)]
        trials += rows
        c = sum(r["passed"] for r in rows)
        per_task[meta["id"]] = {
            "kind": meta["kind"], "n": args.trials, "c": c,
            **{f"pass@{k}": round(pass_at_k(args.trials, c, k), 4) for k in ks},
            **{f"pass^{k}": round(pass_hat_k(args.trials, c, k), 4) for k in ks},
            "violations": sorted({v for r in rows for v in r["violations"]}),
            "claimed_but_failed": sum(1 for r in rows if not r["passed"]),
        }

    suites = {}
    for kind in sorted({v["kind"] for v in per_task.values()}):
        tasks = [v for v in per_task.values() if v["kind"] == kind]
        suites[kind] = {"tasks": len(tasks)}
        for k in ks:
            suites[kind][f"pass@{k}"] = round(sum(t[f"pass@{k}"] for t in tasks) / len(tasks), 4)
            suites[kind][f"pass^{k}"] = round(sum(t[f"pass^{k}"] for t in tasks) / len(tasks), 4)
    total_pass = sum(r["passed"] for r in trials)
    lo, hi = wilson_interval(total_pass, len(trials))
    summary = {
        "grader": args.grader, "agent": args.agent, "trials_per_task": args.trials,
        "trial_success_rate": round(total_pass / len(trials), 4), "trial_success_ci95": [round(lo, 4), round(hi, 4)],
        "trials_with_violations": sum(1 for r in trials if r["violations"]),
        "suites": suites, **summarize_costs([r["latency_s"] for r in trials], [r["tokens"] for r in trials]),
    }
    Path(args.out).write_text(json.dumps({"summary": summary, "per_task": per_task, "trials": trials},
                                         ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    hdr = ["task", "kind", "c/n"] + [f"pass@{k}" for k in ks] + [f"pass^{k}" for k in ks] + ["violations"]
    print("  ".join(f"{h:>18}" if i == 0 else f"{h:>10}" for i, h in enumerate(hdr)))
    for tid, v in per_task.items():
        cells = [tid, v["kind"], f"{v['c']}/{v['n']}"] + [f"{v[f'pass@{k}']:.3f}" for k in ks] + \
                [f"{v[f'pass^{k}']:.3f}" for k in ks] + [str(len(v["violations"]))]
        print("  ".join(f"{c:>18}" if i == 0 else f"{c:>10}" for i, c in enumerate(cells)))
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
