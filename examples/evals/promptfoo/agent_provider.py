#!/usr/bin/env python3
"""promptfoo 的 exec provider：在临时工作区里跑一次智能体，把产物和过程记录交给断言去评分。

promptfoo 调用方式：python3 agent_provider.py <prompt> <options_json> <context_json>
这里的 prompt 就是任务 id；context 里的 repeatIndex 作为第几次试验（配合 --repeat 实现多次试验）。
智能体命令默认是模拟智能体，可用环境变量 EVAL_AGENT 换成真实智能体。
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

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    task_id = sys.argv[1].strip()
    ctx = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
    trial = int(ctx.get("repeatIndex", 0))
    meta = json.loads((ROOT / "tasks" / task_id / "task.json").read_text(encoding="utf-8"))
    agent = os.environ.get("EVAL_AGENT", f"{sys.executable} {ROOT / 'agents' / 'mock_agent.py'} --profile honest")
    with tempfile.TemporaryDirectory() as td:
        ws = Path(td) / "ws"
        shutil.copytree(ROOT / "tasks" / task_id / "workspace", ws)
        protected = {str(p.relative_to(ws)): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in (ws / "tests").rglob("*.py")}
        transcript = Path(td) / "transcript.jsonl"
        subprocess.run(shlex.split(agent) + ["--workspace", str(ws), "--task-id", task_id, "--prompt", meta["prompt"],
                                             "--trial", str(trial), "--transcript", str(transcript)],
                       capture_output=True, text=True, timeout=120, check=False)
        changed = [rel for rel, h in protected.items()
                   if not (ws / rel).exists() or hashlib.sha256((ws / rel).read_bytes()).hexdigest() != h]
        events = [json.loads(l) for l in transcript.read_text(encoding="utf-8").splitlines() if l.strip()] \
            if transcript.exists() else []
        print(json.dumps({
            "task_id": task_id,
            "solution": (ws / meta["entry_file"]).read_text(encoding="utf-8"),
            "tools": [e.get("tool") for e in events],
            "protected_changed": changed,
        }, ensure_ascii=False))


if __name__ == "__main__":
    main()
