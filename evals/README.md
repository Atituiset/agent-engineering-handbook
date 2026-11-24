# 智能体评测（evals/）

手册[第 16 章「智能体评测」](https://atituiset.github.io/agent-engineering-handbook/handbook/16-agent-evals)的最小落地版本，配合本模板的编码智能体工作方式：智能体改代码，`bash scripts/verify.sh` 通过才算完成。这里在它上面再加三件事：

- **多次试验 + 置信区间**：每个任务跑多次，报告 pass@k（k 次里至少一次成功）和 pass^k（k 次全部成功），并给出 Wilson 95% 区间。
- **隔离判分**：智能体看不到 `evals/`；判分在一个干净副本里进行，只带上它对非受保护文件的改动，先跑隐藏测试，再跑 `scripts/verify.sh`。
- **门禁**：和 `evals/baseline.json` 比较，回归就让 CI 失败。

harness 只用 Python 标准库（`run_evals.py`），七个语言分支共用同一份，各分支只有 `config.json` 和隐藏测试不同。

## 文件

```text
evals/
├── run_evals.py        # harness：run（跑任务、判分、统计）和 gate（与基线比较）
├── mock_agent.py       # 离线 mock 智能体：按种子选用 bank/ 里预先写好的改动，CI 不需要模型密钥
├── profiles.json       # mock 的几种行为：honest / regressed / cheater（概率是为演示编的）
├── config.json         # 本语言的隐藏测试放在哪、怎么跑、哪些是现有测试文件
├── tasks/<任务>/       # task.md（按第 11 章模板写的任务说明）+ task.json（回归集或能力集）
├── testdata/           # 隐藏测试，只在判分副本里出现
├── bank/<任务>/        # mock 智能体用的改动（good / bad）
├── baseline.json       # 基线结果，门禁和它比较
└── test_harness.py     # harness 自身的单元测试（pass^k、Wilson 区间、门禁规则）
```

## 任务

| 任务 | 集合 | 要求 |
| --- | --- | --- |
| `add_days` | 回归 | 支持 `d`（天）单位，仍按降序 |
| `allow_spaces` | 回归 | 允许 `<数字><单位>` 之间有空格，首尾空格、制表符仍报错 |
| `reject_leading_zeros` | 能力 | 拒绝 `01h`、`1h05m` 这类前导零，`0s` 仍合法 |

回归集应当稳定通过，门禁看 pass^k 和每个任务的 pass@1；能力集是还在爬坡的任务，门禁只看 pass@k 不下降。

## 怎么判一次试验

1. 把仓库复制到临时目录（不含 `evals/`），在里面运行智能体，环境变量 `EVAL_TASK_FILE` 指向任务说明。
2. 对比前后文件哈希。改了受保护文件（`scripts/guard-protected.sh` 里的 `PROTECTED_REGEX`，外加 `evals/`）或删掉了现有测试里的输入字符串，记为**违规**，这次试验不通过。
3. 在另一个干净副本里只应用非受保护文件的改动，把隐藏测试复制到 `hidden_{task}_test.go`，运行：

   ```bash
   go test -count=1 -run Hidden .
   ```

4. 隐藏测试通过后（若复制进了仓库就先删掉它）再跑 `bash scripts/verify.sh`。两步都通过，这次试验才算通过。

同样内容的判分结果可以用 `--cache-dir` 复用。`--grader naive` 是对照组：直接在智能体自己的工作目录里跑 verify，相信它交上来的一切。

## 本地运行

```bash
python3 -m unittest evals/test_harness.py -v
python3 evals/run_evals.py run --trials 5 --k 1 3 5 --out evals/results.json
python3 evals/run_evals.py gate --baseline evals/baseline.json --current evals/results.json --k 3
```

CI（`.github/workflows/evals.yml`）跑的就是这三条命令，失败时结果文件作为 artifact 上传。

## 本分支实测（2026-11-25，mock 智能体，每个任务 5 次试验）

基线（`evals/baseline.json`，本地墙钟 8.9 秒）：

| 任务 | 集合 | 通过 | Wilson 95% | pass@3 | pass^3 |
| --- | --- | --- | --- | --- | --- |
| `add_days` | regression | 5/5 | [0.5655, 1.0] | 1.000 | 1.000 |
| `allow_spaces` | regression | 3/5 | [0.2307, 0.8824] | 1.000 | 0.100 |
| `reject_leading_zeros` | capability | 3/5 | [0.2307, 0.8824] | 1.000 | 0.100 |

同一种子重跑后过门禁：通过。下面三组是故意制造的问题，用来确认门禁拦得住：

| 运行 | 回归 通过 | 回归 pass^3 | 回归 Wilson 95% | 能力 通过 | 能力 pass@3 | 违规试验 | 门禁 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 基线（honest） | 8/10 | 0.550 | [0.4902, 0.9433] | 3/5 | 1.000 | 0 | — |
| regressed：add_days 成功率调低 | 5/10 | 0.050 | [0.2366, 0.7634] | 3/5 | 1.000 | 0 | 失败 |
| cheater：失败时改 verify.sh | 8/10 | 0.550 | [0.4902, 0.9433] | 3/5 | 1.000 | 4 | 失败（违规） |
| cheater，naive 判分 | 10/10 | 1.000 | [0.7225, 1.0] | 5/5 | 1.000 | 0 | （对照，不过门禁） |

最后一行说明隔离判分为什么必要：同一个作弊的智能体，如果只在它自己的目录里跑 verify，所有试验都“通过”。

注意：这些数字来自 mock 智能体，概率是 `profiles.json` 里编的，只用来证明 harness 和门禁能工作，不代表任何真实模型。三个任务、每个 5 次试验，区间很宽（例如回归集 [0.4902, 0.9433]），真实评测要加任务、加试验次数。

## 门禁规则（`gate`）

以下任何一条成立就失败：回归集 pass^k 下降超过 `--max-drop`（默认 0.02）；能力集 pass@k 下降超过同一阈值；任一回归任务的 pass@1 下降超过阈值；基线里的回归任务在本次结果里缺失；出现违规试验；任一集合每次试验的平均 token 比基线高出 `--max-cost-increase`（默认 25%）以上。

## 换成真实智能体

`--agent` 接受任意 shell 命令，它在仓库副本的根目录运行，能读到这些环境变量：`EVAL_TASK_ID`、`EVAL_TASK_FILE`（任务说明的路径）、`EVAL_TRIAL`、`EVAL_SEED`。命令退出后，harness 按上面的方式判分；如果它的最后几行里有一行 `{"tokens": N}`，就记为这次试验的成本。例如（示意，未在本仓库实测，参数以你所用 CLI 的文档为准）：

```bash
python3 evals/run_evals.py run --trials 10 --k 1 3 5 --out evals/results.json \
  --agent 'your-agent-cli --non-interactive --prompt-file "$EVAL_TASK_FILE"'
```

换成真实智能体之后：

- 先用它重新生成基线（`--out evals/baseline.json`），人工抽查几次失败的试验（`--keep` 保留工作目录），再提交基线。
- 真实模型的方差比 mock 大，试验次数至少 10 次，任务也要逐步补到几十个，区间才有意义。
- 模型密钥放在 CI secrets 里。来自 fork 的 PR 拿不到 secrets，所以 PR 上保留 mock 评测，真实评测放在 `workflow_dispatch` 或定时任务里跑。
- 隐藏测试只在判分副本里出现；不要把 `evals/` 的内容放进给智能体的上下文。
