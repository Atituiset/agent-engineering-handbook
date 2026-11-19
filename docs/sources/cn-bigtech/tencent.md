# 国内大厂专题 · 腾讯

> 含腾讯技术工程、腾讯云开发者、CodeBuddy/WorkBuddy、WeTest、微信、腾讯游戏、腾讯音乐（TME，腾讯控股子公司）等。每条都有摘要、逐字核对过的原文引文（英文保留原文）和链接。**所有数字均为团队或厂商自报、尚未独立验证**；会议条目只有议题摘要（演讲者自述），标「尚未开讲」的是 2026-12 AICon 北京的预告。检索与核对时间：2026-11 中旬（北京时间）。原则编号 P01–P20 见 [共识度/佐证](/compare/evidence)，Q01–Q13 见 [第 12 章](/handbook/12-quality-cicd#principles)。横向比较见 [国内大厂对比](/compare/cn-bigtech)。

| 编号 | 标题 | 类型 | 证据 |
| --- | --- | --- | --- |
| [TX01](#tx01) | 不只是 Memory：用本体与三层图谱让 Coding Agent 越用越懂项目 | 团队文章 | 团队自报（内部试验，作者自注局限） |
| [TX02](#tx02) | 从 Vibe Coding 到 AI 原生研发团队：一套能落地的工程实践（Vibe Flowing） | 团队文章 | 团队自报 |
| [TX03](#tx03) | Harness Engineering：AI 能在真正“出事会炸”的后端系统里写代码吗？（腾讯 CDN LEGO） | 团队文章 | 团队自报 |
| [TX04](#tx04) | 从 Vibe Coding 到 Agentic Engineering：重构后台开发全流程 | 团队文章 | 个人实践（腾讯工程师） |
| [TX05](#tx05) | QQ 音乐 Harness Engineering 实践（大仓多服务） | 团队文章 | 团队自述 |
| [TX06](#tx06) | Harness Engineering 如何驱动云端智能体：腾讯云 ADP 的设计实践 | 团队文章 | 团队自述（产品博客） |
| [TX07](#tx07) | 游戏开发生产力重构：从单点 AIGC 到 Harness 工程闭环 | 团队文章 | 团队自报（会议整理稿） |
| [TX08](#tx08) | 腾讯 2025 研发大数据报告：50% 新增代码由 AI 辅助生成，AI 参与 94% 的代码评审 | 媒体报道 | 团队自报（官方报告，媒体转述） |
| [TX09](#tx09) | 腾讯发布 AI CLI 并开启 CodeBuddy IDE 公测：AI 评审贡献占比从 12% 到 35% | 媒体报道 | 团队自报（媒体转述） |
| [TX10](#tx10) | 腾讯研发模式被 AI 重塑：需求吞吐率成为 AI Coding 的核心指标 | 媒体报道 | 高管口述（媒体采访） |
| [TX11](#tx11) | 腾讯 AI 三年：代码 AI 率从 23% 到 90%，最大的坑不是技术 | 媒体报道 | 高管口述（媒体采访） |
| [TX12](#tx12) | 腾讯健康：我们有 40% 的代码是 AI 写的 | 团队文章 | 团队自报 |
| [TX13](#tx13) | 腾讯 CodeBuddy IDE 如何成为一个“全栈高级工程师”？ | 媒体报道 | 团队自报（媒体采访） |
| [TX14](#tx14) | AI Native 企业研发工具链：架构重构与持续演进（AICon 北京 2026 议题） | 会议议题 | 议题摘要（演讲者自述，尚未开讲） |
| [TX15](#tx15) | 测试智能体驱动质量工程新范式（AICon 上海 2026 议题） | 会议议题 | 议题摘要（演讲者自述） |
| [TX16](#tx16) | 失败一次，受益多次：测试 Agent 从记忆到持续学习（QCon 上海 2026 议题） | 会议议题 | 议题摘要（演讲者自述） |
| [TX17](#tx17) | 用 Harness 工程打造 SRE 可控的生产环境（QCon 上海 2026 议题） | 会议议题 | 议题摘要（演讲者自述） |
| [TX18](#tx18) | 从“能审”到“审出闭环”：AI Code Review 规模化实践（QCon 上海 2026 议题） | 会议议题 | 议题摘要（演讲者自述） |
| [TX19](#tx19) | AI Agent 执行环境的规模化难题：CubeSandbox 的解法与实践（QCon 上海 2026 议题） | 会议议题 | 议题摘要（演讲者自述） |
| [TX20](#tx20) | CAT：基于检索增强 LLM 的低成本 UI 自动化测试——微信案例 | 论文 | 论文（工业部署，团队自报） |
| [TX21](#tx21) | Tencent WeTest AI 测试智能体：从固定脚本到自主 Agent（游戏测试） | 团队文章 | 团队自述（产品博客） |
| [TX22](#tx22) | A.S.E（AICGSecEval）：仓库级 AI 生成代码安全评测基准 | 开源仓库 | 开源仓库 README（团队自述） |
| [TX23](#tx23) | WorkBuddy 企业版与 AI Coding 的组织账：个人提效≠组织提效 | 媒体报道 | 高管口述（媒体报道） |

### TX01 · 不只是 Memory：用本体与三层图谱让 Coding Agent 越用越懂项目 {#tx01}
**作者/机构**：腾讯技术工程（云数据库研发团队）｜**日期**：2026-11-13｜[原文](https://news.qq.com/rain/a/20261113A0BF6G00)

团队让 Agent 承担“设计完成到上线前测试”这一段 Loop：人定目标、设计与业务取舍，Agent 把设计转成可观察的验收条件，实现、验证、失败后定位修复；构建、部署、等待等常规步骤交给确定性工具。团队 Memory 由 Chat Memory、Wiki、CodeGraph、Skill 四类资产组成，并以“工程事实 / 项目语义 / bug_fixed 经验”三层互索引图谱组织。作者明确说明 58%→65% 只是 Bug 定位子任务的初步信号，不能换算成整体效率。

> “在一项内部代码 Bug 定位试验中, 加入上述图谱能力后, Agent 的问题定位成功率从 58% 提升到 65%, 增加了 7 个百分点。”

**证据类型**：团队自报（内部试验，作者自注局限）｜**对应原则**：[P18](/compare/evidence#p18) [P19](/compare/evidence#p19) [P06](/compare/evidence#p06) [Q02](/handbook/12-quality-cicd#q02)

### TX02 · 从 Vibe Coding 到 AI 原生研发团队：一套能落地的工程实践（Vibe Flowing） {#tx02}
**作者/机构**：腾讯技术工程（masoncai，海外网络运营平台团队）｜**日期**：2026-07-21｜[原文](https://news.qq.com/rain/a/20260721A09ALQ00)

一个“所有组件都由 AI 维护”的内部运营平台：monorepo 让 AI 一次看到前后端；AGENTS.md 集中写分层规则（只能向下调用）、文件红线和检查命令；提交前必须过 ruff/ty、oxlint/vue-tsc；Playwright 截图做 AI 自测，最终由提需求的运营同事验收，MR 仍需管理员审批合并。对 TDD 的取舍很务实：AI 易写“自欺欺人”的测试，所以用规则兜底，而不追求严格先写测试。

> “覆盖率目标定在 70%，作为参考值不阻断。”

**证据类型**：团队自报｜**对应原则**：[P03](/compare/evidence#p03) [P04](/compare/evidence#p04) [P05](/compare/evidence#p05) [P06](/compare/evidence#p06) [Q02](/handbook/12-quality-cicd#q02) [Q05](/handbook/12-quality-cicd#q05)

### TX03 · Harness Engineering：AI 能在真正“出事会炸”的后端系统里写代码吗？（腾讯 CDN LEGO） {#tx03}
**作者/机构**：腾讯技术工程（lancelotluo，腾讯 CDN 团队）｜**日期**：2026-04-21｜[原文](https://news.qq.com/rain/a/20260421A06DXU00)

在百万行级 C++ CDN 核心框架里落地 AI Coding：围绕“上下文、约束、反馈”设计五层 Harness，Hook 自动采集、踩坑日志（Pitfall Journal）等多条反馈通道，以及 3 个模型并行、辩论式、“全员无新发现自动收敛”的对抗式 CR。案例里一次读写竞争修复从 5 天压到 1 天，但作者同时写明方案没考虑线程初始化、并非最优解——是少见的同时报收益与缺陷的记录。

> “LEGO的对抗式CR通过多模型并行审查和交叉验证，能够发现更深层的问题”

**证据类型**：团队自报｜**对应原则**：[Q07](/handbook/12-quality-cicd#q07) [P19](/compare/evidence#p19) [P12](/compare/evidence#p12) [P06](/compare/evidence#p06)

### TX04 · 从 Vibe Coding 到 Agentic Engineering：重构后台开发全流程 {#tx04}
**作者/机构**：腾讯技术工程（seanguo，网易号转载）｜**日期**：2026-04-17｜[原文](https://www.163.com/dy/article/KQO1VBLM0518R7MO.html)

一线后台工程师用 Claude Code + 自定义 Skill/Command/MCP，把 PM、代码平台、DevOps、日志平台串进一个终端会话：人定义目标、约束和质量标准，AI 在结构化流程里执行，关键节点人工审核。两条教训：自定义 Skill 的价值是编排串联而非从零实现；AI 生成的 MR 审查意见必须逐条人工判断。

> “所以 reviewer 拿到 AI 的审查结果后，每一条都要过脑子判断，该采纳的采纳，不靠谱的直接丢掉。”

**证据类型**：个人实践（腾讯工程师）｜**对应原则**：[P13](/compare/evidence#p13) [P14](/compare/evidence#p14) [P08](/compare/evidence#p08) [Q06](/handbook/12-quality-cicd#q06)

### TX05 · QQ 音乐 Harness Engineering 实践（大仓多服务） {#tx05}
**作者/机构**：腾讯云开发者（QQ 音乐团队）｜**日期**：2026-05-21｜[原文](https://cloud.tencent.com/developer/article/2671876)

面向 monorepo 多服务场景的开源工程框架：把“隐性规范、历史决策、服务契约（IDL 字段冻结）、跨服务依赖、演进轨迹”五类 AI 盲区分别落成工程制品——服务矩阵自动解析依赖、IDL 门禁防止 AI 猜依赖、Self-Refinement 闭环把纠错沉淀为团队资产，并要求每个关键节点有可机读的质量门禁与审计记录。

> “提升上下文质量，是比提升模型能力更高效的杠杆。”

**证据类型**：团队自述｜**对应原则**：[P05](/compare/evidence#p05) [P04](/compare/evidence#p04) [P19](/compare/evidence#p19) [P02](/compare/evidence#p02)

### TX06 · Harness Engineering 如何驱动云端智能体：腾讯云 ADP 的设计实践 {#tx06}
**作者/机构**：腾讯云 ADP 团队｜**日期**：2026-07-17｜[原文](https://adp.tencent.com/zh/blog/agent-harness-engineering-adp-practice)

平台团队视角：Agent = Model + Harness。ADP 把 Agent Loop、Memory、Sandbox、Tools/MCP 解耦并用稳定接口连接，以便容器崩溃可恢复、沙箱可替换重建、模型或 Loop 升级不牵动底层；Harness 负责工具、状态、权限、上下文、恢复、评估、观测与反馈闭环，并记录轨迹以支持 replay/eval。

> “Agent Harness不是一个花哨的新名词，而是 Agent 从 demo 走向生产之后必然出现的工程抽象。”

**证据类型**：团队自述（产品博客）｜**对应原则**：[P15](/compare/evidence#p15) [P18](/compare/evidence#p18) [Q08](/handbook/12-quality-cicd#q08) [Q09](/handbook/12-quality-cicd#q09)

### TX07 · 游戏开发生产力重构：从单点 AIGC 到 Harness 工程闭环 {#tx07}
**作者/机构**：gawain2048（腾讯云开发者社区；整理腾讯游戏技术专家杨梦舟的分享）｜**日期**：2026-06-11｜[原文](https://developer.cloud.tencent.com/article/2686566)

游戏工程（UE 的 C++、蓝图、资产引用）里很多问题只有进编辑器和运行时才暴露。做法：把 SVN/Git 作为 AI 参与项目的底层安全机制（基于 diff 与日志可回滚）；建立“启动引擎→运行游戏→取日志→修复/输出结论”的自循环证据链；把“编译 0 error”作为量化验收，新坑点写回 Memory。

> “实现“编译已通过 (0 error)”的量化验证指标”

**证据类型**：团队自报（会议整理稿）｜**对应原则**：[P06](/compare/evidence#p06) [P09](/compare/evidence#p09) [P19](/compare/evidence#p19) [Q02](/handbook/12-quality-cicd#q02)

### TX08 · 腾讯 2025 研发大数据报告：50% 新增代码由 AI 辅助生成，AI 参与 94% 的代码评审 {#tx08}
**作者/机构**：雷峰网（报道腾讯官方报告）｜**日期**：2025-10-24｜[原文](https://www.leiphone.com/category/industrynews/vULCngEsMJdQ2yxs.html)

腾讯官方年度报告的公开口径：超 90% 工程师使用 CodeBuddy，50% 新增代码由 AI 辅助生成，平均编码时间缩短 40%，整体研发效能提升超 20%；代码评审环节 AI 参与度 94%，28% 的缺陷由 AI 直接发现并被采纳；另列腾讯云“65% 新增代码来自 CodeBuddy、人均千行 BUG 率降低 31.5%”。注意“AI 辅助生成”与“AI 生成”的口径不同。

> “代码评审环节，AI参与度也高达94%”

**证据类型**：团队自报（官方报告，媒体转述）｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q12](/handbook/12-quality-cicd#q12)

### TX09 · 腾讯发布 AI CLI 并开启 CodeBuddy IDE 公测：AI 评审贡献占比从 12% 到 35% {#tx09}
**作者/机构**：量子位（梦晨，报道腾讯 CodeBuddy 团队）｜**日期**：2025-09-09｜[原文](https://www.qbitai.com/2025/09/329704.html)

CodeBuddy 团队对比 2024 与 2025 的内部实践：重心从代码补全转向以智能体为代表的项目级生成，并“更加关注 AI 代码评审环节”。这是腾讯较早把“AI 在评审中的贡献占比”单列为指标的公开数据。

> “AI 生成代码占比从35% 增加到50%；AI在代码评审中贡献占比从12%增加到35%。”

**证据类型**：团队自报（媒体转述）｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q12](/handbook/12-quality-cicd#q12)

### TX10 · 腾讯研发模式被 AI 重塑：需求吞吐率成为 AI Coding 的核心指标 {#tx10}
**作者/机构**：第一财经（郑栩彤，采访汤道生、刘毅等）｜**日期**：2026-06-05｜[原文](https://www.yicai.com/news/103218044.html)

CodeBuddy/WorkBuddy 负责人刘毅：2022 年 AI 代码接受程度不到 30%，到 2025 年底大部分团队 90% 以上代码由 AI 生成，程序员同时开多个任务。指标从“生成率”转向“需求吞吐率”；挑战是 AI 幻觉把风险带到生产、人类专家被评审淹没，因此要“用 AI 发现 AI 代码的错误、用 AI 自动测试”。团队组织更扁平、上下文对全员透明。

> “现在，需求吞吐率成为了AI Coding的核心指标，代表组织的创新速度。”

**证据类型**：高管口述（媒体采访）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [Q06](/handbook/12-quality-cicd#q06) [P08](/compare/evidence#p08)

### TX11 · 腾讯 AI 三年：代码 AI 率从 23% 到 90%，最大的坑不是技术 {#tx11}
**作者/机构**：CSDN（搜狐转载，采访刘毅）｜**日期**：2026-06-08｜[原文](https://www.sohu.com/a/1033866890_115128)

同一位负责人的另一篇访谈，补充了“踩过的坑”：Token 成本是第一关，需要精细化成本治理；2026 年行业强调 harness，即给 AI 更多约束和更快的校验迭代；引入 AI 评审时，生产代码的 AI 与评审代码的 AI 必须不同。最难的是组织：个人提效≠组织提效。

> “不能让同一个 AI 自己检查自己”

**证据类型**：高管口述（媒体采访）｜**对应原则**：[Q07](/handbook/12-quality-cicd#q07) [P17](/compare/evidence#p17) [Q12](/handbook/12-quality-cicd#q12)

### TX12 · 腾讯健康：我们有 40% 的代码是 AI 写的 {#tx12}
**作者/机构**：CodeBuddy（腾讯云开发者社区专栏）｜**日期**：2024-11-20｜[原文](https://cloud.tencent.com/developer/article/2467438)

早期（补全时代）推广样本：先组建跨岗位“先锋小组”记录 Good/Badcase、双周会反馈，再全面推广；累计 600+ Badcase。用生成率、采纳率、活跃率等多维指标做运营，并发现命名不规范、缺注释、逻辑复杂、复制大块代码会降低 AI 效果。可与 2026 年的“需求吞吐率”口径对照，看指标如何演变。

> “团队通过对 AI 代码助手的使用数据统计分析后发现，代码补全采纳率与使用的熟练度呈正相关”

**证据类型**：团队自报｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [P03](/compare/evidence#p03)

### TX13 · 腾讯 CodeBuddy IDE 如何成为一个“全栈高级工程师”？ {#tx13}
**作者/机构**：AI 前线（褚杏娟，采访腾讯 CodeBuddy 团队）｜**日期**：2025-07-29｜[原文](https://news.qq.com/rain/a/20250729A05FAH00)

产品立项依据来自内部调研：程序员大部分时间花在沟通对齐而非 IDE 里；因此 CodeBuddy 想覆盖“需求拆解—架构设计—UI—前后端—测试部署”全链路，并内置 200+ 场景知识库生成结构化需求文档再交给 Code Agent。报道同时给出“43% 代码由 AI 生成、千行 bug 率降 31.5%”的内部口径。

> “腾讯内部调研发现，一个程序员只有 37% 的时间在真正使用 IDE 做开发”

**证据类型**：团队自报（媒体采访）｜**对应原则**：[P01](/compare/evidence#p01) [Q12](/handbook/12-quality-cicd#q12)

### TX14 · AI Native 企业研发工具链：架构重构与持续演进（AICon 北京 2026 议题） {#tx14}
**作者/机构**：陈偲颖（腾讯资深研发工程师）｜**日期**：2026-12（议题预告）｜[原文](https://aicon.infoq.cn/2026/beijing/presentation/7424)

平台从“配置驱动”转向“意图驱动”：业务操作工具协议化、能力原子化（明确输入输出、副作用、幂等），Agent 运行时工程化，上下文平台化，以及由用户打断、连续失败、方案修正等“摩擦信号”驱动的改进闭环；权限、审计、评测与人工审批贯穿，高风险操作必须审批。

> “我们的实践从配置驱动转向意图驱动：用户表达业务目标，系统结合专家知识生成方案，通过低代码 Harness 编排执行。”

**证据类型**：议题摘要（演讲者自述，尚未开讲）｜**对应原则**：[P14](/compare/evidence#p14) [P15](/compare/evidence#p15) [P19](/compare/evidence#p19) [Q08](/handbook/12-quality-cicd#q08)

### TX15 · 测试智能体驱动质量工程新范式（AICon 上海 2026 议题） {#tx15}
**作者/机构**：张晔（腾讯端服务质效技术负责人）｜**日期**：2026-06（AICon 上海）｜[原文](https://aicon.infoq.cn/2026/shanghai/presentation/7101)

把测试智能体定义为“质量执行系统”而非模型能力展示：围绕测试目标完成理解、规划、感知、执行、判定和恢复，在 Web、移动端、桌面端形成多端闭环；工程难点是认知稳定性、GUI 感知准确性、动作可靠性和结果判定可信度。

> “测试智能体并不是单一模型能力的展示，而是由多模型协同、端侧工具编排、执行反馈、证据沉淀和治理机制共同组成的质量执行系统。”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[Q02](/handbook/12-quality-cicd#q02) [Q05](/handbook/12-quality-cicd#q05) [Q10](/handbook/12-quality-cicd#q10)

### TX16 · 失败一次，受益多次：测试 Agent 从记忆到持续学习（QCon 上海 2026 议题） {#tx16}
**作者/机构**：赵旭峰（腾讯 Agent 端到端落地负责人）｜**日期**：2026-10（QCon 上海）｜[原文](https://qcon.infoq.cn/2026/shanghai/presentation/7341)

针对“版本一改脚本就要重写、失败只留一行 fail、踩坑留在个人脑子里”：先设计稳定的数据结构（知识库、脚本、执行产物），再设计 Agent 行为；失败时基于截图、报告、埋点证据自动归因并升版重试，区分成功路径、失败经验和负向知识，并权衡模型反思、运行证据与人工审核的可信度。

> “先设计稳定的数据结构（知识库、脚本、执行产物），再设计Agent行为”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[P19](/compare/evidence#p19) [P18](/compare/evidence#p18) [Q10](/handbook/12-quality-cicd#q10)

### TX17 · 用 Harness 工程打造 SRE 可控的生产环境（QCon 上海 2026 议题） {#tx17}
**作者/机构**：王杰（腾讯游戏高级 SRE 工程师）｜**日期**：2026-10（QCon 上海）｜[原文](https://qcon.infoq.cn/2026/shanghai/presentation/7292)

腾讯游戏先把应用交付代码化、GitOps 化，于是“发布变更”变成“改代码改配置”，正好落在 AI Coding 最成熟的区间；所有变更必经 Git 与人工 Review，多 SRE Agent 参与扩缩容、配置调整、故障修复，过程完整记录、评估后沉淀为跨业务能力。核心观点：不让 LLM 变确定，而用 Harness 管住不确定性。

> “我们的解决方案不是让 LLM 变确定，而是用 Harness 工程管控它的不确定性”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[P15](/compare/evidence#p15) [P08](/compare/evidence#p08) [P04](/compare/evidence#p04) [Q11](/handbook/12-quality-cicd#q11)

### TX18 · 从“能审”到“审出闭环”：AI Code Review 规模化实践（QCon 上海 2026 议题） {#tx18}
**作者/机构**：李阳杰（腾讯音乐集团 TME/酷狗研效中心）｜**日期**：2026-10（QCon 上海）｜[原文](https://qcon.infoq.cn/2026/shanghai/presentation/7339)

腾讯音乐（腾讯控股子公司）的 AICR：MCP 动态拉取需求文档、仓库文件与运行时数据做上下文；异构模型多轮采样 + 垂类 Agent 矩阵；只审 Commit/Push 增量并语义去重；与 SonarQube、单测、接口自动化联动“双向印证、降噪”；Push 触发→报告→企微通知→修复→追踪验证，一键采纳/忽略回流自学习。

> “Vibe Coding 时代，代码生产力激增，质量债加速累积，传统 AI 审查“只发现不闭环”。”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q07](/handbook/12-quality-cicd#q07) [Q03](/handbook/12-quality-cicd#q03)

### TX19 · AI Agent 执行环境的规模化难题：CubeSandbox 的解法与实践（QCon 上海 2026 议题） {#tx19}
**作者/机构**：龙进（腾讯云 CubeSandbox 核心 maintainer）｜**日期**：2026-10（QCon 上海）｜[原文](https://qcon.infoq.cn/2026/shanghai/presentation/7393)｜[相关链接](https://github.com/TencentCloud/CubeSandbox)

Agent 负载从一次性执行走向长周期、有状态、大规模并行，既要安全承载不可信代码又要扛突发并发。CubeSandbox 走 MicroVM + 快照路线，以沙箱为基本计算单元，提供暂停恢复、快照克隆，自报冷启动约 60ms、单实例内存 5MB 以内。

> “基于MicroVM + 快照路线，以沙箱为基本计算单元，实现算力与状态两个维度的弹性”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[P15](/compare/evidence#p15) [Q09](/handbook/12-quality-cicd#q09)

### TX20 · CAT：基于检索增强 LLM 的低成本 UI 自动化测试——微信案例 {#tx20}
**作者/机构**：Sidong Feng 等（含微信团队，arXiv / ASE 2024）｜**日期**：2024-09-12｜[原文](https://arxiv.org/abs/2409.07829)

用 RAG 检索微信历史测试样例作为 few-shot，生成动作序列；用传统机器学习做 UI 元素匹配、LLM 只作补充优化器，以控制成本。已集成进微信测试平台。是“LLM 不单干、与确定性方法分工”的工业样本。

> “achieving 90% UI automation with $0.34 cost, outperforming the state-of-the-art”

**证据类型**：论文（工业部署，团队自报）｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05) [P06](/compare/evidence#p06)

### TX21 · Tencent WeTest AI 测试智能体：从固定脚本到自主 Agent（游戏测试） {#tx21}
**作者/机构**：腾讯 WeTest 官方博客｜**日期**：2026-09-09｜[原文](https://kr.wetest.net/blog/tencent-wetest-ai-agents-automated-testing-qa-1263.html)

WeTest 两套游戏测试方案：一类用“感知—操作—判断”的 Agent 结合游戏知识、实时状态与日志证据，决策调用稳定脚本并闭环验证；另一类训练对战型 Agent 并检验泛化（对训练集外 Boss 的胜率）。质量判断按功能覆盖是否达到 100%/90% 并追查失败根因。

> “We analyze whether each feature coverage reaches 100% or 90%, identify where failures occurred, and continue to investigate the root causes.”

**证据类型**：团队自述（产品博客）｜**对应原则**：[Q02](/handbook/12-quality-cicd#q02) [Q05](/handbook/12-quality-cicd#q05)

### TX22 · A.S.E（AICGSecEval）：仓库级 AI 生成代码安全评测基准 {#tx22}
**作者/机构**：腾讯悟空代码安全团队（GitHub 开源）｜**日期**：2026｜[原文](https://github.com/Tencent/AICGSecEval)

不在函数片段上评“AI 写的代码安不安全”，而是在真实仓库上下文里评，支持 LLM 直接生成与 Claude Code 等 Agent 生成两种模式，用 Docker 复现构建与验证。腾讯同组织下还开源了 VulnGym（白盒漏洞挖掘 Agent 基准）与 AI-Infra-Guard（Agent/MCP/Skills 扫描）。

> “A.S.E (AICGSecEval) is a repository-level AI-generated code security evaluation benchmark developed by Tencent Wukong Code Security Team.”

**证据类型**：开源仓库 README（团队自述）｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08) [P15](/compare/evidence#p15)

### TX23 · WorkBuddy 企业版与 AI Coding 的组织账：个人提效≠组织提效 {#tx23}
**作者/机构**：新浪财经（报道腾讯）｜**日期**：2026-06-09｜[原文](https://finance.sina.com.cn/jjxw/2026-06-09/doc-iniauvas6486062.shtml)

报道 WorkBuddy 企业版发布时引述的内部数据：初期 AI 生成代码接受度不足 30%，到 2025 年底 CodeBuddy 覆盖 90% 工程师、多数团队超 90% 代码由 AI 生成、编码时间缩短 40%。负责人把“需求从立项到上线的流转效率”作为是否真正赋能组织的判据。

> “刘毅强调，单纯的个人效率提升没有意义，只有需求从立项到上线的流转效率提升，才代表AI真正赋能组织。”

**证据类型**：高管口述（媒体报道）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12)
