# 智能体评测：可运行的最小示例

这是手册 [第 16 章「智能体评测」](https://atituiset.github.io/agent-engineering-handbook/handbook/16-agent-evals) 的配套代码。
全部使用**模拟智能体**（`agents/mock_agent.py`），不调用任何模型 API，也不需要 API key。
核心 harness、裁判校准和配对评测只依赖 Python 标准库（3.11+）；promptfoo 和 Inspect 两个版本分别需要 Node 22.22+ 和 `pip install inspect-ai`。

## 目录

| 路径 | 作用 |
| --- | --- |
| `tasks/<id>/task.json` | 任务说明：类型（回归 / 能力）、来源（从哪次真实失败整理来的）、受保护路径、禁用工具 |
| `tasks/<id>/workspace/` | 交给智能体的工作区：待实现的 `solution.py` 和**可见**测试 |
| `tasks/<id>/hidden/` | **隐藏**测试，只有评分器能看到，从不拷进智能体的工作区 |
| `agents/mock_agent.py`、`agents/profiles.json` | 确定性的模拟智能体。`honest` 正常做题；`honest_v2` 模拟改了提示词后某个任务变差；`cheater` 做不出来时会改可见测试、去找隐藏答案 |
| `harness/run_evals.py` | 多次试验的评测 runner：确定性结果检查、过程检查、pass@k / pass^k、成本与延迟 |
| `harness/metrics.py` | pass@k、pass^k 的无偏估计，Wilson 置信区间，分位数 |
| `harness/compare.py` | 回归门禁：和 `baseline.json` 比，掉得超过阈值或出现过程违规就失败 |
| `judge/calibrate.py` | LLM 裁判校准：一致率、Cohen's kappa、失败类召回率与精确率、版本漂移、换位一致性 |
| `vuln/paired_eval.py` | 漏洞检测的配对评测：P-C / P-V / P-R、MCC、笨基线、按训练截止日期分组 |
| `promptfoo/` | 同一套任务的 promptfoo 版（exec provider + python 断言 + `--repeat`） |
| `inspect/` | 同一套任务的 Inspect 版（`epochs` + `pass_at_3` / `pass_k_3` reducer） |
| `tests/test_harness.py` | harness 自身的测试：指标数值、作弊能否被抓到、门禁能否拦住退化 |

CI 配置在仓库根目录的 [`.github/workflows/agent-evals.yml`](../../.github/workflows/agent-evals.yml)。

## 跑起来

```bash
cd examples/evals

# 1. harness 自测
python3 -m unittest discover -s tests -v

# 2. 回归集：每个任务 5 次试验，隔离评分
python3 harness/run_evals.py --agent "python3 agents/mock_agent.py --profile honest" --trials 5 --k 1 3 5 --out results.json
python3 harness/compare.py --baseline baseline.json --current results.json --max-drop 0.02 --k 3

# 3. 对比：作弊的智能体在「直接跑工作区测试」的评分方式下拿满分，在隔离评分下被抓到
python3 harness/run_evals.py --grader naive    --agent "python3 agents/mock_agent.py --profile cheater" --out results-naive.json
python3 harness/run_evals.py --grader isolated --agent "python3 agents/mock_agent.py --profile cheater" --out results-isolated.json

# 4. 模拟一次退化，确认门禁会失败（预期退出码 1）
python3 harness/run_evals.py --agent "python3 agents/mock_agent.py --profile honest_v2" --out results-v2.json
python3 harness/compare.py --baseline baseline.json --current results-v2.json

# 5. 裁判校准与配对漏洞评测
python3 judge/calibrate.py --labels judge/data/labels.csv --judge judge_v1 --compare judge_v2 --pairwise judge/data/pairwise.csv
python3 vuln/paired_eval.py --pairs vuln/data/pairs.jsonl --predictions vuln/data/model_predictions.jsonl --cutoff 2026-06-01

# 6. 框架版本（可选）
PROMPTFOO_DISABLE_TELEMETRY=1 npx promptfoo@0.126.0 eval -c promptfoo/promptfooconfig.yaml --repeat 3 --no-cache --no-share
pip install inspect-ai==0.3.292 && python3 inspect/run_inspect.py
```

## 换成你的智能体

`run_evals.py` 通过命令行调用智能体，接口是：

```
<agent> --workspace DIR --task-id ID --prompt TEXT --trial N --transcript FILE
```

智能体在 `DIR` 里改代码，把每一步工具调用按 JSONL 写进 `FILE`（至少包含 `tool` 字段），最后在标准输出打印一行 JSON，可以带 `tokens`。
把 `--agent` 换成包装你真实智能体（Claude Code、Codex CLI、自研 harness）的脚本即可。promptfoo 和 Inspect 版本读环境变量 `EVAL_AGENT`。

真实场景里还要补上的东西：

- 任务从真实失败里整理，先攒 20–50 个；每个任务写清楚「从哪次失败来」。
- 隐藏测试和评分脚本放在智能体所在的容器 / 机器之外；本示例只用目录隔离来演示，不是安全边界。
- 真实智能体的结果不是确定的，基线要多跑几次、阈值要留出噪声余量；本示例里 5 次试验的抽样噪声已经大到会让没变的任务「看起来变差」。
- CI 里带模型密钥时，fork 来的 PR 不要拿到密钥（见手册第 12 章示例 C）。

## 数据说明

`judge/data/`、`vuln/data/` 和 `agents/profiles.json` 里的数字、C 代码片段和标签都是**为演示人工构造的**，不来自任何真实模型、真实 CVE 或真实评测结果。
