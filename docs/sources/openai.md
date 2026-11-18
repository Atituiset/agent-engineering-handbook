# OpenAI / Codex

> OpenAI 工程博客、Codex 文档与 Cookbook 中关于编码智能体实践的原文。涉及 OpenAI 内部效率、代码量等数字均为 **「厂商自报、尚未独立验证」**。所有链接于 2026-11-18 打开核对（openai.com 部分页面对脚本返回 403，已用浏览器式抓取确认内容）。

[[toc]]

### OA01 · Harness engineering: leveraging Codex in an agent-first world {#oa01}
**作者**：Ryan Lopopolo（OpenAI）｜**日期**：2026-02-11｜[原文](https://openai.com/index/harness-engineering/)

一个团队以「0 行手写代码」为硬约束，五个月内由 Codex 写出约百万行代码的内部产品（约 1,500 个合并 PR，3 名工程师起步，人均每天约 3.5 个 PR）。关键教训：(1) 早期慢不是因为模型不行，而是**环境欠规范**——失败时问「缺了什么能力、如何让它对智能体可读且可强制执行」；(2) **给地图而不是千页手册**：约 100 行的 AGENTS.md 只做目录，知识放在结构化 `docs/` 里作为事实源；(3) **强制不变量、不微观管理实现**：每个业务域固定分层（Types → Config → Repo → Service → Runtime → UI），依赖方向由自定义 linter 和结构测试机械校验；(4) 让 UI、日志、指标对智能体可读（每个 worktree 可独立启动、接入 Chrome DevTools Protocol、LogQL/PromQL）；(5) 智能体会复制仓库里已有的坏模式，团队曾每周五花 20% 时间清理「AI slop」，后改为把「黄金原则」编码进仓库并让后台任务持续扫描、开重构 PR，像垃圾回收一样偿还技术债。

> "When something failed, the fix was almost never 'try harder.' ... human engineers always stepped into the task and asked: 'what capability is missing, and how do we make it both legible and enforceable for the agent?'"

> "By enforcing invariants, not micromanaging implementations, we let agents ship fast without undermining the foundation."

作者也坦承：尚不知道完全由智能体生成的系统的架构一致性在多年尺度上如何演化。

`与本手册关系：第 04 章核心案例` `厂商自报、尚未独立验证`

### OA02 · Unrolling the Codex agent loop {#oa02}
**作者**：Michael Bolin（OpenAI）｜**日期**：2026-01-23｜[原文](https://openai.com/index/unrolling-the-codex-agent-loop/)

系列文章第一篇，拆解 Codex CLI 的智能体循环：组装指令与上下文 → 推理 → 模型要么回答、要么请求工具调用 → 执行工具并把输出追加回上下文 → 重复。还介绍了提示缓存、上下文增长与自动压缩（`/responses/compact` 端点）等实现细节。适合想理解「harness 到底做了什么」的工程师。

### OA03 · Custom instructions with AGENTS.md {#oa03}
**机构**：OpenAI（Codex 文档）｜**日期**：持续更新｜[原文](https://developers.openai.com/codex/guides/agents-md)

说明 Codex 启动时如何构建指令链：先读 Codex home 下的全局文件，再从项目根目录一路走到当前目录，逐级读取 `AGENTS.md` / `AGENTS.override.md`，越近的文件优先级越高。实践含义：全局放个人习惯，仓库根放项目约定，子目录放局部规则。

`厂商文档`

### OA04 · Codex Best practices {#oa04}
**机构**：OpenAI（ChatGPT Learn / Codex 指南）｜**日期**：持续更新｜[原文](https://learn.chatgpt.com/guides/best-practices)

建议把 Codex 当作「需要配置和持续改进的队友」。默认提示四要素：**Goal（目标）/ Context（相关文件与报错）/ Constraints（标准、架构、安全要求）/ Done when（完成标准）**。好的 AGENTS.md 应包括：仓库布局、如何运行、构建/测试/lint 命令、工程约定与 PR 期望、约束与禁止事项、「完成」的定义与验证方式。重复工作做成 skills，稳定流程做成自动化。

`厂商文档`

### OA05 · How OpenAI uses Codex {#oa05}
**机构**：OpenAI｜**日期**：2026-01-14｜[原文](https://openai.com/business/learn/how-openai-uses-codex/)

基于内部访谈与使用数据整理的七类用例（代码理解、重构迁移、性能优化、补测试、提速、保持心流、探索）与最佳实践：大改动先用 Ask 模式出计划再切 Code 模式；任务粒度以「人类约一小时 / 几百行」为宜；持续改进运行环境（启动脚本、环境变量）以降低出错率；**像写 GitHub Issue 一样写提示**（文件路径、组件名、diff、参照「像模块 X 那样实现」）；用 AGENTS.md 提供持久上下文；用 Best-of-N 并行出多个方案再择优。

`厂商自报`

### OA06 · Run long horizon tasks with Codex {#oa06}
**机构**：OpenAI Developers 博客｜**日期**：2026（未标注具体日期）｜[原文](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex)

作者让 Codex 从空仓库自主构建一个设计工具，连续运行约 25 小时、约 1,300 万 token、约 3 万行代码。成功的关键不是某条巧妙提示，而是组合：规格文件（目标与约束）、带验收标准的里程碑 `plans.md`、智能体操作手册 `implement.md`、持续验证（测试/lint/类型检查/构建）、以及实时状态与审计日志 `documentation.md`——即「持久化的项目记忆」防止漂移、稳定「完成」的定义。

`作者自述的实验，非生产部署`

### OA07 · Codex as a platform: build on the open agent harness {#oa07}
**机构**：OpenAI Developers 博客｜**日期**：2026（未标注具体日期）｜[原文](https://developers.openai.com/blog/codex-as-a-platform)

介绍开源的 Codex harness 与 app-server 协议：管理会话状态、流式执行、工具调用、沙箱与审批策略，并允许把智能体嵌入现有软件。观点：一个可用的智能体远不止「提示 + 模型回答」，还需要上下文维护、工具、进度暴露、失败处理与人工审批。

### OA08 · A practical guide to building agents（PDF） {#oa08}
**机构**：OpenAI｜**日期**：2025｜[原文](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)

面向产品与工程团队的智能体构建指南：智能体 = 模型 + 工具 + 指令；先从单智能体起步，复杂度确实需要时再拆多智能体（管理者模式 / 去中心化交接）；护栏要分层（相关性、安全、PII、工具风险分级等），并为高风险操作和反复失败设计人工介入点。

### OA09 · GPT-5 prompting guide {#oa09}
**机构**：OpenAI Cookbook｜**日期**：2025｜[原文](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide)

讨论如何控制「智能体积极性」（eagerness）：需要更少探索时明确停止条件与工具调用预算，需要更多自主时明确「直到问题解决才结束」；使用工具前言（preamble）让模型说明计划；以及在编码场景中写清代码风格与项目约定。指南特别提醒：指令中相互矛盾的内容会让模型浪费推理去调和冲突，应在系统提示与规则文件中消除矛盾。

`厂商文档`
