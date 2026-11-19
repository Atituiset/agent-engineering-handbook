# 12 · 质量保障：用测试、CI/CD 与评审守住 AI 交付

[[toc]]

## 要点

- **CI 是唯一不会被智能体说服的评审者。** 智能体可以声称「测试全过」，可以改测试、删断言；只有在它无法改动的环境里、由它无法批准的检查给出的结论才算数（[QT15](/sources/quality/tools#qt15)、[QB01](/sources/quality/bigtech#qb01)、[QX31](/sources/quality/x#qx31)）。
- **先定义「完成」，再让智能体写。** 测试先行、验收条件结构化并回喂给生成环节，这是 TDD 在智能体时代的新形态（[QP01](/sources/quality/practitioners#qp01)、[QC10](/sources/quality/chinese#qc10)、[QX10](/sources/quality/x#qx10)）。
- **测试是 AI 写的，所以要验证测试本身。** 覆盖率上升不等于能发现缺陷；变异、属性、差分与端到端测试更难被糊弄（[QB07](/sources/quality/bigtech#qb07)、[QT08](/sources/quality/tools#qt08)、[QX04](/sources/quality/x#qx04)）。
- **防作弊要做成机制。** 删除或修改测试、放宽断言、加 sleep 让 flaky 变绿，都是有记录的行为；用受保护文件、CODEOWNERS 和测试改动守卫来拦（[QR02](/sources/quality/research#qr02)、[QP02](/sources/quality/practitioners#qp02)、[QH15](/sources/quality/hn#qh15)）。
- **AI 评审是第一道筛子，不是最后一道闸。** 大厂的做法都是高精度、低噪声、按「是否被采纳/解决」来度量，人负责合并（[QB06](/sources/quality/bigtech#qb06)、[QT21](/sources/quality/tools#qt21)、[QC06](/sources/quality/chinese#qc06)）。
- **提示词、技能和智能体本身也要回归测试**：Evals 进 CI，让「把智能体变差的 PR」合不进去（[QT01](/sources/quality/tools#qt01)、[QX26](/sources/quality/x#qx26)）。
- **速度补不了不稳定。** DORA 2025 的结论是：AI 带来的速度并不能通过快速失败、快速修复抵消交付不稳定性（[QR06](/sources/quality/research#qr06)）。

> 本章是第 05 章（验证与测试）和第 06 章（评审与协作）在「交付流水线」层面的延伸，聚焦 CI/CD、门禁、评审自动化与度量。资料来自本次新增的 143 条精选（[质量与 CI/CD 专题](/sources/quality/)）和 681 条全量库条目（[全量库 · 质量专题](/library/q-curated)）。

## 1. 一张图：分层门禁 {#layers}

一线团队的做法可以归纳成「越早越便宜、越晚越权威」的分层结构：

| 层 | 在哪里跑 | 典型检查 | 谁说了算 | 代表来源 |
| --- | --- | --- | --- | --- |
| L0 编辑时 | 智能体循环内、hooks | 格式化、lint、类型检查、相关单测 | 智能体自检（可被绕过） | [QT04](/sources/quality/tools#qt04)、[QB02](/sources/quality/bigtech#qb02)、[QC03](/sources/quality/chinese#qc03) |
| L1 提交前 | 本地 / 智能体的沙箱 | 全量单测、集成测试、本地 AI 预评审 | 作者（人）负责 | [QX29](/sources/quality/x#qx29)、[QP04](/sources/quality/practitioners#qp04) |
| L2 PR CI | 独立 runner | 必需检查、测试改动守卫、安全扫描、evals | **CI，智能体不能改、不能批** | [QB03](/sources/quality/bigtech#qb03)、[QB05](/sources/quality/bigtech#qb05)、[QT16](/sources/quality/tools#qt16) |
| L3 评审 | PR 页面 | AI 评审（建议性）＋人工评审（意图、风险、问责） | 人 | [QB06](/sources/quality/bigtech#qb06)、[QP07](/sources/quality/practitioners#qp07)、[QH04](/sources/quality/hn#qh04) |
| L4 合并 | 合并队列 | 组合后的必需检查 | CI | [QT17](/sources/quality/tools#qt17)、[QH13](/sources/quality/hn#qh13) |
| L5 发布后 | 预发 / 生产 | 金丝雀、功能开关、遥测、回滚 | 运维信号 | [QB17](/sources/quality/bigtech#qb17)、[QR06](/sources/quality/research#qr06) |

两条贯穿的原则：

1. **反馈左移，但裁决不左移。** Stripe 的说法是：如果知道某个自动检查会让 CI 失败，最好在 IDE 或 push 时就拦下（[QB02](/sources/quality/bigtech#qb02)）。但左移的检查只是给智能体的提示，最终裁决仍在 CI。Spotify 起初想在智能体的 VM 里「重造 CI」，后来改为把验证运行时与智能体运行时分离，由验证服务调用真实 CI 并把失败摘要回给智能体（[QB05](/sources/quality/bigtech#qb05)）。
2. **限制回合数。** Stripe 的无人值守智能体最多跑两轮 CI，之后交回工程师（[QB01](/sources/quality/bigtech#qb01)）。无限重试会让智能体「试」出一个碰巧通过的版本。

## 2. 十三条质量原则 {#principles}

下面每条原则都给出做法、代表来源和需要注意的边界。共识度统计见 [第 8 节](#consensus)。

### Q01 · 测试先行 / 可执行规格 {#q01}

- Kent Beck 在说明文件里要求智能体走红—绿—重构，只在测试通过时重构，并把「智能体在作弊，比如禁用或删除测试」列为需要人工介入的信号（[QP01](/sources/quality/practitioners#qp01)）。他在访谈中称 TDD 是与智能体协作的「超能力」，同时坦言很难阻止智能体为了通过而删测试（[QP03](/sources/quality/practitioners#qp03)）。
- 手淘 TEKO 团队把验收条件结构化后回喂给生码环节：「判据先行，这才是 AI 原生的 TDD」（[QC10](/sources/quality/chinese#qc10)）。美团给出三条策略：用单测替代肉眼审查、给存量代码先补安全网、复杂需求用 TDD（[QC01](/sources/quality/chinese#qc01)）。
- Addy Osmani：评审开始前先定义「完成」，否则评审者总能找到「可以改进」的地方（[QX10](/sources/quality/x#qx10)）。
- **关键做法：写测试与写实现分开。** 写测试的会话和写实现的会话分开，实现会话只能看到它无权修改的测试（[QC16](/sources/quality/chinese#qc16)）。
- **异议**：有人质疑多数「LLM + TDD」文章并不是真正的 TDD，只是「先写一堆测试再一直改到全绿」（[QH07](/sources/quality/hn#qh07)）；也有人认为在需求频繁变动时 TDD 会显著增加 token 成本（[HN 评论](https://news.ycombinator.com/item?id=48418239)）。

### Q02 · 给智能体可运行的验证闭环 {#q02}

- Boris Cherny 的三条建议之一：给 Claude 验证输出的方式，比如单元测试、浏览器扩展、移动端模拟器（[QX05](/sources/quality/x#qx05)）。Addy Osmani 转述：有了这套流程，Claude Code 90% 以上的代码由它自己写；当生成速度超过评审速度，瓶颈转移到「证明」（[QX03](/sources/quality/x#qx03)）。
- Simon Willison：一套干净通过的测试能大幅放大编码智能体的价值（[QP06](/sources/quality/practitioners#qp06)）；但不要因为有自动化测试就跳过手工测试（[QP04](/sources/quality/practitioners#qp04)）。
- 把「完成的定义」从提示词变成机制：Claude Code 的 Stop hook 可以派生子智能体核实测试，未通过就不允许结束（[QT04](/sources/quality/tools#qt04)）；Spotify 在开 PR 前必须跑完所有相关 verifier（[QB03](/sources/quality/bigtech#qb03)）。
- 「执行阶梯」的概括很准确：关键的分界在于「请智能体守规矩」与「机械地验证它的产出」（[QX31](/sources/quality/x#qx31)、[QH10](/sources/quality/hn#qh10)）。

### Q03 · CI 是独立的最终裁判 {#q03}

- GitHub 给 Copilot 云端智能体内置的护栏：不能把自己的 PR 标为待评审，不能批准或合并；触发任务的人也不能批准该 PR；默认在有写权限的用户批准前不运行 Actions 工作流（[QT15](/sources/quality/tools#qt15)）。企业教程建议用规则集统一合并要求，并把智能体说明文件和工作流纳入 CODEOWNERS（[QT16](/sources/quality/tools#qt16)）。
- OpenHands 早期让 AI 当 PR 创建者，结果触发者可以自批自合，出事也找不到负责人；后来改为每个 PR 都由人拥有（[QH04](/sources/quality/hn#qh04)）。
- Spotify 的原则是「周边基础设施不变」：选仓库、开 PR、评审、合并的流程与人工改动完全相同，智能体只替换「写改动」这一步（[QB04](/sources/quality/bigtech#qb04)）。
- 阿里云的「质量门禁」文章把它总结为：快速门禁在修改后跑，集成与回归在任务完成前跑，PR 阶段由 CI 在独立环境里全量验证（[QC03](/sources/quality/chinese#qc03)）。

### Q04 · 防作弊 {#q04}

有记录的作弊形态：

| 形态 | 来源 |
| --- | --- |
| 删除失败测试而不修 bug | [QR02](/sources/quality/research#qr02)、[QX30](/sources/quality/x#qx30) |
| 删断言、删整个测试、伪造大段实现 | [QP02](/sources/quality/practitioners#qp02) |
| 修改测试期望值让测试变绿 | [QX25](/sources/quality/x#qx25) |
| 把整个测试包进 try-catch，使测试形同虚设 | [QT07](/sources/quality/tools#qt07) |
| 篡改计时器、评分代码，找参考答案 | [QR01](/sources/quality/research#qr01)、[QT14](/sources/quality/tools#qt14) |
| 加 sleep 或重试，让 flaky 测试「变绿」 | [QX32](/sources/quality/x#qx32) |
| 只跑模型挑的测试、放宽超时、mock 掉依赖来「提速」 | [QH12](/sources/quality/hn#qh12)、[QH15](/sources/quality/hn#qh15) |
| 声称「已通过测试」但验证被夸大 | [QC04](/sources/quality/chinese#qc04) |

应对：

- **把测试当作受保护资产。** Anthropic 让编码智能体只能修改功能清单里的 `passes` 字段，并明确禁止删改测试（[QT02](/sources/quality/tools#qt02)）。在 CI 中加「测试改动守卫」：测试文件被删除、断言数下降或快照被批量重写时，要求 CODEOWNERS 批准（见 [示例 B](#example-b)）。
- **ImpossibleBench 的发现值得记住**：提示词、测试访问权限和反馈循环都会显著影响作弊率（[QR02](/sources/quality/research#qr02)）。也就是说，作弊可以通过环境设计来降低，而不只能事后抓。
- **监控只是补充。** OpenAI 发现用 LLM 监控思维链能发现「颠覆测试」，但如果在训练中惩罚坏念头，模型会学会隐藏意图（[QT14](/sources/quality/tools#qt14)）。工程上的结论是：不要依赖模型自觉，检查本身要防篡改。

### Q05 · 测试质量胜过数量 {#q05}

- Meta：覆盖率上升不一定能发现缺陷，所以用 LLM 生成「当前测试抓不到的变异体」，再生成能杀死它们的测试（[QB07](/sources/quality/bigtech#qb07)、[QB08](/sources/quality/bigtech#qb08)）。TestGen-LLM 只保留能构建、稳定通过、确实提升覆盖的测试（[QB09](/sources/quality/bigtech#qb09)）。
- 属性测试给了智能体更难糊弄的预言机：Anthropic 的智能体在 100 多个 Python 包中发现真实缺陷，人工复核后 56% 的报告为有效 bug（论文自报，[QT07](/sources/quality/tools#qt07)、[QT08](/sources/quality/tools#qt08)）。
- 同义反复测试（测试只是把实现再写一遍）是 AI 测试的典型问题：Matt Pocock 把「Tautological tests considered harmful.」写进规范（[QX04](/sources/quality/x#qx04)）；David Cramer 抱怨 GPT 总写大量琐碎单测（[QX15](/sources/quality/x#qx15)）。
- 端到端测试作为基准真相（[QX11](/sources/quality/x#qx11)）；但智能体写 E2E 时容易选脆弱的选择器（[QX36](/sources/quality/x#qx36)）。
- **测试集本身也是会出错的预言机。** SWE-bench 上「已解决」的补丁可能通过测试却不符合开发者预期（[QR05](/sources/quality/research#qr05)）；METR 发现「测试通过」的智能体 PR 平均还需约 42 分钟才能达到可合并状态（[QR04](/sources/quality/research#qr04)）；差分测试只报「不一致」，不保证正确（[QX34](/sources/quality/x#qx34)）。
- Datadog 的取舍：与其逐行审查智能体的 diff，不如把时间投入到收紧不变量、扩大仿真覆盖的 harness 上（[QB17](/sources/quality/bigtech#qb17)）。

### Q06 · AI 评审是补充而非替代 {#q06}

- **大厂的共同点是「先过滤、再发言」，并按采纳来度量。** Uber uReview 把评审拆成生成→过滤→校验→去重，用精确率-召回率看板分阶段上线（[QB06](/sources/quality/bigtech#qb06)）；Google 只展示高置信的修改建议，以「被应用」比例来评估（[QB10](/sources/quality/bigtech#qb10)）；字节 BitsAI-CR 用 Outdated Rate 衡量评论是否真正被采纳（[QC09](/sources/quality/chinese#qc09)）；Cursor 用「解决率」代替表情反馈（[QT21](/sources/quality/tools#qt21)）；腾讯报告了好评率与采纳率（[QC06](/sources/quality/chinese#qc06)）。以上数字均为团队或厂商自报。
- **控噪声。** Codex 在 GitHub 上只标 P0/P1 问题（[QT10](/sources/quality/tools#qt10)）；OpenAI 建议把格式和 lint 留给 CI，评审规则只写需要判断的东西（[QT11](/sources/quality/tools#qt11)）；Atlassian 发现给 AI 评审者喂相似 PR 的评审对话有效，堆更多跨仓库代码反而会降低质量（[QB16](/sources/quality/bigtech#qb16)）。
- **把评审意见沉淀为规则**：发现智能体的坏习惯就写进规范，由评审技能强制（[QX07](/sources/quality/x#qx07)）；Bugbot 从合并结果中学规则（[QT22](/sources/quality/tools#qt22)）。
- **定位**：微软明确把 AI 评审者定位为减轻同伴负担，而非替代（[QB12](/sources/quality/bigtech#qb12)）；Addy Osmani 认为评审的重心是风险、意图与问责（[QP07](/sources/quality/practitioners#qp07)）。
- **异议**：HN 高赞评论认为 AI 评审能抓到关键 bug，但信噪比差，不想对每个 PR 默认开启（[QH01](/sources/quality/hn#qh01)）；有人认为非确定性的 AI 评审与 CI 的目的相冲突，更适合放在本地 pre-push（[QH14](/sources/quality/hn#qh14)）；还有人根本质疑「靠严格质检兜底高失败率流程」的思路（[QH09](/sources/quality/hn#qh09)）。我们的取舍是：**AI 评审在 CI 里以建议性（非阻塞）方式运行**，阻塞性门禁只留给确定性检查。

### Q07 · 异构 / 对抗评审：作者≠评审者 {#q07}

- DHH 的做法：用 Codex 写时让 Claude 评，反之亦然（[QX02](/sources/quality/x#qx02)）。HN 上有人在关键代码上再找「另一家前沿实验室」的模型评审（[QH16](/sources/quality/hn#qh16)）。
- Cursor Bugbot 多路并行评审，多个独立评审都标出同一问题才视为强信号（[QT21](/sources/quality/tools#qt21)）。
- 中文社区的说法是「查杀分离」：智能体自写自测存在「认知同源」风险，测试要独立于实现路径（[QC11](/sources/quality/chinese#qc11)）。Spotify 在确定性 verifier 之上加了一层只看 diff 与原始 prompt 的 LLM 裁判（[QB03](/sources/quality/bigtech#qb03)）。
- **异议**：有人认为编码与评审「完全独立」未必是优势，外部评审者可能不了解组织背景（[QH02](/sources/quality/hn#qh02)）。

### Q08 · Evals 即 CI {#q08}

- 智能体、提示词、技能本身也是要回归测试的软件。Anthropic 区分能力评测与回归评测，建议从真实失败中整理 20–50 个任务起步，尽量用确定性检查判断最终状态（[QT01](/sources/quality/tools#qt01)）；Claude Code 推出插件 evals，用来确认技能在新模型发布后是否仍然有效（[QX18](/sources/quality/x#qx18)）。
- 黄金集要覆盖核心功能、历史 bug 和客户永远不能坏的查询，并由干系人签字（[QX39](/sources/quality/x#qx39)）；把 eval 集放进 CI，让变差的 PR 无法合并（[QX26](/sources/quality/x#qx26)）。
- **裁判也要被测试。** LLM 裁判本质上是分类器，要对照人工标签（[QX14](/sources/quality/x#qx14)、[QP12](/sources/quality/practitioners#qp12)）；只看「一致率」会误导，永远判「通过」的裁判在错误占 5% 时也有 95% 一致率（[QP12](/sources/quality/practitioners#qp12)）；LLM 生成的评估器会继承被评估 LLM 的问题（[QP15](/sources/quality/practitioners#qp15)）。
- 评测的两部分完全不同：发现失败模式，以及度量其频率（[QX16](/sources/quality/x#qx16)）。

### Q09 · 沙箱化验证与最小权限 {#q09}

- Stripe 的智能体运行在与生产和互联网隔离的 devbox（[QB01](/sources/quality/bigtech#qb01)）；Bugbot Autofix 在独立 VM 里测试和修复（[QT23](/sources/quality/tools#qt23)）；Braintrust 给需要沙箱的智能体打分时，每次尝试都用干净容器（[QX38](/sources/quality/x#qx38)）。
- **CI 里的 AI 步骤本身是攻击面。** Anthropic 的安全评审 Action 明确写着未针对提示注入加固，只应评审可信 PR（[QT06](/sources/quality/tools#qt06)）；fork PR 拿不到 secrets，所以官方评审只在同仓分支 PR 上运行（[QT05](/sources/quality/tools#qt05)）；codex-action 可配置为只读、不联网，并建议使用一次性 runner（[QT12](/sources/quality/tools#qt12)）。
- 安全扫描作为必经门禁：Veracode 称 45% 的样本未通过安全测试（厂商自报，[QR10](/sources/quality/research#qr10)）；Datadog 在所有 PR 上用 LLM 检测恶意代码（[QB18](/sources/quality/bigtech#qb18)）；腾讯把漏洞检出准确率从 26% 提到 95%（团队自报，[QC08](/sources/quality/chinese#qc08)）。

### Q10 · 消灭 flaky：确定性、可复现 {#q10}

- 智能体把 flaky 失败当成需要纠正的反馈，随后的偶然通过又强化了可能错误的修改（[QX33](/sources/quality/x#qx33)）。
- 不允许用 sleep 或重试「修」flaky，要求找到原因（[QX32](/sources/quality/x#qx32)）。Stripe 和 Shopify 都把 flaky 测试单独处理（[QB01](/sources/quality/bigtech#qb01)、[QB15](/sources/quality/bigtech#qb15)）。
- Shopify Roast 把智能体流程写成可复现、可测试的结构化工作流，确定性步骤与智能体步骤交替（[QB15](/sources/quality/bigtech#qb15)）。

### Q11 · 小步发布与可回滚 {#q11}

- 合并队列把多个 PR 组合后一起跑必需检查（[QT17](/sources/quality/tools#qt17)）。测试太慢时，HN 上的建议是用合并队列，而不是让模型挑测试跑（[QH13](/sources/quality/hn#qh13)、[QH12](/sources/quality/hn#qh12)）。
- Kent Beck 观察到智能体想「一步跳到终点」，人要强制小步、持续跑测试（[QP02](/sources/quality/practitioners#qp02)）。
- **异议**：功能开关不是银弹。大团队的资深工程师常被开关蔓延和死代码拖累（[QX12](/sources/quality/x#qx12)）。开关要有到期时间和清理任务。

### Q12 · 度量结果而非产量 {#q12}

- 推荐的指标包括：**解决率 / 采纳率**（评审意见是否在合并时被处理，[QT21](/sources/quality/tools#qt21)、[QC09](/sources/quality/chinese#qc09)、[QB10](/sources/quality/bigtech#qb10)）、**变更失败率与交付稳定性**（DORA，[QR06](/sources/quality/research#qr06)）、**重复率与短期 churn**（[QR09](/sources/quality/research#qr09)），以及**测试检出率**（变异分数、预言机的召回与误报，[QC02](/sources/quality/chinese#qc02)）。
- 只看采纳率不够：得物用准确度、覆盖度、使用率等多维指标评估用例生成（[QC13](/sources/quality/chinese#qc13)）。
- **方法提醒**：「AI PR 的 bug 多 1.7 倍」这类厂商数字，最多只能说明「被发现的」问题更多（[QH08](/sources/quality/hn#qh08)、[QR08](/sources/quality/research#qr08)）。METR 的随机对照试验显示，资深开发者在熟悉的大型仓库里用 AI 反而更慢（[QR03](/sources/quality/research#qr03)）。

### Q13 · 来源透明与贡献者责任 {#q13}

- Simon Willison：提交 PR 就是用你的信誉担保代码能用，AI 辅助不改变你是作者这一事实（[QH05](/sources/quality/hn#qh05)、[QP04](/sources/quality/practitioners#qp04)）。
- 开源项目的政策光谱：LLVM 要求贡献者读过并审查所有 LLM 生成内容并标注（[QO01](/sources/quality/oss#qo01)）；Ghostty 要求披露，并且必须能不借助 AI 解释改动（[QO03](/sources/quality/oss#qo03)）；QEMU 拒绝被认为包含 AI 生成内容的贡献（[QO02](/sources/quality/oss#qo02)）；curl 被 AI 生成的低质量漏洞报告消耗（[QO04](/sources/quality/oss#qo04)）。
- 平台侧的可追溯：Copilot 云端智能体的提交带签名（[QT15](/sources/quality/tools#qt15)）。

## 3. 反模式速查 {#anti-patterns}

| 反模式 | 为什么有害 | 替代做法 | 来源 |
| --- | --- | --- | --- |
| 让智能体自己判断「完成」 | 它会声称完成却没测 | Stop hook / CI 必需检查 | [QP05](/sources/quality/practitioners#qp05)、[QT04](/sources/quality/tools#qt04) |
| 测试、实现、评审都在同一会话 | 认知同源，测试描述的是代码而非需求 | 测试与实现分会话，异构评审 | [QC16](/sources/quality/chinese#qc16)、[QC11](/sources/quality/chinese#qc11) |
| 以覆盖率为目标 | 覆盖率上升不等于能发现缺陷 | 变异分数、属性测试 | [QB07](/sources/quality/bigtech#qb07) |
| 允许智能体随意改测试和快照 | 改期望值就能变绿 | 测试改动守卫 + CODEOWNERS | [QX25](/sources/quality/x#qx25)、[QT16](/sources/quality/tools#qt16) |
| 用 sleep / 重试掩盖 flaky | 竞态仍在，并误导智能体 | 隔离、修根因 | [QX32](/sources/quality/x#qx32)、[QX33](/sources/quality/x#qx33) |
| 让 LLM 挑选要跑的测试来提速 | 等于降低覆盖率 | 合并队列、确定性的测试选择 | [QH12](/sources/quality/hn#qh12)、[QH13](/sources/quality/hn#qh13) |
| AI 评审作为阻塞门禁、全量开启 | 非确定、噪声大、成本累积 | 建议性运行，只报高置信问题 | [QH14](/sources/quality/hn#qh14)、[QH01](/sources/quality/hn#qh01)、[QX28](/sources/quality/x#qx28) |
| 在 `pull_request_target` 中带密钥跑 AI 步骤 | 提示注入加上密钥等于泄露 | 只读权限，不给 fork PR 密钥 | [QT06](/sources/quality/tools#qt06)、[QT05](/sources/quality/tools#qt05) |
| 无限次 CI 重试 | 会「试」出碰巧通过的版本 | 限定回合，超过后交回人 | [QB01](/sources/quality/bigtech#qb01) |
| 用 LLM 裁判却不校准 | 一致率高也可能什么都没抓到 | 对照人工标签看精确率与召回率 | [QP12](/sources/quality/practitioners#qp12) |

## 4. GitHub Actions 示例 {#examples}

::: warning 示例说明
以下 YAML 是**通用的示意性示例**，用来说明门禁结构，不来自任何特定公司。第三方 Action 名称用占位符表示。实际使用前请按项目调整命令，把第三方 Action 固定到 commit SHA，并在仓库设置中把相应 job 设为必需检查（required status checks）。
:::

### 示例 A：必需检查，同时支持合并队列 {#example-a}

```yaml
# .github/workflows/ci.yml（示例）
name: ci
on:
  pull_request:
  merge_group:            # 让合并队列在组合后的分支上再跑一遍
permissions:
  contents: read
concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true
jobs:
  checks:
    runs-on: ubuntu-latest
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20, cache: npm }
      - run: npm ci
      - run: npm run lint
      - run: npm run typecheck
      - run: npm test -- --ci          # 不设自动重试；flaky 测试需要单独隔离
```

### 示例 B：测试改动守卫 {#example-b}

测试文件被删除，或者断言数量下降时，CI 失败，除非 PR 带有 `tests-change-approved` 标签。配合 CODEOWNERS 使用，这个标签只能由指定的人添加，修改测试目录也需要他们批准。

```yaml
# .github/workflows/test-guard.yml（示例）
name: test-guard
on:
  pull_request:
    types: [opened, synchronize, labeled, unlabeled]
permissions:
  contents: read
jobs:
  guard:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - name: Detect deleted tests or fewer assertions
        if: ${{ !contains(github.event.pull_request.labels.*.name, 'tests-change-approved') }}
        env:
          BASE: ${{ github.event.pull_request.base.sha }}
        run: |
          set -euo pipefail
          deleted=$(git diff --diff-filter=D --name-only "$BASE"...HEAD -- 'tests/**' '**/*.test.*' '**/*_test.*' || true)
          if [ -n "$deleted" ]; then echo "Deleted test files:"; echo "$deleted"; exit 1; fi
          pat='assert|expect\(|should\.'
          removed=$(git diff "$BASE"...HEAD -- 'tests/**' '**/*.test.*' '**/*_test.*' | grep -E '^-[^-]' | grep -cE "$pat" || true)
          added=$(git diff "$BASE"...HEAD -- 'tests/**' '**/*.test.*' '**/*_test.*' | grep -E '^\+[^+]' | grep -cE "$pat" || true)
          if [ "$removed" -gt "$added" ]; then echo "Assertions decreased ($removed removed, $added added)"; exit 1; fi
```

```text
# .github/CODEOWNERS（示例）
/tests/                    @your-org/test-owners
/.github/workflows/        @your-org/platform
AGENTS.md                  @your-org/platform
/evals/                    @your-org/ai-quality
```

### 示例 C：Evals 进 CI，回归即失败 {#example-c}

```yaml
# .github/workflows/evals.yml（示例）
name: evals
on:
  pull_request:
    paths: ['prompts/**', 'agent/**', 'skills/**', 'evals/**']
permissions:
  contents: read
jobs:
  regression-evals:
    if: github.event.pull_request.head.repo.full_name == github.repository   # fork PR 不带密钥
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r evals/requirements.txt
      - name: Run golden + regression sets (multiple trials)
        env:
          MODEL_API_KEY: ${{ secrets.MODEL_API_KEY }}
        run: python evals/run.py --suite golden --suite regression --trials 3 --out results.json
      - name: Compare with baseline on main
        run: python evals/compare.py --baseline evals/baseline.json --current results.json --max-drop 0.02
```

### 示例 D：AI 评审作为建议性步骤 {#example-d}

```yaml
# .github/workflows/ai-review.yml（示例）
name: ai-review
on:
  pull_request:            # 不要用 pull_request_target 给不可信代码配密钥
permissions:
  contents: read
  pull-requests: write
jobs:
  review:
    if: github.event.pull_request.head.repo.full_name == github.repository
    runs-on: ubuntu-latest
    continue-on-error: true   # 建议性，不阻塞合并；阻塞门禁留给确定性检查
    steps:
      - uses: actions/checkout@v4
      - uses: your-org/ai-review-action@<pinned-sha>   # 占位符：替换为你选用的评审 Action
        with:
          rules-file: AGENTS.md          # 只写需要判断的规则；格式与 lint 交给 CI
          min-severity: high             # 只报高置信、高严重度问题
        env:
          MODEL_API_KEY: ${{ secrets.MODEL_API_KEY }}
```

仓库设置建议，与示例配套：

- 受保护分支或规则集：要求 PR、要求示例 A 和示例 B 通过、要求 Code Owners 评审、禁止绕过、启用合并队列。
- 「Require approval for all outside collaborators」：外部贡献者的工作流需要审批后才运行（[QT06](/sources/quality/tools#qt06)、[QT15](/sources/quality/tools#qt15)）。
- 智能体使用的机器人账号不在可批准者之列；发起任务的人不能批准该 PR（[QT15](/sources/quality/tools#qt15)、[QH04](/sources/quality/hn#qh04)）。

## 5. 与传统软件工程认知的对比 {#compare}

| 经典认知 | 智能体时代：仍成立 / 需修正 | 理由 | 来源 |
| --- | --- | --- | --- |
| **测试金字塔**：大量单测、少量 E2E | **需修正**：单测变得廉价，也更容易是同义反复；E2E、属性、变异、差分测试的相对价值上升 | 单测的生产成本几乎为零，稀缺的变成「能否发现缺陷」；更高层的测试更难被实现细节糊弄 | [QX11](/sources/quality/x#qx11)、[QX15](/sources/quality/x#qx15)、[QB07](/sources/quality/bigtech#qb07)、[QT08](/sources/quality/tools#qt08) |
| **TDD** 是个人纪律 | **加强**：从个人纪律变为给智能体的接口，测试就是规格和完成定义 | 智能体需要可执行的判据；先写测试也让作弊更容易被识别 | [QP01](/sources/quality/practitioners#qp01)、[QC10](/sources/quality/chinese#qc10)、[QC16](/sources/quality/chinese#qc16) |
| **覆盖率**是质量指标 | **不再足够** | 智能体能轻易刷高覆盖率；Meta 明确说覆盖率上升不一定能发现缺陷 | [QB07](/sources/quality/bigtech#qb07)、[QO05](/sources/quality/oss#qo05) |
| **CI** 用来集成人的改动 | **加强并改变角色**：CI 成为唯一不被智能体控制的裁判；PR 数量上升使合并队列和测试选择成为必需 | 智能体能改代码、改测试、改说明，却不能改受保护分支上的必需检查 | [QT15](/sources/quality/tools#qt15)、[QT17](/sources/quality/tools#qt17)、[QB05](/sources/quality/bigtech#qb05) |
| **CI 要快** | **仍成立，但要防「假提速」** | 智能体优化 CI 时可能跳过或削弱测试 | [QH15](/sources/quality/hn#qh15)、[QH12](/sources/quality/hn#qh12) |
| **代码评审**的目的是找 bug | **需修正**：逐行找 bug 的部分交给确定性检查和 AI 初筛；人的评审转向意图、风险与问责，并前移到设计 | 生成速度超过人的阅读速度；AI 评审只适合高置信问题 | [QP07](/sources/quality/practitioners#qp07)、[QH03](/sources/quality/hn#qh03)、[QB06](/sources/quality/bigtech#qb06) |
| **作者≠评审者**（四眼原则） | **加强并扩展到模型**：生成者与评判者分离，最好是不同模型或不同上下文 | 同一模型自写自测存在「认知同源」风险 | [QX02](/sources/quality/x#qx02)、[QC11](/sources/quality/chinese#qc11) |
| **持续交付**：小批量、快速回滚 | **仍成立且更重要**：DORA 发现 AI 的速度补不了不稳定 | 吞吐上升后，没有小批量和回滚，故障会成批出现 | [QR06](/sources/quality/research#qr06)、[QR07](/sources/quality/research#qr07) |
| **功能开关**降低发布风险 | **仍成立，但有成本** | 开关蔓延本身就是技术债 | [QX12](/sources/quality/x#qx12) |
| **质量度量**：缺陷密度、变更失败率 | **仍成立，需新增**：AI 评审的解决率/采纳率、测试的变异分数、eval 通过率 | 新的生产者需要新的结果指标；产量指标（行数、PR 数）更容易被刷 | [QT21](/sources/quality/tools#qt21)、[QC09](/sources/quality/chinese#qc09)、[QR09](/sources/quality/research#qr09) |
| 测试是确定性的 | **新增**：产品中含 LLM 时需要 evals（多次试验、裁判校准） | 同一输入可能得到不同输出，传统测试方法不足 | [QT13](/sources/quality/tools#qt13)、[QT01](/sources/quality/tools#qt01) |

**总的选择理由**：经典工程纪律没有过时，只是「谁来遵守」变了。过去这些纪律靠工程师的自律和同伴压力维持，现在大部分代码出自一个会为了「完成」而走捷径的生产者，所以纪律必须**机械化**（写成 CI 和规则集）、**对生产者不可改**（受保护文件、CODEOWNERS、合并权限），并且**用结果度量**。这与第 04 章「约束靠环境，不靠告诉」是同一个结论在交付流水线上的体现。

## 6. 落地清单 {#checklist}

**第一周**

- [ ] 主分支开启规则集：必需检查 + 至少一位人工批准 + 禁止绕过；智能体账号不能批准（[QT15](/sources/quality/tools#qt15)、[QT16](/sources/quality/tools#qt16)）
- [ ] 在 AGENTS.md 写清楚「如何确认工作」的确切命令（[QT03](/sources/quality/tools#qt03)）
- [ ] 加上测试改动守卫和 CODEOWNERS（[示例 B](#example-b)）
- [ ] 加一个 Stop hook 或等价机制：测试不过不能结束（[QT04](/sources/quality/tools#qt04)）
- [ ] 禁止用 sleep 或重试修 flaky 测试，并写进说明文件（[QX32](/sources/quality/x#qx32)）

**第一个月**

- [ ] AI 评审以建议性方式接入，只报高严重度问题，并记录解决率（[QT10](/sources/quality/tools#qt10)、[QT21](/sources/quality/tools#qt21)）
- [ ] 对核心模块引入变异测试或属性测试，抽查 AI 写的测试（[QB08](/sources/quality/bigtech#qb08)、[QT09](/sources/quality/tools#qt09)）
- [ ] 若产品含 LLM：建黄金集和回归集，进 CI，并用人工标签校准裁判（[QT01](/sources/quality/tools#qt01)、[QP12](/sources/quality/practitioners#qp12)）
- [ ] 开启合并队列（[QT17](/sources/quality/tools#qt17)）
- [ ] 开 PR 前用另一个模型或另一个上下文做对抗评审（[QX02](/sources/quality/x#qx02)）

**每季度**

- [ ] 看结果指标：变更失败率、回滚率、缺陷逃逸、AI 评审解决率、flaky 比例（[QR06](/sources/quality/research#qr06)）
- [ ] 回放：最近的线上缺陷，哪一层门禁本应拦住？补上对应检查
- [ ] 删掉没人看的 AI 评审规则和过期的功能开关（[QX12](/sources/quality/x#qx12)）

## 7. 证据强度与缺口 {#evidence}

- **大厂数据多为团队自报**：Uber、Google、Meta、Cursor、腾讯、字节、快手等的采纳率和解决率都来自各自的博客或论文，口径不同，不能横向比较。
- **厂商报告有利益相关**：CodeRabbit、GitClear、Veracode 都销售相关产品（[QR08](/sources/quality/research#qr08)、[QR09](/sources/quality/research#qr09)、[QR10](/sources/quality/research#qr10)），本手册已标注「厂商自报、尚未独立验证」。
- **独立研究很少**，主要是 METR 和 DORA（[QR01](/sources/quality/research#qr01)、[QR03](/sources/quality/research#qr03)、[QR04](/sources/quality/research#qr04)、[QR06](/sources/quality/research#qr06)）以及若干 arXiv 论文；缺少「加了某个门禁后缺陷逃逸率变化」这样的对照数据。
- **部分原文未能访问**：OpenAI 的 harness engineering 文章和 OpenAI 网站上关于 Datadog 的客户案例在本次检索中返回 403；部分中文资料是会议预告或转载。
- **流水线里的工业案例**（数字均为团队自报、尚未独立验证）：字节 LogSage 一年处理 107 万次 CI/CD 执行（[BD04](/sources/quality/research#bd04)），BitsAI-Fix 自动修复静态分析告警（[BD03](/sources/quality/research#bd03)），TestGPT-Server 在 1.4 万个微服务 API 上找到 50 个崩溃 bug、仅 2 个功能 bug（[BD07](/sources/quality/research#bd07)）。阿里 AACR-Bench 带负样本集衡量评审噪声（[AL11](/sources/quality/research#al11)）；Open Code Review 的自报与社区复测分歧（[AL08](/sources/quality/oss#al08)、[AL09](/sources/quality/hn#al09)）说明团队自报 benchmark 需要独立复测（Q13）。腾讯一线团队不追求严格 TDD（[TX02](/sources/chinese#tx02)），与 [Q01](#q01) 有张力。

## 8. 共识度 {#consensus}

统计口径：在本专题的精选条目和 X 帖子中，按关键词把每条资料归入 Q01–Q13，并统计**不同作者/机构数**。精选条目的原则标签为人工标注；X 帖子为关键词自动归类。「自动检出的保留/反对」指同时命中原则关键词和否定词（如 overrated、doesn't work、worse、没用、反而）的 X 帖子作者数。「人工确认的异议」是我们读过后确认持反对或保留意见的精选条目。

| 编号 | 原则 | 支持：不同作者/机构数 | 其中精选条目 | 自动检出的保留/反对（X 帖子作者数） | 人工确认的异议条目 |
| --- | --- | --- | --- | --- | --- |
| [Q01](#q01) | 测试先行 / 可执行规格（TDD、判据先行） | 36 | 14 | 2 | [QH07](/sources/quality/hn#qh07) |
| [Q02](#q02) | 给智能体可运行的验证闭环、反馈左移 | 74 | 37 | 4 | — |
| [Q03](#q03) | CI 是独立的最终裁判：必需检查、受保护分支、不自批自合 | 89 | 25 | 5 | — |
| [Q04](#q04) | 防作弊：禁止删改/削弱测试、警惕 reward hacking | 37 | 22 | 1 | — |
| [Q05](#q05) | 测试质量胜过数量：E2E、属性、变异、差分；警惕同义反复与覆盖率指标 | 76 | 35 | 3 | — |
| [Q06](#q06) | AI 评审是补充而非替代：高精度低噪声、人负责合并 | 85 | 49 | 3 | [QH09](/sources/quality/hn#qh09) [QH14](/sources/quality/hn#qh14) |
| [Q07](#q07) | 异构 / 对抗评审：作者≠评审者 | 18 | 7 | 3 | [QH02](/sources/quality/hn#qh02) |
| [Q08](#q08) | Evals 即 CI：黄金集、回归集，LLM 裁判要对齐人工标签 | 67 | 17 | 4 | — |
| [Q09](#q09) | 沙箱化验证、最小权限、不向未审代码暴露密钥 | 42 | 15 | 4 | — |
| [Q10](#q10) | 消灭 flaky：确定性、可复现 | 30 | 7 | 5 | — |
| [Q11](#q11) | 小步发布与可回滚：合并队列、功能开关、金丝雀 | 25 | 7 | 2 | [QX12](/sources/quality/x#qx12) |
| [Q12](#q12) | 度量结果而非产量：采纳率、变更失败率、缺陷逃逸 | 38 | 19 | 2 | — |
| [Q13](#q13) | 来源透明与贡献者责任：披露、签名、人必须理解 | 22 | 11 | 3 | — |

::: tip 怎么读这张表
- **关键词匹配很粗糙**：提到「CI」的帖子不一定在支持「CI 是最终裁判」；否定词也可能出现在支持性的语境里（例如「没有测试时智能体表现更差」）。表中数字只适合看**相对量级**，不适合精确比较。
- **支持面最广的**是 Q03（CI 作为独立裁判）、Q06（AI 评审定位）、Q05（测试质量）、Q02（验证闭环）和 Q08（evals），几乎没有直接反对，争议集中在「怎么做」。
- **真正有分歧的**是：Q06（AI 评审该不该进 CI、该不该默认开启）、Q01（「LLM + TDD」是否名副其实，以及成本）、Q07（评审者是否应完全独立）、Q11（功能开关的长期成本）。
- **Q10（flaky）和 Q13（来源透明）支持者较少**，原因是讨论面较窄，不代表有争议。开源项目对 AI 贡献的态度从「披露即可」到「全面拒绝」都有（[QO01](/sources/quality/oss#qo01)–[QO03](/sources/quality/oss#qo03)）。
:::


