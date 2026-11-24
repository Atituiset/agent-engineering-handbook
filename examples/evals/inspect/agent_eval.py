"""Inspect 版：同一套任务，用 Inspect 的 epochs + pass_at / pass_k reducer 算 pass@k 和 pass^k。

运行（在 examples/evals 目录下，不需要模型 API key）：
    pip install inspect-ai
    python inspect/run_inspect.py
或：
    inspect eval inspect/agent_eval.py --model mockllm/model --epochs 5

solver 不调用模型，而是把外部智能体（默认是 agents/mock_agent.py）当黑盒跑一遍，
所以 --model 用 Inspect 自带的 mockllm/model 占位即可。换成真实智能体时设置 EVAL_AGENT，
或者把 solver 换成 Inspect 自带的 react() 智能体并去掉 mockllm。
scorer 在独立临时目录里用隐藏测试评分，并检查过程记录和受保护文件。
"""
from __future__ import annotations

import hashlib
import json
import os
import shlex
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from inspect_ai import Epochs, Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import CORRECT, INCORRECT, Score, Target, accuracy, scorer
from inspect_ai.solver import Generate, TaskState, solver

ROOT = Path(__file__).resolve().parents[1]
AGENT = os.environ.get("EVAL_AGENT", f"{sys.executable} {ROOT / 'agents' / 'mock_agent.py'} --profile honest")


def load_samples() -> list[Sample]:
    samples = []
    for d in sorted((ROOT / "tasks").iterdir()):
        if (d / "task.json").exists():
            meta = json.loads((d / "task.json").read_text(encoding="utf-8"))
            samples.append(Sample(id=meta["id"], input=meta["prompt"], target="hidden tests pass",
                                  metadata={"task_id": meta["id"], "kind": meta["kind"]}))
    return samples


@solver
def external_agent():
    async def solve(state: TaskState, generate: Generate) -> TaskState:
        task_id = state.metadata["task_id"]
        meta = json.loads((ROOT / "tasks" / task_id / "task.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as td:
            ws = Path(td) / "ws"
            shutil.copytree(ROOT / "tasks" / task_id / "workspace", ws)
            before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (ws / "tests").glob("*.py")}
            transcript = Path(td) / "transcript.jsonl"
            subprocess.run(shlex.split(AGENT) + ["--workspace", str(ws), "--task-id", task_id, "--prompt", meta["prompt"],
                                                 "--trial", str(state.epoch - 1), "--transcript", str(transcript)],
                           capture_output=True, text=True, timeout=120, check=False)
            after = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (ws / "tests").glob("*.py")}
            state.store.set("solution", (ws / meta["entry_file"]).read_text(encoding="utf-8"))
            state.store.set("tools", [json.loads(l).get("tool") for l in transcript.read_text().splitlines() if l.strip()]
                            if transcript.exists() else [])
            state.store.set("protected_changed", sorted(k for k in before if before[k] != after.get(k)))
        return state
    return solve


@scorer(metrics=[accuracy()])
def isolated_grader():
    async def score(state: TaskState, target: Target) -> Score:
        task_id = state.metadata["task_id"]
        meta = json.loads((ROOT / "tasks" / task_id / "task.json").read_text(encoding="utf-8"))
        bad_tools = [t for t in state.store.get("tools", []) if t in meta["forbidden_tools"]]
        changed = state.store.get("protected_changed", [])
        if bad_tools or changed:
            return Score(value=INCORRECT, explanation=f"process violation: {bad_tools} {changed}")
        with tempfile.TemporaryDirectory() as td:
            gd = Path(td)
            (gd / meta["entry_file"]).write_text(state.store.get("solution", ""), encoding="utf-8")
            (gd / "hidden_tests").mkdir()
            for f in (ROOT / "tasks" / task_id / "hidden").glob("test_*.py"):
                shutil.copyfile(f, gd / "hidden_tests" / f.name)
            proc = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "hidden_tests", "-p", "test_*.py"],
                                  cwd=gd, capture_output=True, text=True, timeout=60,
                                  env={"PATH": os.environ.get("PATH", ""), "PYTHONPATH": str(gd)})
        return Score(value=CORRECT if proc.returncode == 0 else INCORRECT,
                     explanation=(proc.stdout + proc.stderr).strip()[-300:])
    return score


@task
def agent_regression(epochs: int = 5):
    return Task(
        dataset=load_samples(),
        solver=external_agent(),
        scorer=isolated_grader(),
        epochs=Epochs(epochs, ["mean", "pass_at_3", "pass_k_3"]),
    )
