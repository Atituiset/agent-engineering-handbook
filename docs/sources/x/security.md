# X 精选 · 安全与权限

> 10 条精选帖子，按发帖日期（UTC）排序。每条都有原帖链接；摘要忠于原文，引文为原帖逐字摘录。**作者自述**为个人经验，厂商员工谈自家产品时请视为**厂商自报**。原则标签为关键词自动归类，见 [共识度/佐证](/compare/evidence)。

[[toc]]

### XS-001 · 把私人数据交给 40 万行 vibe coding 代码？ {#xs-001}
**作者**：Andrej Karpathy（@karpathy）｜**日期**：2026-02-20｜[原帖](https://x.com/karpathy/status/2024987174077432126)｜♥ 17317

Karpathy 买了 Mac mini 准备试玩 claws 类智能体，但对运行 OpenClaw 心存疑虑：把私人数据和密钥交给一个「40 万行 vibe coded」、正被大规模攻击的项目并不吸引人，他已看到实例暴露和 RCE 漏洞的报道。

> "giving my private data/keys to 400K lines of vibe coded monster"

原则：[P02](/compare/evidence#p02) [P05](/compare/evidence#p05) [P13](/compare/evidence#p13) [P15](/compare/evidence#p15) [P16](/compare/evidence#p16)

### XS-002 · --dangerously-skip-permissions 很快，也是负债 {#xs-002}
**作者**：Daniel Vermillion（@dxverm）｜**日期**：2026-06-22｜[原帖](https://x.com/dxverm/status/2069042900537635015)｜♥ 0

Daniel Vermillion 承认自己用跳过权限模式运行 Claude Code，并列举公开流传的事故：智能体无视权限拒绝删除文件、Replit 智能体在代码冻结期间清空生产数据库、一个反斜杠导致删除整个 Windows 安装。他总结共同点是 YOLO 模式加一条本该被拦下的命令。事故为作者转述。

> "The common thread is YOLO mode plus one command that should"

原则：[P02](/compare/evidence#p02) [P06](/compare/evidence#p06) [P12](/compare/evidence#p12) [P15](/compare/evidence#p15) [P17](/compare/evidence#p17)

### XS-003 · Codex Security Review：在 PR 中做安全审查 {#xs-003}
**作者**：OpenAI Developers（@OpenAIDevs）｜**日期**：2026-08-06｜[原帖](https://x.com/OpenAIDevs/status/2085482310636560830)｜♥ 1493

OpenAI 发布研究预览版 Codex Security Review：利用仓库上下文深入检查 GitHub PR 中的安全问题，并在 PR 中直接给出可操作的发现，可设置为自动审查。厂商公告。

> "using repository context to surface actionable findings directly in the PR"

原则：[P02](/compare/evidence#p02) [P08](/compare/evidence#p08)

### XS-004 · Codex 为每个 PR 做安全审查 {#xs-004}
**作者**：Greg Brockman（@gdb）｜**日期**：2026-08-06｜[原帖](https://x.com/gdb/status/2085496677725860064)｜♥ 1376

OpenAI 总裁 Greg Brockman 宣布 Codex 可以对每个 GitHub PR 做安全审查并内联给出发现，这是利用模型提升代码与企业安全的整体计划的一部分。厂商公告。

> "Codex can now perform a security review of every GitHub pull request, leaving findings inline."

原则：[P08](/compare/evidence#p08)

### XS-005 · 叠加多层防护，间接提示注入在未见攻击上接近 0 {#xs-005}
**作者**：Boris Cherny（@bcherny）｜**日期**：2026-08-07｜[原帖](https://x.com/bcherny/status/2085860677990883454)｜♥ 2847

Boris Cherny 称叠加多层（模型训练、输入探针、检查意图的分类器）后，间接提示注入在未见过的攻击上可降到接近 0，并宣布 auto mode 将成为 Claude Code 默认。厂商自报，数据来自其发布的报告。

> "you can get indirect prompt injection to ~0 on unseen attacks if you stack enough layers"

原则：[P05](/compare/evidence#p05) [P15](/compare/evidence#p15)

### XS-006 · 把危险命令藏进真实会话：人工评审只抓到 13.6% {#xs-006}
**作者**：Ado（@adocomplete）｜**日期**：2026-08-13｜[原帖](https://x.com/adocomplete/status/2087957562859913525)｜♥ 124

Anthropic 的 Ado 介绍一项实验：在真实编码会话中藏入危险命令，让 1053 名专业开发者评审，人工只发现 13.6%，auto mode 发现 89%；随后 auto mode 成为 Pro、Max、Team 套餐的默认权限模式。厂商自报，实验设计细节见其原文。它说明「逐条人工批准」并不是可靠的安全措施。

> "Humans caught 13.6%"

原则：[P08](/compare/evidence#p08) [P15](/compare/evidence#p15)

### XS-007 · 模型发现沙箱跑不了，没问就自己写 CI 工作流推到 GitHub {#xs-007}
**作者**：Simon Willison（@simonw）｜**日期**：2026-08-20｜[原帖](https://x.com/simonw/status/2090299859693695283)｜♥ 294

Simon Willison 让云端 Claude Code 试验一个代码执行沙箱；模型发现环境不支持（没有 /dev/kvm），于是没有先询问他，就自己写了一个 GitHub Actions 工作流并直接推送到 GitHub 去跑实验。这是智能体「过度主动」越出预期边界的真实例子。

> "without asking me first, it wrote a GitHub Actions workflow to run the experiments and pushed that directly to GitHub instead!"

原则：[P15](/compare/evidence#p15)

### XS-008 · Codex Auto-review：用第二个智能体审查高风险动作 {#xs-008}
**作者**：Tibo（@thsottiaux）｜**日期**：2026-10-06｜[原帖](https://x.com/thsottiaux/status/2107368734981517634)｜♥ 12142

OpenAI Codex 负责人 Tibo 宣布 Auto-review 对 ChatGPT 登录用户免费。他说默认沙箱要求逐项批准，容易造成「决策疲劳」，除非花大量时间配置规则；Auto-review 让第二个智能体审查主智能体的所有动作，唯一目标是阻止高风险操作，从而能放心跑长任务。厂商自报。

> "which is prone to decision fatigue unless you spend a lot of time configuring specific rules"

原则：[P01](/compare/evidence#p01) [P08](/compare/evidence#p08) [P15](/compare/evidence#p15) [P17](/compare/evidence#p17)

### XS-009 · 给编码智能体接入上下文工具，与防数据外泄之间的平衡 {#xs-009}
**作者**：dex（@dexhorthy）｜**日期**：2026-10-14｜[原帖](https://x.com/dexhorthy/status/2110430733009600654)｜♥ 129

dex 回忆与一位大型企业 CISO 的讨论：如何在给开发者提供让编码智能体更有用的工具（连接工单、邮件、Slack 等 MCP）的同时，防止数据外泄、提示注入和凭据劫持。

> "while avoiding data exfiltration, prompt injection, credential hij"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P14](/compare/evidence#p14) [P15](/compare/evidence#p15)

### XS-010 · 外部沙箱模式：智能体跑在本机，代码在沙箱里执行 {#xs-010}
**作者**：Simon Willison（@simonw）｜**日期**：2026-11-17｜[原帖](https://x.com/simonw/status/2122500307557265651)｜♥ 1217

Simon Willison 探索为编码智能体写出的代码做沙箱隔离的新方式，描述「外部沙箱」模式：智能体在 Mac 上运行，但代码在 WebAssembly、QEMU 或 Apple Container 沙箱中执行，并给出 Claude Code、Codex 和 Pi 的演示。

> "agents run on your Mac but execute code in a WebAssembly or QEMU or Apple Container sandbox"

原则：[P15](/compare/evidence#p15)
