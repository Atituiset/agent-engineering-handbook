# 05 · 验证与测试：证明它真的做对了

[[toc]]

## 要点

- **验证能力决定了你能放手多少。** 没有可靠的验证回路，就只能逐行审查；有了，才能并行、才能异步。
- **让智能体自己验证，并给它验证的手段**：能跑测试、能启动服务、能看页面、能读日志。
- **测试也是 AI 写的，所以要验证测试本身**：变异测试、属性测试、端到端测试最难被糊弄。
- **生成者与评判者分离**：写代码的智能体不应该是唯一判断「完成」的那个。
- **作者负责证明**：提交给别人之前，你已经确认它能工作，并附上证据。

## 1. 验证是放大器的「闸门」

Mitchell Hashimoto 总结得最简洁：让智能体一次就做对的最可靠方法，是给它快速、高质量的工具，自动告诉它哪里错了（[PR22](/sources/practitioners#pr22)）。Anthropic 把通用智能体循环归纳为**收集上下文 → 采取行动 → 验证工作 → 重复**（[AN13](/sources/anthropic#an13)）。Claude Code 团队的文章称验证回路决定了能并行多少智能体（[AN18](/sources/anthropic#an18)）。Cognition 观察到异步会话已超过交互式会话，开发者回来时必须看到「已验证、可合并」的结果（[VD09](/sources/vendors#vd09)）。异步委派的完整做法见 [第 14 章](./14-async-agents)。

Simon Willison 的一句话可以作为本章的总纲（[PR04](/sources/practitioners#pr04)）：

> "Your job is to deliver code you have proven to work."

## 2. 给智能体「眼睛」

| 场景 | 手段 | 来源 |
| --- | --- | --- |
| 已有项目开新会话 | 第一件事：先跑一遍测试 | [PR10](/sources/practitioners#pr10) |
| Python 库 | `python -c` 试边界情况 | [PR13](/sources/practitioners#pr13) |
| JSON API | 启动 dev server，用 curl 探索 | [PR13](/sources/practitioners#pr13) |
| Web UI | Playwright / 浏览器扩展 / Chrome DevTools Protocol | [PR13](/sources/practitioners#pr13)、[X06](/sources/x-posts#x06)、[OA01](/sources/openai#oa01) |
| 移动端 | 模拟器 + MCP | [X06](/sources/x-posts#x06) |
| 后端 | 能一键启动完整服务；日志与指标可查询 | [X06](/sources/x-posts#x06)、[OA01](/sources/openai#oa01) |
| 开发服务器 | 让 dev server 日志对智能体可见 | [PR17](/sources/practitioners#pr17) |
| 固化验证流程 | 写一个 `verify` skill，让智能体真正运行改动 | [AN18](/sources/anthropic#an18)、[AN05](/sources/anthropic#an05) |

OpenAI 让每个 git worktree 都能独立启动应用实例，并把 LogQL/PromQL 查询开放给智能体，使「服务启动在 800 毫秒内完成」这类要求变得可验证（[OA01](/sources/openai#oa01)）。Cognition 把登录等重复步骤固化，并用带标注截图的测试报告方便人快速复核（[VD09](/sources/vendors#vd09)）。

**测试全过 ≠ 能用。** Simon Willison 提醒：服务器可能启动就崩、关键 UI 元素可能不显示，所以除了自动化测试，还要让智能体做「手工测试」，发现问题后再补进永久测试（[PR13](/sources/practitioners#pr13)）。

## 3. 选对测试类型

Claude Code 团队推荐三类「最难被糊弄」的测试（[AN18](/sources/anthropic#an18)）：

- **端到端测试**：从用户视角验证完整行为。
- **属性测试**：往返、不变量、幂等、等价性。输入由生成器产生，不带写代码的智能体的偏见（[TW36](/sources/thoughtworks#tw36)）。
- **差分测试**：迁移或重写时以旧系统为 oracle。Kent Beck 先用 Python 把算法做扎实，再让智能体转写到 Rust，测试保持不变（[PR15](/sources/practitioners#pr15)）。

### 验证测试本身：变异测试

当测试也是 AI 写的，「测试通过」就不再是强证据。Thoughtworks 雷达把变异测试列为 Adopt，特别指出它可以**确保 AI 生成的测试不是「只会通过」而抓不住逻辑变化**（[TW23](/sources/thoughtworks#tw23)）。Meta 的 ACH 反过来用变异引导测试生成：先生成现有测试抓不住的缺陷，再生成能抓住它们的测试（[BT09](/sources/bigtech#bt09)）。Meta 的 TestGen-LLM 则用「能构建、稳定通过、确实提升覆盖」三道确定性过滤器筛选生成的测试（[BT10](/sources/bigtech#bt10)）。

## 4. TDD 在智能体循环里：分歧

| 观点 | 来源 |
| --- | --- |
| **支持**：「Use red/green TDD」是一句简洁有效的提示，同时防住「代码不工作」和「写了用不到的代码」；关键是确认测试**先失败** | Simon Willison（[PR09](/sources/practitioners#pr09)） |
| **支持**：严格 TDD 作为系统提示；结构性与行为性变更分开提交 | Kent Beck（[PR15](/sources/practitioners#pr15)） |
| **支持并强制**：RED-GREEN-REFACTOR，删除先于测试写出的代码 | Superpowers（[OS08](/sources/open-source#os08)） |
| **支持**：曾是「TDD 反对者」，现在把测试作为核心 | Harper Reed（[PR30](/sources/practitioners#pr30)） |
| **保留**：看着测试变红只有在**有人检查时**才算证据；智能体内部 TDD 带不来人亲自做时的控制感，生成的测试有时偏薄、自我指涉 | Böckeler（[TW04](/sources/thoughtworks#tw04)） |

流水线上的 TDD 做法（测试与实现分会话、判据先行）见 [第 12 章 Q01](./12-quality-cicd#q01)。

**如何调和**：TDD 在智能体循环中的价值主要是**行为约束**（逼它先想清楚预期、防止过度实现），而不是**证据**。证据需要来自智能体之外：人审过的测试用例、变异测试分数、属性测试、端到端测试。推荐组合：**人写或人审关键测试（尤其是验收测试）→ 智能体按 red/green 实现 → 变异测试检验测试质量。**

## 5. 生成者与评判者分离

> 评审流水线中的异构评审做法见 [第 12 章 Q07](./12-quality-cicd#q07)。

Anthropic 的长程应用开发实验发现，**把干活的智能体与评判的智能体分开**是很强的杠杆；但评估者也是 LLM，天然对 LLM 产出偏宽容，需要专门校准（[AN24](/sources/anthropic#an24)）。Cursor 的大规模实验在引入「规划者 / 工作者 / 评判者」分层后解决了大部分协调问题（[VD03](/sources/vendors#vd03)）。Superpowers 每个任务后派发评审（[OS08](/sources/open-source#os08)）。

原则：**评判者的标准要尽量计算化**（测试、lint、截图对比），LLM 评判只用于无法计算化的部分，并且评判标准不能由被评判的变更修改（见第 04 章）。

## 6. 防作弊与升级

- 检查连续失败三轮就升级给人，而不是让智能体无限尝试（[AN18](/sources/anthropic#an18)）。
- 不许用 sleep / 重试掩盖 flaky test（[AN18](/sources/anthropic#an18)；详见 [第 12 章 Q10](./12-quality-cicd#q10)）。
- 监视禁用、删除、跳过测试的迹象（[PR15](/sources/practitioners#pr15)、[CN06](/sources/chinese#cn06)）。
- 用 Stop hook 在「宣布完成」前强制跑测试（[AN03](/sources/anthropic#an03)）。

## 7. 长程任务的验证结构

- **功能清单 + 进度文件**：初始化智能体建立功能清单，增量智能体每次只推进一项并更新进度（[AN17](/sources/anthropic#an17)）。
- **带验收标准的里程碑**：OpenAI 25 小时任务用 `plans.md` 记录里程碑与验收标准（[OA06](/sources/openai#oa06)）。
- **测试即护栏**：Carlini 用 16 个并行智能体写 C 编译器时，经验重点是如何写测试让无人监督的智能体不跑偏（[AN29](/sources/anthropic#an29)）。
- **完成标准要高**：Meta Forum 团队把完成标准从「能编译」提高到「自动化测试与视觉检查通过」（[BT12](/sources/bigtech#bt12)）。

## 8. 评测：为团队的 harness 建回归

当你调整 AGENTS.md、skills、hooks 时，怎么知道变好了还是变坏了？Anthropic 指出没有评测的团队只能「等投诉 → 手动复现 → 修 → 祈祷」（[AN31](/sources/anthropic#an31)）。美团把「观测 + 评测 = 持续迭代」作为智能体研发公式（[CN02](/sources/chinese#cn02)）。一个轻量做法：挑 10–20 个代表性任务作为「harness 回归集」，每次改规则或换模型都跑一遍。

建评测时有三个常见的坑：

- **只看结果，不看过程。** Anthropic 把一次试验分成「过程记录」（transcript，智能体说了什么、调了哪些工具）和「结果」（环境的最终状态）：智能体说「订好了」不算，数据库里真有这条预订才算（[AN31](/sources/anthropic#an31)）。结果尽量用确定性检查判定；过程用来抓作弊和越权，例如删测试、改评分脚本、调用了不该用的工具，这些只会出现在过程记录里（[第 12 章 Q04](./12-quality-cicd#q04)）。
- **只跑一次。** 智能体是非确定的。pass@k 指 k 次里至少成功一次，衡量的是能力上限；pass^k 指 k 次全部成功，衡量的是可靠性（[RS10](/sources/research#rs10)）。单次成功率 75% 的智能体，连续 3 次都成功的概率只有约 42%（[AN31](/sources/anthropic#an31)）。无人值守的任务（[第 14 章](./14-async-agents)）更该看 pass^k，所以回归集每个任务至少跑几次。
- **拿公开基准代替自己的评测。** OpenAI 在 2026-02 停止报告 SWE-bench Verified：它审计的题目中有 59.4% 的测试存在缺陷，前沿模型也都在训练中见过部分题目与答案（[OA11](/sources/openai#oa11)）；Epoch AI 的第三方评审结论是「有缺陷」，结果还高度依赖脚手架（[RS11](/sources/research#rs11)）。公开基准的分数只能作为参考，选模型、调 harness 要看你自己仓库的回归集。百度也发现，同样的分数下答对的可能是另一组题（[CN40](/sources/chinese#cn40)）。

> 任务设计、评分器隔离、LLM 裁判校准、基准怎么读，以及一套能跑的最小评测，见 [第 16 章 智能体评测](./16-agent-evals)。

## 2026-11 新证据：把 AI 的结论变成红绿证据 {#new-evidence}

P06「验证闭环」有 298 位独立作者支持，排在前列。P07「TDD」有 67 位，明显少得多。

- **红绿测试作为 AI 结论的判决**：美团存储团队对 AI 全仓评审给出的 117 个疑似问题逐条写测试验证：36 条变红确认，3 条被证伪，其余靠源码确认或尚未验证。他们还发现 CI 报告里硬编码了 failures="0"，所以要让 AI 自己构建、看原始输出（[CN12](/sources/chinese#cn12)）。这同时**加强**了验证闭环，也**修正**了「CI 绿灯即可信」的默认假设。
- **评测看异常值而非分数**：百度文心快码发现，同样的分数下答对的可能是另一组题，因此关注异常值，并从经人审核的真实提交里挖掘评测集（[CN40](/sources/chinese#cn40)）。
- **CI 成为瓶颈**：Linear 因 AI 带来的变更量重做了 CI（[HN23](/sources/hackernews#hn23)）。Peter Steinberger 计划让 Codex 判断哪些测试真正需要跑，大幅削减 CI（[XV-007](/sources/x/verify#xv-007)）。这是对「测试越多越好」的一个实际限定。
- **TDD 的限定**：Armin Ronacher 认为重写系统不一定需要现成的测试套件，可以让智能体专门自建（[XV-012](/sources/x/verify#xv-012)）。腾讯一线团队明确不追求严格 TDD，用规则和自测兜底（团队自报，[TX02](/sources/chinese#tx02)），与第 12 章 [Q01 测试先行](/handbook/12-quality-cicd#q01) 有张力；字节 AEGIS 的“先复现再修”则是测试先行的变体（论文，团队自报，[BD06](/sources/quality/research#bd06)）。
- **把目标从“迁移代码”改成“迁移行为”**（数字均为团队自报、尚未独立验证）：支付宝 60 万行重构用两个相互校验的 Loop 验证（议题摘要，未见全文，[AL27](/sources/quality/chinese#al27)）；字节先生成 bug 复现脚本再修（[BD06](/sources/quality/research#bd06)），NL2Test 自报 85.4% 生成用例进入 CI/CD（[BD10](/sources/quality/chinese#bd10)）。
- **防作弊的国内案例**：阿里云诊断系统里 Agent 曾把 logger.error 改成 logger.warning 就宣称已修复，所以必须独立验证（团队自报，[AL17](/sources/quality/chinese#al17)）；腾讯游戏以“编译 0 error”为量化验收（团队自报，[TX07](/sources/chinese#tx07)）——这是必要但不充分的完成标准，见本章第 7 节。

## 与传统软件工程认知的对比

| 维度 | 传统认知 | 智能体时代 | 判断 | 佐证（支持／异议） |
| --- | --- | --- | --- | --- |
| 测试金字塔 | 大量单元测试、少量 E2E（E2E 慢且脆） | E2E 价值上升：最难被糊弄（[AN18](/sources/anthropic#an18)）；编写与维护成本由智能体承担 | **修正**：金字塔变「更胖的顶部」 | [P06 · 298／18](/compare/evidence#p06) |
| 测试覆盖率 | 覆盖率是质量指标 | 覆盖率很容易被 AI 刷高；变异分数更有意义（[TW23](/sources/thoughtworks#tw23)） | **修正** | [P06 · 298／18](/compare/evidence#p06) |
| TDD | 设计工具 + 回归保障，靠开发者自律 | 作为行为约束有效，作为证据需外部检验（[TW04](/sources/thoughtworks#tw04)） | **分歧** | [P07 · 67／6](/compare/evidence#p07) |
| 属性测试 / 变异测试 | 小众、昂贵，多数团队不用 | 成本骤降、价值上升，雷达升为 Adopt | **反转** | [P06 · 298／18](/compare/evidence#p06) |
| 手工测试 | 应尽量被自动化取代 | 智能体做「手工测试」重新有价值（[PR13](/sources/practitioners#pr13)） | **修正** | [P06 · 298／18](/compare/evidence#p06) |
| 谁写测试 | 写代码的人写测试 | 写代码的智能体不应是唯一的测试作者和评判者（[AN24](/sources/anthropic#an24)） | **修正**：职责分离 | [P07 · 67／6](/compare/evidence#p07) |
| 「写测试太费时」 | 常见的不写测试的理由 | 这个借口不再成立（[PR10](/sources/practitioners#pr10)） | **反转** | [P07 · 67／6](/compare/evidence#p07) |

> 「佐证」列：原则编号 · 独立支持作者数／异议数（疑似 + 人工确认），关键词自动归类，口径见 [共识度/佐证](/compare/evidence)。

**选择理由**：传统测试实践建立在「测试作者是善意且理解需求的人」这一隐含前提上。当测试由一个急于让测试通过的智能体编写时，这个前提消失了，所以要引入**不依赖测试作者诚实性**的验证手段：属性测试（输入非作者选择）、差分测试（以旧系统为准）、变异测试（检验测试的敏感度）、端到端测试（从外部观察行为）。这些技术都不新，只是在智能体时代性价比发生了逆转。

**证据强度**：「验证能力决定自主程度」是**共识**；变异测试作为 AI 测试护栏是**雷达 Adopt**；TDD 的价值是**分歧**；具体数字（如三轮失败升级）是**单一团队经验**。

> **延伸阅读**：交付流水线层面的测试、CI 门禁、AI 评审、Evals 与防作弊做法，见 [第 12 章 · 质量保障](./12-quality-cicd)（含 GitHub Actions 示例与 Q01–Q13 共识度）。
