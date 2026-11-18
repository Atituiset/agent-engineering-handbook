# X 精选 · 约束与架构

> 6 条精选帖子，按发帖日期（UTC）排序。每条都有原帖链接；摘要忠于原文，引文为原帖逐字摘录。**作者自述**为个人经验，厂商员工谈自家产品时请视为**厂商自报**。原则标签为关键词自动归类，见 [共识度/佐证](/compare/evidence)。

[[toc]]

### XK-001 · gritql + husky 胜过 agents.md：在提交时用 linter 强制架构模式 {#xk-001}
**作者**：Saoud Rizwan（@sdrzn）｜**日期**：2026-01-31｜[原帖](https://x.com/sdrzn/status/2017732893024653682)｜♥ 205

Cline 创始人 Saoud Rizwan 认为模型无法读完整个代码库来理解架构模式，但可以在提交时用 linter 强制执行，而不是浪费 token 去填充「非确定性」的规则文件；他们用 husky pre-commit hook 运行自定义 linter。这是「约束可执行化」的直接例证。

> "you CAN enforce this at commit time with linters instead of wasting tokens filling up non-deterministic rules files"

原则：[P04](/compare/evidence#p04) [P05](/compare/evidence#p05) [P12](/compare/evidence#p12)

### XK-002 · Uncle Bob：我可能在过度约束智能体 {#xk-002}
**作者**：Uncle Bob Martin（@unclebobmartin）｜**日期**：2026-09-07｜[原帖](https://x.com/unclebobmartin/status/2096994914185662851)｜♥ 2263

Robert C. Martin 说几个月来他一直在验证一个假设：智能体需要由确定性工具组成的 harness 来约束，强制遵循严格流程（Gherkin、代码、单元测试、CRAP、变异测试等）；但模型在此期间进步巨大，他开始认为自己在过度约束它们，甚至是大幅过度约束。

> "I'm starting to think that I'm over constraining them."

原则：[P06](/compare/evidence#p06) [P12](/compare/evidence#p12)

### XK-003 · Uncle Bob：我花几周搭 harness，模型进步让它变得多余 {#xk-003}
**作者**：Uncle Bob Martin（@unclebobmartin）｜**日期**：2026-09-11｜[原帖](https://x.com/unclebobmartin/status/2098432570887217520)｜♥ 3265

Robert C. Martin 说他花了几周搭建一个严格约束智能体的 harness（各种关卡、测试、工具、协议），但在此期间智能体进步很大，他的 harness 几乎不再需要。他强调并未放弃约束和工具：单元测试、CRAP 指标和变异测试仍能发现 bug；现在给智能体一个重大任务加少量指导，40 分钟后回来，覆盖率高、变异测试完成、架构干净。他开始认为 harness 不应把智能体当成软件设计中的组件。作者自述，是对「重型 harness」的重要反思。

> "I have not given up on constraints and tooling.  Unit testing is still important."

原则：[P05](/compare/evidence#p05) [P06](/compare/evidence#p06) [P17](/compare/evidence#p17)

### XK-004 · 最大的设计失误：同步数据库访问在 50 个并行会话下成了瓶颈 {#xk-004}
**作者**：Peter Steinberger（@steipete）｜**日期**：2026-09-26｜[原帖](https://x.com/steipete/status/2103648679169257737)｜♥ 2331

Peter Steinberger 说他把项目迁到 sqlite 时最大的设计失误是采用同步数据库访问：一个智能体只向你汇报时没问题，但当一个智能体可能并行跑 50 个会话、整个团队都在用时就成了限制。他用 /goal 让智能体落地了 575 个 PR 迁移到异步 worker。作者自述。

> "The biggest design mistake I made when we moved OC to sqlite: using sync db access."

原则：[P08](/compare/evidence#p08) [P11](/compare/evidence#p11)

### XK-005 · 每纠正一次，就写成一条 lint 规则，而不是往 agents.md 里加话 {#xk-005}
**作者**：宝玉（@dotey）｜**日期**：2026-11-15｜[原帖](https://x.com/dotey/status/2121835140850602200)｜♥ 1191

宝玉整理 Lauren Tan 在 AI Engineer 大会演讲《All Code Is Slop (Except Mine)》的要点：每纠正 AI 一次，就把这次纠正写成 lint 这类自动检查规则，少往 agents.md 等说明文档里加话；违反 lint 的代码会直接报错、提交不上去，而文档里的话 AI 不一定照做。

> "每纠正 AI 一次，就把这次纠正写成 lint 这类自动检查规则，少往 agents.md 这类说明文档里加话。"

原则：[P03](/compare/evidence#p03) [P04](/compare/evidence#p04) [P16](/compare/evidence#p16)

### XK-006 · 「黑盒编程」：把精力放在需求、架构约束和验收标准上 {#xk-006}
**作者**：Barret李靖（@Barret_China）｜**日期**：2026-11-18｜[原帖](https://x.com/Barret_China/status/2123058891869098232)｜♥ 305

Barret李靖 说团队有不少高并发系统用 Rust 编写，但精通 Rust 的人不多，仍敢让 AI 开发，原因是把更多精力放在需求、架构约束和验收标准上：性能与稳定性水位、必须遵守的安全规范、必须通过的测试都提前定义清楚；具体实现交给 AI，但复杂系统的架构仍需关注。

> "因为我们开始把更多精力放在需求、架构约束和验收标准上。"

原则：[P04](/compare/evidence#p04) [P05](/compare/evidence#p05) [P06](/compare/evidence#p06) [P15](/compare/evidence#p15)
