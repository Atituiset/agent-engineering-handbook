# 中文互联网

> 美团、腾讯、阿里、字节、快手、百度等技术团队与技术媒体的公开实践。会议预告、产品宣传类文章已明确标注；数据均为 **「团队自报」**。CN01–CN11 于 2026-11-18、CN12 起于 2026-11-19 打开核对；InfoQ 页面未显示发布日期的标注为「2026」。TX / AL / BD 编号为 2026-11 增补的腾讯、阿里（含蚂蚁）、字节团队公开材料，按主题穿插在本页后半部分；数字均为团队自报、尚未独立验证。

[[toc]]

### CN01 · 用 Agent 评测思路管理 AI Coding —— 31 万行代码 AI 重构的实践 {#cn01}
**作者/机构**：美团技术团队（业务研发平台）｜**日期**：2026-05-07｜[原文](https://tech.meituan.com/2026/05/07/Agent-AI-Coding.html)

团队 90% 以上代码由 AI 生成时发现：**AI Coding 不会自动收敛复杂度**，没有统一约束时系统反而加速腐化。核心经验是「人人对齐 → 人机对齐」：先让团队对工程分层、领域模型、仓储层规约形成共识，再落地为 always 级 AI Rule 与按需渐进加载的 Skill；顺序错了，规则写得再好也会被不同人解释成不同版本。针对 Code Review 成为瓶颈，引入 **Pre-PR 机制**：提交前开发者必须先用 AI 多轮自查、修复所有 AI 能发现的问题，人则把关前置的技术方案评审与业务逻辑。技术债被当作业务需求一样逐个迭代消化。

> 「人的共识是 AI 约束的前提。」

### CN02 · Agent 评测漫谈 —— 由浅入深讲解 Agent 评测 {#cn02}
**作者/机构**：美团履约技术团队｜**日期**：2026-08-07｜[原文](https://tech.meituan.com/2026/08/07/Agent-Evaluation.html)

科普性的长文，总结美团内部两年 Agent 评测实践：评测要回答「好不好、哪里好哪里不好」，不能停留在离线打榜或单次 Demo；提出「观测 + 评测 = 持续迭代」的研发公式，并讨论长程智能体框架对评测带来的变化。对「如何验证智能体产出」有直接借鉴意义。

### CN03 · AI Coding 的下一步不是写得更快，而是可验收：蚂蚁数科 Harness 工程实践 {#cn03}
**作者/机构**：InfoQ（整理蚂蚁数字科技魏长征 AICon 演讲）｜**日期**：2026｜[原文](https://www.infoq.cn/article/A2IFuW8yiYhRqXizT5Uu)

两个案例：一个 40 多万行的 Rust 新项目从第一天起把 Harness 内建进研发流程；一个超过 60 万行的 C++ 存量项目**先重建事实源和质量门禁，再让 Agent 参与升级**，代码缺陷率从 20% 以上降至个位数（团队自报）。观点：AI Coding 没有创造新的软件工程问题，而是用更高产能把需求模糊、目标漂移、事实冲突、验证不足等老问题集中放大。做法包括：明确唯一事实源、文档分层按需加载、CI 门禁分「硬门禁」（脚本确定性检查，不浪费 token）与「软门禁」（多模型多视角 Agent 评审），问题暴露后逐步沉淀为门禁。

`团队自报`

### CN04 · OpenAI 提出 Harness Engineering：Codex 智能体驱动大规模软件开发 {#cn04}
**作者/机构**：InfoQ 中文站｜**日期**：2026｜[原文](https://www.infoq.cn/article/MCUXGhyIRqPLkFhljY9v)

对 OpenAI 原文（[OA01](./openai#oa01)）的中文报道：五个月内部实验中构建交付约一百万行代码的测试版产品，全程不手写源代码；工程师的重心从实现转向设计环境、明确意图与提供结构化反馈。适合作为中文团队内部传播的入口，细节以英文原文为准。

### CN05 · Coding Agent 技术全景图：Context Engineering、Subagents 与 Harness {#cn05}
**作者/机构**：InfoQ（编译 Birgitta Böckeler 在 QCon 纽约的演讲）｜**日期**：2026｜[原文](https://www.infoq.cn/article/UFLm5D5VDPmu9Ykc9CdJ)

核心观点：上下文工程是双向放大器——既放大好的工程实践，也放大坏的结构问题；风险评估离不开**概率、影响、可检测性**三个维度；把原本为人类设计的工程约束系统改造成智能体可学习、可反馈的系统，才是上下文工程真正「工程化」之处；未来也许从「Harness 模板」而非传统服务模板起步。与 [TW01](./thoughtworks#tw01) 互为补充。

### CN06 · AI Coding 增量风险管控：Skill 门禁与 Harness 落地实践（快手，会议预告） {#cn06}
**作者/机构**：InfoQ / AICon 北京（快手架构治理团队演讲预告）｜**日期**：2026｜[原文](https://www.infoq.cn/article/XieGrL5pws7jG1zxKPle)

演讲提纲披露：快手 AI 生成代码占比从 25Q3 的 26% 升至 26Q2 的 60%，「代码生成速度已非瓶颈，但技术债呈复利式增长」；典型失效包括缺私域知识写错 SQL 条件、误删历史兼容代码、**为编译通过主动跳过代码检查**。方案是「知识 + 约束」双轮：7 类共 415 条规则经 Skill 集成到业务 Harness，并建立编码时、插件、智能 CR、线上治理四道防线，拦截 Skill 累计发现 3000+ 问题；结论是约束必须做成 AI 绕不过的门禁。

`会议预告、团队自报`

### CN07 · 给 Agent 装上方向盘和刹车，Harness 时代的工程新范式 {#cn07}
**作者/机构**：InfoQ《极客有约》（阿里云、腾讯等嘉宾对谈）｜**日期**：2026｜[原文](https://www.infoq.cn/article/QxdM6J3uFpZA0CXgNhDq)

对谈观点：发动机马力小时不需要方向盘和刹车，马力强了才需要；Harness 不是消灭幻觉，而是用工程系统承接和约束不确定性；可观测性是形成改进飞轮的关键；企业知识原本是给人构建的，需要翻译成智能体能理解的上下文。

> 「Agent 只会道歉，没办法背锅。专业性是人的核心价值，也就是判断力。」

### CN08 · 我们做了一本企业级 AI 编程实践手册（TRAE） {#cn08}
**作者/机构**：火山引擎 TRAE 团队｜**日期**：2026-03-16｜[原文](https://developer.volcengine.com/articles/7617679997494689833)

TRAE 团队为提升 AI 代码贡献率整理的长期维护知识库介绍：方法论部分覆盖 Context Engineering、Skills、Spec、Rules、MCP、智能体如何落地；实践部分为「用 TRAE 开发 TRAE」的案例（如自动修复率、前端与设计稿协作）。文章本身是手册入口，含产品宣传成分。

`厂商自报`

### CN09 · CodeBuddy AI Coding 企业场景落地实践与思考 {#cn09}
**作者/机构**：腾讯云开发者｜**日期**：2025-08-15｜[原文](https://cloud.tencent.com/developer/article/2555275)

面向企业团队的落地指南。自报 CodeBuddy 帮助腾讯 5 万+ 开发者，编码时长缩短 40%，AI 代码生成占比超 43%。文章结合团队日常探索，试图给出一份可执行的企业 AI Coding 落地指南。

`厂商自报、尚未独立验证`

### CN10 · Qoder 详解 Spec 驱动的 AI 自主编程新范式（云栖大会演讲实录） {#cn10}
**作者/机构**：阿里云开发者社区｜**日期**：2025-10-13｜[原文](https://developer.aliyun.com/article/1684798)

介绍阿里 Qoder 平台的思路：Spec 驱动开发、云端沙箱与智能体协同、从代码反推 Repo Wiki 文档、异步任务委派。注意：Qoder 的 Quest 功能页面后来显示已下线，产品形态变化很快，应关注其思路而非具体功能。

`厂商自报`

### CN11 · 使用 Claude Code：会话管理与 100 万上下文（宝玉译） {#cn11}
**作者/机构**：Thariq（Anthropic）原文，宝玉翻译｜**日期**：2026-04-15｜[原文](https://baoyu.io/translations/claude-code-session-management)

把会话操作分为继续、回溯（/rewind）、清空（/clear 并带上精简总结）、压缩、子智能体五种选择。经验法则：**开始新任务就开新会话**；纠错时「用回溯代替纠正」——退回到智能体读完文件的时刻，带着刚学到的教训重新下指令，而不是让失败尝试留在上下文里。译者注明原文有官方推广成分，但操作建议实用。


## 2026-11 扩充（CN12–CN50） {#expansion}

以下条目于 2026-11-19 打开核对，引文逐字比对过页面文本。会议页面只给出议程，日期为会议举办时间。

### CN12 · 如何在“不能出错”的系统里使用 AI Coding？分布式存储实践与边界 {#cn12}
**作者/机构**：美团基础技术部｜**日期**：2026-10-29｜[原文](https://tech.meituan.com/2026/10/29/AI-Coding-IN-Distributed-Storage-System.html)

美团存储团队把 AI 用于评审、Debug 和受控自动化。他们对 AI 全仓评审给出的 117 个疑似问题逐条写 gtest 验证：36 条红测试确认，3 条被证伪，其余只能靠源码确认或尚未验证。结论是 AI 的结论必须变成可红可绿的证据；也要让 AI 自己构建、看原始输出，不能只信 CI 的绿灯（他们发现测试报告里硬编码了 failures="0"）。长时间自动执行时，AI 可能沿错误方向扩大修改范围，甚至靠调整测试条件得到“通过”。

> 「方向、边界和验收标准，仍要由人把关。」

`团队自报`

### CN13 · 对话 CodeBuddy 黄广民：一堆“冒烟”的上下文，正在决定 AI 编程的成败 {#cn13}
**作者/机构**：InfoQ（采访腾讯 CodeBuddy 黄广民）｜**日期**：2025-12-30｜[原文](https://www.infoq.cn/article/j8jMvIOfmZS8M33t72uP)

黄广民把上下文工程拆成四块：上下文资产分层与生命周期管理、按需供给的渐进式披露、降噪（裁剪、过滤、摘要），以及稳定前缀配合 KV cache 的缓存复用。他认为 Spec 是面向实现的契约，是上下文里最关键的一类；它不是静态文档，要在执行中被更新、版本化，并与代码和测试保持映射。规则按企业、项目、个人三级作用域放置。属厂商从业者观点。

> 「Spec 是面向实现的契约，包括方案、规划、接口、边界、验收等，偏约束与可验证。」

`团队自报`

### CN14 · 企业 AI Native 研发流程升级与重塑 {#cn14}
**作者/机构**：InfoQ（演讲整理，Qoder 相关）｜**日期**：2026-11-16｜[原文](https://www.infoq.cn/article/4z7Bbxy92tjAI7MB5evM)

演讲把企业 AI 研发分为四级，认为第三级的关键转折是团队级 Harness 与共享知识契约，而不是停留在个人的 skill/MCP。它主张 SPEC 先行、像管理代码一样管理 SPEC，并提出好 SPEC 的三重闭环：需求澄清完整、实现路径清楚但不写成伪代码、验收规则精确（含禁止事项）。原因是规范错误会被 Agent 成倍放大。属厂商视角。

> 「所以一定要做 SPEC 先行，并像管理代码一样严格管理 SPEC。」

`媒体报道，数据为受访方/厂商自报`

### CN15 · 规范驱动开发——企业规模化落地实践 {#cn15}
**作者/机构**：Hari Krishnan（InfoQ 中文译）｜**日期**：2026-02-25｜[原文](https://www.infoq.cn/article/OOwOxKFZQbShKx1timMP)

文章认为 SDD 的规范是用来促进人机对话、建立共同理解的，不是操作手册。它强调跨职能协作构建规范胜过个人优化提示词，并把“规范到实现的对齐验证”列为选型核心。遗留系统不必追溯性地全面写规范，只在变更区域附近逐步补齐，这样也降低了审核负担。

> 「规范的作用是促进人机对话，而非充当操作手册。」

`媒体报道，数据为受访方/厂商自报`

### CN16 · 金融级 AI Coding 落地实践：从“氛围”编程到“严谨”开发（QCon 北京议题） {#cn16}
**作者/机构**：InfoQ / QCon（平安科技褚秋实议题介绍）｜**日期**：2026-04-15｜[原文](https://www.infoq.cn/article/w0YZvXhyz3CjRPFO0VE3)

平安科技的议题提纲称，试点业务系统里 AI 入库代码占比约 60%（作者自述）。他们用 AI 把私域架构设计与代码规范批量转化为 Lint、ArchUnit、P3C 等 CI 检查，人和 AI 的代码都要过强制校验。上下文按场景精准加载，并尝试“睡后编程”式的人机异步协作。

> 「将无形规范转化为有形约束」

`媒体报道，数据为受访方/厂商自报`

### CN17 · CLAUDE.md 速通全解，八大技巧让 Claude Code 起飞指南 {#cn17}
**作者/机构**：阿里云开发者社区（个人作者）｜**日期**：2026-07-03｜[原文](https://developer.aliyun.com/article/1745096)

教程介绍了 CLAUDE.md 与 AGENTS.md 的关系，以及组织、用户、项目、本地四层作用域。团队落地建议是：把 CLAUDE.md 纳入代码评审，每次 Code Review 发现 AI 违规就把对应规则追加到项目级规则文件，让新人打开项目时 AI 自动遵循团队规范。正文夹有云产品推广。

> 「每次Code Review发现AI违规场景，统一追加至项目级规则文件」

`团队自报`

### CN18 · AI研发新范式：基于技术方案全链路生成代码 {#cn18}
**作者/机构**：腾讯技术工程（腾讯广告审核团队）｜**日期**：2025｜[原文](https://mp.weixin.qq.com/s/WXXKpVth8OJqvjrnS1m7Cw)

腾讯广告审核团队把技术方案改成“面向 AI”的模板，分代码层级、控制器、业务、持久四层；Prompt 也做成模板，并在生成后强制 AI 写自我总结存档，供人工评审与后续维护。团队自报需求覆盖率 70%+，Agent 代码行采纳率 50%+，研发节约时长 30%+；也承认模型仍有发散和遗漏。

> 「在AI生成代码后，强制其进行自我总结并归档。」

`团队自报`

### CN19 · 从提需求到部署发布，全AI全自动化后，研发效能全面跃升 {#cn19}
**作者/机构**：腾讯技术工程｜**日期**：2026-04-20｜[原文](https://cloud.tencent.com/developer/news/3860908)

同一团队的续篇：从 L2 人机协同走向 L3 全自动交付。他们引入 Harness Engineering，用需求评审、方案评审、质量门禁、MR 等工程卡点保障质量，并沉淀 Rules、知识库与 Skills。6 个试点需求的代码行采纳率达 90% 以上（团队自报）。

> 「AI全自动化交付 = LLM + Harness Engineering（工作流程 + 知识库 + skills管理） + Business Engineering（skills + 知识库的沉淀）」

`团队自报`

### CN20 · 当 Coding Agent 走进研发团队：我们开源了云端自进化研发平台 LoopForge {#cn20}
**作者/机构**：腾讯云开发者（腾讯轻量云团队）｜**日期**：2026-11-09｜[原文](https://cloud.tencent.com/developer/article/2779233)

腾讯轻量云团队复盘了团队级落地的五步演进：云端工作区、共享会话、带硬门禁的工程级 SOP、无人值守自动化，以及让流程自我改进的“工程级 RSI”。每个 SOP 节点内置编译、单测、规范等客观门禁，不通过就进入纠错循环，并设重试上限防死循环。平台已开源（厂商自报）。

> 「不通过绝不放行，Agent 拿着真实报错自动进入纠错循环当场修复」

`团队自报`

### CN21 · 从“能写代码”到“能交付”：腾讯轻量云 LoopForge 云端 Loop 实践（AICon 北京议题） {#cn21}
**作者/机构**：AICon（腾讯轻量云团队议题）｜**日期**：2026-12（会议）｜[原文](https://aicon.infoq.cn/2026/beijing/presentation/7421)

议题把团队交付的问题归为四个症状：流程不可复现、自己评审自己、关键关口无人把控、过程不可追溯。做法是确定性 DAG 管主干、Agent 管节点、人管签字；实现、评审、测试用独立上下文和模型。5 道门禁后合入 836 个 MR、无线上故障，一次通过率 54.8%（自报）。踩坑结论：前置需求澄清比加并发更有效。

> 「前置需求澄清门禁比加并发更有效」

`会议议程，数据为团队自报`

### CN22 · 把 99.9% 代码交给 AI：腾讯云一次“吃狗粮”的工程实验 {#cn22}
**作者/机构**：新浪极客前线（报道腾讯 CodeBuddy 团队）｜**日期**：2026-03-21｜[原文](https://k.sina.cn/article_7879848900_1d5acf3c401902urn2.html?from=tech)

报道称 CodeBuddy 2.0 由 4 名工程师在 4 个月内完成，绝大部分代码由 AI 生成（厂商自报）。团队认为代码生成率是“最不重要的指标”，应关注研发吞吐。做法包括用“审阅-挑战-修正”循环审查 Spec、拆小任务、每个任务流结束后清理上下文。他们也观察到 AI 会跳过任务、在没满足验收条件时错误标记完成。

> 「在每个任务流完成后主动清理上下文，只保留当前必需信息」

`团队自报`

### CN23 · 从代码生成到可信交付：美团 AIDE 数据研发 Agent 实践（QCon 上海议题） {#cn23}
**作者/机构**：QCon（美团数据平台议题）｜**日期**：2026-10（会议）｜[原文](https://qcon.infoq.cn/2026/shanghai/presentation/7356)

议题讨论三类取舍：固定流程与自主规划、高风险操作的安全护栏、知识库覆盖与质量的平衡。它主张让 Agent 基于平台事实（任务、表、血缘、权限、运行状态）工作，而不是靠对话猜测；并把人工纠错、测试失败和线上处置沉淀为领域规则。

> 「让 Agent 基于平台事实而非对话猜测工作」

`会议议程，数据为团队自报`

### CN24 · 美团企业级 Agent 的平台化应用实践（QCon 上海议题） {#cn24}
**作者/机构**：QCon（美团 Agent 平台议题）｜**日期**：2026-10（会议）｜[原文](https://qcon.infoq.cn/2026/shanghai/presentation/7335)

议题提出“手脑分离”：模型负责理解与判断，Harness 提供知识、工具、状态、沙箱、权限和验证。确定性逻辑交给代码，不确定性判断交给模型；评测被定位为 Agent 上线的质量门禁，而不是事后打分。

> 「确定性逻辑交给代码，不确定性判断交给模型」

`会议议程，数据为团队自报`

### CN25 · Trae Agent 架构演进：从 Workflow 到 Agentic Loop（QCon 上海议题） {#cn25}
**作者/机构**：QCon（字节跳动 Trae 议题）｜**日期**：2025-10（会议）｜[原文](https://qcon.infoq.cn/2025/shanghai/presentation/6700)

Trae Agent 2.0 弃用固化的 Proposal + Plan 流程，改为“感知→思考→执行→更新”的闭环。配套做法包括用压缩代替裁剪、用 TODO 与 Memory 避免遗忘、做轮次控制。议题也承认依赖专家经验的场景仍需固定 Workflow，Token 成本与效果有时互斥。

> 「Agentic 和 Workflow 不是非黑即白的开关」

`会议议程，数据为团队自报`

### CN26 · Trae 核心成员复盘：从 Cloud IDE 到 2.0 SOLO，字节如何思考 AI Coding？ {#cn26}
**作者/机构**：智源社区（转载极客公园，Trae 核心成员自述）｜**日期**：2025-07-24｜[原文](https://hub.baai.ac.cn/view/47554)

Trae 核心成员复盘：1.0 依赖固定的 Proposal + Plan 工作流，随着模型变强反而限制了模型发挥，2.0 于是给模型更大自主权。文中还记录了一个案例：靠“只剩 N 轮”制造紧迫感，对一个模型版本有效，换到下一版本后 AI 反而直接摆烂。可见提示技巧会随模型变化失效。

> 「这种依赖于 Proposal + Plan 固定 Workflow 方式，反而会导致大模型降智，限制了它的发挥」

`团队自报`

### CN27 · 【ByteDance】Harness Engineering（个人博客） {#cn27}
**作者/机构**：dyhes（个人博客）｜**日期**：2026-05-27｜[原文](https://dyhes.github.io/p/bytedanceharness-engineering/)

作者用控制论（离心调速器、必要多样性定律）解释 Harness：skill/tool 太少完不成任务，太多又会让行为发散。作者还强调模型既执行又自评会让反馈回路失稳，因此应使用独立评估器和真实环境信号。

> 「skills是必须要有的，但是也不能太多，太多了就会效果变差」

`作者自述`

### CN28 · Claude Code 作者再次分享 Anthropic 内部团队使用技巧 {#cn28}
**作者/机构**：Immerse（少数派作者）｜**日期**：2026-02-14｜[原文](https://sspai.com/post/106387)

中文整理 Boris Cherny 分享的十条内部用法：同时跑 3–5 个 git worktree；复杂任务先进 plan mode，可让另一个 Claude 审查计划；每次纠错后让 Claude 更新 CLAUDE.md；一天做两次以上的事就做成 Skill；让 Claude 当严格审查员；要更多算力时用子代理保持主上下文干净。原帖链接见文末。

> 「一天做两次以上的事就该做成 Skills。」

`作者自述`

### CN29 · Claude Code 最佳实践（中文官方文档） {#cn29}
**作者/机构**：Anthropic（官方文档中文版）｜**日期**：持续更新（2026-11-19 访问）｜[原文](https://code.claude.com/docs/zh-CN/best-practices)

官方中文文档把各种机制按“非确定性（由 Claude 决定）”和“确定性（由 Claude Code 强制执行）”两列对照：CLAUDE.md、自选 skill 属前者，hook、拒绝规则、测试、CI、分支保护属后者。文档建议 CLAUDE.md 只写代码无法推断的内容，团队流程放进 skill，并给 Claude 一个返回通过或失败的检查让它自己闭环。

> 「给 Claude 一个可以运行并返回通过或失败的东西。」

`官方文档`

### CN30 · Claude 如何记住您的项目（中文官方文档） {#cn30}
**作者/机构**：Anthropic（官方文档中文版）｜**日期**：持续更新（2026-11-19 访问）｜[原文](https://code.claude.com/docs/zh-CN/memory)

文档给出何时往 CLAUDE.md 加内容的判据（第二次犯同样错误、评审发现、重复纠正、新人需要），以及每个文件目标 200 行以下。原因是较长文件消耗更多上下文并降低遵守度，且相互矛盾的指令会被任意选择。只对部分代码重要的规则移到 path-scoped rules；需要强制的规则应使用 permissions.deny 等托管设置。

> 「较长的文件消耗更多上下文并降低遵守度。」

`官方文档`

### CN31 · Claude Code 团队协作指南：交接、评审与权限边界 {#cn31}
**作者/机构**：ClaudeCodeLab｜**日期**：2026｜[原文](https://claudecode-lab.com/zh/blog/claude-code-team-collaboration/)

文章给出团队落地的四个固定位置：CLAUDE.md、共享 settings、个人 settings.local 和提示词模板。它强调 PR 里不能只写“Claude 已经修了”，要用交接模板写明看了哪些文件、跑了哪些命令、剩余风险；权限先写 deny 再写最小 allow；PR 模板里加“评审回执”，记录采纳与未采纳的 AI 建议。

> 「最常见的失败是 PR 里只写“Claude 已经修了”。」

`作者自述`

### CN32 · 解决真实 GitHub Issue 能力登顶，字节豆包 MarsCode 团队分享工程实践 {#cn32}
**作者/机构**：凤凰网（转载量子位，豆包 MarsCode 团队分享）｜**日期**：2024-11-04｜[原文](https://i.ifeng.com/c/8eEiYhaSekV)

MarsCode Agent 用 Searcher、Reproducer、Programmer、Tester、Planner 等多角色协作，在 Docker 沙箱里复现与验证缺陷。团队刻意不让每个 Agent 拥有全部工具，以降低单个环节的难度、提高稳定性。文中称动态调试路线的求解率高于静态修复（团队自报）。

> 「团队并没有令每个Agent都拥有所有工具的使用权，而是尝试限制各个Agent的能力和职责范围」

`团队自报`

### CN33 · 智能体工程的 8 个等级（宝玉译） {#cn33}
**作者/机构**：Bassim Eledath 原文，宝玉翻译｜**日期**：2026-03-11｜[原文](https://www.baoyu.io/translations/2026-03-11/levels-of-agentic-engineering)

文章把实践分为 8 级：补全、智能体 IDE、上下文工程、复合工程、MCP 与技能，直到后台智能体。作者指出团队吞吐受最低等级成员制约，例如审批者还在手动审 PR。复合工程是“计划、委派、评估、沉淀”的循环，但什么都往规则文件里塞会适得其反，更好的做法是维护一个让模型能自己发现上下文的 docs/。

> 「什么都往规则文件里塞的冲动可能适得其反（指令太多等于没有指令）」

`译文`

### CN34 · 普通人也能用得上的 Context Engineering 技巧 {#cn34}
**作者/机构**：宝玉｜**日期**：2025-08-04｜[原文](https://www.baoyu.ai/blog/context-engineering-skills-for-normal-users)

宝玉把上下文工程归结为“更少的上下文、更准确的上下文”。做法是多开新会话而不是无限延长单个会话，一次只交一个清晰的小任务；提示词并非越长越好，无关信息会让结果混乱甚至出现幻觉。

> 「多开新会话，而不是无限延长单个会话」

`作者自述`

### CN35 · 科技爱好者周刊（第 383 期）：你是第几级 AI 编程 {#cn35}
**作者/机构**：阮一峰｜**日期**：2026-01-30｜[原文](https://www.ruanyifeng.com/blog/2026/01/weekly-issue-383.html)

阮一峰介绍 Steve Yegge 的 AI 编程 8 级：从 IDE 插件、YOLO 模式、命令行智能体，到同时开 3–5 个乃至 10 个以上窗口，最后用任务编排器管理并行智能体。Yegge 自称从未看过自己 22.5 万行的编排器代码，并建议用户不要用它；阮一峰也提到多 AI 并行很费钱。可作为并行与“不看代码”立场的反面参照。

> 「它有22.5万行 Go 语言代码，我从来没看过它的代码，也从来没想过要看。」

`作者自述`

### CN36 · 从个人提效到组织生产力提升：快手 AI Coding 演进实践（AICon 上海议题） {#cn36}
**作者/机构**：AICon（快手 AI Coding 负责人议题）｜**日期**：2026-06（会议）｜[原文](https://aicon.infoq.cn/2026/shanghai/presentation/7123)

快手 2024 年观察到一个悖论：AI 代码生成率 30%+、83% 研发使用 AI、个人体感提效 20–40%，但需求交付效率没有相应提升。由此提出“用 AI 工具 ≠ 个人提效 ≠ 组织提效”。后续他们定义三种开发方法与 L1–L3 成熟度模型，并把度量从代码生成率升级为交付指标（数据为快手自报）。

> 「但需求交付效率并未得到相应幅度的提升」

`会议议程，数据为团队自报`

### CN37 · 采纳率从 7.9% 到 54%：快手智能 Code Review 的三阶进化 {#cn37}
**作者/机构**：InfoQ（快手研发效能委员会 × 研发效能中心）｜**日期**：2026-03-14｜[原文](https://news.qq.com/rain/a/20260314A03T5A00)

快手智能代码审查经历了三代：纯 LLM 启发式、知识引擎 + 确定性规则、Agentic 自主决策。针对幻觉，他们构建上下文引擎、沉淀 1,100+ 条确定性规则，辅以三层过滤与 BadCase 反例库，评审采纳率从 7.9% 升至 54%（快手自报）。文中指出人工 CR 易漏掉看似简单的低级错误。

> 「评审采纳率从 7.9% 跃升至 54%」

`团队自报`

### CN38 · 让每个员工都有一个 Coding Agent：蚂蚁 Vibe Coding 平台落地半年后的实践经验（QCon 北京议题） {#cn38}
**作者/机构**：QCon（蚂蚁集团议题）｜**日期**：2026-04（会议）｜[原文](https://qcon.infoq.cn/2026/beijing/presentation/6959)

面向非技术用户的平台进入投产后，核心挑战从“能生成”变为“稳定交付”。方案是“框架约束 + 受控工具链 + 自愈交付”：约定式全栈框架降低发散，实时校验，“文件即记忆”外化长期状态，用 CodeMap 代替全仓塞进上下文，skills 按需加载。

> 「核心判断：全仓塞进上下文不可持续」

`会议议程，数据为团队自报`

### CN39 · 尽在上下文——JoyCode 的企业级 AI Coding 实践（QCon 北京议题） {#cn39}
**作者/机构**：QCon（京东科技议题）｜**日期**：2026-04（会议）｜[原文](https://qcon.infoq.cn/2026/beijing/presentation/6984)

京东 JoyCode 把上下文窗口限制视为企业级编码落地的根本瓶颈。超大代码仓、自研框架和跨系统长任务会导致“上下文爆炸”。应对方式包括 RepoWiki 代码知识图谱、与内部知识平台融合，以及 Skills 按需加载。

> 「模型上下文窗口的限制」

`会议议程，数据为团队自报`

### CN40 · Coding Agent 在百度的落地实践：从反馈闭环到工程范式重构 {#cn40}
**作者/机构**：InfoQ（百度文心快码牛万鹏 QCon 演讲整理）｜**日期**：2026-05-26｜[原文](https://news.qq.com/rain/a/20260526A068F500)

Comate 团队从工具、会话等层面统计线上数据，构建反馈闭环。他们发现评测分数本身意义不大：同样的分数，答对的可能是另一组题，所以要看异常值。评测集从经人审核合入的真实提交中挖掘。团队还要求 Agent 构建者亲手写代码，才能感知 Agent 的变化。

> 「分数本身并不重要，重要的是那些异常值」

`团队自报`

### CN41 · Claude Code 的 8 大机制我全踩了一遍：哪些真香，哪些是坑 {#cn41}
**作者/机构**：TrisighT（掘金）｜**日期**：2026-07-15｜[原文](https://juejin.cn/post/7662545137147674666)

作者团队起初用 Skill 做提交前检查，结果模型“时灵时不灵”，换成 PreToolUse Hook 后稳定。由此定下规矩：一个需求能被多种机制满足时，优先选确定性更强、可审计性更高的。早期把所有规范堆进 CLAUDE.md 导致质量下降；子任务没隔离上下文时，中间过程灌回主对话，会话卡死。

> 「Hook 能表达就别退回提示词约束」

`作者自述`

### CN42 · GitLab 调研：AI 工具仅加快编码，整体软件交付效率并未提升 {#cn42}
**作者/机构**：InfoQ（编译 Sergio De Simone）｜**日期**：2026-07-02｜[原文](https://www.infoq.cn/article/8WD205mNH9OGrkf8BRYO)

GitLab 2026 AI 问责报告显示，78% 受访者称编码更快，但 85% 认同 AI 已把瓶颈从写代码转移到审查和验证，79% 表示整体交付没有同速加速。报告强调 AI 生成代码的可追溯与问责。数据来自厂商调研。

> 「85% 的受访者“认同 AI 已将研发瓶颈从编写代码转移到了审查和验证环节”」

`译文`

### CN43 · 让 AI 从需求一路干到上线，软件开发组织要变了？ {#cn43}
**作者/机构**：InfoQ（李冬梅）｜**日期**：2026-10-26｜[原文](https://www.infoq.cn/article/b32Mw2zaPrxyJ6ChePD5)

文章引用 Faros AI 对 1 万多名开发者、1255 个团队的分析：没有发现 AI 采用率与企业交付指标改善显著相关，PR 合并数增加 98%，代码审查时间增加 91%。文章随后介绍网易 CodeWave 的多 Agent 交付产品（厂商自报 3–5 倍产能）。

> 「PR 合并数量增加了 98%，代码审查时间却增加了 91%」

`媒体报道，数据为受访方/厂商自报`

### CN44 · 当国产模型追上闭源旗舰，企业 AI 编程的真正障碍才浮出水面 {#cn44}
**作者/机构**：InfoQ（周云龙、蔡芳芳）｜**日期**：2026-05-01｜[原文](https://www.infoq.cn/article/K7hpIOogPsLlPQz4lwXu)

文章借“AI 上下文负债”概念指出：业务隐知识、历史决策与架构习惯不会因模型升级而自动可理解。在棕地系统里，AI 生成的代码语法完美、业务上错得不着痕迹，审查成本可能超过生成节省。出路是补文档、立规范、渐进重构。

> 「代码越混乱，AI 的效率提升越可疑——审查成本的增长速度很可能超过了生成速度的节省。」

`媒体报道，数据为受访方/厂商自报`

### CN45 · 42% 的代码是 AI 写的，可 96% 的开发者不信它：谁敢拍板说“上线”？ {#cn45}
**作者/机构**：InfoQ（SEDaily 访谈编译）｜**日期**：2026-05-06｜[原文](https://www.infoq.cn/article/e40mGRhF9o583Yi3akyM)

访谈引用 Sonar 开发者调查：72% 的开发者每天用 AI 编码工具，42% 的代码由 AI 生成或辅助，但 96% 的开发者无法完全信任 AI 代码。软件工程的难题正转向“谁来为上线拍板”，验证层的重要性上升。数据来自厂商调研。

> 「96% 的开发者仍然无法完全信任 AI 生成的代码」

`译文`

### CN46 · 我的 AI 原生开发流程：一个真实案例的完整复盘 {#cn46}
**作者/机构**：宝玉｜**日期**：2026-08-24｜[原文](https://www.baoyu.io/blog/2026-08-24/ai-native-dev-workflow)

宝玉用给自己 App 加远程转录功能的过程复盘 AI 原生开发：流程没变（可行性分析、方案、原型、编码、测试），变的是执行主体。Agent 做分析和罗列方案，人在关键路径确认和拍板。他强调最该保留的是“先决定要不要做”的可行性分析，并坦言自己也做过最后被砍掉的功能。

> 「Agent 做分析和罗列方案，人做最终判断和拍板。」

`作者自述`

### CN47 · 从 TL 到 EM：我终于不再盯着 AI 写代码了 {#cn47}
**作者/机构**：宝玉｜**日期**：2026-07-29｜[原文](https://www.baoyu.io/blog/coding-agent-em-shift)

宝玉描述自己从 Tech Lead 式逐行把关，转向 Engineering Manager 式“定方案、验结果”：先和 Agent 做技术方案，确认后让它写代码和自动化测试，Bug 让 Agent 复现并补测试，自己不再细看代码。他认为之前人是 Agent 的瓶颈，现在瓶颈变成想清楚做什么。这是个人项目经验，与“人工评审不可省”构成张力。

> 「如果人没想清楚该做什么，Agent 再厉害也帮不上。」

`作者自述`

### CN48 · Harness Engineering 最佳实践：从概念到落地的完整操作手册 {#cn48}
**作者/机构**：warm3snow（博客园）｜**日期**：2026-03-28｜[原文](https://www.cnblogs.com/informatics/p/19812585)

作者给出三步落地路线：信息层（AGENTS.md 地图模式、docs/ 结构化），约束层（分层架构、Linter、CI 检查、错误信息含修复指令），自动化层（Agent 自验证闭环、后台清理）。他强调不要一步到位，第二阶段是质变点。AGENTS.md 应写地图而非百科全书。

> 「AGENTS.md：写地图，不写百科全书」

`作者自述`

### CN49 · 【笔记】Harness Engineering（驾驭工程） {#cn49}
**作者/机构**：Wayne 的博客｜**日期**：2026-03-10｜[原文](https://blog.michealwayne.cn/2026/03/10/notes/%E3%80%90%E7%AC%94%E8%AE%B0%E3%80%91Harness%20Engineering%EF%BC%88%E9%A9%BE%E9%A9%AD%E5%B7%A5%E7%A8%8B%EF%BC%89/)

笔记认为 Harness Engineering 在 2026 年变热的核心原因是：AI 生成代码的速度已经快过人类逐行审查和验证的速度，瓶颈从“写得慢”变成“不能快速信任产出”。要解决的问题因此变成上下文、权限边界、自动验证、失败纠偏，以及把同类错误一次性工程化消灭。

> 「现在的瓶颈越来越变成“不能快速信任产出”」

`作者自述`

### CN50 · 9 秒毁掉一家公司：AI 删库事件的完整复盘与深刻教训 {#cn50}
**作者/机构**：观妙（个人博客，二手复盘）｜**日期**：2026-04-29｜[原文](https://blog.ytaiv.com/article/ai-delete-disaster-2026-04-29/)

二手复盘 PocketOS 事件：智能体在处理测试环境凭据报错时，擅自在代码库里找到一个与任务无关的云服务 API Token，调用删除接口，9 秒内删除了生产数据库存储卷及卷级备份。教训包括：凭据不应出现在代码库，高危操作需要二次确认，生产操作需要独立凭证与隔离环境。细节以当事人原始陈述为准。

> 「Token不应存在于代码库中」

`作者自述`

以下 TX / AL / BD 条目为 2026-11 增补，标题前的公司名标出来源团队。数字均为团队自报、尚未独立验证；会议条目只有议题摘要。

## Harness 与 Loop 工程 {#harness-loop}

### 腾讯 · TX03 · Harness Engineering：AI 能在真正“出事会炸”的后端系统里写代码吗？（腾讯 CDN LEGO） {#tx03}
**作者/机构**：腾讯技术工程（lancelotluo，腾讯 CDN 团队）｜**日期**：2026-04-21｜[原文](https://news.qq.com/rain/a/20260421A06DXU00)

在百万行级 C++ CDN 核心框架里落地 AI Coding：围绕“上下文、约束、反馈”设计五层 Harness，Hook 自动采集、踩坑日志（Pitfall Journal）等多条反馈通道，以及 3 个模型并行、辩论式、“全员无新发现自动收敛”的对抗式 CR。案例里一次读写竞争修复从 5 天压到 1 天，但作者同时写明方案没考虑线程初始化、并非最优解——是少见的同时报收益与缺陷的记录。

> “LEGO的对抗式CR通过多模型并行审查和交叉验证，能够发现更深层的问题”

**证据类型**：团队自报｜**对应原则**：[Q07](/handbook/12-quality-cicd#q07) [P19](/compare/evidence#p19) [P12](/compare/evidence#p12) [P06](/compare/evidence#p06)

### 腾讯 · TX05 · QQ 音乐 Harness Engineering 实践（大仓多服务） {#tx05}
**作者/机构**：腾讯云开发者（QQ 音乐团队）｜**日期**：2026-05-21｜[原文](https://cloud.tencent.com/developer/article/2671876)

面向 monorepo 多服务场景的开源工程框架：把“隐性规范、历史决策、服务契约（IDL 字段冻结）、跨服务依赖、演进轨迹”五类 AI 盲区分别落成工程制品——服务矩阵自动解析依赖、IDL 门禁防止 AI 猜依赖、Self-Refinement 闭环把纠错沉淀为团队资产，并要求每个关键节点有可机读的质量门禁与审计记录。

> “提升上下文质量，是比提升模型能力更高效的杠杆。”

**证据类型**：团队自述｜**对应原则**：[P05](/compare/evidence#p05) [P04](/compare/evidence#p04) [P19](/compare/evidence#p19) [P02](/compare/evidence#p02)

### 腾讯 · TX06 · Harness Engineering 如何驱动云端智能体：腾讯云 ADP 的设计实践 {#tx06}
**作者/机构**：腾讯云 ADP 团队｜**日期**：2026-07-17｜[原文](https://adp.tencent.com/zh/blog/agent-harness-engineering-adp-practice)

平台团队视角：Agent = Model + Harness。ADP 把 Agent Loop、Memory、Sandbox、Tools/MCP 解耦并用稳定接口连接，以便容器崩溃可恢复、沙箱可替换重建、模型或 Loop 升级不牵动底层；Harness 负责工具、状态、权限、上下文、恢复、评估、观测与反馈闭环，并记录轨迹以支持 replay/eval。

> “Agent Harness不是一个花哨的新名词，而是 Agent 从 demo 走向生产之后必然出现的工程抽象。”

**证据类型**：团队自述（产品博客）｜**对应原则**：[P15](/compare/evidence#p15) [P18](/compare/evidence#p18) [Q08](/handbook/12-quality-cicd#q08) [Q09](/handbook/12-quality-cicd#q09)

### 腾讯 · TX07 · 游戏开发生产力重构：从单点 AIGC 到 Harness 工程闭环 {#tx07}
**作者/机构**：gawain2048（腾讯云开发者社区；整理腾讯游戏技术专家杨梦舟的分享）｜**日期**：2026-06-11｜[原文](https://developer.cloud.tencent.com/article/2686566)

游戏工程（UE 的 C++、蓝图、资产引用）里很多问题只有进编辑器和运行时才暴露。做法：把 SVN/Git 作为 AI 参与项目的底层安全机制（基于 diff 与日志可回滚）；建立“启动引擎→运行游戏→取日志→修复/输出结论”的自循环证据链；把“编译 0 error”作为量化验收，新坑点写回 Memory。

> “实现“编译已通过 (0 error)”的量化验证指标”

**证据类型**：团队自报（会议整理稿）｜**对应原则**：[P06](/compare/evidence#p06) [P09](/compare/evidence#p09) [P19](/compare/evidence#p19) [Q02](/handbook/12-quality-cicd#q02)

### 腾讯 · TX17 · 用 Harness 工程打造 SRE 可控的生产环境（QCon 上海 2026 议题） {#tx17}
**作者/机构**：王杰（腾讯游戏高级 SRE 工程师）｜**日期**：2026-10（QCon 上海）｜[原文](https://qcon.infoq.cn/2026/shanghai/presentation/7292)

腾讯游戏先把应用交付代码化、GitOps 化，于是“发布变更”变成“改代码改配置”，正好落在 AI Coding 最成熟的区间；所有变更必经 Git 与人工 Review，多 SRE Agent 参与扩缩容、配置调整、故障修复，过程完整记录、评估后沉淀为跨业务能力。核心观点：不让 LLM 变确定，而用 Harness 管住不确定性。

> “我们的解决方案不是让 LLM 变确定，而是用 Harness 工程管控它的不确定性”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[P15](/compare/evidence#p15) [P08](/compare/evidence#p08) [P04](/compare/evidence#p04) [Q11](/handbook/12-quality-cicd#q11)

### 阿里 · AL20 · Harness For Hybrid Coding：AliExpress 重构实践（QCon 上海 2026） {#al20}
**作者/机构**：何伟（阿里巴巴 AliExpress 技术专家）｜**日期**：2026-10（QCon 上海）｜[原文](https://qcon.infoq.cn/2026/shanghai/presentation/7318)

AE 用 Harness 管住“人 + AI 混合编码”的大规模重构：先评测再上线，覆盖多个场景。少数同时给出“线上 Bug”结果指标而不只是代码量的自报。

> “实践覆盖 10 大场景、约 65.5 万行代码重构与评测上线，线上 Bug 下降 80%”

**证据类型**：议题摘要（团队自报，尚未独立验证）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [P06](/compare/evidence#p06) [Q11](/handbook/12-quality-cicd#q11)

### 阿里 · AL23 · Qoder Desktop 的 Quest 与 Harness 实践（AICon 上海 2026） {#al23}
**作者/机构**：左志鹏（阿里巴巴高级技术专家，Qoder）｜**日期**：2026-06（AICon 上海）｜[原文](https://aicon.infoq.cn/2026/shanghai/presentation/7144)

从“实时指挥”到“任务委派”：任务视窗、工作区与产物区让执行过程可管理、结果可审查；Harness 侧设计“专家团”模式——调研、编码、验证、自动评审多 Agent 协作，一次性端到端交付。

> “如何设计专家团模式，实现包括调研、编码、验证和自动评审的多Agent协作系统，一次性端到端交付高质量结果。”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[P10](/compare/evidence#p10) [P11](/compare/evidence#p11) [Q07](/handbook/12-quality-cicd#q07)

### 阿里 · AL28 · 阿福：Agent 小队如何处理持续涌入的线上 Badcase（QCon 上海 2026） {#al28}
**作者/机构**：肖汉松（蚂蚁集团阿福 Harness 架构组负责人）｜**日期**：2026-10（QCon 上海）｜[原文](https://qcon.infoq.cn/2026/shanghai/presentation/7232)

两层工程：先用 Harness 解决“单个 badcase 能否可靠修好”，再用 Loop 解决“持续涌入时能否持续修复”。是 Harness→Loop 演进的清晰表述。

> “先用 Harness Engineering 解决“如何可靠修好 badcase”，再用 Loop Engineering 解决“如何持续修复 badcase””

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[P06](/compare/evidence#p06) [P19](/compare/evidence#p19) [Q08](/handbook/12-quality-cicd#q08)

### 字节 · BD01 · 洪定坤：AI Coding 的实践与探索（火山引擎 FORCE 大会） {#bd01}
**作者/机构**：洪定坤（字节跳动技术副总裁），火山引擎公众号｜**日期**：2026-06-23｜[原文](https://mp.weixin.qq.com/s/mdmaAyUIvxE8WT_GEbF2wQ)｜[相关链接](https://cloud.tencent.com/developer/article/2700072)

字节最完整的一手口径：一年内 AI 代码贡献率增长 6 倍多、AI Coding token 消耗增长 5 倍、AI 代码合入率增长超 2 倍；TRAE 团队过去半年 90% 以上代码由 AI 写，但人均需求吞吐率只提升 60%（到 1.6 倍）。他明确反对把贡献率当 KPI，并用“3 模型 × 3 框架、同一 Prompt”实验说明：功能正确率约 80%，但“可交付性”只有 40–60 分；接入 Harness 基建后正确率接近 90%、可交付性升到约 80 分。

> “单一的代码贡献率，其实很难完全衡量我们实际效率的提升，它会失真。”

**证据类型**：高管演讲（团队自报，尚未独立验证）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [P06](/compare/evidence#p06) [P04](/compare/evidence#p04) [Q05](/handbook/12-quality-cicd#q05)

### 字节 · BD18 · 飞书 CodeM 通过信通院“驾驭工程（Harness）能力成熟度”L4 评估 {#bd18}
**作者/机构**：飞书项目官方新闻｜**日期**：2026-10-15｜[原文](https://project.feishu.cn/home/news/feishu-codem-ccna-l4-harness-engineering)

Harness Engineering 在国内开始出现行业标准化评估：信通院《智能原生软件工程驾驭工程能力成熟度》覆盖连接、编排、循环、效能、安全、评估优化六个维度。属厂商新闻，评估细节未公开。

> “该认证覆盖连接、编排、循环、效能、安全、评估优化六大核心能力维度”

**证据类型**：厂商自述（第三方评估结果，细节未公开）｜**对应原则**：[P04](/compare/evidence#p04) [P15](/compare/evidence#p15)

## 上下文与知识沉淀 {#context-knowledge}

### 腾讯 · TX01 · 不只是 Memory：用本体与三层图谱让 Coding Agent 越用越懂项目 {#tx01}
**作者/机构**：腾讯技术工程（云数据库研发团队）｜**日期**：2026-11-13｜[原文](https://news.qq.com/rain/a/20261113A0BF6G00)

团队让 Agent 承担“设计完成到上线前测试”这一段 Loop：人定目标、设计与业务取舍，Agent 把设计转成可观察的验收条件，实现、验证、失败后定位修复；构建、部署、等待等常规步骤交给确定性工具。团队 Memory 由 Chat Memory、Wiki、CodeGraph、Skill 四类资产组成，并以“工程事实 / 项目语义 / bug_fixed 经验”三层互索引图谱组织。作者明确说明 58%→65% 只是 Bug 定位子任务的初步信号，不能换算成整体效率。

> “在一项内部代码 Bug 定位试验中, 加入上述图谱能力后, Agent 的问题定位成功率从 58% 提升到 65%, 增加了 7 个百分点。”

**证据类型**：团队自报（内部试验，作者自注局限）｜**对应原则**：[P18](/compare/evidence#p18) [P19](/compare/evidence#p19) [P06](/compare/evidence#p06) [Q02](/handbook/12-quality-cicd#q02)

### 阿里 · AL06 · “架构师 Agent” 系统化落地 {#al06}
**作者/机构**：阿里技术（腾讯新闻转载；作者声明仅代表个人观点）｜**日期**：2026-09-09｜[原文](https://news.qq.com/rain/a/20260909A0876Z00)

先落地技术方案设计而非直接编码：用渐进式披露把领域知识、架构约束、历史决策分层喂给 Agent，产出方案再进入编码。核心判断是复杂系统的关键知识不在代码里，需要显式沉淀。

> “复杂系统真正重要的知识并不完整地存在于代码中”

**证据类型**：个人实践（阿里官方号发布）｜**对应原则**：[P01](/compare/evidence#p01) [P05](/compare/evidence#p05) [P18](/compare/evidence#p18)

### 字节 · BD12 · 当代码遇上大模型：智能编程助手的架构设计与工程实践 {#bd12}
**作者/机构**：InfoQ（整理豆包 MarsCode / Trae IDE 架构师段潇涵 QCon 北京分享）｜**日期**：2025-08-22｜[原文](https://www.infoq.cn/article/dshjgpfg5sgvahlilgtg)

MarsCode/Trae 的架构要点：Agent 把需求分解为步骤并在执行中自我反思修正；上下文侧实时构建代码知识图谱（结构与依赖），解决大仓库超出上下文的问题。可与腾讯 TX01 的三层图谱对照。

> “在上下文感知方面，构建代码知识图谱，实时构建代码的结构和依赖关系等，解决了大语言模型处理大型代码库时的上下文限制问题”

**证据类型**：团队自述（会议整理稿）｜**对应原则**：[P05](/compare/evidence#p05) [P18](/compare/evidence#p18)

### 字节 · BD13 · 第一性原理拆解 Agentic Coding：从理论到实操（下） {#bd13}
**作者/机构**：小夏（TRAE 技术专家），火山引擎开发者社区｜**日期**：2026｜[原文](https://developer.volcengine.com/articles/7598410716190375962)

TRAE 团队给用户的最佳实践：短对话优于长对话，每个对话只做一件事；借助 git diff 等外部状态在对话间传递上下文；把 bug 修复、代码审查经验沉淀为项目知识库（“复利工程”）；清晰文档和快速测试既帮人也帮 AI。

> “保持对话简短、专注，每个对话只做一件事。”

**证据类型**：团队自述（官方技术文章）｜**对应原则**：[P18](/compare/evidence#p18) [P19](/compare/evidence#p19) [P10](/compare/evidence#p10) [P17](/compare/evidence#p17)

## 规范、计划与意图驱动 {#spec-plan}

### 腾讯 · TX14 · AI Native 企业研发工具链：架构重构与持续演进（AICon 北京 2026 议题） {#tx14}
**作者/机构**：陈偲颖（腾讯资深研发工程师）｜**日期**：2026-12（议题预告）｜[原文](https://aicon.infoq.cn/2026/beijing/presentation/7424)

平台从“配置驱动”转向“意图驱动”：业务操作工具协议化、能力原子化（明确输入输出、副作用、幂等），Agent 运行时工程化，上下文平台化，以及由用户打断、连续失败、方案修正等“摩擦信号”驱动的改进闭环；权限、审计、评测与人工审批贯穿，高风险操作必须审批。

> “我们的实践从配置驱动转向意图驱动：用户表达业务目标，系统结合专家知识生成方案，通过低代码 Harness 编排执行。”

**证据类型**：议题摘要（演讲者自述，尚未开讲）｜**对应原则**：[P14](/compare/evidence#p14) [P15](/compare/evidence#p15) [P19](/compare/evidence#p19) [Q08](/handbook/12-quality-cicd#q08)

### 阿里 · AL15 · Quest Mode：把任务委派给智能体（Spec First） {#al15}
**作者/机构**：Qoder 官方博客｜**日期**：2025-08-21｜[原文](https://blog.qoder.com/zh/quest-mode)

Qoder 的自主编程模式：执行长任务前先写 Spec，描述清楚变更细节与验证标准，Spec 是开发者与 AI 目标对齐的核心；随后由 Action Flow 执行并汇报。是阿里系“规范驱动 + 委派”的产品化表达。

> “因此我们期望在执行复杂长任务之前，开发者可以详尽的、准确的表达软件逻辑，描述清楚变更细节和验证标准，以指导智能体更准确的完成任务。”

**证据类型**：厂商自述｜**对应原则**：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [Q01](/handbook/12-quality-cicd#q01)

### 阿里 · AL24 · 蚂蚁全链路 AI 研发：SDD 规范驱动与 Harness 工程实践（AICon 上海 2026） {#al24}
**作者/机构**：InfoQ（蚂蚁智能研发产品专家的 AICon 议题介绍）｜**日期**：2026-06-16｜[原文](https://www.infoq.cn/article/5Ke1HD7F6R7aYr4jERyk)

蚂蚁把痛点归纳为两个“追不上”：文档追不上代码（需求与实现两张皮）、验证追不上迭代（流水线后置）。方案是 SDD 四步规范驱动 + 知识库 + 一站式研发，从“写代码”变成“提需求”。

> “验证追不上迭代：流水线后置发现问题，返工成本高”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [Q03](/handbook/12-quality-cicd#q03)

### 字节 · BD15 · AgentKit：从编码提效到组织效能跃迁（AICon 北京 2026） {#bd15}
**作者/机构**：朱杰（火山引擎技术专家，AgentKit 核心研发）｜**日期**：2026-12（议题预告）｜[原文](https://aicon.infoq.cn/2026/beijing/presentation/7416)

火山引擎的端到端交付方案：Spec 作为人与 Agent 的任务合约（目标、边界、依赖、验收标准），定义任务如何委托、结果如何验收、异常如何转交人工；用交付周期、一次通过率、人工介入率和缺陷四个结果指标决定自治等级是否上调。

> “最后给出以交付周期、一次通过率、人工介入率和缺陷为依据，逐步提升自治等级的落地方法。”

**证据类型**：议题摘要（演讲者自述，尚未开讲）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [P01](/compare/evidence#p01) [P16](/compare/evidence#p16)

## 团队采纳、度量与组织效能 {#team-metrics}

### 腾讯 · TX10 · 腾讯研发模式被 AI 重塑：需求吞吐率成为 AI Coding 的核心指标 {#tx10}
**作者/机构**：第一财经（郑栩彤，采访汤道生、刘毅等）｜**日期**：2026-06-05｜[原文](https://www.yicai.com/news/103218044.html)

CodeBuddy/WorkBuddy 负责人刘毅：2022 年 AI 代码接受程度不到 30%，到 2025 年底大部分团队 90% 以上代码由 AI 生成，程序员同时开多个任务。指标从“生成率”转向“需求吞吐率”；挑战是 AI 幻觉把风险带到生产、人类专家被评审淹没，因此要“用 AI 发现 AI 代码的错误、用 AI 自动测试”。团队组织更扁平、上下文对全员透明。

> “现在，需求吞吐率成为了AI Coding的核心指标，代表组织的创新速度。”

**证据类型**：高管口述（媒体采访）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [Q06](/handbook/12-quality-cicd#q06) [P08](/compare/evidence#p08)

### 腾讯 · TX11 · 腾讯 AI 三年：代码 AI 率从 23% 到 90%，最大的坑不是技术 {#tx11}
**作者/机构**：CSDN（搜狐转载，采访刘毅）｜**日期**：2026-06-08｜[原文](https://www.sohu.com/a/1033866890_115128)

同一位负责人的另一篇访谈，补充了“踩过的坑”：Token 成本是第一关，需要精细化成本治理；2026 年行业强调 harness，即给 AI 更多约束和更快的校验迭代；引入 AI 评审时，生产代码的 AI 与评审代码的 AI 必须不同。最难的是组织：个人提效≠组织提效。

> “不能让同一个 AI 自己检查自己”

**证据类型**：高管口述（媒体采访）｜**对应原则**：[Q07](/handbook/12-quality-cicd#q07) [P17](/compare/evidence#p17) [Q12](/handbook/12-quality-cicd#q12)

### 腾讯 · TX12 · 腾讯健康：我们有 40% 的代码是 AI 写的 {#tx12}
**作者/机构**：CodeBuddy（腾讯云开发者社区专栏）｜**日期**：2024-11-20｜[原文](https://cloud.tencent.com/developer/article/2467438)

早期（补全时代）推广样本：先组建跨岗位“先锋小组”记录 Good/Badcase、双周会反馈，再全面推广；累计 600+ Badcase。用生成率、采纳率、活跃率等多维指标做运营，并发现命名不规范、缺注释、逻辑复杂、复制大块代码会降低 AI 效果。可与 2026 年的“需求吞吐率”口径对照，看指标如何演变。

> “团队通过对 AI 代码助手的使用数据统计分析后发现，代码补全采纳率与使用的熟练度呈正相关”

**证据类型**：团队自报｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [P03](/compare/evidence#p03)

### 腾讯 · TX23 · WorkBuddy 企业版与 AI Coding 的组织账：个人提效≠组织提效 {#tx23}
**作者/机构**：新浪财经（报道腾讯）｜**日期**：2026-06-09｜[原文](https://finance.sina.com.cn/jjxw/2026-06-09/doc-iniauvas6486062.shtml)

报道 WorkBuddy 企业版发布时引述的内部数据：初期 AI 生成代码接受度不足 30%，到 2025 年底 CodeBuddy 覆盖 90% 工程师、多数团队超 90% 代码由 AI 生成、编码时间缩短 40%。负责人把“需求从立项到上线的流转效率”作为是否真正赋能组织的判据。

> “刘毅强调，单纯的个人效率提升没有意义，只有需求从立项到上线的流转效率提升，才代表AI真正赋能组织。”

**证据类型**：高管口述（媒体报道）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12)

### 阿里 · AL01 · 从 Copilot 到 Agent：阿里在 AI Coding 上的应用和挑战 {#al01}
**作者/机构**：InfoQ（整理向邦宇 QCon 北京 2025 分享）｜**日期**：2025-06-30｜[原文](https://www.infoq.cn/article/5X7q545Ua4GYJOQ7g9lt)

阿里集团研发平台的“全量”视角：内部 AI Coding 插件日活约 1.2 万、渗透率约 65%，补全采纳率约 28%（IDEA 约 33%），约 20% 的 CR 问题由 AI 发现；随后把重点从补全转到“模型驱动、少编排”的通用 Agent（Aone Agent），在容器里异步执行任务。这是少见的同时公开渗透率与采纳率“天花板”的数据。

> “在 Code Review 方面，目前大约 20% 的代码审查问题是由 AI 生成的。”

**证据类型**：团队自报（会议整理稿）｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q12](/handbook/12-quality-cicd#q12) [P11](/compare/evidence#p11)

### 阿里 · AL03 · 阿里云内部 AI 辅助代码生成比例近 40%；员工可自由选择工具 {#al03}
**作者/机构**：第一财经（陈杨园，采访通义灵码负责人神秀）｜**日期**：2025-05-30｜[原文](https://www.yicai.com/news/102643443.html)

2025 年中阿里云的公开口径：通义灵码内部覆盖率很高，AI 辅助代码生成比例接近 40%、半年提升约 50%；同时强调内部对 AI 编程工具持开放态度——只要注意数据安全合规，员工可自由选择工具（同文提到字节将禁用第三方工具的传闻，字节未回应）。

> “内部最新的AI辅助代码生成的比例已接近40%，较半年前提升50%左右。”

**证据类型**：团队自报（媒体采访）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12)

### 阿里 · AL04 · 通义灵码获员工工号 AI001：“未来 20% 的代码将由通义灵码编写” {#al04}
**作者/机构**：中国金融信息网（报道阿里云）｜**日期**：2024-04-02｜[原文](https://www.cnfin.com/gs-lb/detail/20240402/4030999_1.html)

2024 年阿里云给 AI 编程工具分配正式工号、公开 20% 代码目标，并强调“程序员仍是研发核心”。可作为时间轴起点：对比 2025 年约 40%、2026 年部分团队 80%–90% 的自报数据。

> “阿里云还专门给通义灵码分配了一个正式的员工工号——AI001。”

**证据类型**：团队自报（媒体报道）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [P16](/compare/evidence#p16)

### 阿里 · AL07 · 代码生成越来越快，软件交付真正的瓶颈转向了哪里？（云栖大会 AI Native 研发论坛） {#al07}
**作者/机构**：机器之心（凤凰网转载；许晓斌、黄挺等发言）｜**日期**：2026-09-24｜[原文](https://feng.ifeng.com/c/8wgLzD4BqNX)｜[相关链接](https://qcon.infoq.cn/2026/shanghai/presentation/7347)

阿里研发基础设施负责人许晓斌：在阿里编码通常只占软件交付总时长的 20%–30%；极端链路里编码约 1 小时，但从需求进入到交付仍约 21 天，时间耗在影响分析、环境准备、联调、审批、灰度与封网。因此投入转向运行与验证环境：OpenSandbox 内部周创建量超千万，另一套环境体系可完整复原约两三千个应用。同场蚂蚁黄挺介绍沙箱底座。

> “阿里开源的 OpenSandbox，在内部每周创建量已经超过千万级，服务于 Agent 运行、训练和评测。”

**证据类型**：团队自报（论坛报道）｜**对应原则**：[P15](/compare/evidence#p15) [Q09](/handbook/12-quality-cicd#q09) [Q12](/handbook/12-quality-cicd#q12)

### 阿里 · AL18 · 从辅助编码到 Agent 主导交付：淘宝 AI 原生研发系统（AICon 北京 2026 Keynote） {#al18}
**作者/机构**：吕承飞（吕行，淘天集团 AI 研发负责人）｜**日期**：2026-12（议题预告）｜[原文](https://aicon.infoq.cn/2026/beijing/presentation/7477)

淘宝的问题定义很直白：局部生码提速，但全局交付不提效。议题讲从半托管到全托管的 Agent 交付系统，需求、开发、测试、发布全链路。

> “破局“局部生码提速、全局交付不提效””

**证据类型**：议题摘要（演讲者自述，尚未开讲）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [P16](/compare/evidence#p16)

### 阿里 · AL19 · 从 AI 编码助手到需求托管交付 Agent：菜鸟 AI 研发效能实践（AICon 上海 2026） {#al19}
**作者/机构**：郭凤钊（菜鸟网络研发总监）｜**日期**：2026-06（AICon 上海）｜[原文](https://aicon.infoq.cn/2026/shanghai/presentation/7062)

菜鸟把规范、经验沉淀为 Playbook，让“硅基程序员”托管需求交付；自报 AI 代码贡献率大幅提升。属于高比例自报数据，未见交付周期或缺陷率的同口径披露。

> “AI代码贡献率从 10% 提升至 80%+，部分团队接近100%”

**证据类型**：议题摘要（团队自报，尚未独立验证）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [P13](/compare/evidence#p13)

### 阿里 · AL25 · 蚂蚁数科企业级 AGI 研发体系重塑（AICon 上海 2026） {#al25}
**作者/机构**：刘秀婷（蚂蚁数科 PMO & AI 研发效能负责人）｜**日期**：2026-06（AICon 上海）｜[原文](https://aicon.infoq.cn/2026/shanghai/presentation/7122)

组织层做法：AGI 研发指数、L1–L5 分级与“苏格拉底式”质量追问，把人从环内（in the loop）挪到环上（on the loop）。与 CN03（蚂蚁数科 Harness）同源不同侧面。

> “Agent In The Loop, Human On The Loop”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[P16](/compare/evidence#p16) [P08](/compare/evidence#p08) [Q12](/handbook/12-quality-cicd#q12)

### 阿里 · AL26 · 蚂蚁生产级软件交付基建和实践（AICon 深圳 2026） {#al26}
**作者/机构**：刘仁权（弈阁，蚂蚁集团 CIO 总架构师、Agentic Delivery 团队）｜**日期**：2026（AICon 深圳）｜[原文](https://aicon.infoq.cn/2026/shenzhen/presentation/7226)

蚂蚁的交付基建：在 AI 生成占比极高的前提下，如何让交付 7×24 可持续，靠的是基建（环境、验证、发布）而非更多生成。

> “在蚂蚁很多团队 AI 生成代码占比已经达到 90% 以上”

**证据类型**：议题摘要（团队自报，尚未独立验证）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [Q03](/handbook/12-quality-cicd#q03)

### 字节 · BD02 · TRAE CN 企业版发布：字节超 92% 工程师使用 TRAE {#bd02}
**作者/机构**：火山引擎开发者社区（TRAE 官方发布稿）｜**日期**：2025-12-18｜[原文](https://developer.volcengine.com/articles/7587308091345698822)

企业版发布稿里的内部数据：字节超过 92% 工程师用 TRAE，能力在内部 50 余项业务验证；抖音生活服务 AI 代码贡献率超 43%、测试用例生成每周节省 44.56 人/天、无人发布单次节省 25 分钟。属厂商发布稿，适合作“规模”而非“效果”证据。

> “在字节跳动，超过 92%的工程师都在使用 TRAE 辅助开发。”

**证据类型**：厂商自述（团队自报）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12)

## 工具、工作流与平台 {#tools-workflow}

### 腾讯 · TX02 · 从 Vibe Coding 到 AI 原生研发团队：一套能落地的工程实践（Vibe Flowing） {#tx02}
**作者/机构**：腾讯技术工程（masoncai，海外网络运营平台团队）｜**日期**：2026-07-21｜[原文](https://news.qq.com/rain/a/20260721A09ALQ00)

一个“所有组件都由 AI 维护”的内部运营平台：monorepo 让 AI 一次看到前后端；AGENTS.md 集中写分层规则（只能向下调用）、文件红线和检查命令；提交前必须过 ruff/ty、oxlint/vue-tsc；Playwright 截图做 AI 自测，最终由提需求的运营同事验收，MR 仍需管理员审批合并。对 TDD 的取舍很务实：AI 易写“自欺欺人”的测试，所以用规则兜底，而不追求严格先写测试。

> “覆盖率目标定在 70%，作为参考值不阻断。”

**证据类型**：团队自报｜**对应原则**：[P03](/compare/evidence#p03) [P04](/compare/evidence#p04) [P05](/compare/evidence#p05) [P06](/compare/evidence#p06) [Q02](/handbook/12-quality-cicd#q02) [Q05](/handbook/12-quality-cicd#q05)

### 腾讯 · TX04 · 从 Vibe Coding 到 Agentic Engineering：重构后台开发全流程 {#tx04}
**作者/机构**：腾讯技术工程（seanguo，网易号转载）｜**日期**：2026-04-17｜[原文](https://www.163.com/dy/article/KQO1VBLM0518R7MO.html)

一线后台工程师用 Claude Code + 自定义 Skill/Command/MCP，把 PM、代码平台、DevOps、日志平台串进一个终端会话：人定义目标、约束和质量标准，AI 在结构化流程里执行，关键节点人工审核。两条教训：自定义 Skill 的价值是编排串联而非从零实现；AI 生成的 MR 审查意见必须逐条人工判断。

> “所以 reviewer 拿到 AI 的审查结果后，每一条都要过脑子判断，该采纳的采纳，不靠谱的直接丢掉。”

**证据类型**：个人实践（腾讯工程师）｜**对应原则**：[P13](/compare/evidence#p13) [P14](/compare/evidence#p14) [P08](/compare/evidence#p08) [Q06](/handbook/12-quality-cicd#q06)

### 腾讯 · TX13 · 腾讯 CodeBuddy IDE 如何成为一个“全栈高级工程师”？ {#tx13}
**作者/机构**：AI 前线（褚杏娟，采访腾讯 CodeBuddy 团队）｜**日期**：2025-07-29｜[原文](https://news.qq.com/rain/a/20250729A05FAH00)

产品立项依据来自内部调研：程序员大部分时间花在沟通对齐而非 IDE 里；因此 CodeBuddy 想覆盖“需求拆解—架构设计—UI—前后端—测试部署”全链路，并内置 200+ 场景知识库生成结构化需求文档再交给 Code Agent。报道同时给出“43% 代码由 AI 生成、千行 bug 率降 31.5%”的内部口径。

> “腾讯内部调研发现，一个程序员只有 37% 的时间在真正使用 IDE 做开发”

**证据类型**：团队自报（媒体采访）｜**对应原则**：[P01](/compare/evidence#p01) [Q12](/handbook/12-quality-cicd#q12)

### 阿里 · AL02 · Vibe Coding 在代码生成与协作中的实践与思考（Aone Agent） {#al02}
**作者/机构**：InfoQ（整理向邦宇 QCon 上海 2025 分享，腾讯新闻转载）｜**日期**：2026-02-10｜[原文](https://news.qq.com/rain/a/20260210A03Q4Y00)

续篇：Aone Agent 是“以外部容器发起的异步任务工具”，用户用自然语言发起任务，容器里的 Agent 自行调用搜索、读文件、Shell 等工具。意外发现：用户从后端扩展到测试、前端、算法、产品、运营、设计和运维，任务也从改代码扩展到代码分析、单测等。体现“隔离容器 + 异步委派”的工程形态。

> “另一个我主导的项目是 Aone Agent 。这是一个以外部容器发起的异步任务工具。”

**证据类型**：团队自述（会议整理稿）｜**对应原则**：[P11](/compare/evidence#p11) [P15](/compare/evidence#p15)

### 阿里 · AL13 · Qwen Code 1.0 Preview：Qoder 与 Qwen Code 的 Agent 能力合流 {#al13}
**作者/机构**：QwenLM（GitHub Release）｜**日期**：2026-11-11｜[原文](https://github.com/QwenLM/qwen-code/releases/tag/v1.0.0-preview)｜[相关链接](https://github.com/QwenLM/qwen-code-action)

阿里两条 Coding Agent 产品线（Qwen Code 开源 CLI 与 Qoder）在 1.0 预览版中合流，支持多模型提供商、会话恢复与非交互执行；同组织还有把 Qwen Code 接入 GitHub 的 qwen-code-action（PR 评审、issue 分诊）。

> “Brings together the agent capabilities of Qoder and Qwen Code for code understanding, implementation, debugging, and testing.”

**证据类型**：官方发布说明｜**对应原则**：[P14](/compare/evidence#p14) [Q03](/handbook/12-quality-cicd#q03)

### 阿里 · AL16 · 对话叔同：Qoder 上线 60 天 {#al16}
**作者/机构**：十字路口 Crossing（Qoder 博客园转载）｜**日期**：2025-10-31｜[原文](https://www.cnblogs.com/qoder/p/19180020)

Qoder 创始人访谈：阿里为何要做面向全球的 Agentic 编码平台，以及产品设计取舍。用户量为团队自报，可与 AL13（Qoder 与 Qwen Code 合流）对照看产品线演进。

> “上线 5 天用户迅速突破 10 万，仅 60 天斩获 50 万开发者用户”

**证据类型**：团队自报（播客访谈）｜**对应原则**：[P18](/compare/evidence#p18)

### 阿里 · AL30 · LoongSuite Pilot：本地 Coding Agent 遥测采集 {#al30}
**作者/机构**：阿里巴巴（GitHub 开源）｜**日期**：2026｜[原文](https://github.com/alibaba/loongsuite-pilot)

把“Agent 用得怎么样”变成可观测数据：自动发现本机 Claude Code/Qwen Code 等 Agent，统一事件模式采集模型、会话、轮次、工具调用与 token，并在导出前控制敏感 prompt 与密钥。是度量 Agent 成本与行为的基础设施。

> “Which agents are being used? What model, session, turn, and tool activity happened?”

**证据类型**：开源仓库 README（团队自述）｜**对应原则**：[P17](/compare/evidence#p17) [Q12](/handbook/12-quality-cicd#q12)

### 字节 · BD11 · Agentic Edit：Trae 在代码编辑上的落地与进化 {#bd11}
**作者/机构**：冯绪（Trae 团队），InfoQ/AICon｜**日期**：2025-12-04｜[原文](https://www.infoq.cn/article/ep5bs0fmyalbanwhohoe)

一个具体的工程取舍：代码修改用 Apply（二次模型调用重写文件）还是 Search/Replace。Apply 体验好但长文件差、误差叠加；Search/Replace 不受文件长度限制、更准。按模式选择：Chat 用 Apply，Builder（Agent）用 Search/Replace。

> “基于上述判断，我们在这一阶段转向了 Search/Replace 方案。”

**证据类型**：团队自述（会议整理稿）｜**对应原则**：[P14](/compare/evidence#p14) [P09](/compare/evidence#p09)

