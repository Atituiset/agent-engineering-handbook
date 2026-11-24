"""用 Python API 跑 Inspect 版评测，打印每个 reducer 的结果；任何一个分数缺失就以非零状态退出。"""
from __future__ import annotations

import sys
from pathlib import Path

from inspect_ai import eval as inspect_eval

sys.path.insert(0, str(Path(__file__).resolve().parent))
from agent_eval import agent_regression  # noqa: E402

logs = inspect_eval(agent_regression(epochs=5), model="mockllm/model", log_dir="inspect/logs", display="none")
log = logs[0]
print("status:", log.status)
found = False
for s in log.results.scores:
    for name, m in s.metrics.items():
        found = True
        print(f"{s.name:<16} reducer={s.reducer!s:<10} {name:<9} {m.value:.3f}")
sys.exit(0 if log.status == "success" and found else 1)
