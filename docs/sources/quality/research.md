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


### 腾讯 · TX20 · CAT：基于检索增强 LLM 的低成本 UI 自动化测试——微信案例 {#tx20}
**作者/机构**：Sidong Feng 等（含微信团队，arXiv / ASE 2024）｜**日期**：2024-09-12｜[原文](https://arxiv.org/abs/2409.07829)

用 RAG 检索微信历史测试样例作为 few-shot，生成动作序列；用传统机器学习做 UI 元素匹配、LLM 只作补充优化器，以控制成本。已集成进微信测试平台。是“LLM 不单干、与确定性方法分工”的工业样本。

> “achieving 90% UI automation with $0.34 cost, outperforming the state-of-the-art”

**证据类型**：论文（工业部署，团队自报）｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05) [P06](/compare/evidence#p06)

### 阿里 · AL11 · AACR-Bench：带仓库上下文的多语言代码评审基准 {#al11}
**作者/机构**：阿里巴巴（GitHub 开源）｜**日期**：2026｜[原文](https://github.com/alibaba/aacr-bench)

评审能力怎么量：200 个真实 PR、50 个开源项目、10 种语言，参考意见来自原始评审讨论与模型生成反馈并经专家标注，另附 155 个 PR 的负样本集（不该报问题的场景）。负样本集是对“评审噪声”的直接度量。

> “The original dataset covers 200 unique pull requests (PRs) from 50 open-source projects across 10 programming languages .”

**证据类型**：开源基准（团队自建）｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q08](/handbook/12-quality-cicd#q08)

### 阿里 · AL14 · Lingma SWE-GPT：面向软件改进的开源过程中心模型 {#al14}
**作者/机构**：Yingwei Ma 等（通义灵码团队，arXiv）｜**日期**：2024-11｜[原文](https://arxiv.org/abs/2411.00622)

不只用静态代码训练，而是学习“真实代码提交过程”——开发者的思考、工具使用、多角色交互，在 SWE-bench Verified 上评测 7B/72B 模型。代表阿里“把软件过程数据当训练信号”的路线。

> “Lingma SWE-GPT systematically incorporates the dynamic interactions and iterative problem-solving inherent in software development process”

**证据类型**：论文（团队自评）｜**对应原则**：[P06](/compare/evidence#p06)

### 阿里 · AL31 · Alipay-PIBench：支付集成场景的 Coding Agent 基准 {#al31}
**作者/机构**：支付宝 / inclusionAI（GitHub 开源）｜**日期**：2026｜[原文](https://github.com/inclusionAI/PIBench)

领域化评测：在真实支付集成任务上评 Coding Agent，并比较“带 Skill / 不带 Skill”两种条件下的 Rubric 通过率。是 Skill 价值的可量化评测思路。

> “Alipay-PIBench is a repository-level benchmark proposed by Alipay”

**证据类型**：开源基准（团队自建）｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08) [P13](/compare/evidence#p13)

### 字节 · BD03 · BitsAI-Fix：字节用 LLM 自动修复 Lint 问题的工业实践 {#bd03}
**作者/机构**：Yuanpeng Li 等（字节跳动，arXiv）｜**日期**：2025-08｜[原文](https://arxiv.org/abs/2508.03487)

把静态分析告警的修复交给 LLM：冷启动阶段自动获取可验证训练数据，上线后用线上反馈持续迭代；奖励函数同时看格式与正确性，并惩罚冗余修改；用“code diff 匹配”持续追踪线上真实效果。与 QC09（BitsAI-CR）同属字节 BitsAI 体系。

> “In production deployment at ByteDance, our solution has supported over 5,000 engineers, resolved more than 12,000 static analysis issues, achieved approximately 85% remediation accuracy, with around 1,000 weekly active adopters.”

**证据类型**：论文（工业部署，团队自报）｜**对应原则**：[Q03](/handbook/12-quality-cicd#q03) [Q12](/handbook/12-quality-cicd#q12) [P19](/compare/evidence#p19)

### 字节 · BD04 · LogSage：LLM 驱动的 CI/CD 失败检测与修复（ASE 2025） {#bd04}
**作者/机构**：Weiyuan Xu 等（字节跳动，arXiv）｜**日期**：2025-06｜[原文](https://arxiv.org/abs/2506.03691)

CI/CD 失败日志的根因分析与修复建议：用 LLM 做根因分析，再用 RAG 复用历史修复、通过工具调用执行自动修复。字节内部一年部署，处理超过 107 万次执行，端到端精度超 80%。是“AI 进流水线”而不是“AI 进 IDE”的样本。

> “In a year-long industrial deployment at ByteDance, it processed over 1.07M executions”

**证据类型**：论文（工业部署，团队自报）｜**对应原则**：[Q03](/handbook/12-quality-cicd#q03) [Q10](/handbook/12-quality-cicd#q10)

### 字节 · BD06 · AEGIS：基于 Agent 的通用 Bug 复现脚本生成（FSE 2025） {#bd06}
**作者/机构**：Xinchen Wang 等（字节跳动 Trae 团队与高校，arXiv）｜**日期**：2024-11｜[原文](https://arxiv.org/abs/2411.18015)

先复现再修：从 issue 描述自动生成能复现 bug 的脚本，用“精简上下文构建”和“有限状态机约束的多反馈优化”约束 Agent 行为，避免长上下文和无序动作。是测试先行（先有失败用例）在 Agent 场景的工程化。

> “we propose an Automated gEneral buG reproductIon Scripts generation framework, named AEGIS, which is the first agent-based framework for the task.”

**证据类型**：论文｜**对应原则**：[Q01](/handbook/12-quality-cicd#q01) [P07](/compare/evidence#p07) [P04](/compare/evidence#p04)

### 字节 · BD07 · TestGPT-Server：在字节用 LLM 自动测试微服务（FSE 2025 工业论文） {#bd07}
**作者/机构**：Jue Wang 等（字节跳动）｜**日期**：2025-06｜[原文](https://conf.researchr.org/details/fse-2025/fse-2025-industry-papers/17/TestGPT-Server-Automatically-Testing-Microservices-with-Large-Language-Models-at-Byt)

LLM 生成测试请求，LLM 辅助的响应分析器识别崩溃，断言挖掘器自动提取功能断言。在 14,366 个微服务 API 上发现 50 个崩溃 bug 和 2 个功能 bug——功能 bug 数量之少本身说明“自动断言”仍是难点。（ACM 全文页 403，这里引用会议页摘要）

> “identifying 50 crash bugs and 2 functional bugs across 14,366 microservice APIs, with minimal manual effort”

**证据类型**：论文（工业部署，团队自报）｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05) [Q02](/handbook/12-quality-cicd#q02)

### 字节 · BD08 · Multi-SWE-bench：多语言 issue 修复基准 {#bd08}
**作者/机构**：Daoguang Zan 等（字节跳动 Seed，arXiv）｜**日期**：2025-04｜[原文](https://arxiv.org/abs/2504.02605)

把 SWE-bench 扩展到 Java、TS、JS、Go、Rust、C、C++，并重视人工标注质量；同时开放 RL 训练用实例社区。是字节在“评测基础设施”上的公共贡献。

> “It includes a total of 1,632 high-quality instances, which were carefully annotated from 2,456 candidates by 68 expert annotators”

**证据类型**：论文（开源基准）｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08)
