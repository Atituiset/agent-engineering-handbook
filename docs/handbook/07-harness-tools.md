# 07 · 工具与 Harness：hooks、skills、子智能体、MCP

[[toc]]

## 要点

- **从「朴素」开始。** Claude Code 的创建者本人的配置「出奇地朴素」；先用默认配置，遇到具体问题再加机制。
- **每种机制解决一类问题**：规则文件 → 常驻知识；skills → 按需知识与流程；hooks → 必须执行的确定性动作；子智能体 → 上下文隔离；MCP/CLI → 外部能力。
- **优先 CLI 与脚本**，它们可组合、可复用、对人和智能体都友好；MCP 用于真正需要的集成。
- **多智能体：读可以并行，写保持单线程**，并设计好编排者与评判者。
- **harness 里的每条规则都编码了一个会过期的假设**，要定期删减。

## 1. 术语：harness 由什么组成

Dex Horthy 把 harness engineering 定义为：设计一个现成智能体的**集成点**——commands、hooks、skills、agents、MCP 等（[X10](/sources/x-posts#x10)）。Böckeler 为编码智能体的上下文配置建立了术语表，区分「谁决定加载」（人、智能体、软件）以及「是否保证被加载」（[TW05](/sources/thoughtworks#tw05)）。据此可以画出一张选型表：

| 机制 | 谁决定加载/执行 | 是否保证 | 适合放什么 | 来源 |
| --- | --- | --- | --- | --- |
| 规则文件（AGENTS.md / CLAUDE.md） | 软件，每次会话 | 加载保证，遵守不保证 | 命令、边界、非标准约定、坑点 | [AN02](/sources/anthropic#an02)、[OA03](/sources/openai#oa03) |
| 路径规则 | 软件，按文件匹配 | 同上 | 某个子系统的约定 | [VD02](/sources/vendors#vd02)、[BT13](/sources/bigtech#bt13) |
| Skills | 智能体按描述判断 | 不保证被调用 | 专项流程、领域知识、脚本 | [AN05](/sources/anthropic#an05)、[AN14](/sources/anthropic#an14) |
| Slash 命令 / 自定义智能体 | 人显式调用 | 调用即执行 | 可复用工作流 | [BT18](/sources/bigtech#bt18)、[BT19](/sources/bigtech#bt19) |
| Hooks | 软件，生命周期事件 | **确定性** | 格式化、拦截、强制测试 | [AN03](/sources/anthropic#an03) |
| 子智能体 | 主智能体或人 | 调用即执行 | 探索、测试、评审等噪声大的工作 | [AN04](/sources/anthropic#an04) |
| MCP 服务器 / CLI | 智能体 | 工具可用 ≠ 被正确使用 | 外部系统、内部工具 | [OS12](/sources/open-source#os12) |
| 权限与沙箱 | 软件 | **确定性** | 能做什么、不能做什么 | [AN26](/sources/anthropic#an26)、[AN27](/sources/anthropic#an27) |

## 2. 从朴素开始

Boris Cherny 说自己的配置「出奇地朴素」，开箱即用就很好，团队里每个人用法都不同（[X05](/sources/x-posts#x05)）。Anthropic 为新模型删减了大部分系统提示（[X07](/sources/x-posts#x07)）。Armin Ronacher 的原则是保持简单——自定义工具就是智能体可以直接运行的普通脚本（[PR17](/sources/practitioners#pr17)）。

**建议的演进顺序**：默认配置 → 精简的 AGENTS.md（命令 + 边界）→ 格式化/lint 的 hook → 一个 verify skill → 按需加子智能体与 MCP。每一步都由一个**具体的、反复出现的失败**驱动，而不是因为「别人都这么配」。

## 3. Hooks：把「必须」变成确定性

Hooks 在工具调用前后、会话结束等事件上执行 shell 命令（[AN03](/sources/anthropic#an03)）。典型用途：

- 编辑后自动格式化与 lint，把错误反馈给智能体；
- 拦截对受保护文件（lint 配置、CI、架构测试、迁移脚本）的修改；
- 在「宣布完成」前强制跑测试；
- 拦截危险命令。

判断标准（[AN01](/sources/anthropic#an01)）：不能有例外的规则 → hook；只是偏好 → 留在规则文件里，或删掉。Kiro 也把 hooks 作为与 specs 并列的核心机制（[VD15](/sources/vendors#vd15)）。

## 4. Skills：按需加载的专业知识

Skills 是「文件夹 + SKILL.md + 脚本/资源」，启动时只看名称与描述（[AN14](/sources/anthropic#an14)）。Anthropic 内部有数百个 skills，经验是（[AN21](/sources/anthropic#an21)）：

- 一个 skill 只做一类事；
- 重点写 **gotchas**，而不是模型已知的常识；
- 用脚本承载确定性步骤。

Simon Willison 认为 skills 可能比 MCP 更具影响力，因为它的简洁（[PR06](/sources/practitioners#pr06)）。Greg Brockman 要求 OpenAI 团队把让 Codex 做过的事都写成 skill 并提交到共享仓库（[X04](/sources/x-posts#x04)）。

**注意**：skill 可能不被调用（[VD11](/sources/vendors#vd11) 中 56% 的用例没调用）。必须执行的流程不要只靠 skill，要用 hook 或明确的命令触发。

> **现成的 skills 去哪找**：各大厂官方仓库、GitHub 高星技能集、各工具的加载路径对照，以及引入第三方 skill 的安全审查清单，见 [第 13 章 · Skills 生态](./13-skills-catalog)。

## 5. 工具设计：接口比示例重要

- 工具是确定性系统与非确定性智能体之间的契约；少而精，命名空间清晰，返回有意义的信息，用真实任务评测（[AN11](/sources/anthropic#an11)）。
- 最有价值的工具是「让模型自己找上下文」的工具（[AN20](/sources/anthropic#an20)）。
- 新一代模型下，与其给使用示例，不如设计更有表达力的参数——示例会把模型限制在特定探索空间（[X07](/sources/x-posts#x07)）。
- 自定义 lint 的报错信息写入修复说明（[OA01](/sources/openai#oa01)）。

### CLI vs MCP

Armin Ronacher 质疑 MCP 的可组合性与 token 成本，主张让模型写代码/脚本完成任务（[PR18](/sources/practitioners#pr18)）；Anthropic 自己也推出了「用代码执行调用 MCP」的方案，称 token 最多降低 98.7%（[AN15](/sources/anthropic#an15)，厂商自报）；Guillermo Rauch 提倡回归 Unix、CLI 与 Markdown（[X11](/sources/x-posts#x11)）。另一方面，MCP 已成为跨厂商的连接标准（[OS12](/sources/open-source#os12)），Greg Brockman 也建议通过 CLI **或** MCP 让内部工具对智能体可用（[X04](/sources/x-posts#x04)）。

**取舍**：内部工具优先做成好用的 CLI（人和智能体都能用、可脚本化、可测试）；需要认证、跨应用或供应商已提供的集成用 MCP；注意每个 MCP 服务器都扩大攻击面（第 09 章）。

## 6. 子智能体与多智能体

**子智能体**的主要价值是**保护主上下文**：把探索、工具输出、重试、中间推理交出去，只带回结论（[TW28](/sources/thoughtworks#tw28)、[PR11](/sources/practitioners#pr11)）。不要过度拆分。

**多智能体**的演进最能说明「经验会过期」：

| 时间 | 观点 | 来源 |
| --- | --- | --- |
| 2025-06 | 不要做多智能体：共享完整轨迹；并行子智能体的隐含决策会冲突 | Cognition（[VD05](/sources/vendors#vd05)） |
| 2025 | 多智能体在广度优先研究上更好，但 token 约为对话的 15 倍 | Anthropic（[AN12](/sources/anthropic#an12)） |
| 2026-01 | 平级自协调失败；规划者/工作者/评判者分层成功 | Cursor（[VD03](/sources/vendors#vd03)） |
| 2026-04 | 修正：多个智能体贡献智能（调研、审查、规划），**写操作保持单线程** | Cognition（[VD06](/sources/vendors#vd06)） |
| 2026 | 16 个并行智能体写 C 编译器；harness 与测试是关键 | Anthropic（[AN29](/sources/anthropic#an29)） |

**取舍**：默认单智能体 + 子智能体；只有当任务天然可并行（批量迁移、调研、多视角评审）且有清晰的编排者与评判者时才上多智能体；**写同一份代码的并行写手**仍然风险很高。Gas Town 这类大规模编排工具是激进实验（[OS10](/sources/open-source#os10)）。

## 7. 长程任务的 harness

- **初始化 + 增量**：初始化智能体建立 `init.sh`、进度日志、功能清单与首个提交；增量智能体每次推进一项并留下交接产物（[AN17](/sources/anthropic#an17)）。
- **规格 + 里程碑 + 进度**：OpenAI 25 小时任务的组合（[OA06](/sources/openai#oa06)）。
- **循环**：Ralph 技术就是一个 bash 循环加规格与强反馈，但作者明确只用于绿地项目（[PR31](/sources/practitioners#pr31)）。
- **自主运行的条件**：auto mode 处理权限、/goal 或 /loop 推动、云端运行、**端到端自我验证**（[X06](/sources/x-posts#x06)）。把任务交给云端或 CI 里的智能体时，环境、权限、交接与并发怎么管，见 [第 14 章](./14-async-agents)。
- **审批疲劳**：用户批准了 93% 的权限请求，所以 Anthropic 用分类器代替逐条确认（[AN26](/sources/anthropic#an26)，厂商自报）。

## 8. harness 会过期

Anthropic 观察到 harness 编码了「模型做不到什么」的假设，这些假设随模型进步迅速过时，因此把「大脑」「手」「会话」解耦（[AN30](/sources/anthropic#an30)）。Armin Ronacher 发现高层 SDK 抽象在真实工具调用面前会破裂（[PR19](/sources/practitioners#pr19)）。12-Factor Agents 主张拥有你的提示、上下文窗口与控制流（[OS02](/sources/open-source#os02)）。实践上：**给每条规则、hook、skill 标注它要解决的失败**，换模型时逐条验证是否仍然需要（[TW20](/sources/thoughtworks#tw20)）。

## 2026-11 新证据：工具越多越好？大量异议 {#new-evidence}

P13「Skills 等可复用指令按需加载」的独立支持数在全库最高（355）。异议合计 20（关键词自动检出的疑似异议 15，人工读过后确认的异议 5）；人工确认的 5 条与 P08 并列全库最多。下方对比表「355／20」中的 20 就是这两类之和。这说明它很热门，不等于它已被证明有效。

- **确定性机制优先**：掘金作者团队用 Skill 做提交前检查时「时灵时不灵」，换成 PreToolUse Hook 后才稳定。他们的规矩是能用 Hook 表达就别退回提示词约束（[CN41](/sources/chinese#cn41)）。官方中文文档也把机制按「非确定性 vs 确定性」两列对照（[CN29](/sources/chinese#cn29)）。这**加强**了 P12（164 位独立支持）。
- **skills/MCP 的异议**：Burke Holland 认为 99% 的 MCP、功能和 skill 都是噪声（[XT-019](/sources/x/tools#xt-019)）。Thorsten Ball 说 Amp 聚会的共识是，由人按序手动调用的 skill「金字塔」是反模式（[XT-042](/sources/x/tools#xt-042)）。Vercel 的评测里 skill 常常未被调用（[HN15](/sources/hackernews#hn15)）。Boris Cherny 也发布了清理未用 skills/MCP 的命令（[XC-018](/sources/x/context#xc-018)）。
- **子智能体被滥用**：dex 认为子智能体自 2025 年中以来被过度使用，并行不能替代深思熟虑的上下文管理（[XT-030](/sources/x/tools#xt-030)）。另一位作者列出多智能体的问题：没有共享状态、Git 冲突、上下文污染（[XA-006](/sources/x/parallel#xa-006)）。
- **harness 比模型更重要**：HN 高热讨论「只改 harness 就提升了 15 个模型的编码表现」（[HN07](/sources/hackernews#hn07)），与腾讯、美团把评测与门禁放进 harness 的做法一致（[CN20](/sources/chinese#cn20)、[CN24](/sources/chinese#cn24)）。

**结论调整**：本章原本建议「按需加载 skills」。现在补充两条前提：先确认它真的会被调用；数量宁少勿多，并在换模型时重新评估。

同一 Prompt 下，功能正确并不等于可交付。字节洪定坤的对照实验（团队自报、尚未独立验证）：功能正确率约 80%，但“可交付性”只有 40–60 分，接入 Harness 基建后升到约 80 分（[BD01](/sources/chinese#bd01)）。腾讯云 ADP 把这个关系写成 Agent = Model + Harness（[TX06](/sources/chinese#tx06)）。从单次 Harness 再往上，蚂蚁阿福的做法是“先可靠修好单个 badcase，再持续修复”（议题摘要，[AL28](/sources/chinese#al28)）；Qoder 的“专家团”把调研、编码、验证、自动评审拆给多个 Agent（议题摘要，[AL23](/sources/chinese#al23)）。沙箱也正在变成基建：阿里 OpenSandbox 内部周创建量超千万（团队自报，[AL07](/sources/chinese#al07)），腾讯则开源了 CubeSandbox（议题摘要，[TX19](/sources/open-source#tx19)）。

## 与传统软件工程认知的对比

| 维度 | 传统认知 | 智能体时代 | 判断 | 佐证（支持／异议） |
| --- | --- | --- | --- | --- |
| 开发环境 | IDE 配置是个人偏好 | harness 是团队资产，应入库、评审、版本化（[X04](/sources/x-posts#x04)） | **修正** | [P13 · 355／20](/compare/evidence#p13) |
| 工具选择 | 选功能最强的框架 | 选「无聊」、稳定、在训练数据中常见、可在仓库内完全推理的技术（[OA01](/sources/openai#oa01)） | **延续**「选择无聊技术」 | [P20 · 5／0](/compare/evidence#p20) |
| Unix 哲学 | 小工具、可组合、文本接口 | 对智能体同样最友好（[X11](/sources/x-posts#x11)、[PR17](/sources/practitioners#pr17)） | **延续并加强** | [P14 · 304／7](/compare/evidence#p14) |
| 抽象层 | 高层框架提效 | 智能体框架的高层抽象常常破裂，需要拥有控制流（[PR19](/sources/practitioners#pr19)、[OS02](/sources/open-source#os02)） | **谨慎** | — |
| 并发 | 多线程写共享状态需要锁与协调 | 多智能体写同一代码库面临同样问题：读并行、写串行（[VD06](/sources/vendors#vd06)） | **延续**：经典并发智慧直接适用 | [P11 · 209／17](/compare/evidence#p11) |
| 自动化脚本 | 一次性脚本可以随便写 | 脚本成为智能体的工具，要有清晰接口与报错 | **修正** | [P14 · 304／7](/compare/evidence#p14) |

> 「佐证」列：原则编号 · 独立支持作者数／异议数（疑似 + 人工确认），关键词自动归类，口径见 [共识度/佐证](/compare/evidence)。

**选择理由**：Harness 本质上是**开发者平台工程**在智能体上的投影——过去平台团队为人提供脚手架、CI 模板、内部 CLI，现在同样的东西要对智能体可读、可调用。经典的 Unix 哲学、选择无聊技术、并发控制原则都直接适用。最大的新变化是「过期速度」：传统工具链几年才变一次，harness 的最佳实践每个模型代际都会变，所以要像对待代码一样对待它——有测试、有评审、能删除。

**证据强度**：「从简开始、按需增加」是**共识**；多智能体的价值是**分歧且在演化**；CLI vs MCP 是**分歧**；具体数字为**厂商自报**。
