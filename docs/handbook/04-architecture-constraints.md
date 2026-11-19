# 04 · 架构约束落地：从「告诉它」到「让它绕不过去」

[[toc]]

> 这是本手册最核心的一章，直接回应「智能体守不住工程与架构约束」这个问题。

## 要点

- **把约束分成两类**：能机械判定的（依赖方向、命名、文件大小、禁用 API）→ 写成 linter / 结构测试 / hook / CI；需要判断的（模块职责、设计取舍）→ 写进精简的上下文与 ADR。
- **强制不变量，而不是微观管理实现。** 规定边界，放开边界内的实现方式。
- **报错信息就是提示词**：自定义 lint 的错误信息里直接写「怎么改」，让失败自动变成指导。
- **约束必须在智能体能「看到」的地方失败**：编码时（hook）、提交前（pre-commit）、PR 时（CI），越早越便宜。
- **变更不能修改评判它的规则**：规则从基础分支读取，受保护文件禁止智能体修改。
- **把技术债清理自动化**：像垃圾回收一样持续小额偿还。

## 1. 为什么写在 AGENTS.md 里不够

Anthropic 的官方文档把指令分为两类（[AN01](/sources/anthropic#an01)）：

- **非确定性指令**：提示词、CLAUDE.md、skills——模型读了再决定是否遵守。
- **确定性指令**：hooks、deny 规则、managed settings、CI——harness 每次都执行。

> "no matter how strongly you word it, whether Claude follows that line on a given turn is still Claude’s call."

HumanLayer 说得更直接：**不要让 LLM 干 linter 的活**（[VD19](/sources/vendors#vd19)）。Martin Fowler 的笔记里也有同样的原则：不要让 LLM 计算能确定性计算的东西（[TW15](/sources/thoughtworks#tw15)）。快手的结论是约束必须做成 **AI 绕不过的门禁**——他们甚至观察到智能体为了编译通过主动跳过代码检查（[CN06](/sources/chinese#cn06)）。

## 2. 核心案例：OpenAI 的分层架构强制

OpenAI 团队在「0 行手写代码」的约束下构建了约百万行的产品（[OA01](/sources/openai#oa01)，厂商自报），其架构约束做法值得逐条借鉴：

1. **固定分层 + 单向依赖**：每个业务域固定分为 Types → Config → Repo → Service → Runtime → UI，代码只能「向前」依赖；横切关注点（认证、连接器、遥测、特性开关）只能通过一个显式接口 Providers 进入；其他一律禁止。
2. **机械执行**：由自定义 linter（也是 Codex 写的）和结构测试强制。
3. **「品味不变量」**：结构化日志、schema 与类型命名约定、文件大小上限、平台可靠性要求，都写成自定义 lint。
4. **报错即指导**：因为 lint 是自定义的，错误信息里直接写入修复说明，注入智能体上下文。
5. **边界集中、局部自治**：规定「在边界处解析数据形状」，但不规定用哪个库。

> "By enforcing invariants, not micromanaging implementations, we let agents ship fast without undermining the foundation."

文中有一句对资深工程师很有启发的话：**这种架构通常要等到有几百名工程师时才会做；有了编码智能体，它是早期前提**——约束才是在不腐化、不漂移的前提下获得速度的关键。在以人为主的流程里这些规则也许显得吹毛求疵，在智能体流程里它们成了乘数：一旦编码，处处同时生效。

## 3. Guides 与 Sensors：一个完整的分类框架

Böckeler 的 harness 框架（[TW01](/sources/thoughtworks#tw01)）把控制手段分成 2×2：

| | 计算型（确定性、便宜、每次都跑） | 推理型（LLM 判断、贵、有方差） |
| --- | --- | --- |
| **Guides（前馈）** | 代码模板、脚手架、参考应用、类型定义 | AGENTS.md、skills、规格、ADR |
| **Sensors（反馈）** | 编译器、类型检查、linter、结构测试、架构测试、变异测试 | AI 代码评审、LLM 评估者 |

原则：**能用计算型就不用推理型**；推理型用于计算型覆盖不到的语义判断。Thoughtworks 雷达把「编码智能体的反馈传感器」列为 Trial（[TW21](/sources/thoughtworks#tw21)）；Böckeler 的后续文章演示了如何配置 ESLint 中默认未开启的复杂度规则、用快照把「比上次更差」的趋势反馈给智能体（[TW03](/sources/thoughtworks#tw03)）。

## 4. 工具箱：把架构规则变成检查

| 语言/场景 | 工具 | 能检查什么 |
| --- | --- | --- |
| Java / .NET | ArchUnit（[OS13](/sources/open-source#os13)） | 包/类依赖、分层、切片、循环依赖 |
| JS / TS | dependency-cruiser（[OS14](/sources/open-source#os14)） | 模块依赖规则、可视化 |
| Python | Import Linter（[OS15](/sources/open-source#os15)） | 分层、独立性、禁止 import |
| 任意 | 自定义 lint + 结构测试（[OA01](/sources/openai#oa01)） | 命名、文件大小、日志格式、禁用 API |
| 任意 | Claude Code hooks（[AN03](/sources/anthropic#an03)） | 编辑前拦截受保护文件、停止前强制跑测试 |
| 任意 | pre-commit（[PR30](/sources/practitioners#pr30)） | 提交时自动 lint / 格式化 / 测试 |
| 任意 | 参考应用 + 漂移检测（[TW07](/sources/thoughtworks#tw07)、[TW22](/sources/thoughtworks#tw22)） | 与团队标准实现的一致性 |

### 在哪一层失败

| 时机 | 机制 | 优点 | 注意 |
| --- | --- | --- | --- |
| 编辑时 | PostToolUse hook 跑格式化 / lint | 智能体立即看到错误并修正 | 要快，慢了会拖垮循环 |
| 宣布完成前 | Stop hook 强制跑测试 | 防止「测试失败也说完成」 | 失败多次应升级给人 |
| 提交时 | pre-commit | 与工具无关 | 智能体可能尝试 `--no-verify`，需 deny 规则 |
| PR 时 | CI 门禁 + 结构测试 | 最终防线，所有人适用 | 反馈慢，不要只靠这一层 |

蚂蚁数科把 CI 门禁分为**硬门禁**（脚本确定性检查，「这类问题没必要浪费 token」）和**软门禁**（多模型多视角 Agent 评审），问题暴露后逐步沉淀为门禁（[CN03](/sources/chinese#cn03)）。快手建立了编码时、插件、智能 CR、线上四道防线（[CN06](/sources/chinese#cn06)）。

## 5. 保护检查本身

智能体会「修改测试让它通过」。几条防线：

- **规则从基础分支读取**：Claude Code 团队的 REVIEW.md 从 base branch 读取，变更无法修改评判它的规则（[AN18](/sources/anthropic#an18)、[AN06](/sources/anthropic#an06)）。

> "If a change can modify the check that judges it, the check is broken."

- **受保护文件**：用 hook 或 deny 规则禁止编辑 lint 配置、CI 配置、架构测试（[AN03](/sources/anthropic#an03)）。
- **监视作弊信号**：Kent Beck 要求留意禁用或删除测试的迹象（[PR15](/sources/practitioners#pr15)）；Superpowers 甚至删除先于测试写出的代码（[OS08](/sources/open-source#os08)）。
- **新门禁先观察后强制**：先以观察模式运行，确认误报率可接受再阻断（[AN18](/sources/anthropic#an18)）。

## 6. 需要判断的约束：上下文 + ADR + 共识

不是所有架构约束都能机械化，例如「编排类」与「能力类」服务的职责边界。美团的做法是：**先人人对齐，再人机对齐**——团队先就分层规范、领域模型、仓储层规约形成共识，再落地为 always 级 AI Rule 与按需加载的 Skill；顺序错了，规则写得再好也会被不同人解释成不同版本（[CN01](/sources/chinese#cn01)）。

- 用**轻量 ADR** 记录关键决策的背景与后果，让智能体读到「为什么」，避免无意推翻（[TW35](/sources/thoughtworks#tw35)）。
- 用**参考应用**而不是长篇描述来传达「我们这里的标准写法」（[TW07](/sources/thoughtworks#tw07)、[TW22](/sources/thoughtworks#tw22)）。
- Meta 把隐性的部落知识显性化为精炼的上下文文件（[BT11](/sources/bigtech#bt11)）。

## 7. 持续偿还：技术债的「垃圾回收」

智能体会复制仓库里已有的模式，包括坏模式。OpenAI 团队曾每周五花 20% 时间手工清理「AI slop」，后来改为把「黄金原则」编码进仓库，由后台任务定期扫描偏离、开重构 PR（[OA01](/sources/openai#oa01)）。人的品味被捕获一次，然后持续作用于每一行代码。Boris Cherny 的维护例程（重复抽象统一、死代码移除、「抽象警察」）是同一思路（[X09](/sources/x-posts#x09)）。Simon Willison 也指出，过去因为耗时而一再推迟的重构（统一 API、改名、拆分大文件）正是智能体的理想任务（[PR14](/sources/practitioners#pr14)）。

## 8. 分歧：门禁该多严？

- **OpenAI**：吞吐量远超人的注意力时，许多传统规范变得适得其反——合并门禁极少、PR 生命周期短、flaky test 常用重跑解决；「在低吞吐环境这样做是不负责任的，在这里常是正确的权衡」（[OA01](/sources/openai#oa01)）。
- **Anthropic Claude Code 团队**：不许用 sleep / 重试掩盖 flaky test（[AN18](/sources/anthropic#an18)）。
- **Kent Beck**：AI 倾向大批量，信任需要小而经验证的步骤（[PR16](/sources/practitioners#pr16)）。

**本手册的取舍**：**架构不变量必须硬阻断，测试稳定性问题不可掩盖，流程性门禁可以按吞吐量调整。** 也就是说，OpenAI 放宽的是「等待」（阻塞式合并、人工审批），没有放宽「架构约束」——他们的分层规则恰恰是全文最严格的部分。

## 2026-11 新证据：机械约束更受认可，「过度约束」开始被反思 {#new-evidence}

- **加强：纠正写成 lint，而不是写进说明文件**。Cline 创始人认为模型读不完整个代码库，但可以在提交时用 linter 强制架构模式（[XK-001](/sources/x/constraints#xk-001)）。Lauren Tan 的演讲要点是：每纠正一次，就写成一条 lint 规则，而不是往 agents.md 里加话（[XK-005](/sources/x/constraints#xk-005)）。平安科技用 AI 把私域架构规范批量转成 Lint、ArchUnit 等 CI 检查（[CN16](/sources/chinese#cn16)）。快手代码评审沉淀了 1,100+ 条确定性规则，采纳率从 7.9% 升到 54%（团队自报，[CN37](/sources/chinese#cn37)）。Boris Cherny 也说，lint 规则与 e2e 测试的杠杆比以前更大了（[XV-002](/sources/x/verify#xv-002)）。
- **修正：harness 的严格程度要跟着模型走**。Robert C. Martin（Uncle Bob）花几周搭了一个严格约束智能体的 harness，期间模型进步让它变得多余（[XK-003](/sources/x/constraints#xk-003)）。他公开反思自己可能在过度约束，但仍保留单元测试与变异测试（[XK-002](/sources/x/constraints#xk-002)）。**结论调整**：本章的机械约束主张不变，但应优先保留「检查结果」的约束（测试、类型、架构规则），谨慎对待「规定步骤」的约束（强制流程、关卡）。后者最容易被模型进步淘汰。
- **并行放大架构缺陷**：Peter Steinberger 说，同步数据库访问在一个智能体时没问题，到 50 个并行会话就成了瓶颈（[XK-004](/sources/x/constraints#xk-004)）。

## 国内大厂佐证 {#cn-bigtech}

> 腾讯、阿里、字节的公开材料（数字均为团队自报、尚未独立验证；横向比较见 [国内大厂对比](/compare/cn-bigtech)）：
>
> - 腾讯一个由 AI 维护的运营平台把分层规则、文件红线和检查命令写进 AGENTS.md，提交前必须过 lint/类型检查（[TX02](/sources/cn-bigtech/tencent#tx02)）；QQ 音乐用 IDL 门禁防止 AI 猜依赖（[TX05](/sources/cn-bigtech/tencent#tx05)）。
> - 腾讯游戏 SRE 让所有变更必经 Git 与人工 Review，用 Harness 管住 LLM 的不确定性（[TX17](/sources/cn-bigtech/tencent#tx17)）；国内已出现针对“驾驭工程（Harness）能力”的信通院成熟度评估（[BD18](/sources/cn-bigtech/bytedance#bd18)）。

## 与传统软件工程认知的对比

| 维度 | 传统认知 | 智能体时代 | 判断 | 佐证（支持／异议） |
| --- | --- | --- | --- | --- |
| 分层架构 | 小团队早期做严格分层是过度设计，等规模大了再说 | 有智能体时，严格分层是**早期前提**（[OA01](/sources/openai#oa01)） | **反转**：智能体的「团队规模」相当于几百人 | [P05 · 184／12](/compare/evidence#p05) |
| 架构守护 | 靠架构师评审、团队自律、口头传承 | 靠机械检查；评审只处理语义层面 | **修正**：ArchUnit 类工具从可选变为必需 | [P04 · 128／15](/compare/evidence#p04) |
| Lint 规则 | 太多规则让人烦，常被关掉 | 对智能体没有「烦」的成本；规则越明确越好 | **反转**：人嫌啰嗦的规则成了乘数 | [P04 · 128／15](/compare/evidence#p04) |
| 错误信息 | 写给人看，简洁即可 | 写给智能体看，**包含修复指导** | **新增** | [P04 · 128／15](/compare/evidence#p04) |
| YAGNI | 不为不存在的需求设计 | 依然成立，且要防止智能体过度设计（[TW09](/sources/thoughtworks#tw09)） | **延续** | — |
| 技术债 | 定期「还债冲刺」 | 持续、小额、自动化偿还（[OA01](/sources/openai#oa01)） | **修正**：清理成本骤降 | — |
| 康威定律 | 系统结构映射组织沟通结构 | 智能体之间缺乏明确结构时协调会失败（[VD03](/sources/vendors#vd03)），架构边界必须显式定义并强制 | **延伸**：约束替代了「组织边界」的作用 | [P05 · 184／12](/compare/evidence#p05) |

> 「佐证」列：原则编号 · 独立支持作者数／异议数（疑似 + 人工确认），关键词自动归类，口径见 [共识度/佐证](/compare/evidence)。

**选择理由**：传统团队里，大量架构约束是靠「人的共识 + 评审」维持的，这在人与人之间可行，因为人有记忆、有声誉、会学习。智能体没有这些，每次会话都从零开始，且会完美地复制它看到的任何模式。因此，**凡是你希望「永远成立」的东西，都必须从文档升级为可执行检查**——这正是传统工程中「规范即代码」「Policy as Code」思想的彻底应用。好消息是，这类工具（ArchUnit、dependency-cruiser、自定义 lint）早已成熟，而且智能体能帮你低成本地写出它们。

**证据强度**：「确定性检查优于提示」是**共识**（厂商文档、Thoughtworks、国内大厂一致）；OpenAI 的具体规模数字是**厂商自报**；门禁严格程度是**分歧**。
