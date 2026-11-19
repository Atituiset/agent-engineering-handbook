# 质量与 CI/CD 专题 · 中文互联网

> 美团、阿里、腾讯、字节、快手、得物、百度、京东等的公开文章与中文社区内容。数字均为团队或厂商自报。 每条都有摘要、逐字核对过的原文引文（英文保留原文）和链接；原则编号 Q01–Q13 见 [第 12 章](/handbook/12-quality-cicd#principles)。检索与核对时间：2026-11 中旬。

### QC01 · AI Coding 与单元测试的协同进化：从验证到驱动 {#qc01}
**作者/机构**：美团技术团队｜**日期**：2025-12-05｜[原文](https://tech.meituan.com/2025/12/05/AI-Coding-Unit-Testing.html)

美团给出三条策略：①用单测替代“肉眼审查”快速验证 AI 改动是否精准，并区分“预期内的失败”（主动改旧逻辑）与“意外失败”（破坏现有功能）；②对存量代码先补可运行的单测作为“安全网”，再让 AI 改；③复杂需求用 TDD，先写失败测试再实现。文中特别设定行为准则，防止 AI 为了通过测试“作弊”去改业务代码或测试。

> “单测快速验证逻辑正确性，安全网保护存量代码演进，TDD模式精准传递需求。”

**证据类型**：团队自报｜**对应原则**：[Q01](/handbook/12-quality-cicd#q01) [Q02](/handbook/12-quality-cicd#q02) [Q04](/handbook/12-quality-cicd#q04)

### QC02 · KuiTest：基于大模型通识的 UI 交互遍历测试 {#qc02}
**作者/机构**：美团技术团队｜**日期**：2026-01-13｜[原文](https://tech.meituan.com/2026/01/13/KuiTest-UI.html)

美团用多模态大模型做 UI 功能测试的“预言机”：把任务拆成“组件功能识别 + 交互后响应验证”两步，结合历史图标库检索，让模型预测点击后的合理结果并自动校验，无需手写脚本。团队自报在 10 大业务线真实场景中召回率 86%、精确率 71%、误报率 1.2%。是“用 LLM 解决测试预言机问题”的工业案例。

> “在美团 10 大业务线的真实场景测试中，KuiTest 整体召回率 86%、精确率 71%、误报率 1.2%，且各业务线表现稳定。”

**证据类型**：团队自报｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05) [Q12](/handbook/12-quality-cicd#q12)

### QC03 · 给 Coding Agent 加上质量门禁：测试如何进入 Agent Loop {#qc03}
**作者/机构**：阿里云开发者社区｜**日期**：2026-08-19｜[原文](https://developer.aliyun.com/article/1756795)

提出把测试、静态分析等确定性检查嵌入 Coding Agent 工作流的“质量门禁”：修改后触发快速门禁（Lint/类型检查/关联单测），任务完成前执行集成与回归测试，PR 阶段由 CI 在独立环境里全量验证并配合受保护分支的必需状态检查；失败信息回到上下文让智能体继续修复。按执行阶段和验证成本分层是核心。

> “本文提出“质量门禁（Quality Gates）”理念，将测试、静态分析等确定性检查嵌入Coding Agent工作流，形成分层验证闭环：修改后触发快速门禁（Lint/类型检查/关联单测），任务完成前执行集成与回归测试，PR阶段由CI进行全量验证。”

**证据类型**：作者自述｜**对应原则**：[Q02](/handbook/12-quality-cicd#q02) [Q03](/handbook/12-quality-cicd#q03)

### QC04 · AI Coding 全生命周期的企业级 FDE 工程实践 {#qc04}
**作者/机构**：阿里云 AI Agent Handbook｜**日期**：2026-11-06｜[原文](https://aliyun.github.io/ai-agent-handbook/cases/fde/ai-coding-lifecycle.html)

阿里云开源手册中的案例：以规格驱动开发为主线，用“三阶段·三产物·三闸门”约束 AI 的高产出，需求条目全编号、可测试并与验收标准双向追溯。列出的失控风险包括口径幻觉、跨文档不一致、AI 误删核心功能页签，以及“验证被夸大为已通过测试”。

> “生成越快，失控风险越大：口径幻觉（一个 AND/OR 之差导致判定引擎结论相反）、跨文档不一致（一次业务决议牵动全链 25 处）、AI 误删核心功能页签、验证被夸大为"已通过测试"。”

**证据类型**：团队自报｜**对应原则**：[Q01](/handbook/12-quality-cicd#q01) [Q04](/handbook/12-quality-cicd#q04) [Q03](/handbook/12-quality-cicd#q03)

### QC05 · 给“氛围编程”系上安全带：阿里集团 AI 代码评审实践与 Benchmark 开源 {#qc05}
**作者/机构**：阿里云开发者社区｜**日期**：2026-03-12｜[原文](https://developer.aliyun.com/article/1716140)

阿里集团的 AI 代码评审助手：AI 接管基础评审，人类聚焦核心风险；并联合南京大学开源支持 10 种语言、具备仓库级上下文感知的代码评审基准 AACR-Bench，由 80 多位资深工程师多轮交叉标注（团队自报）。说明 AI 评审也需要自己的评测基准。

> “阿里集团历时一年半、经数万亿Token真实场景打磨，推出AI代码评审助手，实现人机协作新范式：AI接管基础评审，人类聚焦核心风险。”

**证据类型**：团队自报｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q08](/handbook/12-quality-cicd#q08)

### QC06 · 腾讯 AICR：智能化代码评审技术探索与应用实践（上） {#qc06}
**作者/机构**：腾讯云开发者社区｜**日期**：2024｜[原文](https://cloud.tencent.com/developer/article/2467447)

腾讯 AI 代码助手与 CR 团队在 MR 场景落地智能评审：支持片段、文件、批量评审与 MR 摘要。团队自报：集团超 60% 的评审用户日常使用，AI 每月发现问题量与人工相当（约 8 万），意见好评率 60%，AI 直接修复的采纳率超过 25%。用好评率、采纳率而非评论数衡量效果。

> “AI 评审发现问题数 8w/月，已与人工发现问题数达相同量级（人工 8w/月），用户对 AI 意见的好评率 60%；代码修复 AI 直接修复问题代码 2.0+ w次/月，采纳率超 25%”

**证据类型**：团队自报｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q12](/handbook/12-quality-cicd#q12)

### QC07 · 腾讯 AICR（下）：评审数据构造与评测难题 {#qc07}
**作者/机构**：腾讯云开发者社区｜**日期**：2024｜[原文](https://cloud.tencent.com/developer/article/2467464)

下篇讨论技术细节：代码评审天然主观，评估 CR 模型效果难以量化；开源 CR 数据质量参差，团队把数据清洗视为总结任务并用思维链提升训练数据质量，配合用户反馈形成数据飞轮。

> “CR 的概念宽泛，涉及评审范围广，在评估大模型的 CR 能力时，由于 CR 天然的主观特性，对 CR 模型的生成效果判断难以量化，结果偏向主观性。”

**证据类型**：团队自报｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q08](/handbook/12-quality-cicd#q08)

### QC08 · 大模型应用实践：AI 助力 Code Review 安全漏洞发现 {#qc08}
**作者/机构**：腾讯安全应急响应中心（啄木鸟代码安全团队）｜**日期**：2024｜[原文](https://security.tencent.com/index.php/blog/msg/210)

腾讯在代码评审中用混元大模型检测安全漏洞：结构化 JSON 输出、分两次调用（先推理再格式化）缓解幻觉，按漏洞类型编写分析步骤。团队自报漏洞检出准确率从 26% 提升到 95%，日均发现 300 多个风险，在代码上线前阻断。

> “经过多轮优化，漏洞检出准确率提升 69%（26%->95%)，日均发现 300+个代码安全风险，可起到在代码上线前提前阻断风险的效果。”

**证据类型**：团队自报｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q09](/handbook/12-quality-cicd#q09)

### QC09 · BitsAI-CR：字节跳动基于 LLM 的自动化代码评审 {#qc09}
**作者/机构**：字节跳动（arXiv 论文）｜**日期**：2025-01-25｜[原文](https://arxiv.org/abs/2501.15134)

字节跳动的两阶段评审框架：RuleChecker 基于评审规则体系初筛问题，ReviewFilter 做精度复核；数据飞轮依靠结构化反馈持续优化，并提出 Outdated Rate 指标——用评论所指代码随后是否被修改来自动衡量开发者是否采纳。是“用采纳行为而非主观评分度量 AI 评审”的代表。

> “Our approach introduces an Outdated Rate metric that can reflect developers' actual adoption of review comments, enabling automated evaluation and systematic optimization at scale.”

**证据类型**：研究/团队自报｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q12](/handbook/12-quality-cicd#q12)

### QC10 · AI 写完代码，谁来验证？手淘 TEKO“写—验—修”自主闭环 {#qc10}
**作者/机构**：InfoQ（QCon 上海演讲整理）｜**日期**：2026｜[原文](https://www.infoq.cn/article/t3XbHewuN37fsodaprUC)

手淘团队的观点：AI 放大了代码生产速度，验证能力却没有同步提升；做法是把验收条件结构化并回喂给生码环节（“判据先行”），让系统可被智能体观测、驱动和复现，形成“生成—验证—修复—复跑”闭环。

> “最反直觉的一步是把验收条件回喂给生码环节——判据先行，这才是 AI 原生的 TDD。”

**证据类型**：团队自报｜**对应原则**：[Q01](/handbook/12-quality-cicd#q01) [Q02](/handbook/12-quality-cicd#q02)

### QC11 · 业务研发中的 Loop Engineering：事前-事中-事后（“查杀分离”） {#qc11}
**作者/机构**：InfoQ（AICon 深圳演讲整理）｜**日期**：2026｜[原文](https://www.infoq.cn/article/kiNAVcGoJjaVXvJGZpyK)

游戏后端质量验证实践：核心理念“查杀分离”——测试需要独立于实现路径，智能体自写自测存在“认知同源”风险；配套 TDD、tester skill、集成测试与 skill evaluator，分别对应事前结构化、事中自动化验证与事后沉淀回灌。

> “分享将从“查杀分离”这一核心理念出发，说明为什么测试需要独立于实现路径，为什么 Agent 自写自测存在认知同源风险；随后展开 TDD、tester skill、lobbytest / ugctest、skill evaluator 四类实践，分别对应事前结构化、事中自动化验证和事后沉淀回灌。”

**证据类型**：团队自报｜**对应原则**：[Q07](/handbook/12-quality-cicd#q07) [Q01](/handbook/12-quality-cicd#q01) [Q04](/handbook/12-quality-cicd#q04)

### QC12 · 快手智能测试用例生成系统的四阶进化（生成率 8%→60%） {#qc12}
**作者/机构**：快手研发效能团队（腾讯新闻转载）｜**日期**：2026-04-10｜[原文](https://news.qq.com/rain/a/20260410A049S000)

快手复盘用例生成系统从 Prompt 工程（生成率 8%）、多智能体人机协作，到引入体系化知识的演进，每一阶段都基于真实 PRD 与统一测试集做系统性测评。文中还提到同团队的智能 Code Review 采纳率从 7.9% 提升到 54%（团队自报）。

> “在《采纳率从 7.9% 到 54%：快手智能 Code Review 的三阶进化》中，快手研发效能团队重点分享了智能代码审查系统如何通过质量过滤与知识沉淀，将 AI 能力嵌入研发交付链路，使其从个人辅助工具升级为团队级的协作生产力。”

**证据类型**：团队自报｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05) [Q06](/handbook/12-quality-cicd#q06) [Q12](/handbook/12-quality-cicd#q12)

### QC13 · 得物基于 AIGC 生成测试用例的探索与实践 {#qc13}
**作者/机构**：得物技术｜**日期**：2024–2025｜[原文](https://tech.dewu.com/article?id=159)

得物用大模型从需求生成测试点与用例：分点输入功能点以覆盖边界与异常；团队反思“只看采纳率”难以全面评估效果，于是制定准确度、覆盖度、使用率等多维指标。团队自报对简单需求可节约约 40% 的用例编写时间。

> “问题描述：AI生成的评价指标只有采纳率，难以全面评估AI生成测试用例的具体效果。”

**证据类型**：团队自报｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05) [Q12](/handbook/12-quality-cicd#q12)

### QC14 · 文心快码单测智能体 vs 传统单测生成 {#qc14}
**作者/机构**：百度 Comate（SegmentFault 专栏）｜**日期**：2025-01-19｜[原文](https://segmentfault.com/a/1190000045992652)

百度 Comate 介绍单测智能体：生成—执行—修复—提升覆盖率的闭环。文中批评基于静态分析批量生成用例的做法冗余度高——“10 个用例只测了其中两处代码”，会拖累后续执行。厂商自报、尚未独立验证。

> “第二种我会利用代码的静态分析来给你大致地生成一些用例，它其实有一个缺点，这个用例的冗余度非常高，可能你 10 个用例只是测了其中的两处代码，这个冗余度是对于你后续的单测的执行事件的保障都是会产生问题的。”

**证据类型**：厂商自报｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05)

### QC15 · JoyCode：SWE-bench Verified 技术报告 {#qc15}
**作者/机构**：京东云开发者社区｜**日期**：2025｜[原文](https://developer.jdcloud.com/article/4387)

京东 JoyCode 团队的基准技术报告，讨论补丁生成与验证：用 Fail2Pass / Pass2Pass 两类单元测试全面验证补丁效果，并对失败做归因迭代。可作为“回归测试（Pass2Pass）与目标测试（Fail2Pass）同时作为门禁”的示例。厂商自报。

> “SWE-bench 作为当前自动软件工程修复领域的代表性基准，要求智能体具备高效的补丁生成与验证能力。”

**证据类型**：厂商自报｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05) [Q03](/handbook/12-quality-cicd#q03)

### QC16 · 当代码由 Agent 编写时，TDD 还重要吗？ {#qc16}
**作者/机构**：OpenReplay 博客（中文版）｜**日期**：2026-11-09｜[原文](https://blog.openreplay.com/zh/tdd-%E4%BB%A3%E7%90%86%E7%BC%96%E5%86%99%E4%BB%A3%E7%A0%81/)

观点：先行编写的测试成了智能体的规格说明，定义“完成”的标准，并能在智能体谎报完成时当场识破。做法：由人编写或审批失败测试，明确要求智能体在不修改测试的前提下让其通过；写测试与写实现分成两个独立会话，实现会话只能看到它无权修改的测试。同时提醒单测全绿不代表真实用户流程能走通。

> “如果由同一个会话同时编写两者，测试最终描述的将是它自己的代码，而不是需求。”

**证据类型**：作者自述｜**对应原则**：[Q01](/handbook/12-quality-cicd#q01) [Q04](/handbook/12-quality-cicd#q04) [Q07](/handbook/12-quality-cicd#q07)


### 腾讯 · TX08 · 腾讯 2025 研发大数据报告：50% 新增代码由 AI 辅助生成，AI 参与 94% 的代码评审 {#tx08}
**作者/机构**：雷峰网（报道腾讯官方报告）｜**日期**：2025-10-24｜[原文](https://www.leiphone.com/category/industrynews/vULCngEsMJdQ2yxs.html)

腾讯官方年度报告的公开口径：超 90% 工程师使用 CodeBuddy，50% 新增代码由 AI 辅助生成，平均编码时间缩短 40%，整体研发效能提升超 20%；代码评审环节 AI 参与度 94%，28% 的缺陷由 AI 直接发现并被采纳；另列腾讯云“65% 新增代码来自 CodeBuddy、人均千行 BUG 率降低 31.5%”。注意“AI 辅助生成”与“AI 生成”的口径不同。

> “代码评审环节，AI参与度也高达94%”

**证据类型**：团队自报（官方报告，媒体转述）｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q12](/handbook/12-quality-cicd#q12)

### 腾讯 · TX09 · 腾讯发布 AI CLI 并开启 CodeBuddy IDE 公测：AI 评审贡献占比从 12% 到 35% {#tx09}
**作者/机构**：量子位（梦晨，报道腾讯 CodeBuddy 团队）｜**日期**：2025-09-09｜[原文](https://www.qbitai.com/2025/09/329704.html)

CodeBuddy 团队对比 2024 与 2025 的内部实践：重心从代码补全转向以智能体为代表的项目级生成，并“更加关注 AI 代码评审环节”。这是腾讯较早把“AI 在评审中的贡献占比”单列为指标的公开数据。

> “AI 生成代码占比从35% 增加到50%；AI在代码评审中贡献占比从12%增加到35%。”

**证据类型**：团队自报（媒体转述）｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q12](/handbook/12-quality-cicd#q12)

### 腾讯 · TX15 · 测试智能体驱动质量工程新范式（AICon 上海 2026 议题） {#tx15}
**作者/机构**：张晔（腾讯端服务质效技术负责人）｜**日期**：2026-06（AICon 上海）｜[原文](https://aicon.infoq.cn/2026/shanghai/presentation/7101)

把测试智能体定义为“质量执行系统”而非模型能力展示：围绕测试目标完成理解、规划、感知、执行、判定和恢复，在 Web、移动端、桌面端形成多端闭环；工程难点是认知稳定性、GUI 感知准确性、动作可靠性和结果判定可信度。

> “测试智能体并不是单一模型能力的展示，而是由多模型协同、端侧工具编排、执行反馈、证据沉淀和治理机制共同组成的质量执行系统。”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[Q02](/handbook/12-quality-cicd#q02) [Q05](/handbook/12-quality-cicd#q05) [Q10](/handbook/12-quality-cicd#q10)

### 腾讯 · TX16 · 失败一次，受益多次：测试 Agent 从记忆到持续学习（QCon 上海 2026 议题） {#tx16}
**作者/机构**：赵旭峰（腾讯 Agent 端到端落地负责人）｜**日期**：2026-10（QCon 上海）｜[原文](https://qcon.infoq.cn/2026/shanghai/presentation/7341)

针对“版本一改脚本就要重写、失败只留一行 fail、踩坑留在个人脑子里”：先设计稳定的数据结构（知识库、脚本、执行产物），再设计 Agent 行为；失败时基于截图、报告、埋点证据自动归因并升版重试，区分成功路径、失败经验和负向知识，并权衡模型反思、运行证据与人工审核的可信度。

> “先设计稳定的数据结构（知识库、脚本、执行产物），再设计Agent行为”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[P19](/compare/evidence#p19) [P18](/compare/evidence#p18) [Q10](/handbook/12-quality-cicd#q10)

### 腾讯 · TX18 · 从“能审”到“审出闭环”：AI Code Review 规模化实践（QCon 上海 2026 议题） {#tx18}
**作者/机构**：李阳杰（腾讯音乐集团 TME/酷狗研效中心）｜**日期**：2026-10（QCon 上海）｜[原文](https://qcon.infoq.cn/2026/shanghai/presentation/7339)

腾讯音乐（腾讯控股子公司）的 AICR：MCP 动态拉取需求文档、仓库文件与运行时数据做上下文；异构模型多轮采样 + 垂类 Agent 矩阵；只审 Commit/Push 增量并语义去重；与 SonarQube、单测、接口自动化联动“双向印证、降噪”；Push 触发→报告→企微通知→修复→追踪验证，一键采纳/忽略回流自学习。

> “Vibe Coding 时代，代码生产力激增，质量债加速累积，传统 AI 审查“只发现不闭环”。”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q07](/handbook/12-quality-cicd#q07) [Q03](/handbook/12-quality-cicd#q03)

### 腾讯 · TX21 · Tencent WeTest AI 测试智能体：从固定脚本到自主 Agent（游戏测试） {#tx21}
**作者/机构**：腾讯 WeTest 官方博客｜**日期**：2026-09-09｜[原文](https://kr.wetest.net/blog/tencent-wetest-ai-agents-automated-testing-qa-1263.html)

WeTest 两套游戏测试方案：一类用“感知—操作—判断”的 Agent 结合游戏知识、实时状态与日志证据，决策调用稳定脚本并闭环验证；另一类训练对战型 Agent 并检验泛化（对训练集外 Boss 的胜率）。质量判断按功能覆盖是否达到 100%/90% 并追查失败根因。

> “We analyze whether each feature coverage reaches 100% or 90%, identify where failures occurred, and continue to investigate the root causes.”

**证据类型**：团队自述（产品博客）｜**对应原则**：[Q02](/handbook/12-quality-cicd#q02) [Q05](/handbook/12-quality-cicd#q05)

### 阿里 · AL05 · 采纳率如何提升至 50%？AI 自动编写单元测试实践总结 {#al05}
**作者/机构**：阿里技术（腾讯新闻转载）｜**日期**：2025-11-10｜[原文](https://news.qq.com/rain/a/20251110A01D5000)

用 Aone Copilot Agent + 精心设计的 prompt 自动生成单测并修改代码，给出采纳率约 50% 的坦率数字，结论是效果上限取决于 prompt 质量与持续优化。

> “从实践来看，AI 代码采纳率约 50%，要获得更好效果需要持续优化 prompt 质量。”

**证据类型**：团队自报｜**对应原则**：[Q01](/handbook/12-quality-cicd#q01) [Q05](/handbook/12-quality-cicd#q05)

### 阿里 · AL10 · Open Code Review：百万真实任务验证的确定性工程与 Agent 协同（QCon 上海 2026 议题） {#al10}
**作者/机构**：李峥峰（Open Code Review 作者、阿里集团 AI 代码评审负责人）｜**日期**：2026-10（QCon 上海）｜[原文](https://qcon.infoq.cn/2026/shanghai/presentation/7216)

评审系统的设计依据来自阿里内部规模化数据：哪些环节必须用确定性工程兜底，哪些交给 Agent；如何在召回、精度与成本之间取舍。可与 AL08 README、AL09 社区复测对照阅读。

> “分享还将结合百万真实任务、阿里内部 2 万余名开发者的使用数据以及 Open Code Review 开源项目实践”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q12](/handbook/12-quality-cicd#q12)

### 阿里 · AL17 · Loop Engineering 实战：AI 云诊断系统从日志扫描到预发部署的自主闭环 {#al17}
**作者/机构**：阿里云开发者（公众号原文 2026-07-07；此处链接为技术栈转载）｜**日期**：2026-07-07｜[原文](https://jishuzhan.net/article/2077288701192445954)｜[相关链接](https://ai.lzw.me/best-blogs/article/adfa3571)

阿里云诊断团队的维护循环：用 MCP 打通连接器、定时巡检与实时告警自动发现问题，诊断/修复/发布固化为 SKILL.md，Git Worktree 并行修复，六层独立验证防“假修复”，State 沉淀经验。自报一周 ERROR 从 1210 条降到 47 条、同类问题修复从 48 分钟降到 15 分钟。最有价值的是失败教训：Agent 会用降级日志级别“修复”问题，所以必须由独立验证判定。

> “曾出现 Agent 把 logger.error 改成 logger.warning 就宣称 "已修复" 的情况”

**证据类型**：团队自报（原文在公众号，引用自转载页）｜**对应原则**：[Q04](/handbook/12-quality-cicd#q04) [Q03](/handbook/12-quality-cicd#q03) [P06](/compare/evidence#p06) [P11](/compare/evidence#p11)

### 阿里 · AL21 · AI Native 质量保障的体系化实践（飞猪，QCon 上海 2026） {#al21}
**作者/机构**：李桐馨（飞猪测试开发工程师）｜**日期**：2026-10（QCon 上海）｜[原文](https://qcon.infoq.cn/2026/shanghai/presentation/7301)

测试侧把用例生成、自动执行、UI 自动化串成体系，并以“采纳率、自动执行比例、UI 自动化成功率”度量。同一会场还有飞猪“交付大脑”议题。

> “目前用例采纳率稳定在 85% 以上”

**证据类型**：议题摘要（团队自报）｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05) [Q12](/handbook/12-quality-cicd#q12)

### 阿里 · AL22 · AgentLoop：用观测、评估与实验驱动 Agent 持续优化（AICon 北京 2026） {#al22}
**作者/机构**：易星尘（阿里云云原生应用平台资深架构师）｜**日期**：2026-12（议题预告）｜[原文](https://aicon.infoq.cn/2026/beijing/presentation/7452)

把 Agent 的线上观测、评估、实验做成闭环：评估 Agent 调用工具查证并给出分数与依据，而不是只让 LLM 打分；评估结果驱动迭代。

> “由评估 Agent 调用工具查证，给出分数与依据”

**证据类型**：议题摘要（演讲者自述，尚未开讲）｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08) [Q02](/handbook/12-quality-cicd#q02)

### 阿里 · AL27 · 支付宝 60 万行巨石应用 AI 重构的可验证交付工程（QCon 上海 2026） {#al27}
**作者/机构**：蒋宇（蚂蚁集团研发工程师）｜**日期**：2026-10（QCon 上海）｜[原文](https://qcon.infoq.cn/2026/shanghai/presentation/7297)

高风险重构（60 万行、600+ 接口）的关键转向：以“行为是否被正确迁移”为验收对象，而不是“代码看起来迁过去了”，并建立两个相互校验的 Loop：一个从老系统提取业务行为、生成场景（人机协同），另一个用这些场景校验新系统。

> “我们将重构目标从“迁移代码”转变为“迁移行为””

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[P06](/compare/evidence#p06) [Q02](/handbook/12-quality-cicd#q02) [Q11](/handbook/12-quality-cicd#q11)

### 阿里 · AL29 · 生产级业务智能体评测：端到端可控架构（AICon 北京 2026） {#al29}
**作者/机构**：韩延玲（蚂蚁 AI 安全实验室资深测试开发专家）｜**日期**：2026-12（议题预告）｜[原文](https://aicon.infoq.cn/2026/beijing/presentation/7464)

评测样本来自生产：录制真实交互并回放，沉淀为可复用评测集，让业务 Agent 的回归有“真实分布”的数据。

> “通过生产交互录制与回放，将真实任务沉淀为可复用评测样本”

**证据类型**：议题摘要（演讲者自述，尚未开讲）｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08) [Q10](/handbook/12-quality-cicd#q10)

### 字节 · BD09 · AI 驱动的智能化单元测试生成：字节跳动的实践与创新 {#bd09}
**作者/机构**：InfoQ（整理字节质量效能专家赵亮 QCon 上海分享）｜**日期**：2024-12-27｜[原文](https://www.infoq.cn/article/8mVuhrLMMEJ8MDjo1U4e)

单测生成不是“让模型写测试”就完事：用真实业务流量采集保证用例真实性，结合深度程序分析与路径提升提高覆盖率，再用断言工程、语法修正与效果度量保证可靠性；覆盖存量与增量两类场景。

> “通过真实业务流量采集、单测框架能力和路径提升技术，有效解决单元测试的用例真实性和覆盖率问题”

**证据类型**：团队自述（会议整理稿）｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05) [Q01](/handbook/12-quality-cicd#q01)

### 字节 · BD10 · 让 QA 真正用起来：测试用例生成 Agent（NL2Test）落地 {#bd10}
**作者/机构**：字节跳动质量保障团队（字节跳动技术团队公众号，摘录页）｜**日期**：2026-09-08｜[原文](https://www.lddgo.net/article/detail/5eqa)｜[相关链接](https://arxiv.org/abs/2607.24000)

字节与复旦合作的 NL2Test：QA 用自然语言描述场景，Agent 生成可运行回归用例。取舍：只做边界清晰的“用例转译”，不替代 QA；能用程序解决的不用 LLM；用 schema 与允许集合约束输出；优先稳定断言。自报 85.4% 生成用例进入 CI/CD、平均约 25% 新增用例来自 Agent、每双周节省约 30 人天。配套论文（u2）将公司匿名为“一家大型面向消费者的互联网公司”。

> “85.4% 的生成用例被集成到 CI/CD 工作流中”

**证据类型**：团队自报（公众号原文摘录 + 论文）｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05) [Q03](/handbook/12-quality-cicd#q03) [Q10](/handbook/12-quality-cicd#q10) [P04](/compare/evidence#p04)

### 字节 · BD14 · TRAE 智能体审查（Agent-powered Code Review）文档 {#bd14}
**作者/机构**：TRAE 官方文档｜**日期**：2026｜[原文](https://docs.trae.cn/ide_agent-powered-code-review?lang=zh)

把评审放到提交前：可审查未提交变更、单次提交或分支差异，生成变更摘要与业务流程变更图；可开启“提交后自动审查”，问题条目一键唤起对话修复。是 IDE 内“写—审—修”闭环的产品形态，但仍是同一工具链内的自审，需与独立 CI 配合。

> “若你希望由 AI 自动审核变更内容，提供总结摘要并识别问题，可以开启自动审查功能。”

**证据类型**：产品文档｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [P08](/compare/evidence#p08)

### 字节 · BD16 · AgentOps 实战：字节复杂 Agent 的效果评测与迭代优化（QCon 上海 2025） {#bd16}
**作者/机构**：史海量（字节 AI Platform，扣子罗盘效果评测后端负责人）｜**日期**：2025-10（QCon 上海）｜[原文](https://qcon.infoq.cn/2025/shanghai/presentation/6729)｜[相关链接](https://www.infoq.cn/article/vxtijzrrenh3lwxnlpxc)

Agent 应用的效果评测体系：评测集构建、指标体系设计、持续集成与线上监测全链路，应对任务定义模糊、结果不确定、线上波动。与 2025 QCon 北京杨晨的 AgentOps 议题同属扣子罗盘线。

> “系统解析从评测集构建、指标体系设计、到持续集成与线上监测的全链路实践方法”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08) [Q10](/handbook/12-quality-cicd#q10)

### 字节 · BD17 · 给 Agent 做“CT”：大规模 Agent 的可观测与质量保障（QCon 北京 2026） {#bd17}
**作者/机构**：钱世俊（字节跳动火山引擎应用观测技术负责人）｜**日期**：2026-04（QCon 北京）｜[原文](https://qcon.infoq.cn/2026/beijing/presentation/6927)

从端到端 Trace（终端→AI 网关→Agent→工具）到根因定位，并把观测数据回流到离线/在线评测与轨迹评测，驱动持续改进与成本优化。

> “观测数据的回流与离线/在线评测、Agent 轨迹评测相结合，驱动了 Agent 的持续改进与成本优化”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08) [P17](/compare/evidence#p17)
