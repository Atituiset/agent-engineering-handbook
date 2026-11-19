# 质量与 CI/CD 专题 · 开源项目政策与工具

> 开源项目如何约束 AI 贡献，以及开源质量工具。 每条都有摘要、逐字核对过的原文引文（英文保留原文）和链接；原则编号 Q01–Q13 见 [第 12 章](/handbook/12-quality-cicd#principles)。检索与核对时间：2026-11 中旬。

### QO01 · LLVM：AI 工具使用政策——贡献者必须读过并审查所有 LLM 生成内容 {#qo01}
**作者/机构**：LLVM 项目｜**日期**：2025–2026｜[原文](https://llvm.org/docs/AIToolPolicy.html)

LLVM 的政策要求贡献者在提交前阅读并审查所有 LLM 生成的代码或文本，并对 AI 辅助的贡献做标注；标注的目的是方便评审，而不是追踪哪部分由 AI 写。政策的出发点是珍惜维护者有限的评审时间，不让“提取式贡献”浪费它。

> “Contributors must read and review all LLM-generated code or text before they”

**证据类型**：开源治理｜**对应原则**：[Q13](/handbook/12-quality-cicd#q13) [Q06](/handbook/12-quality-cicd#q06)

### QO02 · QEMU：代码来源（provenance）政策 {#qo02}
**作者/机构**：QEMU 项目｜**日期**：持续更新｜[原文](https://www.qemu.org/docs/master/devel/code-provenance.html)

QEMU 的贡献文档强调 Signed-off-by 等来源声明的法律含义，要求生成文件必须声明来源；针对 AI 辅助开发的增多，政策拒绝被认为包含或源自 AI 生成内容的贡献（研究 API 等其他 AI 用途不在此列），主要顾虑是版权与许可。是“来源可追溯”在开源治理中最严格的例子。

> “believed to include or derive from AI generated content”

**证据类型**：开源治理｜**对应原则**：[Q13](/handbook/12-quality-cicd#q13)

### QO03 · Ghostty：AI 使用政策（必须披露、必须能解释） {#qo03}
**作者/机构**：Ghostty 项目（Mitchell Hashimoto）｜**日期**：持续更新｜[原文](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md)

Ghostty 的 AI 政策：任何形式的 AI 使用都必须披露（写明工具与辅助程度）；人必须完全理解所有代码——如果不借助 AI 工具就无法解释改动做了什么、如何与系统交互，就不要贡献；AI 生成的内容提交前必须经人审阅和精简；明显是 AI 垃圾的贡献者会被列入公开名单并阻止后续贡献。

> “All AI usage in any form must be disclosed.”

**证据类型**：开源治理｜**对应原则**：[Q13](/handbook/12-quality-cicd#q13) [Q06](/handbook/12-quality-cicd#q06)

### QO04 · curl：死于一千份 AI 垃圾报告 {#qo04}
**作者/机构**：Daniel Stenberg（curl 作者）｜**日期**：2025-07-14｜[原文](https://daniel.haxx.se/blog/2025/07/14/death-by-a-thousand-slops/)

curl 作者描述 AI 生成的低质量漏洞报告如何消耗维护者精力，并列出典型例子。虽然对象是安全报告而非 PR，但反映了同一问题：没有验证证据的 AI 产出会把成本转嫁给评审者。作者表示要用 2025 年余下时间评估对策。

> “I want us to use the rest of the year 2025 to evaluate and think.”

**证据类型**：作者自述｜**对应原则**：[Q13](/handbook/12-quality-cicd#q13)

### QO05 · Mutahunter：语言无关的 LLM 变异测试工具 {#qo05}
**作者/机构**：codeintegrity-ai（GitHub）｜**日期**：2024–2025｜[原文](https://github.com/codeintegrity-ai/mutahunter)

开源的 LLM 驱动变异测试工具，利用 LLM 生成上下文相关的变异体来检验测试套件的缺陷检出能力，可接入 CI。代表了“用变异分数而非覆盖率衡量测试质量”的工具化方向。项目自述，未独立评估。

> “Open-Source Language Agnostic LLM-based Mutation Testing”

**证据类型**：项目自述｜**对应原则**：[Q05](/handbook/12-quality-cicd#q05)


### 阿里 · AL08 · Open Code Review：阿里开源的 AI 代码评审 CLI（精度优先的取舍） {#al08}
**作者/机构**：阿里巴巴（GitHub 开源）｜**日期**：2026｜[原文](https://github.com/alibaba/open-code-review)

阿里集团 AI 代码评审团队开源的 CLI：批评通用 Agent 做评审会“偷工减料”、只看部分文件、定位漂移，于是用确定性工程（文件全覆盖、定位校准）+ Agent 协同；README 自报相同模型下 Precision/F1 高于 Claude Code、token 约 1/9，并明说 Recall 更低是有意取舍。独立复测见 AL09。

> “Note that its Recall is lower than general-purpose agents — a deliberate trade-off favoring precision over noise.”

**证据类型**：开源仓库 README（团队自报 benchmark）｜**对应原则**：[Q06](/handbook/12-quality-cicd#q06) [Q04](/handbook/12-quality-cicd#q04)
