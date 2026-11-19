# 02 · 上下文工程：给什么、给多少、何时给

[[toc]]

## 要点

- **上下文是边际收益递减的有限资源。** 越长召回越差（context rot），越杂越容易冲突。
- **AGENTS.md / CLAUDE.md 是「地图」，不是「百科全书」。** 只写模型读不到、猜不到、且每次都需要的东西。
- **渐进式披露**：常驻上下文只放索引，细节按需加载（skills、链接文档、子目录规则）。
- **能交给确定性工具的，就别写进上下文。** 「不要让 LLM 干 linter 的活。」
- **会话要短、任务要窄**：一个任务一个会话；纠错优先「回溯」而不是「追加纠正」。
- **定期修剪**：每次换模型都重新审视规则，删掉不再需要的。

## 1. 为什么「写更多规则」反而更糟

Anthropic 把上下文定义为有限的「注意力预算」，并指出 context rot：上下文越长，模型对其中信息的召回越差（[AN10](/sources/anthropic#an10)）。Drew Breunig 给出了四种失败模式：中毒、分心、混淆、冲突（[PR36](/sources/practitioners#pr36)）。HumanLayer 的经验是前沿模型大约能较稳定地遵循 150–200 条指令，建议 CLAUDE.md 不超过 300 行、越短越好（[VD19](/sources/vendors#vd19)）。

Anthropic 自己也踩过坑：在内部转录里看到「适当写文档」与「不要加注释」这类互相冲突的指令同时出现在一次请求中；为新模型删掉 80% 以上系统提示后，评测没有可测量的损失（[X07](/sources/x-posts#x07)，厂商自报）。一次质量事故复盘甚至追溯到一条「减少啰嗦」的系统提示指令（[AN32](/sources/anthropic#an32)）。Thoughtworks 雷达把这种现象列为 Caution：**智能体指令膨胀**（[TW20](/sources/thoughtworks#tw20)）。

## 2. 证据：上下文文件到底有没有用？（分歧）

这是本手册中证据冲突最明显的话题，必须并列呈现：

| 来源 | 结论 | 场景 |
| --- | --- | --- |
| arXiv 2602.11988（[RS06](/sources/research#rs06)） | 上下文文件**总体不提高**成功率，成本增加 20% 以上；但其中的指令被很好遵守；仓库概览没用；适合写**非标准实践** | SWE-bench 类任务 + 真实仓库 issue |
| arXiv 2605.10039（[RS07](/sources/research#rs07)） | 文件大小、位置、结构、矛盾**都没有可检测影响**；会话越长遵守率越低 | 1,650 次会话、单一简单标注指令 |
| Vercel（[VD11](/sources/vendors#vd11)） | 把约 8KB 文档索引放进 AGENTS.md 达到 100%，skills 最高 79%，56% 用例里 skill 没被调用 | 训练数据之外的新框架 API |
| Meta（[BT11](/sources/bigtech#bt11)） | 59 份精炼上下文文件让每任务工具调用减少约 40% | 大型数据管线的「部落知识」（团队自报） |
| GitHub（[BT16](/sources/bigtech#bt16)） | 分析 2,500+ 仓库：命令前置、用代码示例、写清边界 | 写法建议，非效果研究 |

**如何调和**：这些结果其实并不矛盾——上下文文件对「**模型本来就知道或能自己读到的东西**」（仓库概览、通用最佳实践）没用甚至有害；对「**模型不可能知道的东西**」（团队私有约定、训练截止后的新 API、隐性业务知识）有用。所以：

> **只写模型读不到、猜不到的东西。** 仓库结构它自己会 `ls`，通用规范它早就学过；你的分层约定、禁用的库、某个模块的历史坑，它不可能知道。

## 3. 写法：一份好的 AGENTS.md 包含什么

综合 [OA01](/sources/openai#oa01)、[OA04](/sources/openai#oa04)、[BT16](/sources/bigtech#bt16)、[AN08](/sources/anthropic#an08)、[VD19](/sources/vendors#vd19)、[X04](/sources/x-posts#x04)：

1. **命令**：构建、测试、lint、启动的确切命令（放最前面）。
2. **边界**：总是做 / 先问 / 绝不做。
3. **非标准约定**：团队特有的、与社区惯例不同的做法。
4. **坑点（gotchas）**：那些「看起来该这样、其实不行」的地方（[X07](/sources/x-posts#x07)、[AN21](/sources/anthropic#an21)）。
5. **地图**：指向更详细文档的链接，而不是把文档内容抄进来。OpenAI 用约 100 行的 AGENTS.md 只做目录，知识放在结构化的 `docs/` 中（[OA01](/sources/openai#oa01)）。

维护规则：Greg Brockman 给 OpenAI 团队的建议是**每当智能体出错或吃力时就更新 AGENTS.md**（[X04](/sources/x-posts#x04)）；Anthropic 的建议是如果一条规则加粗强调后仍被忽略，就把它改成 hook（[AN01](/sources/anthropic#an01)）。两者结合：**先写进文件；若仍被违反且不能有例外，升级为确定性检查；若已不再被需要，删掉。**

## 4. 渐进式披露

Thoughtworks 雷达把渐进式上下文披露列为 Adopt（[TW18](/sources/thoughtworks#tw18)）。实现手段：

- **Skills**：启动时只看到名称与描述，需要时才加载全文（[AN14](/sources/anthropic#an14)、[PR06](/sources/practitioners#pr06)）。Anthropic 把验证与代码评审从系统提示挪进了按需调用的 skills（[X07](/sources/x-posts#x07)）。
- **分层规则文件**：全局 → 仓库根 → 子目录，越近越优先（[OA03](/sources/openai#oa03)、[AN02](/sources/anthropic#an02)）；Cursor 规则可按文件通配符生效（[VD02](/sources/vendors#vd02)）。
- **工具按需发现**：Tool Search 与代码执行，避免一次加载全部工具定义（[AN15](/sources/anthropic#an15)、[AN16](/sources/anthropic#an16)）。

**权衡（分歧）**：Vercel 的实验说明，对「每个任务都需要」的知识，常驻上下文比依赖模型主动调用 skill 更可靠（[VD11](/sources/vendors#vd11)）。经验法则：**高频且必需 → 常驻索引；低频或专项 → skill。**

## 5. 会话管理：短、窄、可回溯

- **一个任务一个会话**；纠错时用回溯代替纠正——退回到失败尝试之前，带着教训重新下指令，而不是让失败尝试留在上下文里（[CN11](/sources/chinese#cn11)）。
- **计划与执行分离上下文**：Claude Code 在接受计划时自动清空上下文，称显著提高计划遵守度（[X08](/sources/x-posts#x08)，厂商自报）。
- **有意压缩**：HumanLayer 建议把上下文利用率保持在约 40–60%，研究、计划、实现各阶段产出可评审的 Markdown 文件再开新上下文（[VD20](/sources/vendors#vd20)）。
- **子智能体隔离噪声**：把探索、跑测试、读大量日志交给子智能体，只把结论带回（[AN04](/sources/anthropic#an04)、[TW28](/sources/thoughtworks#tw28)、[PR11](/sources/practitioners#pr11)）。
- **评估压缩质量**：Factory 用「探针」问题检验压缩后是否还记得报错、改过的文件、下一步与决策理由（[VD14](/sources/vendors#vd14)）。

LangChain 的四分类是很好的思考框架：**写出去（Write）、选进来（Select）、压缩（Compress）、隔离（Isolate）**（[VD18](/sources/vendors#vd18)）。Manus 的生产经验补充了 KV 缓存友好（前缀稳定、只追加）与「屏蔽而非移除工具」（[VD17](/sources/vendors#vd17)）。

## 6. 文档本身也会成为负担

智能体会读到过时文档并被误导。Thoughtworks 把 AI 驱动的文档泛滥列为 Caution（[TW31](/sources/thoughtworks#tw31)）。蚂蚁数科强调「唯一事实源」：哪份文件定义设计契约、API 以哪份为准必须明确，不能有多个相互冲突的来源（[CN03](/sources/chinese#cn03)）。OpenAI 用后台任务扫描过时文档并开 PR 修复（[OA01](/sources/openai#oa01)）。

## 2026-11 新证据：精简仍是主流，但「多给」和「少给」都有新数据 {#new-evidence}

P02「上下文精简、按需加载」与 P03「项目说明文件短小且持续维护」分别有 327 与 210 位独立作者支持，是全库最强的共识之一。新证据带来三点修正。

- **长上下文确实会退化**：Chroma 的 Context Rot 报告显示，模型表现随输入长度变化并不均匀。HN 评论区的一线经验是对话越长越差，「一旦混乱就重新开始」（[HN29](/sources/hackernews#hn29)）。官方中文文档给出的量化建议是每个 CLAUDE.md 控制在 200 行以内，因为较长的文件会降低遵守度（[CN30](/sources/chinese#cn30)）。
- **「按需加载」不一定胜过「直接放进去」**：Vercel 的评测里，把压缩后的文档索引直接放进 AGENTS.md，效果好于让智能体按需调用 skill；56% 的案例中 skill 从未被调用（[HN15](/sources/hackernews#hn15)）。**结论调整**：渐进式披露的前提是模型真的会去取。关键知识如果放在可选的 skill 里，可能根本没被读到。
- **规则要随模型删减**：Anthropic 为新模型删掉了约 80% 的系统提示词（[XC-020](/sources/x/context#xc-020)）。Every 团队发现新模型在旧 skills 下表现变差，删掉重来反而更好（[XC-021](/sources/x/context#xc-021)）。Dirk Kok 删除了全部 skills，并精简了 agents.md（[XC-024](/sources/x/context#xc-024)）。这加强了本章「规则演进要主动删减」的判断。
- **异议**：Mckay Wrigley 主张首先要痴迷上下文工程，宁可多给（[XC-003](/sources/x/context#xc-003)）。dex 认为自动压缩已大幅改进，显式清理不总是必要（[XC-042](/sources/x/context#xc-042)），为智能体写的摘要文档只有在提速且不降质时才值得（[XC-041](/sources/x/context#xc-041)）。中文团队把这件事称为「AI 上下文负债」：棕地代码库的隐性知识不会因为换了模型而自动可理解（[CN44](/sources/chinese#cn44)）。

## 国内大厂佐证 {#cn-bigtech}

> 腾讯、阿里、字节的公开材料（数字均为团队自报、尚未独立验证；横向比较见 [国内大厂对比](/compare/cn-bigtech)）：
>
> - 腾讯云数据库团队把团队记忆组织成“工程事实 / 项目语义 / bug 经验”三层图谱，Bug 定位成功率 58%→65%，并自注只是子任务信号（[TX01](/sources/cn-bigtech/tencent#tx01)）；QQ 音乐把大仓里的隐性规范、服务契约等五类盲区落成工程制品（[TX05](/sources/cn-bigtech/tencent#tx05)）。
> - 字节 MarsCode/Trae 用实时代码知识图谱突破大仓上下文限制（[BD12](/sources/cn-bigtech/bytedance#bd12)），TRAE 团队建议“短对话、每次只做一件事”（[BD13](/sources/cn-bigtech/bytedance#bd13)）；阿里的判断是复杂系统的关键知识不在代码里，需要显式沉淀（[AL06](/sources/cn-bigtech/alibaba#al06)）。

## 与传统软件工程认知的对比

| 维度 | 传统认知 | 智能体时代 | 判断 | 佐证（支持／异议） |
| --- | --- | --- | --- | --- |
| 文档 | 写给人看，详尽越好；常常没人读 | 写给智能体看，每次都被读；**越精简越好** | **修正**：文档从「参考」变成「运行时输入」，冗余有直接成本 | [P02 · 327／23](/compare/evidence#p02) |
| 编码规范 | 写在 wiki 里，靠评审执行 | 能机械检查的交给 linter/hook，只把「判断题」留给上下文（[VD19](/sources/vendors#vd19)） | **加强**：「规范即代码」从最佳实践变成必需 | [P04 · 128／15](/compare/evidence#p04) |
| 知识传承 | 靠老员工口口相传、结对 | 隐性知识必须显性化，否则智能体永远不知道（[BT11](/sources/bigtech#bt11)） | **修正**：部落知识是智能体效果的上限 | [P03 · 210／13](/compare/evidence#p03) |
| 单一事实源 | DRY 原则应用于代码 | DRY 同样应用于文档与上下文（[CN03](/sources/chinese#cn03)） | **延续并扩展** | [P03 · 210／13](/compare/evidence#p03) |
| 规则演进 | 规则只增不减，越积越多 | 规则要随模型能力**主动删减**（[TW20](/sources/thoughtworks#tw20)） | **新增**：progression testing | [P19 · 52／5](/compare/evidence#p19) |
| 「多给信息总没错」 | 给人更多背景通常有益 | 多余信息会稀释注意力、引入冲突（[AN10](/sources/anthropic#an10)） | **反转** | [P02 · 327／23](/compare/evidence#p02) |

> 「佐证」列：原则编号 · 独立支持作者数／异议数（疑似 + 人工确认），关键词自动归类，口径见 [共识度/佐证](/compare/evidence)。

**选择理由**：传统上「文档写得越全越好」是因为人能自行筛选、跳读；模型不能有效跳读，每个 token 都参与注意力竞争。因此上下文工程更像**接口设计**而不是写文档：最小化、明确、可组合、版本化。当证据冲突时（[RS06](/sources/research#rs06) vs [VD11](/sources/vendors#vd11)），按「模型能否自己获得这条信息」来决定是否写进上下文，是目前最能自洽的判断标准。

**证据强度**：「精简优于冗长」是**共识**；上下文文件的净效果是**分歧**（研究与厂商实验结论不同）；具体数字（150–200 条、40–60%）是**经验值**，不要当作硬阈值。
