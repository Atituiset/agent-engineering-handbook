# 独立工程师与意见领袖

> 一线资深工程师的个人博客与公开演讲：Simon Willison、Kent Beck、Armin Ronacher、Mitchell Hashimoto、Steve Yegge、Addy Osmani、Harper Reed、Geoffrey Huntley、Andrej Karpathy 等。均为 **「作者自述的个人经验」**，不是对照实验。链接于 2026-11-18 核对。

[[toc]]

## Simon Willison

### PR01 · Here’s how I use LLMs to help me write code {#pr01}
**作者**：Simon Willison｜**日期**：2025-03-11｜[原文](https://simonwillison.net/2025/Mar/11/using-llms-for-code/)

一份系统的个人方法论：设定合理预期（把 LLM 当作过度自信的结对伙伴）、注意训练截止日期、上下文为王、让它给出多个选项、对生产代码像对待「数字实习生」那样明确指令、**你必须测试它写的东西**、坏的初次结果是起点而非失败、做好随时接手的准备。

> "a bad initial result isn’t a failure, it’s a starting point for pushing the model in the direction of the thing you actually want."

### PR02 · Vibe engineering {#pr02}
**作者**：Simon Willison｜**日期**：2025-10-07｜[原文](https://simonwillison.net/2025/Oct/7/vibe-engineering/)

为「资深专业人员借助 LLM 加速、同时对产出完全负责」的那一端起名 vibe engineering，以区别于不看代码的 vibe coding。列出让智能体更高效的工程实践：自动化测试、提前计划、完善文档、良好的版本控制习惯、有效的自动化、代码评审文化、手工 QA、研究能力、预览环境、知道该外包什么——这些本来就是优秀工程实践，在智能体时代回报更高。

### PR03 · Embracing the parallel coding agent lifestyle {#pr03}
**作者**：Simon Willison｜**日期**：2025-10-05｜[原文](https://simonwillison.net/2025/Oct/5/parallel-coding-agents/)

作者起初怀疑并行跑多个智能体——瓶颈是人审查结果的速度。后来找到适合并行的任务：调研/原型、理解现有系统如何工作、小型维护任务、以及事先规格写得很清楚的工作；评审负担较轻的任务更适合并行。

### PR04 · Your job is to deliver code you have proven to work {#pr04}
**作者**：Simon Willison｜**日期**：2025-12-18｜[原文](https://simonwillison.net/2025/Dec/18/code-proven-to-work/)

批评把大量未经验证的 AI 代码甩给评审者的做法。证明代码可用需要两步：**手工测试**（亲眼看到它工作，最好附上过程记录）与**自动化测试**；编码智能体也应被引导去证明自己的改动有效。责任在提交者，而不是评审者。

> "Your job is to deliver code you have proven to work."

### PR05 · Context engineering {#pr05}
**作者**：Simon Willison｜**日期**：2025-06-27｜[原文](https://simonwillison.net/2025/Jun/27/context-engineering/)

赞同用「context engineering」取代「prompt engineering」：后者常被误解为「在聊天框里打字」，而前者准确描述了为模型精心组织上下文这项工程工作。

### PR06 · Claude Skills are awesome, maybe a bigger deal than MCP {#pr06}
**作者**：Simon Willison｜**日期**：2025-10-16｜[原文](https://simonwillison.net/2025/Oct/16/claude-skills/)

Skills 的简洁性是其力量所在：只是 Markdown 加可选脚本，开头只占用很少 token，按需加载；依赖于智能体拥有代码执行环境。作者认为它可能比 MCP 更具影响力。

### PR07 · Agentic Engineering Patterns（系列导言） {#pr07}
**作者**：Simon Willison｜**日期**：2026-02-23｜[原文](https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/)

仿照《设计模式》的章节体例，系统整理「专业工程师用编码智能体放大自身能力」的模式。定义 agentic engineering：使用既能生成又能执行代码的智能体，从而能独立测试与迭代。以下 PR08–PR13 为该系列中与本手册最相关的章节。

### PR08 · Writing code is cheap now {#pr08}
**作者**：Simon Willison｜**日期**：2026｜[原文](https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/)

最大挑战是适应「写代码变便宜了」：我们许多宏观（设计、估算、计划）与微观习惯都建立在代码昂贵的前提上。但「好代码」仍然昂贵——能工作、**我们知道它能工作**、解决正确的问题、优雅处理错误、简单最小、有测试保护、文档与现状一致、设计允许未来变更（同时坚持 YAGNI）、满足各种非功能质量。

### PR09 · Red/green TDD {#pr09}
**作者**：Simon Willison｜**日期**：2026｜[原文](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/)

「Use red/green TDD」是让编码智能体写出更精简可靠代码的一句简洁提示：先写测试、确认失败（红）、再实现到通过（绿）。它同时防住两类常见错误：写出不工作的代码、写出不必要且从未被使用的代码；确认「先失败」这一步不能省，否则测试可能本来就会通过。

### PR10 · First run the tests {#pr10}
**作者**：Simon Willison｜**日期**：2026｜[原文](https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/)

与智能体在已有项目开新会话时，先让它「跑一下测试」：这告诉它存在测试套件并迫使它搞清如何运行，使它之后几乎必然会用测试检查改动；测试数量也暗示了项目规模；并让它进入「测试心态」。作者认为「写测试太费时」的老借口在智能体时代已不成立。

### PR11 · Subagents {#pr11}
**作者**：Simon Willison｜**日期**：2026｜[原文](https://simonwillison.net/guides/agentic-engineering-patterns/subagents/)

上下文上限多年未显著增长（通常上限约 100 万 token，且基准常显示 20 万以下质量更好），子智能体用全新上下文完成子任务，保护主上下文。可并行（如批量更新受影响模板）也可专门化（评审者、测试运行者、调试者）。提醒不要过度拆分：子智能体的主要价值是保护根上下文与处理 token 密集操作。

### PR12 · Anti-patterns: things to avoid {#pr12}
**作者**：Simon Willison｜**日期**：2026｜[原文](https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/)

头号反模式是**把未经审查的代码强加给协作者**：如果你提交了智能体产出的成百上千行代码却没做过确保其可用的工作，就是把真正的工作转嫁给评审者。好的 PR 应该：作者已确认可用、足够小以便高效评审（几个小 PR 胜过一个大 PR）、附带说明上下文与验证证据。

### PR13 · Agentic manual testing {#pr13}
**作者**：Simon Willison｜**日期**：2026｜[原文](https://simonwillison.net/guides/agentic-engineering-patterns/agentic-manual-testing/)

编码智能体相对普通 LLM 的核心优势是能执行代码验证自己的产出。除了自动化测试，还应让智能体做「手工测试」——测试全过不代表能用：用 `python -c` 试边界情况、用 curl 探索 JSON API、用 Playwright 等浏览器自动化测 Web UI；发现问题后把新情况补进永久的自动化测试。

### PR14 · AI should help us produce better code {#pr14}
**作者**：Simon Willison｜**日期**：2026｜[原文](https://simonwillison.net/guides/agentic-engineering-patterns/better-code/)

如果采用智能体明显降低了代码质量，应直接解决那个问题。以技术债的视角看：过去因成本放弃的「正确做法」（重构、补测试、改名、拆分）现在可以交给智能体；AI 也让我们能用原型考虑更多方案；并引用 Every 的「复利工程（Compound Engineering）」——每个项目结束做复盘，把学到的东西沉淀回智能体指令。

## Kent Beck

### PR15 · Augmented Coding: Beyond the Vibes {#pr15}
**作者**：Kent Beck｜**日期**：2025｜[原文](https://tidyfirst.substack.com/p/augmented-coding-beyond-the-vibes)

用「增强编码」完成一个 B+ 树库（Rust 与 Python）。区分 vibe coding（只关心行为）与 augmented coding（关心代码、复杂度、测试与覆盖率）。他的系统提示要求严格 TDD：先写定义一小步功能的失败测试，结构性变更与行为性变更分开提交并在提交信息中注明；同时警惕「精灵」作弊的迹象，例如禁用或删除测试。

> "In vibe coding you don't care about the code, just the behavior of the system."

### PR16 · Trust Is the Binding Constraint {#pr16}
**作者**：Kent Beck｜**日期**：2026-10-30｜[原文](https://newsletter.kentbeck.com/p/trust-is-the-binding-constraint)

团队积累代码的速度快于积累信任的速度，「没有信任的代码」正是项目失败之处。信任积累缓慢而瞬间蒸发；XP 价值观（沟通、简单、反馈、勇气、尊重）本质上是「制造信任的系统」。他特别警告：AI 倾向大批量，而信任需要小而经验证的步骤；人人都会被推向「单人 AI 开发」，这是巨大的错误。

> "AI wants big batches, trust wants small verified steps."

## Armin Ronacher

### PR17 · Agentic Coding Recommendations {#pr17}
**作者**：Armin Ronacher（Flask 作者）｜**日期**：2025-06-12｜[原文](https://lucumr.pocoo.org/2025/6/12/agentic-coding/)

个人实践：保持简单——自定义工具就是智能体可以直接运行的普通脚本，很少用 MCP；新后端项目推荐 Go（上下文传递显式、测试运行直接增量、生态稳定），而智能体有时会搞错 Rust 的 `cargo test` 调用方式；让开发服务器日志对智能体可见；写简单、显式、少魔法的代码，并让工具快速、输出清晰、对误用有防护。

### PR18 · Tools: Code Is All You Need {#pr18}
**作者**：Armin Ronacher｜**日期**：2025-07-03｜[原文](https://lucumr.pocoo.org/2025/7/3/tools/)

质疑 MCP 的可组合性与 token 成本：与其给模型一堆工具，不如让它写代码（脚本）来完成任务——代码可复用、可审查、可以不经推理重复执行。作者很喜欢 Claude Code 在写代码过程中顺手生成的小工具。

### PR19 · Agent Design Is Still Hard {#pr19}
**作者**：Armin Ronacher｜**日期**：2025-11-21｜[原文](https://lucumr.pocoo.org/2025/11/21/agents-are-hard/)

自建智能体的经验：高层 SDK 的抽象在真实工具调用面前会破裂，模型间差异大到需要自己驱动智能体循环；缓存控制、强化提示、工具提示与供应商端工具等细节决定了抽象是否合适；测试与评测依然困难。

### PR20 · Fast and Hard Code {#pr20}
**作者**：Armin Ronacher｜**日期**：2026-08-22｜[原文](https://lucumr.pocoo.org/2026/8/22/fast-hard-code/)

观察到 LLM 让语言选择的后果变小：熟悉一门语言的成本不再重要，对人有意义的部分摩擦对智能体不复存在，人们甚至可以让智能体用自己完全不熟悉的语言写代码；同时出现了追求「快而小」的软件的风潮，因为 LLM 擅长在不改变行为的前提下优化代码。

## Mitchell Hashimoto

### PR21 · Vibing a Non-Trivial Ghostty Feature {#pr21}
**作者**：Mitchell Hashimoto（HashiCorp 联合创始人、Ghostty 作者）｜**日期**：2025-10-11｜[原文](https://mitchellh.com/writing/non-trivial-vibing)

完整记录用智能体实现 Ghostty 一个非平凡功能的过程：先自己做 AI 之前的规划；经常让智能体出方案后**整体丢弃并重来**；在关键处自己写骨架（描述性函数名、参数、TODO 注释）再让智能体填充；最后人工清理代码，以便自己理解并「教育未来读这段代码的智能体」。智能体特别擅长生成测试与模拟代码。

### PR22 · My AI Adoption Journey {#pr22}
**作者**：Mitchell Hashimoto｜**日期**：2026-02-05｜[原文](https://mitchellh.com/writing/my-ai-adoption-journey)

六步采纳路径：放弃聊天机器人改用智能体 → 用智能体重做自己已完成的工作以校准预期 → 下班前布置「日终智能体」 → 把有把握的「灌篮」任务外包 → **构建 harness** → 始终有一个智能体在跑。第五步的要点：最可靠的办法是给智能体快速、高质量的工具，自动告诉它哪里错了。

> "The most sure-fire way to achieve this is to give the agent fast, high quality tools to automatically tell it when it is wrong."

## Steve Yegge

### PR23 · Revenge of the junior developer {#pr23}
**作者**：Steve Yegge（Sourcegraph）｜**日期**：2025-03-22｜[原文](https://sourcegraph.com/blog/revenge-of-the-junior-developer)

描绘从补全、聊天到智能体、再到「智能体舰队」的演进，预言开发者角色转向管理和编排多个智能体；拥抱新工具的初级开发者可能比抗拒的资深开发者更有优势。文风夸张，应作为趋势判断而非方法论阅读。

### PR24 · The death of the stubborn developer {#pr24}
**作者**：Steve Yegge｜**日期**：2024-12-10｜[原文](https://sourcegraph.com/blog/the-death-of-the-stubborn-developer)

前一篇的前传：提出「chat-oriented programming（CHOP）」，认为拒绝采用 AI 的资深开发者会被淘汰。观点激进，代表了 2024–2025 年「乐观派」的典型论调。

### PR25 · Beads：a memory upgrade for your coding agent {#pr25}
**作者**：Steve Yegge｜**日期**：持续更新｜[原文](https://github.com/steveyegge/beads)

把任务/问题追踪做成智能体友好的、基于 git 的图结构，让智能体跨会话记住待办、依赖与发现，替代散乱的 Markdown 计划文件。（仓库现位于 gastownhall 组织下。）

## Addy Osmani

### PR26 · The 70% problem: Hard truths about AI-assisted coding {#pr26}
**作者**：Addy Osmani｜**日期**：2024-12-04｜[原文](https://addyo.substack.com/p/the-70-problem-hard-truths-about)

AI 能很快带你完成约 70%，但剩下的 30%（边界情况、可维护性、安全、生产就绪）依然困难，而这恰恰需要工程经验；资深工程师从 AI 中获益更多，因为他们知道如何引导与纠错，初学者则容易陷入「修一个 bug 冒出两个」的循环。

### PR27 · My LLM coding workflow going into 2026 {#pr27}
**作者**：Addy Osmani｜**日期**：2026-01-04｜[原文](https://addyosmani.com/blog/ai-coding-workflow/)

先写规格与计划、小块迭代、给足相关上下文（需要哪几个模块就给哪几个）、用规则文件写清风格约定、让测试与自动化检查兜底、频繁提交以便回退、**只合并自己理解了的代码**、把每次会话当作学习机会。

> "Scope management is everything - feed the LLM manageable tasks, not the whole codebase at once."

### PR28 · How to write a good spec for AI agents {#pr28}
**作者**：Addy Osmani｜**日期**：2026-01-13｜[原文](https://addyosmani.com/blog/good-spec/)

规格要「刚好够用」：覆盖结构、风格、测试与边界，但不要压垮模型的注意力预算；把规格当作有清晰章节的 PRD；长规格拆分成多个文件；让智能体把规格与计划拆成可单独实现和测试的小任务；明确「总是 / 先问 / 绝不」三级边界；简单孤立的任务不需要厚重规格。

## Harper Reed、Geoffrey Huntley、Jesse Vincent

### PR29 · My LLM codegen workflow atm {#pr29}
**作者**：Harper Reed｜**日期**：2025-02-16｜[原文](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/)

广为流传的绿地项目工作流：用对话模型「一次问一个问题」打磨想法形成 `spec.md` → 用推理模型生成分步、每步可测的提示计划 `prompt_plan.md` 与 `todo.md` → 交给编码智能体逐步执行。存量代码则先打包上下文再做小任务。

> "Brainstorm spec, then plan a plan, then execute using LLM codegen. Discrete loops."

### PR30 · Basic Claude Code {#pr30}
**作者**：Harper Reed｜**日期**：2025-05-08｜[原文](https://harper.blog/2025/05/08/basic-claude-code/)

把上一篇工作流迁移到 Claude Code，并承认自己曾是「TDD 反对者」但现在把测试作为核心；建议把 lint、格式化、测试放进 pre-commit hook，让智能体在提交时自动被纠正。

### PR31 · Ralph Wiggum as a "software engineer" {#pr31}
**作者**：Geoffrey Huntley｜**日期**：2025-07-14｜[原文](https://ghuntley.com/ralph/)

「Ralph」技术的纯粹形式就是一个 bash 循环：`while :; do cat PROMPT.md | claude-code ; done`。配合规格文件、计划文件与强反馈（编译器、测试），让智能体在循环中持续推进绿地项目；作者用「给 Ralph 立路标」比喻人需要不断调整提示来纠正缺陷，并明确表示绝不会在已有代码库上用 Ralph——它只适合绿地项目。

### PR32 · You are using Cursor AI incorrectly… {#pr32}
**作者**：Geoffrey Huntley｜**日期**：2025-02-08｜[原文](https://ghuntley.com/stdlib/)

批评常见用法：提示欠规格、只会说「请实现 XYZ」。主张构建一个「规则标准库」（stdlib）：让智能体把每次学到的约定写成规则文件，逐步积累，再配合有健全类型系统和编译器报错的语言，驱动高产出。

### PR33 · Superpowers: How I'm using coding agents in October 2025 {#pr33}
**作者**：Jesse Vincent｜**日期**：2025-10-09｜[原文](https://blog.fsck.com/2025/10/09/superpowers/)

介绍 Superpowers skills 库（见 [OS08](./open-source#os08)）：默认在实现前先与人讨论计划（brainstorm → plan → implement），把 TDD、系统化调试、代码评审等写成强制性技能，并利用说服心理学原则（权威、承诺）提高智能体遵守技能的概率。

## 其他

### PR34 · Andrej Karpathy: Software Is Changing (Again) {#pr34}
**作者**：Andrej Karpathy｜**日期**：2025-06-17 演讲（视频 2025-06-18 发布）｜[原文](https://www.youtube.com/watch?v=LCEmiRjPEtQ)

在 YC AI Startup School 的主题演讲，提出 Software 3.0（用自然语言编程）、LLM 是「有缺陷的人类精神」、应构建「部分自主」的产品并让人保持对生成-验证回路的掌控（类似钢铁侠战衣的「自主滑块」），强调把 AI「拴在短绳上」、加快验证速度。

### PR35 · The New Skill in AI is Not Prompting, It's Context Engineering {#pr35}
**作者**：Philipp Schmid（Google DeepMind）｜**日期**：2025-06-30｜[原文](https://www.philschmid.de/context-engineering)

把上下文拆解为系统指令、用户提示、短期状态/历史、长期记忆、检索信息、可用工具与结构化输出，主张「大多数智能体失败不是模型失败，而是上下文失败」。

### PR36 · How Long Contexts Fail {#pr36}
**作者**：Drew Breunig｜**日期**：2025-06-22｜[原文](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html)

长上下文的四种失败模式：**上下文中毒**（幻觉进入上下文被反复引用）、**上下文分心**（上下文压过训练知识）、**上下文混淆**（无关内容影响回答）、**上下文冲突**（上下文内部互相矛盾）。为「为什么规则写多了反而更不听话」提供了很好的解释词汇。
