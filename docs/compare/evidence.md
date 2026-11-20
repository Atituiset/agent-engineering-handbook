# 共识度 / 佐证强度

> 一条实践被许多**互不相干**的作者独立提出，本身就是它可靠的证据之一；反过来，有分量的异议说明它有适用边界。本页把全量库中较早收录的 2,223 条资料（约 1,487 个不同作者/机构；全量库现有 3,195 条）按 20 条原则做了统计。**这是关键词自动归类得到的粗略信号，不是严格的文献计量**，请结合「人工确认的异议/限定」与原文阅读。
>
> 2026-11 新增的质量与 CI/CD 专题（681 条）使用另一组原则 Q01–Q13，统计结果见 [第 12 章 · 共识度](/handbook/12-quality-cicd#consensus)；本页 P01–P20 的数字仍基于原先的 2,223 条。

## 统计口径 {#method}

- **数据**：[全量库](/library/)的全部条目：X 帖子、Hacker News 讨论串、GitHub 仓库、原始报告精选条目与中文网页。
- **归类**：用正则关键词把每条匹配到原则 P01–P20（例如出现 `CLAUDE.md`/`AGENTS.md` 记为 P03）。X 帖子用全文；HN 只用标题（精选的 HN 讨论加上摘要）；GitHub 用项目描述；精选条目用整段摘要与引文。**误报与漏报都存在。**
- **独立作者**：同一作者/机构只算一次。X 按账号；HN 按被讨论文章的域名（GitHub、Medium 等平台按「域名/用户」），自述帖按提交者；GitHub 按仓库所有者；精选条目按作者/机构（例如 Anthropic 的多篇文章只算 1）。检索时已排除转推。**同一人在不同平台的账号可能被重复计数**，所以数字偏向上限。
- **支持**：匹配到该原则、且文本中**没有**否定性措辞的条目的独立作者数。
- **疑似异议（关键词）**：匹配到该原则、且文本含 “overrated / doesn't work / waste of time / 没用 / 反而” 等否定措辞的条目的独立作者数。**需要人工复核**：其中很多其实是在批评相反做法。
- **人工确认的异议/限定**：编者阅读精选条目后挑出的、明确反对或限定该原则的观点，逐条列出链接。

## 总表 {#summary}

| 原则 | 相关章节 | 独立支持 | 其中 X / HN / GitHub / 精选 | 疑似异议（关键词） | 人工确认的异议/限定 |
| --- | --- | --- | --- | --- | --- |
| [P01 计划先行、规格先于代码](#p01) | [03](/handbook/03-spec-and-plan) | **260** | 193 / 14 / 36 / 18 | 10 | 4 |
| [P02 上下文精简、按需加载](#p02) | [02](/handbook/02-context-engineering) | **327** | 246 / 22 / 37 / 25 | 20 | 3 |
| [P03 项目说明文件短小且持续维护](#p03) | [02](/handbook/02-context-engineering) | **210** | 159 / 12 / 24 / 15 | 10 | 3 |
| [P04 约束可执行化：lint、类型、CI 胜过文字](#p04) | [04](/handbook/04-architecture-constraints) | **128** | 96 / 3 / 14 / 15 | 13 | 2 |
| [P05 架构边界与不变量要显式](#p05) | [04](/handbook/04-architecture-constraints) | **184** | 144 / 5 / 17 / 19 | 11 | 1 |
| [P06 验证闭环：让智能体能自检](#p06) | [05](/handbook/05-verification) | **298** | 239 / 13 / 23 / 26 | 16 | 2 |
| [P07 测试先行（TDD）](#p07) | [05](/handbook/05-verification) | **67** | 60 / 1 / 3 / 3 | 5 | 1 |
| [P08 人工评审不可省](#p08) | [06](/handbook/06-review-collaboration) | **254** | 193 / 18 / 22 / 24 | 16 | 5 |
| [P09 小步、可回滚的变更](#p09) | [06](/handbook/06-review-collaboration) | **49** | 42 / 2 / 1 / 4 | 3 | 0 |
| [P10 子智能体隔离上下文](#p10) | [07](/handbook/07-harness-tools) | **151** | 112 / 6 / 25 / 9 | 9 | 1 |
| [P11 并行智能体与隔离工作区](#p11) | [07](/handbook/07-harness-tools) | **209** | 152 / 12 / 35 / 10 | 14 | 3 |
| [P12 Hooks 提供确定性保障](#p12) | [07](/handbook/07-harness-tools) | **164** | 115 / 2 / 34 / 14 | 5 | 0 |
| [P13 Skills 等可复用指令按需加载](#p13) | [07](/handbook/07-harness-tools) | **355** | 196 / 20 / 121 / 19 | 15 | 5 |
| [P14 工具与 MCP 要精简](#p14) | [07](/handbook/07-harness-tools) | **304** | 127 / 115 / 50 / 14 | 7 | 0 |
| [P15 最小权限与沙箱](#p15) | [09](/handbook/09-security) | **179** | 119 / 17 / 28 / 16 | 9 | 1 |
| [P16 人要理解并为代码负责](#p16) | [01](/handbook/01-mental-model) | **190** | 103 / 75 / 5 / 8 | 8 | 2 |
| [P17 成本与 token 意识](#p17) | [08](/handbook/08-team-process) | **167** | 119 / 31 / 10 / 8 | 9 | 0 |
| [P18 长任务靠外部状态与进度文件](#p18) | [07](/handbook/07-harness-tools) | **171** | 123 / 11 / 29 / 8 | 3 | 0 |
| [P19 把错误沉淀为规则（复利）](#p19) | [08](/handbook/08-team-process) | **52** | 40 / 0 / 1 / 11 | 4 | 1 |
| [P20 选主流、无聊的技术栈](#p20) | [04](/handbook/04-architecture-constraints) | **5** | 5 / 0 / 0 / 0 | 0 | 0 |

读法：支持数高说明「很多人在说」，不等于「一定对」；GitHub 与 X 上的数量也受话题热度影响（例如 Skills、MCP 相关的仓库很多）。人工确认的异议往往比数字更有信息量。特别注意：P13（Skills）、P14（MCP/工具精简）、P11（并行）的关键词只能识别「谈到了这个话题」，分不清是在推荐还是在反对、是要多装还是要精简，因此这几项的「支持」数**主要反映话题热度**，应以下方人工确认的异议为准。P20（主流技术栈）关键词过窄，数字偏低。

## P01 · 计划先行、规格先于代码 {#p01}

相关章节：[03](/handbook/03-spec-and-plan)｜独立支持 **260**（X 193、HN 14、GitHub 36、精选 18）｜疑似异议 10｜人工确认的异议/限定 4

**代表性支持**：

- [AN07 · Common workflows](/sources/anthropic#an07)（Anthropic / Claude Code）
- [OA05 · How OpenAI uses Codex](/sources/openai#oa05)（OpenAI / Codex）
- [BT03 · Conductor: Introducing context-driven development for](/sources/bigtech#bt03)（Google · Meta · GitHub）
- [VD01 · Best practices for coding with agents](/sources/vendors#vd01)（工具厂商）
- [TW06 · Understanding Spec-Driven-Development: Kiro, spec-kit](/sources/thoughtworks#tw06)（Thoughtworks 技术雷达）
- [PR02 · Vibe engineering](/sources/practitioners#pr02)（独立工程师）
- [X08 · Boris Cherny：接受计划时自动清空上下文](/sources/x-posts#x08)（X 帖子（v1 精选））
- [CN08 · 我们做了一本企业级 AI 编程实践手册（TRAE）](/sources/chinese#cn08)（火山引擎 TRAE 团队）

**人工确认的异议 / 限定**：

- [Boris Cherny：自己现在用 auto mode 而不是 plan mode](/sources/x/plan#xp-005)
- [Thariq：很多用户自己做计划，并不需要 plan mode](/sources/x/plan#xp-007)
- [Burke Holland：全盘接受默认建议的计划等于没做（限定）](/sources/x/plan#xp-006)
- [Trae 2.0 弃用固定的 Proposal + Plan 流程，交给 Agentic Loop](/sources/chinese#cn25)

**疑似异议样本（关键词命中，需人工复核）**：

- [lots feedback here, many of you are planning yourself & don't need pla](https://x.com/trq212/status/2103212051065921632)（Thariq (@trq212)）
- [Google 正式开放 Gemini 4 Carbon：付费 API 今天可用，引入价到 11 月 30 日；普通用户要订 Ultra，每月](https://x.com/dotey/status/2120191790774960630)（宝玉 (@dotey)）
- [的资深工程师在生产中跑这套循环——2026 年的收敛形态是一个刻意无聊的闭环，而支撑它的几乎所有实践，都在管理同一个约束：上下文窗口。 《A](https://x.com/yibie/status/2086618951648424157)（yibie (@yibie)）
- [给大家带来Kimi-K3.1-Pro 实测! 直接说结论, K3.1-Pro保持了一直以来的高质量前端水平. 无论是审美还是空间理解, 3D](https://x.com/karminski3/status/2115895561836720236)（karminski-牙医 (@karminski3)）
- [I've been using Claude Code for a few days for my iOS app, and it has ](https://x.com/JoshuaNewton/status/1940888060956377230)（Josh Newton (@JoshuaNewton)）
- [Anthropic 悄悄发布了一个官方插件，叫 claude-code-setup 这不是第三方工具，是 Anthropic 自己团队做的，](https://x.com/yaohui12138/status/2059819859345825923)（超级个体｜柿子 (@yaohui12138)）

## P02 · 上下文精简、按需加载 {#p02}

相关章节：[02](/handbook/02-context-engineering)｜独立支持 **327**（X 246、HN 22、GitHub 37、精选 25）｜疑似异议 20｜人工确认的异议/限定 3

**代表性支持**：

- [AN04 · Create custom subagents](/sources/anthropic#an04)（Anthropic / Claude Code）
- [OA02 · Unrolling the Codex agent loop](/sources/openai#oa02)（OpenAI / Codex）
- [BT01 · Gemini CLI（开源仓库）](/sources/bigtech#bt01)（Google · Meta · GitHub）
- [VD02 · Rules（Cursor 文档）](/sources/vendors#vd02)（工具厂商）
- [TW01 · Harness engineering for coding agent users](/sources/thoughtworks#tw01)（Thoughtworks 技术雷达）
- [PR05 · Context engineering](/sources/practitioners#pr05)（独立工程师）
- [X01 · Karpathy：+1 for "context engineering"](/sources/x-posts#x01)（X 帖子（v1 精选））
- [X08 · Boris Cherny：接受计划时自动清空上下文](/sources/x-posts#x08)（X 帖子（v1 精选））

**人工确认的异议 / 限定**：

- [Mckay Wrigley：首要是痴迷上下文工程，宁可多给（与「精简」有张力）](/sources/x/context#xc-003)
- [dex：自动压缩变好后，显式清理不总是必要（限定）](/sources/x/context#xc-042)
- [《智能体工程的 8 个等级》：天平已倾向能容忍嘈杂上下文的模型](/sources/chinese#cn33)

**疑似异议样本（关键词命中，需人工复核）**：

- [Something I have been thinking about: in the past, the best engineers ](https://x.com/bcherny/status/2077460395279692197)（Boris Cherny (@bcherny)）
- [Very interested in what the coming era of highly bespoke software migh](https://x.com/karpathy/status/2024583544157458452)（Andrej Karpathy (@karpathy)）
- [Claude Code token 总是不够用？5 个实测省 token 技巧 每次看到 token 飙到 100k+ 的时候心都在滴血。实](https://x.com/shijianzhongg/status/2077566980719309178)（婷 (@shijianzhongg)）
- [的资深工程师在生产中跑这套循环——2026 年的收敛形态是一个刻意无聊的闭环，而支撑它的几乎所有实践，都在管理同一个约束：上下文窗口。 《A](https://x.com/yibie/status/2086618951648424157)（yibie (@yibie)）
- [PSA: you might have accrued plugins that are needlessly living in your](https://x.com/nickbaumann_/status/2118458876680884299)（Nick (@nickbaumann_)）
- [Why horizontal tabs? Vertical is navigation. Organizational. Hierarchi](https://x.com/shadcn/status/2104873649702387819)（shadcn (@shadcn)）

## P03 · 项目说明文件短小且持续维护 {#p03}

相关章节：[02](/handbook/02-context-engineering)｜独立支持 **210**（X 159、HN 12、GitHub 24、精选 15）｜疑似异议 10｜人工确认的异议/限定 3

**代表性支持**：

- [AN01 · Best practices for Claude Code](/sources/anthropic#an01)（Anthropic / Claude Code）
- [OA01 · Harness engineering: leveraging Codex in an agent-fir](/sources/openai#oa01)（OpenAI / Codex）
- [BT01 · Gemini CLI（开源仓库）](/sources/bigtech#bt01)（Google · Meta · GitHub）
- [VD02 · Rules（Cursor 文档）](/sources/vendors#vd02)（工具厂商）
- [TW18 · Progressive context disclosure（Adopt，2026-11）](/sources/thoughtworks#tw18)（Thoughtworks 技术雷达）
- [X04 · Greg Brockman：OpenAI 如何让团队转向智能体式开发](/sources/x-posts#x04)（X 帖子（v1 精选））
- [CN17 · CLAUDE.md 速通全解，八大技巧让 Claude Code 起飞指南](/sources/chinese#cn17)（阿里云开发者社区（个人作者））
- [CN28 · Claude Code 作者再次分享 Anthropic 内部团队使用技巧](/sources/chinese#cn28)（Immerse（少数派作者））

**人工确认的异议 / 限定**：

- [Saoud Rizwan：提交时用 linter 强制，胜过写进 agents.md](/sources/x/constraints#xk-001)
- [Lauren Tan（宝玉整理）：每次纠正写成 lint 规则，而不是往 agents.md 加话](/sources/x/constraints#xk-005)
- [dex：为智能体写的摘要文档，只有提速且不降质时才值得](/sources/x/context#xc-041)

**疑似异议样本（关键词命中，需人工复核）**：

- [Something I have been thinking about: in the past, the best engineers ](https://x.com/bcherny/status/2077460395279692197)（Boris Cherny (@bcherny)）
- [Claude Code token 总是不够用？5 个实测省 token 技巧 每次看到 token 飙到 100k+ 的时候心都在滴血。实](https://x.com/shijianzhongg/status/2077566980719309178)（婷 (@shijianzhongg)）
- [的资深工程师在生产中跑这套循环——2026 年的收敛形态是一个刻意无聊的闭环，而支撑它的几乎所有实践，都在管理同一个约束：上下文窗口。 《A](https://x.com/yibie/status/2086618951648424157)（yibie (@yibie)）
- [感觉能调好 Codex 的可以去当心理医生了，分享一段我给 GPT 6.1 Sol 配置的 AGENTS.md ，效果非常好hh “你是 C](https://x.com/Fei2411/status/2123017612741554208)（FeiZ (@Fei2411)）
- [用 Claude Code 的都去跑一下 /doctor prompt-audit！ 这是 Claude Code 团队的 @lydiaha](https://x.com/berryxia/status/2121235974336520383)（Berryxia.AI (@berryxia)）
- [if you want to improve how you use AI or your agentic systems, the one](https://x.com/stackbenchdev/status/2052002941884661792)（StackBench (@stackbenchdev)）

## P04 · 约束可执行化：lint、类型、CI 胜过文字 {#p04}

相关章节：[04](/handbook/04-architecture-constraints)｜独立支持 **128**（X 96、HN 3、GitHub 14、精选 15）｜疑似异议 13｜人工确认的异议/限定 2

**代表性支持**：

- [AN01 · Best practices for Claude Code](/sources/anthropic#an01)（Anthropic / Claude Code）
- [OA01 · Harness engineering: leveraging Codex in an agent-fir](/sources/openai#oa01)（OpenAI / Codex）
- [VD03 · Scaling long-running autonomous coding](/sources/vendors#vd03)（工具厂商）
- [TW01 · Harness engineering for coding agent users](/sources/thoughtworks#tw01)（Thoughtworks 技术雷达）
- [PR30 · Basic Claude Code](/sources/practitioners#pr30)（独立工程师）
- [CN03 · AI Coding 的下一步不是写得更快，而是可验收：蚂蚁数科 Harness 工程实践](/sources/chinese#cn03)（InfoQ（整理蚂蚁数字科技魏长征 AICon 演讲））
- [CN06 · AI Coding 增量风险管控：Skill 门禁与 Harness 落地实践（快手，会议预告）](/sources/chinese#cn06)（InfoQ / AICon 北京（快手架构治理团队演讲预告））
- [CN12 · 如何在“不能出错”的系统里使用 AI Coding？分布式存储实践与边界](/sources/chinese#cn12)（美团基础技术部）

**人工确认的异议 / 限定**：

- [Uncle Bob：花几周搭的严格 harness，被模型进步变得多余](/sources/x/constraints#xk-003)
- [Uncle Bob：我可能在过度约束智能体（但仍保留单元测试与变异测试）](/sources/x/constraints#xk-002)

**疑似异议样本（关键词命中，需人工复核）**：

- [Software horror: litellm PyPI supply chain attack. Simple 'pip install](https://x.com/karpathy/status/2036487306585268612)（Andrej Karpathy (@karpathy)）
- [Something I have been thinking about: in the past, the best engineers ](https://x.com/bcherny/status/2077460395279692197)（Boris Cherny (@bcherny)）
- [的资深工程师在生产中跑这套循环——2026 年的收敛形态是一个刻意无聊的闭环，而支撑它的几乎所有实践，都在管理同一个约束：上下文窗口。 《A](https://x.com/yibie/status/2086618951648424157)（yibie (@yibie)）
- [程序员需要逐渐接受一个现实，未来很多编程工作会变成黑盒编程。 我们团队有不少系统是用 Rust 写的，但真正精通 Rust 的人并不多。有些](https://x.com/Barret_China/status/2123058891869098232)（Barret李靖 (@Barret_China)）
- [if you want to improve how you use AI or your agentic systems, the one](https://x.com/stackbenchdev/status/2052002941884661792)（StackBench (@stackbenchdev)）
- [I've been using Claude Code for a few days for my iOS app, and it has ](https://x.com/JoshuaNewton/status/1940888060956377230)（Josh Newton (@JoshuaNewton)）

## P05 · 架构边界与不变量要显式 {#p05}

相关章节：[04](/handbook/04-architecture-constraints)｜独立支持 **184**（X 144、HN 5、GitHub 17、精选 19）｜疑似异议 11｜人工确认的异议/限定 1

**代表性支持**：

- [AN03 · Automate actions with hooks](/sources/anthropic#an03)（Anthropic / Claude Code）
- [OA01 · Harness engineering: leveraging Codex in an agent-fir](/sources/openai#oa01)（OpenAI / Codex）
- [BT02 · Provide context with GEMINI.md files](/sources/bigtech#bt02)（Google · Meta · GitHub）
- [VD03 · Scaling long-running autonomous coding](/sources/vendors#vd03)（工具厂商）
- [TW02 · Harness Engineering — first thoughts](/sources/thoughtworks#tw02)（Thoughtworks 技术雷达）
- [PR13 · Agentic manual testing](/sources/practitioners#pr13)（独立工程师）
- [X10 · dex：「harness engineering」一词的提出](/sources/x-posts#x10)（X 帖子（v1 精选））
- [CN03 · AI Coding 的下一步不是写得更快，而是可验收：蚂蚁数科 Harness 工程实践](/sources/chinese#cn03)（InfoQ（整理蚂蚁数字科技魏长征 AICon 演讲））

**人工确认的异议 / 限定**：

- [Uncle Bob：「确定性工具强制严格流程」的假设可能过度](/sources/x/constraints#xk-002)

**疑似异议样本（关键词命中，需人工复核）**：

- [Something I have been thinking about: in the past, the best engineers ](https://x.com/bcherny/status/2077460395279692197)（Boris Cherny (@bcherny)）
- [这期用皮影戏讲清 BaoCut 虚拟主播的工作原理： - 拆：AI 画一张正面像，再改十一次，程序逐像素比对，拆出二十七层 - 动：给整张画](https://x.com/dotey/status/2120208679005810803)（宝玉 (@dotey)）
- [的资深工程师在生产中跑这套循环——2026 年的收敛形态是一个刻意无聊的闭环，而支撑它的几乎所有实践，都在管理同一个约束：上下文窗口。 《A](https://x.com/yibie/status/2086618951648424157)（yibie (@yibie)）
- [程序员需要逐渐接受一个现实，未来很多编程工作会变成黑盒编程。 我们团队有不少系统是用 Rust 写的，但真正精通 Rust 的人并不多。有些](https://x.com/Barret_China/status/2123058891869098232)（Barret李靖 (@Barret_China)）
- [Anthropic 悄悄发布了一个官方插件，叫 claude-code-setup 这不是第三方工具，是 Anthropic 自己团队做的，](https://x.com/yaohui12138/status/2059819859345825923)（超级个体｜柿子 (@yaohui12138)）
- [What if your AI coding agent could find a bug, fix it, test the soluti](https://x.com/Bic_Revelation/status/2112940728154292705)（𝓑𝓲𝓬_𝓡𝓮𝓿𝓮𝓵𝓪𝓽𝓲𝓸𝓷 (@Bic_Revelatio）

## P06 · 验证闭环：让智能体能自检 {#p06}

相关章节：[05](/handbook/05-verification)｜独立支持 **298**（X 239、HN 13、GitHub 23、精选 26）｜疑似异议 16｜人工确认的异议/限定 2

**代表性支持**：

- [AN03 · Automate actions with hooks](/sources/anthropic#an03)（Anthropic / Claude Code）
- [OA01 · Harness engineering: leveraging Codex in an agent-fir](/sources/openai#oa01)（OpenAI / Codex）
- [BT02 · Provide context with GEMINI.md files](/sources/bigtech#bt02)（Google · Meta · GitHub）
- [VD01 · Best practices for coding with agents](/sources/vendors#vd01)（工具厂商）
- [TW01 · Harness engineering for coding agent users](/sources/thoughtworks#tw01)（Thoughtworks 技术雷达）
- [PR02 · Vibe engineering](/sources/practitioners#pr02)（独立工程师）
- [X01 · Karpathy：+1 for "context engineering"](/sources/x-posts#x01)（X 帖子（v1 精选））
- [X04 · Greg Brockman：OpenAI 如何让团队转向智能体式开发](/sources/x-posts#x04)（X 帖子（v1 精选））

**人工确认的异议 / 限定**：

- [Peter Steinberger：让 Codex 决定哪些测试要跑，大幅削减 CI](/sources/x/verify#xv-007)
- [美团：CI 的绿灯本身可能不可信，要看原始输出（限定）](/sources/chinese#cn12)

**疑似异议样本（关键词命中，需人工复核）**：

- [This is a super exciting release - Claude Fable 5 is the same underlyi](https://x.com/karpathy/status/2064409694761054332)（Andrej Karpathy (@karpathy)）
- [Something I have been thinking about: in the past, the best engineers ](https://x.com/bcherny/status/2077460395279692197)（Boris Cherny (@bcherny)）
- [Google 正式开放 Gemini 4 Carbon：付费 API 今天可用，引入价到 11 月 30 日；普通用户要订 Ultra，每月](https://x.com/dotey/status/2120191790774960630)（宝玉 (@dotey)）
- [At @vercel we got to test this model before release. Best way to summa](https://x.com/rauchg/status/2119878364794372162)（Guillermo Rauch (@rauchg)）
- [Claude Code token 总是不够用？5 个实测省 token 技巧 每次看到 token 飙到 100k+ 的时候心都在滴血。实](https://x.com/shijianzhongg/status/2077566980719309178)（婷 (@shijianzhongg)）
- [的资深工程师在生产中跑这套循环——2026 年的收敛形态是一个刻意无聊的闭环，而支撑它的几乎所有实践，都在管理同一个约束：上下文窗口。 《A](https://x.com/yibie/status/2086618951648424157)（yibie (@yibie)）

## P07 · 测试先行（TDD） {#p07}

相关章节：[05](/handbook/05-verification)｜独立支持 **67**（X 60、HN 1、GitHub 3、精选 3）｜疑似异议 5｜人工确认的异议/限定 1

**代表性支持**：

- [TW04 · TDD inside the agent loop — theater or actual value?](/sources/thoughtworks#tw04)（Thoughtworks 技术雷达）
- [PR09 · Red/green TDD](/sources/practitioners#pr09)（独立工程师）
- [OS08 · Superpowers](/sources/open-source#os08)（开源项目与规范）
- [A few random notes from claude coding quite a bit last few w](/sources/x/workflow#xw-006)（Andrej Karpathy (@karpathy)）
- [Our tips on how to use Cursor: - Start with a plan (Shift+Ta](/sources/x/workflow#xw-005)（Michael Truell (@mntruell)）
- [Claude Code (Opus 4.6) vs. Codex (GPT-5.4) Reddit 上看到的「Claud](/sources/x/failures#xf-005)（meng shao (@shao__meng)）
- [发现一个非常值得收藏的 AI 编程开源项目：ECC（Everything Claude Code）。 如果你在用 Cla](/sources/x/tools#xt-041)（Sword-xyj (@SwordXyj)）
- [作者通过10个月的日常高强度使用（包括赢得 Anthropic x Forum Ventures 黑客松），构建了一套完](/sources/x/tools#xt-008)（鳞片狗 (@linpiangou)）

**人工确认的异议 / 限定**：

- [Armin Ronacher：重写系统不一定需要现成测试套件，可让智能体自建（限定）](/sources/x/verify#xv-012)

**疑似异议样本（关键词命中，需人工复核）**：

- [的资深工程师在生产中跑这套循环——2026 年的收敛形态是一个刻意无聊的闭环，而支撑它的几乎所有实践，都在管理同一个约束：上下文窗口。 《A](https://x.com/yibie/status/2086618951648424157)（yibie (@yibie)）
- [Claude Code and Codex bandaided our bug 16/16. One line fixed it: Code](https://x.com/stas_sorokin_/status/2122070969552347646)（Stanislav Sorokin (@stas_sorok）
- [What if your AI coding agent could find a bug, fix it, test the soluti](https://x.com/Bic_Revelation/status/2112940728154292705)（𝓑𝓲𝓬_𝓡𝓮𝓿𝓮𝓵𝓪𝓽𝓲𝓸𝓷 (@Bic_Revelatio）
- [研究 Vibe Coding 都能写论文了，来自中科院、杜克大学等的这篇《基于大语言模型的Vibe Coding综述》，还是花了点功夫把 V](https://x.com/dotey/status/1982640123440234754)（宝玉 (@dotey)）
- [Skills for Real Engineers Most AI agents can write code, but they are ](https://x.com/0xRoboAI/status/2091950919114178879)（Robo (@0xRoboAI)）

## P08 · 人工评审不可省 {#p08}

相关章节：[06](/handbook/06-review-collaboration)｜独立支持 **254**（X 193、HN 18、GitHub 22、精选 24）｜疑似异议 16｜人工确认的异议/限定 5

**代表性支持**：

- [AN04 · Create custom subagents](/sources/anthropic#an04)（Anthropic / Claude Code）
- [OA01 · Harness engineering: leveraging Codex in an agent-fir](/sources/openai#oa01)（OpenAI / Codex）
- [BT04 · Conductor Update: Introducing Automated Reviews](/sources/bigtech#bt04)（Google · Meta · GitHub）
- [VD01 · Best practices for coding with agents](/sources/vendors#vd01)（工具厂商）
- [TW01 · Harness engineering for coding agent users](/sources/thoughtworks#tw01)（Thoughtworks 技术雷达）
- [PR02 · Vibe engineering](/sources/practitioners#pr02)（独立工程师）
- [X02 · Karpathy：从 vibe coding 到 agentic engineering](/sources/x-posts#x02)（X 帖子（v1 精选））
- [X04 · Greg Brockman：OpenAI 如何让团队转向智能体式开发](/sources/x-posts#x04)（X 帖子（v1 精选））

**人工确认的异议 / 限定**：

- [Jarred Sumner：预计几个月内变成自动评审 + 新上下文判定 + 自动合并](/sources/x/review#xr-004)
- [Ado（Anthropic）：真实会话中人工评审只抓到 13.6% 的危险命令——人工评审单独不够](/sources/x/security#xs-006)
- [Uncle Bob：人工评审已成瓶颈，需要新的监督方式](/sources/x/review#xr-008)
- [宝玉：从 TL 转向 EM，代码不怎么细看，靠方案与验收把关](/sources/chinese#cn47)
- [HN 讨论：评审成为瓶颈且令人疲惫](/sources/hackernews#hn26)

**疑似异议样本（关键词命中，需人工复核）**：

- [Something I have been thinking about: in the past, the best engineers ](https://x.com/bcherny/status/2077460395279692197)（Boris Cherny (@bcherny)）
- [Google 正式开放 Gemini 4 Carbon：付费 API 今天可用，引入价到 11 月 30 日；普通用户要订 Ultra，每月](https://x.com/dotey/status/2120191790774960630)（宝玉 (@dotey)）
- [的资深工程师在生产中跑这套循环——2026 年的收敛形态是一个刻意无聊的闭环，而支撑它的几乎所有实践，都在管理同一个约束：上下文窗口。 《A](https://x.com/yibie/status/2086618951648424157)（yibie (@yibie)）
- [Here's my updated review of each personal agent: 1. Grok Bot Pros: A t](https://x.com/petergyang/status/2113042717270049028)（Peter Yang (@petergyang)）
- [I use Astra for a lot of video editing, here's how I do it: - I'm alwa](https://x.com/nickbaumann_/status/2108564021955743951)（Nick (@nickbaumann_)）
- [感觉能调好 Codex 的可以去当心理医生了，分享一段我给 GPT 6.1 Sol 配置的 AGENTS.md ，效果非常好hh “你是 C](https://x.com/Fei2411/status/2123017612741554208)（FeiZ (@Fei2411)）

## P09 · 小步、可回滚的变更 {#p09}

相关章节：[06](/handbook/06-review-collaboration)｜独立支持 **49**（X 42、HN 2、GitHub 1、精选 4）｜疑似异议 3｜人工确认的异议/限定 0

**代表性支持**：

- [AN19 · How the Claude Code team does code review](/sources/anthropic#an19)（Anthropic / Claude Code）
- [VD06 · Multi-Agents: What's Actually Working](/sources/vendors#vd06)（工具厂商）
- [TW06 · Understanding Spec-Driven-Development: Kiro, spec-kit](/sources/thoughtworks#tw06)（Thoughtworks 技术雷达）
- [PR14 · AI should help us produce better code](/sources/practitioners#pr14)（独立工程师）
- [Our tips on how to use Cursor: - Start with a plan (Shift+Ta](/sources/x/workflow#xw-005)（Michael Truell (@mntruell)）
- [很多人用 Claude Code，项目里却只有一个 CLAUDE.md。 真正可维护的配置，通常会拆成几层： 1、CLA](/sources/x/context#xc-016)（Vince 聊开发 (@vincemask)）
- [Claude Code is really amazingly cool with the sub-agents fea](/sources/x/tools#xt-001)（Jeffrey Emanuel (@doodlestein)）
- [The best projects are using more automated reviews, validati](/sources/x/review#xr-007)（Kyle Daigle (@kdaigle)）

**疑似异议样本（关键词命中，需人工复核）**：

- [的资深工程师在生产中跑这套循环——2026 年的收敛形态是一个刻意无聊的闭环，而支撑它的几乎所有实践，都在管理同一个约束：上下文窗口。 《A](https://x.com/yibie/status/2086618951648424157)（yibie (@yibie)）
- [Skills for Real Engineers Most AI agents can write code, but they are ](https://x.com/0xRoboAI/status/2091950919114178879)（Robo (@0xRoboAI)）

## P10 · 子智能体隔离上下文 {#p10}

相关章节：[07](/handbook/07-harness-tools)｜独立支持 **151**（X 112、HN 6、GitHub 25、精选 9）｜疑似异议 9｜人工确认的异议/限定 1

**代表性支持**：

- [AN04 · Create custom subagents](/sources/anthropic#an04)（Anthropic / Claude Code）
- [VD05 · Don’t Build Multi-Agents](/sources/vendors#vd05)（工具厂商）
- [TW05 · Context Engineering for Coding Agents](/sources/thoughtworks#tw05)（Thoughtworks 技术雷达）
- [X06 · Boris Cherny：让模型自主运行数小时到数天的五个建议](/sources/x-posts#x06)（X 帖子（v1 精选））
- [CN05 · Coding Agent 技术全景图：Context Engineering、Subagents 与 Ha](/sources/chinese#cn05)（InfoQ（编译 Birgitta Böckeler 在 Q）
- [CN11 · 使用 Claude Code：会话管理与 100 万上下文（宝玉译）](/sources/chinese#cn11)（Thariq（Anthropic）原文，宝玉翻译）
- [CN28 · Claude Code 作者再次分享 Anthropic 内部团队使用技巧](/sources/chinese#cn28)（Immerse（少数派作者））
- [OS07 · awesome-claude-code](/sources/open-source#os07)（开源项目与规范）

**人工确认的异议 / 限定**：

- [dex：子智能体自 2025 年中以来被过度使用和滥用](/sources/x/tools#xt-030)

**疑似异议样本（关键词命中，需人工复核）**：

- [Claude Code token 总是不够用？5 个实测省 token 技巧 每次看到 token 飙到 100k+ 的时候心都在滴血。实](https://x.com/shijianzhongg/status/2077566980719309178)（婷 (@shijianzhongg)）
- [的资深工程师在生产中跑这套循环——2026 年的收敛形态是一个刻意无聊的闭环，而支撑它的几乎所有实践，都在管理同一个约束：上下文窗口。 《A](https://x.com/yibie/status/2086618951648424157)（yibie (@yibie)）
- [Run tasks in parallel using sub-agents in Claude Code to eliminate con](https://x.com/nickytonline/status/1990939780335440381)（Nick Taylor (@nickytonline)）
- [if you want to improve how you use AI or your agentic systems, the one](https://x.com/stackbenchdev/status/2052002941884661792)（StackBench (@stackbenchdev)）
- [I've been using Claude Code for a few days for my iOS app, and it has ](https://x.com/JoshuaNewton/status/1940888060956377230)（Josh Newton (@JoshuaNewton)）
- [Anthropic 悄悄发布了一个官方插件，叫 claude-code-setup 这不是第三方工具，是 Anthropic 自己团队做的，](https://x.com/yaohui12138/status/2059819859345825923)（超级个体｜柿子 (@yaohui12138)）

## P11 · 并行智能体与隔离工作区 {#p11}

相关章节：[07](/handbook/07-harness-tools)｜独立支持 **209**（X 152、HN 12、GitHub 35、精选 10）｜疑似异议 14｜人工确认的异议/限定 3

**代表性支持**：

- [AN07 · Common workflows](/sources/anthropic#an07)（Anthropic / Claude Code）
- [OA01 · Harness engineering: leveraging Codex in an agent-fir](/sources/openai#oa01)（OpenAI / Codex）
- [BT06 · Agent Development Kit（ADK）文档](/sources/bigtech#bt06)（Google · Meta · GitHub）
- [VD05 · Don’t Build Multi-Agents](/sources/vendors#vd05)（工具厂商）
- [TW14 · How far can we push AI autonomy in code generation?](/sources/thoughtworks#tw14)（Thoughtworks 技术雷达）
- [PR03 · Embracing the parallel coding agent lifestyle](/sources/practitioners#pr03)（独立工程师）
- [CN28 · Claude Code 作者再次分享 Anthropic 内部团队使用技巧](/sources/chinese#cn28)（Immerse（少数派作者））
- [CN35 · 科技爱好者周刊（第 383 期）：你是第几级 AI 编程](/sources/chinese#cn35)（阮一峰）

**人工确认的异议 / 限定**：

- [「并行」不等于更好：共享状态缺失、Git 冲突、上下文污染](/sources/x/parallel#xa-006)
- [dex：并行不能替代深思熟虑的上下文管理](/sources/x/tools#xt-030)
- [腾讯 LoopForge：前置需求澄清门禁比加并发更有效](/sources/chinese#cn21)

**疑似异议样本（关键词命中，需人工复核）**：

- [I had the same thought so I've been playing with it in nanochat. E.g. ](https://x.com/karpathy/status/2027521323275325622)（Andrej Karpathy (@karpathy)）
- [Google 正式开放 Gemini 4 Carbon：付费 API 今天可用，引入价到 11 月 30 日；普通用户要订 Ultra，每月](https://x.com/dotey/status/2120191790774960630)（宝玉 (@dotey)）
- [At @vercel we got to test this model before release. Best way to summa](https://x.com/rauchg/status/2119878364794372162)（Guillermo Rauch (@rauchg)）
- [Claude Code token 总是不够用？5 个实测省 token 技巧 每次看到 token 飙到 100k+ 的时候心都在滴血。实](https://x.com/shijianzhongg/status/2077566980719309178)（婷 (@shijianzhongg)）
- [的资深工程师在生产中跑这套循环——2026 年的收敛形态是一个刻意无聊的闭环，而支撑它的几乎所有实践，都在管理同一个约束：上下文窗口。 《A](https://x.com/yibie/status/2086618951648424157)（yibie (@yibie)）
- [Run tasks in parallel using sub-agents in Claude Code to eliminate con](https://x.com/nickytonline/status/1990939780335440381)（Nick Taylor (@nickytonline)）

## P12 · Hooks 提供确定性保障 {#p12}

相关章节：[07](/handbook/07-harness-tools)｜独立支持 **164**（X 115、HN 2、GitHub 34、精选 14）｜疑似异议 5｜人工确认的异议/限定 0

**代表性支持**：

- [AN01 · Best practices for Claude Code](/sources/anthropic#an01)（Anthropic / Claude Code）
- [BT10 · Automated Unit Test Improvement using LLMs at Meta（Te](/sources/bigtech#bt10)（Google · Meta · GitHub）
- [VD01 · Best practices for coding with agents](/sources/vendors#vd01)（工具厂商）
- [TW01 · Harness engineering for coding agent users](/sources/thoughtworks#tw01)（Thoughtworks 技术雷达）
- [PR30 · Basic Claude Code](/sources/practitioners#pr30)（独立工程师）
- [X10 · dex：「harness engineering」一词的提出](/sources/x-posts#x10)（X 帖子（v1 精选））
- [CN03 · AI Coding 的下一步不是写得更快，而是可验收：蚂蚁数科 Harness 工程实践](/sources/chinese#cn03)（InfoQ（整理蚂蚁数字科技魏长征 AICon 演讲））
- [CN21 · 从“能写代码”到“能交付”：腾讯轻量云 LoopForge 云端 Loop 实践（AICon 北京议题）](/sources/chinese#cn21)（AICon（腾讯轻量云团队议题））

**疑似异议样本（关键词命中，需人工复核）**：

- [的资深工程师在生产中跑这套循环——2026 年的收敛形态是一个刻意无聊的闭环，而支撑它的几乎所有实践，都在管理同一个约束：上下文窗口。 《A](https://x.com/yibie/status/2086618951648424157)（yibie (@yibie)）
- [if you want to improve how you use AI or your agentic systems, the one](https://x.com/stackbenchdev/status/2052002941884661792)（StackBench (@stackbenchdev)）
- [Anthropic 悄悄发布了一个官方插件，叫 claude-code-setup 这不是第三方工具，是 Anthropic 自己团队做的，](https://x.com/yaohui12138/status/2059819859345825923)（超级个体｜柿子 (@yaohui12138)）
- [What if your AI coding agent could find a bug, fix it, test the soluti](https://x.com/Bic_Revelation/status/2112940728154292705)（𝓑𝓲𝓬_𝓡𝓮𝓿𝓮𝓵𝓪𝓽𝓲𝓸𝓷 (@Bic_Revelatio）

## P13 · Skills 等可复用指令按需加载 {#p13}

相关章节：[07](/handbook/07-harness-tools)｜独立支持 **355**（X 196、HN 20、GitHub 121、精选 19）｜疑似异议 15｜人工确认的异议/限定 5

**代表性支持**：

- [AN01 · Best practices for Claude Code](/sources/anthropic#an01)（Anthropic / Claude Code）
- [OA04 · Codex Best practices](/sources/openai#oa04)（OpenAI / Codex）
- [VD01 · Best practices for coding with agents](/sources/vendors#vd01)（工具厂商）
- [TW05 · Context Engineering for Coding Agents](/sources/thoughtworks#tw05)（Thoughtworks 技术雷达）
- [PR06 · Claude Skills are awesome, maybe a bigger deal than M](/sources/practitioners#pr06)（独立工程师）
- [X04 · Greg Brockman：OpenAI 如何让团队转向智能体式开发](/sources/x-posts#x04)（X 帖子（v1 精选））
- [X10 · dex：「harness engineering」一词的提出](/sources/x-posts#x10)（X 帖子（v1 精选））
- [CN06 · AI Coding 增量风险管控：Skill 门禁与 Harness 落地实践（快手，会议预告）](/sources/chinese#cn06)（InfoQ / AICon 北京（快手架构治理团队演讲预告））

**人工确认的异议 / 限定**：

- [Thorsten Ball：由人按序手动调用的 skill「金字塔」是反模式](/sources/x/tools#xt-042)
- [Dirk Kok：删除所有 skills、精简 agents.md 后工作流更好](/sources/x/context#xc-024)
- [Every：新模型在旧 skills 下表现变差，删掉重来更好](/sources/x/context#xc-021)
- [Burke Holland：99% 的 MCP、功能和 skill 都是噪声](/sources/x/tools#xt-019)
- [Vercel 评测：AGENTS.md 胜过 skills（多数情况下 skill 未被调用）](/sources/hackernews#hn15)

**疑似异议样本（关键词命中，需人工复核）**：

- [I had the same thought so I've been playing with it in nanochat. E.g. ](https://x.com/karpathy/status/2027521323275325622)（Andrej Karpathy (@karpathy)）
- [Something I have been thinking about: in the past, the best engineers ](https://x.com/bcherny/status/2077460395279692197)（Boris Cherny (@bcherny)）
- [这期用皮影戏讲清 BaoCut 虚拟主播的工作原理： - 拆：AI 画一张正面像，再改十一次，程序逐像素比对，拆出二十七层 - 动：给整张画](https://x.com/dotey/status/2120208679005810803)（宝玉 (@dotey)）
- [At @vercel we got to test this model before release. Best way to summa](https://x.com/rauchg/status/2119878364794372162)（Guillermo Rauch (@rauchg)）
- [的资深工程师在生产中跑这套循环——2026 年的收敛形态是一个刻意无聊的闭环，而支撑它的几乎所有实践，都在管理同一个约束：上下文窗口。 《A](https://x.com/yibie/status/2086618951648424157)（yibie (@yibie)）
- [claude-opus-5.5 写前端真是又找回当年的感觉了啊 趁着假期休息把之前 vibe coding 的各种小工具升级了一波, 各种屎](https://x.com/karminski3/status/2107652131662774721)（karminski-牙医 (@karminski3)）

## P14 · 工具与 MCP 要精简 {#p14}

相关章节：[07](/handbook/07-harness-tools)｜独立支持 **304**（X 127、HN 115、GitHub 50、精选 14）｜疑似异议 7｜人工确认的异议/限定 0

**代表性支持**：

- [AN03 · Automate actions with hooks](/sources/anthropic#an03)（Anthropic / Claude Code）
- [OA02 · Unrolling the Codex agent loop](/sources/openai#oa02)（OpenAI / Codex）
- [BT01 · Gemini CLI（开源仓库）](/sources/bigtech#bt01)（Google · Meta · GitHub）
- [VD13 · Context Management in Amp](/sources/vendors#vd13)（工具厂商）
- [TW05 · Context Engineering for Coding Agents](/sources/thoughtworks#tw05)（Thoughtworks 技术雷达）
- [PR06 · Claude Skills are awesome, maybe a bigger deal than M](/sources/practitioners#pr06)（独立工程师）
- [X04 · Greg Brockman：OpenAI 如何让团队转向智能体式开发](/sources/x-posts#x04)（X 帖子（v1 精选））
- [X06 · Boris Cherny：让模型自主运行数小时到数天的五个建议](/sources/x-posts#x06)（X 帖子（v1 精选））

**疑似异议样本（关键词命中，需人工复核）**：

- [Software horror: litellm PyPI supply chain attack. Simple 'pip install](https://x.com/karpathy/status/2036487306585268612)（Andrej Karpathy (@karpathy)）
- [Claude Code token 总是不够用？5 个实测省 token 技巧 每次看到 token 飙到 100k+ 的时候心都在滴血。实](https://x.com/shijianzhongg/status/2077566980719309178)（婷 (@shijianzhongg)）
- [Your life will get a lot easier when you realize that 99% of every MCP](https://x.com/burkeholland/status/2065134777162670585)（Burke Holland (@burkeholland)）
- [dropping every hot keyword in one post: kimi, claude code, codex, gpt ](https://x.com/raf_piek/status/2080018079363355039)（Rafał Piekara (@raf_piek)）
- [Anthropic 悄悄发布了一个官方插件，叫 claude-code-setup 这不是第三方工具，是 Anthropic 自己团队做的，](https://x.com/yaohui12138/status/2059819859345825923)（超级个体｜柿子 (@yaohui12138)）
- [Simon Willison 对「Claude Code sub-agents」的分析和评价，还有一个典型案例，在用 Claude Code](https://x.com/shao__meng/status/1977319498790412368)（meng shao (@shao__meng)）

## P15 · 最小权限与沙箱 {#p15}

相关章节：[09](/handbook/09-security)｜独立支持 **179**（X 119、HN 17、GitHub 28、精选 16）｜疑似异议 9｜人工确认的异议/限定 1

**代表性支持**：

- [AN04 · Create custom subagents](/sources/anthropic#an04)（Anthropic / Claude Code）
- [OA04 · Codex Best practices](/sources/openai#oa04)（OpenAI / Codex）
- [BT01 · Gemini CLI（开源仓库）](/sources/bigtech#bt01)（Google · Meta · GitHub）
- [VD03 · Scaling long-running autonomous coding](/sources/vendors#vd03)（工具厂商）
- [TW11 · The role of developer skills in agentic coding](/sources/thoughtworks#tw11)（Thoughtworks 技术雷达）
- [PR26 · The 70% problem: Hard truths about AI-assisted coding](/sources/practitioners#pr26)（独立工程师）
- [X06 · Boris Cherny：让模型自主运行数小时到数天的五个建议](/sources/x-posts#x06)（X 帖子（v1 精选））
- [CN10 · Qoder 详解 Spec 驱动的 AI 自主编程新范式（云栖大会演讲实录）](/sources/chinese#cn10)（阿里云开发者社区）

**人工确认的异议 / 限定**：

- [Boris Cherny：头号建议是 auto mode（用分类器代替逐条批准）——对「逐条人工确认」的修正](/sources/x/parallel#xa-012)

**疑似异议样本（关键词命中，需人工复核）**：

- [Software horror: litellm PyPI supply chain attack. Simple 'pip install](https://x.com/karpathy/status/2036487306585268612)（Andrej Karpathy (@karpathy)）
- [Google 正式开放 Gemini 4 Carbon：付费 API 今天可用，引入价到 11 月 30 日；普通用户要订 Ultra，每月](https://x.com/dotey/status/2120191790774960630)（宝玉 (@dotey)）
- [At @vercel we got to test this model before release. Best way to summa](https://x.com/rauchg/status/2119878364794372162)（Guillermo Rauch (@rauchg)）
- [的资深工程师在生产中跑这套循环——2026 年的收敛形态是一个刻意无聊的闭环，而支撑它的几乎所有实践，都在管理同一个约束：上下文窗口。 《A](https://x.com/yibie/status/2086618951648424157)（yibie (@yibie)）
- [程序员需要逐渐接受一个现实，未来很多编程工作会变成黑盒编程。 我们团队有不少系统是用 Rust 写的，但真正精通 Rust 的人并不多。有些](https://x.com/Barret_China/status/2123058891869098232)（Barret李靖 (@Barret_China)）
- [人类最强模型 Claude Fable 5.2 和 Mythos 5.2 发布。 几乎所有能力都超过了 Opus 5.5 。 这是人类目前最](https://x.com/oran_ge/status/2119933301767180631)（Orange AI (@oran_ge)）

## P16 · 人要理解并为代码负责 {#p16}

相关章节：[01](/handbook/01-mental-model)｜独立支持 **190**（X 103、HN 75、GitHub 5、精选 8）｜疑似异议 8｜人工确认的异议/限定 2

**代表性支持**：

- [VD03 · Scaling long-running autonomous coding](/sources/vendors#vd03)（工具厂商）
- [TW01 · Harness engineering for coding agent users](/sources/thoughtworks#tw01)（Thoughtworks 技术雷达）
- [PR02 · Vibe engineering](/sources/practitioners#pr02)（独立工程师）
- [X02 · Karpathy：从 vibe coding 到 agentic engineering](/sources/x-posts#x02)（X 帖子（v1 精选））
- [X04 · Greg Brockman：OpenAI 如何让团队转向智能体式开发](/sources/x-posts#x04)（X 帖子（v1 精选））
- [CN24 · 美团企业级 Agent 的平台化应用实践（QCon 上海议题）](/sources/chinese#cn24)（QCon（美团 Agent 平台议题））
- [CN36 · 从个人提效到组织生产力提升：快手 AI Coding 演进实践（AICon 上海议题）](/sources/chinese#cn36)（AICon（快手 AI Coding 负责人议题））
- [After two years of vibecoding, I'm back to writing by hand](/sources/hackernews#hn04)（atmoio.substack.com（提交者 mobita）

**人工确认的异议 / 限定**：

- [Steve Yegge（阮一峰转述）：22.5 万行代码从没看过，也不打算看](/sources/chinese#cn35)
- [宝玉：个人项目中代码不怎么细看](/sources/chinese#cn47)

**疑似异议样本（关键词命中，需人工复核）**：

- [Software horror: litellm PyPI supply chain attack. Simple 'pip install](https://x.com/karpathy/status/2036487306585268612)（Andrej Karpathy (@karpathy)）
- [的资深工程师在生产中跑这套循环——2026 年的收敛形态是一个刻意无聊的闭环，而支撑它的几乎所有实践，都在管理同一个约束：上下文窗口。 《A](https://x.com/yibie/status/2086618951648424157)（yibie (@yibie)）
- [claude-opus-5.5 写前端真是又找回当年的感觉了啊 趁着假期休息把之前 vibe coding 的各种小工具升级了一波, 各种屎](https://x.com/karminski3/status/2107652131662774721)（karminski-牙医 (@karminski3)）
- [dropping every hot keyword in one post: kimi, claude code, codex, gpt ](https://x.com/raf_piek/status/2080018079363355039)（Rafał Piekara (@raf_piek)）
- [context-engineering：上下文工程替代vibe coding成为新的AI潮流，提示词工程师逐步退出历史舞台，可转为上下文工程](https://x.com/aigclink/status/1942374295910638039)（AIGCLINK (@aigclink)）
- [What if your AI coding agent could find a bug, fix it, test the soluti](https://x.com/Bic_Revelation/status/2112940728154292705)（𝓑𝓲𝓬_𝓡𝓮𝓿𝓮𝓵𝓪𝓽𝓲𝓸𝓷 (@Bic_Revelatio）

## P17 · 成本与 token 意识 {#p17}

相关章节：[08](/handbook/08-team-process)｜独立支持 **167**（X 119、HN 31、GitHub 10、精选 8）｜疑似异议 9｜人工确认的异议/限定 0

**代表性支持**：

- [AN22 · Using Claude Code: Spending your effort](/sources/anthropic#an22)（Anthropic / Claude Code）
- [VD04 · Improved token efficiency for longer agent runs](/sources/vendors#vd04)（工具厂商）
- [TW03 · Maintainability sensors for coding agents](/sources/thoughtworks#tw03)（Thoughtworks 技术雷达）
- [PR14 · AI should help us produce better code](/sources/practitioners#pr14)（独立工程师）
- [X01 · Karpathy：+1 for "context engineering"](/sources/x-posts#x01)（X 帖子（v1 精选））
- [CN25 · Trae Agent 架构演进：从 Workflow 到 Agentic Loop（QCon 上海议题）](/sources/chinese#cn25)（QCon（字节跳动 Trae 议题））
- [CN44 · 当国产模型追上闭源旗舰，企业 AI 编程的真正障碍才浮出水面](/sources/chinese#cn44)（InfoQ（周云龙、蔡芳芳））
- [RS06 · Evaluating AGENTS.md: Are Repository-Level Context Fi](/sources/research#rs06)（研究与数据）

**疑似异议样本（关键词命中，需人工复核）**：

- [Cool chart showing the ratio of Tab complete requests to Agent request](https://x.com/karpathy/status/2027501331125239822)（Andrej Karpathy (@karpathy)）
- [Google 正式开放 Gemini 4 Carbon：付费 API 今天可用，引入价到 11 月 30 日；普通用户要订 Ultra，每月](https://x.com/dotey/status/2120191790774960630)（宝玉 (@dotey)）
- [Claude Code token 总是不够用？5 个实测省 token 技巧 每次看到 token 飙到 100k+ 的时候心都在滴血。实](https://x.com/shijianzhongg/status/2077566980719309178)（婷 (@shijianzhongg)）
- [的资深工程师在生产中跑这套循环——2026 年的收敛形态是一个刻意无聊的闭环，而支撑它的几乎所有实践，都在管理同一个约束：上下文窗口。 《A](https://x.com/yibie/status/2086618951648424157)（yibie (@yibie)）
- [I use Astra for a lot of video editing, here's how I do it: - I'm alwa](https://x.com/nickbaumann_/status/2108564021955743951)（Nick (@nickbaumann_)）
- [人类最强模型 Claude Fable 5.2 和 Mythos 5.2 发布。 几乎所有能力都超过了 Opus 5.5 。 这是人类目前最](https://x.com/oran_ge/status/2119933301767180631)（Orange AI (@oran_ge)）

## P18 · 长任务靠外部状态与进度文件 {#p18}

相关章节：[07](/handbook/07-harness-tools)｜独立支持 **171**（X 123、HN 11、GitHub 29、精选 8）｜疑似异议 3｜人工确认的异议/限定 0

**代表性支持**：

- [AN02 · How Claude remembers your project（CLAUDE.md 与记忆）](/sources/anthropic#an02)（Anthropic / Claude Code）
- [OA06 · Run long horizon tasks with Codex](/sources/openai#oa06)（OpenAI / Codex）
- [BT02 · Provide context with GEMINI.md files](/sources/bigtech#bt02)（Google · Meta · GitHub）
- [VD03 · Scaling long-running autonomous coding](/sources/vendors#vd03)（工具厂商）
- [TW01 · Harness engineering for coding agent users](/sources/thoughtworks#tw01)（Thoughtworks 技术雷达）
- [PR25 · Beads：a memory upgrade for your coding agent](/sources/practitioners#pr25)（独立工程师）
- [CN25 · Trae Agent 架构演进：从 Workflow 到 Agentic Loop（QCon 上海议题）](/sources/chinese#cn25)（QCon（字节跳动 Trae 议题））
- [CN30 · Claude 如何记住您的项目（中文官方文档）](/sources/chinese#cn30)（Anthropic（官方文档中文版））

**疑似异议样本（关键词命中，需人工复核）**：

- [Google 正式开放 Gemini 4 Carbon：付费 API 今天可用，引入价到 11 月 30 日；普通用户要订 Ultra，每月](https://x.com/dotey/status/2120191790774960630)（宝玉 (@dotey)）
- [At @vercel we got to test this model before release. Best way to summa](https://x.com/rauchg/status/2119878364794372162)（Guillermo Rauch (@rauchg)）
- [的资深工程师在生产中跑这套循环——2026 年的收敛形态是一个刻意无聊的闭环，而支撑它的几乎所有实践，都在管理同一个约束：上下文窗口。 《A](https://x.com/yibie/status/2086618951648424157)（yibie (@yibie)）

## P19 · 把错误沉淀为规则（复利） {#p19}

相关章节：[08](/handbook/08-team-process)｜独立支持 **52**（X 40、HN 0、GitHub 1、精选 11）｜疑似异议 4｜人工确认的异议/限定 1

**代表性支持**：

- [AN32 · An update on recent Claude Code quality reports](/sources/anthropic#an32)（Anthropic / Claude Code）
- [PR14 · AI should help us produce better code](/sources/practitioners#pr14)（独立工程师）
- [CN03 · AI Coding 的下一步不是写得更快，而是可验收：蚂蚁数科 Harness 工程实践](/sources/chinese#cn03)（InfoQ（整理蚂蚁数字科技魏长征 AICon 演讲））
- [CN06 · AI Coding 增量风险管控：Skill 门禁与 Harness 落地实践（快手，会议预告）](/sources/chinese#cn06)（InfoQ / AICon 北京（快手架构治理团队演讲预告））
- [CN19 · 从提需求到部署发布，全AI全自动化后，研发效能全面跃升](/sources/chinese#cn19)（腾讯技术工程）
- [CN20 · 当 Coding Agent 走进研发团队：我们开源了云端自进化研发平台 LoopForge](/sources/chinese#cn20)（腾讯云开发者（腾讯轻量云团队））
- [CN23 · 从代码生成到可信交付：美团 AIDE 数据研发 Agent 实践（QCon 上海议题）](/sources/chinese#cn23)（QCon（美团数据平台议题））
- [CN33 · 智能体工程的 8 个等级（宝玉译）](/sources/chinese#cn33)（Bassim Eledath 原文，宝玉翻译）

**人工确认的异议 / 限定**：

- [Every：旧 skills 在新模型下成了负担——沉淀下来的规则也要定期删减](/sources/x/context#xc-021)

**疑似异议样本（关键词命中，需人工复核）**：

- [Anthropic 发了新模型，OpenAI 发了台游戏机：Codex 版 Chromatic 掌机开卖，200 美元，用 Codex 自己](https://x.com/dotey/status/2119873970920997274)（宝玉 (@dotey)）
- [的资深工程师在生产中跑这套循环——2026 年的收敛形态是一个刻意无聊的闭环，而支撑它的几乎所有实践，都在管理同一个约束：上下文窗口。 《A](https://x.com/yibie/status/2086618951648424157)（yibie (@yibie)）
- [claude-opus-5.5 写前端真是又找回当年的感觉了啊 趁着假期休息把之前 vibe coding 的各种小工具升级了一波, 各种屎](https://x.com/karminski3/status/2107652131662774721)（karminski-牙医 (@karminski3)）

## P20 · 选主流、无聊的技术栈 {#p20}

相关章节：[04](/handbook/04-architecture-constraints)｜独立支持 **5**（X 5、HN 0、GitHub 0、精选 0）｜疑似异议 0｜人工确认的异议/限定 0

**代表性支持**：

- [anthropic built their own git. Most interesting mental shift](/sources/x/team#xm-013)（dex (@dexhorthy)）

