# X 精选 · Hooks、Skills、子智能体与 MCP

> 42 条精选帖子，按发帖日期（UTC）排序。每条都有原帖链接；摘要忠于原文，引文为原帖逐字摘录。**作者自述**为个人经验，厂商员工谈自家产品时请视为**厂商自报**。原则标签为关键词自动归类，见 [共识度/佐证](/compare/evidence)。

[[toc]]

### XT-001 · 子代理工作流支撑连续 4 小时的大规模类型修复 {#xt-001}
**作者**：Jeffrey Emanuel（@doodlestein）｜**日期**：2025-06-25｜[原帖](https://x.com/doodlestein/status/1937729842172047679)｜♥ 64

Jeffrey Emanuel 用 Claude Code 子代理修复 10 万多行 Python 中 mypy 报出的全部类型问题，连续运行 4 小时以上、消耗超过一百万 token，他认为这只有依靠子代理工作流才能做到。作者自述。

> "This is only possible because the sub-agent workflows"

原则：[P02](/compare/evidence#p02) [P06](/compare/evidence#p06) [P09](/compare/evidence#p09) [P10](/compare/evidence#p10) [P11](/compare/evidence#p11)

### XT-002 · Hooks：把「请记得做」变成「一定会执行」 {#xt-002}
**作者**：Rohan Paul（@rohanpaul_ai）｜**日期**：2025-07-01｜[原帖](https://x.com/rohanpaul_ai/status/1939910693106639061)｜♥ 39

Rohan Paul 介绍 Claude Code 推出 Hooks：在会话关键时刻自动运行的 shell 脚本，把非正式的聊天指令变成必定触发的命令，使格式化、日志和安全检查不再依赖模型记得提示词。

> "so formatting, logging, or safety checks never depend on the model remembering a prompt"

原则：[P02](/compare/evidence#p02) [P04](/compare/evidence#p04) [P12](/compare/evidence#p12) [P15](/compare/evidence#p15)

### XT-003 · 需要只读子智能体：收集上下文的子智能体常常忍不住动手改文件 {#xt-003}
**作者**：Yaya Soumah（@YayaSoumah）｜**日期**：2025-07-18｜[原帖](https://x.com/YayaSoumah/status/1946213029802369529)｜♥ 22

Yaya Soumah 建议 Claude Code 提供只读版本的子智能体：本应只收集上下文的子智能体常常「热情过度」自己去改文件，导致主实例的状态混乱。

> "Claude Code should make a version of the sub agent that is READ-ONLY."

原则：[P02](/compare/evidence#p02) [P10](/compare/evidence#p10) [P11](/compare/evidence#p11)

### XT-004 · 用子智能体搭复杂系统：用命令把子智能体串起来以求可靠 {#xt-004}
**作者**：elvis（@omarsar0）｜**日期**：2025-07-26｜[原帖](https://x.com/omarsar0/status/1949204315350216789)｜♥ 1301

elvis 演示用 Claude Code 子智能体构建多智能体深度研究系统，并建议用斜杠命令把子智能体串起来以提高可靠性。

> "Chain subagents with /commands for reliability."

原则：[P10](/compare/evidence#p10) [P11](/compare/evidence#p11)

### XT-005 · 用 hook 按需追加「ultrathink」 {#xt-005}
**作者**：Mckay Wrigley（@mckaywrigley）｜**日期**：2025-08-04｜[原帖](https://x.com/mckaywrigley/status/1952466679239524624)｜♥ 1568

Mckay Wrigley 建议为 Claude Code 写一个 hook：请求以「-u」结尾时自动加上「ultrathink」提示，以便按需提高推理投入。说明 hooks 也可用来做提示层面的确定性改写。

> "Everyone should create a hook for Claude Code that adds an “ultrathink” prompt to requests ending in “-u”."

原则：[P12](/compare/evidence#p12)

### XT-006 · Agent Habitats：执行环境与模型同样重要 {#xt-006}
**作者**：Amjad Masad（@amasad）｜**日期**：2025-12-30｜[原帖](https://x.com/amasad/status/2005904266980905070)｜♥ 499

Replit CEO Amjad Masad 预测 2026 年人们会意识到「Agent Habitats」——代码执行、存储、计算机操作和工具——与模型本身同样重要；拼凑第三方服务可以做出漂亮演示，但长周期的实用智能体工作需要这些组件协同。厂商观点。

> "is as important as the model itself"

原则：[P06](/compare/evidence#p06) [P17](/compare/evidence#p17)

### XT-007 · Tool Search：按需加载工具定义 {#xt-007}
**作者**：Aakash Gupta（@aakashgupta）｜**日期**：2026-01-15｜[原帖](https://x.com/aakashgupta/status/2011664388424454262)｜♥ 599

Aakash Gupta 评论 Claude Code 的 Tool Search：不再预先加载全部工具定义，而是加载搜索索引、按需拉取工具。帖中引用的数据（7 个 MCP 服务器在输入前就消耗 67k token 等）为转述，属厂商与用户自报。

> "Instead of preloading every tool definition upfront"

原则：[P02](/compare/evidence#p02) [P05](/compare/evidence#p05) [P06](/compare/evidence#p06) [P14](/compare/evidence#p14) [P15](/compare/evidence#p15) [P18](/compare/evidence#p18)

### XT-008 · 一份 10 个月高强度使用的 Claude Code 工作流总结 {#xt-008}
**作者**：鳞片狗（@linpiangou）｜**日期**：2026-01-18｜[原帖](https://x.com/linpiangou/status/2012706087246475448)｜♥ 1

鳞片狗总结一份社区指南：作者把 Claude Code 配置模块化为规则、技能、命令和代理，形成分层治理；Skills 定义较大的工作流（如 /tdd、/refactor-clean），Commands 是可快速执行的提示词。内容为二手总结。

> "作者将 Claude Code 的配置模块化，分为规则、技能、命令和代理"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P04](/compare/evidence#p04) [P05](/compare/evidence#p05) [P06](/compare/evidence#p06) [P07](/compare/evidence#p07) [P08](/compare/evidence#p08) [P09](/compare/evidence#p09) [P10](/compare/evidence#p10) [P11](/compare/evidence#p11) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13) [P14](/compare/evidence#p14) [P15](/compare/evidence#p15) [P18](/compare/evidence#p18)

### XT-009 · Hooks 的有效用法：PreToolUse、PostToolUse、Stop {#xt-009}
**作者**：Shakthi（@v_shakthi）｜**日期**：2026-03-31｜[原帖](https://x.com/v_shakthi/status/2038869951541629338)｜♥ 0

Shakthi 解释 hooks 改变了「输入—回答—评审」的循环：它们是在会话生命周期特定节点自动触发的 shell 命令，PreToolUse 在 Claude 调用工具前触发，PostToolUse 在之后触发，Stop 在会话结束时触发。

> "Hooks are shell commands that fire automatically at specific lifecycle points"

原则：[P02](/compare/evidence#p02) [P04](/compare/evidence#p04) [P05](/compare/evidence#p05) [P06](/compare/evidence#p06) [P08](/compare/evidence#p08) [P12](/compare/evidence#p12)

### XT-010 · SKILL.md：用模块化、按需加载的指令对抗上下文膨胀 {#xt-010}
**作者**：tut\_ml（@tut_ml）｜**日期**：2026-04-01｜[原帖](https://x.com/tut_ml/status/2039308271560106464)｜♥ 377

作者指出很多人把所有指令塞进 CLAUDE.md 或 .cursorrules，导致每次启动都加载全部规则、浪费上下文和 token。他推荐 SKILL.md 思路：拆成小而专注的 skill 文件夹，只在当前任务需要时加载。

> "The problem is context bloat."

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P06](/compare/evidence#p06) [P08](/compare/evidence#p08) [P13](/compare/evidence#p13) [P14](/compare/evidence#p14)

### XT-011 · 社区整理的 claude-code-best-practice 指南 {#xt-011}
**作者**：sitin（@sitinme）｜**日期**：2026-04-12｜[原帖](https://x.com/sitinme/status/2043172254083629476)｜♥ 2242

博主 sitin 介绍 GitHub 项目 claude-code-best-practice：把 Claude Code 的技巧、工作流和配置模板系统整理，覆盖 Agents、Commands、Skills、Hooks、MCP、Subagents，并横向比较 Superpowers、Spec Kit 等工作流方案。帖中 Star 数与「86 条以上技巧」均为作者转述。

> "把 Claude Code 怎么用、怎么配置、怎么选工作流，全部整理成了一份系统化的指南"

原则：[P01](/compare/evidence#p01) [P10](/compare/evidence#p10) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13) [P14](/compare/evidence#p14) [P15](/compare/evidence#p15)

### XT-012 · 四个常用 Skill 项目：superpowers 强制「头脑风暴→规格→计划→执行」 {#xt-012}
**作者**：Suu（@Suu766）｜**日期**：2026-05-01｜[原帖](https://x.com/Suu766/status/2050145044594581653)｜♥ 102

Suu 推荐几个社区 Skill 项目，其中 superpowers 强制走「头脑风暴→规格→计划→执行（带审查）」流程，作者认为复杂任务不容易跑偏。项目功能与效果为作者转述。

> "强制走 “头脑风暴→规格→计划→执行（带审查）” 流程"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P08](/compare/evidence#p08) [P10](/compare/evidence#p10) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13) [P15](/compare/evidence#p15)

### XT-013 · 投资 harness 工程，比选哪个模型更重要 {#xt-013}
**作者**：StackBench（@stackbenchdev）｜**日期**：2026-05-06｜[原帖](https://x.com/stackbenchdev/status/2052002941884661792)｜♥ 3

StackBench 说常有人抱怨 Claude Code「笨」「啰嗦」「每次会话都丢上下文」，但花一个周末做 harness 工作——范围明确的 CLAUDE.md、为重复工作流写 skills、加入评审步骤——之后体验明显改善。作者经验。

> "it matters more than which model you pick."

原则：[P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P04](/compare/evidence#p04) [P06](/compare/evidence#p06) [P08](/compare/evidence#p08) [P10](/compare/evidence#p10) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13) [P17](/compare/evidence#p17)

### XT-014 · claude-code-setup：扫描项目后建议该开哪些 MCP、Skills、Hooks {#xt-014}
**作者**：Alvaro Cintas（@dr_cintas）｜**日期**：2026-05-20｜[原帖](https://x.com/dr_cintas/status/2057144795953262797)｜♥ 316

Alvaro Cintas 介绍 Anthropic 官方插件 claude-code-setup：扫描项目结构、依赖和代码模式，然后建议启用哪些 MCP（文档、Playwright）、Skills（Plan agent 等）、Hooks（自动格式化、自动 lint、屏蔽敏感文件）和子智能体。功能为作者转述。

> "Hooks (auto-format, auto-lint, block sensitive files)"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P04](/compare/evidence#p04) [P06](/compare/evidence#p06) [P08](/compare/evidence#p08) [P10](/compare/evidence#p10) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13) [P14](/compare/evidence#p14)

### XT-015 · 子代理：把 grep/读文件的噪声挡在主上下文之外 {#xt-015}
**作者**：蛋黄堡（@Hamburgerai）｜**日期**：2026-05-23｜[原帖](https://x.com/Hamburgerai/status/2058100482774839778)｜♥ 1

蛋黄堡推荐一篇关于 Claude Code 子代理的长文：会话变长后，主代理大量 grep、find、读文件的输出堆进上下文，变成噪声并稀释重要信息。子代理拥有独立上下文窗口和系统提示，主代理只收到最终总结；可在 .claude/agents/ 用 Markdown 定义并团队共享。

> "主代理只收到最终的总结结果，中间过程完全隔离，不污染主线程"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P05](/compare/evidence#p05) [P10](/compare/evidence#p10)

### XT-016 · Claude Code 的四层：CLAUDE.md、Skills、Hooks、子智能体 {#xt-016}
**作者**：Jian Wang（@jianw851）｜**日期**：2026-05-27｜[原帖](https://x.com/jianw851/status/2059688976366313532)｜♥ 196

Jian Wang 认为 Claude Code 不是终端聊天机器人，而是四层结构：CLAUDE.md 是持久的项目记忆，Skills 是会自动触发的可复用知识包，Hooks 是确定性的安全与自动化规则，子智能体拥有隔离的上下文。

> "deterministic safety + automation rules"

原则：[P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P04](/compare/evidence#p04) [P05](/compare/evidence#p05) [P10](/compare/evidence#p10) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13) [P15](/compare/evidence#p15) [P18](/compare/evidence#p18)

### XT-017 · claude-code-setup：扫描项目后建议 hooks、skills、MCP 和子代理 {#xt-017}
**作者**：超级个体｜柿子（@yaohui12138）｜**日期**：2026-05-28｜[原帖](https://x.com/yaohui12138/status/2059819859345825923)｜♥ 36

柿子介绍 Anthropic 官方插件 claude-code-setup：扫描项目后建议该配哪些 hooks、skills、MCP servers、子代理与自动化，并一步步帮你配置；例如用 hooks 在保存时自动跑测试、提交前自动格式化。安装量为作者转述的官方数据。

> "保存时自动跑测试、提交前自动格式化代码"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P04](/compare/evidence#p04) [P05](/compare/evidence#p05) [P06](/compare/evidence#p06) [P08](/compare/evidence#p08) [P10](/compare/evidence#p10) [P11](/compare/evidence#p11) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13) [P14](/compare/evidence#p14) [P15](/compare/evidence#p15)

### XT-018 · 嵌套子智能体：用「智能体启动智能体」管理上下文 {#xt-018}
**作者**：Boris Cherny（@bcherny）｜**日期**：2026-06-09｜[原帖](https://x.com/bcherny/status/2064327225504403752)｜♥ 5582

Boris Cherny 宣布 Claude Code 支持嵌套子智能体，深度先限制为 5，目的是让智能体启动智能体，以更好地管理上下文。厂商自报。

> "agents kicking off agents as a way to better manage context"

原则：[P02](/compare/evidence#p02) [P10](/compare/evidence#p10)

### XT-019 · 99% 的 MCP、功能和 skill 都是噪声 {#xt-019}
**作者**：Burke Holland（@burkeholland）｜**日期**：2026-06-11｜[原帖](https://x.com/burkeholland/status/2065134777162670585)｜♥ 198

GitHub Copilot 团队的 Burke Holland 认为，几乎所有 MCP、功能、skill 都是噪声，你不需要它们；只要学会你选定的 harness，使用内置功能即可。这是对「堆配置」的有力反对。

> "99% of every MCP, feature, skill, etc is pure noise."

原则：[P13](/compare/evidence#p13) [P14](/compare/evidence#p14)

### XT-020 · 有效的 Skills：窄、结构化、确定、可复用、省上下文 {#xt-020}
**作者**：Nick Babich（@101babich）｜**日期**：2026-06-17｜[原帖](https://x.com/101babich/status/2067200564610351597)｜♥ 10

Nick Babich 给出 Claude Code Skills 检查清单：skill 应像小而可重复的工作流，而不是巨大的指令堆；一个 skill 只做一件事，步骤化、确定性强，映射真实团队流程，并节省上下文。

> "Claude Code Skills work best when they are designed like small, repeatable workflows, not giant instruction dumps."

原则：[P02](/compare/evidence#p02) [P06](/compare/evidence#p06) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13)

### XT-021 · 子智能体不是「免费的并行工人」 {#xt-021}
**作者**：Aakash Gour（@AakashGourX）｜**日期**：2026-06-29｜[原帖](https://x.com/AakashGourX/status/2071516201617174928)｜♥ 3

Aakash Gour 不认同把 Claude Code 子智能体当成免费并行工人的看法。他的流程是：先让 Claude 写实施计划，人审查方案，再逐步执行，只在合适的地方使用子智能体。

> "Most people assume Claude Code sub-agents are basically "free parallel workers.""

原则：[P01](/compare/evidence#p01) [P08](/compare/evidence#p08) [P10](/compare/evidence#p10) [P11](/compare/evidence#p11)

### XT-022 · MCP 集成的几个阶段：从「全能协议」到工具路由层 {#xt-022}
**作者**：Ankur Gupta（@getpy）｜**日期**：2026-07-15｜[原帖](https://x.com/getpy/status/2077414587138552122)｜♥ 10

Ankur Gupta 戏称开发者接入 MCP 的阶段：起初觉得它能解决一切，然后被认证折磨，接着太多工具污染上下文、模型调错工具，最后自己加一层路由，只按提示注入相关工具子集。

> "Too many tools are polluting my context and LLM is invoking the wrong tool"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P05](/compare/evidence#p05) [P06](/compare/evidence#p06) [P14](/compare/evidence#p14) [P17](/compare/evidence#p17)

### XT-023 · 通用智能体 harness + CLI/MCP，胜过产品内置的问答框 {#xt-023}
**作者**：Mitchell Hashimoto（@mitchellh）｜**日期**：2026-07-16｜[原帖](https://x.com/mitchellh/status/2077788454860316915)｜♥ 2011

Mitchell Hashimoto 说在他用过的每个产品里，通用智能体 harness（Codex、Claude、OpenCode）加 CLI/MCP 都比产品内置的「随便问」聊天框好用，一大原因是可以用最新的前沿模型，另一个是能混合更多上下文。

> "Using a generic agent harness (e.g. Codex, Claude, OpenCode) + CLI/MCP is better than "Ask me anything" built-in product chat boxes"

原则：[P02](/compare/evidence#p02) [P14](/compare/evidence#p14)

### XT-024 · 模型越强，harness 应该越薄 {#xt-024}
**作者**：烟花老师（@teach_fireworks）｜**日期**：2026-07-26｜[原帖](https://x.com/teach_fireworks/status/2081298933457006792)｜♥ 2

作者读了 Claude Code 团队关于新模型的文章后反思 Codex 的用法：模型越强越值得给更多自主权，离模型越近的那层 harness 应该越薄，而工具层应该更丰富。属个人解读。

> "The closer you get to the model, the thinner your harness should become."

原则：[P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P04](/compare/evidence#p04) [P05](/compare/evidence#p05) [P06](/compare/evidence#p06) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13) [P15](/compare/evidence#p15) [P16](/compare/evidence#p16)

### XT-025 · 把 harness、上下文与行动空间与单一模型家族解耦 {#xt-025}
**作者**：Malte Ubl（@cramforce）｜**日期**：2026-07-27｜[原帖](https://x.com/cramforce/status/2081804273386664340)｜♥ 61

Vercel CTO Malte Ubl 赞同 Satya Nadella 的说法：把 harness、上下文/信号和行动空间与单一模型家族分开构建，结合专用模型、数据、智能体、工具、安全上下文和 harness，才能推进「单位结果成本」的前沿。

> "This is the benefit of building the harness, context/signals, and action space separate from one model family."

原则：[P02](/compare/evidence#p02) [P17](/compare/evidence#p17)

### XT-026 · 用 Claude 的 skill creator 做 skill：它会做测试、展示结果、反复征求反馈 {#xt-026}
**作者**：Ethan Mollick（@emollick）｜**日期**：2026-08-20｜[原帖](https://x.com/emollick/status/2090293321142874168)｜♥ 602

Ethan Mollick 认为如果在意细节，直接让 Claude 创建 skill 仍是做可复用 skill 的最好方式：ChatGPT 倾向于「变魔术」直接替你完成，而 Claude 会做测试、展示结果，并反复征求输入和反馈。

> "Claude does tests and shows results, repeatedly asking for input & feedback"

原则：[P06](/compare/evidence#p06) [P13](/compare/evidence#p13)

### XT-027 · 即时 harness：为长任务现场 vibe 一个专用 harness {#xt-027}
**作者**：eric zakariasson（@ericzakariasson）｜**日期**：2026-09-19｜[原帖](https://x.com/ericzakariasson/status/2101340036667191384)｜♥ 269

Eric Zakariasson 说做长周期项目时，他有时会临时写一个新的 harness 来支撑具体用例，例如让任务在虚拟机上运行并定期向他汇报。

> "i vibe code new harnesses to support the use case"

原则：[P16](/compare/evidence#p16) [P18](/compare/evidence#p18)

### XT-028 · 测一测你的 skill 或插件到底有没有让答案变好 {#xt-028}
**作者**：Addy Osmani（@addyosmani）｜**日期**：2026-09-21｜[原帖](https://x.com/addyosmani/status/2101921871092658655)｜♥ 1766

Addy Osmani 提醒 Claude Code 可以评测一个 skill 或插件是否真的改善了回答：在插件目录里描述好的结果长什么样，Claude 会写测试用例并运行评测。这是「skills 也需要验证」的工具支持。

> "Claude Code can test if a skill or plugin actually improves Claude's answers."

原则：[P06](/compare/evidence#p06) [P13](/compare/evidence#p13)

### XT-029 · Learn Harness Engineering：14 讲 8 个项目的开源课程 {#xt-029}
**作者**：Tech with Mak（@techNmak）｜**日期**：2026-10-16｜[原帖](https://x.com/techNmak/status/2111159344754745592)｜♥ 1139

Tech with Mak 推荐 Walking Labs 的开源课程，用 14 讲和 8 个实践项目讲如何构建更可靠的 AI 编码智能体，内容包括智能体指令（AGENTS.md/CLAUDE.md）、上下文管理与持久化等。

> "Agent instructions (AGENTS.md / CLAUDE.md)"

原则：[P02](/compare/evidence#p02) [P03](/compare/evidence#p03)

### XT-030 · 子智能体被滥用：并行不能替代深思熟虑的上下文管理 {#xt-030}
**作者**：dex（@dexhorthy）｜**日期**：2026-10-24｜[原帖](https://x.com/dexhorthy/status/2114117782111752262)｜♥ 513

dex 认为自 2025 年中以来子智能体被过度使用和滥用；它们在合适场景下杠杆很高，但社交媒体的热度鼓励越来越多的并行，而不是深思熟虑的上下文管理，这让普通用户吃了亏。这是对 P10/P11 的保留意见。

> "encouraging more and more parallelism instead of thoughtful context management"

原则：[P02](/compare/evidence#p02) [P10](/compare/evidence#p10) [P11](/compare/evidence#p11)

### XT-031 · 子智能体就像浏览器标签页 {#xt-031}
**作者**：Prasenjit Sarkar（@stretchcloud）｜**日期**：2026-10-24｜[原帖](https://x.com/stretchcloud/status/2114043492628381721)｜♥ 15

作者引用 Anthropic 文章中的一个比喻：子智能体基本上就是浏览器标签页——你打开一个去追一条支线，它在全新的上下文窗口中工作、不记得你刚才在做什么，最后把结果交回。

> "subagents are basically browser tabs"

原则：[P02](/compare/evidence#p02) [P10](/compare/evidence#p10) [P18](/compare/evidence#p18)

### XT-032 · 加子智能体之前先问：它解决什么问题？ {#xt-032}
**作者**：Addy Osmani（@addyosmani）｜**日期**：2026-10-27｜[原帖](https://x.com/addyosmani/status/2114967833708732607)｜♥ 1173

Addy Osmani 建议在增加子智能体前先问它解决什么问题，问题往往出在臃肿的系统提示；Skills 和工具搜索可以在不拆分上下文的情况下解决。他的经验法则是：只有在工作可并行、需要全新上下文等情况下才保留子智能体。

> "Before adding another subagent ask what problem it's solving. A bloated system prompt is often the issue."

原则：[P02](/compare/evidence#p02) [P10](/compare/evidence#p10) [P11](/compare/evidence#p11) [P13](/compare/evidence#p13)

### XT-033 · 智能体会不会只剩一个工具？Code Mode {#xt-033}
**作者**：Philipp Schmid（@_philschmid）｜**日期**：2026-11-02｜[原帖](https://x.com/_philschmid/status/2117278154918092817)｜♥ 398

Google 的 Philipp Schmid 回顾智能体工具的演进：从少量工具，到动态工具搜索，再到把一切收拢进「代码模式」；他撰文解释 Code Mode 的原理、为什么带类型的 JS/Python 沙箱可能优于直接用 bash。

> "We went from a handful of tools, to dynamic tool search, and now to collapsing everything into code mode."

原则：[P14](/compare/evidence#p14) [P15](/compare/evidence#p15)

### XT-034 · Agent 时代，Debug 基本功仍有门槛 {#xt-034}
**作者**：Barret李靖（@Barret_China）｜**日期**：2026-11-08｜[原帖](https://x.com/Barret_China/status/2119427366892257490)｜♥ 562

Barret李靖 认为 Agent as a Service 成为常态后，调试 Agent 会成为高频操作：执行太慢、效果差、太费钱、同样任务每次路径不同，都需要 Debug。关注点会从函数级性能分析扩展到「决策分析」，需要能看清执行全过程的工具。

> "AI 时代程序员的 Debug 基本功依然是一项有门槛的技能"

原则：[P02](/compare/evidence#p02) [P05](/compare/evidence#p05) [P13](/compare/evidence#p13)

### XT-035 · Skill 应在智能体遇到困难时被动创建，而不是预先堆 {#xt-035}
**作者**：Quinn Slack（@sqs）｜**日期**：2026-11-14｜[原帖](https://x.com/sqs/status/2121728182235881656)｜♥ 241

Amp 的 Quinn Slack 建议：skill 应该在智能体遇到困难时才创建，而不是预先准备；总要问智能体怎样能做得更好，答案往往不是 skill；最后让智能体评估你的 skill。

> "Skills should be made reactively when the agent struggles with something"

原则：[P13](/compare/evidence#p13)

### XT-036 · 用最聪明的模型规划，再委派给快速模型的子智能体 {#xt-036}
**作者**：Guillermo Rauch（@rauchg）｜**日期**：2026-11-14｜[原帖](https://x.com/rauchg/status/2121739228698886454)｜♥ 404

Guillermo Rauch 说他所有项目都是先用最聪明的模型做规划，再委派给快速模型的子智能体执行，这只需要在全局 AGENTS.md 里写一行指令。作者自述。

> "All my projects are built by planning with the smartest model + delegating to fast model subagents."

原则：[P01](/compare/evidence#p01) [P10](/compare/evidence#p10)

### XT-037 · Agent 调试正在从 Function Profiling 走向 Decision Profiling {#xt-037}
**作者**：Barret李靖（@Barret_China）｜**日期**：2026-11-15｜[原帖](https://x.com/Barret_China/status/2121949262942720331)｜♥ 314

Barret李靖 推荐几款 harness 插件，其中能直观看到上下文变化、Token 消耗和多 Agent 运行状态的工具，对分析长任务中的决策偏差很有帮助；他认为 Agent 的性能优化很多时候要从工具接口和执行路径入手。

> "Agent Debug 正在从 Function Profiling 走向 Decision Profiling"

原则：[P02](/compare/evidence#p02) [P05](/compare/evidence#p05) [P11](/compare/evidence#p11) [P14](/compare/evidence#p14) [P17](/compare/evidence#p17) [P18](/compare/evidence#p18)

### XT-038 · Cursor 官方插件仓库：rules + skills + MCP + hooks 打包 {#xt-038}
**作者**：ReignSwords（@ReignSwords）｜**日期**：2026-11-18｜[原帖](https://x.com/ReignSwords/status/2123077551778091467)｜♥ 1

作者介绍 cursor/plugins 仓库：一个插件把 rules、skills、MCP 服务器和 hooks 打包成可安装、可升级、可分享的单元，每个插件上架和更新都要人工审核。他认为以前各自攒 rules、skill、MCP 的方式可以收敛。数量与 star 数为作者转述。

> "一个插件 = rules + skills + MCP 服务器 + hooks"

原则：[P03](/compare/evidence#p03) [P06](/compare/evidence#p06) [P08](/compare/evidence#p08) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13) [P14](/compare/evidence#p14) [P15](/compare/evidence#p15) [P18](/compare/evidence#p18) [P19](/compare/evidence#p19)

### XT-039 · Claude Code 实验性 Code Mode：把多步工具调用写成一段脚本 {#xt-039}
**作者**：旅途（@lt5573486353754）｜**日期**：2026-11-18｜[原帖](https://x.com/lt5573486353754/status/2122986245194404032)｜♥ 0

作者介绍 Claude Code 的实验功能 Code Mode：先写一段 JavaScript 把 Bash、Read、Edit 等调用串起来一次执行。官方文档点名三类适用场景：批量改动多文件、先过滤大量搜索结果再交给模型、并行跑测试/lint/类型检查等无依赖命令。版本与日期为作者转述。

> "几条没依赖的命令，测试、lint、类型检查一起跑"

原则：[P04](/compare/evidence#p04) [P06](/compare/evidence#p06) [P12](/compare/evidence#p12) [P15](/compare/evidence#p15) [P17](/compare/evidence#p17)

### XT-040 · 问题可能不在模型，而在你怎么让它干活：Harness Engineering {#xt-040}
**作者**：Bro哥（@iMicodex）｜**日期**：2026-11-18｜[原帖](https://x.com/iMicodex/status/2123055822679011511)｜♥ 7

Bro哥指出 AI 写代码出错、忘记上下文、没测就说完成时，很多人第一反应是换更强的模型；他认为问题可能在于工作方式，并列出 learn-harness-engineering、12-factor-agents、AGENTS.md、Spec Kit 等开源项目。

> "但有没有可能，问题根本不在模型，而在你怎么让它干活？"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P05](/compare/evidence#p05) [P06](/compare/evidence#p06)

### XT-041 · Everything Claude Code：规划、TDD、独立评审、自动验证、持续学习 {#xt-041}
**作者**：Sword-xyj（@SwordXyj）｜**日期**：2026-11-18｜[原帖](https://x.com/SwordXyj/status/2123065196398661881)｜♥ 4

作者介绍开源项目 ECC（Everything Claude Code），把 Agents、Skills、Hooks、Rules、Memory 组合成一套工作流：先拆需求、定计划，用 TDD 开发，让独立 Agent 审查，执行测试与构建来验证，并从会话中提取经验沉淀为 Skills。数量为作者转述。

> "持续学习：从开发会话中提取经验，沉淀成可复用的 Skills。"

原则：[P01](/compare/evidence#p01) [P06](/compare/evidence#p06) [P07](/compare/evidence#p07) [P08](/compare/evidence#p08) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13) [P14](/compare/evidence#p14) [P15](/compare/evidence#p15) [P18](/compare/evidence#p18) [P19](/compare/evidence#p19)

### XT-042 · Amp 聚会共识：人手动按序调用的 skill「金字塔」是反模式 {#xt-042}
**作者**：Thorsten Ball（@thorstenball）｜**日期**：2026-11-18｜[原帖](https://x.com/thorstenball/status/2122922917478715556)｜♥ 207

Amp 的 Thorsten Ball 说在 Amp 聚会上大家一致认为：精心搭建、由人按确定顺序手动调用的 skill 金字塔，看起来是一种反模式。

> "Elaborate pyramids of skills that are invoked deterministically by hand, by a human, seems like an anti-pattern."

原则：[P12](/compare/evidence#p12) [P13](/compare/evidence#p13)
