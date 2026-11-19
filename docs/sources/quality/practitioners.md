# 质量与 CI/CD 专题 · 一线工程师与方法论

> Kent Beck、Simon Willison、Addy Osmani、Birgitta Böckeler、Hamel Husain、Eugene Yan、Shreya Shankar 等人的文章。 每条都有摘要、逐字核对过的原文引文（英文保留原文）和链接；原则编号 Q01–Q13 见 [第 12 章](/handbook/12-quality-cicd#principles)。检索与核对时间：2026-11 中旬。

### QP01 · Kent Beck：增强编程而非氛围编程——在意代码、测试与覆盖率 {#qp01}
**作者/机构**：Kent Beck｜**日期**：2025｜[原文](https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes)

TDD 提出者 Kent Beck 区分“氛围编程”（只在意行为）和“增强编程”（在意代码、复杂度、测试和覆盖率）。他在说明文件里要求智能体遵循 TDD 与 Tidy First：红-绿-重构、只在测试通过时重构、测试名描述行为；并列出需要人工介入的信号，其中之一是智能体在作弊，例如禁用或删除测试。

> “Any indication that the genie was cheating, for example by disabling or deleting tests.”

**证据类型**：作者自述｜**对应原则**：[Q01](/handbook/12-quality-cicd#q01) [Q04](/handbook/12-quality-cicd#q04)

### QP02 · Kent Beck：精灵想要一步跳到终点 {#qp02}
**作者/机构**：Kent Beck｜**日期**：2025｜[原文](https://newsletter.kentbeck.com/p/genie-wants-to-leap)

Kent Beck 观察到智能体倾向于“一大步跳到完成”，而不是小步、每一步都能编译、测试都能跑；他见过非常恶劣的行为：删除测试中的断言、删除整个测试、伪造大段实现。结论是人要把握节奏，强制小步与持续运行测试。

> “I’ve seen truly pernicious behavior like deleting assertions from tests, deleting whole tests, & faking large swathes of implementation.”

**证据类型**：作者自述｜**对应原则**：[Q04](/handbook/12-quality-cicd#q04) [Q01](/handbook/12-quality-cicd#q01) [Q11](/handbook/12-quality-cicd#q11)

### QP03 · Pragmatic Engineer × Kent Beck：TDD 是与 AI 智能体协作的“超能力” {#qp03}
**作者/机构**：Gergely Orosz 访谈 Kent Beck｜**日期**：2025-07-09｜[原文](https://newsletter.pragmaticengineer.com/p/tdd-ai-agents-and-coding-with-kent)

访谈要点：Kent Beck 认为 TDD 是使用 AI 智能体时的“超能力”；单元测试能防止智能体在修改中破坏既有功能；同时他坦言难以阻止智能体为了“通过”而删除测试。

> “Test driven development (TDD) is a “superpower” when working with AI agents.”

**证据类型**：作者自述｜**对应原则**：[Q01](/handbook/12-quality-cicd#q01) [Q04](/handbook/12-quality-cicd#q04)

### QP04 · Simon Willison：你的工作是交付已被证明能工作的代码 {#qp04}
**作者/机构**：Simon Willison｜**日期**：2025-12-18｜[原文](https://simonwillison.net/2025/Dec/18/code-proven-to-work/)

Simon Willison 批评“用 LLM 产出巨大未测试 PR 丢给评审者”的做法：提交前必须自己证明代码能工作——先手工测试（从已知状态出发、执行改动、观察结果，含边界情况），再附上一个“实现被回滚就会失败”的自动化测试；智能体可以替你跑这些检查，但证据由你负责。他也提醒不要因为有自动化测试就跳过手工测试。（此链接 v2 已收录，本专题从质量保障角度重读。）

> “Don’t be tempted to skip the manual test because you think the automated test has you covered already!”

**证据类型**：作者自述｜**对应原则**：[Q02](/handbook/12-quality-cicd#q02) [Q13](/handbook/12-quality-cicd#q13) [Q05](/handbook/12-quality-cicd#q05)

### QP05 · Simon Willison：Vibe engineering——好测试、好评审、可预览环境放大 LLM 价值 {#qp05}
**作者/机构**：Simon Willison｜**日期**：2025-10-07｜[原文](https://simonwillison.net/2025/Oct/7/vibe-engineering/)

与“氛围编程”相对，Simon 用“vibe engineering”描述资深工程师负责任地使用智能体：自动化测试、计划、文档、版本控制、CI、代码评审、手工 QA、预览环境都让智能体更有用；智能体可能没测就声称能用，任何改动也可能悄悄破坏无关功能；擅长代码评审的人与 LLM 合作会更顺利。（此链接 v2 已收录，本专题从质量保障角度重读。）

> “Your agent might claim something works without having actually tested it at all, plus any new change could break an unrelated feature without you realizing it.”

**证据类型**：作者自述｜**对应原则**：[Q02](/handbook/12-quality-cicd#q02) [Q06](/handbook/12-quality-cicd#q06) [Q11](/handbook/12-quality-cicd#q11)

### QP06 · Simon Willison：设计智能体循环——一套干净通过的测试是最大杠杆 {#qp06}
**作者/机构**：Simon Willison｜**日期**：2025-09-30｜[原文](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/)

谈如何为智能体设计“有明确目标、可反复试错”的循环：依赖升级、Dockerfile 瘦身、性能优化都可以交给智能体，前提是有可靠的测试作为判据；凭据只给测试或预发环境，把破坏控制在小范围。

> “The value you can get from coding agents and other LLM coding tools is massively amplified by a good, cleanly passing test suite.”

**证据类型**：作者自述｜**对应原则**：[Q02](/handbook/12-quality-cicd#q02) [Q09](/handbook/12-quality-cicd#q09)

### QP07 · Addy Osmani：AI 写代码更快，你的工作仍是证明它能工作 {#qp07}
**作者/机构**：Addy Osmani｜**日期**：2026-01-07｜[原文](https://addyosmani.com/blog/code-review-ai/)

Google 的 Addy Osmani 谈 AI 时代的代码评审：变更要带着证据（手工验证 + 自动化测试）提交，评审用于把关风险、意图与问责；AI 很擅长起草边界测试，但 AI 评审工具需要仔细配置；安全方面主张“AI 标记、人工核实”的混合模式。

> “Ship changes with evidence like manual verification and automated tests, then use review for risk, intent, and accountability.”

**证据类型**：作者自述｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q13](/handbook/12-quality-cicd#q13) [Q02](/handbook/12-quality-cicd#q02)

### QP08 · Martin Fowler 网站：面向编码智能体用户的 Harness Engineering {#qp08}
**作者/机构**：Birgitta Böckeler（martinfowler.com）｜**日期**：2026｜[原文](https://martinfowler.com/articles/harness-engineering.html)

Thoughtworks 的 Birgitta Böckeler 把 harness 定义为“除模型以外的一切”，并区分前馈的“指南”和反馈的“传感器”；能确定性检查的（lint、结构测试、死代码检测、覆盖质量分析、依赖扫描）应做成计算型传感器，语义判断（语义重复、冗余测试、暴力修复）才交给 LLM，但它昂贵且概率性。她明确提醒：把信任寄托在 AI 生成的测试上，目前还不够好。

> “This approach puts a lot of faith into the AI-generated tests, that's not good enough yet.”

**证据类型**：作者自述｜**对应原则**：[Q02](/handbook/12-quality-cicd#q02) [Q05](/handbook/12-quality-cicd#q05) [Q04](/handbook/12-quality-cicd#q04)

### QP09 · Martin Fowler 网站：Exploring Generative AI 系列（TDD 指令与 AI 失误清单） {#qp09}
**作者/机构**：Birgitta Böckeler 等（martinfowler.com）｜**日期**：2023–2026｜[原文](https://martinfowler.com/articles/exploring-gen-ai.html)

Thoughtworks 长期连载的系列，包含给智能体 TDD 指令前后对代码与测试质量的对比、AI“失误”案例清单，以及用智能体迁移测试框架的实验。团队自称是 TDD 的坚定实践者，也指出两种风险：放大坏实践、以及开发者厌倦不停评审建议。

> “At Thoughtworks, we are strong practitioners of Test Driven Development (TDD).”

**证据类型**：作者自述｜**对应原则**：[Q01](/handbook/12-quality-cicd#q01) [Q06](/handbook/12-quality-cicd#q06)

### QP10 · Hamel Husain：你的 AI 产品需要 Evals {#qp10}
**作者/机构**：Hamel Husain｜**日期**：2024-03-29｜[原文](https://hamel.dev/blog/posts/evals/)

经典长文：把评测分为单元测试式断言、人工与模型评估、A/B 测试三层；断言不仅用于测试，还可用于数据清洗和推理时的自动重试；模型评估器与人工标签对齐后仍需周期性复核一致性。是 LLM 应用“评测即测试”的奠基材料之一。

> “After bringing the model-based evaluator in line with the human, you must continue doing periodic exercises to monitor the model and human agreement.”

**证据类型**：作者自述｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08)

### QP11 · Hamel Husain：AI Evals FAQ（持续更新） {#qp11}
**作者/机构**：Hamel Husain｜**日期**：2026-09-18｜[原文](https://hamel.dev/blog/posts/evals-faq/)

面向工程师与产品经理的 Evals 问答合集：建议先自己标注至少 30 条 trace 再看智能体给出的建议；如何抽样生产 trace；改裁判提示词时用“与人工标签的一致性”来衡量是否变好。核心观点是：先看数据、找失败模式，再自动化。

> “Start by annotating at least 30 traces yourself before reviewing suggestions from an agent.”

**证据类型**：作者自述｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08)

### QP12 · Hamel Husain：LLM-as-a-Judge 完整指南——用人工标签验证裁判 {#qp12}
**作者/机构**：Hamel Husain｜**日期**：2024-10-29｜[原文](https://hamel.dev/blog/posts/llm-judge/)

一步步构建 LLM 裁判并用人工标签验证：看数据之前写不出好的裁判提示词；“一致率”会误导——如果错误只占 5%，一个永远判“通过”的裁判也有 95% 一致率却抓不到任何错误，所以要看精确率/召回率等。

> “For example, if an error occurs in 5% of examples, a judge that always predicts Pass still has 95% agreement while detecting none of the errors.”

**证据类型**：作者自述｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08)

### QP13 · Eugene Yan：LLM 裁判救不了产品，修好流程才行 {#qp13}
**作者/机构**：Eugene Yan｜**日期**：2025-04-20｜[原文](https://eugeneyan.com/writing/eval-process/)

Eugene Yan 认为评测的价值在于流程而非工具：抽样输出、标注质量与缺陷、改进自动评估器，形成“写评测→改系统→跑评测→集成改进”的循环，类似先写测试的 TDD；组织纪律决定这个反馈回路能否维持。

> “write evals, make changes, run evals, integrate improvements”

**证据类型**：作者自述｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08) [Q01](/handbook/12-quality-cicd#q01)

### QP14 · Eugene Yan：LLM 评估器到底有多可靠（文献综述） {#qp14}
**作者/机构**：Eugene Yan｜**日期**：2024-08-18｜[原文](https://eugeneyan.com/writing/llm-evaluators/)

对 LLM-as-Judge 研究的系统综述：直接打分、成对比较、参考答案等方式各有适用场景；部分微调的评估器在公平性测试集上甚至不如随机，说明它们可能过拟合于表面特征。结论是：裁判本身也需要被评测。

> “Similarly, on evaluation datasets for fairness (LLMBar), the finetuned LLM-evaluators performed worse than random guessing, suggesting that they were biased (or perhaps overfitted) on superficial quality.”

**证据类型**：作者自述｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08)

### QP15 · Shreya Shankar 等：谁来验证验证者？ {#qp15}
**作者/机构**：Shreya Shankar 等（arXiv）｜**日期**：2024-04-18｜[原文](https://arxiv.org/abs/2404.12272)

EvalGen 论文：LLM 生成的评估函数会继承被评估 LLM 的所有问题，仍需人工验证；提出混合主动的方法，让用户在标注过程中逐步确定评估标准并实现断言，使评估器与人的要求对齐。

> “Yet LLM-generated evaluators simply inherit all the problems of the LLMs they evaluate, requiring further human validation.”

**证据类型**：研究｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08)
