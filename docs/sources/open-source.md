# 开源项目与规范

> 可以直接拿来用的开源规范、工具与方法论仓库。仓库内容持续变化，描述基于 2026-11-18 打开时的 README/首页。星标数等易变数字不作引用。

[[toc]]

## 指令与上下文规范

### OS01 · AGENTS.md {#os01}
**机构**：开放格式（多家厂商共同支持）｜**日期**：持续更新｜[原文](https://agents.md/)

「给智能体看的 README」：一个专门的、可预测的位置，存放帮助编码智能体在项目中工作的上下文与指令（安装命令、测试命令、代码风格等）。README 面向人，AGENTS.md 补充那些对人来说过于细节、但智能体需要的内容。官网称已被超过 6 万个开源项目使用（自报）。写法建议见 [BT16](./bigtech#bt16)，效果的争议见 [RS06](./research#rs06)。

### OS02 · 12-Factor Agents {#os02}
**作者/机构**：Dex Horthy / HumanLayer｜**日期**：持续更新｜[原文](https://github.com/humanlayer/12-factor-agents)

仿照「12-Factor App」，总结构建可上生产的 LLM 应用的原则：自然语言转工具调用、拥有你的提示、**拥有你的上下文窗口**、工具只是结构化输出、统一执行状态与业务状态、用工具调用联系人类、拥有你的控制流、把错误压缩进上下文、小而专注的智能体、把智能体做成无状态 reducer 等。核心思想：成功的生产级智能体大多是「大部分确定性代码 + 恰到好处的 LLM 步骤」，而不是把一切交给框架循环。

### OS03 · Spec Kit {#os03}
**机构**：GitHub｜**日期**：持续更新｜[原文](https://github.com/github/spec-kit)

开源工具包，为编码智能体提供结构化流程、可复用模板与有记录的产出。当前 README 把它定位为多流程：规格驱动开发（规格贯穿计划、实现与收敛）、缺陷修复（评估原因、限定范围修复、记录验证）、想法评估等，可直接使用、定制或自带流程。早期版本以 specify → plan → tasks → implement 与项目「宪章（constitution）」闻名。介绍文章见 [BT15](./bigtech#bt15)，实际使用评价见 [TW06](./thoughtworks#tw06)。

### OS04 · BMad Method {#os04}
**机构**：bmad-code-org｜**日期**：持续更新｜[原文](https://github.com/bmad-code-org/BMAD-METHOD)

「敏捷 AI 驱动开发」方法论：覆盖做什么、如何组织、如何随学习而改变，而不只是代码；决策保持显式、上下文向前传递、流程按工作规模伸缩——小改动直接构建，复杂工作获得需要的深度。可以端到端使用，也可以把它的简报、规格与架构文档接入既有交付流程。

### OS05 · Aider：Specifying coding conventions {#os05}
**机构**：Aider｜**日期**：持续更新｜[原文](https://aider.chat/docs/usage/conventions.html)

最早的「约定文件」实践之一：写一个小的 `CONVENTIONS.md`（例如「优先用 httpx 而不是 requests」「尽可能使用类型」），以只读方式加载进会话。是 CLAUDE.md / AGENTS.md 一类做法的早期形态，说明这一模式先于厂商标准就已被独立发现。

## 技能、工作流与编排

### OS06 · anthropics/skills {#os06}
**机构**：Anthropic｜**日期**：持续更新｜[原文](https://github.com/anthropics/skills)

Agent Skills 的官方示例仓库：skill 是由指令、脚本和资源组成的文件夹，智能体按需动态加载，以可重复的方式完成特定任务。标准本身见 agentskills.io；设计思路见 [AN14](./anthropic#an14)。

### OS07 · awesome-claude-code {#os07}
**作者**：hesreallyhim（社区）｜**日期**：持续更新｜[原文](https://github.com/hesreallyhim/awesome-claude-code)

社区精选的 Claude Code 资源集合：skills、子智能体、hooks、斜杠命令、状态栏、插件与工作流。适合寻找现成 harness 组件，但质量参差，引入前应自行审查（尤其是 hooks 与脚本的安全性）。

### OS08 · Superpowers {#os08}
**作者**：Jesse Vincent (obra)｜**日期**：持续更新｜[原文](https://github.com/obra/superpowers)

「一套可工作的智能体技能框架与软件开发方法论」。基本工作流：写代码前先 brainstorming 澄清需求 → 写计划（强调 YAGNI、DRY）→ 按任务派发全新子智能体执行，每个任务后评审 → 实现期间强制 RED-GREEN-REFACTOR（写失败测试、看它失败、写最少代码、看它通过、提交），并**删除先于测试写出的代码** → 任务间请求代码评审。作者的设计思路见 [PR33](./practitioners#pr33)。

### OS09 · OpenHands {#os09}
**机构**：OpenHands（原 All-Hands-AI）｜**日期**：持续更新｜[原文](https://github.com/All-Hands-AI/OpenHands)

开源的 AI 驱动开发平台，当前形态是自托管的「开发者控制中心」，可在本地、远程或云端后端运行 OpenHands、Claude Code、Codex、Gemini 等兼容智能体，并自动化日常任务（如把 issue 分解为任务）。适合需要自托管、可审计的团队研究其架构。

### OS10 · Gas Town {#os10}
**作者**：Steve Yegge（现 gastownhall 组织）｜**日期**：持续更新｜[原文](https://github.com/steveyegge/gastown)

多智能体工作区管理器：协调多个编码智能体并行处理不同任务，用 git 支撑的 hooks 持久化工作状态，提供邮箱、身份与交接机制，README 自称可从「4–10 个智能体就混乱」扩展到 20–30 个。与 [PR25](./practitioners#pr25) Beads 配套。属于激进的实验性方向，生产使用前应谨慎。

### OS11 · Advanced Context Engineering for Coding Agents（ACE-FCA） {#os11}
**作者/机构**：Dex Horthy / HumanLayer｜**日期**：2025｜[原文](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents)

「研究 → 计划 → 实现」三阶段工作流与「频繁的有意压缩」：把上下文利用率保持在约 40–60%，每阶段产出一份可被人评审的 Markdown 产物。核心论点：在存量大代码库中，人对研究与计划的评审杠杆远高于对代码的评审。详见 [VD20](./vendors#vd20)。

### OS12 · Model Context Protocol (MCP) {#os12}
**机构**：开放标准（Anthropic 发起）｜**日期**：持续更新｜[原文](https://modelcontextprotocol.io/)

把 AI 应用连接到外部系统（数据源、工具、工作流）的开源标准，「像 AI 应用的 USB-C 接口」。工程上需要注意两点：工具定义占用上下文（参见 [AN15](./anthropic#an15) 的代码执行方案）；每接入一个 MCP 服务器都扩大了攻击面（参见 [SC01](./security#sc01)）。

## 架构约束工具（把「规则」变成「检查」）

### OS13 · ArchUnit {#os13}
**机构**：TNG / 开源社区｜**日期**：v1.5.0 发布于 2026-08-04｜[原文](https://www.archunit.org/)

用普通 Java 单元测试框架检查 Java 代码架构的库：包与类之间的依赖、分层与切片、循环依赖等，基于字节码分析；也有 .NET 移植版。在智能体时代，它是把「分层架构约束」从文档变成 CI 检查的直接手段——这正是 OpenAI harness 文章中「结构测试」的同类工具。

### OS14 · dependency-cruiser {#os14}
**作者**：Sander Verweij｜**日期**：持续更新｜[原文](https://github.com/sverweij/dependency-cruiser)

按你自己的规则校验并可视化 JavaScript/TypeScript 项目的依赖：在构建中以文本报告违规，也能生成依赖图。适合在前端/Node 项目中实现「UI 层不得直接依赖数据层」之类的不变量。

### OS15 · Import Linter {#os15}
**作者**：David Seddon｜**日期**：持续更新｜[原文](https://github.com/seddonym/import-linter)

「给你的 Python 架构做 lint」：对 Python 模块间的 import 施加约束（分层、独立性、禁止依赖），并提供浏览器界面探索包的架构。Python 项目中落实分层约束的轻量方案。


## 沙箱与执行环境 {#sandbox}

以下为开源的智能体执行环境相关条目。

### 腾讯 · TX19 · AI Agent 执行环境的规模化难题：CubeSandbox 的解法与实践（QCon 上海 2026 议题） {#tx19}
**作者/机构**：龙进（腾讯云 CubeSandbox 核心 maintainer）｜**日期**：2026-10（QCon 上海）｜[原文](https://qcon.infoq.cn/2026/shanghai/presentation/7393)｜[相关链接](https://github.com/TencentCloud/CubeSandbox)

Agent 负载从一次性执行走向长周期、有状态、大规模并行，既要安全承载不可信代码又要扛突发并发。CubeSandbox 走 MicroVM + 快照路线，以沙箱为基本计算单元，提供暂停恢复、快照克隆，自报冷启动约 60ms、单实例内存 5MB 以内。

> “基于MicroVM + 快照路线，以沙箱为基本计算单元，实现算力与状态两个维度的弹性”

**证据类型**：议题摘要（演讲者自述）｜**对应原则**：[P15](/compare/evidence#p15) [Q09](/handbook/12-quality-cicd#q09)
