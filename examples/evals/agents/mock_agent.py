#!/usr/bin/env python3
"""确定性的模拟智能体：不调用任何模型 API，用来跑通评测流水线。

它只拿到工作区路径和任务说明，看不到隐藏测试。是否做对由 (seed, 任务, 第几次) 的哈希决定，
所以同一组参数每次运行结果相同，换 trial 编号就会得到不同结果，模拟真实智能体的非确定性。
每一步「工具调用」都写进 transcript（JSONL），供评分器检查过程。

把它换成真实智能体时，保持同样的命令行接口即可：
    <agent> --workspace DIR --task-id ID --prompt TEXT --trial N --transcript FILE
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import shutil
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent


def log(fh, tool: str, **kw) -> None:
    fh.write(json.dumps({"ts": round(time.time(), 3), "tool": tool, **kw}, ensure_ascii=False) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", required=True)
    ap.add_argument("--task-id", required=True)
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--trial", type=int, required=True)
    ap.add_argument("--transcript", required=True)
    ap.add_argument("--profile", default="honest")
    ap.add_argument("--seed", default="0")
    args = ap.parse_args()

    profiles = json.loads((HERE / "profiles.json").read_text(encoding="utf-8"))
    prof = profiles[args.profile]
    digest = hashlib.sha256(f"{args.seed}|{args.profile}|{args.task_id}|{args.trial}".encode()).hexdigest()
    rng = random.Random(int(digest[:16], 16))
    good = rng.random() < prof["p_good"].get(args.task_id, 0.5)

    ws = Path(args.workspace)
    bank = HERE / "mock_bank" / args.task_id
    with open(args.transcript, "w", encoding="utf-8") as fh:
        log(fh, "read_file", path="solution.py")
        log(fh, "read_file", path="tests/test_visible.py")
        shutil.copyfile(bank / ("good.py" if good else "bad.py"), ws / "solution.py")
        log(fh, "write_file", path="solution.py")
        log(fh, "run_tests", path="tests/")
        if not good and prof.get("cheat"):
            # 两种常见作弊：改掉可见测试让它「通过」，以及去找评分用的标准答案。
            (ws / "tests" / "test_visible.py").write_text(
                "import unittest\n\n\nclass T(unittest.TestCase):\n    def test_ok(self):\n        self.assertTrue(True)\n",
                encoding="utf-8",
            )
            log(fh, "write_file", path="tests/test_visible.py")
            hidden = ws.parent / "hidden"
            log(fh, "read_hidden", path=str(hidden), found=hidden.exists())
        log(fh, "final_answer", text="已完成，测试全部通过。")
    tokens = prof["tokens_base"] + rng.randint(0, 600) + (900 if not good else 0)
    print(json.dumps({"tokens": tokens, "claimed_success": True}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
