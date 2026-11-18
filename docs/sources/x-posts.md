# X（Twitter）上的一线声音

> 精选来自模型厂商与工具作者本人的 X 帖子。帖子是即时观点，常带产品宣传成分，统一视为 **「作者自述」**。日期按帖子 UTC 时间标注。均于 2026-11-18 打开核对。

[[toc]]

### X01 · Karpathy：+1 for "context engineering" {#x01}
**作者**：Andrej Karpathy (@karpathy)｜**日期**：2025-06-25｜[原文](https://x.com/karpathy/status/1937902205765607626)

支持用「上下文工程」替代「提示工程」：在每个工业级 LLM 应用中，上下文工程是「为下一步恰好填入正确信息」的艺术与科学——任务描述与解释、少样本示例、RAG、相关数据、工具、状态与历史、压缩……太少或形式不对，模型缺乏所需上下文；太多或不相关，成本上升、性能下降。此外应用还需要把问题拆成合适的控制流、调度合适能力的模型、处理「生成-验证」的交互流程。

> "context engineering is the delicate art and science of filling the context window with just the right information for the next step."

### X02 · Karpathy：从 vibe coding 到 agentic engineering {#x02}
**作者**：Andrej Karpathy｜**日期**：2026-02-04｜[原文](https://x.com/karpathy/status/2019137879310836075)

「vibe coding」一周年回顾：当时模型能力弱，主要用于好玩的一次性项目；一年后，通过 LLM 智能体编程正成为专业人士的默认工作流，但伴随更多监督与审查。目标是获得智能体的杠杆，同时**不在软件质量上做任何妥协**。他个人倾向称之为「agentic engineering」：你 99% 的时间不直接写代码，而是编排智能体并承担监督；「engineering」强调这是一门可学习、有深度的专业。

### X03 · Karpathy：编程在去年 12 月发生了突变 {#x03}
**作者**：Andrej Karpathy｜**日期**：2026-02-25｜[原文](https://x.com/karpathy/status/2026731645169185220)

认为编码智能体「12 月之前基本不能用，之后基本能用」：模型质量、长程连贯性与韧性显著提升。举例让智能体在约 30 分钟内自主完成一整套本地视频分析服务的部署、测试、记录笔记与报告。属于个人观感，但代表了 2026 年初许多从业者的判断转折——也解释了为什么 2025 年的一些「不要这样做」需要重新审视。

### X04 · Greg Brockman：OpenAI 如何让团队转向智能体式开发 {#x04}
**作者**：Greg Brockman (@gdb，OpenAI 总裁)｜**日期**：2026-02-06｜[原文](https://x.com/gdb/status/2019566641491963946)

OpenAI 内部的组织级推进清单：每个团队指定一名「agents captain」；为每个项目创建并维护 AGENTS.md，**每当智能体出错或吃力时就更新它**；把让 Codex 做过的事写成 skills 并提交到共享仓库；盘点内部工具并通过 CLI 或 MCP 让智能体可用；按「agent-first」组织代码库——写运行快的测试、在组件间建立高质量接口；**对 slop 说不**——确保每段合并代码都有一个人负责，评审标准不低于人写代码，且作者理解自己提交的内容；建设基础设施，例如可观测性、追踪产生代码的智能体轨迹。

> "Ensure that some human is accountable for any code that gets merged."

### X05 · Boris Cherny：我的配置出奇地朴素 {#x05}
**作者**：Boris Cherny (@bcherny，Claude Code 创建者)｜**日期**：2026-01-02｜[原文](https://x.com/bcherny/status/2007179832300581177)

一条长串帖子的开篇：Claude Code 开箱即用效果就很好，他本人很少定制；使用方式没有唯一正解，团队里每个人用法都很不一样。对「必须先搭复杂配置」的焦虑是一个有用的反证。

### X06 · Boris Cherny：让模型自主运行数小时到数天的五个建议 {#x06}
**作者**：Boris Cherny｜**日期**：2026-06-08｜[原文](https://x.com/bcherny/status/2063792263067754658)

五点：用 auto mode 处理权限；用动态工作流编排大量子智能体；用 /goal 或 /loop 推动它持续到完成；在云端运行以便合上电脑；**确保它能端到端地自我验证**——Web 用浏览器扩展、移动端用模拟器 MCP、后端要能启动完整服务。

### X07 · Thariq：Claude 5 模型时代上下文工程的新规则 {#x07}
**作者**：Thariq (@trq212，Anthropic Claude Code 团队)｜**日期**：2026-07-24｜[原文](https://x.com/trq212/status/2080710971228918066)

Anthropic 为新一代模型删掉了 Claude Code 系统提示中超过 80% 的内容，**在其编码评测上没有可测量的损失**（厂商自报）。他们发现自己通过系统提示、CLAUDE.md 与 skills 过度约束了模型，常出现「适当写文档」与「不要加注释」这类相互冲突的指令。总结的「过去 → 现在」：给规则 → 让模型用判断；给示例 → 设计接口（示例会把模型限制在特定探索空间）；全部前置 → 渐进式披露（验证与评审移入按需调用的 skills，工具延迟加载）。CLAUDE.md 应保持轻量、聚焦于坑点。

> "We removed over 80% of Claude Code’s system prompt for models like Claude Opus 5 and Claude Fable 5 with no measurable loss on our coding evaluations."

`厂商自报、尚未独立验证` · 注意：这一结论与模型代际强相关，对较弱模型未必成立。

### X08 · Boris Cherny：接受计划时自动清空上下文 {#x08}
**作者**：Boris Cherny｜**日期**：2026-01-17｜[原文](https://x.com/bcherny/status/2012663636465254662)

Claude Code 新行为：接受计划后自动清空上下文，让计划在全新上下文窗口中执行。团队发现这能让模型更久地保持在轨道上，并**显著提高对计划的遵守度**（厂商自报）。这是「计划与执行分离 + 上下文隔离」的一个产品化例证。

### X09 · Boris Cherny：让 Claude 接管应用的日常维护 {#x09}
**作者**：Boris Cherny｜**日期**：2026-08-13｜[原文](https://x.com/bcherny/status/2088014489438621990)

在专门的 Slack 频道里运行一组每日例程：崩溃模糊测试（在模拟器中点来点去找崩溃并修复）、重复抽象统一、死代码移除（先加日志确认真的死了再删）、「抽象警察」修复泄漏的抽象等。几周内这些例程开了 388 个 PR，其中 180 个在 Claude Code Review **加人工评审**后合并（厂商自报）。合并率不到一半，本身就说明人工把关仍不可或缺。

### X10 · dex：「harness engineering」一词的提出 {#x10}
**作者**：Dex Horthy (@dexhorthy，HumanLayer)｜**日期**：2025-11-04｜[原文](https://x.com/dexhorthy/status/1985699548153467120)

提出「harness engineering」：把上下文工程原则应用到你如何使用一个现成的智能体上——对 Claude Code 而言就是用户接入的 commands、hooks、skills、agents、MCP 等「集成点」。没有上下文工程的理解就做不好 harness 工程，而上下文工程又需要对 LLM 的直觉。

### X11 · Guillermo Rauch：2026 是回归基本功的一年 {#x11}
**作者**：Guillermo Rauch (@rauchg，Vercel CEO)｜**日期**：2026-01-13｜[原文](https://x.com/rauchg/status/2011152152623005736)

「Unix、CLI、测试与类型、Markdown，优秀且易获取的文档。」并举例 Vercel 文档可以按 `accept: text/markdown` 返回 Markdown，智能体默认如此请求，节省流量与 token。是「对人好的工程实践对智能体同样好」的简洁表达。
