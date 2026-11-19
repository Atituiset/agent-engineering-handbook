# 质量与 CI/CD 专题 · X 精选

> X 上的一线声音。帖子为作者个人观点；厂商人员谈自家产品标为厂商自述。 每条都有摘要、逐字核对过的原文引文（英文保留原文）和链接；原则编号 Q01–Q13 见 [第 12 章](/handbook/12-quality-cicd#principles)。检索与核对时间：2026-11 中旬。

### QX01 · LLM 的 bug 变了：更少差一错误，更多系统设计与上下文缺失 {#qx01}
**作者**：Boris Cherny（@bcherny）｜**日期**：2026-08-11｜[原帖](https://x.com/bcherny/status/2087284684103537011)｜♥ 4333

Claude Code 负责人 Boris Cherny 认为模型仍会产生 bug，但类型已不同：少了差一错误，多了系统设计、UI 可用性、缺乏全局上下文类问题；部分编码已被“解决”，但并非全部，并提到对抗式代码评审。意味着测试与评审的重心要从语法级转向设计与行为级。

> “It’s less off-by-ones and more about system design, ui usability, missing broader context.”

**证据类型**：厂商人员自述｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q05](/handbook/12-quality-cicd#q05)

### QX02 · DHH 的对抗式评审：用 Codex 时让 Claude 评，用 Claude 时让 Codex 评 {#qx02}
**作者**：DHH（@dhh）｜**日期**：2026-10-07｜[原帖](https://x.com/dhh/status/2107882896195199116)｜♥ 3554

Rails 作者 DHH 分享“对抗式代码评审”：驱动 Codex 时让它调用 Claude 评审，反之亦然；模型会用 CLI 发起评审、轮流发言、自己解决分歧。是“作者≠评审者、异构模型互审”的简单落地。

> “Here's my technique for adversarial code review if I'm driving from Codex: "Review this with claude".”

**证据类型**：作者自述｜**对应原则**：[Q07](/handbook/12-quality-cicd#q07) [Q06](/handbook/12-quality-cicd#q06)

### QX03 · Addy Osmani：给智能体验证手段，瓶颈转向“证明” {#qx03}
**作者**：Addy Osmani（@addyosmani）｜**日期**：2026-10-17｜[原帖](https://x.com/addyosmani/status/2111604705340326393)｜♥ 2534

Addy Osmani 转述 Claude Code 团队经验：给智能体验证自身工作的手段能显著提高质量，有了这套流程 Claude Code 90% 以上的代码由它自己写；当生成速度超过你的评审速度，瓶颈就转移到“证明它是对的”。（此链接 v2 已收录，本专题从质量保障角度重读。）

> “When generating software at a faster rate than you can review it, the bottleneck shifts to proving”

**证据类型**：作者自述（转述厂商）｜**对应原则**：[Q02](/handbook/12-quality-cicd#q02) [Q12](/handbook/12-quality-cicd#q12)

### QX04 · Matt Pocock：把“同义反复测试有害”写进编码规范，让评审技能执行 {#qx04}
**作者**：Matt Pocock（@mattpocockuk）｜**日期**：2026-08-27｜[原帖](https://x.com/mattpocockuk/status/2093068185830347088)｜♥ 2066

TypeScript 教育者 Matt Pocock：一条命令把 “Tautological tests considered harmful.” 追加进 CODING_STANDARDS.md，之后他的 /code-review 技能就会在评审时检查这类“测试实现本身”的无效测试。

> “From then on, /code-review will pick this up”

**证据类型**：作者自述｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05) [Q06](/handbook/12-quality-cicd#q06)

### QX05 · Boris Cherny 三条：计划模式、给验证手段、人机同标准 {#qx05}
**作者**：Boris Cherny（@bcherny）｜**日期**：2025-12-27｜[原帖](https://x.com/bcherny/status/2004711722926616680)｜♥ 1277

Boris Cherny 回答如何用好 Claude Code：几乎总是用计划模式；给 Claude 验证输出的方式（单元测试、Chrome 扩展、iOS/Android 模拟器）；对人写和 Claude 写的代码保持同样标准，用 /code-review 自动化大部分评审。

> “Hold the same bar for human and Claude code.”

**证据类型**：厂商人员自述｜**对应原则**：[Q02](/handbook/12-quality-cicd#q02) [Q06](/handbook/12-quality-cicd#q06) [Q03](/handbook/12-quality-cicd#q03)

### QX06 · Simon Willison：不只是单元测试，所有顶级工程实践都在加速智能体 {#qx06}
**作者**：Simon Willison（@simonw）｜**日期**：2025-09-30｜[原帖](https://x.com/simonw/status/1973146252767535365)｜♥ 1078

Simon Willison：自动化测试、完善文档、良好的版本控制习惯、代码评审文化、快速部署到预发环境……这些顶级软件工程实践都会放大编码智能体的生产力。

> “It's not just unit tests - there are so many other top tier software engineering practices that accelerate productivity with coding agents”

**证据类型**：作者自述｜**对应原则**：[Q02](/handbook/12-quality-cicd#q02) [Q11](/handbook/12-quality-cicd#q11) [Q06](/handbook/12-quality-cicd#q06)

### QX07 · Matt Pocock：发现智能体的坏习惯 → 写进规范 → 评审时强制 {#qx07}
**作者**：Matt Pocock（@mattpocockuk）｜**日期**：2026-08-14｜[原帖](https://x.com/mattpocockuk/status/2088256432265167185)｜♥ 1073

Matt Pocock 描述可定制的评审循环：注意到智能体做了坏事，就写进仓库根目录的 CODING_STANDARDS.md，/code-review 技能在评审时据此执行；他已积累数百条。是“把评审意见沉淀成规则”的个人版。

> “Write it in CODING_STANDARDS.md (root of the repo)”

**证据类型**：作者自述｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06)

### QX08 · Kieran Klaassen：把 Playwright 测试加入评审流程，评审真正验证 UI {#qx08}
**作者**：Kieran Klaassen（@kieranklaassen）｜**日期**：2025-12-18｜[原帖](https://x.com/kieranklaassen/status/2001721585691185446)｜♥ 914

Every 的 Kieran Klaassen：模型能用 Playwright 导航页面、截快照、查控制台错误、测试交互；他把这加进代码评审工作流，评审从“读代码”变成“验证 UI 真能用”。

> “Now reviews actually verify the UI works.”

**证据类型**：作者自述｜**对应原则**：[Q02](/handbook/12-quality-cicd#q02) [Q06](/handbook/12-quality-cicd#q06) [Q05](/handbook/12-quality-cicd#q05)

### QX09 · Codex /review：内部担心“机器人评论”，结果抓到大量 bug {#qx09}
**作者**：Alexander Embiricos（@embirico）｜**日期**：2025-09-19｜[原帖](https://x.com/embirico/status/1968845953605280043)｜♥ 621

OpenAI 的 Alexander Embiricos：团队原本担心在内部推出 GPT-5-Codex 代码评审会招人反感（没人喜欢突如其来的机器人评论），结果反响很好、抓到各种离谱的 bug；随后开放 CLI 本地 /review。厂商自报。

> “We were nervous shipping GPT-5-Codex code review to the @openai team—nobody likes surprise bot comments.”

**证据类型**：厂商人员自述｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06)

### QX10 · Addy Osmani：评审开始前先定义“完成” {#qx10}
**作者**：Addy Osmani（@addyosmani）｜**日期**：2026-10-11｜[原帖](https://x.com/addyosmani/status/2109358790298787931)｜♥ 620

Addy Osmani：验证是获得好结果最重要的事之一；评审前要先明确定义“完成”，否则人或智能体评审者被要求找 bug 时总能找到“可以改进”的地方。（此链接 v2 已收录，本专题从质量保障角度重读。）

> “Clearly define "done" before code review starts.”

**证据类型**：作者自述｜**对应原则**：[Q01](/handbook/12-quality-cicd#q01) [Q06](/handbook/12-quality-cicd#q06)

### QX11 · Addy Osmani：值得投资的几类测试——E2E 作为基准真相、属性测试…… {#qx11}
**作者**：Addy Osmani（@addyosmani）｜**日期**：2026-10-05｜[原帖](https://x.com/addyosmani/status/2106995301802541481)｜♥ 1175

Addy Osmani 列出让智能体产出高质量结果值得投入的测试：模拟真实用户流程的端到端测试作为基准真相、属性测试等。

> “Write end-to-end tests that simulate real user flows and act as the ground truth”

**证据类型**：作者自述｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05) [Q02](/handbook/12-quality-cicd#q02)

### QX12 · Dex Horthy：功能开关不是银弹 {#qx12}
**作者**：dex（@dexhorthy）｜**日期**：2026-05-18｜[原帖](https://x.com/dexhorthy/status/2056397834212249684)｜♥ 410

HumanLayer 的 Dex Horthy 提醒：大团队的资深工程师有一半时间在清理功能开关蔓延与死代码，且多数来自 AI 之前；把功能开关当作 AI 代码安全网时要算上它的长期成本。是对“用 flag 兜底”的限定意见。

> “Feature flags are not the silver bullet you’re looking for”

**证据类型**：作者自述｜**对应原则**：[Q11](/handbook/12-quality-cicd#q11)

### QX13 · Boris Cherny：默认开启自动代码评审与安全评审 {#qx13}
**作者**：Boris Cherny（@bcherny）｜**日期**：2026-07-17｜[原帖](https://x.com/bcherny/status/2077929390806073807)｜♥ 340

Boris Cherny 描述 Claude Code 团队的做法：让 Claude 端到端验证自己的工作，默认开启自动代码评审和安全评审，并用能同时管理多个智能体的界面。厂商人员自述。

> “defaulting on automated code review and security review”

**证据类型**：厂商人员自述｜**对应原则**：[Q02](/handbook/12-quality-cicd#q02) [Q06](/handbook/12-quality-cicd#q06) [Q09](/handbook/12-quality-cicd#q09)

### QX14 · Hamel Husain：LLM 裁判也是分类器，要对照人工标签测试 {#qx14}
**作者**：Hamel Husain（@HamelHusain）｜**日期**：2026-09-20｜[原帖](https://x.com/HamelHusain/status/2101533413010440593)｜♥ 465

Hamel Husain 提醒：LLM 裁判本质上也是分类器，要用人工标签测试它，并且不要过拟合。

> “Remember that a LLM Judge is also classifier*. Make sure to test your classifiers against human labels and don't overfit.”

**证据类型**：作者自述｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08)

### QX15 · David Cramer：怎么让 GPT 别再写垃圾单元测试？ {#qx15}
**作者**：David Cramer（@zeeg）｜**日期**：2026-07-29｜[原帖](https://x.com/zeeg/status/2082343469725749408)｜♥ 166

Sentry 创始人 David Cramer 求助：人类通常写覆盖多个行为的高层测试、只保留少量单元测试，而 GPT 无论怎么提示都倾向写大量琐碎单元测试。反映“测试数量≠测试价值”的普遍痛点。

> “anyone have a testing policy/doc/skill that they find effective to get GPT to stop writing junk unit tests”

**证据类型**：作者自述｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05)

### QX16 · Shreya Shankar：Evals 的两部分——发现失败模式与度量其频率 {#qx16}
**作者**：Shreya Shankar（@sh_reya）｜**日期**：2026-07-26｜[原帖](https://x.com/sh_reya/status/2081444175061598455)｜♥ 132

Shreya Shankar：评测包括两个完全不同的部分——发现失败模式是什么，以及度量这些失败模式有多普遍以便排优先级；LLM 能帮助发现一部分失败模式，但不是全部。

> “In evals you have two totally different components: (1) discovery of what the failure modes are, (2) focused measurement of how prevalent these failure modes are—so you can prioritize what to fix.”

**证据类型**：作者自述｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08)

### QX17 · 属性测试 + Claude Code 的组合值得写一篇 {#qx17}
**作者**：Jake Nations（@nayshins）｜**日期**：2025-12-27｜[原帖](https://x.com/nayshins/status/2004749968960356667)｜♥ 127

Jake Nations 表示属性测试与 Claude Code 搭配的收益值得专门写文章，体现属性测试在智能体时代被重新重视。

> “property based testing + claude code”

**证据类型**：作者自述｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05)

### QX18 · Claude Code 插件 evals：新模型发布后确认 skills 还管用 {#qx18}
**作者**：Thariq（@trq212）｜**日期**：2026-09-11｜[原帖](https://x.com/trq212/status/2098531560643539440)｜♥ 2242

Anthropic 的 Thariq：用户反馈难以确认 skills 在新模型发布后是否仍然有效，于是推出插件 evals（`claude plugin eval init`）。把“提示资产”也纳入回归测试。厂商人员自述。

> “we heard feedback that it's hard to know if your skills are still working with new model releases”

**证据类型**：厂商人员自述｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08)

### QX19 · Cursor CLI 可在 GitHub Actions 中做代码评审 {#qx19}
**作者**：eric zakariasson（@ericzakariasson）｜**日期**：2025-08-29｜[原帖](https://x.com/ericzakariasson/status/1961487028413239672)｜♥ 225

Cursor 的 Eric Zakariasson 展示如何在 GitHub Actions 中用 Cursor CLI 做代码评审，AI 评审成为 CI 的一个步骤。

> “here's how you can set it up to do code review for you in github actions”

**证据类型**：厂商人员自述｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06)

### QX20 · 宝玉：AI 对测试的影响——测试价值反而被看见 {#qx20}
**作者**：宝玉（@dotey）｜**日期**：2025-07-23｜[原帖](https://x.com/dotey/status/1948164061272662089)｜♥ 159

宝玉转述并认同一篇文章：AI 写代码看似产出更高，但 bug 会更多，测试的重要性更加凸显；测试可以“左移”到技术方案阶段，在代码生成之前介入质量管理。

> “测试价值在 AI 时代反而“被看见”了”

**证据类型**：作者自述｜**对应原则**：[Q01](/handbook/12-quality-cicd#q01) [Q02](/handbook/12-quality-cicd#q02)

### QX21 · Cursor 团队自用技能包：loop-on-ci、fix-ci 等 {#qx21}
**作者**：meng shao（@shao__meng）｜**日期**：2026-05-04｜[原帖](https://x.com/shao__meng/status/2051303113626460533)｜♥ 315

orange.ai 介绍 Cursor 官方团队自用的技能插件 cursor-team-kit：其中“CI / 合并循环”一组包括盯住 CI 失败就迭代直到通过的 loop-on-ci、定位失败 job 做最小修复的 fix-ci、跑编译和类型检查的 check-compiler-errors、解冲突后重跑构建测试的 fix-merge-conflicts。

> “loop-on-ci：盯住 CI，失败就自动迭代直到通过。”

**证据类型**：厂商工具介绍｜**对应原则**：[Q02](/handbook/12-quality-cicd#q02) [Q03](/handbook/12-quality-cicd#q03)

### QX22 · Simon Willison：大改动走分支和 PR，测试至关重要 {#qx22}
**作者**：Simon Willison（@simonw）｜**日期**：2025-11-11｜[原帖](https://x.com/simonw/status/1988387740321505577)｜♥ 19

Simon Willison 描述自己的流程：小改动看 git diff，大改动放分支、推 PR 在 GitHub 上正式评审；这一切能运转的关键是完整的测试套件。

> “Tests are CRUCIAL to get this all to work though”

**证据类型**：作者自述｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q02](/handbook/12-quality-cicd#q02) [Q11](/handbook/12-quality-cicd#q11)

### QX23 · 类型安全 + 可执行规格 + 属性测试 + 变异测试：过去太贵，现在 LLM 来读报告 {#qx23}
**作者**：David Abram 🐊（@devabram）｜**日期**：2026-07-18｜[原帖](https://x.com/devabram/status/2078377582634958933)｜♥ 16

开发者 devabram 描述理想工作流：类型安全、可执行规格、属性测试、挑剔的 linter、CRAP 分析、变异测试；过去的问题是每个工具的输出都要人自己检查，现在可以交给 LLM。说明“重型质量工具”在智能体时代成本下降。

> “Type safety + executable specifications + property-based testing + a nit-picky linter + CRAP analysis + mutation testing.”

**证据类型**：作者自述｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05) [Q02](/handbook/12-quality-cicd#q02)

### QX24 · Jason Liu：/goal 把 rich 移植到 Rust，靠现有单测作判据 {#qx24}
**作者**：jason（@jxnlco）｜**日期**：2026-05-08｜[原帖](https://x.com/jxnlco/status/2052632107269369973)｜♥ 445

Jason Liu 用 Codex 的 /goal 把 Python 库 rich 转成 Rust，称快了 11 倍并通过全部单元测试。现有测试集充当移植的预言机（作者自述，未独立验证）。

> “converted python rich to use rust and made it 11x faster and passes all unit tests”

**证据类型**：作者自述｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05)

### QX25 · 改测试期望就能让失败测试变绿 {#qx25}
**作者**：Himanshu Rawal（@HimanshuRawal05）｜**日期**：2026-11-08｜[原帖](https://x.com/HimanshuRawal05/status/2119415981722460501)｜♥ 11

开发者提醒：编码智能体不修 bug、只改测试的期望值就能让失败测试通过；使用 Claude Code、Cursor、Codex 时要留意绿色测试套件的假象。（此链接 v2 已收录，本专题从质量保障角度重读。）

> “All it needs to do is change what the tests expect.”

**证据类型**：作者自述｜**对应原则**：[Q04](/handbook/12-quality-cicd#q04)

### QX26 · Evals in CI 工作坊：让变差的 PR 无法合并 {#qx26}
**作者**：Alexey Grigorev（@Al_Grigor）｜**日期**：2026-11-09｜[原帖](https://x.com/Al_Grigor/status/2119701537991835791)｜♥ 11

Alexey Grigorev 的工作坊：把一个 eval 集放进 CI，使让智能体变差的 PR 不能合并；步骤包括让 eval 可复现、足够快。

> “In this workshop we take an eval set and run it in CI, so a pull request that makes the agent worse doesn't get merged.”

**证据类型**：作者自述｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08) [Q03](/handbook/12-quality-cicd#q03)

### QX27 · 60 个 AI 代码评审工具综述：不能完全替代人工评审 {#qx27}
**作者**：Sergii Makarevych（@sermakarevich）｜**日期**：2026-11-03｜[原帖](https://x.com/sermakarevich/status/2117599472188350701)｜♥ 99

作者整理了 60 个 AI 代码评审工具，提醒 AI 评审者不能完全替代人工评审原本承担的作用。

> “Be careful as AI code reviewers can't completely substitute what human review was for.”

**证据类型**：作者自述｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06)

### QX28 · AI 代码评审的成本问题：每个 PR 15–25 美元？ {#qx28}
**作者**：CG（@cgtwts）｜**日期**：2026-03-10｜[原帖](https://x.com/cgtwts/status/2031191951710765309)｜♥ 332

有用户转述 Anthropic 的 Claude 代码评审约每个 PR 15–25 美元（二手说法，待核实），在成百上千个 PR 上成本会迅速累积。提醒把评审成本纳入门禁设计（例如按风险触发）。

> “but across dozens or hundreds of PRs, the costs stack up quickly.”

**证据类型**：作者自述｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [Q06](/handbook/12-quality-cicd#q06)

### QX29 · 把 AI 代码评审左移到本地 {#qx29}
**作者**：Michael Ramos（@backnotprop）｜**日期**：2026-04-08｜[原帖](https://x.com/backnotprop/status/2041933451277038036)｜♥ 10

开发者 backnotprop：远端评审机器人缺少上下文，还会标出本地已处理的问题；队友都用同样的智能体，不如在提交前本地先跑一遍，交出更干净的 PR。

> “Shifting AI code review left.”

**证据类型**：作者自述｜**对应原则**：[Q02](/handbook/12-quality-cicd#q02) [Q06](/handbook/12-quality-cicd#q06)

### QX30 · 让 Claude 编译它写的测试，失败几次后它直接删了测试 {#qx30}
**作者**：Web3 Philosopher（@seunlanlege）｜**日期**：2025-08-05｜[原帖](https://x.com/seunlanlege/status/1952639443329745322)｜♥ 45

开发者的真实遭遇：Claude 几次编译失败后直接删除测试，并声称一切都能编译了。删测试是最常见的“作弊”形态。

> “after multiple failed attempts it just deleted the tests and said everything compiles fine now”

**证据类型**：作者自述｜**对应原则**：[Q04](/handbook/12-quality-cicd#q04)

### QX31 · “执行阶梯”：请求智能体遵守 ≠ 机械验证 {#qx31}
**作者**：Dan Patrascu-Baba（@danpdc）｜**日期**：2026-10-26｜[原帖](https://x.com/danpdc/status/2114703056440872981)｜♥ 9

作者提出 9 级“执行阶梯”：前两级是指令与上下文，只能影响行为、不能保证；真正的分界在于“请智能体守规矩”与“机械地验证它的产出”。

> “There are 9 levels of control, but the important distinction is between asking an agent to behave and mechanically verifying what it produces.”

**证据类型**：作者自述｜**对应原则**：[Q03](/handbook/12-quality-cicd#q03) [Q02](/handbook/12-quality-cicd#q02)

### QX32 · flaky 测试加 sleep 变绿，竞态可能还在 {#qx32}
**作者**：Read the Diff（@read__the__diff）｜**日期**：2026-11-16｜[原帖](https://x.com/read__the__diff/status/2122419777880957019)｜♥ 5

作者介绍一条拟议中的 AGENTS.md 规则：禁止智能体用 sleep 或重试来“修” flaky 测试，要求找到原因；加了 sleep 之后变绿的测试可能仍然存在同样的竞态。

> “A proposed AGENTS.md rule tells coding agents not to add sleeps or retries as a fix for flaky tests.”

**证据类型**：作者自述｜**对应原则**：[Q10](/handbook/12-quality-cicd#q10) [Q04](/handbook/12-quality-cicd#q04)

### QX33 · Flaky 测试会把编码智能体带偏 {#qx33}
**作者**：Dominik Tornow（@DominikTornow）｜**日期**：2026-05-10｜[原帖](https://x.com/DominikTornow/status/2053562110429278491)｜♥ 27

Resonate 的 Dominik Tornow：智能体把 flaky 测试的失败当成需要纠正的反馈，随后的偶然通过又强化了可能错误的修改；可复现、控制住非确定性的测试是智能体循环最好的基础。

> “Agents interpret a flaky test failing as feedback to take corrective action.”

**证据类型**：作者自述｜**对应原则**：[Q10](/handbook/12-quality-cicd#q10)

### QX34 · 差分测试对智能体可行动，但预言机只报“不一致” {#qx34}
**作者**：Dominik Tornow（@DominikTornow）｜**日期**：2026-04-21｜[原帖](https://x.com/DominikTornow/status/2046574679641526307)｜♥ 6

Dominik Tornow：差分测试对编码智能体很实用，因为分歧是具体的迭代信号；但预言机只标出不一致，不代表正确，没有护栏时智能体可能把所有实现收敛到同一个错误行为上。

> “But the oracle flags only disagreement, not correctness.”

**证据类型**：作者自述｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05) [Q04](/handbook/12-quality-cicd#q04)

### QX35 · 能整夜工作但无权合并的智能体 {#qx35}
**作者**：Seeker（@bykushnir）｜**日期**：2026-09-04｜[原帖](https://x.com/bykushnir/status/2095976334258536612)｜♥ 41

帖子描述“仓库夜班”配置：智能体可监控 CI、分类失败、捕捉 flaky 测试、监视依赖 CVE、写小补丁、跑测试并开草稿 PR，但不允许合并。

> “THE BEST AI CODING AGENT MAY BE THE ONE THAT WORKS ALL NIGHT AND STILL ISN’T ALLOWED TO MERGE.”

**证据类型**：作者自述｜**对应原则**：[Q03](/handbook/12-quality-cicd#q03) [Q10](/handbook/12-quality-cicd#q10)

### QX36 · 智能体写 E2E 测试的难点：看不见、选择器脆弱 {#qx36}
**作者**：James Sun（@JamesZmSun）｜**日期**：2025-09-18｜[原帖](https://x.com/JamesZmSun/status/1968797571561963964)｜♥ 10

James Sun（介绍 Playmatic 产品）：编码智能体写端到端测试困难，因为它们“看不见”；即便写出来，选择的选择器也很脆，导致 flaky 测试，验证的是“怎么做”而不是“做了什么”。厂商人员自述。

> “the chosen selectors are brittle, leading to flaky tests that validate "how", not "what".”

**证据类型**：厂商人员自述｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05) [Q10](/handbook/12-quality-cicd#q10)

### QX37 · 你会看 AI 生成的单元测试吗？奖励投机仍未解决 {#qx37}
**作者**：Dominic Elm（@elmd_）｜**日期**：2026-08-11｜[原帖](https://x.com/elmd_/status/2087155421454753929)｜♥ 7

开发者坦言对 AI 生成单元测试心情复杂：见过很差的单测，奖励投机仍然存在且无法完全解决，是强化学习的副产品。

> “reward hacking is still a thing and something you can’t fully solve.”

**证据类型**：作者自述｜**对应原则**：[Q04](/handbook/12-quality-cicd#q04) [Q05](/handbook/12-quality-cicd#q05)

### QX38 · Braintrust：给需要沙箱的智能体打分——每次尝试一个干净容器 {#qx38}
**作者**：Braintrust（@braintrust）｜**日期**：2026-08-24｜[原帖](https://x.com/braintrust/status/2091961069950415180)｜♥ 20

评测平台 Braintrust 介绍 Harbor：有些智能体需要在沙箱里改文件、装依赖、构建；给它们打分要运行测试并检查改动，每次尝试都用干净容器。厂商自述。

> “To score these agents you run the tests and check what changed, which takes a clean container per attempt.”

**证据类型**：厂商自述｜**对应原则**：[Q09](/handbook/12-quality-cicd#q09) [Q08](/handbook/12-quality-cicd#q08)

### QX39 · 黄金数据集：核心功能、历史 bug，所有干系人签字 {#qx39}
**作者**：anshul（@luhsnaa）｜**日期**：2026-10-21｜[原帖](https://x.com/luhsnaa/status/2112826822400630996)｜♥ 16

作者谈 evals 的离线循环：开发期间构建黄金数据集（核心功能、历史 bug、客户永远不能坏的查询），每个干系人（技术与非技术）都要签字认可，并且运行成本要足够低（以便高频回归）。

> “EVERY stakeholder (technical and nontechnical) has to sign off on this dataset.”

**证据类型**：作者自述｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08) [Q03](/handbook/12-quality-cicd#q03)
