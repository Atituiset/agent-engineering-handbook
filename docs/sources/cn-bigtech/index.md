# 国内大厂专题：说明与索引

> 这个专题回答：**腾讯、阿里、字节这三家，怎样把大模型和编码智能体用进软件工程？** 范围包括 AI 编码工具的规模化推广、Harness/Loop 工程、规范驱动（Spec/SDD）、AI 代码评审、测试智能体与 CI/CD、沙箱与执行环境、Agent 评测，以及他们自己承认的问题。横向比较与结论见 [国内大厂对比](/compare/cn-bigtech)。

## 规模 {#stats}

| 公司 | 精选条目 | 全量库新增 | 精选页 | 全量库页 |
| --- | --- | --- | --- | --- |
| 腾讯 | 23（TX） | 72 | [腾讯](./tencent) | [全量 · 腾讯](/library/cn-bigtech-tencent) |
| 阿里（含蚂蚁） | 31（AL） | 145（另有 1 条此前已收录，补了精选链接） | [阿里](./alibaba) | [全量 · 阿里](/library/cn-bigtech-alibaba) |
| 字节 | 20（BD） | 74 | [字节](./bytedance) | [全量 · 字节](/library/cn-bigtech-bytedance) |
| 合计 | **74** | **291** | | |

- 全量库新增的 291 条里：精选 73 条（另 1 条精选与已收录链接重复）、会议议题与中文网页 79 条、英文网页 8 条、GitHub 仓库 104 个、X 帖子 24 条、HN 讨论 3 个。在 [在线筛选](/library/#explorer) 的「全部专题」里可选「国内大厂」或单家公司；CSV/JSON 的 `topic` 为 `cn-bigtech`，`co`/`company` 为公司。
- **与已有条目不重复**：此前已收录的 [CN03](/sources/chinese#cn03)（蚂蚁数科 Harness）、[CN08](/sources/chinese#cn08)（TRAE 手册）、[CN09](/sources/chinese#cn09)/[CN13](/sources/chinese#cn13)（CodeBuddy）、[CN10](/sources/chinese#cn10)/[CN14](/sources/chinese#cn14)（Qoder）、[CN18](/sources/chinese#cn18)/[CN19](/sources/chinese#cn19)/[CN22](/sources/chinese#cn22)（腾讯）、[CN20](/sources/chinese#cn20)/[CN21](/sources/chinese#cn21)（LoopForge）、[CN25](/sources/chinese#cn25)/[CN26](/sources/chinese#cn26)/[CN32](/sources/chinese#cn32)（Trae/MarsCode）、[CN38](/sources/chinese#cn38)（蚂蚁 Vibe Coding 平台），以及质量专题的 [QC05](/sources/quality/chinese#qc05)（阿里 AI 评审）、[QC06](/sources/quality/chinese#qc06)/[QC07](/sources/quality/chinese#qc07)（腾讯 AICR）、[QC09](/sources/quality/chinese#qc09)（BitsAI-CR）、[QC10](/sources/quality/chinese#qc10)（手淘 TEKO）、[QC11](/sources/quality/chinese#qc11)（查杀分离）都没有重复写；同一内容的会议页、转载页也没有再做精选。
- 检索与核对时间：2026-11 中旬（北京时间）。

## 收录与核对规则 {#rules}

- **引文逐字核对**：每条精选的引文都与抓取到的页面正文做过去空白后的逐字比对（脚本校验，74/74 通过）；英文保留原文。
- **核对作者归属**：腾讯云开发者社区、阿里云开发者社区、火山引擎开发者社区都允许个人投稿。精选只收官方账号或文中明确标明团队的文章；个人投稿只进全量库，并在「热度/备注」栏标注（如「社区个人文章」「TRAE 用户投稿」）。
- **证据类型**（见每条末尾）：
  - **团队自报**：公司官方文章、发布稿、论文里关于自家实践的数字，**尚未独立验证**；
  - **高管口述（媒体采访）**：媒体转述负责人的说法；
  - **议题摘要（演讲者自述）**：QCon/AICon 议题页只有摘要和提纲，不等于演讲全文；标「尚未开讲」的是 2026-12 AICon 北京的预告；
  - **论文（工业部署，团队自报）**：作者来自该公司的论文，部署数据同样是自报；
  - **转载**：原文不可直接访问时引用转载页，并注明原始出处；
  - **第三方独立复测 / 分析**：非该公司的人做的测试或分析，样本通常很小，但很重要。
- **口径不一致要当心**：「AI 辅助生成的新增代码占比」「AI 生成代码占比」「AI 代码贡献率」「补全采纳率」「AI 代码合入率」是不同指标，各家甚至同一家不同年份的口径都不一样，不能直接横比。

## 缺口 {#gaps}

- **抓不到或不完整**：ACM 数字图书馆（TestGPT-Server 全文，403，改用会议页摘要）、CSDN（521）、trae.ai 博客与 Seed 中文博客（JS 渲染，正文为空）、掘金、InfoQ 写作社区、虎嗅；InfoQ 新闻「TRAE 月活已超百万」只抓到标题（只进全量库）。
- **公众号原文**：不少一手文章首发在微信公众号，部分只能通过腾讯新闻、网易号、技术栈、BestBlogs 摘录页等转载访问；已在条目里注明。阿里云 Loop Engineering 一文的原文发布在「阿里云开发者」公众号，本页引用的是转载。
- **归属未完全确认**：NL2Test 论文把公司匿名为“一家大型面向消费者的互联网公司”，归属依据是字节跳动技术团队公众号的同名文章；ScaleSWE、AIO Sandbox 等只进全量库。
- **X 检索受限**：X 搜索每次只返回少量帖子，本轮只收到 24 条相关帖子；「字节全面禁止个人使用 Claude Code / Codex」等说法只是 X 上的传闻，**未经核实**，正文没有采用。
- **三家材料不均衡**：字节的一手工程博客较少，更多是论文与开源；腾讯以官方号长文为主；阿里（含蚂蚁）会议议题最多。会议议题只能说明“他们说在做什么”，不能说明效果。
