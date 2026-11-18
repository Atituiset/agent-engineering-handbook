# X 精选 · 上下文与说明文件

> 45 条精选帖子，按发帖日期（UTC）排序。每条都有原帖链接；摘要忠于原文，引文为原帖逐字摘录。**作者自述**为个人经验，厂商员工谈自家产品时请视为**厂商自报**。原则标签为关键词自动归类，见 [共识度/佐证](/compare/evidence)。

[[toc]]

### XC-001 · 别在 CLAUDE.md 里重复 Cursor 规则，直接引用 {#xc-001}
**作者**：Ian Nuttall（@iannuttall）｜**日期**：2025-06-09｜[原帖](https://x.com/iannuttall/status/1932071699111182737)｜♥ 368

Ian Nuttall 建议在 Cursor 中使用 Claude Code 时不要重复规则：让智能体基于已有规则生成 CLAUDE.md，并在其中引用 .cursor/rules 下的规则文件，这样更新 Cursor 规则也会同步作用于 Claude Code。

> "Don't repeat your rules in CLAUDE.⁠md"

原则：[P03](/compare/evidence#p03)

### XC-002 · 规则文件别超过 200 行，只强调必须遵守的规则 {#xc-002}
**作者**：Paco Muro（@PacoMuro_）｜**日期**：2025-06-28｜[原帖](https://x.com/PacoMuro_/status/1938900340079755333)｜♥ 2

Paco Muro 的经验：提示尽量简洁，只突出强制规则；规则或 CLAUDE.md 等上下文提示不要超过 200 行，否则上下文增长后模型记不住；架构和功能如果已在代码中存在，模型会自己学到，无需在规则里强调。作者自述。

> "Try to never have more than 200 lines of context prompts"

原则：[P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P05](/compare/evidence#p05) [P16](/compare/evidence#p16)

### XC-003 · 要让编码智能体变强，首先要痴迷于上下文工程 {#xc-003}
**作者**：Mckay Wrigley（@mckaywrigley）｜**日期**：2025-07-23｜[原帖](https://x.com/mckaywrigley/status/1947834179611501004)｜♥ 1597

Mckay Wrigley 认为提升编码智能体效果的首要事项是上下文工程：好的上下文带来好的计划，好的计划带来好的结果；模型像每次都从零开始的天才，所以要「过量」提供上下文来给它们做入职。注意这与「上下文精简」的建议存在张力。

> "Great Context = Great Plan = Great Result"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02)

### XC-004 · AGENTS.md：给 AI 智能体的 README {#xc-004}
**作者**：Kisalay（@Kisalay_）｜**日期**：2025-08-24｜[原帖](https://x.com/Kisalay_/status/1959510608329466104)｜♥ 0

Kisalay 解释 AGENTS.md 的定位：README 写给人看，告诉贡献者如何运行、构建和贡献；智能体则需要知道测试命令、代码风格、CI 流程等项目规则。没有标准时，每个智能体各自猜测，导致失误和浪费的运行。

> "READMEs are for humans."

原则：[P01](/compare/evidence#p01) [P04](/compare/evidence#p04) [P06](/compare/evidence#p06) [P11](/compare/evidence#p11)

### XC-005 · 我的 CLAUDE.md 只有两行 {#xc-005}
**作者**：Jacob Bartlett（@jacobtechtavern）｜**日期**：2025-09-10｜[原帖](https://x.com/jacobtechtavern/status/1965853091296600123)｜♥ 2

Jacob Bartlett 解释 CLAUDE.md 会在每次会话开始时注入上下文，可用来规定代码标准；他的整个 CLAUDE.md 只有两行，例如不要到处加多余注释。这是「说明文件宜短」的一个极端例子。作者自述。

> "My entire"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P08](/compare/evidence#p08)

### XC-006 · Cursor 重建上下文机制：动态发现而非全部塞入提示 {#xc-006}
**作者**：Michael Truell（@mntruell）｜**日期**：2026-01-07｜[原帖](https://x.com/mntruell/status/2008793943472062807)｜♥ 2477

Cursor CEO Michael Truell 称他们重建了智能体使用上下文的方式：不再把一切塞进提示，而是通过文件、工具和历史动态发现上下文，token 用量减少 46.9%，给智能体留出更多工作空间。厂商自报数据。

> "Instead of stuffing everything into a prompt, Cursor dynamically discovers context via files, tools, and history"

原则：[P02](/compare/evidence#p02) [P17](/compare/evidence#p17)

### XC-007 · 说明文件种类的膨胀 {#xc-007}
**作者**：josh（@nishimiya）｜**日期**：2026-01-20｜[原帖](https://x.com/nishimiya/status/2013614892754915391)｜♥ 72

josh 列出一长串给模型的配置与说明载体：系统提示、模型配置、工具 schema、.cursor/rules、readme、prompt.md、agents.md、claude.md、registry、skill.md、plan.md、copilot-instructions.md……以讽刺的方式指出这类文件正在泛滥。

> "copilot-instructions․md"

原则：[P01](/compare/evidence#p01) [P03](/compare/evidence#p03) [P13](/compare/evidence#p13)

### XC-008 · 一份 4000 字指南的核心：上下文窗口管理 {#xc-008}
**作者**：Aakash Gupta（@aakashgupta）｜**日期**：2026-01-22｜[原帖](https://x.com/aakashgupta/status/2014208332136095874)｜♥ 924

Aakash Gupta 总结一份长篇 Claude Code 指南，认为其核心约束是上下文窗口管理：启用太多工具后 200k 窗口在压缩前可能只剩 70k，每个 MCP、插件、hook、子智能体都在消耗同一份有限资源。帖中引用的 token 数为转述他人数据。

> "every MCP, plugin, hook, and subagent you add isn’t free"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P10](/compare/evidence#p10) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13) [P14](/compare/evidence#p14) [P17](/compare/evidence#p17) [P18](/compare/evidence#p18)

### XC-009 · 分层配置：CLAUDE.md 只写一行「去读 AGENTS.md」 {#xc-009}
**作者**：Michael Nauton（@MichaelNau58251）｜**日期**：2026-03-07｜[原帖](https://x.com/MichaelNau58251/status/2030274993574056180)｜♥ 0

Michael Nauton 设计了分层配置：CLAUDE.md 只有一行指向 AGENTS.md；AGENTS.md 作为入口、路由和共享规则；再按工作类型加载 Protocol 和 Personality。他说每次会话只加载 3 个文件，不用的配置不会进入上下文。作者自述。

> "CLAUDE.md: one line — "read AGENTS.md""

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P05](/compare/evidence#p05) [P11](/compare/evidence#p11) [P17](/compare/evidence#p17)

### XC-010 · Trellis：在多个 AI 编程工具之间统一上下文 {#xc-010}
**作者**：Kevin Ma（@kevinma_dev_zh）｜**日期**：2026-03-12｜[原帖](https://x.com/kevinma_dev_zh/status/2032043626172465364)｜♥ 202

Kevin Ma 介绍 Trellis：在项目里建一个目录，存放代码规范、任务 PRD 和工作流，切换到任何 AI 工具都能注入这些上下文，并支持 git worktree 并行；团队里一人写好的规范，其他人直接复用。

> "把代码规范、任务 PRD、工作流都存进去"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P11](/compare/evidence#p11) [P15](/compare/evidence#p15)

### XC-011 · 显式、可浏览的记忆：个人 wiki 优于「越用越懂你」 {#xc-011}
**作者**：Andrej Karpathy（@karpathy）｜**日期**：2026-04-04｜[原帖](https://x.com/karpathy/status/2040572272944324650)｜♥ 9115

Karpathy 赞赏把个人记忆做成显式 wiki 的做法：相比「据称越用越好」的隐式个性化，wiki 形式的记忆是显式的、可浏览的，你能看到智能体记住了什么。这一思路与把项目知识写进可检查的 Markdown 文件一致。

> "The memory artifact is explicit and navigable"

原则：[P13](/compare/evidence#p13) [P16](/compare/evidence#p16) [P18](/compare/evidence#p18)

### XC-012 · agents-md：一份约 200 行的「高级工程师」行为规范 {#xc-012}
**作者**：Geek Lite（@QingQ77）｜**日期**：2026-04-21｜[原帖](https://x.com/QingQ77/status/2046395996016419050)｜♥ 250

Geek Lite 介绍开源 agents-md 文件：综合 Karpathy 总结的编程智能体失败模式和 Boris Cherny 的工作流，要求智能体在用户出错时反驳、只做最小必要修改、不擅自重构无关代码、先跑验证再报告完成、遇到歧义主动询问。文件约 200 行，用符号链接同时充当 CLAUDE.md 和 GEMINI.md。

> "只做最小必要修改、不擅自重构无关代码、先跑验证再报告完成"

原则：[P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P06](/compare/evidence#p06)

### XC-013 · 每个仓库各自重写 AGENTS.md/CLAUDE.md/.cursor/rules {#xc-013}
**作者**：Sunny R Gupta 🐰（@sunnykgupta）｜**日期**：2026-04-23｜[原帖](https://x.com/sunnykgupta/status/2047406063310532745)｜♥ 276

Sunny Gupta 观察到，很多优秀工程师觉得自己在 AI 编码工具上落后了，原因是规则、hooks、skills 和「最佳实践」组合太多；大家各自在每个仓库重写 AGENTS.md、CLAUDE.md、.cursor/rules，重复摸索。

> "Rewriting AGENTS.md, CLAUDE.md, .cursor/rules in each repo"

原则：[P03](/compare/evidence#p03) [P04](/compare/evidence#p04) [P05](/compare/evidence#p05) [P06](/compare/evidence#p06) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13)

### XC-014 · 换新模型时要重写 skills 和 CLAUDE.md {#xc-014}
**作者**：Alex Albert（@alexalbert__）｜**日期**：2026-06-09｜[原帖](https://x.com/alexalbert__/status/2064467657483829441)｜♥ 2933

Anthropic 的 Alex Albert 给新模型的使用建议：给它更大、更有野心的任务；默认用高推理强度；重写 skills 和 CLAUDE.md，因为为旧模型写的指令会把新模型锚定在过时的模式上。厂商自报。

> "Instructions written for prior models anchor Fable to stale pattern"

原则：[P03](/compare/evidence#p03) [P06](/compare/evidence#p06) [P13](/compare/evidence#p13) [P17](/compare/evidence#p17)

### XC-015 · 10 步记忆文件设置：CLAUDE.md 不超过 200 行，只留它总记不住的事 {#xc-015}
**作者**：Harry Tandy（@HarryTandy）｜**日期**：2026-06-19｜[原帖](https://x.com/HarryTandy/status/2068013110531600547)｜♥ 15

Harry Tandy 整理一份 CLAUDE.md 设置步骤：先 /init 让 Claude 起草，再删掉显而易见的内容；保持 200 行以内，只保留 Claude 总是遗漏的事实；写明项目栈和精确的开发、lint、测试命令。

> "Only keep facts Claude keeps missing."

原则：[P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P04](/compare/evidence#p04) [P06](/compare/evidence#p06) [P08](/compare/evidence#p08) [P15](/compare/evidence#p15) [P18](/compare/evidence#p18)

### XC-016 · Claude Code 配置分层：别把一切塞进一个 CLAUDE.md {#xc-016}
**作者**：Vince 聊开发（@vincemask）｜**日期**：2026-06-27｜[原帖](https://x.com/vincemask/status/2070737784848183415)｜♥ 650

Vince 建议把 Claude Code 配置拆成多层：CLAUDE.md 放项目级上下文与规范，settings.json 管权限、模型和 hooks，rules/ 按主题拆规则，commands/ 沉淀重复工作流，skills/ 按任务动态加载，agents/ 定义专用子智能体，hooks/ 在工具调用前后自动校验。

> "配置一多，别全塞进一个文件。"

原则：[P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P05](/compare/evidence#p05) [P09](/compare/evidence#p09) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13) [P14](/compare/evidence#p14) [P15](/compare/evidence#p15) [P19](/compare/evidence#p19)

### XC-017 · 瓶颈不在模型，而在仓库结构 {#xc-017}
**作者**：Anjula Dwivedi（@HeyAnjula）｜**日期**：2026-07-07｜[原帖](https://x.com/HeyAnjula/status/2074372249155682777)｜♥ 43

Anjula Dwivedi 认为同样的模型和提示词，有人得到聊天机器人，有人得到自主工程师，差别在于仓库的目录与上下文结构。她提出分层组织上下文的「Context Ladder」做法。属个人经验分享，标题措辞偏营销。

> "The model isn't your bottleneck. Your repo is"

原则：[P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P04](/compare/evidence#p04) [P06](/compare/evidence#p06) [P10](/compare/evidence#p10) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13) [P14](/compare/evidence#p14) [P15](/compare/evidence#p15) [P18](/compare/evidence#p18)

### XC-018 · /checkup：清理 skills/MCP、拆分 CLAUDE.md {#xc-018}
**作者**：Boris Cherny（@bcherny）｜**日期**：2026-07-08｜[原帖](https://x.com/bcherny/status/2074997570317779038)｜♥ 11585

Boris Cherny 发布 /checkup 命令：清理未使用的 skills、MCP 和插件以节省上下文；把本地 CLAUDE.md 与仓库中的去重；把根 CLAUDE.md 拆成嵌套 CLAUDE.md 和 skills；关闭慢 hooks；预先批准常被拒绝的只读命令。这说明官方也把「上下文卫生」视为需要定期维护的事。厂商自报。

> "Break up root CLAUDE.md into nested CLAUDE.md's + skills"

原则：[P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13)

### XC-019 · 给模型看示例而不是令牌名：shadcn registry 的「黄金样例集」 {#xc-019}
**作者**：shadcn（@shadcn）｜**日期**：2026-07-21｜[原帖](https://x.com/shadcn/status/2079485535593148754)｜♥ 383

shadcn 解释他们构建 CLI 与 registry 的思路：模型看到一个 prop 或设计令牌名毫无意义，但看到具体的按钮和表单代码，就知道如何创建主按钮、表单里的提交按钮应是主色。registry 保存团队的「黄金样例集」，结合 skills 与 CLI 教智能体检索并拉入上下文。

> "A registry holds your golden set."

原则：[P02](/compare/evidence#p02) [P13](/compare/evidence#p13)

### XC-020 · Claude 5 模型的上下文工程新规则 {#xc-020}
**作者**：Thariq（@trq212）｜**日期**：2026-07-24｜[原帖](https://x.com/trq212/status/2080710971228918066)｜♥ 16318

Anthropic 的 Thariq 撰文称，团队为最新模型删掉了约 80% 的 Claude Code 系统提示词，并总结了编写系统提示词、Skills 与 CLAUDE.md 的经验。文章区分「提示词」与「上下文」：上下文由系统提示词、Skills、CLAUDE.md、记忆等拼装而成，会在许多请求间通用，因此不能写得过于具体。厂商自报。

> "We removed ~80% of the Claude Code system prompt for our newest models"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P13](/compare/evidence#p13) [P18](/compare/evidence#p18)

### XC-021 · 新模型与旧 skills 不兼容：删掉重来反而更好 {#xc-021}
**作者**：Dan Shipper（@danshipper）｜**日期**：2026-07-24｜[原帖](https://x.com/danshipper/status/2080700057892815114)｜♥ 2408

Every 团队测试新模型时发现，它在原有 skills 和插件下会争辩指令、提前停止；删掉现有 skills 从头开始后效果显著变好。Dan Shipper 总结：新模型破坏向后兼容，为旧模型构建的复杂工作流可能拖后腿，需要花时间围绕新模型重建。作者自述测试。

> "Then we deleted our existing skills and started from scratch."

原则：[P06](/compare/evidence#p06) [P13](/compare/evidence#p13) [P19](/compare/evidence#p19)

### XC-022 · 两个智能体、一个仓库：一份规范契约加薄适配层 {#xc-022}
**作者**：Divyam（@talwar_divyam）｜**日期**：2026-08-02｜[原帖](https://x.com/talwar_divyam/status/2083945120773341494)｜♥ 6

Divyam 指出 Codex 读 AGENTS.md、Claude Code 读 CLAUDE.md，两个智能体可能悄悄形成两套「仓库真相」；解法是一份规范的主契约，再加针对各智能体的薄适配层。

> "The fix is one canonical contract with thin agent-specific adapters."

原则：[P01](/compare/evidence#p01) [P03](/compare/evidence#p03) [P04](/compare/evidence#p04) [P05](/compare/evidence#p05) [P06](/compare/evidence#p06) [P08](/compare/evidence#p08) [P11](/compare/evidence#p11) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13) [P15](/compare/evidence#p15) [P18](/compare/evidence#p18)

### XC-023 · 一个只有约 50 行 CLAUDE.md 的高星仓库 {#xc-023}
**作者**：Quri（@qurisage）｜**日期**：2026-08-04｜[原帖](https://x.com/qurisage/status/2084670647322415247)｜♥ 6

作者介绍一个基于 Karpathy 观点整理的 CLAUDE.md 仓库：没有代码，只有约 50 行文字，主要写的是模型「不该做什么」。帖中 star 数为作者转述。它说明短小的负面约束清单很受欢迎。

> "Just one file, CLAUDE.md, with about 50 lines of text."

原则：[P03](/compare/evidence#p03) [P05](/compare/evidence#p05) [P06](/compare/evidence#p06) [P13](/compare/evidence#p13)

### XC-024 · 删掉所有 skills、精简 agents.md，回到朴素工作流 {#xc-024}
**作者**：Dirk Kok · AI agents（@dirkkok）｜**日期**：2026-08-19｜[原帖](https://x.com/dirkkok/status/2090040410152300632)｜♥ 0

Dirk Kok 更新自己的开发流程：退掉高价编码套餐、换用另一家模型，同时删除了所有 skills、精简了 agents.md，工作流变得「朴素」。这是对「配置越多越好」的反例。作者自述。

> "I deleted all my skills and trimmed the agents.md file."

原则：[P01](/compare/evidence#p01) [P03](/compare/evidence#p03) [P13](/compare/evidence#p13) [P17](/compare/evidence#p17)

### XC-025 · 只维护 AGENTS.md，用符号链接生成 CLAUDE.md {#xc-025}
**作者**：Ian Nuttall（@iannuttall）｜**日期**：2026-08-25｜[原帖](https://x.com/iannuttall/status/2092341967606763711)｜♥ 21

Ian Nuttall 给出一个提示词，让智能体在开发目录里自动为 CLAUDE.md 建立指向 AGENTS.md 的符号链接，从而只维护一份说明文件。

> "so I only ever maintain AGENTS.md, never CLAUDE.md"

原则：[P01](/compare/evidence#p01) [P03](/compare/evidence#p03) [P06](/compare/evidence#p06)

### XC-026 · Shopify CEO：只读 CLAUDE.md 会造成团队「脑裂」 {#xc-026}
**作者**：tobi lutke（@tobi）｜**日期**：2026-08-25｜[原帖](https://x.com/tobi/status/2092259436538495186)｜♥ 19414

Shopify CEO Tobi Lütke 表示考虑在 Shopify 禁用 Claude Code，直到它读取 AGENTS.md 和 .agents/skills；只认 CLAUDE.md 会在团队成员使用不同工具时造成「split brain」问题。（此后 Claude Code 增加了 AGENTS.md 后备读取，见本页其他条目。）

> "Insisting on only reading CLAUDE.md sometimes leads to split brain problems when different team members use different tools."

原则：[P03](/compare/evidence#p03) [P13](/compare/evidence#p13)

### XC-027 · AGENTS.md 捐给 Linux 基金会下的 Agentic AI Foundation {#xc-027}
**作者**：Romain Huet（@romainhuet）｜**日期**：2026-08-27｜[原帖](https://x.com/romainhuet/status/2092767496260743513)｜♥ 289

OpenAI 的 Romain Huet 表示，为了开放生态，他们把 AGENTS.md 贡献给 Linux 基金会旗下的 Agentic AI Foundation，并参与创建 Agent Plugins；用户的指令、skills 和插件应该能随人迁移到不同工具。厂商公告。

> "we contributed AGENTS.md to the Agentic AI Foundation under the @linuxfoundation"

原则：[P03](/compare/evidence#p03) [P13](/compare/evidence#p13)

### XC-028 · Amp 的上下文分析：377 个 MCP 工具和 AGENTS.md 正在塞满你的上下文 {#xc-028}
**作者**：Quinn Slack（@sqs）｜**日期**：2026-09-10｜[原帖](https://x.com/sqs/status/2097909378603212876)｜♥ 100

Amp 的 Quinn Slack 介绍线程用量/成本页新增的上下文分析：如果大量 MCP 工具和 AGENTS.md 文件挤占了上下文，可以直接问 Amp，它会告诉你。厂商功能，体现「先观测上下文再优化」。

> "If you have 377 MCP tools and AGENTS.md files junking up your context"

原则：[P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P14](/compare/evidence#p14) [P17](/compare/evidence#p17)

### XC-029 · 清理 skills 与上下文的几个命令，各回答一个问题 {#xc-029}
**作者**：Addy Osmani（@addyosmani）｜**日期**：2026-09-11｜[原帖](https://x.com/addyosmani/status/2098297991019057363)｜♥ 749

Addy Osmani 整理 Claude Code 中与上下文卫生相关的命令：哪些 skill 在用、每个 skill 占多少成本、修复配置和 CLAUDE.md 积累的「债」、窗口里现在有什么、什么在消耗额度。说明上下文与 skill 也会像代码一样积累债务。

> "fixes setup + CLAUDE.md debt"

原则：[P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P13](/compare/evidence#p13) [P17](/compare/evidence#p17)

### XC-030 · Claude Code 开始支持 AGENTS.md（无 CLAUDE.md 时读取） {#xc-030}
**作者**：Thariq（@trq212）｜**日期**：2026-09-18｜[原帖](https://x.com/trq212/status/2101009392611278961)｜♥ 31272

Thariq 宣布 Claude Code 从 2.1.277 版起：如果某个目录没有 CLAUDE.md，会检查并使用 AGENTS.md，可在 /config 中切换。这是说明文件跨工具统一的一步。厂商公告。

> "if there is no CLAUDE.md in a folder, Claude will check for and use AGENTS.md"

原则：[P03](/compare/evidence#p03)

### XC-031 · 上下文里大部分是用不上的工具输出 {#xc-031}
**作者**：Sakata（@sakatayasha）｜**日期**：2026-09-21｜[原帖](https://x.com/sakatayasha/status/2101899579977355571)｜♥ 43

作者介绍开源中间件 context-mode：位于智能体与工具之间，先裁剪冗长的工具输出再进入上下文，并跨智能体保存会话记忆。帖中「98%」与 star 数为作者转述，未独立验证。

> "trim 98% of noisy tool output before it eats the context window"

原则：[P02](/compare/evidence#p02) [P05](/compare/evidence#p05) [P12](/compare/evidence#p12) [P14](/compare/evidence#p14) [P18](/compare/evidence#p18)

### XC-032 · 同一个文件名，不同的发现规则 {#xc-032}
**作者**：Align（@Align_4939）｜**日期**：2026-09-21｜[原帖](https://x.com/Align_4939/status/2102074589010632963)｜♥ 0

作者对比 Claude Code 与 Codex 读取说明文件的差异：Claude Code 只把 AGENTS.md 当后备，向上查找，CLAUDE.md 存在时 AGENTS.md 被忽略；Codex 从 git 根向下查找，优先 AGENTS.override.md，文件大小约有 32 KiB 上限。他认为这才是团队同时维护多份文件的根源。版本细节为作者整理。

> "Same filename, different discovery."

原则：[P03](/compare/evidence#p03) [P06](/compare/evidence#p06) [P10](/compare/evidence#p10) [P12](/compare/evidence#p12) [P18](/compare/evidence#p18)

### XC-033 · Cursor 的经验：一个改进 harness token 效率的提示词 {#xc-033}
**作者**：eric zakariasson（@ericzakariasson）｜**日期**：2026-09-23｜[原帖](https://x.com/ericzakariasson/status/2102853511637774551)｜♥ 3258

Cursor 的 Eric Zakariasson 分享一个基于 Cursor 经验的提示词，用来改进智能体 harness 的 token 效率，涵盖系统提示、工具定义、请求拼装、上下文缓存、压缩和检索等环节。

> "the system prompt, tool definitions, request assembly, context caching, compaction, and retrieval"

原则：[P02](/compare/evidence#p02)

### XC-034 · 用普通 Codex 也能做：定时任务 + 到处放 agents.md 的记忆库 {#xc-034}
**作者**：jason（@jxnlco）｜**日期**：2026-09-30｜[原帖](https://x.com/jxnlco/status/2105335286528119089)｜♥ 397

OpenAI 的 jason 说新产品的大部分功能用原生 Codex 也能实现：他之前用 15 个带心跳自动化的置顶任务，加一个 GitHub 记忆仓库，到处放 agents.md 文件，让所有智能体都能贡献，并让技术和非技术同事都能按他的规则克隆、贡献。作者自述。

> "Github repo for a memory vault based with agents.md files everywhere so all your agents can contribute"

原则：[P03](/compare/evidence#p03) [P18](/compare/evidence#p18)

### XC-035 · 默认上下文加大到 500k，以减少压缩发生 {#xc-035}
**作者**：Tibo（@thsottiaux）｜**日期**：2026-10-11｜[原帖](https://x.com/thsottiaux/status/2109430343346581527)｜♥ 14699

Codex 负责人 Tibo 宣布通过 Codex 使用的模型默认上下文从 272k 提高到 500k，理由是减少压缩的次数，帮助需要长时间保留大量上下文与细节的任务。厂商公告。

> "it helps reduce occurrence of compactions"

原则：[P02](/compare/evidence#p02)

### XC-036 · 每个会话只从系统提示和工具开始 {#xc-036}
**作者**：Ado（@adocomplete）｜**日期**：2026-10-12｜[原帖](https://x.com/adocomplete/status/2109781357924958269)｜♥ 113

Anthropic 的 Ado 解释：每个 Claude Code 会话开始时只有系统提示和工具；可以在 CLAUDE.md（或 AGENTS.md）中设置全仓库上下文，自动记忆默认开启，让 Claude 从交互中记住和学习。厂商说明。

> "Each Claude Code session starts with only the system prompt and tools."

原则：[P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P18](/compare/evidence#p18)

### XC-037 · AGENTS.md 放在仓库里，也可能根本没被加载 {#xc-037}
**作者**：Kyle Tse（@shtse8）｜**日期**：2026-10-13｜[原帖](https://x.com/shtse8/status/2109983383405355416)｜♥ 12

Kyle Tse 查阅五家编码智能体的文档后指出，同一个文件名在各家的加载规则不同：例如 Claude Code 只有在没有 CLAUDE.md 等文件时才读 AGENTS.md，添加个人 CLAUDE.local.md 会悄悄让 AGENTS.md 失效。建议核对各工具的实际加载行为。作者整理，规则可能随版本变化。

> "your AGENTS.md can sit in the repo and still never load"

原则：[P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P04](/compare/evidence#p04) [P08](/compare/evidence#p08) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13) [P15](/compare/evidence#p15) [P18](/compare/evidence#p18)

### XC-038 · 智能体不是上下文不够，而是被不需要的工具输出淹没 {#xc-038}
**作者**：Fajar M Reza（@FReza1984）｜**日期**：2026-10-19｜[原帖](https://x.com/FReza1984/status/2112165384728277233)｜♥ 0

作者指出一次 MCP 调用就可能向提示里倒入一万多 token 的 JSON，一个失败的测试会带来成千上万行日志，其中大多是重复的键、堆栈帧和模型用不上的数据行。主张在工具输出进入上下文前先过滤。

> "Your coding agent isn't running out of context. It's drowning in tool output it never needed."

原则：[P02](/compare/evidence#p02) [P06](/compare/evidence#p06) [P07](/compare/evidence#p07) [P14](/compare/evidence#p14)

### XC-039 · Claude Code、Codex、Cursor 共用 AGENTS.md 的一个陷阱 {#xc-039}
**作者**：Rajesh M（@Rajesh7113）｜**日期**：2026-10-21｜[原帖](https://x.com/Rajesh7113/status/2112769346913403322)｜♥ 2

Rajesh M 提醒：仓库只有 AGENTS.md 时 Claude Code 会读取它，但两者都存在时默认只读 CLAUDE.md。三种工具混用的团队要么只保留 AGENTS.md，要么让 CLAUDE.md 引用它。作者整理，行为可能随版本变化。

> "If your repo has both, Claude only reads CLAUDE.md by default."

原则：[P03](/compare/evidence#p03) [P04](/compare/evidence#p04) [P06](/compare/evidence#p06)

### XC-040 · 同一会话里加载多个 skill 会不会弄脏上下文？ {#xc-040}
**作者**：dex（@dexhorthy）｜**日期**：2026-10-25｜[原帖](https://x.com/dexhorthy/status/2114408588991222156)｜♥ 132

HumanLayer 的 dex 回答一个问题：五步流程每步一个 skill，是放在同一会话、拆给子智能体，还是每步压缩或新开会话？他的直觉是五步问题不大，但每个后续 skill 都会分走对前面内容的注意力，需要权衡。

> "Each successive skill will take a share of attention"

原则：[P02](/compare/evidence#p02) [P10](/compare/evidence#p10) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13) [P18](/compare/evidence#p18)

### XC-041 · 给代码库写摘要文档，只有在提速且不降质时才值得 {#xc-041}
**作者**：dex（@dexhorthy）｜**日期**：2026-10-30｜[原帖](https://x.com/dexhorthy/status/2116003536098263419)｜♥ 0

dex 认为任何为智能体准备的文档或摘要（如每个目录的压缩摘要），只有在提高速度且不降低质量时才有意义；除非你为自己的代码库建了专门的评测并密切盯着，否则更简单的做法是接受一点速度损失，每次都从源码出发。

> "simpler answer is live with a little speed hit and just go from source every time"

原则：[P17](/compare/evidence#p17)

### XC-042 · 压缩变好了：何时还需要手动清理上下文 {#xc-042}
**作者**：dex（@dexhorthy）｜**日期**：2026-11-07｜[原帖](https://x.com/dexhorthy/status/2119165267368698188)｜♥ 153

dex 认为如今自动压缩改进很多，某些情况下不必为了模型的专注度而显式清空或外置上下文，但为了与人协作、在智能体或机器之间交接，外置仍有用。他把自动压缩阈值设在 400k，在 200k–400k 之间按模型和 harness 手动压缩。这是对早期「频繁 /clear」建议的修正。

> "still useful for collab w/ humans or handoff between agents / machines though!"

原则：[P02](/compare/evidence#p02) [P05](/compare/evidence#p05) [P10](/compare/evidence#p10) [P18](/compare/evidence#p18)

### XC-043 · Home Repo：一个仓库集中放 skills、指导文件和 wiki {#xc-043}
**作者**：Matt Pocock（@mattpocockuk）｜**日期**：2026-11-10｜[原帖](https://x.com/mattpocockuk/status/2120260969750540327)｜♥ 3459

Matt Pocock 介绍他在多个仓库间使用智能体的方法：建一个「home」仓库存放所有 skills、指导文件和 wiki，在其中运行智能体，并在 AGENTS.md 里写上其他仓库的位置指引。好处是指导文件和工具集中一处、有统一的运行入口、便于跨仓库做大范围修改。

> "I have a single repo (the home) where all of my skills, steering files, wiki etc live."

原则：[P03](/compare/evidence#p03) [P13](/compare/evidence#p13)

### XC-044 · 提示词也会过期：/doctor prompt-audit 检查 CLAUDE.md {#xc-044}
**作者**：Berryxia.AI（@berryxia）｜**日期**：2026-11-13｜[原帖](https://x.com/berryxia/status/2121235974336520383)｜♥ 131

Berryxia 转述 Claude Code 团队的提醒：CLAUDE.md、skills、agents 和自定义命令中可能有「为老模型写的提示词写法」，在新模型上反而拖后腿。审计报告会优先列出失效路径、失效命令和互相冲突的指令（全局与项目各一份、说法不一）。版本号与浏览量为作者转述。

> "很多人觉得 CLAUDE.md 写好一次就能一直用。其实提示词也会过期。"

原则：[P03](/compare/evidence#p03) [P13](/compare/evidence#p13)

### XC-045 · 把官方提示词片段放进 AGENTS.md，治「不说人话」和「AI 味」 {#xc-045}
**作者**：Vic TALK（@victalk6886）｜**日期**：2026-11-18｜[原帖](https://x.com/victalk6886/status/2122991031041847445)｜♥ 7

Vic TALK 转述 Codex 负责人对新模型体验粗糙的回应，并把官方文档中针对表达问题的提示词译成中文，建议直接放进项目或全局 AGENTS.md：用用户的说法、关键点先讲、最终回复自成一体等。说明 AGENTS.md 也承担「行为偏好」配置。

> "直接放进项目或全局的 AGENTS.md 就行"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P06](/compare/evidence#p06) [P10](/compare/evidence#p10) [P14](/compare/evidence#p14) [P15](/compare/evidence#p15) [P16](/compare/evidence#p16) [P18](/compare/evidence#p18)
