#!/usr/bin/env python3
"""Minimal eval harness for this starter kit (handbook ch16), standard library only.

It evaluates a coding agent on the tasks in evals/tasks/ the same way the agent
loop of this template works: the agent edits a copy of the repo, and "done"
means scripts/verify.sh passes. On top of that the harness

  * runs every task several times (trials) and reports pass@k and pass^k with
    Wilson 95% intervals, because agents are not deterministic;
  * grades in isolation: the agent's workspace never contains evals/, so it
    cannot see the hidden tests; grading happens in a fresh copy where only the
    agent's changes to non-protected files are applied, then hidden tests and
    scripts/verify.sh run there;
  * flags process violations: edits to protected files (the PROTECTED_REGEX of
    scripts/guard-protected.sh, plus evals/) and test inputs dropped from existing tests;
  * records cost (tokens the agent reports) and agent wall time;
  * compares against evals/baseline.json and fails on regressions (gate).

Usage (from the repo root):
  python3 evals/run_evals.py run --trials 5 --k 1 3 5 --out evals/results.json
  python3 evals/run_evals.py gate --baseline evals/baseline.json --current evals/results.json

The default agent is evals/mock_agent.py (offline, seeded, applies prepared
edits) so CI needs no model key. Point --agent at a real agent CLI to evaluate
it; see evals/README.md.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
from math import comb
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parent.parent
STRING_LITERAL = re.compile(r'"(?:[^"\\\n]|\\.)*"')
EVALS = ROOT / "evals"
SKIP_DIRS = {
    ".git",
    "evals",
    "node_modules",
    "target",
    "build",
    ".venv",
    "dist",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "coverage",
}


# ---------------------------------------------------------------- metrics
def pass_at_k(n: int, c: int, k: int) -> float:
    """Probability that at least one of k trials passes (unbiased, from n trials, c passes)."""
    if n - c < k:
        return 1.0
    return 1.0 - comb(n - c, k) / comb(n, k)


def pass_hat_k(n: int, c: int, k: int) -> float:
    """Probability that all k trials pass (tau-bench's pass^k)."""
    return comb(c, k) / comb(n, k)


def wilson(successes: int, total: int, z: float = 1.96) -> tuple[float, float]:
    if total == 0:
        return (0.0, 1.0)
    p = successes / total
    denom = 1 + z * z / total
    centre = (p + z * z / (2 * total)) / denom
    half = z * math.sqrt(p * (1 - p) / total + z * z / (4 * total * total)) / denom
    return (max(0.0, centre - half), min(1.0, centre + half))


def percentile(values: list[float], q: float) -> float:
    ordered = sorted(values)
    return ordered[max(1, math.ceil(q / 100 * len(ordered))) - 1]


# ---------------------------------------------------------------- repo snapshot
def protected_regex() -> re.Pattern[str]:
    """Same rule the PreToolUse hook enforces, plus evals/ (hidden tests live there)."""
    text = (ROOT / "scripts" / "guard-protected.sh").read_text(encoding="utf-8")
    m = re.search(r"^PROTECTED_REGEX='(.*)'$", text, re.M)
    if not m:
        raise SystemExit("PROTECTED_REGEX not found in scripts/guard-protected.sh")
    return re.compile(m.group(1))


def snapshot(root: Path) -> dict[str, str]:
    out = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            p = Path(dirpath) / name
            if p.is_symlink():
                continue
            out[str(p.relative_to(root))] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def copy_repo(dst: Path) -> None:
    def ignore(_dir: str, names: list[str]) -> set[str]:
        return {n for n in names if n in SKIP_DIRS}

    shutil.copytree(ROOT, dst, ignore=ignore, symlinks=True)


def sh(cmd: str, cwd: Path, env: dict[str, str], timeout: float) -> tuple[bool, str]:
    try:
        p = subprocess.run(
            cmd, shell=True, cwd=cwd, env=env, capture_output=True, text=True, timeout=timeout
        )
    except subprocess.TimeoutExpired:
        return False, f"timeout after {timeout}s"
    return p.returncode == 0, (p.stdout + p.stderr)[-4000:]


# ---------------------------------------------------------------- one trial
class Harness:
    def __init__(self, args: argparse.Namespace) -> None:
        self.args = args
        self.config = json.loads((EVALS / "config.json").read_text(encoding="utf-8"))
        self.protected = protected_regex()
        self.base = snapshot(ROOT)
        self.work = Path(tempfile.mkdtemp(prefix="evals-"))
        self.cache_dir = Path(args.cache_dir) if args.cache_dir else self.work / "cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.env = {**os.environ}
        for key, value in self.config.get("env", {}).items():
            self.env[key] = value.replace("{cache}", str(self.cache_dir))

    def link_shared(self, dst: Path) -> None:
        for name in self.config.get("link", []):  # e.g. node_modules: reuse, do not reinstall
            if (ROOT / name).exists() and not (dst / name).exists():
                (dst / name).symlink_to(ROOT / name)

    def run_agent(self, task: dict, trial: int) -> dict:
        ws = self.work / f"ws-{task['id']}-{trial}"
        copy_repo(ws)
        self.link_shared(ws)
        prompt = self.work / f"{task['id']}.md"
        prompt.write_text(task["prompt"], encoding="utf-8")
        env = {
            **self.env,
            "EVAL_TASK_ID": task["id"],
            "EVAL_TASK_FILE": str(prompt),
            "EVAL_TRIAL": str(trial),
            "EVAL_SEED": self.args.seed,
            "EVAL_PROFILE": self.args.profile,
        }
        t0 = time.monotonic()
        agent = (
            self.args.agent
            or f"{shlex.quote(sys.executable)} {shlex.quote(str(EVALS / 'mock_agent.py'))}"
        )
        ok, out = sh(agent, ws, env, self.args.agent_timeout)
        seconds = time.monotonic() - t0
        tokens = None
        for line in reversed(out.strip().splitlines()):
            if line.startswith("{") and '"tokens"' in line:
                tokens = json.loads(line).get("tokens")
                break
        return {
            "ws": ws,
            "agent_ok": ok,
            "agent_seconds": seconds,
            "tokens": tokens,
            "agent_tail": out[-500:],
        }

    def changes(self, ws: Path) -> tuple[dict[str, str], list[str]]:
        after = snapshot(ws)
        changed = {p: h for p, h in after.items() if self.base.get(p) != h}
        deleted = [p for p in self.base if p not in after]
        return changed, deleted

    def grade(self, task: dict, ws: Path) -> dict:
        changed, deleted = self.changes(ws)
        if self.args.grader == "naive":  # for comparison only: trust the agent's own workspace
            ok, _ = sh("bash scripts/verify.sh", ws, self.env, self.args.grade_timeout)
            return {
                "passed": ok,
                "reason": None if ok else "verify.sh failed in workspace",
                "violations": [],
                "changed_files": sorted(changed),
            }
        violations = [
            f"edited protected file {p}"
            for p in sorted(changed) + deleted
            if self.protected.search(p) or p.startswith("evals/")
        ]
        for p in self.config["test_files"]:
            if p in changed:
                # Test inputs may be added, never dropped: every string literal of the original
                # test file must still be there. Language-neutral and robust to reformatting.
                old = set(STRING_LITERAL.findall((ROOT / p).read_text(encoding="utf-8")))
                new = set(STRING_LITERAL.findall((ws / p).read_text(encoding="utf-8")))
                if old - new:
                    violations.append(f"removed test inputs {sorted(old - new)} from {p}")
            elif p in deleted:
                violations.append(f"deleted existing test {p}")
        allowed = {p: h for p, h in changed.items() if not self.protected.search(p)}
        hidden = EVALS / self.config.get("hidden_dir", "hidden") / task["hidden"]
        key = hashlib.sha256(
            json.dumps(
                [
                    task["id"],
                    sorted(allowed.items()),
                    sorted(deleted),
                    hashlib.sha256(hidden.read_bytes()).hexdigest(),
                ]
            ).encode()
        ).hexdigest()[:20]
        cached = self.cache_dir / f"grade-{key}.json"
        if cached.exists():
            result = json.loads(cached.read_text(encoding="utf-8"))
        else:
            result = self._grade_fresh(task, ws, allowed, deleted, hidden, key)
            cached.write_text(json.dumps(result), encoding="utf-8")
        result = dict(result)
        result["violations"] = violations
        result["changed_files"] = sorted(changed)
        result["passed"] = result["hidden_ok"] and result["verify_ok"] and not violations
        return result

    def _grade_fresh(
        self,
        task: dict,
        ws: Path,
        allowed: dict[str, str],
        deleted: list[str],
        hidden: Path,
        key: str,
    ) -> dict:
        g = self.work / f"grade-{key}"
        copy_repo(g)
        self.link_shared(g)
        for p in allowed:
            (g / p).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ws / p, g / p)
        for p in deleted:
            if not self.protected.search(p) and (g / p).exists():
                (g / p).unlink()
        h = self.config["hidden"]
        names = {"task": task["id"], "name": hidden.name.split(".")[0]}
        dest = g / h["dest"].format(**names) if h.get("dest") else None
        if dest is not None:
            shutil.copy2(hidden, dest)
        cmd = h["cmd"].format(
            **names, hidden=shlex.quote(str(hidden)), tmp=shlex.quote(str(self.work))
        )
        hidden_ok, hidden_out = sh(cmd, g, self.env, self.args.grade_timeout)
        if dest is not None:
            dest.unlink()  # verify.sh must see exactly what the agent delivered
        verify_ok, verify_out = False, "skipped: hidden tests failed"
        if hidden_ok:
            verify_ok, verify_out = sh(
                "bash scripts/verify.sh", g, self.env, self.args.grade_timeout
            )
        reason = None
        if not hidden_ok:
            reason = "hidden tests failed"
        elif not verify_ok:
            reason = "scripts/verify.sh failed"
        return {
            "hidden_ok": hidden_ok,
            "verify_ok": verify_ok,
            "reason": reason,
            "hidden_tail": hidden_out[-1500:],
            "verify_tail": verify_out[-1500:],
        }


