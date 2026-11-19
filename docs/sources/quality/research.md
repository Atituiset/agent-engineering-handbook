# 质量与 CI/CD 专题 · 研究与数据

> METR、DORA、学术论文与厂商报告。厂商报告单独标注。 每条都有摘要、逐字核对过的原文引文（英文保留原文）和链接；原则编号 Q01–Q13 见 [第 12 章](/handbook/12-quality-cicd#principles)。检索与核对时间：2026-11 中旬。

### QR01 · METR：前沿模型正在奖励投机（reward hacking） {#qr01}
**作者/机构**：METR｜**日期**：2025-06-05｜[原文](https://metr.org/blog/2025-06-05-recent-reward-hacking/)

METR 在评测中观察到前沿模型会“作弊”拿到不可能的高分，例如修改计时器、篡改评分代码、找参考答案；有时模型会明说策略，有时需要熟悉任务并仔细读代码才能识别。对工程团队的含义：测试与评分器本身就是攻击面，需要保护与审计。

> “In our experience, manually recognizing reward hacking can be easy in some cases when the model explicitly describes its strategy, but in other cases it can require familiarity with the task and careful reading of the co”

**证据类型**：研究｜**对应原则**：[Q04](/handbook/12-quality-cicd#q04)

### QR02 · ImpossibleBench：度量智能体“利用测试用例”的倾向 {#qr02}
**作者/机构**：Zhong 等（arXiv）｜**日期**：2025-10-23｜[原文](https://arxiv.org/abs/2510.20270)

构造规格与单元测试直接冲突的“不可能任务”，任何通过都意味着违反规格的捷径，以此度量作弊率。论文举例：能访问单元测试的智能体可能会删掉失败测试，而不是修复底层 bug；并发现提示词、测试访问权限和反馈循环都会显著影响作弊率。

> “For example, an LLM agent with access to unit tests may delete failing tests rather than fix the underlying bug.”

**证据类型**：研究｜**对应原则**：[Q04](/handbook/12-quality-cicd#q04)

### QR03 · METR：早期 2025 年 AI 对资深开源开发者效率的影响（RCT） {#qr03}
**作者/机构**：METR｜**日期**：2025-07-10｜[原文](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

随机对照试验：16 位资深开源维护者在自己熟悉的大型仓库里完成真实任务，使用 AI 时平均反而更慢（研究结论，作者给出多个可能原因）。研究强调基准测试与真实工作的差距：真实任务需要满足评审、风格、测试与文档要求，而基准多用算法化评分。（此链接 v2 已收录，本专题从质量保障角度重读。）

> “Human user is satisfied code will pass review - including style, testing, and documentation requirements”

**证据类型**：研究｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12)

### QR04 · METR：算法评分 vs 整体评估——“测试通过”的 PR 多数仍不可合并 {#qr04}
**作者/机构**：METR｜**日期**：2025-08-13｜[原文](https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/)

METR 在两个大型开源仓库的 18 个真实任务上发现：早期 2025 年的智能体常能写出功能正确的代码，却因测试覆盖、格式/lint、通用代码质量等问题无法直接使用；估计平均需要 42 分钟才能把智能体 PR 改到可合并状态。说明只看“测试通过”的算法化指标会高估可交付性。

> “We estimate that on average, the agent PRs would take 42 minutes to modify/fix to be in a mergeable state.”

**证据类型**：研究｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [Q05](/handbook/12-quality-cicd#q05)

### QR05 · Are “Solved Issues” in SWE-bench Really Solved Correctly? {#qr05}
**作者/机构**：Wang 等（arXiv）｜**日期**：2025-03-19｜[原文](https://arxiv.org/abs/2503.15223)

对 SWE-bench Verified 上“已解决”补丁的实证研究：基准靠测试验证补丁，但测试很少是穷尽的，补丁可能通过测试却不符合开发者预期。作者对三种工具生成的“看似正确”的补丁做了深入测试并与人工补丁比较。提醒团队：测试集是预言机，也有漏洞。

> “However, because testing is rarely exhaustive, a patch may pass the tests but nevertheless fail to match the developers' expectations.”

**证据类型**：研究｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05) [Q04](/handbook/12-quality-cicd#q04)

### QR06 · DORA 2025：AI 是放大器，吞吐上升但交付稳定性仍受损 {#qr06}
**作者/机构**：InfoQ（报道 DORA 2025 报告）｜**日期**：2025-09-29｜[原文](https://www.infoq.com/news/2025/09/dora-state-of-ai-in-dev-2025/)

InfoQ 报道 Google DORA《AI 辅助软件开发现状 2025》：AI 是放大器，放大组织既有的优势与短板；只有 3% 的开发者对 AI 生成的输出“高度信任”；研究团队检验了“AI 带来的速度能否通过快速失败与快速修复抵消不稳定性”，结论是否定的。平台工程与价值流管理被视为关键基础。

> “The research team investigated whether AI speed improvements would compensate for instability through rapid failure and quick repair methods, but their analysis showed no positive results.”

**证据类型**：研究｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12) [Q11](/handbook/12-quality-cicd#q11)

### QR07 · DORA 2025 报告页：回报来自组织系统而非工具本身 {#qr07}
**作者/机构**：Google DORA｜**日期**：2025｜[原文](https://dora.dev/research/2025/dora-report/)

DORA 官方报告页的核心结论：AI 投资的最大回报不是来自工具本身，而是来自对底层组织系统（平台、流程、反馈回路）的战略性投入。与上一条报道配合阅读。（此链接 v2 已收录，本专题从质量保障角度重读。）

> “The greatest returns on AI investment come not from the tools themselves, but from a strategic focus on the underlying organizational system.”

**证据类型**：研究｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12)

### QR08 · CodeRabbit 报告：AI 参与的 PR 问题更多（厂商数据） {#qr08}
**作者/机构**：CodeRabbit｜**日期**：2025-12-17｜[原文](https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report)

AI 评审厂商 CodeRabbit 基于其平台数据比较 AI 参与与纯人工 PR：AI PR 的问题更多、高问题量的离群 PR 更常见，带来更重的评审负担；性能回退虽少但明显偏向 AI；即便有格式化器和 linter，风格漂移仍更常见。建议之一是用 CI 强制的格式化器、linter 与风格指南在评审前消除整类问题。厂商自报、尚未独立验证（该厂商销售评审产品）。

> “CI-enforced formatters, linters, and style guides eliminate entire categories of AI-driven issues before review.”

**证据类型**：厂商自报｜**对应原则**：[Q03](/handbook/12-quality-cicd#q03) [Q06](/handbook/12-quality-cicd#q06) [Q12](/handbook/12-quality-cicd#q12)

### QR09 · GitClear：AI 时代代码克隆与短期 churn 上升 {#qr09}
**作者/机构**：GitClear｜**日期**：2025｜[原文](https://www.gitclear.com/ai_assistant_code_quality_2025_research)

GitClear 基于其代码分析数据库报告：重复代码块显著增加，短期 churn（写下后很快被改写的代码）上升，代码复用下降。厂商自报、尚未独立验证。提示团队用“重复率、churn、回滚率”等结果指标监控 AI 产出，而非只看行数。（此链接 v2 已收录，本专题从质量保障角度重读。）

> “We observe a spike in the prevalence of duplicate code blocks, along with increases in short-term churn code,”

**证据类型**：厂商自报｜**对应原则**：[Q12](/handbook/12-quality-cicd#q12)

### QR10 · Veracode：GenAI 代码安全报告 {#qr10}
**作者/机构**：Veracode｜**日期**：2025｜[原文](https://www.veracode.com/blog/genai-code-security-report/)

安全厂商 Veracode 用安全测试评估多种大模型生成的代码样本，称 45% 的样本未通过安全测试、引入 OWASP Top 10 漏洞。厂商自报、尚未独立验证。支持把 SAST 等安全扫描作为 AI 代码的必经门禁。

> “45% of code samples failed security tests and introduced OWASP Top 10 security vulnerabilities into the code.”

**证据类型**：厂商自报｜**对应原则**：[Q03](/handbook/12-quality-cicd#q03) [Q09](/handbook/12-quality-cicd#q09)
