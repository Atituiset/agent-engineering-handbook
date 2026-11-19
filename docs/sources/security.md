# 安全

> 智能体拿到了读写文件、执行命令、联网的能力，安全模型必须随之改变。本页只收录**防御性**的原则、模式与工程实践，不包含任何攻击细节。

[[toc]]

### SC01 · The lethal trifecta for AI agents {#sc01}
**作者**：Simon Willison｜**日期**：2025-06-16｜[原文](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)

「致命三要素」：**访问私有数据**、**暴露于不可信内容**、**能够对外通信**。一旦智能体同时具备这三项能力，攻击者就能诱导它读取你的私有数据并发送出去。坏消息是我们仍无法 100% 可靠地防止这一点，「护栏」类产品不能保证安全；对混搭工具的终端用户来说，唯一安全的办法是**完全避免这三者的组合**。这是本手册安全章节的第一原则。

> "The only way to stay safe there is to avoid that lethal trifecta combination entirely."

### SC02 · Design Patterns for Securing LLM Agents against Prompt Injections {#sc02}
**作者**：Luca Beurer-Kellner 等 14 位作者（含 Florian Tramèr）｜**日期**：2025-06-10｜[原文](https://arxiv.org/abs/2506.08837)

提出一组有原则的设计模式，用于构建对提示注入具有**可证明抵抗力**的智能体，并系统分析这些模式在效用与安全之间的权衡，配以案例研究。核心思想是通过架构（限制不可信输入能影响的动作范围）而不是靠模型「自觉」来获得安全性——与传统安全中的最小权限、隔离原则一脉相承。

### SC03 · We Have a Package for You! A Comprehensive Analysis of Package Hallucinations {#sc03}
**机构**：arXiv 论文｜**日期**：2024-06-12｜[原文](https://arxiv.org/abs/2406.10279)

用 16 个代码生成模型生成 57.6 万个 Python/JavaScript 代码样本：商业模型平均至少 5.2%、开源模型 21.7% 的推荐包是幻觉出来的，共出现 205,474 个不同的幻觉包名。这是一种新型的「包混淆」供应链威胁。

### SC04 · The Rise of Slopsquatting {#sc04}
**机构**：Socket｜**日期**：2025-04-08｜[原文](https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks)

「slopsquatting」（由 PSF 的 Seth Larson 命名）：抢注 LLM 幻觉出的、并不存在的包名，等待被 AI 引导的开发者安装。研究显示同一提示重复十次时，43% 的幻觉包每次都会出现，39% 从不重现——幻觉要么高度稳定、要么完全随机，稳定的那部分正是可被利用的。防御：依赖白名单、安装前校验、锁文件与依赖审查。

`厂商博客（Socket 销售供应链安全产品）`

### SC05 · OWASP Top 10 for LLM Applications {#sc05}
**机构**：OWASP Gen AI Security Project｜**日期**：2025 版｜[原文](https://genai.owasp.org/llm-top-10/)

LLM 应用的十大风险清单（2025 版），提示注入（LLM01:2025）居首。可作为团队威胁建模与评审清单的起点。

### SC06 · A Practical Guide to Security in November 2026 {#sc06}
**作者/机构**：Jack Cable（Cognition）｜**日期**：2026-11-03｜[原文](https://cognition.ai/blog/practical-guide-to-security-november-2026)

在近期密集安全事件背景下的务实建议：多年来已知的安全最佳实践依然有效——攻击者利用未打补丁的服务器或被盗凭据并不需要高级 AI；AI 让攻击更快更便宜，但不妨碍你关闭整条基础攻击路径。对使用智能体的团队而言，补丁、凭据管理与最小权限仍然是第一优先级。

### SC07 · 厂商的沙箱与权限实践（索引） {#sc07}
**作者/机构**：Anthropic、Thoughtworks｜**日期**：见各条｜[原文](./anthropic#an27)

与本页相关、已在其他分类收录的条目：Claude Code 沙箱（文件系统与网络双重隔离，[AN27](./anthropic#an27)）、跨产品的隔离策略（[AN28](./anthropic#an28)）、auto mode 的分类器式权限审批（[AN26](./anthropic#an26)）、Thoughtworks 雷达将「智能体沙箱」列为 Adopt（[TW24](./thoughtworks#tw24)）、「有毒流分析」（[TW25](./thoughtworks#tw25)）、编码助手扩大供应链攻击面——被攻陷的 MCP 服务器或规则文件可向智能体注入指令（[TW12](./thoughtworks#tw12)）。



### 腾讯 · TX22 · A.S.E（AICGSecEval）：仓库级 AI 生成代码安全评测基准 {#tx22}
**作者/机构**：腾讯悟空代码安全团队（GitHub 开源）｜**日期**：2026｜[原文](https://github.com/Tencent/AICGSecEval)

不在函数片段上评“AI 写的代码安不安全”，而是在真实仓库上下文里评，支持 LLM 直接生成与 Claude Code 等 Agent 生成两种模式，用 Docker 复现构建与验证。腾讯同组织下还开源了 VulnGym（白盒漏洞挖掘 Agent 基准）与 AI-Infra-Guard（Agent/MCP/Skills 扫描）。

> “A.S.E (AICGSecEval) is a repository-level AI-generated code security evaluation benchmark developed by Tencent Wukong Code Security Team.”

**证据类型**：开源仓库 README（团队自述）｜**对应原则**：[Q08](/handbook/12-quality-cicd#q08) [P15](/compare/evidence#p15)

### 字节 · BD19 · Trae IDE 遥测与隐私分析：关闭遥测后仍持续上报 {#bd19}
**作者/机构**：segmentationf4u1t（独立研究者，GitHub）｜**日期**：2025-07｜[原文](https://github.com/segmentationf4u1t/trae_telemetry_research)｜[相关链接](https://news.ycombinator.com/item?id=44703164)

独立研究者抓包分析：即使开启遥测退出（opt-out），Trae 仍上报系统信息、多种设备标识与使用数据；在 HN 获 954 分讨论。对“用这类商业编码工具处理私有代码”的团队，是需要单独评估的数据边界问题（官方回应未在本次检索中核到）。

> “Trae continues to transmit a broad set of data even with telemetry opt-out enabled”

**证据类型**：第三方独立分析（单一研究者）｜**对应原则**：[P15](/compare/evidence#p15) [Q13](/handbook/12-quality-cicd#q13)
