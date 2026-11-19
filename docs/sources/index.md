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
| [Anthropic / Claude Code](./anthropic) | AN | 36 | 官方文档、工程博客、claude.dev、研究博客 |
| [OpenAI / Codex](./openai) | OA | 9 | Harness engineering、Codex 智能体循环、AGENTS.md、内部实践 |
| [Google · Meta · GitHub](./bigtech) | BT | 19 | Gemini CLI / Conductor、ADK、Meta 测试生成与部落知识、Copilot 与 Spec Kit |
| [工具厂商](./vendors) | VD | 20 | Cursor、Cognition、Vercel、Amp、Factory、Kiro、Manus、LangChain、HumanLayer |
| [Thoughtworks 与 martinfowler.com](./thoughtworks) | TW | 36 | Böckeler 等人的系列文章、技术雷达条目 |
| [独立工程师与意见领袖](./practitioners) | PR | 36 | Simon Willison、Kent Beck、Armin Ronacher、Mitchell Hashimoto 等 |
| [X 精选（按主题，v2 主力来源）](./x/) | XW/XC/XP/XV/XR/XK/XT/XA/XS/XM/XF | 205 | 141 位作者；工作流、上下文、计划、测试、评审、约束、工具、并行、安全、团队、失败与反思 |
| [X 帖子（v1）](./x-posts) | X | 11 | Karpathy、Greg Brockman、Boris Cherny、Thariq 等 |
| [Hacker News 高热讨论](./hackernews) | HN | 29 | 高互动讨论串与评论区代表性观点 |
| [中文互联网](./chinese) | CN | 50 | 美团、腾讯、快手、百度、字节、蚂蚁、京东、阿里云、InfoQ、宝玉、阮一峰、少数派等 |
| [开源项目与规范](./open-source) | OS | 15 | AGENTS.md、Spec Kit、MCP、Superpowers、架构约束工具 |
| [研究与数据](./research) | RS | 8 | METR、DORA、GitClear、AGENTS.md 评估论文 |
| [安全](./security) | SC | 6 + 索引 | 致命三要素、提示注入设计模式、包幻觉 |
| [质量与 CI/CD 专题](./quality/)（2026-11 新增） | QB/QT/QP/QR/QO/QC/QX/QH | 143 | 测试、CI 门禁、AI 评审、Evals、沙箱验证、合并队列与发布、护栏、度量与反模式；大厂、工具、工程师、研究、开源、中文、X、HN |

精选合计约 **620 条**完整条目（不含交叉索引）：v1 的 207 条，加上 2026-11 扩充的 X 精选 205 条、中文 39 条、HN 29 条，以及质量与 CI/CD 专题的 143 条（其中 14 条链接与此前条目重复，从质量角度重读）。

此外，[全量库](/library/)收录 **2,904 条**资料（X 帖子 1,501 条、HN 讨论 539 个、GitHub 仓库 526 个、精选条目与网页 338 条；其中质量专题新增 681 条），只列元数据，用于统计各条实践的 [共识度/佐证](/compare/evidence)。

## 如何阅读

1. **先看厂商，再看独立声音，最后看数据。** 厂商最了解自己的工具，但有推广动机；独立工程师的经验更贴近日常，但样本是个人；研究最严谨，但往往落后于模型代际。
2. **注意时间。** 2025 年中与 2026 年下半年的模型能力差别很大，一些「过去必须这样做」的规则已被厂商自己推翻（见 [X07](./x-posts#x07)）。
3. **找分歧。** 本报告刻意保留了相互矛盾的观点：上下文文件到底有没有用（[RS06](./research#rs06) vs [VD11](./vendors#vd11)）、要不要多智能体（[VD05](./vendors#vd05) vs [VD06](./vendors#vd06)）、TDD 在智能体循环中是否有效（[TW04](./thoughtworks#tw04) vs [PR09](./practitioners#pr09)）。手册在 [对比与取舍](/compare/) 中讨论如何选择。
