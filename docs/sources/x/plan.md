# X 精选 · 计划与规格

> 8 条精选帖子，按发帖日期（UTC）排序。每条都有原帖链接；摘要忠于原文，引文为原帖逐字摘录。**作者自述**为个人经验，厂商员工谈自家产品时请视为**厂商自报**。原则标签为关键词自动归类，见 [共识度/佐证](/compare/evidence)。

[[toc]]

### XP-001 · 怎样让 Claude Code 写出最好的计划？ {#xp-001}
**作者**：Dan Shipper（@danshipper）｜**日期**：2025-07-09｜[原帖](https://x.com/danshipper/status/1943020541687795772)｜♥ 47

Dan Shipper 提出两种做法并在团队中做实验：让 Claude 写计划、存成文件、评审后修改；或者让 Claude 启动 3 个子智能体各写一份计划，再评审综合。

> "how do you make Claude Code create the best plan?"

原则：[P01](/compare/evidence#p01) [P08](/compare/evidence#p08) [P10](/compare/evidence#p10)

### XP-002 · Speckit-Ralph：把规格驱动开发变成自动迭代循环 {#xp-002}
**作者**：merlin（@merlinonthemoon）｜**日期**：2026-01-16｜[原帖](https://x.com/merlinonthemoon/status/2012299910658380074)｜♥ 0

merlin 把 GitHub spec-kit 与 Ralph Wiggum「永不放弃」循环结合：从规格中提取任务，用 Claude Code 或 Codex 自动迭代实现。他认为 Ralph 循环配合这种规格框架特别有效。作者自述的自有项目。

> "It turns Spec-Driven Development into an automated iteration engine"

原则：[P01](/compare/evidence#p01) [P16](/compare/evidence#p16) [P18](/compare/evidence#p18)

### XP-003 · 以前花 45 分钟撤销没要求的改动，直到用 Plan Mode {#xp-003}
**作者**：Michael / slashdev.io（@slashdevhq）｜**日期**：2026-01-28｜[原帖](https://x.com/slashdevhq/status/2016612964829196396)｜♥ 0

作者说过去让 Claude 直接做功能，之后要花 45 分钟撤销自己没要求的改动；用了 Plan Mode 后，流程变成先计划、把架构定好，再执行。作者自述。

> "Now my workflow: Plan Mode first, get the architecture perfect, then execute."

原则：[P01](/compare/evidence#p01) [P05](/compare/evidence#p05) [P17](/compare/evidence#p17)

### XP-004 · Claude 做规划与架构、Codex 执行、Claude 冒烟测试 {#xp-004}
**作者**：Amit Bhatia（@amitbhatia_）｜**日期**：2026-04-10｜[原帖](https://x.com/amitbhatia_/status/2042682666336817533)｜♥ 11

Amit Bhatia 分享用 compound engineering 插件开发一个平台的分工：Claude Code 加 compound engineering 负责规划和架构，Codex 负责执行，Claude 负责冒烟测试与部署。体现「规划与执行分离、跨模型分工」。作者自述。

> "claude code + compound engineering for planning and architecture"

原则：[P01](/compare/evidence#p01) [P05](/compare/evidence#p05) [P06](/compare/evidence#p06) [P13](/compare/evidence#p13) [P19](/compare/evidence#p19)

### XP-005 · Boris Cherny：为什么我现在用 auto mode 而不是 plan mode {#xp-005}
**作者**：Boris Cherny（@bcherny）｜**日期**：2026-06-08｜[原帖](https://x.com/bcherny/status/2064034799711588805)｜♥ 2188

Boris Cherny 与 Cat Wu 在 Claude Code GA 一周年时对谈，话题包括他为什么现在用 auto mode 而不是 plan mode、定时任务如何在他看到之前修复 bug、以及为何大部分编码在手机上完成。这表明「计划先行」在强模型和熟练用户那里有弱化的趋势，属于对 P01 的修正性意见。

> "why I use auto mode instead of plan mode"

原则：[P01](/compare/evidence#p01)

### XP-006 · 计划模式很好，但如果你全盘接受默认建议，还不如不计划 {#xp-006}
**作者**：Burke Holland（@burkeholland）｜**日期**：2026-06-19｜[原帖](https://x.com/burkeholland/status/2068040807177736240)｜♥ 63

GitHub Copilot 团队的 Burke Holland 提醒：如果只是接受智能体计划中的所有默认建议，计划这一步等于白做；计划的价值在于人投入思考、做出判断。

> "You gotta engage your brain."

原则：[P01](/compare/evidence#p01) [P15](/compare/evidence#p15)

### XP-007 · 很多人自己做计划，并不需要 plan mode {#xp-007}
**作者**：Thariq（@trq212）｜**日期**：2026-09-24｜[原帖](https://x.com/trq212/status/2103212051065921632)｜♥ 2167

Claude Code 团队的 Thariq 回应反馈：很多用户自己做规划，不需要 plan mode；另一些人则喜欢进入一个让 Claude 只思考、与你头脑风暴的模式。他计划把 plan mode 改为内置模组，并允许用户自定义模式。说明「计划先行」是原则，plan mode 只是实现方式之一。

> "many of you are planning yourself & don't need plan mode"

原则：[P01](/compare/evidence#p01)

### XP-008 · 更好的 HTML 计划：简单语言、代码片段、提出问题、带原型 {#xp-008}
**作者**：Thariq（@trq212）｜**日期**：2026-10-05｜[原帖](https://x.com/trq212/status/2107192901537329354)｜♥ 4717

Thariq 在开发一个让 Claude Code 生成更好 HTML 计划的 skill：使用简单语言，展示代码片段，主动提出问题并做出界面原型；用 lint 减少 Claude 常见的失败情况。厂商实验。

> "Linting reduces the normal failure cases that Claude runs into."

原则：[P04](/compare/evidence#p04) [P13](/compare/evidence#p13)