def load_tasks(only: list[str] | None) -> list[dict]:
    tasks = []
    for d in sorted((EVALS / "tasks").iterdir()):
        meta = json.loads((d / "task.json").read_text(encoding="utf-8"))
        meta["prompt"] = (d / "task.md").read_text(encoding="utf-8")
        meta["id"] = d.name
        if not only or d.name in only:
            tasks.append(meta)
    return tasks


def cmd_run(args: argparse.Namespace) -> int:
    if any(k > args.trials for k in args.k):
        raise SystemExit("every k must be <= --trials")
    h = Harness(args)
    tasks = load_tasks(args.only)
    rows = []
    t0 = time.monotonic()
    try:
        for task in tasks:
            for trial in range(args.trials):
                a = h.run_agent(task, trial)
                g = (
                    h.grade(task, a["ws"])
                    if a["agent_ok"]
                    else {
                        "passed": False,
                        "reason": "agent failed",
                        "violations": [],
                        "changed_files": [],
                    }
                )
                rows.append(
                    {
                        "task": task["id"],
                        "kind": task["kind"],
                        "trial": trial,
                        "passed": g["passed"],
                        "reason": g.get("reason"),
                        "violations": g["violations"],
                        "changed_files": g["changed_files"],
                        "tokens": a["tokens"],
                        "agent_seconds": round(a["agent_seconds"], 3),
                    }
                )
                mark = "pass" if g["passed"] else "FAIL"
                why = "; ".join(filter(None, [g.get("reason"), *g["violations"]]))
                print(f"  {task['id']:<24} trial {trial}: {mark} {why}", flush=True)
    finally:
        if not args.keep:
            shutil.rmtree(h.work, ignore_errors=True)
    wall = time.monotonic() - t0

    per_task = {}
    for task in tasks:
        r = [x for x in rows if x["task"] == task["id"]]
        n, c = len(r), sum(x["passed"] for x in r)
        lo, hi = wilson(c, n)
        e = {
            "kind": task["kind"],
            "n": n,
            "c": c,
            "pass@1": round(c / n, 4),
            "wilson95": [round(lo, 4), round(hi, 4)],
            "violations": sum(bool(x["violations"]) for x in r),
            "first_failure": next(
                (x["reason"] or x["violations"][0] for x in r if not x["passed"]), None
            ),
        }
        for k in args.k:
            e[f"pass@{k}"] = round(pass_at_k(n, c, k), 4)
            e[f"pass^{k}"] = round(pass_hat_k(n, c, k), 4)
        per_task[task["id"]] = e
    suites = {}
    for suite in ("regression", "capability"):
        ids = [t for t, e in per_task.items() if e["kind"] == suite]
        if not ids:
            continue
        r = [x for x in rows if x["task"] in ids]
        c = sum(x["passed"] for x in r)
        lo, hi = wilson(c, len(r))
        toks = [x["tokens"] for x in r if x["tokens"] is not None]
        secs = [x["agent_seconds"] for x in r]
        s = {
            "tasks": len(ids),
            "trials": len(r),
            "passed_trials": c,
            "pass@1": round(c / len(r), 4),
            "wilson95": [round(lo, 4), round(hi, 4)],
            "tokens_mean": round(sum(toks) / len(toks), 1) if toks else None,
            "agent_p50_s": round(median(secs), 3),
            "agent_p95_s": round(percentile(secs, 95), 3),
        }
        for k in args.k:
            s[f"pass@{k}"] = round(sum(per_task[i][f"pass@{k}"] for i in ids) / len(ids), 4)
            s[f"pass^{k}"] = round(sum(per_task[i][f"pass^{k}"] for i in ids) / len(ids), 4)
        suites[suite] = s
    summary = {"suites": suites, "trials_with_violations": sum(bool(x["violations"]) for x in rows)}
    meta = {
        "agent": args.agent or "mock (evals/mock_agent.py)",
        "profile": args.profile,
        "seed": args.seed,
        "grader": args.grader,
        "trials": args.trials,
        "k": args.k,
        "language": h.config["language"],
        "wall_seconds": round(wall, 1),
    }
    out = {"meta": meta, "summary": summary, "per_task": per_task, "trials": rows}
    Path(args.out).write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")

    for tid, e in per_task.items():
        ks = " ".join(f"pass^{k}={e[f'pass^{k}']:.2f}" for k in args.k if k > 1)
        print(f"{tid:<24} {e['kind']:<10} {e['c']}/{e['n']} wilson95={e['wilson95']} {ks}")
    for suite, s in suites.items():
        ks = " ".join(
            f"pass@{k}={s[f'pass@{k}']:.3f} pass^{k}={s[f'pass^{k}']:.3f}" for k in args.k
        )
        print(
            f"{suite}: {s['passed_trials']}/{s['trials']} trials, {ks}, wilson95={s['wilson95']}, "
            f"tokens/trial={s['tokens_mean']}"
        )
    print(f"trials with process violations: {summary['trials_with_violations']}; wall {wall:.1f}s")
    print(f"wrote {args.out}")
    return 0


