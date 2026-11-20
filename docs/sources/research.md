# 研究与数据

> 对照实验、调查与论文。这是本报告中证据等级最高的一组，但也要注意：大多数研究有时间窗口（模型代际变化很快）、样本与场景局限。下面同时列出「支持」与「反对」常见做法的结果。

[[toc]]

## 生产力：感知与现实

### RS01 · Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity {#rs01}
**机构**：METR｜**日期**：2025-07-10｜[原文](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

随机对照试验：16 位资深开源开发者在自己长期贡献的大型仓库（平均 2.2 万+ 星、100 万+ 行代码）上完成 246 个真实 issue，随机分配允许或禁止使用 AI。结果：**使用 AI 时完成时间反而长 19%**；开发者事前预期 AI 会让自己快 24%，事后仍认为快了 20%。METR 强调这只是 2025 年初能力在特定场景下的快照。2026-02 的后续实验见 [RS09](#rs09)。

> "developers expected AI to speed them up by 24%, and even after experiencing the slowdown, they still believed AI had sped them up by 20%."

`对照实验；场景局限：熟悉代码库的资深开发者、早期 2025 工具`

### RS09 · We are Changing our Developer Productivity Experiment Design（METR 后续实验） {#rs09}
**机构**：METR｜**日期**：2026-02-24｜[原文](https://metr.org/blog/2026-02-24-uplift-update/)

RS01 的后续。2025 年 8 月起的新实验共 57 位开发者（10 位来自原研究，47 位新招募）、143 个仓库、800 多个任务。原始结果：原研究的回访开发者完成时间变化 −18%（置信区间 −38% 到 +9%），新招募开发者 −4%（置信区间 −15% 到 +9%），即点估计转为加速，但区间都跨过 0。METR 明确认为这组数据**信号不可靠**：越来越多开发者因为不愿在不用 AI 的条件下工作而拒绝参加；30%–50% 的受访者承认不提交那些「不想在没有 AI 时做」的任务；报酬从每小时 150 美元降到 50 美元也带来选择偏差；同时并行使用多个智能体的人很难准确记录用时。METR 判断真实加速可能更高，上述估计更像下限，并已着手改用其他实验设计。

`对照实验（后续）；作者自评为弱证据：选择效应严重`

### RS02 · The Impact of AI on Developer Productivity: Evidence from GitHub Copilot {#rs02}
**作者**：Sida Peng, Eirini Kalliamvakou, Peter Cihon, Mert Demirer｜**日期**：2023-02-13｜[原文](https://arxiv.org/abs/2302.06590)

受控实验：让开发者尽快用 JavaScript 实现一个 HTTP 服务器，使用 Copilot 的实验组比对照组快 55.8%。常被引用为「AI 提效」的证据，但任务是小型、定义清晰的绿地任务，与 RS01 的场景几乎相反——两者合读才能看到全貌：**提效强烈依赖任务类型与对代码库的熟悉程度**。

### RS03 · State of AI-assisted Software Development 2025 {#rs03}
**机构**：DORA（Google Cloud）｜**日期**：2025｜[原文](https://dora.dev/research/2025/dora-report/)

年度报告的核心结论：AI 的主要角色是**放大器**，放大组织既有的优势与弱点；AI 投资的最大回报不来自工具本身，而来自对底层组织系统（平台、流程、实践）的战略性投入。这与本手册「harness 先于模型」的主线一致。

### RS04 · 2025 Stack Overflow Developer Survey — AI {#rs04}
**机构**：Stack Overflow｜**日期**：2025｜[原文](https://survey.stackoverflow.co/2025/ai)

84% 的受访者正在或计划在开发流程中使用 AI 工具（上年为 76%），51% 的专业开发者每天使用。采用率已不是问题，问题在于如何用好。

## 代码质量

### RS05 · AI Copilot Code Quality: 2025 Look Back at 12 Months of Data {#rs05}
**机构**：GitClear｜**日期**：2025｜[原文](https://www.gitclear.com/ai_assistant_code_quality_2025_research)

分析 2020–2024 年 2.11 亿行变更代码：与重构相关的「移动」代码占比从 2021 年的 25% 降至 2024 年的不到 10%，被归类为「复制/粘贴」的代码从 8.3% 升至 12.3%；代码克隆增长 4 倍，「复制粘贴」首次超过「移动」。说明 AI 辅助下 DRY 与重构习惯正在退化——需要用工具与流程主动对冲。

`厂商研究（GitClear 销售代码分析产品），相关性而非因果`

## 上下文文件到底有没有用？（存在争议）

### RS06 · Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents? {#rs06}
**机构**：arXiv 预印本｜**日期**：2026-02-12｜[原文](https://arxiv.org/abs/2602.11988)

在 SWE-bench 任务（LLM 生成的上下文文件）与一组带有开发者提交上下文文件的真实仓库 issue 上评估：**提供上下文文件总体上没有提高任务成功率，却让推理成本平均增加 20% 以上**；该结论跨模型、跨智能体、跨 LLM 生成与人工编写的文件都成立。细节：文件中的指令确实被很好地遵守，但被厂商推荐的「仓库概览」并无帮助。结论：上下文文件适合用来规定**非标准的编码实践**，任何提效尝试都应在部署前严格评估。

> "context files are useful for specifying non-standard coding practices"

### RS07 · Instruction Adherence in Coding Agent Configuration Files: A Factorial Study {#rs07}
**作者**：Damon McMillan｜**日期**：2026-05-11｜[原文](https://arxiv.org/abs/2605.10039)

在两个 TypeScript 代码库上运行 1,650 次 Claude Code CLI 会话，操纵四个文件结构变量（文件大小、指令位置、文件架构、相邻文件中的矛盾）。**四个结构变量及其两两交互均未产生可检测的影响**；最大的效应来自会话内部：智能体每多生成一个函数，遵守指令的几率约下降 5.6%。启示：与其纠结规则文件怎么排版，不如控制会话长度、把关键约束交给确定性检查。

`单作者预印本、单一简单目标指令，外推需谨慎`

### RS08 · Hacker News 讨论：AGENTS.md 研究 {#rs08}
**机构**：Hacker News 社区｜**日期**：2026-03-08｜[原文](https://news.ycombinator.com/item?id=47295454)

围绕 RS06 论文的社区讨论帖。热度不高（核对时约 20 分），列出仅为方便读者查看从业者对该结论的不同反应；本报告不据此得出任何结论。

## 工业论文与基准（2026-11 增补） {#industry-papers}

以下论文与基准来自腾讯、阿里、字节团队，数字均为团队自报、尚未独立验证。

### 阿里 · AL12 · Qwen3-Coder：在世界中自主编程（Agent RL 与 2 万并行环境） {#al12}
**作者/机构**：通义千问 Qwen 团队｜**日期**：2025-07｜[原文](https://qwenlm.github.io/zh/blog/qwen3-coder/)

模型侧的“验证闭环”：通过自动扩展测试样例构造可验证的 RL 训练实例；Agent RL 的主要难点是环境扩展，借助阿里云基础设施同时运行 2 万个独立环境做多轮交互训练。与 AL07 的沙箱规模互为印证。

> “借助阿里云的基础设施，实现同时运行 20k 独立环境。”

**证据类型**：团队自述（模型发布博客）｜**对应原则**：[Q09](/handbook/12-quality-cicd#q09) [Q02](/handbook/12-quality-cicd#q02)

### 字节 · BD05 · Trae Agent：测试时扩展的软件工程 Agent（SWE-bench Verified 第一） {#bd05}

**作者/机构**：Trae Research Team（字节跳动，arXiv）｜**日期**：2025-07｜[原文](https://arxiv.org/abs/2507.23370)｜[相关链接](https://github.com/bytedance/trae-agent)

> **2026-11 注**：SWE-bench Verified 已被 OpenAI 停止使用、被 Epoch AI 评为「有缺陷」（[OA11](./openai#oa11)、[RS11](#rs11)）。下面的「第一」是当时的榜单排名，不宜再作为能力证据引用。

把 issue 修复当作“最优解搜索”：生成多个候选补丁，再由剪枝与选择 Agent 收敛，解决集成空间大与仓库级理解两大难题；开源为 bytedance/trae-agent。注意 75.20% 是排行榜成绩，不代表内部业务交付质量。

> “Trae Agent has achieved first place on the SWE-bench Verified leaderboard, with a notable Pass@1 score of 75.20%.”

**证据类型**：论文（基准成绩，团队自报）｜**对应原则**：[P10](/compare/evidence#p10) [Q07](/handbook/12-quality-cicd#q07) [Q08](/handbook/12-quality-cicd#q08)

### 字节 · BD20 · Repo2Run：大规模自动构建代码仓库可执行环境（NeurIPS 2025） {#bd20}
**作者/机构**：字节跳动（GitHub 开源）｜**日期**：2025｜[原文](https://github.com/bytedance/Repo2Run)

Agent 能不能验证，取决于仓库能不能跑起来：LLM Agent 在 Docker 沙箱里自动配置环境、为 Python 仓库生成无错的 Dockerfile。是 SWE 训练与评测（Multi-SWE-bench 等）背后的环境基建。

> “Repo2Run: Automated Building Executable Environment for Code Repository at Scale”

**证据类型**：开源仓库（论文配套）｜**对应原则**：[Q09](/handbook/12-quality-cicd#q09) [P15](/compare/evidence#p15)

## 评测方法与基准的局限（2026-11 增补） {#eval-methods}

### RS10 · τ-bench：工具-智能体-用户交互的基准与 pass^k 指标 {#rs10}
**作者**：Shunyu Yao、Noah Shinn 等｜**日期**：2024-06｜[原文](https://arxiv.org/abs/2406.12045)

模拟用户与带领域 API 和政策规则的智能体对话，用对话结束时的数据库状态与目标状态比对来评分。论文提出 **pass^k**：同一任务跑 k 次**全部**成功的概率，用来衡量可靠性，区别于「k 次里至少成功一次」的 pass@k。当时最强的函数调用智能体在零售场景成功率不到 50%，pass^8 低于 25%。

`学术论文；场景是客服类工具调用，不是编码`

### RS11 · SWE-bench Verified – Benchmark review（Epoch AI） {#rs11}
**机构**：Epoch AI｜**日期**：2026-09-03｜[原文](https://epoch.ai/benchmarks/swe-bench-verified/review)

第三方基准评审，结论为 **Flawed**。依据包括：Epoch 2025-06 的早期评审已指出污染风险高、结果高度依赖所用脚手架；OpenAI 2026-02 的审计（[OA11](./openai#oa11)）发现 59.4% 被审题目的测试有缺陷，推算至少 16.4% 的题目是坏的；另有研究者找到可以拿满分的 reward hack。

`第三方评审`

## 技能形成与组织能力（2026-11 增补） {#skills-org}

### RS12 · How AI assistance impacts the formation of coding skills（随机对照实验） {#rs12}
**机构**：Anthropic｜**日期**：2026-01｜[原文](https://www.anthropic.com/research/AI-assistance-coding-skills)｜[论文](https://arxiv.org/abs/2601.20245)

52 位（多数为初级的）软件工程师学习一个不熟悉的 Python 异步库 Trio 并完成两个功能，随后测验。用 AI 的组平均 50 分，手写组 67 分，差距在统计上显著；差距最大的是调试题。用 AI 的组平均快约两分钟，但不显著。用法决定结果：完全交给 AI 写或靠 AI 调试的人得分最低（低于 40%）；用 AI 提问概念、要解释、生成后追问理解的人得分在 65% 以上。作者提醒样本小、只测了学习后的即时理解。

`随机对照实验（厂商研究团队）；样本小，场景是学习新库`

### RS13 · DORA AI Capabilities Model {#rs13}
**机构**：DORA（Google Cloud）｜**日期**：2025-11（报告页最后更新 2025-11-25）｜[原文](https://dora.dev/ai/capabilities-model/report/)

[RS03](#rs03) 的配套报告。基于 2025 年调查数据，识别出七项能放大 AI 收益的组织能力：清晰且传达到位的 AI 立场、健康的数据生态、AI 可访问的内部数据、扎实的版本控制实践、小批量工作、以用户为中心、高质量的内部平台。报告为每项能力给出落地做法与度量方式。例如它把版本控制称为 AI 时代的「安全网」，要求团队熟练使用回滚。

`调查研究（相关性）`

## 另见

- Meta TestGen-LLM 论文（LLM 生成测试 + 确定性过滤）：[BT10](./bigtech#bt10)
- Meta ACH 变异测试：[BT09](./bigtech#bt09)
- 包幻觉研究：[SC03](./security#sc03)
