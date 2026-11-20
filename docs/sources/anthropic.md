# Anthropic / Claude Code

> 本页收录 Anthropic 官方工程博客、Claude Code 文档与 claude.dev 博客中，与「如何驾驭编码智能体」直接相关的原文。凡涉及 Anthropic 自家产品效果、内部数据的数字，均为 **「厂商自报、尚未独立验证」**。所有链接均于 2026-11-18 打开核对。

[[toc]]

## 官方最佳实践与文档

### AN01 · Best practices for Claude Code {#an01}
**机构**：Anthropic（Claude Code 官方文档）｜**日期**：持续更新（2026-11 访问）｜[原文](https://code.claude.com/docs/en/best-practices)

文档把会话失败归为四类：缺少仓库里读不到的信息、没有可运行的检查来判断「是否完成」、发生了「绝不能发生 / 必须发生」的事、花费超出任务价值。核心框架是把每条指令分为 **非确定性**（提示词、CLAUDE.md、skills——模型读了再决定）与 **确定性**（hooks、deny 规则、managed settings、CI——harness 每次都执行）。建议多数时候让模型判断，只有「不能有例外」的规则才写成 hook；如果某条 CLAUDE.md 规则加粗强调后仍被忽略，就该改成 hook，反之只是偏好的 hook 应删掉。

> "You could’ve written either of these as a line in CLAUDE.md or in your prompt, and Claude would follow it nearly every time. But no matter how strongly you word it, whether Claude follows that line on a given turn is still Claude’s call."

`与本手册关系：第 02、04 章的核心依据` `厂商文档`

### AN02 · How Claude remembers your project（CLAUDE.md 与记忆） {#an02}
**机构**：Anthropic（Claude Code 文档）｜**日期**：持续更新｜[原文](https://code.claude.com/docs/en/memory)

说明 CLAUDE.md 的层级（组织级、用户级、项目级、子目录级）如何被加载、如何用 `@` 导入其它文件、以及自动记忆的工作方式。实践要点：项目级 CLAUDE.md 纳入版本控制与团队共享，个人偏好放在用户级文件，子目录的说明按需加载。2026-11 核对：两类记忆都只是上下文、不是强制配置，必须拦截的动作要用 PreToolUse hook；自动记忆每个会话加载前 200 行或 25KB；压缩后项目根目录的 CLAUDE.md 会重新读入，只在对话里给出的指令可能丢失。

`厂商文档`

### AN03 · Automate actions with hooks {#an03}
**机构**：Anthropic（Claude Code 文档）｜**日期**：持续更新｜[原文](https://code.claude.com/docs/en/hooks-guide)

Hooks 是在智能体生命周期事件（如工具调用前后、会话结束 Stop）上执行的确定性 shell 命令，可用于格式化、拦截对受保护文件的修改、在「宣布完成」前强制跑测试等。它是把「架构约束 / 团队规范」从「希望模型遵守」变成「harness 必然执行」的主要手段。

`厂商文档`

### AN04 · Create custom subagents {#an04}
**机构**：Anthropic（Claude Code 文档）｜**日期**：持续更新｜[原文](https://code.claude.com/docs/en/sub-agents)

子智能体拥有独立的上下文窗口、系统提示与工具白名单，适合探索、跑测试、评审等「会产生大量一次性中间输出」的工作，只把结论返回主会话。文档建议为子智能体设置明确的职责描述与最小工具权限。

`厂商文档`

### AN05 · Extend Claude with skills {#an05}
**机构**：Anthropic（Claude Code 文档）｜**日期**：持续更新｜[原文](https://code.claude.com/docs/en/skills)

Skills 是包含 SKILL.md、脚本与参考资料的文件夹，模型根据描述按需加载（渐进式披露）。文档中内置了 `/run`、`/verify` 等技能，用于「构建并启动应用、在运行中的应用上确认改动」，体现了把验证流程固化为可复用技能的思路。

`厂商文档`

### AN06 · Customize Code Review（REVIEW.md） {#an06}
**机构**：Anthropic（Claude Code 文档）｜**日期**：持续更新｜[原文](https://code.claude.com/docs/en/code-review-customize)

团队可以通过提交到仓库的 CLAUDE.md 或 REVIEW.md 来调整 AI 代码评审：减少吹毛求疵、忽略生成文件、加入团队关心的规则。配合 AN18 的做法：评审规则从基础分支读取，变更本身无法修改评判它的规则。

`厂商文档`

### AN07 · Common workflows {#an07}
**机构**：Anthropic（Claude Code 文档）｜**日期**：持续更新｜[原文](https://code.claude.com/docs/en/common-workflows)

覆盖理解新代码库、修 bug、重构、用计划模式（Plan Mode）先出方案再改代码、并行 worktree 会话、写测试与 PR 等常见流程的官方推荐步骤。适合作为团队内部 onboarding 的起点。

`厂商文档`

### AN08 · Using CLAUDE.md files: Customizing Claude Code for your codebase {#an08}
**机构**：Anthropic（claude.com 博客）｜**日期**：2025-11-25｜[原文](https://claude.com/blog/using-claude-md-files)

介绍 CLAUDE.md 可记录常用命令、核心工具、代码风格、测试方式、仓库约定、环境搭建与项目特有警告；没有强制格式，建议保持简洁、人类可读，并可用 `/init` 生成初稿后人工修订。

`厂商文档`

## 工程博客：智能体设计的基本功

### AN09 · Building effective agents {#an09}
**作者**：Erik Schluntz、Barry Zhang（Anthropic）｜**日期**：2024-12-19｜[原文](https://www.anthropic.com/engineering/building-effective-agents)

区分 **workflow**（预定义代码路径编排 LLM）与 **agent**（模型动态决定流程与工具），总结了提示链、路由、并行化、编排者-工作者、评估者-优化者等可组合模式。核心建议是先找最简单的方案，只在必要时增加复杂度，甚至可能根本不需要智能体。

> "Consistently, the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns."

### AN10 · Effective context engineering for AI agents {#an10}
**机构**：Anthropic Applied AI 团队｜**日期**：2025-09-29｜[原文](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

提出「上下文工程」是提示工程的自然演进：上下文是边际收益递减的有限资源，存在 **context rot**（上下文越长、召回越差）。给出的方法包括：寻找最小的高信号 token 集合、系统提示找准「高度」、工具精简、即时（just-in-time）检索、长任务使用压缩（compaction）、结构化笔记与子智能体架构。

> "Context, therefore, must be treated as a finite resource with diminishing marginal returns."

### AN11 · Writing effective tools for agents — with agents {#an11}
**机构**：Anthropic｜**日期**：2025-09-11｜[原文](https://www.anthropic.com/engineering/writing-tools-for-agents)

工具是确定性系统与非确定性智能体之间的契约。建议：先做原型、用真实任务构建评测、让 Claude 分析评测记录来改进工具；选择少而精的工具而非把每个 API 包一层；给工具命名空间；返回有意义、节省 token 的上下文；像写提示词一样写工具描述。

### AN12 · How we built our multi-agent research system {#an12}
**机构**：Anthropic｜**日期**：2025-06-13｜[原文](https://www.anthropic.com/engineering/multi-agent-research-system)

介绍 Research 功能的编排者-工作者架构。多智能体在「广度优先、可并行」的研究类任务上表现更好，但代价是 token：文中称智能体约用对话的 4 倍 token，多智能体系统约 15 倍，因此只适合价值足够高的任务。还总结了提示设计、评测与生产可靠性方面的教训。

`厂商自报、尚未独立验证`

### AN13 · Building agents with the Claude Agent SDK {#an13}
**机构**：Anthropic｜**日期**：2025-09-29｜[原文](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)

把 Claude Code 背后的 harness 抽象为 Agent SDK，并提炼出通用智能体循环：**收集上下文 → 采取行动 → 验证工作 → 重复**。强调验证环节可以是规则（lint）、视觉反馈（截图）或 LLM 评审。

### AN14 · Equipping agents for the real world with Agent Skills {#an14}
**机构**：Anthropic｜**日期**：2025-10-16（2025-12-18 更新为开放标准）｜[原文](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

Skills 用「文件夹 + SKILL.md + 脚本/资源」承载程序性知识，模型启动时只看到名称与描述，需要时才读取全文和附属文件（渐进式披露），从而在不撑爆上下文的前提下扩展能力。

### AN15 · Code execution with MCP: Building more efficient agents {#an15}
**机构**：Anthropic｜**日期**：2025-11-04｜[原文](https://www.anthropic.com/engineering/code-execution-with-mcp)

把 MCP 服务器呈现为代码 API，让智能体写代码调用工具、在执行环境里过滤中间数据，而不是把所有工具定义与结果塞进上下文。文中示例称 token 用量最多可降低 98.7%。

`厂商自报、尚未独立验证`

### AN16 · Introducing advanced tool use {#an16}
**机构**：Anthropic｜**日期**：2025-11-24｜[原文](https://www.anthropic.com/engineering/advanced-tool-use)

介绍 Tool Search Tool（按需发现工具，而非一次加载全部定义）、Programmatic Tool Calling（用代码编排多次工具调用，中间结果不进上下文）与工具使用示例三项能力，目标是让智能体在成百上千个工具下仍保持上下文精简。

### AN17 · Effective harnesses for long-running agents {#an17}
**机构**：Anthropic｜**日期**：2025-11-26｜[原文](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

长任务的根本难题是每个新会话都「失忆」。方案是 **初始化智能体**（搭好 `init.sh`、`claude-progress.txt` 进度日志、功能清单与首个 git 提交）+ **增量编码智能体**（每次只推进一项功能、留下清晰产物、用 git 与进度文件交接）。灵感直接来自优秀工程师的日常习惯。

> "The key insight here was finding a way for agents to quickly understand the state of work when starting with a fresh context window..."

### AN18 · How the Claude Code team thinks about verification {#an18}
**作者**：Addy Osmani（claude.dev 博客）｜**日期**：2026-11-16｜[原文](https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/)

文中称 Claude Code 团队约 90% 代码由 Claude 编写和评审，验证回路决定了能并行多少智能体。推荐三类测试：**端到端**（最难被糊弄）、**属性测试**（往返、不变量、幂等、等价性）、**差分测试**（迁移时以旧系统为 oracle）。团队做法包括：建立 `verify` skill 让智能体真正运行改动；检查连续三轮失败即升级给人；39 项可从 diff 触发的可靠性清单；评审规则（REVIEW.md）从基础分支读取，变更不能修改评判它的规则；新门禁先「观察模式」再「强制模式」；不许用 sleep/重试掩盖 flaky test；规则文件要定期修剪。

> "If a change can modify the check that judges it, the check is broken."

`厂商自报、尚未独立验证（90%、+10 分等数字）`

### AN19 · How the Claude Code team does code review {#an19}
**作者**：Addy Osmani、Morgan Westlee Lunt、Qing Wang（claude.dev 博客）｜**日期**：2026-10-15｜[原文](https://claude.dev/blog/solving-code-review-at-anthropic/)

文中称 Anthropic monorepo 每日落地变更从 5 月约 2,500 增至 9 月 30,000 以上；6–9 月 Claude Code 仓库合并 PR 翻倍、回滚占比下降 40% 以上。做法是「多层而非单一闸门」：作者先自证、每个 PR 先过 AI 评审（多个智能体找 bug、另一组投票确认才发布）、可阻断的安全评审、lint/类型/测试/构建、按风险分级的人工审批、以及一键回滚。把「是否有人读过代码」换成「这次变更可能出什么错、哪道检查最合适」。

> "We think 'did a human read the code?' is an imprecise proxy for 'what could go wrong with this change, and which check—automated or human—is the right one to catch it?'"

`厂商自报、尚未独立验证`

### AN20 · Seeing like an agent: how we design tools in Claude Code {#an20}
**作者**：Thariq Shihipar｜**日期**：2026-04-10｜[原文](https://claude.dev/blog/seeing-like-an-agent/)

从模型视角讨论工具设计：何时给一个通用工具（bash/代码执行）、何时给专用工具，以及 AskUserQuestion、TodoWrite→Tasks 等工具的演化。结论之一是最有价值的工具是「让模型自己找上下文」的工具，并通过子智能体做渐进式披露（如 Claude Code Guide 子智能体）。

> "The most consequential tools we've built are the ones that let Claude find its own context."

### AN21 · Lessons from building Claude Code: How we use skills {#an21}
**作者**：Thariq Shihipar｜**日期**：2026-06-03｜[原文](https://claude.dev/blog/lessons-from-building-claude-code-how-we-use-skills/)

Anthropic 内部有数百个在用 skills，可归为九类（如库/SDK 使用说明、验证、数据查询、自动化流程、代码审查等）。经验：一个 skill 只做一类事；重点写「gotchas」而非模型已知的常识；用脚本和模板代替长篇说明；skill 可以带配置与简单记忆；通过插件市场分发并度量使用情况。

### AN22 · Using Claude Code: Spending your effort {#an22}
**作者**：Thariq Shihipar｜**日期**：2026-09-25｜[原文](https://claude.dev/blog/spending-your-effort/)

作者实验发现「effort」主要调节模型做多少验证与边界测试、用多少自主判断。经验法则：低 effort 用于头脑风暴与小改；中等用于常规功能；高 effort 用于验证重要或边界多的场景（如遗留代码修 bug）；最高用于完全自主的端到端构建。作者自己的循环是「让模型先采访我 → 低 effort 实现 → 我审查 → 高 effort 验证」。

### AN23 · A harness for every task: dynamic workflows in Claude Code {#an23}
**机构**：Anthropic（claude.dev 博客）｜**日期**：2026-06-02｜[原文](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code)

介绍 Claude Code 可以按任务动态编写并编排自己的多智能体 harness（扇出并行、验证者智能体等），以及最能发挥其作用的使用模式。代表了「harness 本身也可以由智能体生成」的方向。

### AN24 · Harness design for long-running application development {#an24}
**机构**：Anthropic｜**日期**：2026-03-24｜[原文](https://www.anthropic.com/research/harness-design-long-running-apps)

受 GAN 启发，采用 **规划者-生成者-评估者** 三智能体结构完成多小时的全栈应用自主开发；先把「设计好不好」这类主观判断转化为可打分的标准。关键发现是：**把干活的智能体与评判的智能体分开**是很强的杠杆，但评估者仍是 LLM，天然对 LLM 产出偏宽容，需要专门校准。

### AN25 · Redesigning source control at Anthropic {#an25}
**机构**：Anthropic｜**日期**：2026-10-13｜[原文](https://www.anthropic.com/research/redesigning-source-control)

当「写代码不再是瓶颈」，源码管理成了最大瓶颈：文中称 2026 年 5 月日均合并约 2,500 次，9 月超过 30,000 次，团队用五个月迁移到自研版本控制系统。启示：智能体时代的瓶颈会向评审、CI、合并、发布等下游转移。

`厂商自报、尚未独立验证`

### AN26 · How we built Claude Code auto mode {#an26}
**机构**：Anthropic｜**日期**：2026-03-25｜[原文](https://www.anthropic.com/research/claude-code-auto-mode)

文中称用户批准了 93% 的权限请求，说明逐条确认会造成「审批疲劳」。auto mode 用基于模型的分类器代替人工审批，目标是拦截不符合用户意图的危险操作，其余放行；是介于「全手动」与「完全跳过权限」之间的折中。

`厂商自报、尚未独立验证`

### AN27 · Making Claude Code safer with sandboxing {#an27}
**机构**：Anthropic｜**日期**：2025-10-20｜[原文](https://www.anthropic.com/engineering/claude-code-sandboxing)

通过文件系统隔离与网络隔离两道边界，让智能体在受限环境内自主运行、减少权限弹窗，同时降低提示注入造成的危害。核心理念：与其让人逐条审批，不如先把爆炸半径限制住。

### AN28 · How we contain Claude across products {#an28}
**机构**：Anthropic｜**日期**：2026-05-25｜[原文](https://www.anthropic.com/research/how-we-contain-claude)

把风险拆成「失败概率 × 失败后果」，工程问题变成如何限制爆炸半径（blast radius）。总结了在 claude.ai、Claude Code、Cowork 中构建隔离与遏制的分层做法。

### AN29 · Building a C compiler with a team of parallel Claudes {#an29}
**作者**：Nicholas Carlini（Anthropic）｜**日期**：2026-02-05｜[原文](https://www.anthropic.com/research/building-c-compiler)

16 个并行智能体在近 2,000 个会话、约 2 万美元 API 成本下，写出约 10 万行、可编译 Linux 6.9（x86/ARM/RISC-V）的 Rust C 编译器。经验重点在 harness：如何写测试让无人监督的智能体不跑偏、如何切分工作以便并行、以及这种方法的天花板。

`作者自述、尚未独立验证`

### AN30 · Scaling Managed Agents: Decoupling the brain from the hands {#an30}
**机构**：Anthropic｜**日期**：2026-04-08｜[原文](https://www.anthropic.com/research/managed-agents)

观察到 harness 里编码了「模型做不到什么」的假设，而这些假设会随模型进步迅速过时（如针对 Sonnet 4.5「上下文焦虑」的补丁）。因此把「大脑」（模型+harness）、「手」（沙箱与工具）、「会话」（事件日志）解耦为稳定接口，让实现可以随时替换——类比操作系统对硬件的虚拟化。

### AN31 · Demystifying evals for AI agents {#an31}
**机构**：Anthropic｜**日期**：2026-01-09｜[原文](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

系统介绍智能体评测：任务、环境、grader（代码断言、LLM 评分、人工）、能力评测与回归评测的区别等。指出没有评测时团队只能「等投诉→手动复现→修→祈祷」，被动且盲目。对于把团队规范变成可度量的检查很有参考价值。

### AN32 · An update on recent Claude Code quality reports {#an32}
**机构**：Anthropic｜**日期**：2026-04-23｜[原文](https://www.anthropic.com/research/april-23-postmortem)

一份事故复盘：用户反馈的质量下降被追溯到三处 harness/产品层改动，其中包括一条「减少啰嗦」的系统提示指令与其它提示改动叠加后损害了编码质量。启示：系统提示、上下文与 harness 的改动同样需要评测与灰度，不只是模型本身。

### AN33 · The components of agent memory {#an33}
**机构**：Anthropic｜**日期**：2026-11-06｜[原文](https://www.anthropic.com/research/components-of-agent-memory)

讨论智能体如何在「不知道之后要用什么」的情况下决定记住什么，借鉴人类睡眠中的记忆巩固，提出离线「dreaming」整理记忆、纠正错误记忆的思路。对团队设计跨会话知识沉淀（进度文件、记忆库）有启发。

### AN34 · Safely scaling multi-agent teams with Claude Fable 5.2 {#an34}
**机构**：Anthropic（claude.dev 博客）｜**日期**：2026-11-09｜[原文](https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/)

1,000 个智能体借助通用工具与共享数据库复现费马大定理形式化证明的实验。安全控制是分层的：每个智能体在无网络沙箱中运行，分类器在执行前检查每条 shell 命令与文件编辑，离线监控审查团队的所有行为。

`厂商自报、尚未独立验证`

### AN35 · How Anthropic teams use Claude Code {#an35}
**机构**：Anthropic｜**日期**：2025-07-24｜[原文](https://www.anthropic.com/news/how-anthropic-teams-use-claude-code)

各职能团队（基础设施、安全、产品、数据、法务等）的使用案例汇编：用 CLAUDE.md 与 MCP 汇集散落的团队知识、在不熟悉的代码库里定位问题、为非工程同事构建自动化工具等。

### AN36 · Introducing the Model Context Protocol {#an36}
**机构**：Anthropic｜**日期**：2024-11-25｜[原文](https://www.anthropic.com/news/model-context-protocol)

MCP 的发布公告：用开放协议连接 AI 应用与数据源/工具，取代为每个组合写一次性集成。现已成为跨厂商的事实标准（见 [OS 页](./open-source#os12)）。

## 2026-11 增补：成本、遥测与上下文管理 {#cost-telemetry}

### AN37 · Monitoring（Claude Code 的 OpenTelemetry 遥测） {#an37}
**机构**：Anthropic（Claude Code 文档）｜**日期**：持续更新（2026-11 核对）｜[原文](https://code.claude.com/docs/en/monitoring-usage)

Claude Code 可以通过 OpenTelemetry 导出遥测：指标走标准 metrics 协议，事件走 logs/events 协议，还可以选择导出分布式追踪。用环境变量配置导出器与端点。指标包括会话数、代码行数、PR 数、提交数、成本与 token 用量；事件包括用户提示、API 请求、工具决策与工具结果。默认不记录提示原文，需要显式开启。

`厂商文档`

### AN38 · Manage costs effectively（Claude Code 成本管理） {#an38}
**机构**：Anthropic（Claude Code 文档）｜**日期**：持续更新（2026-11 核对）｜[原文](https://code.claude.com/docs/en/costs)

Claude Code 按 token 计费，自动使用提示缓存与自动压缩。降成本的建议：任务之间用 `/clear` 开新会话；给 `/compact` 写保留重点；多数编码任务用较便宜的模型，复杂架构决策才用最强的模型，简单子智能体可单独指定小模型；不用的 MCP 服务器关掉，能用 CLI 就用 CLI；用 hook 预处理大日志；把不常用的说明从 CLAUDE.md 移到 skill；简单任务调低 effort 或思考预算；啰嗦的操作交给子智能体，但子智能体的请求同样计费。文档给出企业部署的平均成本约为每位开发者每个活跃日 13 美元（厂商自报），并建议先用小范围试点建立基线。`/usage` 会显示提示缓存命中率与未命中的可能原因（如工具定义变化）。

`厂商文档；成本数字为厂商自报`

### AN39 · Prompt caching（Claude API 文档） {#an39}
**机构**：Anthropic（Claude 平台文档）｜**日期**：持续更新（2026-11 核对）｜[原文](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

提示缓存按**前缀**复用：后续请求只要前缀相同，就从缓存继续，降低延迟与成本。默认缓存寿命 5 分钟，每次命中会刷新；也可选 1 小时。计价倍数：5 分钟写入为基础输入价的 1.25 倍，1 小时写入为 2 倍，缓存读取为 0.1 倍（个别模型例外）。

`厂商文档`

### AN40 · Context editing（Claude API 文档） {#an40}
**机构**：Anthropic（Claude 平台文档）｜**日期**：持续更新（2026-11 核对）｜[原文](https://platform.claude.com/docs/en/build-with-claude/context-editing)

随着对话增长自动管理上下文的两种策略：**工具结果清理**适合工具调用多、旧结果已不再需要的智能体工作流；**思考块清理**可以选择保留多少轮的思考以兼顾连续性。可以设置触发阈值与保留数量。它是「压缩」之外的另一种手段：不是摘要，而是有选择地删掉过期内容。

`厂商文档`