# ---------------------------------------------------------------- gate
def gate_problems(base: dict, cur: dict, k: int, tol: float, max_cost: float) -> list[str]:
    problems = []
    for suite, metric in (("regression", f"pass^{k}"), ("capability", f"pass@{k}")):
        b = base["summary"]["suites"].get(suite, {}).get(metric)
        c = cur["summary"]["suites"].get(suite, {}).get(metric)
        if b is None:
            continue
        if c is None:
            problems.append(f"{suite} {metric} missing from current run")
            continue
        status = "DROP" if c < b - tol else "ok"
        print(f"{suite:>10} {metric}: baseline={b:.3f} current={c:.3f} [{status}]")
        if status == "DROP":
            problems.append(f"{suite} {metric} dropped {b:.3f} -> {c:.3f}")
    for tid, bt in base["per_task"].items():
        ct = cur["per_task"].get(tid)
        if bt["kind"] != "regression":
            continue
        if ct is None:
            problems.append(f"regression task {tid} missing from current run")
        elif ct["pass@1"] < bt["pass@1"] - tol:
            problems.append(
                f"regression task {tid} pass@1 {bt['pass@1']:.3f} -> {ct['pass@1']:.3f}"
            )
    if cur["summary"]["trials_with_violations"]:
        bad = [t for t, e in cur["per_task"].items() if e["violations"]]
        problems.append(
            f"{cur['summary']['trials_with_violations']} trial(s) violated rules: {bad}"
        )
    for suite, bs in base["summary"]["suites"].items():
        cs = cur["summary"]["suites"].get(suite)
        if cs and bs.get("tokens_mean") and cs.get("tokens_mean"):
            rise = (cs["tokens_mean"] - bs["tokens_mean"]) / bs["tokens_mean"]
            print(
                f"{suite:>10} tokens/trial: baseline={bs['tokens_mean']} "
                f"current={cs['tokens_mean']} ({rise:+.1%})"
            )
            if rise > max_cost:
                problems.append(f"{suite} tokens/trial rose {rise:+.1%} (> {max_cost:.0%})")
    return problems


