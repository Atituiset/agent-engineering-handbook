# 原始报告：说明与索引

这是本站的「原始报告」部分：从模型厂商官方博客与文档、大厂工程博客、Thoughtworks / martinfowler.com、独立资深工程师博客、X 帖子、中文技术社区、开源项目与学术研究中，整理出的关于**如何驾驭大模型与编码智能体**的一手资料。

[实践手册](/handbook/) 中的每一条建议都回链到这里的条目编号（例如 [AN01](/sources/anthropic#an01)），读者可以顺着链接回到原文自行判断。

## 收录与核对规则

- **只收录核对过的链接。** 每条链接都在 2026-11-18 前后实际打开过：用脚本抓取并检查 HTTP 200 与页面标题；少数屏蔽脚本抓取的站点（如 openai.com、Hacker News、部分 JS 渲染页面）改用浏览器式抓取核对。打不开、已下线或内容对不上的来源一律不收。
- **摘要忠于原文。** 每条 2–5 句中文摘要；引文为英文原句，逐字比对过页面文本。
- **标注证据性质。** `厂商自报` 指数字和结论来自产品方本身，未经独立验证；`作者自述` 指个人经验；`团队自报`、`会议预告` 同理。只有「研究与数据」一类是对照实验或调查。
- **不编造。** 没有在原文中找到的日期标为「持续更新」或只写年份；数字只用原文出现过的。
- **版权。** 摘要与引文的权利归原作者所有，请以原文为准。本站原创文字以 CC BY 4.0 发布。

## 分类索引

| 分类 | 编号 | 条目数 | 内容 |
| --- | --- | --- | --- |
| [Anthropic / Claude Code](./anthropic) | AN | 40 | 官方文档、工程博客、claude.dev、研究博客；含成本、遥测、提示缓存与 context editing |
| [OpenAI / Codex](./openai) | OA | 12 | Harness engineering、Codex 智能体循环、AGENTS.md、内部实践、Codex 云端任务、提示缓存、SWE-bench Verified 弃用 |
| [Google · Meta · GitHub](./bigtech) | BT | 22 | Gemini CLI / Conductor、ADK、Meta 测试生成与部落知识、Copilot 与 Spec Kit、Copilot 云端会话与公开代码匹配、Google 代码迁移 |
| [工具厂商](./vendors) | VD | 22 | Cursor、Cognition、Vercel、Amp、Factory、Kiro、Manus、LangChain、HumanLayer；含 Cursor 云端智能体、LangGraph 持久化 |
| [Thoughtworks 与 martinfowler.com](./thoughtworks) | TW | 36 | Böckeler 等人的系列文章、技术雷达条目 |
| [独立工程师与意见领袖](./practitioners) | PR | 36 | Simon Willison、Kent Beck、Armin Ronacher、Mitchell Hashimoto 等 |
| [X 精选（按主题，v2 主力来源）](./x/) | XW/XC/XP/XV/XR/XK/XT/XA/XS/XM/XF | 205 | 141 位作者；工作流、上下文、计划、测试、评审、约束、工具、并行、安全、团队、失败与反思 |
| [X 帖子（v1）](./x-posts) | X | 11 | Karpathy、Greg Brockman、Boris Cherny、Thariq 等 |
| [Hacker News 高热讨论](./hackernews) | HN | 29 | 高互动讨论串与评论区代表性观点 |
| [中文互联网](./chinese) | CN / TX / AL / BD | 89 | 美团、腾讯、快手、百度、字节、蚂蚁、京东、阿里云、InfoQ、宝玉、阮一峰、少数派等；含 2026-11 增补的腾讯、阿里（含蚂蚁）、字节团队材料（TX / AL / BD） |
| [开源项目与规范](./open-source) | OS / TX | 18 | AGENTS.md、Spec Kit、MCP、Superpowers、架构约束工具；含 CubeSandbox、OpenTelemetry GenAI 语义约定、A2A |
| [研究与数据](./research) | RS / AL / BD | 17 | METR（含 2026-02 后续）、DORA（含 AI 能力模型）、GitClear、AGENTS.md 评估论文、τ-bench、SWE-bench Verified 审计、技能形成对照实验、美国版权局报告；含 Qwen3-Coder、Trae Agent、Repo2Run 等工业论文 |
| [安全](./security) | SC / TX / BD | 13 + 索引 | 致命三要素、提示注入设计模式、包幻觉、MCP 授权与工具投毒、二选规则、CaMeL、自适应攻击；含 A.S.E 安全评测与 Trae 遥测分析 |
| [智能体评测专题](./evals)（2026-11 新增） | EV | 20 | 评分器隔离与评测作弊、LLM 裁判的偏差与版本漂移、基础设施噪声、SWE-Bench Pro / τ²-bench / OSWorld / Terminal-Bench、代码评审与漏洞检测评测、八个评测框架的官方文档 |
| [质量与 CI/CD 专题](./quality/)（2026-11 新增） | QB/QT/QP/QR/QO/QC/QX/QH / TX/AL/BD | 172 | 测试、CI 门禁、AI 评审、Evals、沙箱验证、合并队列与发布、护栏、度量与反模式；大厂、工具、工程师、研究、开源、中文、X、HN；含按主题分散进来的腾讯、阿里、字节条目 |

精选合计约 **740 条**完整条目（不含交叉索引）：v1 的 207 条，加上 2026-11 扩充的 X 精选 205 条、中文 39 条、HN 29 条，质量与 CI/CD 专题（含后来按主题并入的测试、评审、评测等条目），以及分散到中文互联网、研究、安全与开源分类中的腾讯、阿里、字节团队材料；2026-11 补齐缺口时又新增 25 条（异步与云端智能体、成本与遥测、评测方法、MCP 与注入防御、技能形成、版权等），之后又为第 16 章新增智能体评测专题 20 条。

此外，[全量库](/library/)收录 **3,215 条**资料（X 帖子 1,525 条、HN 讨论 542 个、GitHub 仓库 630 个、精选条目与网页 518 条），只列元数据，用于统计各条实践的 [共识度/佐证](/compare/evidence)。腾讯、阿里、字节相关条目带有公司字段，可在 [在线筛选](/library/#explorer) 中按公司查看。

## 如何阅读

1. **先看厂商，再看独立声音，最后看数据。** 厂商最了解自己的工具，但有推广动机；独立工程师的经验更贴近日常，但样本是个人；研究最严谨，但往往落后于模型代际。
2. **注意时间。** 2025 年中与 2026 年下半年的模型能力差别很大，一些「过去必须这样做」的规则已被厂商自己推翻（见 [X07](./x-posts#x07)）。
3. **找分歧。** 本报告刻意保留了相互矛盾的观点：上下文文件到底有没有用（[RS06](./research#rs06) vs [VD11](./vendors#vd11)）、要不要多智能体（[VD05](./vendors#vd05) vs [VD06](./vendors#vd06)）、TDD 在智能体循环中是否有效（[TW04](./thoughtworks#tw04) vs [PR09](./practitioners#pr09)）。手册在 [对比与取舍](/compare/) 中讨论如何选择。
