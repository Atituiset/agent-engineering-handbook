# 传统工程 vs Agent 时代：总表

> 给有多年开发经验的读者：你熟悉的那些原则，在智能体时代哪些依然成立、哪些需要修正、哪些被反转？每一行都给出判断与理由，并回链到手册章节和原始来源。

[[toc]]

## 判断标记

- **延续**：原则依然成立，做法基本不变。
- **加强**：原则依然成立，而且比以前更重要。
- **修正**：原则的目标不变，但实现方式需要改变。
- **反转**：过去的权衡在新的成本结构下方向相反。
- **分歧**：一线实践者意见不一，需要自己判断。

## 总表

| 经典实践 / 认知 | 智能体时代的变化 | 判断 | 理由 | 详见 |
| --- | --- | --- | --- | --- |
| **设计评审** | 评审对象前移到「计划」，频率从月级变为小时级 | 修正 | 智能体在需求空白处做假设；改计划远比改代码便宜（[VD20](/sources/vendors#vd20)、[TW14](/sources/thoughtworks#tw14)） | [03](/handbook/03-spec-and-plan) |
| **TDD** | 作为行为约束有效；作为证据需要外部检验 | 分歧 | 支持：[PR09](/sources/practitioners#pr09)、[PR15](/sources/practitioners#pr15)；保留：[TW04](/sources/thoughtworks#tw04) | [05](/handbook/05-verification) |
| **测试金字塔** | E2E、属性、差分测试价值上升 | 修正 | 最难被糊弄；编写成本由智能体承担（[AN18](/sources/anthropic#an18)） | [05](/handbook/05-verification) |
| **测试覆盖率** | 容易被刷高，变异分数更有意义 | 修正 | AI 写的测试可能「只会通过」（[TW23](/sources/thoughtworks#tw23)） | [05](/handbook/05-verification) |
| **代码评审（逐行）** | 多层检查 + 风险分级 | 修正 | 「有人读过」是不精确的代理指标（[AN19](/sources/anthropic#an19)）；均匀评审沦为表演（[TW27](/sources/thoughtworks#tw27)） | [06](/handbook/06-review-collaboration) |
| **小 PR / 小步提交** | 更加重要 | 加强 | AI 倾向大批量，信任需要小步验证（[PR16](/sources/practitioners#pr16)、[PR12](/sources/practitioners#pr12)） | [06](/handbook/06-review-collaboration) |
| **DRY** | 智能体倾向复制粘贴；需要工具主动对冲 | 加强 | 克隆代码上升、重构下降（[RS05](/sources/research#rs05)）；智能体复制已有模式（[OA01](/sources/openai#oa01)） | [04](/handbook/04-architecture-constraints) |
| **分层架构（小团队早期）** | 从「过度设计」变为「早期前提」 | 反转 | 智能体的有效「团队规模」相当于几百人；约束让速度不以腐化为代价（[OA01](/sources/openai#oa01)） | [04](/handbook/04-architecture-constraints) |
| **架构守护靠评审与自律** | 靠机械检查（ArchUnit、自定义 lint、结构测试） | 修正 | 智能体没有记忆与声誉，只有可执行检查能持续生效（[AN01](/sources/anthropic#an01)、[CN06](/sources/chinese#cn06)） | [04](/handbook/04-architecture-constraints) |
| **Lint 规则少一点，别烦人** | 规则越明确越好，报错信息写修复指导 | 反转 | 对智能体没有「烦」的成本；一旦编码处处生效（[OA01](/sources/openai#oa01)） | [04](/handbook/04-architecture-constraints) |
| **文档越详尽越好** | 越精简越好；只写模型读不到的 | 反转 | 上下文有限且会腐化（[AN10](/sources/anthropic#an10)）；概览类内容无益（[RS06](/sources/research#rs06)） | [02](/handbook/02-context-engineering) |
| **ADR** | 增加用途：智能体可读的「为什么」 | 加强 | 防止架构被无意推翻（[TW35](/sources/thoughtworks#tw35)） | [04](/handbook/04-architecture-constraints) |
| **单一事实源** | 从代码扩展到文档与上下文 | 加强 | 冲突的文档会误导智能体（[CN03](/sources/chinese#cn03)、[TW31](/sources/thoughtworks#tw31)） | [02](/handbook/02-context-engineering) |
| **结对编程** | 「与 AI 结对」不能替代人与人结对 | 延续 | 知识传播与集体所有权是社会功能（[TW13](/sources/thoughtworks#tw13)、[TW30](/sources/thoughtworks#tw30)） | [06](/handbook/06-review-collaboration) |
| **持续集成** | 地位更高；要更快、要能被智能体本地复现 | 加强 | CI 是最终防线；反馈要尽量前移到 hook（[CN03](/sources/chinese#cn03)、[AN03](/sources/anthropic#an03)） | [04](/handbook/04-architecture-constraints) |
| **阻塞式合并门禁** | 极高吞吐下可放宽流程性门禁，但不放宽架构不变量 | 分歧 | OpenAI 放宽（[OA01](/sources/openai#oa01)）；Anthropic 不许掩盖 flaky（[AN18](/sources/anthropic#an18)） | [04](/handbook/04-architecture-constraints) |
| **YAGNI** | 依然成立，并用于约束智能体与 SDD 工具 | 延续 | 智能体常实现未要求的功能、为不存在的问题设计（[TW14](/sources/thoughtworks#tw14)、[TW09](/sources/thoughtworks#tw09)） | [03](/handbook/03-spec-and-plan) |
| **反对大前期设计（BDUF）** | 计划先行，但计划是小时级的 | 延续 | 小步迭代仍是保持掌控的最好方式（[TW06](/sources/thoughtworks#tw06)） | [03](/handbook/03-spec-and-plan) |
| **模型驱动开发** | Spec-as-source 有相似承诺与风险 | 警惕 | 历史上多数未兑现（[TW06](/sources/thoughtworks#tw06)） | [03](/handbook/03-spec-and-plan) |
| **康威定律** | 智能体没有组织结构；架构边界必须显式强制 | 延伸 | 平级自协调失败，需要层级（[VD03](/sources/vendors#vd03)） | [04](/handbook/04-architecture-constraints) |
| **Brooks 定律** | 加智能体同样有协调成本 | 延续 | 读并行、写单线程（[VD06](/sources/vendors#vd06)） | [07](/handbook/07-harness-tools) |
| **代码行数不是生产率** | 「AI 代码占比」是新变种 | 延续 | 古德哈特定律（[TW32](/sources/thoughtworks#tw32)） | [08](/handbook/08-team-process) |
| **选择无聊技术** | 对智能体更友好 | 加强 | 可组合、API 稳定、训练数据中常见（[OA01](/sources/openai#oa01)） | [07](/handbook/07-harness-tools) |
| **Unix 哲学** | 智能体最友好的接口 | 加强 | CLI、文本、可组合（[X11](/sources/x-posts#x11)、[PR17](/sources/practitioners#pr17)） | [07](/handbook/07-harness-tools) |
| **最小权限** | 智能体必须默认沙箱 | 加强 | 提示注入无根治方案（[SC01](/sources/security#sc01)、[TW24](/sources/thoughtworks#tw24)） | [09](/handbook/09-security) |
| **人工审批危险操作** | 审批疲劳；改为沙箱 + 分类器 + 风险分级 | 修正 | 93% 请求被批准（[AN26](/sources/anthropic#an26)） | [09](/handbook/09-security) |
| **技术债专项治理** | 持续、自动化、随需求消化 | 修正 | 清理成本骤降（[OA01](/sources/openai#oa01)、[CN01](/sources/chinese#cn01)） | [08](/handbook/08-team-process) |
| **「写代码很贵」** | 写代码便宜，好代码依然贵 | 修正 | 成本从打字转向验证与设计（[PR08](/sources/practitioners#pr08)） | [01](/handbook/01-mental-model) |
| **「写测试太费时」** | 不再成立 | 反转 | [PR10](/sources/practitioners#pr10) | [05](/handbook/05-verification) |

## 三条贯穿性的结论

### 1. 「隐性」必须变成「显性」

传统团队靠大量隐性机制运转：口头共识、代码评审中的言传身教、老员工的记忆、对彼此声誉的在意。智能体不参与这些机制。所以凡是重要的东西，都要显性化：意图写成计划，约定写成规则，规则能机械化的写成检查，历史写成 ADR。

### 2. 经典纪律的「性价比」被重新定价

属性测试、变异测试、架构测试、严格分层、详尽的 lint——过去它们「好是好，但太贵」。智能体让编写和维护它们的成本骤降，同时让它们的价值（约束一个不知疲倦但不可信的生产者）骤升。**过去因成本放弃的最佳实践，现在值得重新捡起来。**

### 3. 人的价值集中到判断与责任

智能体可以承担越来越多的「how」，但「why」——做什么、为什么、什么算对、出了问题谁负责——仍然在人这里（[TW08](/sources/thoughtworks#tw08)、[X04](/sources/x-posts#x04)、[CN07](/sources/chinese#cn07)）。这正是多年工程经验最有价值的地方。

## 进一步阅读

- [决策指南：什么时候用什么](./decision-guide)
- [实践手册导读](/handbook/)
