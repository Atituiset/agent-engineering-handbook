# 国内大厂对比：腾讯 · 阿里 · 字节

> 本页基于 [国内大厂专题](/sources/cn-bigtech/) 的 74 条精选和 291 条全量资料，比较三家如何把大模型与编码智能体用进软件工程，并与美国大厂的公开实践、本手册的原则对照。**文中所有数字都是团队自报、尚未独立验证**；会议条目只有议题摘要。检索与核对时间：2026-11 中旬（北京时间）。

## 一句话结论 {#tldr}

三家都自报 AI 生成代码的比例已经很高（腾讯“大部分团队 90% 以上”、蚂蚁“很多团队 90% 以上”、TRAE 团队“90% 以上”），**但也都公开承认交付效率没有同比放大**，于是在 2026 年不约而同地把重心从“生成”转到 **Harness/Loop 工程、可验证交付和结果指标**。差别主要在路线：腾讯偏 **工程体系与官方长文复盘**，阿里偏 **平台与基础设施（沙箱、评审、运行时）+ 会议议题**，字节偏 **论文与开源（BitsAI、Trae Agent、基准）**。

## 一表看三家 {#table}

| 维度 | 腾讯 | 阿里（含蚂蚁） | 字节 |
| --- | --- | --- | --- |
| 主力工具 | CodeBuddy（IDE/CLI）、WorkBuddy | Aone Copilot/Aone Agent、通义灵码、Qoder、Qwen Code、蚂蚁 CodeFuse | TRAE（含 SOLO）、豆包 MarsCode、飞书 CodeM、火山引擎 AgentKit |
| 公开的规模数字（团队自报、尚未独立验证） | 超 90% 工程师使用 CodeBuddy，50% 新增代码 AI 辅助生成，编码时间 -40%（[TX08](/sources/cn-bigtech/tencent#tx08)）；接受率 23%/不到 30%→大部分团队 90%+（[TX10](/sources/cn-bigtech/tencent#tx10)、[TX11](/sources/cn-bigtech/tencent#tx11)） | 集团插件日活约 1.2 万、渗透率约 65%、补全采纳率约 28%（[AL01](/sources/cn-bigtech/alibaba#al01)）；阿里云 AI 辅助生成近 40%（2025-05，[AL03](/sources/cn-bigtech/alibaba#al03)）；菜鸟 10%→80%+（[AL19](/sources/cn-bigtech/alibaba#al19)）；蚂蚁很多团队 90%+（[AL26](/sources/cn-bigtech/alibaba#al26)） | 超 92% 工程师使用 TRAE（[BD02](/sources/cn-bigtech/bytedance#bd02)）；一年 AI 代码贡献率增长 6 倍多、合入率增长超 2 倍；TRAE 团队 90%+ 代码由 AI 写（[BD01](/sources/cn-bigtech/bytedance#bd01)） |
| 承认的“没放大” | 个人提效≠组织提效，北极星改为“需求吞吐率”（[TX10](/sources/cn-bigtech/tencent#tx10)、[TX23](/sources/cn-bigtech/tencent#tx23)） | 编码只占交付总时长 20%–30%，极端链路编码 1 小时、交付约 21 天（[AL07](/sources/cn-bigtech/alibaba#al07)）；“局部生码提速、全局交付不提效”（[AL18](/sources/cn-bigtech/alibaba#al18)） | 90% AI 代码，人均需求吞吐率只到 1.6 倍；反对把贡献率当 KPI（[BD01](/sources/cn-bigtech/bytedance#bd01)） |
| Harness / Loop | CDN 五层 Harness（[TX03](/sources/cn-bigtech/tencent#tx03)）、QQ 音乐大仓 Harness（[TX05](/sources/cn-bigtech/tencent#tx05)）、游戏 UE 证据链（[TX07](/sources/cn-bigtech/tencent#tx07)）、SRE GitOps（[TX17](/sources/cn-bigtech/tencent#tx17)）、ADP 平台（[TX06](/sources/cn-bigtech/tencent#tx06)）、LoopForge（[CN20](/sources/chinese#cn20)） | Harness→Loop 两级（[AL28](/sources/cn-bigtech/alibaba#al28)）、云诊断 Loop（[AL17](/sources/cn-bigtech/alibaba#al17)）、Qoder 专家团（[AL23](/sources/cn-bigtech/alibaba#al23)）、蚂蚁数科 Harness（[CN03](/sources/chinese#cn03)） | “可交付性”实验：接入 Harness 后 40–60 分→约 80 分（[BD01](/sources/cn-bigtech/bytedance#bd01)）；AgentKit 自治等级（[BD15](/sources/cn-bigtech/bytedance#bd15)）；飞书 CodeM 通过“驾驭工程”评估（[BD18](/sources/cn-bigtech/bytedance#bd18)） |
| 规范 / 计划 | 意图驱动工具链（[TX14](/sources/cn-bigtech/tencent#tx14)）、AGENTS.md 分层规则（[TX02](/sources/cn-bigtech/tencent#tx02)） | Qoder Spec First（[AL15](/sources/cn-bigtech/alibaba#al15)）、蚂蚁 SDD（[AL24](/sources/cn-bigtech/alibaba#al24)）、架构师 Agent（[AL06](/sources/cn-bigtech/alibaba#al06)） | Spec 作为任务合约（[BD15](/sources/cn-bigtech/bytedance#bd15)）、TRAE 内置 Plan/Spec 工作流（[BD14](/sources/cn-bigtech/bytedance#bd14)） |
| AI 代码评审 | 3 模型对抗式 CR（[TX03](/sources/cn-bigtech/tencent#tx03)）；写与审必须用不同 AI（[TX11](/sources/cn-bigtech/tencent#tx11)）；AI 参与 94% 评审（[TX08](/sources/cn-bigtech/tencent#tx08)）；TME 异构多 Agent + SonarQube 联动（[TX18](/sources/cn-bigtech/tencent#tx18)）；AICR（[QC06](/sources/quality/chinese#qc06)） | Open Code Review 精度优先 + 确定性工程（[AL08](/sources/cn-bigtech/alibaba#al08)、[AL10](/sources/cn-bigtech/alibaba#al10)）；AACR-Bench 带负样本（[AL11](/sources/cn-bigtech/alibaba#al11)）；约 20% CR 问题由 AI 发现（[AL01](/sources/cn-bigtech/alibaba#al01)） | BitsAI-CR（[QC09](/sources/quality/chinese#qc09)）；TRAE 提交前智能体审查（[BD14](/sources/cn-bigtech/bytedance#bd14)） |
| 测试 / CI | 测试智能体“质量执行系统”（[TX15](/sources/cn-bigtech/tencent#tx15)）、测试 Agent 记忆（[TX16](/sources/cn-bigtech/tencent#tx16)）、微信 CAT（[TX20](/sources/cn-bigtech/tencent#tx20)）、WeTest（[TX21](/sources/cn-bigtech/tencent#tx21)） | 单测生成采纳率约 50%（[AL05](/sources/cn-bigtech/alibaba#al05)）、飞猪用例采纳率 85%+（[AL21](/sources/cn-bigtech/alibaba#al21)）、支付宝“迁移行为”双 Loop（[AL27](/sources/cn-bigtech/alibaba#al27)）、AE 线上 Bug -80%（[AL20](/sources/cn-bigtech/alibaba#al20)） | LogSage 进 CI/CD（[BD04](/sources/cn-bigtech/bytedance#bd04)）、BitsAI-Fix（[BD03](/sources/cn-bigtech/bytedance#bd03)）、TestGPT-Server（[BD07](/sources/cn-bigtech/bytedance#bd07)）、单测生成（[BD09](/sources/cn-bigtech/bytedance#bd09)）、NL2Test（[BD10](/sources/cn-bigtech/bytedance#bd10)）、AEGIS 复现（[BD06](/sources/cn-bigtech/bytedance#bd06)） |
| 沙箱 / 执行环境 | CubeSandbox（MicroVM + 快照，[TX19](/sources/cn-bigtech/tencent#tx19)） | OpenSandbox 内部周创建超千万、约两三千应用可完整复原（[AL07](/sources/cn-bigtech/alibaba#al07)）；Qwen3-Coder 2 万并行 RL 环境（[AL12](/sources/cn-bigtech/alibaba#al12)） | Repo2Run（[BD20](/sources/cn-bigtech/bytedance#bd20)）；AIO Sandbox、SandboxFusion（全量库） |
| 评测 / 可观测 | A.S.E 安全评测（[TX22](/sources/cn-bigtech/tencent#tx22)）；ADP 轨迹 replay/eval（[TX06](/sources/cn-bigtech/tencent#tx06)） | AgentLoop 评估 Agent 查证打分（[AL22](/sources/cn-bigtech/alibaba#al22)）、生产录制回放评测（[AL29](/sources/cn-bigtech/alibaba#al29)）、LoongSuite Pilot 遥测（[AL30](/sources/cn-bigtech/alibaba#al30)）、PIBench（[AL31](/sources/cn-bigtech/alibaba#al31)） | Multi-SWE-bench（[BD08](/sources/cn-bigtech/bytedance#bd08)）、AgentOps 评测（[BD16](/sources/cn-bigtech/bytedance#bd16)）、Agent 观测（[BD17](/sources/cn-bigtech/bytedance#bd17)） |
| 第三方的反方证据 | 本轮未找到针对腾讯工具的独立测评 | 社区复测 Open Code Review 精度约 12%（作者称已修复，[AL09](/sources/cn-bigtech/alibaba#al09)）；对 Qwen3-Coder 的安全测评及其方法争议（全量库） | Trae 关闭遥测后仍上报（[BD19](/sources/cn-bigtech/bytedance#bd19)） |

## 各家的特点 {#distinctive}

### 腾讯：工程体系 + 坦率复盘

- **把“自检”从流程里拿掉**：多模型对抗评审（[TX03](/sources/cn-bigtech/tencent#tx03)）、“写与审必须是不同的 AI”（[TX11](/sources/cn-bigtech/tencent#tx11)）、异构多 Agent 评审（[TX18](/sources/cn-bigtech/tencent#tx18)）——是三家里异构评审讲得最明确的。
- **愿意写局限**：CDN 案例同时写了“5 天→1 天”和“方案非最优”（[TX03](/sources/cn-bigtech/tencent#tx03)）；图谱实验写明 58%→65% 只是子任务信号（[TX01](/sources/cn-bigtech/tencent#tx01)）；Vibe Flowing 坦言不追求严格 TDD、覆盖率只作参考值（[TX02](/sources/cn-bigtech/tencent#tx02)）。
- **指标口径变化最清楚**：2024 年看补全采纳率（[TX12](/sources/cn-bigtech/tencent#tx12)），2025 年看 AI 代码占比与评审贡献（[TX09](/sources/cn-bigtech/tencent#tx09)），2026 年改看需求吞吐率（[TX10](/sources/cn-bigtech/tencent#tx10)）。

### 阿里（含蚂蚁）：平台与基础设施

- **把验证环境当一等公民**：OpenSandbox、应用级环境复原（[AL07](/sources/cn-bigtech/alibaba#al07)），以及 RL 训练的 2 万并行环境（[AL12](/sources/cn-bigtech/alibaba#al12)）。这与手册“验证决定你能放手多少”一致，只是阿里把它做成了平台。
- **评审做成开源产品 + 基准**：Open Code Review、AACR-Bench（[AL08](/sources/cn-bigtech/alibaba#al08)、[AL11](/sources/cn-bigtech/alibaba#al11)），并公开承认“精度优先、召回更低”的取舍；也正因为开源，才有了社区复测（[AL09](/sources/cn-bigtech/alibaba#al09)）。
- **蚂蚁的“可验证交付”**：迁移行为而非迁移代码（[AL27](/sources/cn-bigtech/alibaba#al27)）、Harness→Loop（[AL28](/sources/cn-bigtech/alibaba#al28)）、生产录制回放评测（[AL29](/sources/cn-bigtech/alibaba#al29)）、人从“环内”到“环上”（[AL25](/sources/cn-bigtech/alibaba#al25)）。

### 字节：论文与开源，度量最直白

- **工业论文最多**：BitsAI-CR/Fix、LogSage、TestGPT-Server、AEGIS、NL2Test（[BD03](/sources/cn-bigtech/bytedance#bd03)、[BD04](/sources/cn-bigtech/bytedance#bd04)、[BD07](/sources/cn-bigtech/bytedance#bd07)、[BD06](/sources/cn-bigtech/bytedance#bd06)、[BD10](/sources/cn-bigtech/bytedance#bd10)），多数把 AI 放在 **CI/静态分析/测试** 这些可判定的环节。
- **最直白的度量反思**：“90% AI 代码 ≠ 10 倍交付”，并用“正确率 vs 可交付性”两轴说明 Harness 的价值（[BD01](/sources/cn-bigtech/bytedance#bd01)）。
- **基准与环境**：Multi-SWE-bench、Repo2Run、Trae Agent（[BD08](/sources/cn-bigtech/bytedance#bd08)、[BD20](/sources/cn-bigtech/bytedance#bd20)、[BD05](/sources/cn-bigtech/bytedance#bd05)）——注意排行榜成绩不代表业务交付质量。

## 自报数字一览（团队自报、尚未独立验证） {#metrics}

| 公司 | 指标 | 数值 | 口径 / 注意 | 来源 |
| --- | --- | --- | --- | --- |
| 腾讯 | 新增代码中 AI 辅助生成占比 | 50%（2025） | “辅助生成”，官方年度报告 | [TX08](/sources/cn-bigtech/tencent#tx08) |
| 腾讯 | AI 参与代码评审 / AI 发现并被采纳的缺陷 | 94% / 28% | 参与度 ≠ 有效检出率 | [TX08](/sources/cn-bigtech/tencent#tx08) |
| 腾讯 | AI 代码占比、AI 评审贡献占比 | 35%→50%，12%→35% | 2024→2025 | [TX09](/sources/cn-bigtech/tencent#tx09) |
| 腾讯 | 大部分团队 AI 生成代码占比 | 90%+（2025 年底） | 高管口述 | [TX10](/sources/cn-bigtech/tencent#tx10)、[TX11](/sources/cn-bigtech/tencent#tx11) |
| 腾讯 | Bug 定位成功率（内部试验） | 58%→65% | 单一子任务，作者提醒不可外推 | [TX01](/sources/cn-bigtech/tencent#tx01) |
| 阿里 | 插件渗透率 / 补全采纳率 | 约 65% / 约 28% | 2025 年中，集团研发平台 | [AL01](/sources/cn-bigtech/alibaba#al01) |
| 阿里 | 阿里云 AI 辅助代码生成比例 | 近 40%（2025-05） | 媒体采访 | [AL03](/sources/cn-bigtech/alibaba#al03) |
| 阿里 | 编码占软件交付总时长 | 20%–30% | 论坛发言 | [AL07](/sources/cn-bigtech/alibaba#al07) |
| 阿里 | 单测生成采纳率 | 约 50% | 单一实践总结 | [AL05](/sources/cn-bigtech/alibaba#al05) |
| 阿里 | AE 重构后线上 Bug | -80% | 议题摘要 | [AL20](/sources/cn-bigtech/alibaba#al20) |
| 阿里 | 云诊断 ERROR / 同类问题修复时长 | 1210→47 条/周，48→15 分钟 | 引自转载页 | [AL17](/sources/cn-bigtech/alibaba#al17) |
| 蚂蚁 | 很多团队 AI 生成代码占比 | 90%+ | 议题摘要 | [AL26](/sources/cn-bigtech/alibaba#al26) |
| 字节 | AI 代码贡献率 / token / 合入率 | 一年 6 倍多 / 5 倍 / 2 倍多 | 增长倍数，非绝对值 | [BD01](/sources/cn-bigtech/bytedance#bd01) |
| 字节 | TRAE 团队 AI 写的代码 / 人均需求吞吐率 | 90%+ / 1.6 倍 | 同一团队两项指标对照 | [BD01](/sources/cn-bigtech/bytedance#bd01) |
| 字节 | 可交付性（同 Prompt 对照实验） | 40–60 分→约 80 分 | 评分标准为团队自定义 | [BD01](/sources/cn-bigtech/bytedance#bd01) |
| 字节 | BitsAI-Fix 修复准确率 | 约 85%（5,000+ 工程师） | 论文自报 | [BD03](/sources/cn-bigtech/bytedance#bd03) |
| 字节 | LogSage 端到端精度 | 超 80%（107 万+ 次执行） | 论文自报 | [BD04](/sources/cn-bigtech/bytedance#bd04) |
| 字节 | NL2Test 生成用例进入 CI/CD | 85.4% | 公众号文章 + 论文（论文匿名公司） | [BD10](/sources/cn-bigtech/bytedance#bd10) |

## 与美国大厂相比 {#vs-us}

| 主题 | 美国大厂（见质量专题） | 国内三家 | 判断 |
| --- | --- | --- | --- |
| 验证闭环 | Stripe Minions 把确定性节点与智能体循环交织、产出“通过 CI、待人评审”的 PR（[QB01](/sources/quality/bigtech#qb01)、[QB02](/sources/quality/bigtech#qb02)）；Spotify 把验证运行时与智能体运行时分离（[QB05](/sources/quality/bigtech#qb05)） | 腾讯游戏“启动引擎→取日志→修复”证据链（[TX07](/sources/cn-bigtech/tencent#tx07)）；支付宝双 Loop（[AL27](/sources/cn-bigtech/alibaba#al27)）；字节 Harness 可交付性实验（[BD01](/sources/cn-bigtech/bytedance#bd01)） | **一致**：都把“能不能被机器验证”当作放手的前提 |
| AI 评审 | Uber uReview 先过滤再评论（[QB06](/sources/quality/bigtech#qb06)）；Microsoft 把 AI 评审者放进现有 PR 流程（[QB12](/sources/quality/bigtech#qb12)） | 腾讯异构/对抗评审更激进（[TX03](/sources/cn-bigtech/tencent#tx03)、[TX11](/sources/cn-bigtech/tencent#tx11)）；阿里精度优先（[AL08](/sources/cn-bigtech/alibaba#al08)） | **一致**：降噪是核心；国内更强调“多模型互审” |
| 测试生成 | Meta 用 LLM 做变异测试与 TestGen-LLM，只保留“可构建、稳定通过、提升覆盖”的测试（[QB08](/sources/quality/bigtech#qb08)、[QB09](/sources/quality/bigtech#qb09)） | 字节用真实流量 + 程序分析生成单测（[BD09](/sources/cn-bigtech/bytedance#bd09)），NL2Test 用 schema 约束输出、优先稳定断言（[BD10](/sources/cn-bigtech/bytedance#bd10)） | **一致**：用确定性过滤器筛 LLM 产物；国内少见变异测试的公开实践 |
| 度量 | DORA 2025：吞吐上升但交付稳定性受损（[QR06](/sources/quality/research#qr06)）；METR RCT 显示资深开发者可能更慢（[QR03](/sources/quality/research#qr03)） | 三家都从“AI 代码占比”转向需求吞吐率、交付周期、一次通过率（[TX10](/sources/cn-bigtech/tencent#tx10)、[BD15](/sources/cn-bigtech/bytedance#bd15)） | **方向一致，但证据弱**：国内只有自报，没有对照实验或第三方调查 |
| 公开方式 | 工程博客多写具体系统与失败案例 | 腾讯官方长文接近；阿里多为会议议题与开源；字节多为论文 | 国内**会议议题占比高**，摘要≠效果 |
| 工具自研 | 多数用 Claude Code / Codex / Copilot 并自建 harness | 三家都有自研 IDE/CLI 与模型（CodeBuddy、Qoder/Qwen Code、TRAE），内部推广与对外商业化并行 | 内部数据同时是销售材料，**利益相关更强** |

## 与手册原则对照 {#principles}

- **强化**：[P06 验证闭环](/compare/evidence#p06) / [Q02](/handbook/12-quality-cicd#q02)（三家都把 Harness 定义为“让 AI 进入可验证流程”）；[Q07 异构/对抗评审](/handbook/12-quality-cicd#q07)（腾讯的多模型互审是最直接的工业佐证）；[Q12 度量结果而非产量](/handbook/12-quality-cicd#q12)（字节、腾讯都公开反思贡献率指标）；[P15 沙箱](/compare/evidence#p15) / [Q09](/handbook/12-quality-cicd#q09)（三家都把沙箱做成基础设施并开源）；[P19 错误沉淀为规则](/compare/evidence#p19)（踩坑日志、Self-Refinement、测试 Agent 记忆）。
- **补充**：国内材料特别强调“**上下文缺口在代码之外**”（服务契约、历史决策、业务语义：[TX05](/sources/cn-bigtech/tencent#tx05)、[AL06](/sources/cn-bigtech/alibaba#al06)、[TX01](/sources/cn-bigtech/tencent#tx01)），比“精简 AGENTS.md”更进一步：需要把团队知识做成可检索的工程资产。
- **分歧 / 需警惕**：
  - **TDD**：腾讯一线团队明确不追求严格 TDD，用规则和自测兜底（[TX02](/sources/cn-bigtech/tencent#tx02)），与 [Q01 测试先行](/handbook/12-quality-cicd#q01) 有张力；字节 AEGIS 的“先复现再修”则是测试先行的变体（[BD06](/sources/cn-bigtech/bytedance#bd06)）。
  - **AI 评审覆盖面**：“AI 参与 94% 评审”这类指标容易被读成“AI 替代评审”，与 [Q06 AI 评审是补充](/handbook/12-quality-cicd#q06) 相悖；同一家公司的一线工程师则强调逐条人工判断（[TX04](/sources/cn-bigtech/tencent#tx04)）。
  - **来源透明（[Q13](/handbook/12-quality-cicd#q13)）**：自研工具的效果数据大多同时用于商业推广；开源评审工具的自报 benchmark 与社区复测出现明显分歧（[AL08](/sources/cn-bigtech/alibaba#al08) vs [AL09](/sources/cn-bigtech/alibaba#al09)）。

## 缺口 {#gaps}

- **没有独立验证**：本轮没有找到针对三家内部效果数字的第三方调查或对照实验；唯一的独立复测（[AL09](/sources/cn-bigtech/alibaba#al09)）样本只有 10 个 PR。
- **会议议题偏多**：阿里/蚂蚁有大量 2026 年 QCon/AICon 议题，部分（AICon 北京，2026-12）尚未开讲。
- **失败案例偏少**：公开写失败与回滚的只有少数（[TX03](/sources/cn-bigtech/tencent#tx03)、[AL17](/sources/cn-bigtech/alibaba#al17)、[TX01](/sources/cn-bigtech/tencent#tx01)）；没有找到三家关于 AI 代码导致线上事故的公开复盘。
- 更多抓取与归属方面的缺口见 [专题说明](/sources/cn-bigtech/#gaps)。
