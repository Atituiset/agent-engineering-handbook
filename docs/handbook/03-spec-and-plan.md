# 03 · 规格驱动与计划先行

[[toc]]

## 要点

- **先计划、后编码**是几乎所有厂商与资深工程师的第一条建议。
- 计划的价值在于**让人在最便宜的时刻纠偏**：改一份 Markdown 计划比改一千行代码便宜得多。
- **规格要「刚好够用」**：目标、约束、完成标准必须有；需求模糊处必须澄清，否则智能体会用假设填补。
- **按任务规模选流程**：小 bug 不要套完整的规格驱动流程。
- **规格驱动开发（SDD）仍在早期**，工具差异大，警惕文档泛滥与「瀑布回潮」。

## 1. 为什么计划先行

智能体最常见的失败之一是**在需求空白处自行假设**。Thoughtworks 的实验里，即便采用了参考应用、分步工作流，智能体仍会「在需求的空白处做出变换不定的假设」（[TW14](/sources/thoughtworks#tw14)）。Meta 的 Forum 团队总结：人能凭直觉消化的歧义，会直接导致智能体失败，所以要把规划当作技术规格来写（[BT12](/sources/bigtech#bt12)）。

各家的「计划先行」做法高度一致：

| 来源 | 做法 |
| --- | --- |
| Cursor（[VD01](/sources/vendors#vd01)） | Plan Mode：调研代码库 → 提问澄清 → 生成可编辑的 Markdown 计划 → 再实现 |
| Claude Code（[AN07](/sources/anthropic#an07)、[X08](/sources/x-posts#x08)） | 计划模式；接受计划后清空上下文执行 |
| OpenAI（[OA05](/sources/openai#oa05)） | 大改动先用 Ask 模式出计划，再切 Code 模式 |
| HumanLayer（[VD20](/sources/vendors#vd20)） | 研究 → 计划 → 实现，人评审研究与计划的杠杆最高 |
| Google Conductor（[BT03](/sources/bigtech#bt03)） | 每项工作一个 track：`spec.md` + `plan.md`，人审批后执行 |
| Harper Reed（[PR29](/sources/practitioners#pr29)） | 一次问一个问题打磨 `spec.md` → 推理模型生成 `prompt_plan.md` → 逐步执行 |
| Mitchell Hashimoto（[PR21](/sources/practitioners#pr21)） | 先自己做 AI 之前的规划；关键处自己写骨架再让智能体填充 |
| Superpowers（[OS08](/sources/open-source#os08)） | brainstorming → 计划 → 按任务派发子智能体 |

HumanLayer 的论点尤其值得资深工程师注意：在大型存量代码库里，**一行错误的研究会导致上千行错误的代码**，所以人的评审应集中在研究与计划阶段（[VD20](/sources/vendors#vd20)）。

## 2. 一份够用的任务说明

OpenAI 的四要素模板几乎可以直接用（[OA04](/sources/openai#oa04)）：

- **Goal**：要达成什么（而不是怎么做）。
- **Context**：相关文件、报错、文档链接。
- **Constraints**：标准、架构、安全要求、不许碰的地方。
- **Done when**：可验证的完成标准——哪些测试通过、哪个页面能看到什么。

Cognition 的建议类似：像对待能力强但缺乏上下文的初级工程师那样，给出方法和起点、定义完成标准与验证方式（[VD07](/sources/vendors#vd07)）。GitHub 把 issue 本身当作提示，要求写清验收标准与涉及文件（[BT14](/sources/bigtech#bt14)、[BT17](/sources/bigtech#bt17)）。

**任务粒度**：Devin 18 个月的经验是最适合交给智能体的任务相当于初级工程师 4–8 小时的工作量，需求清晰前置、结果可验证（[VD08](/sources/vendors#vd08)）。

## 3. 让智能体「拷问」你

在动手之前让智能体反过来提问，消除歧义、暴露隐含假设——Thoughtworks 雷达称之为 Grilling，列为 Trial（[TW29](/sources/thoughtworks#tw29)）。Harper Reed 的「一次只问一个问题」（[PR29](/sources/practitioners#pr29)）与 Superpowers 的 brainstorming 技能（[OS08](/sources/open-source#os08)）是同一思路。

## 4. 规格驱动开发（SDD）：三个层次

Böckeler 把 SDD 分成三个层次（[TW06](/sources/thoughtworks#tw06)）：

| 层次 | 含义 | 代表工具 |
| --- | --- | --- |
| Spec-first | 先写规格，再让 AI 开发；规格用完可弃 | 大多数 Plan Mode |
| Spec-anchored | 规格随功能演进持续维护，是长期事实源 | Kiro（[VD16](/sources/vendors#vd16)）、Conductor（[BT03](/sources/bigtech#bt03)） |
| Spec-as-source | 人只编辑规格，不碰代码 | Tessl 等（实验性） |

工具对比：Spec Kit 按 Specify → Plan → Tasks → Implement 分阶段，每阶段有人工检查点（[BT15](/sources/bigtech#bt15)、[OS03](/sources/open-source#os03)）；Kiro 用三份文件（需求、设计、任务），需求用 EARS 记法写验收标准（[VD15](/sources/vendors#vd15)、[VD16](/sources/vendors#vd16)）；BMad 强调流程按工作规模伸缩（[OS04](/sources/open-source#os04)）；阿里 Qoder 也走 Spec 驱动路线（[CN10](/sources/chinese#cn10)）。

### 分歧与警告

- **对小问题流程过重**：Böckeler 用 Kiro 修一个小 bug，需求文档把它变成 4 个用户故事、16 条验收标准，「像拿大锤砸核桃」（[TW06](/sources/thoughtworks#tw06)）。
- **评审 Markdown 未必比评审代码容易**：大量生成的规格文档难以审阅（[TW06](/sources/thoughtworks#tw06)）。
- **文档泛滥**：生成的 Markdown 很快过时，智能体会被过时文档误导（[TW31](/sources/thoughtworks#tw31)）。
- **对前期大设计的怀疑**：Böckeler 认为历史经验表明小步迭代才是保持掌控的最好方式（[TW06](/sources/thoughtworks#tw06)）；雷达把 SDD 列为 Assess（[TW33](/sources/thoughtworks#tw33)）。
- **另一面**：OpenAI 25 小时的长程任务之所以成功，关键是规格文件、带验收标准的里程碑计划与持续更新的进度文档的组合（[OA06](/sources/openai#oa06)）；Addy Osmani 也主张把规格当作结构化 PRD，但强调简单任务不需要厚重规格（[PR28](/sources/practitioners#pr28)）。

**本手册的取舍**：**按风险和规模选流程。** 小改动：一段带「Done when」的提示即可；中等功能：Plan Mode 产出计划，人审一遍；大型或长程任务：spec-anchored，规格、计划、进度文件入库并持续维护。计划文件完成使命后要么归档、要么删除，不要让它们变成新的过时文档。

## 5. 计划里应该写什么

- 要改哪些文件/模块、为什么。
- 每一步的验证方式（跑哪个测试、看哪个页面）。
- 明确的「不做什么」（防止范围蔓延；[TW14](/sources/thoughtworks#tw14) 观察到智能体常实现未要求的功能）。
- 拆分为可独立提交、独立验证的小步（[PR28](/sources/practitioners#pr28)、[PR16](/sources/practitioners#pr16)）。
- 涉及架构决策时，引用或新增 ADR（[TW35](/sources/thoughtworks#tw35)）。

## 2026-11 新证据：计划先行是共识，「plan mode」不是 {#new-evidence}

P01「计划先行、规格先于代码」有 260 位独立作者支持，但人工确认的异议也最集中。**结论调整**：要坚持的是「先想清楚、写下来、让人审过」，而不是某个特定的工具模式。

- **异议来自工具作者本人**：Claude Code 负责人 Boris Cherny 说自己现在用 auto mode 而不是 plan mode（[XP-005](/sources/x/plan#xp-005)）。Thariq 说很多用户自己做计划，不需要 plan mode（[XP-007](/sources/x/plan#xp-007)）。字节 Trae 2.0 弃用了固定的 Proposal + Plan 流程，因为随着模型变强，它反而限制了模型发挥（[CN25](/sources/chinese#cn25)、[CN26](/sources/chinese#cn26)）。
- **计划的价值在于人审**：Burke Holland 提醒，如果全盘接受智能体计划里的默认建议，计划这一步等于白做（[XP-006](/sources/x/plan#xp-006)）。这与本章「计划是评审对象」的论点一致。
- **企业侧更强调 SPEC**：国内多家团队把 SPEC 当作核心资产，像管理代码一样管理，并要求写清验收与禁止事项（[CN14](/sources/chinese#cn14)、[CN13](/sources/chinese#cn13)）。SDD 的规范被定位为「促进人机对话，而非操作手册」（[CN15](/sources/chinese#cn15)）。腾讯一个团队的踩坑结论是，前置需求澄清比加并发更有效（[CN21](/sources/chinese#cn21)）。Qoder 的 Quest Mode 要求长任务前先写清变更细节与验证标准（团队自报，[AL15](/sources/chinese#al15)）；蚂蚁把痛点概括为“文档追不上代码、验证追不上迭代”，用 SDD 四步规范驱动（议题摘要，[AL24](/sources/chinese#al24)）。火山引擎 AgentKit 把 Spec 当作人与 Agent 的任务合约（目标、边界、依赖、验收标准）（议题摘要，[BD15](/sources/chinese#bd15)）；腾讯研发工具链从“配置驱动”转向“意图驱动”（议题摘要，[TX14](/sources/chinese#tx14)）。

## 与传统软件工程认知的对比

| 维度 | 传统认知 | 智能体时代 | 判断 | 佐证（支持／异议） |
| --- | --- | --- | --- | --- |
| 前期设计 | 敏捷反对大前期设计（BDUF），主张演进式设计 | 计划先行重新变得重要，但计划是**以小时计**的，不是以月计 | **延续敏捷精神**：「刚好够用的设计」，只是频率更高 | [P01 · 260／14](/compare/evidence#p01) |
| 需求文档 | 常被视为官僚负担，口头沟通 + 代码即文档 | 智能体无法「问隔壁同事」，书面化的意图成为必需（[BT12](/sources/bigtech#bt12)） | **修正**：书面意图的价值上升 | [P01 · 260／14](/compare/evidence#p01) |
| 设计评审 | 评审设计文档，再评审代码 | 评审**计划**的杠杆高于评审代码（[VD20](/sources/vendors#vd20)） | **加强**：评审前移 | [P01 · 260／14](/compare/evidence#p01) |
| 用户故事 / 验收标准 | 给人看的沟通工具 | 变成智能体的「完成判据」（[OA04](/sources/openai#oa04)、[VD15](/sources/vendors#vd15)） | **延续**，并要求可机器验证 | [P06 · 298／18](/compare/evidence#p06) |
| 模型驱动开发（MDD） | 曾承诺「只改模型、自动生成代码」，多数失败 | Spec-as-source 有相似的承诺与风险（[TW06](/sources/thoughtworks#tw06)） | **警惕历史重演** | [P01 · 260／14](/compare/evidence#p01) |
| 估算 | 估算编码工作量 | 编码几乎不再是成本中心，估算重点转向澄清、验证与评审 | **修正** | — |

> 「佐证」列：原则编号 · 独立支持作者数／异议数（疑似 + 人工确认），关键词自动归类，口径见 [共识度/佐证](/compare/evidence)。

**选择理由**：计划先行不是回到瀑布。瀑布的问题是反馈周期长（月级）；而智能体时代的「计划—执行—验证」循环是小时级甚至分钟级的，它本质上是**把敏捷的短反馈环压得更短**，同时补上了智能体缺失的「隐性共识」。经典的 YAGNI 与小步迭代原则正好用来约束 SDD 工具的过度文档化倾向。

**证据强度**：「先计划后编码」是**共识**；SDD 工具的价值是**分歧**（Thoughtworks 谨慎，工具厂商积极）；「研究/计划评审杠杆最高」是**经验判断**，尚无对照研究。
