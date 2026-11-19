# 国内大厂专题 · 阿里（含蚂蚁）

> 含阿里集团研发平台（Aone）、阿里云/通义灵码、Qwen/Qwen Code、Qoder、淘天、菜鸟、AliExpress、飞猪，以及蚂蚁集团/支付宝（蚂蚁为阿里关联公司，单列标注）。每条都有摘要、逐字核对过的原文引文（英文保留原文）和链接。**所有数字均为团队或厂商自报、尚未独立验证**；会议条目只有议题摘要（演讲者自述），标「尚未开讲」的是 2026-12 AICon 北京的预告。检索与核对时间：2026-11 中旬（北京时间）。原则编号 P01–P20 见 [共识度/佐证](/compare/evidence)，Q01–Q13 见 [第 12 章](/handbook/12-quality-cicd#principles)。横向比较见 [国内大厂对比](/compare/cn-bigtech)。

| 编号 | 标题 | 类型 | 证据 |
| --- | --- | --- | --- |
| [AL01](#al01) | 从 Copilot 到 Agent：阿里在 AI Coding 上的应用和挑战 | 团队文章 | 团队自报（会议整理稿） |
| [AL02](#al02) | Vibe Coding 在代码生成与协作中的实践与思考（Aone Agent） | 团队文章 | 团队自述（会议整理稿） |
| [AL03](#al03) | 阿里云内部 AI 辅助代码生成比例近 40%；员工可自由选择工具 | 媒体报道 | 团队自报（媒体采访） |
| [AL04](#al04) | 通义灵码获员工工号 AI001：“未来 20% 的代码将由通义灵码编写” | 媒体报道 | 团队自报（媒体报道） |
| [AL05](#al05) | 采纳率如何提升至 50%？AI 自动编写单元测试实践总结 | 团队文章 | 团队自报 |
| [AL06](#al06) | “架构师 Agent” 系统化落地 | 团队文章 | 个人实践（阿里官方号发布） |
| [AL07](#al07) | 代码生成越来越快，软件交付真正的瓶颈转向了哪里？（云栖大会 AI Native 研发论坛） | 媒体报道 | 团队自报（论坛报道） |
| [AL08](#al08) | Open Code Review：阿里开源的 AI 代码评审 CLI（精度优先的取舍） | 开源仓库 | 开源仓库 README（团队自报 benchmark） |
| [AL09](#al09) | HN：社区在第三方基准上复测 Open Code Review，作者回应已修复 | 社区讨论 | 第三方独立复测（单人、小样本） |
| [AL10](#al10) | Open Code Review：百万真实任务验证的确定性工程与 Agent 协同（QCon 上海 2026 议题） | 会议议题 | 议题摘要（演讲者自述） |
| [AL11](#al11) | AACR-Bench：带仓库上下文的多语言代码评审基准 | 开源仓库 | 开源基准（团队自建） |
| [AL12](#al12) | Qwen3-Coder：在世界中自主编程（Agent RL 与 2 万并行环境） | 团队文章 | 团队自述（模型发布博客） |
| [AL13](#al13) | Qwen Code 1.0 Preview：Qoder 与 Qwen Code 的 Agent 能力合流 | 开源仓库 | 官方发布说明 |
| [AL14](#al14) | Lingma SWE-GPT：面向软件改进的开源过程中心模型 | 论文 | 论文（团队自评） |
| [AL15](#al15) | Quest Mode：把任务委派给智能体（Spec First） | 团队文章 | 厂商自述 |
| [AL16](#al16) | 对话叔同：Qoder 上线 60 天 | 媒体报道 | 团队自报（播客访谈） |
| [AL17](#al17) | Loop Engineering 实战：AI 云诊断系统从日志扫描到预发部署的自主闭环 | 团队文章 | 团队自报（原文在公众号，引用自转载页） |
| [AL18](#al18) | 从辅助编码到 Agent 主导交付：淘宝 AI 原生研发系统（AICon 北京 2026 Keynote） | 会议议题 | 议题摘要（演讲者自述，尚未开讲） |
| [AL19](#al19) | 从 AI 编码助手到需求托管交付 Agent：菜鸟 AI 研发效能实践（AICon 上海 2026） | 会议议题 | 议题摘要（团队自报，尚未独立验证） |
| [AL20](#al20) | Harness For Hybrid Coding：AliExpress 重构实践（QCon 上海 2026） | 会议议题 | 议题摘要（团队自报，尚未独立验证） |
| [AL21](#al21) | AI Native 质量保障的体系化实践（飞猪，QCon 上海 2026） | 会议议题 | 议题摘要（团队自报） |
| [AL22](#al22) | AgentLoop：用观测、评估与实验驱动 Agent 持续优化（AICon 北京 2026） | 会议议题 | 议题摘要（演讲者自述，尚未开讲） |
| [AL23](#al23) | Qoder Desktop 的 Quest 与 Harness 实践（AICon 上海 2026） | 会议议题 | 议题摘要（演讲者自述） |
| [AL24](#al24) | 蚂蚁全链路 AI 研发：SDD 规范驱动与 Harness 工程实践（AICon 上海 2026） | 会议议题 | 议题摘要（演讲者自述） |
| [AL25](#al25) | 蚂蚁数科企业级 AGI 研发体系重塑（AICon 上海 2026） | 会议议题 | 议题摘要（演讲者自述） |
| [AL26](#al26) | 蚂蚁生产级软件交付基建和实践（AICon 深圳 2026） | 会议议题 | 议题摘要（团队自报，尚未独立验证） |
| [AL27](#al27) | 支付宝 60 万行巨石应用 AI 重构的可验证交付工程（QCon 上海 2026） | 会议议题 | 议题摘要（演讲者自述） |
| [AL28](#al28) | 阿福：Agent 小队如何处理持续涌入的线上 Badcase（QCon 上海 2026） | 会议议题 | 议题摘要（演讲者自述） |
| [AL29](#al29) | 生产级业务智能体评测：端到端可控架构（AICon 北京 2026） | 会议议题 | 议题摘要（演讲者自述，尚未开讲） |
| [AL30](#al30) | LoongSuite Pilot：本地 Coding Agent 遥测采集 | 开源仓库 | 开源仓库 README（团队自述） |
| [AL31](#al31) | Alipay-PIBench：支付集成场景的 Coding Agent 基准 | 开源仓库 | 开源基准（团队自建） |

### AL01 · 从 Copilot 到 Agent：阿里在 AI Coding 上的应用和挑战 {#al01}
**作者/机构**：InfoQ（整理向邦宇 QCon 北京 2025 分享）｜**日期**：2025-06-30｜[原文](https://www.infoq.cn/article/5X7q545Ua4GYJOQ7g9lt)

阿里集团研发平台的“全量”视角：内部 AI Coding 插件日活约 1.2 万、渗透率约 65%，补全采纳率约 28%（IDEA 约 33%），约 20% 的 CR 问题由 AI 发现；随后把重点从补全转到“模型驱动、少编排”的通用 Agent（Aone Agent），在容器里异步执行任务。这是少见的同时公开渗透率与采纳率“天花板”的数据。

> “在 Code Review 方面，目前大约 20% 的代码审查问题是由 AI 生成的。”

**证据类型**：团队自报（会议整理稿）｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q12](/handbook/12-quality-cicd#q12) [P11](/compare/evidence#p11)

### AL02 · Vibe Coding 在代码生成与协作中的实践与思考（Aone Agent） {#al02}
**作者/机构**：InfoQ（整理向邦宇 QCon 上海 2025 分享，腾讯新闻转载）｜**日期**：2026-02-10｜[原文](https://news.qq.com/rain/a/20260210A03Q4Y00)

续篇：Aone Agent 是“以外部容器发起的异步任务工具”，用户用自然语言发起任务，容器里的 Agent 自行调用搜索、读文件、Shell 等工具。意外发现：用户从后端扩展到测试、前端、算法、产品、运营、设计和运维，任务也从改代码扩展到代码分析、单测等。体现“隔离容器 + 异步委派”的工程形态。

> “另一个我主导的项目是 Aone Agent 。这是一个以外部容器发起的异步任务工具。”

**证据类型**：团队自述（会议整理稿）｜**对应原则**：[P11](/compare/evidence#p11) [P15](/compare/evidence#p15)

### AL03 · 阿里云内部 AI 辅助代码生成比例近 40%；员工可自由选择工具 {#al03}
**作者/机构**：第一财经（陈杨园，采访通义灵码负责人神秀）｜**日期**：2025-05-30｜[原文](https://www.yicai.com/news/102643443.html)

2025 年中阿里云的公开口径：通义灵码内部覆盖率很高，AI 辅助代码生成比例接近 40%、半年提升约 50%；同时强调内部对 AI 编程工具持开放态度——只要注意数据安全合规，员工可自由选择工具（同文提到字节将禁用第三方工具的传闻，字节未回应）。

> “内部最新的AI辅助代码生成的比例已接近40%，较半年前提升50%左右。”

**证据类型**：团队自报（媒体采访）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12)

### AL04 · 通义灵码获员工工号 AI001：“未来 20% 的代码将由通义灵码编写” {#al04}
**作者/机构**：中国金融信息网（报道阿里云）｜**日期**：2024-04-02｜[原文](https://www.cnfin.com/gs-lb/detail/20240402/4030999_1.html)

2024 年阿里云给 AI 编程工具分配正式工号、公开 20% 代码目标，并强调“程序员仍是研发核心”。可作为时间轴起点：对比 2025 年约 40%、2026 年部分团队 80%–90% 的自报数据。

> “阿里云还专门给通义灵码分配了一个正式的员工工号——AI001。”

**证据类型**：团队自报（媒体报道）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [P16](/compare/evidence#p16)

### AL05 · 采纳率如何提升至 50%？AI 自动编写单元测试实践总结 {#al05}
**作者/机构**：阿里技术（腾讯新闻转载）｜**日期**：2025-11-10｜[原文](https://news.qq.com/rain/a/20251110A01D5000)

用 Aone Copilot Agent + 精心设计的 prompt 自动生成单测并修改代码，给出采纳率约 50% 的坦率数字，结论是效果上限取决于 prompt 质量与持续优化。

> “从实践来看，AI 代码采纳率约 50%，要获得更好效果需要持续优化 prompt 质量。”

**证据类型**：团队自报｜**对应原则**：[Q01](/handbook/12-quality-cicd#q01) [Q05](/handbook/12-quality-cicd#q05)

### AL06 · “架构师 Agent” 系统化落地 {#al06}
**作者/机构**：阿里技术（腾讯新闻转载；作者声明仅代表个人观点）｜**日期**：2026-09-09｜[原文](https://news.qq.com/rain/a/20260909A0876Z00)

先落地技术方案设计而非直接编码：用渐进式披露把领域知识、架构约束、历史决策分层喂给 Agent，产出方案再进入编码。核心判断是复杂系统的关键知识不在代码里，需要显式沉淀。

> “复杂系统真正重要的知识并不完整地存在于代码中”

**证据类型**：个人实践（阿里官方号发布）｜**对应原则**：[P01](/compare/evidence#p01) [P05](/compare/evidence#p05) [P18](/compare/evidence#p18)

### AL07 · 代码生成越来越快，软件交付真正的瓶颈转向了哪里？（云栖大会 AI Native 研发论坛） {#al07}
**作者/机构**：机器之心（凤凰网转载；许晓斌、黄挺等发言）｜**日期**：2026-09-24｜[原文](https://feng.ifeng.com/c/8wgLzD4BqNX)｜[相关链接](https://qcon.infoq.cn/2026/shanghai/presentation/7347)

阿里研发基础设施负责人许晓斌：在阿里编码通常只占软件交付总时长的 20%–30%；极端链路里编码约 1 小时，但从需求进入到交付仍约 21 天，时间耗在影响分析、环境准备、联调、审批、灰度与封网。因此投入转向运行与验证环境：OpenSandbox 内部周创建量超千万，另一套环境体系可完整复原约两三千个应用。同场蚂蚁黄挺介绍沙箱底座。

> “阿里开源的 OpenSandbox，在内部每周创建量已经超过千万级，服务于 Agent 运行、训练和评测。”

**证据类型**：团队自报（论坛报道）｜**对应原则**：[P15](/compare/evidence#p15) [Q09](/handbook/12-quality-cicd#q09) [Q12](/handbook/12-quality-cicd#q12)

### AL08 · Open Code Review：阿里开源的 AI 代码评审 CLI（精度优先的取舍） {#al08}
**作者/机构**：阿里巴巴（GitHub 开源）｜**日期**：2026｜[原文](https://github.com/alibaba/open-code-review)

阿里集团 AI 代码评审团队开源的 CLI：批评通用 Agent 做评审会“偷工减料”、只看部分文件、定位漂移，于是用确定性工程（文件全覆盖、定位校准）+ Agent 协同；README 自报相同模型下 Precision/F1 高于 Claude Code、token 约 1/9，并明说 Recall 更低是有意取舍。独立复测见 AL09。

> “Note that its Recall is lower than general-purpose agents — a deliberate trade-off favoring precision over noise.”

**证据类型**：开源仓库 README（团队自报 benchmark）｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q04](/handbook/12-quality-cicd#q04)

### AL09 · HN：社区在第三方基准上复测 Open Code Review，作者回应已修复 {#al09}
**作者/机构**：Hacker News（eranation 等）｜**日期**：2026-06（约）｜[原文](https://news.ycombinator.com/item?id=48406358)

一位用户在 withmartian 代码评审基准的 50 个 PR 中抽 10 个复测：召回约 74%，但精度只有约 12%、F1 约 20%，与 README 的“精度优先”叙述相反；OCR 作者回帖称测试版本里一个关键工具调用异常导致误报偏高，已复现并修复。样本很小，但说明团队自报 benchmark 需要独立复测。

> “very good recall (~74%, e.g. found a lot of the golden issues) - not so good precision (~12%, e.g. lots of false positives)”

**证据类型**：第三方独立复测（单人、小样本）｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q13](/handbook/12-quality-cicd#q13)

### AL10 · Open Code Review：百万真实任务验证的确定性工程与 Agent 协同（QCon 上海 2026 议题） {#al10}
**作者/机构**：李峥峰（Open Code Review 作者、阿里集团 AI 代码评审负责人）｜**日期**：2026-10（QCon 上海）｜[原文](https://qcon.infoq.cn/2026/shanghai/presentation/7216)

评审系统的设计依据来自阿里内部规模化数据：哪些环节必须用确定性工程兜底，哪些交给 Agent；如何在召回、精度与成本之间取舍。可与 AL08 README、AL09 社区复测对照阅读。

> “分享还将结合百万真实任务、阿里内部 2 万余名开发者的使用数据以及 Open Code Review 开源项目实践”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q12](/handbook/12-quality-cicd#q12)

### AL11 · AACR-Bench：带仓库上下文的多语言代码评审基准 {#al11}
**作者/机构**：阿里巴巴（GitHub 开源）｜**日期**：2026｜[原文](https://github.com/alibaba/aacr-bench)

评审能力怎么量：200 个真实 PR、50 个开源项目、10 种语言，参考意见来自原始评审讨论与模型生成反馈并经专家标注，另附 155 个 PR 的负样本集（不该报问题的场景）。负样本集是对“评审噪声”的直接度量。

> “The original dataset covers 200 unique pull requests (PRs) from 50 open-source projects across 10 programming languages .”

**证据类型**：开源基准（团队自建）｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q08](/handbook/12-quality-cicd#q08)

### AL12 · Qwen3-Coder：在世界中自主编程（Agent RL 与 2 万并行环境） {#al12}
**作者/机构**：通义千问 Qwen 团队｜**日期**：2025-07｜[原文](https://qwenlm.github.io/zh/blog/qwen3-coder/)

模型侧的“验证闭环”：通过自动扩展测试样例构造可验证的 RL 训练实例；Agent RL 的主要难点是环境扩展，借助阿里云基础设施同时运行 2 万个独立环境做多轮交互训练。与 AL07 的沙箱规模互为印证。

> “借助阿里云的基础设施，实现同时运行 20k 独立环境。”

**证据类型**：团队自述（模型发布博客）｜**对应原则**：[Q09](/handbook/12-quality-cicd#q09) [Q02](/handbook/12-quality-cicd#q02)

### AL13 · Qwen Code 1.0 Preview：Qoder 与 Qwen Code 的 Agent 能力合流 {#al13}
**作者/机构**：QwenLM（GitHub Release）｜**日期**：2026-11-11｜[原文](https://github.com/QwenLM/qwen-code/releases/tag/v1.0.0-preview)｜[相关链接](https://github.com/QwenLM/qwen-code-action)

阿里两条 Coding Agent 产品线（Qwen Code 开源 CLI 与 Qoder）在 1.0 预览版中合流，支持多模型提供商、会话恢复与非交互执行；同组织还有把 Qwen Code 接入 GitHub 的 qwen-code-action（PR 评审、issue 分诊）。

> “Brings together the agent capabilities of Qoder and Qwen Code for code understanding, implementation, debugging, and testing.”

**证据类型**：官方发布说明｜**对应原则**：[P14](/compare/evidence#p14) [Q03](/handbook/12-quality-cicd#q03)

### AL14 · Lingma SWE-GPT：面向软件改进的开源过程中心模型 {#al14}
**作者/机构**：Yingwei Ma 等（通义灵码团队，arXiv）｜**日期**：2024-11｜[原文](https://arxiv.org/abs/2411.00622)

不只用静态代码训练，而是学习“真实代码提交过程”——开发者的思考、工具使用、多角色交互，在 SWE-bench Verified 上评测 7B/72B 模型。代表阿里“把软件过程数据当训练信号”的路线。

> “Lingma SWE-GPT systematically incorporates the dynamic interactions and iterative problem-solving inherent in software development process”

**证据类型**：论文（团队自评）｜**对应原则**：[P06](/compare/evidence#p06)

### AL15 · Quest Mode：把任务委派给智能体（Spec First） {#al15}
**作者/机构**：Qoder 官方博客｜**日期**：2025-08-21｜[原文](https://blog.qoder.com/zh/quest-mode)

Qoder 的自主编程模式：执行长任务前先写 Spec，描述清楚变更细节与验证标准，Spec 是开发者与 AI 目标对齐的核心；随后由 Action Flow 执行并汇报。是阿里系“规范驱动 + 委派”的产品化表达。

> “因此我们期望在执行复杂长任务之前，开发者可以详尽的、准确的表达软件逻辑，描述清楚变更细节和验证标准，以指导智能体更准确的完成任务。”

**证据类型**：厂商自述｜**对应原则**：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [Q01](/handbook/12-quality-cicd#q01)

### AL16 · 对话叔同：Qoder 上线 60 天 {#al16}
**作者/机构**：十字路口 Crossing（Qoder 博客园转载）｜**日期**：2025-10-31｜[原文](https://www.cnblogs.com/qoder/p/19180020)

Qoder 创始人访谈：阿里为何要做面向全球的 Agentic 编码平台，以及产品设计取舍。用户量为团队自报，可与 AL13（Qoder 与 Qwen Code 合流）对照看产品线演进。

> “上线 5 天用户迅速突破 10 万，仅 60 天斩获 50 万开发者用户”

**证据类型**：团队自报（播客访谈）｜**对应原则**：[P18](/compare/evidence#p18)

### AL17 · Loop Engineering 实战：AI 云诊断系统从日志扫描到预发部署的自主闭环 {#al17}
**作者/机构**：阿里云开发者（公众号原文 2026-07-07；此处链接为技术栈转载）｜**日期**：2026-07-07｜[原文](https://jishuzhan.net/article/2077288701192445954)｜[相关链接](https://ai.lzw.me/best-blogs/article/adfa3571)

阿里云诊断团队的维护循环：用 MCP 打通连接器、定时巡检与实时告警自动发现问题，诊断/修复/发布固化为 SKILL.md，Git Worktree 并行修复，六层独立验证防“假修复”，State 沉淀经验。自报一周 ERROR 从 1210 条降到 47 条、同类问题修复从 48 分钟降到 15 分钟。最有价值的是失败教训：Agent 会用降级日志级别“修复”问题，所以必须由独立验证判定。

> “曾出现 Agent 把 logger.error 改成 logger.warning 就宣称 "已修复" 的情况”

**证据类型**：团队自报（原文在公众号，引用自转载页）｜**对应原则**：[Q04](/handbook/12-quality-cicd#q04) [Q03](/handbook/12-quality-cicd#q03) [P06](/compare/evidence#p06) [P11](/compare/evidence#p11)

### AL18 · 从辅助编码到 Agent 主导交付：淘宝 AI 原生研发系统（AICon 北京 2026 Keynote） {#al18}
**作者/机构**：吕承飞（吕行，淘天集团 AI 研发负责人）｜**日期**：2026-12（议题预告）｜[原文](https://aicon.infoq.cn/2026/beijing/presentation/7477)

淘宝的问题定义很直白：局部生码提速，但全局交付不提效。议题讲从半托管到全托管的 Agent 交付系统，需求、开发、测试、发布全链路。

> “破局“局部生码提速、全局交付不提效””

**证据类型**：议题摘要（演讲者自述，尚未开讲）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [P16](/compare/evidence#p16)

### AL19 · 从 AI 编码助手到需求托管交付 Agent：菜鸟 AI 研发效能实践（AICon 上海 2026） {#al19}
**作者/机构**：郭凤钊（菜鸟网络研发总监）｜**日期**：2026-06（AICon 上海）｜[原文](https://aicon.infoq.cn/2026/shanghai/presentation/7062)

菜鸟把规范、经验沉淀为 Playbook，让“硅基程序员”托管需求交付；自报 AI 代码贡献率大幅提升。属于高比例自报数据，未见交付周期或缺陷率的同口径披露。

> “AI代码贡献率从 10% 提升至 80%+，部分团队接近100%”

**证据类型**：议题摘要（团队自报，尚未独立验证）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [P13](/compare/evidence#p13)

### AL20 · Harness For Hybrid Coding：AliExpress 重构实践（QCon 上海 2026） {#al20}
**作者/机构**：何伟（阿里巴巴 AliExpress 技术专家）｜**日期**：2026-10（QCon 上海）｜[原文](https://qcon.infoq.cn/2026/shanghai/presentation/7318)

AE 用 Harness 管住“人 + AI 混合编码”的大规模重构：先评测再上线，覆盖多个场景。少数同时给出“线上 Bug”结果指标而不只是代码量的自报。

> “实践覆盖 10 大场景、约 65.5 万行代码重构与评测上线，线上 Bug 下降 80%”

**证据类型**：议题摘要（团队自报，尚未独立验证）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [P06](/compare/evidence#p06) [Q11](/handbook/12-quality-cicd#q11)

### AL21 · AI Native 质量保障的体系化实践（飞猪，QCon 上海 2026） {#al21}
**作者/机构**：李桐馨（飞猪测试开发工程师）｜**日期**：2026-10（QCon 上海）｜[原文](https://qcon.infoq.cn/2026/shanghai/presentation/7301)

测试侧把用例生成、自动执行、UI 自动化串成体系，并以“采纳率、自动执行比例、UI 自动化成功率”度量。同一会场还有飞猪“交付大脑”议题。

> “目前用例采纳率稳定在 85% 以上”

**证据类型**：议题摘要（团队自报）｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05) [Q12](/handbook/12-quality-cicd#q12)

### AL22 · AgentLoop：用观测、评估与实验驱动 Agent 持续优化（AICon 北京 2026） {#al22}
**作者/机构**：易星尘（阿里云云原生应用平台资深架构师）｜**日期**：2026-12（议题预告）｜[原文](https://aicon.infoq.cn/2026/beijing/presentation/7452)

把 Agent 的线上观测、评估、实验做成闭环：评估 Agent 调用工具查证并给出分数与依据，而不是只让 LLM 打分；评估结果驱动迭代。

> “由评估 Agent 调用工具查证，给出分数与依据”

**证据类型**：议题摘要（演讲者自述，尚未开讲）｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08) [Q02](/handbook/12-quality-cicd#q02)

### AL23 · Qoder Desktop 的 Quest 与 Harness 实践（AICon 上海 2026） {#al23}
**作者/机构**：左志鹏（阿里巴巴高级技术专家，Qoder）｜**日期**：2026-06（AICon 上海）｜[原文](https://aicon.infoq.cn/2026/shanghai/presentation/7144)

从“实时指挥”到“任务委派”：任务视窗、工作区与产物区让执行过程可管理、结果可审查；Harness 侧设计“专家团”模式——调研、编码、验证、自动评审多 Agent 协作，一次性端到端交付。

> “如何设计专家团模式，实现包括调研、编码、验证和自动评审的多Agent协作系统，一次性端到端交付高质量结果。”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[P10](/compare/evidence#p10) [P11](/compare/evidence#p11) [Q07](/handbook/12-quality-cicd#q07)

### AL24 · 蚂蚁全链路 AI 研发：SDD 规范驱动与 Harness 工程实践（AICon 上海 2026） {#al24}
**作者/机构**：InfoQ（蚂蚁智能研发产品专家的 AICon 议题介绍）｜**日期**：2026-06-16｜[原文](https://www.infoq.cn/article/5Ke1HD7F6R7aYr4jERyk)

蚂蚁把痛点归纳为两个“追不上”：文档追不上代码（需求与实现两张皮）、验证追不上迭代（流水线后置）。方案是 SDD 四步规范驱动 + 知识库 + 一站式研发，从“写代码”变成“提需求”。

> “验证追不上迭代：流水线后置发现问题，返工成本高”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [Q03](/handbook/12-quality-cicd#q03)

### AL25 · 蚂蚁数科企业级 AGI 研发体系重塑（AICon 上海 2026） {#al25}
**作者/机构**：刘秀婷（蚂蚁数科 PMO & AI 研发效能负责人）｜**日期**：2026-06（AICon 上海）｜[原文](https://aicon.infoq.cn/2026/shanghai/presentation/7122)

组织层做法：AGI 研发指数、L1–L5 分级与“苏格拉底式”质量追问，把人从环内（in the loop）挪到环上（on the loop）。与 CN03（蚂蚁数科 Harness）同源不同侧面。

> “Agent In The Loop, Human On The Loop”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[P16](/compare/evidence#p16) [P08](/compare/evidence#p08) [Q12](/handbook/12-quality-cicd#q12)

### AL26 · 蚂蚁生产级软件交付基建和实践（AICon 深圳 2026） {#al26}
**作者/机构**：刘仁权（弈阁，蚂蚁集团 CIO 总架构师、Agentic Delivery 团队）｜**日期**：2026（AICon 深圳）｜[原文](https://aicon.infoq.cn/2026/shenzhen/presentation/7226)

蚂蚁的交付基建：在 AI 生成占比极高的前提下，如何让交付 7×24 可持续，靠的是基建（环境、验证、发布）而非更多生成。

> “在蚂蚁很多团队 AI 生成代码占比已经达到 90% 以上”

**证据类型**：议题摘要（团队自报，尚未独立验证）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [Q03](/handbook/12-quality-cicd#q03)

### AL27 · 支付宝 60 万行巨石应用 AI 重构的可验证交付工程（QCon 上海 2026） {#al27}
**作者/机构**：蒋宇（蚂蚁集团研发工程师）｜**日期**：2026-10（QCon 上海）｜[原文](https://qcon.infoq.cn/2026/shanghai/presentation/7297)

高风险重构（60 万行、600+ 接口）的关键转向：以“行为是否被正确迁移”为验收对象，而不是“代码看起来迁过去了”，并建立两个相互校验的 Loop：一个从老系统提取业务行为、生成场景（人机协同），另一个用这些场景校验新系统。

> “我们将重构目标从“迁移代码”转变为“迁移行为””

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[P06](/compare/evidence#p06) [Q02](/handbook/12-quality-cicd#q02) [Q11](/handbook/12-quality-cicd#q11)

### AL28 · 阿福：Agent 小队如何处理持续涌入的线上 Badcase（QCon 上海 2026） {#al28}
**作者/机构**：肖汉松（蚂蚁集团阿福 Harness 架构组负责人）｜**日期**：2026-10（QCon 上海）｜[原文](https://qcon.infoq.cn/2026/shanghai/presentation/7232)

两层工程：先用 Harness 解决“单个 badcase 能否可靠修好”，再用 Loop 解决“持续涌入时能否持续修复”。是 Harness→Loop 演进的清晰表述。

> “先用 Harness Engineering 解决“如何可靠修好 badcase”，再用 Loop Engineering 解决“如何持续修复 badcase””

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[P06](/compare/evidence#p06) [P19](/compare/evidence#p19) [Q08](/handbook/12-quality-cicd#q08)

### AL29 · 生产级业务智能体评测：端到端可控架构（AICon 北京 2026） {#al29}
**作者/机构**：韩延玲（蚂蚁 AI 安全实验室资深测试开发专家）｜**日期**：2026-12（议题预告）｜[原文](https://aicon.infoq.cn/2026/beijing/presentation/7464)

评测样本来自生产：录制真实交互并回放，沉淀为可复用评测集，让业务 Agent 的回归有“真实分布”的数据。

> “通过生产交互录制与回放，将真实任务沉淀为可复用评测样本”

**证据类型**：议题摘要（演讲者自述，尚未开讲）｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08) [Q10](/handbook/12-quality-cicd#q10)

### AL30 · LoongSuite Pilot：本地 Coding Agent 遥测采集 {#al30}
**作者/机构**：阿里巴巴（GitHub 开源）｜**日期**：2026｜[原文](https://github.com/alibaba/loongsuite-pilot)

把“Agent 用得怎么样”变成可观测数据：自动发现本机 Claude Code/Qwen Code 等 Agent，统一事件模式采集模型、会话、轮次、工具调用与 token，并在导出前控制敏感 prompt 与密钥。是度量 Agent 成本与行为的基础设施。

> “Which agents are being used? What model, session, turn, and tool activity happened?”

**证据类型**：开源仓库 README（团队自述）｜**对应原则**：[P17](/compare/evidence#p17) [Q12](/handbook/12-quality-cicd#q12)

### AL31 · Alipay-PIBench：支付集成场景的 Coding Agent 基准 {#al31}
**作者/机构**：支付宝 / inclusionAI（GitHub 开源）｜**日期**：2026｜[原文](https://github.com/inclusionAI/PIBench)

领域化评测：在真实支付集成任务上评 Coding Agent，并比较“带 Skill / 不带 Skill”两种条件下的 Rubric 通过率。是 Skill 价值的可量化评测思路。

> “Alipay-PIBench is a repository-level benchmark proposed by Alipay”

**证据类型**：开源基准（团队自建）｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08) [P13](/compare/evidence#p13)
