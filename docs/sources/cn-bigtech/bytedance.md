# 国内大厂专题 · 字节

> 含 TRAE/豆包 MarsCode、BitsAI、字节质量效能/质量保障团队、Seed、火山引擎、飞书 CodeM 等。每条都有摘要、逐字核对过的原文引文（英文保留原文）和链接。**所有数字均为团队或厂商自报、尚未独立验证**；会议条目只有议题摘要（演讲者自述），标「尚未开讲」的是 2026-12 AICon 北京的预告。检索与核对时间：2026-11 中旬（北京时间）。原则编号 P01–P20 见 [共识度/佐证](/compare/evidence)，Q01–Q13 见 [第 12 章](/handbook/12-quality-cicd#principles)。横向比较见 [国内大厂对比](/compare/cn-bigtech)。

| 编号 | 标题 | 类型 | 证据 |
| --- | --- | --- | --- |
| [BD01](#bd01) | 洪定坤：AI Coding 的实践与探索（火山引擎 FORCE 大会） | 演讲实录 | 高管演讲（团队自报，尚未独立验证） |
| [BD02](#bd02) | TRAE CN 企业版发布：字节超 92% 工程师使用 TRAE | 媒体报道 | 厂商自述（团队自报） |
| [BD03](#bd03) | BitsAI-Fix：字节用 LLM 自动修复 Lint 问题的工业实践 | 论文 | 论文（工业部署，团队自报） |
| [BD04](#bd04) | LogSage：LLM 驱动的 CI/CD 失败检测与修复（ASE 2025） | 论文 | 论文（工业部署，团队自报） |
| [BD05](#bd05) | Trae Agent：测试时扩展的软件工程 Agent（SWE-bench Verified 第一） | 论文 | 论文（基准成绩，团队自报） |
| [BD06](#bd06) | AEGIS：基于 Agent 的通用 Bug 复现脚本生成（FSE 2025） | 论文 | 论文 |
| [BD07](#bd07) | TestGPT-Server：在字节用 LLM 自动测试微服务（FSE 2025 工业论文） | 论文 | 论文（工业部署，团队自报） |
| [BD08](#bd08) | Multi-SWE-bench：多语言 issue 修复基准 | 论文 | 论文（开源基准） |
| [BD09](#bd09) | AI 驱动的智能化单元测试生成：字节跳动的实践与创新 | 团队文章 | 团队自述（会议整理稿） |
| [BD10](#bd10) | 让 QA 真正用起来：测试用例生成 Agent（NL2Test）落地 | 团队文章 | 团队自报（公众号原文摘录 + 论文） |
| [BD11](#bd11) | Agentic Edit：Trae 在代码编辑上的落地与进化 | 团队文章 | 团队自述（会议整理稿） |
| [BD12](#bd12) | 当代码遇上大模型：智能编程助手的架构设计与工程实践 | 团队文章 | 团队自述（会议整理稿） |
| [BD13](#bd13) | 第一性原理拆解 Agentic Coding：从理论到实操（下） | 团队文章 | 团队自述（官方技术文章） |
| [BD14](#bd14) | TRAE 智能体审查（Agent-powered Code Review）文档 | 产品文档 | 产品文档 |
| [BD15](#bd15) | AgentKit：从编码提效到组织效能跃迁（AICon 北京 2026） | 会议议题 | 议题摘要（演讲者自述，尚未开讲） |
| [BD16](#bd16) | AgentOps 实战：字节复杂 Agent 的效果评测与迭代优化（QCon 上海 2025） | 会议议题 | 议题摘要（演讲者自述） |
| [BD17](#bd17) | 给 Agent 做“CT”：大规模 Agent 的可观测与质量保障（QCon 北京 2026） | 会议议题 | 议题摘要（演讲者自述） |
| [BD18](#bd18) | 飞书 CodeM 通过信通院“驾驭工程（Harness）能力成熟度”L4 评估 | 媒体报道 | 厂商自述（第三方评估结果，细节未公开） |
| [BD19](#bd19) | Trae IDE 遥测与隐私分析：关闭遥测后仍持续上报 | 开源仓库 | 第三方独立分析（单一研究者） |
| [BD20](#bd20) | Repo2Run：大规模自动构建代码仓库可执行环境（NeurIPS 2025） | 开源仓库 | 开源仓库（论文配套） |

### BD01 · 洪定坤：AI Coding 的实践与探索（火山引擎 FORCE 大会） {#bd01}
**作者/机构**：洪定坤（字节跳动技术副总裁），火山引擎公众号｜**日期**：2026-06-23｜[原文](https://mp.weixin.qq.com/s/mdmaAyUIvxE8WT_GEbF2wQ)｜[相关链接](https://cloud.tencent.com/developer/article/2700072)

字节最完整的一手口径：一年内 AI 代码贡献率增长 6 倍多、AI Coding token 消耗增长 5 倍、AI 代码合入率增长超 2 倍；TRAE 团队过去半年 90% 以上代码由 AI 写，但人均需求吞吐率只提升 60%（到 1.6 倍）。他明确反对把贡献率当 KPI，并用“3 模型 × 3 框架、同一 Prompt”实验说明：功能正确率约 80%，但“可交付性”只有 40–60 分；接入 Harness 基建后正确率接近 90%、可交付性升到约 80 分。

> “单一的代码贡献率，其实很难完全衡量我们实际效率的提升，它会失真。”

**证据类型**：高管演讲（团队自报，尚未独立验证）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [P06](/compare/evidence#p06) [P04](/compare/evidence#p04) [Q05](/handbook/12-quality-cicd#q05)

### BD02 · TRAE CN 企业版发布：字节超 92% 工程师使用 TRAE {#bd02}
**作者/机构**：火山引擎开发者社区（TRAE 官方发布稿）｜**日期**：2025-12-18｜[原文](https://developer.volcengine.com/articles/7587308091345698822)

企业版发布稿里的内部数据：字节超过 92% 工程师用 TRAE，能力在内部 50 余项业务验证；抖音生活服务 AI 代码贡献率超 43%、测试用例生成每周节省 44.56 人/天、无人发布单次节省 25 分钟。属厂商发布稿，适合作“规模”而非“效果”证据。

> “在字节跳动，超过 92%的工程师都在使用 TRAE 辅助开发。”

**证据类型**：厂商自述（团队自报）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12)

### BD03 · BitsAI-Fix：字节用 LLM 自动修复 Lint 问题的工业实践 {#bd03}
**作者/机构**：Yuanpeng Li 等（字节跳动，arXiv）｜**日期**：2025-08｜[原文](https://arxiv.org/abs/2508.03487)

把静态分析告警的修复交给 LLM：冷启动阶段自动获取可验证训练数据，上线后用线上反馈持续迭代；奖励函数同时看格式与正确性，并惩罚冗余修改；用“code diff 匹配”持续追踪线上真实效果。与 QC09（BitsAI-CR）同属字节 BitsAI 体系。

> “In production deployment at ByteDance, our solution has supported over 5,000 engineers, resolved more than 12,000 static analysis issues, achieved approximately 85% remediation accuracy, with around 1,000 weekly active adopters.”

**证据类型**：论文（工业部署，团队自报）｜**对应原则**：[Q03](/handbook/12-quality-cicd#q03) [Q12](/handbook/12-quality-cicd#q12) [P19](/compare/evidence#p19)

### BD04 · LogSage：LLM 驱动的 CI/CD 失败检测与修复（ASE 2025） {#bd04}
**作者/机构**：Weiyuan Xu 等（字节跳动，arXiv）｜**日期**：2025-06｜[原文](https://arxiv.org/abs/2506.03691)

CI/CD 失败日志的根因分析与修复建议：用 LLM 做根因分析，再用 RAG 复用历史修复、通过工具调用执行自动修复。字节内部一年部署，处理超过 107 万次执行，端到端精度超 80%。是“AI 进流水线”而不是“AI 进 IDE”的样本。

> “In a year-long industrial deployment at ByteDance, it processed over 1.07M executions”

**证据类型**：论文（工业部署，团队自报）｜**对应原则**：[Q03](/handbook/12-quality-cicd#q03) [Q10](/handbook/12-quality-cicd#q10)

### BD05 · Trae Agent：测试时扩展的软件工程 Agent（SWE-bench Verified 第一） {#bd05}
**作者/机构**：Trae Research Team（字节跳动，arXiv）｜**日期**：2025-07｜[原文](https://arxiv.org/abs/2507.23370)｜[相关链接](https://github.com/bytedance/trae-agent)

把 issue 修复当作“最优解搜索”：生成多个候选补丁，再由剪枝与选择 Agent 收敛，解决集成空间大与仓库级理解两大难题；开源为 bytedance/trae-agent。注意 75.20% 是排行榜成绩，不代表内部业务交付质量。

> “Trae Agent has achieved first place on the SWE-bench Verified leaderboard, with a notable Pass@1 score of 75.20%.”

**证据类型**：论文（基准成绩，团队自报）｜**对应原则**：[P10](/compare/evidence#p10) [Q07](/handbook/12-quality-cicd#q07) [Q08](/handbook/12-quality-cicd#q08)

### BD06 · AEGIS：基于 Agent 的通用 Bug 复现脚本生成（FSE 2025） {#bd06}
**作者/机构**：Xinchen Wang 等（字节跳动 Trae 团队与高校，arXiv）｜**日期**：2024-11｜[原文](https://arxiv.org/abs/2411.18015)

先复现再修：从 issue 描述自动生成能复现 bug 的脚本，用“精简上下文构建”和“有限状态机约束的多反馈优化”约束 Agent 行为，避免长上下文和无序动作。是测试先行（先有失败用例）在 Agent 场景的工程化。

> “we propose an Automated gEneral buG reproductIon Scripts generation framework, named AEGIS, which is the first agent-based framework for the task.”

**证据类型**：论文｜**对应原则**：[Q01](/handbook/12-quality-cicd#q01) [P07](/compare/evidence#p07) [P04](/compare/evidence#p04)

### BD07 · TestGPT-Server：在字节用 LLM 自动测试微服务（FSE 2025 工业论文） {#bd07}
**作者/机构**：Jue Wang 等（字节跳动）｜**日期**：2025-06｜[原文](https://conf.researchr.org/details/fse-2025/fse-2025-industry-papers/17/TestGPT-Server-Automatically-Testing-Microservices-with-Large-Language-Models-at-Byt)

LLM 生成测试请求，LLM 辅助的响应分析器识别崩溃，断言挖掘器自动提取功能断言。在 14,366 个微服务 API 上发现 50 个崩溃 bug 和 2 个功能 bug——功能 bug 数量之少本身说明“自动断言”仍是难点。（ACM 全文页 403，这里引用会议页摘要）

> “identifying 50 crash bugs and 2 functional bugs across 14,366 microservice APIs, with minimal manual effort”

**证据类型**：论文（工业部署，团队自报）｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05) [Q02](/handbook/12-quality-cicd#q02)

### BD08 · Multi-SWE-bench：多语言 issue 修复基准 {#bd08}
**作者/机构**：Daoguang Zan 等（字节跳动 Seed，arXiv）｜**日期**：2025-04｜[原文](https://arxiv.org/abs/2504.02605)

把 SWE-bench 扩展到 Java、TS、JS、Go、Rust、C、C++，并重视人工标注质量；同时开放 RL 训练用实例社区。是字节在“评测基础设施”上的公共贡献。

> “It includes a total of 1,632 high-quality instances, which were carefully annotated from 2,456 candidates by 68 expert annotators”

**证据类型**：论文（开源基准）｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08)

### BD09 · AI 驱动的智能化单元测试生成：字节跳动的实践与创新 {#bd09}
**作者/机构**：InfoQ（整理字节质量效能专家赵亮 QCon 上海分享）｜**日期**：2024-12-27｜[原文](https://www.infoq.cn/article/8mVuhrLMMEJ8MDjo1U4e)

单测生成不是“让模型写测试”就完事：用真实业务流量采集保证用例真实性，结合深度程序分析与路径提升提高覆盖率，再用断言工程、语法修正与效果度量保证可靠性；覆盖存量与增量两类场景。

> “通过真实业务流量采集、单测框架能力和路径提升技术，有效解决单元测试的用例真实性和覆盖率问题”

**证据类型**：团队自述（会议整理稿）｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05) [Q01](/handbook/12-quality-cicd#q01)

### BD10 · 让 QA 真正用起来：测试用例生成 Agent（NL2Test）落地 {#bd10}
**作者/机构**：字节跳动质量保障团队（字节跳动技术团队公众号，摘录页）｜**日期**：2026-09-08｜[原文](https://www.lddgo.net/article/detail/5eqa)｜[相关链接](https://arxiv.org/abs/2607.24000)

字节与复旦合作的 NL2Test：QA 用自然语言描述场景，Agent 生成可运行回归用例。取舍：只做边界清晰的“用例转译”，不替代 QA；能用程序解决的不用 LLM；用 schema 与允许集合约束输出；优先稳定断言。自报 85.4% 生成用例进入 CI/CD、平均约 25% 新增用例来自 Agent、每双周节省约 30 人天。配套论文（u2）将公司匿名为“一家大型面向消费者的互联网公司”。

> “85.4% 的生成用例被集成到 CI/CD 工作流中”

**证据类型**：团队自报（公众号原文摘录 + 论文）｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05) [Q03](/handbook/12-quality-cicd#q03) [Q10](/handbook/12-quality-cicd#q10) [P04](/compare/evidence#p04)

### BD11 · Agentic Edit：Trae 在代码编辑上的落地与进化 {#bd11}
**作者/机构**：冯绪（Trae 团队），InfoQ/AICon｜**日期**：2025-12-04｜[原文](https://www.infoq.cn/article/ep5bs0fmyalbanwhohoe)

一个具体的工程取舍：代码修改用 Apply（二次模型调用重写文件）还是 Search/Replace。Apply 体验好但长文件差、误差叠加；Search/Replace 不受文件长度限制、更准。按模式选择：Chat 用 Apply，Builder（Agent）用 Search/Replace。

> “基于上述判断，我们在这一阶段转向了 Search/Replace 方案。”

**证据类型**：团队自述（会议整理稿）｜**对应原则**：[P14](/compare/evidence#p14) [P09](/compare/evidence#p09)

### BD12 · 当代码遇上大模型：智能编程助手的架构设计与工程实践 {#bd12}
**作者/机构**：InfoQ（整理豆包 MarsCode / Trae IDE 架构师段潇涵 QCon 北京分享）｜**日期**：2025-08-22｜[原文](https://www.infoq.cn/article/dshjgpfg5sgvahlilgtg)

MarsCode/Trae 的架构要点：Agent 把需求分解为步骤并在执行中自我反思修正；上下文侧实时构建代码知识图谱（结构与依赖），解决大仓库超出上下文的问题。可与腾讯 TX01 的三层图谱对照。

> “在上下文感知方面，构建代码知识图谱，实时构建代码的结构和依赖关系等，解决了大语言模型处理大型代码库时的上下文限制问题”

**证据类型**：团队自述（会议整理稿）｜**对应原则**：[P05](/compare/evidence#p05) [P18](/compare/evidence#p18)

### BD13 · 第一性原理拆解 Agentic Coding：从理论到实操（下） {#bd13}
**作者/机构**：小夏（TRAE 技术专家），火山引擎开发者社区｜**日期**：2026｜[原文](https://developer.volcengine.com/articles/7598410716190375962)

TRAE 团队给用户的最佳实践：短对话优于长对话，每个对话只做一件事；借助 git diff 等外部状态在对话间传递上下文；把 bug 修复、代码审查经验沉淀为项目知识库（“复利工程”）；清晰文档和快速测试既帮人也帮 AI。

> “保持对话简短、专注，每个对话只做一件事。”

**证据类型**：团队自述（官方技术文章）｜**对应原则**：[P18](/compare/evidence#p18) [P19](/compare/evidence#p19) [P10](/compare/evidence#p10) [P17](/compare/evidence#p17)

### BD14 · TRAE 智能体审查（Agent-powered Code Review）文档 {#bd14}
**作者/机构**：TRAE 官方文档｜**日期**：2026｜[原文](https://docs.trae.cn/ide_agent-powered-code-review?lang=zh)

把评审放到提交前：可审查未提交变更、单次提交或分支差异，生成变更摘要与业务流程变更图；可开启“提交后自动审查”，问题条目一键唤起对话修复。是 IDE 内“写—审—修”闭环的产品形态，但仍是同一工具链内的自审，需与独立 CI 配合。

> “若你希望由 AI 自动审核变更内容，提供总结摘要并识别问题，可以开启自动审查功能。”

**证据类型**：产品文档｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [P08](/compare/evidence#p08)

### BD15 · AgentKit：从编码提效到组织效能跃迁（AICon 北京 2026） {#bd15}
**作者/机构**：朱杰（火山引擎技术专家，AgentKit 核心研发）｜**日期**：2026-12（议题预告）｜[原文](https://aicon.infoq.cn/2026/beijing/presentation/7416)

火山引擎的端到端交付方案：Spec 作为人与 Agent 的任务合约（目标、边界、依赖、验收标准），定义任务如何委托、结果如何验收、异常如何转交人工；用交付周期、一次通过率、人工介入率和缺陷四个结果指标决定自治等级是否上调。

> “最后给出以交付周期、一次通过率、人工介入率和缺陷为依据，逐步提升自治等级的落地方法。”

**证据类型**：议题摘要（演讲者自述，尚未开讲）｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [P01](/compare/evidence#p01) [P16](/compare/evidence#p16)

### BD16 · AgentOps 实战：字节复杂 Agent 的效果评测与迭代优化（QCon 上海 2025） {#bd16}
**作者/机构**：史海量（字节 AI Platform，扣子罗盘效果评测后端负责人）｜**日期**：2025-10（QCon 上海）｜[原文](https://qcon.infoq.cn/2025/shanghai/presentation/6729)｜[相关链接](https://www.infoq.cn/article/vxtijzrrenh3lwxnlpxc)

Agent 应用的效果评测体系：评测集构建、指标体系设计、持续集成与线上监测全链路，应对任务定义模糊、结果不确定、线上波动。与 2025 QCon 北京杨晨的 AgentOps 议题同属扣子罗盘线。

> “系统解析从评测集构建、指标体系设计、到持续集成与线上监测的全链路实践方法”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08) [Q10](/handbook/12-quality-cicd#q10)

### BD17 · 给 Agent 做“CT”：大规模 Agent 的可观测与质量保障（QCon 北京 2026） {#bd17}
**作者/机构**：钱世俊（字节跳动火山引擎应用观测技术负责人）｜**日期**：2026-04（QCon 北京）｜[原文](https://qcon.infoq.cn/2026/beijing/presentation/6927)

从端到端 Trace（终端→AI 网关→Agent→工具）到根因定位，并把观测数据回流到离线/在线评测与轨迹评测，驱动持续改进与成本优化。

> “观测数据的回流与离线/在线评测、Agent 轨迹评测相结合，驱动了 Agent 的持续改进与成本优化”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08) [P17](/compare/evidence#p17)

### BD18 · 飞书 CodeM 通过信通院“驾驭工程（Harness）能力成熟度”L4 评估 {#bd18}
**作者/机构**：飞书项目官方新闻｜**日期**：2026-10-15｜[原文](https://project.feishu.cn/home/news/feishu-codem-ccna-l4-harness-engineering)

Harness Engineering 在国内开始出现行业标准化评估：信通院《智能原生软件工程驾驭工程能力成熟度》覆盖连接、编排、循环、效能、安全、评估优化六个维度。属厂商新闻，评估细节未公开。

> “该认证覆盖连接、编排、循环、效能、安全、评估优化六大核心能力维度”

**证据类型**：厂商自述（第三方评估结果，细节未公开）｜**对应原则**：[P04](/compare/evidence#p04) [P15](/compare/evidence#p15)

### BD19 · Trae IDE 遥测与隐私分析：关闭遥测后仍持续上报 {#bd19}
**作者/机构**：segmentationf4u1t（独立研究者，GitHub）｜**日期**：2025-07｜[原文](https://github.com/segmentationf4u1t/trae_telemetry_research)｜[相关链接](https://news.ycombinator.com/item?id=44703164)

独立研究者抓包分析：即使开启遥测退出（opt-out），Trae 仍上报系统信息、多种设备标识与使用数据；在 HN 获 954 分讨论。对“用国内大厂工具处理私有代码”的团队，是需要单独评估的数据边界问题（官方回应未在本次检索中核到）。

> “Trae continues to transmit a broad set of data even with telemetry opt-out enabled”

**证据类型**：第三方独立分析（单一研究者）｜**对应原则**：[P15](/compare/evidence#p15) [Q13](/handbook/12-quality-cicd#q13)

### BD20 · Repo2Run：大规模自动构建代码仓库可执行环境（NeurIPS 2025） {#bd20}
**作者/机构**：字节跳动（GitHub 开源）｜**日期**：2025｜[原文](https://github.com/bytedance/Repo2Run)

Agent 能不能验证，取决于仓库能不能跑起来：LLM Agent 在 Docker 沙箱里自动配置环境、为 Python 仓库生成无错的 Dockerfile。是 SWE 训练与评测（Multi-SWE-bench 等）背后的环境基建。

> “Repo2Run: Automated Building Executable Environment for Code Repository at Scale”

**证据类型**：开源仓库（论文配套）｜**对应原则**：[Q09](/handbook/12-quality-cicd#q09) [P15](/compare/evidence#p15)
