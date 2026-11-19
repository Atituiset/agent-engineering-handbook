# 质量与 CI/CD 专题：说明与索引

> 这个专题回答一个问题：**一线大厂和优秀工程师怎样保证 AI 或智能体交付的代码质量？** 范围包括测试（TDD、单测、E2E、属性测试、变异测试）、CI/CD 门禁、AI 代码评审、Evals、沙箱化验证、合并队列与发布策略、护栏（必需检查、CODEOWNERS、来源与签名）、度量，以及反模式（删测试、reward hacking、快照覆盖）。综合结论见 [第 12 章 · 质量保障](/handbook/12-quality-cicd)。

## 规模 {#stats}

- **精选 172 条**：每条都有中文摘要、原文引文和原文链接。引文已与原文逐字核对：网页用抓取的正文，X 用 API 返回的帖子全文，HN 用 Firebase API 返回的评论正文。其中 14 条的链接 v2 已收录，这里从质量保障的角度重新解读。另有 29 条腾讯、阿里、字节的测试、评审、评测与 CI 条目按主题并入本专题（标题前有公司标注，编号仍为 TX / AL / BD）。
- **全量库新增 681 条**（主题标记为「质量保障与 CI/CD」）：X 帖子 290 条、GitHub 仓库 211 个、Hacker News 讨论串 96 个、本专题新增的精选条目 77 条、其他网页 7 条。见 [全量库 · 质量专题](/library/q-curated)，也可在 [在线筛选](/library/#explorer) 中选主题「质量保障与 CI/CD」。
- 检索和核对时间为 2026-11 中旬（北京时间）。

## 分页 {#pages}

| 页面 | 编号 | 条目数 | 内容 |
| --- | --- | --- | --- |
| [大厂与平台团队实践](./bigtech) | QB | 19 | Stripe、Spotify、Uber、Meta、Google、Microsoft、Airbnb、Shopify、Atlassian、Datadog |
| [工具与官方文档](./tools) | QT | 23 | Anthropic、OpenAI、GitHub、Google、Cursor、Hypothesis |
| [一线工程师与方法论](./practitioners) | QP | 15 | Kent Beck、Simon Willison、Addy Osmani、Birgitta Böckeler、Hamel Husain、Eugene Yan、Shreya Shankar |
| [研究与数据](./research) | QR / TX / AL / BD | 19 | METR、ImpossibleBench、SWE-bench 实证、DORA，以及厂商报告（已标注）；含 AACR-Bench、LogSage、BitsAI-Fix、TestGPT、NL2Test 等工业论文 |
| [开源项目政策与工具](./oss) | QO / AL | 6 | LLVM、QEMU、Ghostty、curl、Mutahunter、Open Code Review |
| [中文互联网](./chinese) | QC / TX / AL / BD | 34 | 美团、阿里、腾讯、字节、快手、得物、百度、京东、手淘等；含按主题并入的测试、评审、评测条目 |
| [X 精选](./x) | QX | 39 | Boris Cherny、DHH、Addy Osmani、Matt Pocock、Simon Willison、Hamel Husain 等 |
| [Hacker News 讨论精选](./hn) | QH / AL | 17 | 包含明确的反对意见；含 Open Code Review 社区复测 |

## 证据类型标注 {#evidence-types}

- **团队自报**：公司工程博客或论文中关于自家实践的数字，未经独立验证。
- **厂商自报**：工具厂商谈自家产品，或销售相关产品的厂商发布的报告，标为「厂商自报、尚未独立验证」。
- **研究**：METR、DORA 与学术论文。
- **作者自述 / 个人观点 / 个人经验**：X 帖子与 HN 评论。

## 原则编号 {#principles}

Q01–Q13 的定义、代表来源和共识度见 [第 12 章](/handbook/12-quality-cicd#principles)。原有的 P01–P20 见 [共识度/佐证](/compare/evidence)。
