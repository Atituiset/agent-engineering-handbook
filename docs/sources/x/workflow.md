# X 精选 · 工作流与心智模型

> 16 条精选帖子，按发帖日期（UTC）排序。每条都有原帖链接；摘要忠于原文，引文为原帖逐字摘录。**作者自述**为个人经验，厂商员工谈自家产品时请视为**厂商自报**。原则标签为关键词自动归类，见 [共识度/佐证](/compare/evidence)。

[[toc]]

### XW-001 · 从 /init 开始、动手前先提交：一份上手清单 {#xw-001}
**作者**：Adam（@adamdotdev）｜**日期**：2025-03-15｜[原帖](https://x.com/adamdotdev/status/1900916171009847749)｜♥ 5781

Adam 给出一份 Claude Code 上手步骤：别再想「vibe coding」；启动后先 /init（monorepo 里每个包目录都做）；加 fetch 和 puppeteer 等 MCP；先手工做功能，遇到厌烦的步骤再交给 Claude 并尽量给足细节；在 Claude 接手前先 stage/commit 以便回退。

> "stage/commit changes before claude takes over"

原则：[P11](/compare/evidence#p11) [P14](/compare/evidence#p14) [P16](/compare/evidence#p16) [P17](/compare/evidence#p17)

### XW-002 · 「从没觉得这么落后」：新的可编程抽象层 {#xw-002}
**作者**：Andrej Karpathy（@karpathy）｜**日期**：2025-12-26｜[原帖](https://x.com/karpathy/status/2004607146781278521)｜♥ 55188

Karpathy 写道，程序员亲手贡献的代码越来越少，职业正在被重构；他认为把过去一年出现的工具正确串起来就可能获得 10 倍效率，没拿到这份提升更像是「技能问题」。他列出需要掌握的新抽象层：智能体、子智能体、提示词、上下文、记忆、权限、工具、插件、skills、hooks、MCP、LSP、斜杠命令、工作流等，并强调要为这些「随机、易错、难以理解且不断变化」的实体建立整体心智模型。

> "There's a new programmable layer of abstraction to master"

原则：[P05](/compare/evidence#p05) [P10](/compare/evidence#p10) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13) [P14](/compare/evidence#p14) [P15](/compare/evidence#p15) [P18](/compare/evidence#p18)

### XW-003 · 把 Boris Cherny 的 9 条技巧写进 CLAUDE.md {#xw-003}
**作者**：卡尔的AI沃茨（@aiwarts）｜**日期**：2026-01-04｜[原帖](https://x.com/aiwarts/status/2007753938616131681)｜♥ 5

卡尔的AI沃茨把 Boris Cherny 分享的技巧写进 CLAUDE.md，让 Claude 在对话结束后自检：同时开多个 Claude Code 会话并打开通知；团队共同维护 CLAUDE.md，看到 Claude 做错就写一条规则；会话从 Plan mode 开始，把计划聊到满意再动手。

> "每次看到Claude做错了什么就写规则进去"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P06](/compare/evidence#p06) [P15](/compare/evidence#p15)

### XW-004 · Cursor 博客的 10 条原则：写代码前先用计划模式，混乱时重开对话 {#xw-004}
**作者**：ℏεsam（@Hesamation）｜**日期**：2026-01-14｜[原帖](https://x.com/Hesamation/status/2011553996465717615)｜♥ 1196

ℏεsam 摘录 Cursor 团队关于与智能体编码的最佳实践博文，认为写出可用代码与写出「slop」的差别在于几条简单原则，例如任何代码之前先用计划模式、智能体混乱时开启新对话等。二手摘要。

> "use plan mode before any code"

原则：[P01](/compare/evidence#p01)

### XW-005 · Cursor 官方使用建议：先计划、测试做反馈、跑偏就回滚 {#xw-005}
**作者**：Michael Truell（@mntruell）｜**日期**：2026-01-20｜[原帖](https://x.com/mntruell/status/2013636888242835810)｜♥ 2994

Cursor CEO Michael Truell 列出使用建议：从计划开始（Plan Mode）；让 Cursor 自己搜索，不要过度手动指定上下文；用测试作为反馈回路（TDD，迭代直到通过）；跑偏时回滚、收紧计划再重跑；保持对话简短。

> "When it goes sideways: revert → tighten the plan → rerun"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P06](/compare/evidence#p06) [P07](/compare/evidence#p07) [P09](/compare/evidence#p09)

### XW-006 · 几周 Claude 编码后的随笔：80% 交给智能体 {#xw-006}
**作者**：Andrej Karpathy（@karpathy）｜**日期**：2026-01-26｜[原帖](https://x.com/karpathy/status/2015883857489522876)｜♥ 40711

Karpathy 记录自己在 11 月到 12 月之间，从约 80% 手写加补全、20% 智能体，转为 80% 智能体编码、20% 修改润色，「主要在用英语编程」。他称这是近二十年来自己编码工作流最大的变化，并认为要获得收益需要适应、配置工具，弄清它能做什么、不能做什么。作者自述。

> "I really am mostly programming in English now"

原则：[P01](/compare/evidence#p01) [P05](/compare/evidence#p05) [P06](/compare/evidence#p06) [P07](/compare/evidence#p07) [P08](/compare/evidence#p08) [P11](/compare/evidence#p11) [P13](/compare/evidence#p13) [P14](/compare/evidence#p14)

### XW-007 · Boris 的 10 个技巧（中文整理） {#xw-007}
**作者**：冰零（@cryozerolabs）｜**日期**：2026-02-02｜[原帖](https://x.com/cryozerolabs/status/2018211127889649733)｜♥ 0

冰零整理 Boris Cherny 的技巧：开 3–5 个 git worktree 并行；复杂任务先写好计划；每次纠正后让 Claude 更新规则；重复的事写成 skill 或命令；让 Claude 质疑你的改动并证明有效；用子代理拆分复杂任务、保持主窗口上下文干净。二手整理。

> "每次纠正后让Claude更新规则，它给自己写规则特别准"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P09](/compare/evidence#p09) [P10](/compare/evidence#p10) [P11](/compare/evidence#p11) [P13](/compare/evidence#p13) [P14](/compare/evidence#p14) [P17](/compare/evidence#p17)

### XW-008 · 经营公司本质上就是内部的上下文工程 {#xw-008}
**作者**：tobi lutke（@tobi）｜**日期**：2026-02-16｜[原帖](https://x.com/tobi/status/2023517423761322157)｜♥ 2580

Shopify CEO Tobi Lütke 认为经营公司就是在内部做上下文工程，这项技能在智能体时代更有价值。

> "Running a company is just context engineering internally."

原则：[P02](/compare/evidence#p02) [P13](/compare/evidence#p13)

### XW-009 · 斯坦福 CS146S《The Modern Software Developer》 {#xw-009}
**作者**：astaxie（@astaxie）｜**日期**：2026-02-24｜[原帖](https://x.com/astaxie/status/2026207677576319296)｜♥ 2634

astaxie 介绍斯坦福 CS146S 课程，10 周依次讲提示词工程、Agent 架构、MCP、上下文工程、安全攻防、Code Review、自动做 App 和上线运维。说明高校课程已经把这些主题当作软件开发的基本功。课程内容为作者转述。

> "依次讲解了提示词工程、Agent 架构、MCP、上下文工程、安全攻防、Code Review"

原则：[P02](/compare/evidence#p02) [P05](/compare/evidence#p05) [P08](/compare/evidence#p08) [P14](/compare/evidence#p14) [P15](/compare/evidence#p15) [P16](/compare/evidence#p16)

### XW-010 · 编码智能体在去年 12 月前后「从不能用到能用」 {#xw-010}
**作者**：Andrej Karpathy（@karpathy）｜**日期**：2026-02-25｜[原帖](https://x.com/karpathy/status/2026731645169185220)｜♥ 36761

Karpathy 认为过去两个月编程的变化不是渐进的，而是集中发生在 12 月：模型质量、长程一致性和韧性显著提高，能推进大而长的任务，足以颠覆默认的编程工作流。他同时提醒这个判断有不少保留条件。

> "coding agents basically didn’t work before December and basically work since"

原则：[P05](/compare/evidence#p05) [P06](/compare/evidence#p06) [P08](/compare/evidence#p08) [P11](/compare/evidence#p11) [P18](/compare/evidence#p18)

### XW-011 · 交付 3 个产品后学到的 4 件事 {#xw-011}
**作者**：Gabastino（@gabastino1）｜**日期**：2026-03-23｜[原帖](https://x.com/gabastino1/status/2035989936441077977)｜♥ 0

Gabastino 总结：永远先用 Plan mode，跳过就会返工两次；小任务胜过大提示词，一次只做一件事；智能体陷入循环时停下来重述目标，而不是一直追问；CLAUDE.md 永远没有写完的一天。

> "Plan mode first. Always. Skip it and you rebuild twice."

原则：[P01](/compare/evidence#p01) [P03](/compare/evidence#p03) [P09](/compare/evidence#p09)

### XW-012 · 来自 Claude Code 团队的要点：Plan mode、给它验证手段、让它反过来采访你 {#xw-012}
**作者**：Tech with Mak（@techNmak）｜**日期**：2026-03-28｜[原帖](https://x.com/techNmak/status/2037788648691884207)｜♥ 4416

Tech with Mak 摘录 claude-code-best-practice 中整理的 Claude Code 团队建议：始终使用 plan mode，并给 Claude 一个验证自己工作的方法；让 Claude 用提问工具反过来「采访」你以澄清需求；用 git worktree 并行。二手摘要。

> "Always use plan mode, give Claude a way to verify"

原则：[P01](/compare/evidence#p01) [P06](/compare/evidence#p06) [P11](/compare/evidence#p11)

### XW-013 · 我们会花更多时间去理解模型的输出 {#xw-013}
**作者**：Andrej Karpathy（@karpathy）｜**日期**：2026-10-02｜[原帖](https://x.com/karpathy/status/2105819303471976479)｜♥ 56866

Karpathy 认为今后会花多得多的时间去理解语言模型的产出，并分享技巧：例如让模型用 ASD-STE100（源自航空维修文档的受控语言规范）来解释问题，借其严格约束获得清晰文字。这与「人要读懂并为产出负责」的主张一致。

> "We'll be spending a lot more time trying to understand the outputs of language models."

原则：[P01](/compare/evidence#p01) [P05](/compare/evidence#p05) [P17](/compare/evidence#p17)

### XW-014 · Lee Robinson 斯坦福 CS146S 讲座：常驻主动智能体的 harness 与上下文工程 {#xw-014}
**作者**：Lee Robinson（@leerob）｜**日期**：2026-10-09｜[原帖](https://x.com/leerob/status/2108650243365736855)｜♥ 4744

Cursor 的 Lee Robinson 分享他在斯坦福 CS146S 的讲座，章节包括模型发生了什么变化、常驻智能体的内部结构、harness 和上下文工程。帖子本身为讲座提纲。

> "How do always-on, proactive agents"

原则：[P02](/compare/evidence#p02)

### XW-015 · 做出「能上线」小产品的 4 步：手册、管上下文、先规划、质量闭环 {#xw-015}
**作者**：Zk（@Zklnbp）｜**日期**：2026-10-14｜[原帖](https://x.com/Zklnbp/status/2110372698618466712)｜♥ 3

作者总结 4 步：把技术栈、目录约定和不许乱改的边界写进 CLAUDE.md；用 /context 和 /compact 管住上下文；用 Plan Mode 先设计、点头后再写；定下验收标准（移动端、空态、加载态等），让它循环打磨到像真产品。

> "上下文是白板：写满了就忘早先的。"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P05](/compare/evidence#p05) [P06](/compare/evidence#p06) [P18](/compare/evidence#p18)

### XW-016 · 瓶颈已不在构建软件：让 Agent 好用、让人好审 {#xw-016}
**作者**：宝玉（@dotey）｜**日期**：2026-11-10｜[原帖](https://x.com/dotey/status/2120237447963415014)｜♥ 198

宝玉认为软件开发的瓶颈已不是把专业软件做出来，而是两件事：让 Agent 更好地使用软件（对 Agent 最友好的是 CLI、MCP 和代码，而不是 GUI）；以及让人更好地预览和微调 Agent 的结果——人主要负责检查、标记、评论和微调。

> "Agent 最友好的方式是 cli、MCP和代码"

原则：[P14](/compare/evidence#p14) [P17](/compare/evidence#p17)
