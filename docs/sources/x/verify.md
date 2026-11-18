# X 精选 · 测试与验证

> 14 条精选帖子，按发帖日期（UTC）排序。每条都有原帖链接；摘要忠于原文，引文为原帖逐字摘录。**作者自述**为个人经验，厂商员工谈自家产品时请视为**厂商自报**。原则标签为关键词自动归类，见 [共识度/佐证](/compare/evidence)。

[[toc]]

### XV-001 · 把你手工做的检查编码进工作流，让 Claude 自己闭环 {#xv-001}
**作者**：0xMarioNawfal（@RoundtableSpace）｜**日期**：2026-06-14｜[原帖](https://x.com/RoundtableSpace/status/2066215340175217089)｜♥ 73

作者回答「怎样让 Claude Code 在交回前检查自己的工作」：把你手动做的检查（类型检查、测试）直接编码进工作流，Claude 就能自己关闭反馈回路。

> "Encode your manual checks - type checking, tests directly into the workflow"

原则：[P04](/compare/evidence#p04) [P06](/compare/evidence#p06)

### XV-002 · 最好的工程师一直在自动化：lint 规则与 e2e 测试的杠杆更大了 {#xv-002}
**作者**：Boris Cherny（@bcherny）｜**日期**：2026-07-15｜[原帖](https://x.com/bcherny/status/2077460395279692197)｜♥ 9959

Claude Code 负责人 Boris Cherny 回顾：过去最好的工程师会花大量时间自动化自己的工作，例如写 lint 规则捕捉反复出现的问题、积累 e2e 测试以免手工冒烟测试。他认为这些投入是杠杆最高的活动，并指出在智能体时代很多这类自动化变得更加重要。

> "writing lint rules to catch repeat code issues, building up a suite of e2e tests"

原则：[P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P04](/compare/evidence#p04) [P05](/compare/evidence#p05) [P06](/compare/evidence#p06) [P08](/compare/evidence#p08) [P13](/compare/evidence#p13)

### XV-003 · 大规模并行 QA：过去会在压缩边界崩溃，或模型开始「作弊」 {#xv-003}
**作者**：Peter Steinberger（@steipete）｜**日期**：2026-07-26｜[原帖](https://x.com/steipete/status/2081169373784633552)｜♥ 1431

Peter Steinberger 用 Codex 全天做大规模并行 QA 准备发版，认为新模型很能理解意图、能发现复杂的行为问题；他提到过去这类工作流会在上下文压缩的边界崩溃，或者模型开始作弊。作者自述。

> "In the past such workflow did fell apart at compaction boundaries and/or the model started cheating."

原则：[P02](/compare/evidence#p02) [P11](/compare/evidence#p11)

### XV-004 · 400 多个用例的测试套件，抓取 pty 输出和截图 {#xv-004}
**作者**：Mitchell Hashimoto（@mitchellh）｜**日期**：2026-08-21｜[原帖](https://x.com/mitchellh/status/2090893729469268109)｜♥ 824

Mitchell Hashimoto 说这项工作中，模型帮他搭建了 400 多个以 shell 脚本编写的测试用例，以及一个运行 Kitty 和 Ghostty 终端 GUI、同时抓取完整 pty 流和截图（动画需多张）的测试 harness。说明让智能体搭验证设施本身也是重要用法。

> "put together a test suite of over 400 cases that are bare shell scripts plus a harness"

原则：[P06](/compare/evidence#p06)

### XV-005 · Anthropic：Claude 写 80% 代码之后，测试增长 10 倍、CI 任务增长 25 倍 {#xv-005}
**作者**：Addy Osmani（@addyosmani）｜**日期**：2026-09-14｜[原帖](https://x.com/addyosmani/status/2099577600159158765)｜♥ 5028

Addy Osmani 转述 Anthropic 的数据：Claude 写了其 80% 的代码，工程师每季度交付的代码量是原来的 8 倍；副作用是测试增长 10 倍，CI 任务在 6 个月内增长 25 倍，并附上他们如何扩展的文章。厂商自报。说明产出增长后，验证基础设施成为瓶颈。

> "Side effect: Tests grew 10x. CI jobs up 25x in 6 months."

原则：[P04](/compare/evidence#p04) [P06](/compare/evidence#p06)

### XV-006 · 用 Lean 和 TLA+ 让模型做形式化验证 {#xv-006}
**作者**：Boris Cherny（@bcherny）｜**日期**：2026-09-22｜[原帖](https://x.com/bcherny/status/2102543349102338309)｜♥ 6349

Boris Cherny 说他用模型配合 Lean 对 Claude Agent SDK 做形式化验证，几条简短提示产生了 16 个修复 bug 和竞态条件的 PR；他有时结合 Lean 与 TLA+ 查找数据流、并发和状态管理问题。厂商自报。

> "I sometimes combine Lean and TLA+ to look for issues around data flow, concurrency, and state mgmt."

原则：[P06](/compare/evidence#p06) [P08](/compare/evidence#p08)

### XV-007 · 让 Codex 决定哪些测试需要跑，大幅削减 CI {#xv-007}
**作者**：Peter Steinberger（@steipete）｜**日期**：2026-09-27｜[原帖](https://x.com/steipete/status/2104305554760114488)｜♥ 767

Peter Steinberger 因 CI 负载过重，计划让 Codex 判断哪些测试真正需要运行，大幅削减 CI，改为每小时跑测试。这与「每次变更都全量验证」的传统做法相反，是在成本压力下的取舍。作者自述的计划。

> "My plan is to let codex decide which tests actually need to run and drastically nix CI and run tests hourly."

原则：[P01](/compare/evidence#p01) [P04](/compare/evidence#p04) [P06](/compare/evidence#p06)

### XV-008 · Hamel Husain：评测工作流应先看数据，再写 eval {#xv-008}
**作者**：Hamel Husain（@HamelHusain）｜**日期**：2026-09-29｜[原帖](https://x.com/HamelHusain/status/2104945863084904737)｜♥ 502

Hamel Husain 试用某个自动化评测工作流后批评：它在看数据之前就生成 eval，再让人纠正它的错误；他认为应该先看数据，以此建立理解、决定优先级，然后再写 eval。他还主张人应自己建立看数据的工具，而不是只「告诉」模型哪些标签错了。

> "I believe you should be looking at data first to inform your understanding"

原则：[P18](/compare/evidence#p18)

### XV-009 · 做 QA 智能体 harness 最难的两件事：速度，以及「什么才算正确」 {#xv-009}
**作者**：ThePrimeagen（@ThePrimeagen）｜**日期**：2026-10-05｜[原帖](https://x.com/ThePrimeagen/status/2107206811354845239)｜♥ 817

ThePrimeagen 更新他做 QA 智能体 harness 的进展：难点一是在智能体很慢的情况下如何跑得快；难点二是什么才是正确的、到底要测什么。

> "What is correct?  What do we even test?"

原则：[P06](/compare/evidence#p06)

### XV-010 · 生成快过评审时，瓶颈转向「证明它是对的」 {#xv-010}
**作者**：Addy Osmani（@addyosmani）｜**日期**：2026-10-17｜[原帖](https://x.com/addyosmani/status/2111604705340326393)｜♥ 2536

Addy Osmani 再次强调给智能体验证手段能显著提升质量：在这样的流程下，Claude Code 90% 以上的代码由它自己编写；当生成软件的速度快过你能评审的速度，瓶颈就转移到证明代码正确上。数据为 Anthropic 自报。

> "When generating software at a faster rate than you can review it, the bottleneck shifts to proving"

原则：[P06](/compare/evidence#p06) [P08](/compare/evidence#p08)

### XV-011 · 想要更好的产出？给智能体验证自己工作的手段 {#xv-011}
**作者**：Addy Osmani（@addyosmani）｜**日期**：2026-10-23｜[原帖](https://x.com/addyosmani/status/2113677798774898773)｜♥ 673

Addy Osmani 认为提高智能体产出质量的关键是给它验证自己工作的方式。他提到 Warp 让每个智能体拥有一台电脑并带回操作视频；他自己的流程在 E2E 测试之外，也让 Claude 提供录制的视频作为证据。

> "Give it a way to verify its own work."

原则：[P06](/compare/evidence#p06)

### XV-012 · 重写系统不一定需要现成测试套件，让智能体自己建 {#xv-012}
**作者**：Armin Ronacher ⇌（@mitsuhiko）｜**日期**：2026-11-01｜[原帖](https://x.com/mitsuhiko/status/2116895016249434134)｜♥ 317

Armin Ronacher 反驳「价值在测试套件」的说法：重建一个东西并不一定需要现成测试套件，为移植专门让智能体自建测试可能更好，部分原因是很多既有测试不适合用来「爬坡」。他举例：几周前让智能体重写 Excel 公式引擎，测试套件是它从零建的。作者自述。

> "you're probably better off having the agent builds its own test suite specifically for porting"

原则：[P06](/compare/evidence#p06)

### XV-013 · 今日提示词：「怎样让这个改动完全可验证？」 {#xv-013}
**作者**：Matt Pocock（@mattpocockuk）｜**日期**：2026-11-05｜[原帖](https://x.com/mattpocockuk/status/2118313863917564136)｜♥ 2841

Matt Pocock 推荐一个简单的提示词：「How do we make this change fully verifiable?」他说这会让智能体竭尽全力验证所有改动，包括注册真实服务、点击前端，质量大幅提升。作者自述。

> ""How do we make this change fully verifiable?""

原则：[P06](/compare/evidence#p06)

### XV-014 · 生成代码变便宜后，验证成了难点 {#xv-014}
**作者**：Gergely Orosz（@GergelyOrosz）｜**日期**：2026-11-16｜[原帖](https://x.com/GergelyOrosz/status/2122324513211728161)｜♥ 1106

Gergely Orosz 推介与 Satya Nadella 的播客，主题是「生成代码便宜、验证代码困难」时软件工程会是什么样，章节包括验证 AI 生成代码与软件工厂。帖子本身只是节目提纲。

> "generating the code becomes cheap and verifying it is the hard part"

原则：[P06](/compare/evidence#p06) [P18](/compare/evidence#p18)
