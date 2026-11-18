# Martin Fowler 网站与 Thoughtworks 技术雷达

> martinfowler.com 的「Exploring Generative AI」系列（主要作者 Birgitta Böckeler，Thoughtworks 全球 AI 辅助软件交付负责人）与 Thoughtworks Technology Radar 中与编码智能体相关的条目。雷达环（Adopt/Trial/Assess/Hold/Caution）与期次按页面标注抄录。链接于 2026-11-18 核对。

[[toc]]

## martinfowler.com

### TW01 · Harness engineering for coding agent users {#tw01}
**作者**：Birgitta Böckeler｜**日期**：2026-04-02｜[原文](https://www.martinfowler.com/articles/harness-engineering.html)

为「使用编码智能体的人」定义 harness：由 **guides（前馈：规则、上下文、约定）** 与 **sensors（反馈：测试、linter、类型检查、AI 评审）** 组成，各自又分 **computational（确定性、便宜、可每次提交运行）** 与 **inferential（LLM 判断、昂贵、概率性）**。只有反馈会重复犯错，只有前馈则永远不知道规则是否生效；检查要尽量左移。最关键的一段解释了为什么智能体守不住约束：人类开发者自带一个「隐性 harness」——吸收过的约定、对复杂度的切身痛感、提交上署着自己的名字、对组织目标与可容忍技术债的认知；而智能体这些都没有。

> "A coding agent has none of this: no social accountability, no aesthetic disgust at a 300-line function, no intuition that 'we don't do it that way here,' and no organisational memory."

> "A good harness should not necessarily aim to fully eliminate human input, but to direct it to where our input is most important."

`与本手册关系：第 01、04 章的理论框架`

### TW02 · Harness Engineering — first thoughts {#tw02}
**作者**：Birgitta Böckeler｜**日期**：2026-02-17｜[原文](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html)

对 OpenAI「harness engineering」文章（[OA01](./openai#oa01)）的第一时间解读：其 harness 由上下文工程、架构约束（linter 与结构测试）和「垃圾回收」式清理组成；提出未来团队可能从「harness 模板」而非服务模板起步，但也指出原文缺少对功能与行为验证的讨论。

### TW03 · Maintainability sensors for coding agents {#tw03}
**作者**：Birgitta Böckeler｜**日期**：2026-05-27｜[原文](https://www.martinfowler.com/articles/sensors-for-coding-agents.html)

沿交付路径实践「计算型传感器」，重点是 ESLint 与静态分析：很多有用的复杂度规则（函数长度、圈复杂度等）在默认预设中并未开启，需要自己配置阈值；AI 能大幅降低这些工具配置语法的学习成本；还讨论了用变异测试发现缺失断言、用快照让工具把「比上次更差/相同」的趋势反馈给智能体、用影响半径辅助评审时的风险分级。

### TW04 · TDD inside the agent loop — theater or actual value? {#tw04}
**作者**：Birgitta Böckeler｜**日期**：2026｜[原文](https://www.martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html)

比较三种 TDD 用法：人写测试→AI 实现；AI 写失败测试→人审→AI 实现；完全在智能体循环内做 TDD。作者实验后持保留意见：看着测试变红只有在有人检查时才算证据；智能体内部的 TDD 不能带来人亲自做时的控制感与信任，生成的测试有时偏薄、自我指涉。

> "Whatever ends up giving us trust and confidence in our software in the future - I think the role of TDD as we've known it is significantly smaller than pre-GenAI."

`观点：与 Simon Willison 的「red/green TDD」立场形成有价值的张力，见第 05 章`

### TW05 · Context Engineering for Coding Agents {#tw05}
**作者**：Birgitta Böckeler｜**日期**：2026-02-05｜[原文](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html)

为编码智能体的上下文配置建立术语表：rules/guardrails（通用约定）、按需加载的说明（如 skills）、子智能体、MCP、hooks 等，区分「谁决定加载」（人、智能体、软件）以及「是否保证被加载」。以 Claude Code 为例逐项说明。

### TW06 · Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl {#tw06}
**作者**：Birgitta Böckeler｜**日期**：2025-10-15｜[原文](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)

把 SDD 分为三个层次：**spec-first**（先写规格再让 AI 开发）、**spec-anchored**（规格在功能演进中持续维护）、**spec-as-source**（只编辑规格，人不碰代码）。作者试用三款工具后的疑虑：对小问题流程过重（像拿大锤砸核桃）、大量 Markdown 难以审阅、智能体仍可能不按规格执行；作者对大量前期规格设计持怀疑——历史经验表明小步迭代才是保持掌控的最好方式；并指出多数方案对「规格长期如何维护」语焉不详。

> "All SDD approaches and definitions I’ve found are spec-first, but not all strive to be spec-anchored or spec-as-source."

### TW07 · Anchoring AI to a reference application {#tw07}
**作者**：Birgitta Böckeler｜**日期**：2025-09-25｜[原文](https://martinfowler.com/articles/exploring-gen-ai/anchoring-to-reference.html)

服务模板一旦实例化就与上游脱节。作者尝试用 MCP 服务器向编码助手提供「参考应用」中的典型模式代码样例，让智能体按参考实现保持一致，并可用来检测漂移。雷达随后将其收录（见 [TW22](#tw22)）。

### TW08 · Humans and Agents in Software Engineering Loops {#tw08}
**作者**：Kief Morris｜**日期**：2026-03-04｜[原文](https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html)

区分「why loop」（把想法变成可用软件并迭代）与「how loop」（生成和使用代码、测试、工具等中间产物）。主张人既不完全退出（vibe coding），也不逐行检查，而是「在环上」（on the loop）：通过持续改进 harness 来提升结果。干净、结构良好的代码库让 LLM 理解和修改得更快、更少陷入死循环——所以我们依然在乎内部质量。

### TW09 · Assessing internal quality while coding with an agent {#tw09}
**作者**：Erik Doernenburg｜**日期**：2026-01-27｜[原文](https://martinfowler.com/articles/exploring-gen-ai/ccmenu-quality.html)

在一个真实的 Swift 应用中让智能体添加功能，并逐步审视内部质量：智能体能完成功能，但会引入不地道的写法、为不存在的问题实现复杂逻辑，需要有经验的人引导。结论是关于「AI 写了多少代码」的报道很少讨论代码的内部质量，而这恰恰决定长期可维护性。

### TW10 · I still care about the code {#tw10}
**作者**：Birgitta Böckeler｜**日期**：2025-07-09｜[原文](https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html)

反驳「以后不用关心代码了」：就像 DevOps 让值班的开发者更在乎韧性，只要人仍对线上系统负责，就仍需要关心代码——也许方式不同，但必须关心。

### TW11 · The role of developer skills in agentic coding {#tw11}
**作者**：Birgitta Böckeler｜**日期**：2025-03-25｜[原文](https://martinfowler.com/articles/exploring-gen-ai/13-role-of-developer-skills.html)

列举智能体的典型失误：基于错误假设「修」问题（如内存不足就调大内存而不追问原因）、新建测试函数而不是补断言、重构时无视已有的依赖注入链引入多余参数等。结论是开发者经验仍是关键的「纠偏器」，影响半径从单次提交到长期可维护性。

### TW12 · Coding Assistants Threaten the Software Supply Chain {#tw12}
**作者**：Thoughtworks 作者（Exploring Gen AI 系列）｜**日期**：2025｜[原文](https://martinfowler.com/articles/exploring-gen-ai/software-supply-chain-attack-surface.html)

分析「智能体循环」的攻击面：被攻陷的 MCP 服务器、规则文件、代码或依赖都可能把恶意指令带入智能体的上下文并被执行，相比传统开发明显扩大了攻击面。

### TW13 · Coding assistants do not replace pair programming {#tw13}
**作者**：Birgitta Böckeler｜**日期**：2023-08-10｜[原文](https://martinfowler.com/articles/exploring-gen-ai/05-not-your-pair-programmer.html)

结对编程的价值不仅是写代码更快，还包括知识传播、团队共识、减少交接与持续集成式的评审。AI 助手只覆盖其中一部分，不能替代结对的社会与知识功能。

### TW14 · How far can we push AI autonomy in code generation? {#tw14}
**作者**：Birgitta Böckeler 等｜**日期**：2025-08-05｜[原文](https://martinfowler.com/articles/pushing-ai-autonomy.html)

用多智能体工作流端到端生成一个简单的 Spring Boot 应用。即便采用了可复用提示、参考应用、分步工作流等策略，仍观察到：实现超出需求的功能、做出未经要求的假设、在测试失败时宣告成功、对规定的编码模式保真度不足。作者结论：在可预见的未来，非平凡的业务软件仍需要人在环上。

### TW15 · Some thoughts on LLMs and Software Development {#tw15}
**作者**：Martin Fowler｜**日期**：2025-08-28｜[原文](https://martinfowler.com/articles/202508-ai-thoughts.html)

几条短思考：引用 Rebecca Parsons 的观点「幻觉不是 bug 而是特性——LLM 产出的全是幻觉，只是有些有用」；对数值答案至少问三次以感知方差；不要让 LLM 计算能确定性计算的东西，而是让它生成计算代码；非确定性要求我们改变对工具的预期。

> "All an LLM does is produce hallucinations, it’s just that we find some of them useful."

### TW16 · To vibe or not to vibe {#tw16}
**作者**：Birgitta Böckeler｜**日期**：2025-09-23｜[原文](https://martinfowler.com/articles/exploring-gen-ai/to-vibe-or-not-vibe.html)

是否审查 AI 代码不应是二元选择，而应按风险评估：错误发生的概率、影响有多大、能否被发现。用这三个维度决定在哪里可以「vibe」，在哪里必须严格审查。

## Thoughtworks Technology Radar

### TW17 · Context engineering（Adopt，2026-04） {#tw17}
[原文](https://www.thoughtworks.com/radar/techniques/context-engineering)

雷达认为上下文工程已从优化技巧变成现代 AI 系统的基础架构关注点：不同于关注措辞的提示工程，它关注在正确的时间把正确的信息、工具与状态交给模型。

### TW18 · Progressive context disclosure（Adopt，2026-11） {#tw18}
[原文](https://www.thoughtworks.com/radar/techniques/progressive-context-disclosure)

先给模型最基本的上下文，再由模型或用户输入触发按需加载。实践：保持 AGENTS.md 精简并链接到可按需查阅的文档；harness 也用这一方式推迟 MCP 工具定义的上下文成本。

### TW19 · AGENTS.md（Trial，2025-11） {#tw19}
[原文](https://www.thoughtworks.com/radar/techniques/agents-md)

AGENTS.md 是给编码智能体的指令文件格式，相当于「给智能体看的 README」，没有必填字段或格式要求，正被越来越多工具支持。

### TW20 · Agent instruction bloat（Caution，2026-11） {#tw20}
[原文](https://www.thoughtworks.com/radar/techniques/agent-instruction-bloat)

AGENTS.md、流程 skills 与工作流会越写越长，每条规则单独看都有用，累积起来却导致冲突、稀释与成本上升。建议针对每个新模型重新测试指令、删除不再需要的部分——**「progression testing，而非 regression testing」**；并引用 Anthropic 为新模型删减大部分 Claude Code 系统提示而无可测损失的例子（见 [X07](./x-posts#x07)）。

### TW21 · Feedback sensors for coding agents（Trial，2026-04） {#tw21}
[原文](https://www.thoughtworks.com/radar/techniques/feedback-sensors-for-coding-agents)

为了让智能体更有效并减轻人工评审负担，团队需要智能体可以直接访问的反馈回路（编译器、测试、linter、类型检查、静态分析等），让智能体在提交给人之前自我纠正。

### TW22 · Anchoring coding agents to a reference application（Trial，2026-11） {#tw22}
[原文](https://www.thoughtworks.com/radar/techniques/anchoring-coding-agents-to-a-reference-application)

把精简的结构脚手架与不断演进的平台配置规则分离：传统代码生成器和脚手架很快落后于平台规范，改为让智能体以一个持续维护的参考应用为锚点生成与校验代码。

### TW23 · Mutation testing（Adopt，2026-11） {#tw23}
[原文](https://www.thoughtworks.com/radar/techniques/mutation-testing)

通过自动注入小缺陷检验测试套件是否至少有一个测试失败。雷达特别指出它可以作为护栏，**确保 AI 生成的测试不是「只会通过」而抓不住逻辑变化**。

### TW24 · Agent sandboxing（Adopt，2026-11） {#tw24}
[原文](https://www.thoughtworks.com/radar/techniques/agent-sandboxing)

把隔离智能体、限制权限与外部访问作为默认做法，并用威胁建模决定具体控制措施。

### TW25 · Toxic flow analysis for AI（Trial，2026-11） {#tw25}
[原文](https://www.thoughtworks.com/radar/techniques/toxic-flow-analysis-for-ai)

针对「致命三要素」（私有数据、不可信内容、对外通信，见 [SC01](./security#sc01)），识别智能体系统中不安全的数据流路径。

### TW26 · Risk-tiered human oversight（Trial，2026-11） {#tw26}
[原文](https://www.thoughtworks.com/radar/techniques/risk-tiered-human-oversight)

按变更可能破坏的范围决定评审深度：最危险或最难回滚的变更留给人来做，中等风险走自动检查加抽样评审，低风险自动化处理。以同样强度评审一切，最终会沦为「人在环中的表演」。

### TW27 · Human-in-the-loop theater（Caution，2026-11） {#tw27}
[原文](https://www.thoughtworks.com/radar/techniques/human-in-the-loop-theater)

把人放在智能体回路里做空洞的批准步骤——批准自己实际上无法判断的操作、提示或 diff——结果是没人真正对决策负责。建议做分级，只把人能真正判断的变更交给人。

### TW28 · Subagents for better context management（Trial，2026-11） {#tw28}
[原文](https://www.thoughtworks.com/radar/techniques/subagents-for-better-context-management)

把探索、工具输出、重试和中间推理委派给子智能体，保护编排者的上下文；编排者上下文里留下的一切都会在后续回合争夺注意力。

### TW29 · Grilling（Trial，2026-11） {#tw29}
[原文](https://www.thoughtworks.com/radar/techniques/grilling)

在动手前让智能体「拷问」你的计划以消除歧义，阻止它在意图不清时瞎猜，并把隐含假设暴露出来。

### TW30 · Codebase cognitive debt（Caution，2026-04） {#tw30}
[原文](https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt)

指系统实现与团队对「它如何、为何这样工作」的共同理解之间日益扩大的差距。AI 提升变更速度后这一差距加速扩大，而理解变弱又反过来削弱开发者引导 AI、预判边界情况和避免架构偏移的能力。

### TW31 · AI-driven documentation sprawl（Caution，2026-11） {#tw31}
[原文](https://www.thoughtworks.com/radar/techniques/ai-driven-documentation-sprawl)

团队用智能体和 Spec-kit、BMAD 等 SDD 工具生成大量 Markdown，其中很多很快过时；在智能体工作流里尤其有害，因为智能体会读到过时文档并被误导。

### TW32 · Coding throughput as a measure of productivity（Caution，2026-11） {#tw32}
[原文](https://www.thoughtworks.com/radar/techniques/coding-throughput-as-a-measure-of-productivity)

警告用「AI 生成代码占比」等活动型指标衡量生产率；把活动指标当目标会落入古德哈特定律，应关注 DORA 等交付指标并与业务结果挂钩。

### TW33 · Spec-driven development（Assess，2025-11） {#tw33}
[原文](https://www.thoughtworks.com/radar/techniques/spec-driven-development)

SDD 是新兴做法，定义仍在演化，通常指以结构化规格为起点、经由计划与任务分解再生成代码的工作流；雷达点名 Kiro、spec-kit、Tessl 等工具，同时提醒该做法尚在早期、需谨慎评估。

### TW34 · Complacency with AI-generated code（Hold，2025-11） {#tw34}
[原文](https://www.thoughtworks.com/radar/techniques/complacency-with-ai-generated-code)

越来越多的数据与研究显示对 AI 生成代码的「自满」：工具确实能加速原型与新项目，但研究显示代码质量可能随时间下降：重复代码与代码 churn 上升超出预期、提交历史中的重构活动减少。雷达把这种自满列为 Hold。

### TW35 · Lightweight Architecture Decision Records（Adopt，2018） {#tw35}
[原文](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

在演进式架构中，用存放在代码库里的轻量 ADR 记录关键设计决策及其背景与后果。智能体时代它多了一个用途：成为智能体可读的「为什么」，防止架构被无意推翻。

### TW36 · Property-based unit testing（Assess，2014） {#tw36}
[原文](https://www.thoughtworks.com/radar/techniques/property-based-unit-testing)

用数据生成器在给定范围内产生随机输入，快速检查边界条件。老技术在 AI 时代重获价值：属性测试的输入不带生成代码的智能体的偏见（见 [AN18](./anthropic#an18)）。