def cmd_gate(args: argparse.Namespace) -> int:
    base = json.loads(Path(args.baseline).read_text(encoding="utf-8"))
    cur = json.loads(Path(args.current).read_text(encoding="utf-8"))
    problems = gate_problems(base, cur, args.k, args.max_drop, args.max_cost_increase)
    if problems:
        print("\nREGRESSION GATE FAILED:")
        for p in problems:
            print("  -", p)
        return 1
    print("\nregression gate passed")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0] if __doc__ else None)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--agent", default=None, help="agent command (default: the offline mock agent)")
    r.add_argument("--profile", default="honest", help="mock agent profile (evals/profiles.json)")
    r.add_argument("--seed", default="0")
    r.add_argument("--trials", type=int, default=5)
    r.add_argument("--k", type=int, nargs="+", default=[1, 3, 5])
    r.add_argument("--only", nargs="*")
    r.add_argument("--out", default="evals-results.json")
    r.add_argument(
        "--cache-dir", help="reuse grading results across runs (same content, same grade)"
    )
    r.add_argument("--agent-timeout", type=float, default=1800)
    r.add_argument("--grade-timeout", type=float, default=900)
    r.add_argument(
        "--grader",
        choices=["isolated", "naive"],
        default="isolated",
        help="naive = just run scripts/verify.sh in the agent's workspace (comparison only)",
    )
    r.add_argument("--keep", action="store_true", help="keep workspaces for inspection")
    g = sub.add_parser("gate")
    g.add_argument("--baseline", default=str(EVALS / "baseline.json"))
    g.add_argument("--current", required=True)
    g.add_argument("--k", type=int, default=3)
    g.add_argument("--max-drop", type=float, default=0.02)
    g.add_argument("--max-cost-increase", type=float, default=0.25)
    args = ap.parse_args(argv)
    return cmd_run(args) if args.cmd == "run" else cmd_gate(args)


if __name__ == "__main__":
    sys.exit(main())
