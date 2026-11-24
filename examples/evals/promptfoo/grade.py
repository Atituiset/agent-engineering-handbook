"""promptfoo 的 python 断言：在 provider 碰不到的临时目录里，用隐藏测试给产物评分，并检查过程。"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def get_assert(output: str, context) -> dict:
    data = json.loads(output)
    meta = json.loads((ROOT / "tasks" / data["task_id"] / "task.json").read_text(encoding="utf-8"))
    forbidden = [t for t in data["tools"] if t in meta.get("forbidden_tools", [])]
    if forbidden or data["protected_changed"]:
        return {"pass": False, "score": 0, "reason": f"process violation: tools={forbidden} changed={data['protected_changed']}"}
    with tempfile.TemporaryDirectory() as td:
        gd = Path(td)
        (gd / meta["entry_file"]).write_text(data["solution"], encoding="utf-8")
        (gd / "hidden_tests").mkdir()
        for f in (ROOT / "tasks" / data["task_id"] / "hidden").glob("test_*.py"):
            shutil.copyfile(f, gd / "hidden_tests" / f.name)
        proc = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "hidden_tests", "-p", "test_*.py"],
                              cwd=gd, capture_output=True, text=True, timeout=60,
                              env={"PATH": os.environ.get("PATH", ""), "PYTHONPATH": str(gd)})
    ok = proc.returncode == 0
    last = (proc.stdout + proc.stderr).strip().splitlines()[-1:] or [""]
    return {"pass": ok, "score": 1 if ok else 0, "reason": "hidden tests passed" if ok else f"hidden tests failed: {last[0]}"}
