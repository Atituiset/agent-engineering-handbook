# 工具厂商与创业公司

> Cursor、Cognition（Devin/Windsurf）、Vercel、Sourcegraph/Amp、Factory、AWS Kiro、Manus、LangChain、HumanLayer 等公司的工程博客与文档。厂商在推广自家产品，涉及效果的数字均为 **「厂商自报、尚未独立验证」**。链接于 2026-11-18 核对。

[[toc]]

## Cursor

### VD01 · Best practices for coding with agents {#vd01}
**机构**：Cursor｜**日期**：2026-01-09｜[原文](https://cursor.com/blog/agent-best-practices)

Cursor 团队的智能体使用指南。最重要的一条是「先计划后编码」：用 Plan Mode 让智能体先调研代码库、提问澄清、生成可编辑的 Markdown 计划，再开始实现。其它要点：判断何时继续对话、何时开新会话；用规则与 skills 定制行为；用 hook 让智能体持续迭代直到测试全部通过，并明确要求「不要修改测试」；专门安排一轮评审；在本地与云端智能体之间切换。

> "The most impactful change you can make is planning before coding."

### VD02 · Rules（Cursor 文档） {#vd02}
**机构**：Cursor｜**日期**：持续更新｜[原文](https://cursor.com/docs/context/rules)

`.cursor/rules` 下的规则可以「始终生效」「按文件通配符生效」「由模型判断是否相关」或「手动引用」，同时支持 AGENTS.md。是「按需加载规则」这一思路在 IDE 中的实现。

`厂商文档`

### VD03 · Scaling long-running autonomous coding {#vd03}
**机构**：Cursor｜**日期**：2026-01-14｜[原文](https://cursor.com/blog/scaling-agents)

让数百个智能体在单一项目上连续运行数周的实验。平级、通过共享文件自我协调的方案失败了：没有层级时智能体变得「规避风险」，只做小而安全的改动、无人负责难题。改为 **规划者 / 工作者 / 评判者** 的分层结构后，大部分协调问题消失。文中称 Solid→React 的就地迁移历时三周以上（+266K/−193K），通过 CI 但仍需仔细评审；不同模型适合不同角色（规划 vs 执行）。

> "A surprising amount of the system's behavior comes down to how we prompt the agents."

`厂商自报、尚未独立验证`

### VD04 · Improved token efficiency for longer agent runs {#vd04}
**机构**：Cursor｜**日期**：2026-09-23｜[原文](https://cursor.com/blog/improved-token-efficiency)

通过精简静态上下文（系统提示与工具定义）、按使用频率 A/B 测试哪些工具常驻上下文、以及更好地利用提示缓存，在不降低质量的前提下把用户 token 成本降低约 7%。说明 harness 层的上下文组装本身就是需要持续度量和优化的工程对象。

`厂商自报`

## Cognition（Devin / Windsurf）

### VD05 · Don’t Build Multi-Agents {#vd05}
**作者**：Walden Yan（Cognition）｜**日期**：2025-06-12｜[原文](https://cognition.ai/blog/dont-build-multi-agents)

提出两条上下文工程原则：**共享上下文，并共享完整的智能体轨迹而非单条消息**；**行动隐含决策**，并行子智能体各自做出的隐含决策会相互冲突。因此当时建议多数场景使用单线程线性智能体，长任务用压缩模型管理历史。

### VD06 · Multi-Agents: What's Actually Working {#vd06}
**作者**：Walden Yan（Cognition）｜**日期**：2026-04-22｜[原文](https://cognition.ai/blog/multi-agents-working)

十个月后的修正：并行「写手」群依然问题重重，但一类更窄的多智能体确实有效——多个智能体贡献智能（调研、审查、规划），**写操作保持单线程**。作者认为无结构的智能体蜂群「多半是干扰」，实用形态是「map-reduce-and-manage」：管理者拆分工作、子智能体执行、管理者综合。

### VD07 · Coding Agents 101: The Art of Actually Getting Things Done {#vd07}
**机构**：Devin（Cognition）｜**日期**：未标注（2025）｜[原文](https://devin.ai/agents101)

面向工程团队的入门指南：像对待能力强但缺乏上下文的初级工程师一样给出清晰的任务说明；指出方法和起点；定义完成标准与验证方式；从小任务开始建立信任；为智能体准备可运行的环境与检查（CI、lint、类型）。

### VD08 · Devin's 2025 Performance Review: Learnings From 18 Months of Agents At Work {#vd08}
**机构**：Cognition｜**日期**：2025-11-14｜[原文](https://cognition.ai/blog/devin-annual-performance-review-2025)

总结 Devin 最擅长的是「需求清晰前置、结果可验证、相当于初级工程师 4–8 小时工作量」的任务，以及可并行的大规模迁移、补测试（人写测试手册、智能体批量执行、代码负责人检查逻辑）。也坦承它不能像资深工程师那样独立处理模糊的端到端项目，视觉设计等需要非常具体的输入。

`厂商自报`

### VD09 · Verifying Agentic Development at Scale {#vd09}
**机构**：Cognition｜**日期**：2026-05-29｜[原文](https://cognition.ai/blog/testing-development)

文中称 Devin 异步触发的会话首次超过交互式会话，因此开发者回来时必须看到「已验证、可合并」的结果。分享了让智能体在云端虚拟机里做端到端测试的经验与失败模式：把登录等重复步骤固化、需要密钥时的协作方式、用带标注截图的测试报告方便人快速复核。

### VD10 · What We Learned Building Cloud Agents {#vd10}
**机构**：Cognition｜**日期**：2026-04-23｜[原文](https://cognition.ai/blog/what-we-learned-building-cloud-agents)

「把 CLI 智能体塞进容器」只是起点：容器共享内核带来隔离风险；容器扛不住等待 CI、评审的异步空档；数百个云端智能体需要编排、治理与各种系统集成。更重要的是组织层面：项目范围、人员配置、评审与发布流程都是为人类做工而设计的，需要随智能体能力反复重估。

## Vercel、Sourcegraph/Amp、Factory

### VD11 · AGENTS.md outperforms skills in our agent evals {#vd11}
**机构**：Vercel｜**日期**：2026-01-27｜[原文](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals)

针对 Next.js 16 新 API（不在模型训练数据中）构建评测：把约 8KB 的压缩文档索引直接放进 AGENTS.md 达到 100% 通过率，而 skills 方案最高 79%；在 56% 的用例中 skill 根本没被调用。启示：对「每个任务都需要的框架知识」，被动常驻上下文比依赖模型主动调用更可靠——但这与「保持 AGENTS.md 精简」需要权衡（见第 02 章）。

`厂商自报、单一评测场景`

### VD12 · How to Build an Agent {#vd12}
**作者**：Thorsten Ball（Amp/Sourcegraph）｜**日期**：2025-04-21｜[原文](https://ampcode.com/how-to-build-an-agent)

用不到 400 行代码（多数是样板）实现一个能读写文件、执行命令的编码智能体，揭示智能体的本质「就是一个 LLM、一个循环和足够的 token」。帮助工程师去魅：真正的差异在工具设计、上下文与反馈回路。

> "It’s an LLM, a loop, and enough tokens."

### VD13 · Context Management in Amp {#vd13}
**机构**：Amp｜**日期**：2026-07-27（原写于 2025-11）｜[原文](https://ampcode.com/guides/context-management)

解释上下文窗口包含什么（消息、回复、工具调用、思考块），为什么要用新线程、交接（handoff）和子智能体管理上下文。文章自己注明：模型已变得更宽容，但上下文管理仍然重要。

### VD14 · Evaluating Context Compression for AI Agents {#vd14}
**机构**：Factory Research｜**日期**：2025-12-16｜[原文](https://factory.ai/news/evaluating-compression)

用「探针」评估压缩质量：压缩后询问智能体原始报错、改过哪些文件、下一步做什么、之前为什么这样决定。结论：结构化摘要比其它方法保留更多有用信息；优化目标不应是「每次请求的 token」，而是「**每个任务的 token**」——压缩过度会让智能体忘记改过的文件、重走死路。

`厂商自报、尚未独立验证`

## AWS Kiro、Manus、LangChain、HumanLayer

### VD15 · Introducing Kiro {#vd15}
**机构**：Kiro（AWS）｜**日期**：2025-07-14｜[原文](https://kiro.dev/blog/introducing-kiro/)

把「vibe coding 到可上线」之间的鸿沟作为目标：通过 specs（需求用 EARS 记法写验收标准，另有设计与任务）与 hooks（文件保存等事件触发的自动化智能体）把原型变成可维护的生产系统。

### VD16 · Specs（Kiro 文档） {#vd16}
**机构**：Kiro（AWS）｜**日期**：持续更新｜[原文](https://kiro.dev/docs/specs/)

规格由三份文件组成：`requirements.md`（用户故事与验收标准）、`design.md`（架构、组件、数据流、错误处理、测试策略）、`tasks.md`（可追踪的离散实现任务）。是规格驱动开发最「结构化」的一种实现。

`厂商文档`

### VD17 · Context Engineering for AI Agents: Lessons from Building Manus {#vd17}
**作者**：Yichao "Peak" Ji（Manus）｜**日期**：2025-07｜[原文](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)

六条来自生产的经验：围绕 KV 缓存设计（命中率是最重要指标，保持前缀稳定、上下文只追加）；**屏蔽而非移除工具**；把文件系统当作无限的外部上下文；用 todo.md「复述」目标以对抗遗忘；保留错误信息让模型从失败中学习；避免被少样本示例「带偏」成固定模式。

### VD18 · Context Engineering（LangChain） {#vd18}
**作者**：Lance Martin（LangChain）｜**日期**：2025-07-02｜[原文](https://blog.langchain.com/context-engineering-for-agents/)

把上下文工程归纳为四类策略：**Write**（写到上下文外，如草稿本、记忆）、**Select**（按需检索进来）、**Compress**（摘要/裁剪）、**Isolate**（拆到子智能体或沙箱）。是理解各种技巧的好分类框架。

### VD19 · Writing a good CLAUDE.md {#vd19}
**机构**：HumanLayer｜**日期**：2025-11-25｜[原文](https://www.humanlayer.dev/blog/writing-a-good-claude-md)

模型是无状态的，CLAUDE.md 是它了解代码库的唯一常驻入口，但模型也常忽略它。建议：少即是多（作者称前沿推理模型大约能较稳定地遵循 150–200 条指令，社区共识是不超过 300 行、越短越好）；用渐进式披露指向更详细文档；**不要让 LLM 干 linter 的活**——格式与风格交给格式化器/linter，并用 hook 把错误反馈给模型。

> "Never send an LLM to do a linter's job"

`作者经验，非严格实验`

### VD20 · Advanced Context Engineering for Coding Agents（ACE-FCA） {#vd20}
**作者**：Dex Horthy（HumanLayer）｜**日期**：2025｜[原文](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents)

在大型、复杂的存量代码库中使用编码智能体的工作流：**研究 → 计划 → 实现**，围绕「频繁的有意压缩」（frequent intentional compaction）设计整个流程，把上下文利用率保持在约 40–60%，并在研究与计划阶段安排高杠杆的人工评审——因为一行错误的研究或计划会放大成成百上千行错误代码。

`作者自述`
