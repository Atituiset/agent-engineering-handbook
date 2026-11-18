# X 精选 · 评审与代码质量

> 14 条精选帖子，按发帖日期（UTC）排序。每条都有原帖链接；摘要忠于原文，引文为原帖逐字摘录。**作者自述**为个人经验，厂商员工谈自家产品时请视为**厂商自报**。原则标签为关键词自动归类，见 [共识度/佐证](/compare/evidence)。

[[toc]]

### XR-001 · 开发速度上去了，上线速度要靠高精度的 AI 评审 {#xr-001}
**作者**：Rohan Paul（@rohanpaul_ai）｜**日期**：2025-08-19｜[原帖](https://x.com/rohanpaul_ai/status/1957868316711616898)｜♥ 23

Rohan Paul 认为 vibe coding 让开发速度很高，但除非能用 AI 高精度地评审 AI 生成的代码，否则无法以同样速度上线；他推荐一款智能体式 PR 评审工具作为团队的第一层质量关。含产品推荐成分。

> "you can not bring code to production at the same speed"

原则：[P04](/compare/evidence#p04) [P05](/compare/evidence#p05) [P08](/compare/evidence#p08) [P16](/compare/evidence#p16) [P17](/compare/evidence#p17)

### XR-002 · 并行再多，瓶颈也在验收；值得投入的是文档与流程自动化 {#xr-002}
**作者**：Kevin Ma（@kevinma_dev_zh）｜**日期**：2026-01-04｜[原帖](https://x.com/kevinma_dev_zh/status/2007652429618434051)｜♥ 34

Kevin Ma 评论 Boris 的工作流：开发速度已经快到评审和测试跟不上，即使有评审智能体，功能验收仍要人来做，并行再多瓶颈也在验收。他认为更值得投入的是维护设计文档、编码规范和最佳实践，以及流程自动化；MCP 不宜多，能用命令行就用命令行。

> "并行跑再多任务，瓶颈在验收那一环。"

原则：[P02](/compare/evidence#p02) [P06](/compare/evidence#p06) [P08](/compare/evidence#p08) [P10](/compare/evidence#p10) [P11](/compare/evidence#p11) [P13](/compare/evidence#p13) [P14](/compare/evidence#p14)

### XR-003 · AI 编程不是 prompt 玄学：差距在需求拆解、任务边界和 review {#xr-003}
**作者**：阿J｜AI编程实战（@charm1728）｜**日期**：2026-05-18｜[原帖](https://x.com/charm1728/status/2056278015932588395)｜♥ 1

一位独立开发者的自我介绍中给出核心观点：用 AI 写代码真正拉开差距的不是提示词技巧，而是需求拆解、任务边界划分和代码评审。

> "真正拉开差距的是需求拆解、任务边界和 review。"

原则：[P05](/compare/evidence#p05) [P08](/compare/evidence#p08) [P19](/compare/evidence#p19)

### XR-004 · Bun 作者预测：几个月内由自动评审 + 新上下文判定 + 自动合并 {#xr-004}
**作者**：Jarred Sumner（@jarredsumner）｜**日期**：2026-07-15｜[原帖](https://x.com/jarredsumner/status/2077504710739956019)｜♥ 712

Jarred Sumner 说今天仍由人按下合并，但他预计几个月内会变成：自动评审给出 LGTM，另一个拥有全新上下文窗口的 Claude 判断改动是否简单、影响范围小，然后自动合并。这是对「人工评审不可省」的反向预测。

> "another Claude with a fresh context window judges if it’s simple and low blast-radius -> auto-merge"

原则：[P02](/compare/evidence#p02) [P08](/compare/evidence#p08)

### XR-005 · Addy Osmani 的评审方式：代码越多，人工评审越有选择性 {#xr-005}
**作者**：Addy Osmani（@addyosmani）｜**日期**：2026-09-07｜[原帖](https://x.com/addyosmani/status/2097027173941141799)｜♥ 1023

Addy Osmani 介绍他现在的评审方式：不再逐行读完所有代码；每个 PR 先由多智能体做第一轮，找 bug、验证、按严重性排序并给出修复建议；凡是重要的变更，批准仍由人决定；低风险变更可以减少人工投入。

> "Approval stays a human call on anything that matters."

原则：[P06](/compare/evidence#p06) [P08](/compare/evidence#p08) [P11](/compare/evidence#p11)

### XR-006 · 「既然都是提示词，何必让我再 ping 一次智能体？」 {#xr-006}
**作者**：Peter Steinberger（@steipete）｜**日期**：2026-09-07｜[原帖](https://x.com/steipete/status/2097091456234111377)｜♥ 1101

Peter Steinberger 向上游项目提交 PR 后被要求做小修改，他质疑这种流程的意义：对方已经写好了提示词，为什么还要让他再叫自己的智能体修改，然后由对方的智能体合并。反映智能体时代代码评审协作方式的摩擦。

> "What’s even the point with this workflow?"

原则：[P08](/compare/evidence#p08)

### XR-007 · 最好的项目在用更多自动评审、冒烟测试和自动回滚跟上节奏 {#xr-007}
**作者**：Kyle Daigle（@kdaigle）｜**日期**：2026-09-16｜[原帖](https://x.com/kdaigle/status/2100218226173182037)｜♥ 51

GitHub COO Kyle Daigle 观察到，最好的项目正在比以往更多地使用自动评审、验证/冒烟测试和自动回滚来跟上开发节奏；PR 数量增长很快，即便 PR 由其他智能体创建，Copilot 代码评审的使用量也大幅增加。厂商观察。

> "The best projects are using more automated reviews, validation/smoke testing, auto-rollbacks than ever before to keep up with the pace."

原则：[P06](/compare/evidence#p06) [P08](/compare/evidence#p08) [P09](/compare/evidence#p09)

### XR-008 · 人工评审是瓶颈、严格 harness 又不再最优时，如何监督智能体？ {#xr-008}
**作者**：Uncle Bob Martin（@unclebobmartin）｜**日期**：2026-09-18｜[原帖](https://x.com/unclebobmartin/status/2100938985543446954)｜♥ 1645

Robert C. Martin 提出他的现行方案：用一个「审讯」工具配合智能体，以类 UML 图展示系统结构，并按 CRAP 和变异测试得分着色；人可以逐层点击深入到代码，发现需要改进的结构后让对应的智能体修改，从架构调整到底层重构都可以。他把工具开源作为模板。作者自述。

> "how should we supervise their output."

原则：[P05](/compare/evidence#p05) [P08](/compare/evidence#p08) [P12](/compare/evidence#p12)

### XR-009 · 永远做对抗式评审；贵模型编排、便宜模型干活 {#xr-009}
**作者**：Terry（@Cardgames）｜**日期**：2026-10-08｜[原帖](https://x.com/Cardgames/status/2107999896988954900)｜♥ 18

作者的 AI 编码建议：用更便宜的子智能体完成实际构建以节省 token；用强模型作为编排者；并且永远做对抗式评审。

> "ALWAYS ADVERSARIAL REVIEW."

原则：[P08](/compare/evidence#p08) [P10](/compare/evidence#p10)

### XR-010 · 证据驱动的人工评审：让智能体拿出「做了什么、为什么是对的」 {#xr-010}
**作者**：Peter Yang（@petergyang）｜**日期**：2026-10-12｜[原帖](https://x.com/petergyang/status/2109433961223180517)｜♥ 29

Peter Yang 转述 Micky 的做法：在不完全信任智能体的阶段，人工评审是最后一步，此前尽量收集智能体给出的证据——前后对比的证据驱动测试等，让智能体呈现「完成了什么、为什么是好的」，以此建立信任并减少人工评审的摩擦。

> "The agent presents evidence: This is the work that's done, and this is why it's good."

原则：[P06](/compare/evidence#p06) [P08](/compare/evidence#p08)

### XR-011 · Claude Code Review 跑在所有 PR 上 {#xr-011}
**作者**：Boris Cherny（@bcherny）｜**日期**：2026-10-16｜[原帖](https://x.com/bcherny/status/2111158313463525518)｜♥ 5048

Boris Cherny 说他离不开 Claude Code Review：它在他所有 PR 上运行，几乎能在合入前抓住所有 bug，是团队既快又能提高质量标准的关键之一。厂商自报，「几乎所有 bug」没有公开度量。

> "It runs on all of my PRs, and catches almost every bug before it goes it."

原则：[P08](/compare/evidence#p08) [P15](/compare/evidence#p15)

### XR-012 · /walden-review：用自己半年的评审记录训练出的评审 skill {#xr-012}
**作者**：Walden（@walden_yan）｜**日期**：2026-10-20｜[原帖](https://x.com/walden_yan/status/2112610802830381394)｜♥ 292

Cognition 的 Walden Yan 厌倦了评审代码，于是基于自己过去 6 个月的 GitHub 评论和智能体会话自动生成一个评审 skill，连评论风格都学了。他每次先跑它再亲自读 PR，认为它能抓住设计、代码模式和架构问题，并提醒这个方法很费 token。作者自述。

> "I always run it before ever reading a PR myself"

原则：[P02](/compare/evidence#p02) [P05](/compare/evidence#p05) [P08](/compare/evidence#p08) [P10](/compare/evidence#p10) [P11](/compare/evidence#p11) [P13](/compare/evidence#p13) [P16](/compare/evidence#p16) [P18](/compare/evidence#p18)

### XR-013 · 腾讯开源 LoopForge：写的人不审，退出码说了算 {#xr-013}
**作者**：Berryxia.AI（@berryxia）｜**日期**：2026-11-16｜[原帖](https://x.com/berryxia/status/2122361955453452651)｜♥ 47

Berryxia 介绍腾讯开源的 AI 代码交付平台 LoopForge，其发布帖称代码从来不是瓶颈，交接才是。做法是把交付流程写成 SOP：计划、写代码、审代码、测试由不同 Agent 担任，写的人不审；编译和测试看退出码，不听 Agent 自己说「好了」；关键节点等人批准；每次运行打分复盘、改进建议经人审后写回 SOP。厂商自报。

> "脚本说了算：编译和测试过没过，看退出码，不听 Agent 自己说「好了」。"

原则：[P01](/compare/evidence#p01) [P06](/compare/evidence#p06) [P19](/compare/evidence#p19)

### XR-014 · 最有用的事：让 LLM 生成的产物更容易被人理解 {#xr-014}
**作者**：David Cramer（@zeeg）｜**日期**：2026-11-17｜[原帖](https://x.com/zeeg/status/2122767883080241305)｜♥ 280

Sentry 创始人 David Cramer 认为，与其追逐各种 skill，更能加速公司的事情是让 LLM 生成的产物更容易被理解，例如评审导览（而不是又一张 mermaid 图或更多 Markdown 文本）或更好的可视化。

> "the most useful thing you can do to accelerate your company is to make LLM generated artifacts easier to understand"

原则：[P08](/compare/evidence#p08) [P13](/compare/evidence#p13)
