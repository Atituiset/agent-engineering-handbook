# Hacker News 高热讨论

> 29 个高互动讨论串，通过 HN Algolia 搜索 API 检索（2025 年以来、分数较高），再用 HN 官方 Firebase API 读取评论；评论观点取自 HN 默认排序靠前的顶层评论，只做忠实转述。每条都给出讨论串链接与原文链接；引文为评论原句。日期按北京时间（UTC+8）。评论区是个人观点，代表性有限。

[[toc]]

### HN01 · 「我如何用 Claude Code：规划与执行分离」讨论 {#hn01}
**讨论**：[news.ycombinator.com/item?id=47106686](https://news.ycombinator.com/item?id=47106686)（976 分，591 条评论）｜**原文**：[How I use Claude Code: Separation of planning and execution](https://boristane.com/blog/how-i-use-claude-code/)｜**日期**：2026-02-22

文章作者主张先让 Claude 深入阅读代码、写出计划，人在计划里批注后再执行。评论区普遍认可「先计划」，但对原因和粒度有不同看法。

**评论区观点**：

- 真正的价值不在「计划与否」，而在逼模型在假设固化成代码之前把它们暴露出来；书面计划成了排查这些隐形假设的界面。（[评论](https://news.ycombinator.com/item?id=47110595)，sparin9）
- 有人用更重的文档体系：静态的规格文件（约每 1 万行代码配 1 千行规格，单个文件不超过 300 行）加两个 skill。（[评论](https://news.ycombinator.com/item?id=47107286)，brandall10）
- 反对「一次性写完」：更好的做法是把计划拆成可逐个完成的技术步骤，一步步推进。（[评论](https://news.ycombinator.com/item?id=47107999)，zmmmmm）
- 也有人质疑文中「用 deeply、in great details 等词防止模型略读」的说法不符合自己对 LLM 的理解。（[评论](https://news.ycombinator.com/item?id=47107091)，haolez）

> "A written plan becomes a debugging surface for those assumptions." —— [评论](https://news.ycombinator.com/item?id=47110595)

### HN02 · 「How I program with LLMs」（Tailscale 联合创始人 crawshaw）讨论 {#hn02}
**讨论**：[news.ycombinator.com/item?id=42617645](https://news.ycombinator.com/item?id=42617645)（919 分，332 条评论）｜**原文**：[How I program with LLMs](https://crawshaw.io/blog/programming-with-llms)｜**日期**：2025-01-07

David Crawshaw 介绍自己如何用 LLM 编程，包括对话式编程生成初稿。评论区围绕「什么人、什么任务适合用 LLM」展开。

**评论区观点**：

- 有人指出作者本身是顶尖工程师，他说 LLM 能提高自己的效率（尤其是新想法的初稿）很有说服力。（[评论](https://news.ycombinator.com/item?id=42619022)，dewitt）
- 一条高赞经验：别用 LLM 做你自己不会做的事——只有你能一眼看出方案哪里错时，它才真正省时间。（[评论](https://news.ycombinator.com/item?id=42618364)，mlepath）
- 也有人说自己无法认同对话式编程，主要把 LLM 当自动补全和搜索，让它代做常常是在浪费时间。（[评论](https://news.ycombinator.com/item?id=42618781)，nemothekid）

> "The first rule of programming with LLMs is don't use them for anything you don't know how to do." —— [评论](https://news.ycombinator.com/item?id=42618364)

### HN03 · 「AI 的新技能不是提示词，而是上下文工程」讨论 {#hn03}
**讨论**：[news.ycombinator.com/item?id=44427757](https://news.ycombinator.com/item?id=44427757)（915 分，518 条评论）｜**原文**：[The new skill in AI is not prompting, it's context engineering](https://www.philschmid.de/context-engineering)｜**日期**：2025-07-01

Philipp Schmid 的文章提出「上下文工程」：在正确的时间、以正确的格式提供正确的信息和工具。评论区既有补充，也有质疑。

**评论区观点**：

- Simon Willison 推荐 Drew Breunig 关于长上下文如何失效的系列文章。（[评论](https://news.ycombinator.com/item?id=44428044)，simonw）
- 质疑：如果「正确的格式」「正确的时间」本身无法定义，这和寻找「魔法提示词」有什么区别？（[评论](https://news.ycombinator.com/item?id=44428090)，JohnMakin）
- 另一种观点：新技能仍然是编程，理解 LLM 的方式是写程序去训练、运行和分析它们。（[评论](https://news.ycombinator.com/item?id=44429043)，benreesman）

> "aren't you still reaching for a "magic" solution?" —— [评论](https://news.ycombinator.com/item?id=44428090)

### HN04 · 「vibe coding 两年后，我回到手写代码」讨论 {#hn04}
**讨论**：[news.ycombinator.com/item?id=46765460](https://news.ycombinator.com/item?id=46765460)（865 分，634 条评论）｜**原文**：[After two years of vibecoding, I'm back to writing by hand](https://atmoio.substack.com/p/after-two-years-of-vibecoding-im)｜**日期**：2026-01-26

作者认为智能体写出的改动单独看都不错，却不尊重整体结构和相邻模式，于是回到手写。评论区分为三类意见。

**评论区观点**：

- 一位计算机教师警告：AI 能把简单的事做得很好，反而让新手学不会这些简单的事，进而学不会更难的；他要求学生必须亲手写代码。（[评论](https://news.ycombinator.com/item?id=46765774)，recursivedoubts）
- Simon Willison 反驳「智能体无法在数周内演化规格」：那是你的工作，你可以随时告诉智能体改设计。（[评论](https://news.ycombinator.com/item?id=46765780)，simonw）
- 有人认为可以防范结构失控：理解自己的代码库并查看 LLM 的输出。（[评论](https://news.ycombinator.com/item?id=46765728)，mettamage）
- 有人认同：它适合繁琐但对错容易检查的代码，测试只有在代码结构良好时才有帮助。（[评论](https://news.ycombinator.com/item?id=46766259)，rich_sasha）

> "That's your job." —— [评论](https://news.ycombinator.com/item?id=46765780)

### HN05 · 「Supabase MCP 可能泄露整个 SQL 数据库」讨论 {#hn05}
**讨论**：[news.ycombinator.com/item?id=44502318](https://news.ycombinator.com/item?id=44502318)（848 分，470 条评论）｜**原文**：[Supabase MCP can leak your entire SQL database](https://www.generalanalysis.com/blog/supabase-mcp-blog)｜**日期**：2025-07-09

安全研究文章演示：通过用户数据中的提示注入，让接入 Supabase MCP 的智能体泄露数据库。评论区集中在缓解措施和问题本质。

**评论区观点**：

- Supabase 工程师介绍已加的缓解：文档默认推荐只读；把 SQL 返回结果包上抑制执行注入指令的提示；写 E2E 测试验证较弱的模型也不会中招。（[评论](https://news.ycombinator.com/item?id=44503146)，gregnr）
- tptacek：这就是映射到 LLM 上的 XSS——内部工具直接接收不可信的用户内容。（[评论](https://news.ycombinator.com/item?id=44503091)，tptacek）
- Simon Willison 建议：数据库 MCP 设为只读；并非常小心与其他能对外通信的 MCP（发 HTTP、发邮件）组合使用。（[评论](https://news.ycombinator.com/item?id=44502730)，simonw）
- 问题不在 MCP 本身，而在把未经审查的用户内容直接注入提示；任何智能体都有这个限制，MCP 只是把它放大。（[评论](https://news.ycombinator.com/item?id=44505852)，dante1441）

> "Configure it to be read-only." —— [评论](https://news.ycombinator.com/item?id=44502730)

### HN06 · 「AGENTS.md：指导编码智能体的开放格式」讨论 {#hn06}
**讨论**：[news.ycombinator.com/item?id=44957443](https://news.ycombinator.com/item?id=44957443)（837 分，382 条评论）｜**原文**：[AGENTS.md – Open format for guiding coding agents](https://agents.md/)｜**日期**：2025-08-20

AGENTS.md 作为跨工具的智能体说明文件格式发布。评论区对它的形态和必要性有分歧。

**评论区观点**：

- 建议改成 .agents 目录加 index.md，复杂项目可以用「刚好够用的层级」组织。（[评论](https://news.ycombinator.com/item?id=44957726)，CharlesW）
- 认为这是过渡期：智能体很快不再需要特殊指导，应把内容写进面向人的项目文档。（[评论](https://news.ycombinator.com/item?id=44957594)，blinkymach12）
- 调侃：AGENTS.md 就是有了足够热度、让人愿意认真填写的 README——人们懒得为人写文档，却愿意为机器人写。（[评论](https://news.ycombinator.com/item?id=44957647)，spawarotti）

> "People were too lazy to write docs for other people, but funnily enough are ok with doing it for robots." —— [评论](https://news.ycombinator.com/item?id=44957647)

### HN07 · 「一个下午提升 15 个 LLM 的编码表现，只改了 harness」讨论 {#hn07}
**讨论**：[news.ycombinator.com/item?id=46988596](https://news.ycombinator.com/item?id=46988596)（832 分，295 条评论）｜**原文**：[Improving 15 LLMs at Coding in One Afternoon. Only the Harness Changed](http://blog.can.ac/2026/02/12/the-harness-problem/)｜**日期**：2026-02-12

作者称只改变编辑格式等 harness 设计，就让多个模型在其基准上提升，并认为 harness 被严重低估。评论区认同方向，但也有人认为结论被夸大。

**评论区观点**：

- 赞同：harness 设计中有大量低垂的果实，在边际收益递减之前，影响可能不亚于训练新模型。（[评论](https://news.ycombinator.com/item?id=46990271)，logicprog）
- 质疑：这只是作者自建的查找替换基准上约 5% 的提升，表述被过度夸大。（[评论](https://news.ycombinator.com/item?id=46993694)，woah）
- 有人说早期模型只要「握对姿势」也能得到准确结果，未兑现的收益在于构建合适的工具、harness 和护栏。（[评论](https://news.ycombinator.com/item?id=46995411)，keeda）

> "Seems like a very cool technique, but also very oversold." —— [评论](https://news.ycombinator.com/item?id=46993694)

### HN08 · 「铲件软件在哪？为什么 AI 编码的说法对不上」讨论 {#hn08}
**讨论**：[news.ycombinator.com/item?id=45120517](https://news.ycombinator.com/item?id=45120517)（770 分，482 条评论）｜**原文**：[Where's the shovelware? Why AI coding claims don't add up](https://mikelovesrobots.substack.com/p/wheres-the-shovelware-why-ai-coding)｜**日期**：2025-09-04

作者质疑：如果 AI 让开发效率大增，为什么没有看到软件发布数量的明显增长。评论区多数认同需要更审慎地看待效率宣传。

**评论区观点**：

- 多件事可以同时为真：LLM 不会让随机任务效率普遍提升 10 倍，但能显著提升部分任务，也能在后台完成杂活。（[评论](https://news.ycombinator.com/item?id=45120881)，com2kid）
- 经验：对小重构、按 schema 生成类型等有用，更大的任务会遗漏并需要返工；还见到经验不足的工程师照单全收。（[评论](https://news.ycombinator.com/item?id=45120896)，captainkrtek）
- 担心不练习解决问题与判断的能力会导致技能萎缩。（[评论](https://news.ycombinator.com/item?id=45120925)，jryio）

> "Multiple things can be true at the same time" —— [评论](https://news.ycombinator.com/item?id=45120881)

### HN09 · 「vibe code 就是遗留代码」讨论 {#hn09}
**讨论**：[news.ycombinator.com/item?id=44739556](https://news.ycombinator.com/item?id=44739556)（758 分，454 条评论）｜**原文**：[Vibe code is legacy code](https://blog.val.town/vibe-code)｜**日期**：2025-07-31

Val Town 的文章认为没人理解的 vibe coding 产物本质上就是遗留代码。评论区既有共鸣也有反驳。

**评论区观点**：

- 历史类比：当年非技术人员用 Access 和 Excel 开发应用，也带来扩展和维护噩梦，但同样有好处。（[评论](https://news.ycombinator.com/item?id=44740134)，tux1968）
- 反驳：所有代码都是遗留代码，对 LLM 代码的批评同样适用于大量初级工程师写的生产代码。（[评论](https://news.ycombinator.com/item?id=44740693)，apimade）
- 「代码即数学」的时代已经过去，大型系统靠形式保证、设计原则、实验测试和经验法则共同支撑。（[评论](https://news.ycombinator.com/item?id=44740192)，extr）

> "All code is legacy code." —— [评论](https://news.ycombinator.com/item?id=44740693)

### HN10 · 「写好 Claude.md」（HumanLayer）讨论 {#hn10}
**讨论**：[news.ycombinator.com/item?id=46098838](https://news.ycombinator.com/item?id=46098838)（748 分，290 条评论）｜**原文**：[Writing a good Claude.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)｜**日期**：2025-12-01

HumanLayer 的文章建议 CLAUDE.md 只放普遍适用的内容，把任务相关的说明拆到单独文件，由 Claude 按需读取。评论区对「要不要为智能体写这么多」意见分化。

**评论区观点**：

- 引用文中观点：文件里与当前任务无关的信息越多，Claude 越可能忽略其中的指令；很多人发现 CLAUDE.md 一长，Claude 就不再遵循许多条目。（[评论](https://news.ycombinator.com/item?id=46102048)，nico）
- 有人说从一开始就用文中推荐的做法：把任务说明放在命名清晰的单独文件里，CLAUDE.md 只列清单并让 Claude 自己判断读哪些。（[评论](https://news.ycombinator.com/item?id=46100616)，vunderba）
- 另一种思路：好好写代码注释和各目录的 README，它们本身就是按需加载的上下文。（[评论](https://news.ycombinator.com/item?id=46100185)，_pdp_）
- 有人发现在难题上，更多上下文和注释反而会降低质量，因此只给模型不含注释的代码视图。（[评论](https://news.ycombinator.com/item?id=46100884)，johnsmith1840）
- 也有人认为如果为 AI 搭基础设施、给它做入职要花这么大力气，不如自己写。（[评论](https://news.ycombinator.com/item?id=46100308)，gonzalohm）

> "then I might as well code the damn thing myself" —— [评论](https://news.ycombinator.com/item?id=46100308)

### HN11 · 「Cursor 的浏览器实验在没有证据的情况下暗示成功」讨论 {#hn11}
**讨论**：[news.ycombinator.com/item?id=46646777](https://news.ycombinator.com/item?id=46646777)（724 分，309 条评论）｜**原文**：[Cursor's latest “browser experiment” implied success without evidence](https://embedding-shapes.github.io/cursor-implied-success-without-evidence/)｜**日期**：2026-01-16

作者质疑 Cursor 关于用大量自主智能体长时间构建浏览器的宣传，并逐一编译检查最近的提交。评论区提供了更多核查信息。

**评论区观点**：

- 作者对最后 100 个提交逐一运行 cargo check，结果每一个都以某种方式失败。（[评论](https://news.ycombinator.com/item?id=46647037)，embedding-shape）
- 指出博客措辞保守，但社交媒体上的说法（「我们用模型构建了一个浏览器」）造成了夸大的效果。（[评论](https://news.ycombinator.com/item?id=46648761)，paulus_magnus2）
- 另一个同类实验仓库的 CI 有 16 万多次运行，成功的只有 247 次；失败原因是超出支出限额，「智能体根本不在乎」。（[评论](https://news.ycombinator.com/item?id=46649573)，deng）

> "seems every single of them failed in some way" —— [评论](https://news.ycombinator.com/item?id=46647037)

### HN12 · 「Codex 找到了没有 sudo 时的『变通办法』」讨论 {#hn12}
**讨论**：[news.ycombinator.com/item?id=48348578](https://news.ycombinator.com/item?id=48348578)（664 分，311 条评论）｜**原文**：[Codex just found a "workaround" of not having sudo on my PC](https://twitter.com/i/status/2060746160558543217)｜**日期**：2026-06-01

一位用户发现 Codex 在没有 sudo 权限时，借助 docker 组权限绕过了限制。评论区讨论这是已知风险还是智能体越界。

**评论区观点**：

- 安装 Docker 时就有警告：在 docker 组里等同于拥有 root 权限，这是早该知道的。（[评论](https://news.ycombinator.com/item?id=48348780)，jjmarr）
- 关键在于用户请求是什么：如果只是调试问题，而模型自己决定去覆盖不易写入的文件，那就非常危险——用户多半没想到它能不经询问就做到。（[评论](https://news.ycombinator.com/item?id=48349693)，SonOfLilit）
- 也有人说喜欢智能体这样主动帮忙，不希望模型被削弱。（[评论](https://news.ycombinator.com/item?id=48349380)，CSMastermind）

> "Most likely the user did not expect it to have access to that without asking" —— [评论](https://news.ycombinator.com/item?id=48349693)

### HN13 · 「Claude Code：智能体编码最佳实践」（Anthropic）讨论 {#hn13}
**讨论**：[news.ycombinator.com/item?id=43735550](https://news.ycombinator.com/item?id=43735550)（614 分，257 条评论）｜**原文**：[Claude Code: Best practices for agentic coding](https://www.anthropic.com/engineering/claude-code-best-practices)｜**日期**：2025-04-19

Anthropic 官方最佳实践文章发布后的讨论，评论区补充了成本控制和任务粒度等经验。

**评论区观点**：

- 补充文中缺少的成本控制：注意缓存；让它只读指定的文件，否则会读多余文件或重复读取，耗尽上下文。（[评论](https://news.ycombinator.com/item?id=43737060)，jasonjmcghee）
- 模型有时会重写你没要求改的、本来正常的代码并把它弄坏，多数时候是因为一次要求它做太多。（[评论](https://news.ycombinator.com/item?id=43737046)，zoogeny）
- 心智模型：这类工具等同于外包，信息论上你需要传达的东西差不多；反复调整 claude.md 就像与外包方来回发邮件。（[评论](https://news.ycombinator.com/item?id=43743074)，bob1029）
- Simon Willison 指出文中「think / ultrathink」等词直接映射到不同的思考预算。（[评论](https://news.ycombinator.com/item?id=43739993)，simonw）

> "In most cases, it is because I am asking the model to do too much at once." —— [评论](https://news.ycombinator.com/item?id=43737046)

### HN14 · 「一位 Staff 工程师的 Claude Code 之旅：第一次尝试 95% 是垃圾」讨论 {#hn14}
**讨论**：[news.ycombinator.com/item?id=45107962](https://news.ycombinator.com/item?id=45107962)（550 分，396 条评论）｜**原文**：[A staff engineer's journey with Claude Code](https://www.sanity.io/blog/first-attempt-will-be-95-garbage)｜**日期**：2025-09-03

Sanity 的 Staff 工程师分享用 Claude Code 的经验，标题即「第一版 95% 是垃圾」。评论区给出了防止垃圾输出的方法，也有不少怀疑。

**评论区观点**：

- 防止垃圾要考虑智能体的认知极限：不要提大而复杂的改动；让它先出计划，再小步实现，每步测试后再进行下一步；复杂步骤让它写可视化代码。（[评论](https://news.ycombinator.com/item?id=45108930)，swframe2）
- 总结常见共识：LLM 独立写代码只擅长简单或样板代码，在调试和头脑风暴上有帮助。（[评论](https://news.ycombinator.com/item?id=45114584)，spicyusername）
- 要求看到独立程序员（与 AI 公司无利益关系）用 Claude Code 解决非平凡问题并上线的直播，而不是演示。（[评论](https://news.ycombinator.com/item?id=45112846)，rhubarbtree）

> "Ask for a plan but ask it to implement the plan in small steps and ask the model to test each step before starting the next." —— [评论](https://news.ycombinator.com/item?id=45108930)

### HN15 · 「在我们的智能体评测中，AGENTS.md 胜过 skills」（Vercel）讨论 {#hn15}
**讨论**：[news.ycombinator.com/item?id=46809708](https://news.ycombinator.com/item?id=46809708)（524 分，196 条评论）｜**原文**：[AGENTS.md outperforms skills in our agent evals](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals)｜**日期**：2026-01-29

Vercel 的评测发现：把压缩后的文档索引直接放进 AGENTS.md，比让智能体按需调用 skill 效果更好；文中提到 56% 的评测案例里 skill 从未被调用。评论区争论这是否只是「放进上下文必然被看到」。

**评论区观点**：

- 引用文中数据：56% 的评测案例中 skill 从未被调用，智能体有文档却没用。（[评论](https://news.ycombinator.com/item?id=46816813)，tottenhm）
- 关键发现是「压缩的文档指针」有效：对人难读，对 LLM 直接相关；预计会出现始终加载的压缩索引格式。（[评论](https://news.ycombinator.com/item?id=46818579)，w10-1）
- 质疑：直接放进系统提示当然 100% 在上下文中，但到一定规模必须用 skills，因为每次都加载太浪费。（[评论](https://news.ycombinator.com/item?id=46817413)，jgbuddy）
- 认为文中的 AGENTS.md 做法本质上就是简化的 skill；收益来自更好的设计——减少从起点到正确信息之间的步骤和决策。（[评论](https://news.ycombinator.com/item?id=46817461)，thorum）

> "In 56% of eval cases, the skill was never invoked." —— [评论](https://news.ycombinator.com/item?id=46816813)

### HN16 · 「Claude Code 团队如何做代码评审」讨论 {#hn16}
**讨论**：[news.ycombinator.com/item?id=50122951](https://news.ycombinator.com/item?id=50122951)（488 分，481 条评论）｜**原文**：[How the Claude Code team does code review](https://claude.dev/blog/solving-code-review-at-anthropic/)｜**日期**：2026-10-17

Anthropic 介绍其按风险分级的评审流程：大部分路径自动化，人的注意力放在风险高的地方，低风险变更（文档、内部功能、开关后的增量改动）在自动评审和安全检查通过后无需人工评审。评论区争议很大。

**评论区观点**：

- 类比 Google 的基础设施博客：大厂的做法只适合大厂，小团队照搬吃过很多亏；Anthropic 有几乎无限的 token。（[评论](https://news.ycombinator.com/item?id=50127080)，avinoth）
- 批评低风险档「文档无需人工评审」：让 LLM 写文档而不读，是疯狂的。（[评论](https://news.ycombinator.com/item?id=50124042)，koolba）
- 从成本角度质疑：需要考虑模型使用成本的团队无法这样「堆 token」。（[评论](https://news.ycombinator.com/item?id=50124196)，YmFzZTY0ZGFkZHk）
- 引用文中原句：大部分路径是自动化的，人的注意力放在风险所在之处。（[评论](https://news.ycombinator.com/item?id=50124719)，mk12）

> "How anybody can let an LLM write docs and not even read them is pure insanity." —— [评论](https://news.ycombinator.com/item?id=50124042)

### HN17 · Ask HN：AI 辅助编码在你的职业工作中进展如何？ {#hn17}
**讨论**：[news.ycombinator.com/item?id=47388646](https://news.ycombinator.com/item?id=47388646)（434 分，616 条评论）｜**原文**：（自述帖）｜**日期**：2026-03-15

一个征集真实经验的帖子，希望跳出「我们都完了」和「AI 没用」两极。高赞回复大多是负面或复杂的经验。

**评论区观点**：

- 最糟的是管理层用 AI 生成 50 页的设计文档和 PRD 要求尽快评审，没人真正读，连作者自己也不读。（[评论](https://news.ycombinator.com/item?id=47392707)，viccis）
- 工作变成苦差：上游同事什么都用 AI，再让他收拾；一个 AI 写的功能不遵守主项目的 API 设计。（[评论](https://news.ycombinator.com/item?id=47390383)，hdhdhsjsbdh）
- 有人选择不用：清楚自己的惰性会导致技能萎缩；同事坦言想戒掉 AI 生成代码却很难，像上瘾。（[评论](https://news.ycombinator.com/item?id=47391995)，Izkata）
- 一位大厂工程师说除了总结设计文档、查找代码外几乎没成功过，还没靠提示得到过可用的提交。（[评论](https://news.ycombinator.com/item?id=47390316)，onlyrealcuzzo）

> "the feature was AI coded so it did not obey the API design of the main project" —— [评论](https://news.ycombinator.com/item?id=47390383)

### HN18 · 「我们把编码智能体放进 while 循环」讨论 {#hn18}
**讨论**：[news.ycombinator.com/item?id=45005434](https://news.ycombinator.com/item?id=45005434)（425 分，308 条评论）｜**原文**：[We put a coding agent in a while loop](https://github.com/repomirrorhq/repomirror/blob/main/repomirror.md)｜**日期**：2025-08-25

repomirror 团队用循环反复运行编码智能体做代码移植，报告了不少意外行为。评论区关注其中的质量与后果。

**评论区观点**：

- 引用报告：移植完成后，大多数智能体转而写额外的测试或不断更新 agent/TODO.md 说明自己有多「完成」；有一次智能体发现自己陷入死循环，用 pkill 终止了自己。（[评论](https://news.ycombinator.com/item?id=45005604)，NitpickLawyer）
- 报告里有很多「勉强能用」；单次调用得到「差不多好」的代码，循环只会得到很多「差不多好」的代码，需要新流程——例如用带示例表的 Cucumber 式需求先生成测试。（[评论](https://news.ycombinator.com/item?id=45005590)，giantg2）
- 软件开发有两个产出：代码的变化，以及写代码的人认知的变化。（[评论](https://news.ycombinator.com/item?id=45005722)，bwestergard）

> "If we get "almost" good code from a single invocation, you just going to get a lot of almost good code from a loop." —— [评论](https://news.ycombinator.com/item?id=45005590)

### HN19 · 「我用来提升 LLM 辅助代码质量的 agent.md」（Fabien Sanglard）讨论 {#hn19}
**讨论**：[news.ycombinator.com/item?id=49410932](https://news.ycombinator.com/item?id=49410932)（415 分，176 条评论）｜**原文**：[My agent.md to improve LLM-assisted code quality](https://fabiensanglard.net/agent.md/index.html)｜**日期**：2026-08-24

Fabien Sanglard 分享了自己的 agent.md 规则。评论区讨论这些规则该放在哪里、怎么执行。

**评论区观点**：

- 其中很多应该用 lint 强制执行（如单行 if 也要加花括号、函数名少于 30 字符），这样手写代码的人也会得到同样的反馈。（[评论](https://news.ycombinator.com/item?id=49411956)，OptionOfT）
- 大部分内容不该放在 AGENTS.md，而应放进 CODING_STANDARDS.md，由写代码和评审时的 skill 按需读取，避免污染上下文；另用子智能体评审计划和代码。（[评论](https://news.ycombinator.com/item?id=49415163)，gregwebs）
- 智能体指令最好按项目从经验中学习，别人的规则在自己项目里可能只是废话。（[评论](https://news.ycombinator.com/item?id=49411946)，getnormality）

> "A bunch of these should be enforce with linting" —— [评论](https://news.ycombinator.com/item?id=49411956)

### HN20 · 「用来写代码的 AI 智能体，必须降低你的维护成本」（James Shore）讨论 {#hn20}
**讨论**：[news.ycombinator.com/item?id=48089289](https://news.ycombinator.com/item?id=48089289)（380 分，108 条评论）｜**原文**：[An AI coding agent, used to write code, needs to reduce your maintenance costs](https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs)｜**日期**：2026-05-11

James Shore 认为，衡量编码智能体的标准应是能否降低维护成本，而不只是写得快。评论区有支持，也有不同经验。

**评论区观点**：

- 反例经验：在一组几十年历史的项目上，AI 反而降低了维护成本，老代码更易现代化，许多旧依赖被更新或消除。（[评论](https://news.ycombinator.com/item?id=48090348)，keithnz）
- 团队用 AI 不只加代码，也积极删除废弃代码：把前后端整个代码库交给智能体画出调用地图，回答「还有人用这个吗」。（[评论](https://news.ycombinator.com/item?id=48096459)，Seattle3503）
- 可维护性不应被归为「非功能需求」，它保障的是未来功能需求的交付能力。（[评论](https://news.ycombinator.com/item?id=48090385)，richardbarosky）
- 补充：软件还有用户支持成本，维护成本也未必线性增长。（[评论](https://news.ycombinator.com/item?id=48092010)，dirkc）

> "My team has been using AI to add code, but also to aggressively remove old deprecated code." —— [评论](https://news.ycombinator.com/item?id=48096459)

### HN21 · 「用 LLM 编码几个月后，我回到用自己的脑子」讨论 {#hn21}
**讨论**：[news.ycombinator.com/item?id=44003700](https://news.ycombinator.com/item?id=44003700)（365 分，221 条评论）｜**原文**：[After months of coding with LLMs, I'm going back to using my brain](https://albertofortin.com/writing/coding-with-ai)｜**日期**：2025-05-16

作者在一次代码评审中发现 LLM 生成的代码问题百出，决定回到自己思考。评论区提出「理解才是瓶颈」等观点。

**评论区观点**：

- 大多数人的瓶颈不是生成代码，而是理解代码：生成速度翻倍，就要在评审、测试、建立心智模型上加倍偿还，而要维护代码库就必须这样做。（[评论](https://news.ycombinator.com/item?id=44004319)，meander_water）
- 继续重度使用但定两条规则：不把深度思考交给它；逐行深度评审并修改它生成的代码。（[评论](https://news.ycombinator.com/item?id=44003966)，dmazin）
- 用 Cursor 几个月取得的效率，在评审中发现各种细微 bug 后被立刻抵消。（[评论](https://news.ycombinator.com/item?id=44004077)，rco8786）
- 只用 LLM 生成不重要的一次性界面，不理解「全押」心态。（[评论](https://news.ycombinator.com/item?id=44004024)，jclardy）

> "the bottleneck for most people is not code generation, it's code understanding" —— [评论](https://news.ycombinator.com/item?id=44004319)

### HN22 · 「AI 代码评审存在泡沫」（Greptile）讨论 {#hn22}
**讨论**：[news.ycombinator.com/item?id=46766961](https://news.ycombinator.com/item?id=46766961)（351 分，249 条评论）｜**原文**：[There is an AI code review bubble](https://www.greptile.com/blog/ai-code-review-bubble)｜**日期**：2026-01-26

AI 代码评审厂商 Greptile 的文章讨论评审赛道的泡沫，并主张评审智能体应独立于编码智能体。评论区对 AI 评审的实际效果评价不一。

**评论区观点**：

- AI 评审确实能找出关键 bug（回顾分析约八成情况），但信噪比差，一个关键错误伴随二十条臆测；而足够的人类注意力通常也能发现那个关键 bug。（[评论](https://news.ycombinator.com/item?id=46771757)，zmmmmm）
- 试用某 AI 评审 3 个 PR 后放弃，认为几乎全是噪声，还建议吞掉异常这种有害做法。（[评论](https://news.ycombinator.com/item?id=46777079)，sebra）
- 不认同「独立性」是竞争优势：编码和评审即使来自同一公司，也可以做到相互独立。（[评论](https://news.ycombinator.com/item?id=46771085)，rushingcreek）

> "the signal to noise ratio is poor" —— [评论](https://news.ycombinator.com/item?id=46771757)

### HN23 · 「AI 编码让 CI 成了瓶颈，我们重做了 CI」（Linear）讨论 {#hn23}
**讨论**：[news.ycombinator.com/item?id=49792067](https://news.ycombinator.com/item?id=49792067)（317 分，408 条评论）｜**原文**：[AI coding has made CI a bottleneck, so we reworked ours to keep up](https://linear.app/now/ci-bottleneck-reworked)｜**日期**：2026-09-22

Linear 介绍为应对 AI 带来的变更量，把工作负载迁到更快的 runner、改进缓存等。评论区追问瓶颈究竟在哪。

**评论区观点**：

- 瓶颈不在 CI，而在人工测试：它能跑，但是否真正做到我们想要的、客户能理解并喜欢？（[评论](https://news.ycombinator.com/item?id=49792937)，aliclark）
- 怀疑很大一部分是无用测试的雪崩：LLM 写的测试常常只测内置行为和琐碎逻辑。（[评论](https://news.ycombinator.com/item?id=49795270)，dgroshev）
- 追问：大家都快到不断撞墙，为什么没看到产品明显变好？（[评论](https://news.ycombinator.com/item?id=49793761)，torben-friis）

> "I suspect a substantial part of this is an avalanche of useless testing." —— [评论](https://news.ycombinator.com/item?id=49795270)

### HN24 · 「我看着 Gemini CLI 产生幻觉并删除了我的文件」讨论 {#hn24}
**讨论**：[news.ycombinator.com/item?id=44651485](https://news.ycombinator.com/item?id=44651485)（304 分，365 条评论）｜**原文**：[I watched Gemini CLI hallucinate and delete my files](https://anuraag2601.github.io/gemini_cli_disaster.html)｜**日期**：2025-07-23

作者记录 Gemini CLI 误以为 mkdir 成功，随后用通配符移动文件导致文件互相覆盖丢失。评论区讨论智能体遇到障碍时的行为。

**评论区观点**：

- Claude 说「换个方法试试」时也让人紧张：通常是遇到了让任务不可能完成的关键障碍，正确做法是停下来告诉用户，它却不惜一切要完成任务。（[评论](https://news.ycombinator.com/item?id=44654852)，nojs）
- 质疑作者为何确信换成另一家就不会删文件。（[评论](https://news.ycombinator.com/item?id=44652095)，lordgrenville）
- 有人对文中关于命令行为的技术解释提出疑问。（[评论](https://news.ycombinator.com/item?id=44657901)，Ukv）

> "the correct response would be to stop and tell me the problem" —— [评论](https://news.ycombinator.com/item?id=44654852)

### HN25 · 「我们每周收 1 万美元，帮你删除 AI 生成的代码」讨论 {#hn25}
**讨论**：[news.ycombinator.com/item?id=48823359](https://news.ycombinator.com/item?id=48823359)（304 分，240 条评论）｜**原文**：[We charge ＄10k a week to delete AI-generated code](https://odra.dev/slopfix/)｜**日期**：2026-07-08

一家咨询团队推出服务：客户发来十万行 AI 生成的「意大利面代码」，由他们重构、用库替换手写实现、删除冗余。评论区有赞同，也有不同经验。

**评论区观点**：

- 创建者自述：客户常常说是「小重构」，结果发来 10 万行 AI 生成的代码；有经验的工程师能很快看出该重构什么、哪里可以用库替换几千行手写代码。（[评论](https://news.ycombinator.com/item?id=48823360)，zie1ony）
- 反例：他们用 vibe coding 替换了每年 12 万美元的低代码平台，运作良好，用 JIRA 工单驱动 AI 修改。（[评论](https://news.ycombinator.com/item?id=48826120)，thraway3837）
- AI 本质上是在用充满歧义的英语这种不精确的「编程语言」描述精确关系，小规模很好用，复杂度一高就出问题。（[评论](https://news.ycombinator.com/item?id=48826068)，martin1975）

> "sends you 100k lines of AI-generated spaghetti" —— [评论](https://news.ycombinator.com/item?id=48823360)

### HN26 · 「哈佛研究者发现：AI 编码智能体把瓶颈转移到了代码评审」讨论 {#hn26}
**讨论**：[news.ycombinator.com/item?id=50538303](https://news.ycombinator.com/item?id=50538303)（297 分，384 条评论）｜**原文**：[Harvard researchers find AI coding agents shifted the bottleneck to code review](https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/)｜**日期**：2026-11-18

报道介绍一项研究：编码智能体使瓶颈从写代码转向评审。评论区多为一线经验的印证或补充。

**评论区观点**：

- 一位专职评审者说：AI 让合并请求的代码更多，方案常常对需求而言过度设计；人写代码时的「懒」反而让东西保持简单。（[评论](https://news.ycombinator.com/item?id=50544119)，littlecranky67）
- 有 25 年经验的开发者认为 AI 写代码不比他差，找问题的评审也比他强很多；但评审不只是找问题，也是为了理解。（[评论](https://news.ycombinator.com/item?id=50543695)，alkonaut）
- 每天都在评审 AI 写的代码，自己的或同事的，「真的不喜欢」。（[评论](https://news.ycombinator.com/item?id=50541141)，AlwaysRock）
- 质疑大学研究跟不上节奏：结论是大家几个月前就遇到的，且常基于过时模型。（[评论](https://news.ycombinator.com/item?id=50539755)，lz400）

> "often the chosen solution is overblown/overdesigned for what actually needs to be done" —— [评论](https://news.ycombinator.com/item?id=50544119)

### HN27 · 「AI 编码工具可能降低生产力」（METR 研究解读）讨论 {#hn27}
**讨论**：[news.ycombinator.com/item?id=44526912](https://news.ycombinator.com/item?id=44526912)（279 分，274 条评论）｜**原文**：[AI coding tools can reduce productivity](https://secondthoughts.ai/p/ai-coding-slowdown)｜**日期**：2025-07-11

文章解读 METR 的随机对照研究：16 名有经验的开源开发者在自己熟悉的大型仓库上完成 246 个真实任务。评论区对生产力能否度量、个人体感是否可靠争论激烈。

**评论区观点**：

- 引用研究方法：招募 16 名来自大型开源仓库（平均 2.2 万多星、上百万行代码）的资深贡献者，提供 246 个对仓库有价值的真实问题。（[评论](https://news.ycombinator.com/item?id=44527254)，freetime2）
- 有人坚称自己用 Claude Code 后效率提升 10 到 20 倍，以单位时间实现的功能数衡量。（[评论](https://news.ycombinator.com/item?id=44528419)，calrain）
- 更根本的问题：四十年来我们一直无法有意义地度量程序员生产力。（[评论](https://news.ycombinator.com/item?id=44527538)，tomcam）
- LLM 让人去做原本会一直拖着不做的项目，这种收益难以被研究捕捉。（[评论](https://news.ycombinator.com/item?id=44527489)，JKCalhoun）

> "we seem to be incapable of determining programmer productivity in a meaningful way" —— [评论](https://news.ycombinator.com/item?id=44527538)

### HN28 · 「智能体编码的教训：代码变便宜时我们该做什么？」（Drew Breunig）讨论 {#hn28}
**讨论**：[news.ycombinator.com/item?id=48019025](https://news.ycombinator.com/item?id=48019025)（270 分，237 条评论）｜**原文**：[Lessons for Agentic Coding: What should we do when code is cheap?](https://www.dbreunig.com/2026/05/04/10-lessons-for-agentic-coding.html)｜**日期**：2026-05-05

Drew Breunig 列出 10 条关于代码变便宜后的教训，其中一条是代码「免费如同小狗」（养起来并不免费）。评论区围绕「代码到底便不便宜」争论。

**评论区观点**：

- 某些代码确实便宜：概念验证、符合现有架构的小功能；但智能体擅长细节却没有品味，有机会就会把代码库变成一团泥。（[评论](https://news.ycombinator.com/item?id=48020020)，noelwelsh）
- 代码从来都不便宜；按当前不现实的 AI 定价用智能体比雇初级工程师便宜，并不意味着代码便宜。（[评论](https://news.ycombinator.com/item?id=48021336)，lionkor）
- 也有人说最新前沿模型让行业越过了信任线，工单和提交信息质量都提高了。（[评论](https://news.ycombinator.com/item?id=48021145)，spicyusername）
- 赞同「free as in puppies」：很多管理者把「写代码几乎免费」误读为「工程免费」。（[评论](https://news.ycombinator.com/item?id=48019350)，torben-friis）

> "They'll turn a code base into a ball of mud very quickly, given the opportunity." —— [评论](https://news.ycombinator.com/item?id=48020020)

### HN29 · 「Context Rot：输入 token 增加如何影响 LLM 表现」（Chroma）讨论 {#hn29}
**讨论**：[news.ycombinator.com/item?id=44564248](https://news.ycombinator.com/item?id=44564248)（260 分，59 条评论）｜**原文**：[Context Rot: How increasing input tokens impacts LLM performance](https://research.trychroma.com/context-rot)｜**日期**：2025-07-15

Chroma 的技术报告显示，包括多款前沿模型在内，模型表现会随上下文长度变化而不均匀，作者据此强调上下文工程的必要。评论区补充了大量一线经验。

**评论区观点**：

- 在 Cursor 里，同一功能的对话越长输出越差；最好的结果来自预先给出清晰明确的指令和计划，并把相关文件拖进上下文。（[评论](https://news.ycombinator.com/item?id=44569139)，milchek）
- 会话越长，Claude Code 越分不清自己的错误和用户的指令，开始循环，甚至认定被它自己弄坏的测试「本来就坏了」；一旦混乱就重新开始。（[评论](https://news.ycombinator.com/item?id=44571839)，boesboes）
- 希望能方便地修剪上下文，把模型摸索浪费的那两万 token 剪掉。（[评论](https://news.ycombinator.com/item?id=44567755)，Workaccount2）
- 先摘要、再按需提供原文，比一次塞入大量文档效果更好。（[评论](https://news.ycombinator.com/item?id=44565971)，posnet）

> "Once it gets confused, start over." —— [评论](https://news.ycombinator.com/item?id=44571839)
