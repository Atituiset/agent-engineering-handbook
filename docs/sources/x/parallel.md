# X 精选 · 并行与长任务

> 23 条精选帖子，按发帖日期（UTC）排序。每条都有原帖链接；摘要忠于原文，引文为原帖逐字摘录。**作者自述**为个人经验，厂商员工谈自家产品时请视为**厂商自报**。原则标签为关键词自动归类，见 [共识度/佐证](/compare/evidence)。

[[toc]]

### XA-001 · 用 worktree 并行、用规格防止「死循环」 {#xa-001}
**作者**：Josh Lehman（@jlehman_）｜**日期**：2025-04-10｜[原帖](https://x.com/jlehman_/status/1910466216520819015)｜♥ 56

Josh Lehman 分享自 Claude Code 发布以来形成的工作流：大量使用 git worktree 并行推进多条工作流；用两步开发流程让工作始终以清晰的规格为依据，以缓解 LLM 的「doom loop」；并把整个流程自动化。作者自述。

> "Mitigate LLM "doom loops" through a a two-step development process that keeps work grounded in a clear specification"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P06](/compare/evidence#p06) [P08](/compare/evidence#p08) [P11](/compare/evidence#p11) [P13](/compare/evidence#p13)

### XA-002 · 同时开 5 个 Claude Code 实例，用 worktree 分头并行 {#xa-002}
**作者**：Alex Albert（@alexalbert__）｜**日期**：2025-04-15｜[原帖](https://x.com/alexalbert__/status/1912158994694898164)｜♥ 1356

Anthropic 的 Alex Albert 认为 Claude Code 最被低估的能力，是用 Git worktree 同时启动约 5 个实例，分别处理项目的不同部分，像在指挥一支软件工程师队伍。2025 年 4 月的较早实践。

> "spin up like 5 Claude Code instances at once using Git worktrees"

原则：[P11](/compare/evidence#p11)

### XA-003 · 同一提示跑多次，挑最好的实现合成 PR {#xa-003}
**作者**：Nick Khami（@skeptrune）｜**日期**：2025-05-26｜[原帖](https://x.com/skeptrune/status/1926831790041280867)｜♥ 17

Nick Khami 描述他一周的工作流：在 Cursor/Codex 中对同一提示运行多次（每次结果都不同），从并行实现中挑最好的合成最终 PR。他列出痛点：分不清会话从哪个分支分出、无法把同一提示同时发给多个智能体等。

> "picking the best of the parallel implementations to synthesize a final PR"

原则：[P08](/compare/evidence#p08) [P11](/compare/evidence#p11)

### XA-004 · 多个智能体并行实现同一功能，挑最好的合并 {#xa-004}
**作者**：Victor（@victor_explore）｜**日期**：2025-05-26｜[原帖](https://x.com/victor_explore/status/1927041085555052768)｜♥ 3

Victor 演示用 git worktree 为每个智能体创建隔离分支，在多个 Claude 实例上执行同一计划，并排比较不同 UI 实现，把最好的合并回主干，以此对冲模型在复杂任务上的失败。

> "Hedge against model failures on complex tasks"

原则：[P01](/compare/evidence#p01) [P11](/compare/evidence#p11) [P12](/compare/evidence#p12) [P17](/compare/evidence#p17)

### XA-005 · 同时跑三个 Claude Code：仍需大量规划、调整和人带入的上下文 {#xa-005}
**作者**：Brad（@BradButner）｜**日期**：2025-06-20｜[原帖](https://x.com/BradButner/status/1935911570904633381)｜♥ 0

Brad 在一整天同时用三个 Claude Code 处理三个项目后表示：在智能体拥有更好的长期记忆、能处理需求覆盖不全并提出正确问题之前，完全自主还很遥远；他仍要带入大量规划、调整、知识和上下文。

> "There was lots of planning, adjustment, knowledge, and context I had to bring in"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P10](/compare/evidence#p10) [P11](/compare/evidence#p11) [P17](/compare/evidence#p17) [P18](/compare/evidence#p18)

### XA-006 · 「并行」不等于更好 {#xa-006}
**作者**：Dave（@php100）｜**日期**：2025-07-07｜[原帖](https://x.com/php100/status/1942042631027966147)｜♥ 8

作者列出用 Claude Code 编排多智能体时遇到的问题：没有共享状态、多个智能体改同一文件导致 Git 冲突、上下文被之前的工作污染、一个失败就全盘失败。他的结论是并行并不意味着更好，一个编排良好的单智能体往往更可靠。这是对并行实践的反面意见。

> ""parallel" doesn't mean better"

原则：[P02](/compare/evidence#p02) [P10](/compare/evidence#p10) [P11](/compare/evidence#p11) [P12](/compare/evidence#p12)

### XA-007 · wt：让 git worktree 变得轻量、可丢弃 {#xa-007}
**作者**：Nick Rempel（@nbrempel）｜**日期**：2025-11-06｜[原帖](https://x.com/nbrempel/status/1986304770429337888)｜♥ 1

Nick Rempel 受 Conductor「每个智能体一个隔离工作区」理念启发，为终端用户写了 wt：一个 git worktree 的轻量包装，让 worktree 创建快速、用完即弃，便于在 Claude Code 和 Codex 中并行跑更多任务。

> "“one agent per isolated workspace”"

原则：[P02](/compare/evidence#p02) [P08](/compare/evidence#p08) [P11](/compare/evidence#p11) [P12](/compare/evidence#p12)

### XA-008 · 大规模迁移：让一个智能体派生多个只迁一个文件的小任务 {#xa-008}
**作者**：vogel（@ryanvogel）｜**日期**：2025-11-16｜[原帖](https://x.com/ryanvogel/status/1989851033724752352)｜♥ 15

vogel 用 Cursor 加 Claude Code 子智能体做较大的迁移：单个智能体容易分心，但如果让一个智能体派生多个任务极小的智能体（每个只迁移一个文件），效果更好。

> "A single agent can get distracted but if you have an agent spawn multiple agents with very small tasks"

原则：[P09](/compare/evidence#p09) [P10](/compare/evidence#p10) [P11](/compare/evidence#p11)

### XA-009 · 同时开 3–5 个 git worktree 并行跑 Claude {#xa-009}
**作者**：AgentBuff（@agentbuff_dev）｜**日期**：2026-03-03｜[原帖](https://x.com/agentbuff_dev/status/2028841337240396086)｜♥ 0

AgentBuff 转述 Claude Code 作者的技巧：同时启动 3–5 个 git worktree，每个运行独立的 Claude 会话，被团队视为最大的生产力提升；有人给 worktree 起名并设 shell 别名一键切换，有人专门留一个「分析」worktree 只看日志、跑查询。

> "同时启动 3–5 个 git worktree，每个 worktree 运行独立的 Claude 会话并行工作"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P04](/compare/evidence#p04) [P06](/compare/evidence#p06) [P08](/compare/evidence#p08) [P10](/compare/evidence#p10) [P11](/compare/evidence#p11) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13) [P14](/compare/evidence#p14) [P15](/compare/evidence#p15)

### XA-010 · Ralph Wiggum 技巧：把人从每一步的循环中移出 {#xa-010}
**作者**：Dr Milan Milanović（@milan_milanovic）｜**日期**：2026-03-31｜[原帖](https://x.com/milan_milanovic/status/2038866383191044427)｜♥ 17

Milan Milanović 解释 Geoffrey Huntley 在 2025 年中提出的 Ralph Wiggum 技巧：多数人逐步使用编码智能体——提示、评审、再提示、再评审，人始终在环；Ralph 用循环让智能体反复执行，去掉这个瓶颈。

> "Prompt, review, re-prompt, review. The human is always in the loop."

原则：[P08](/compare/evidence#p08) [P18](/compare/evidence#p18)

### XA-011 · Codex 当大脑和评审，Claude Code 执行，task.md 当共享记忆 {#xa-011}
**作者**：Kun Lei（@kunlei15）｜**日期**：2026-05-10｜[原帖](https://x.com/kunlei15/status/2053462727675498775)｜♥ 6

Kun Lei 分享心智模型：Codex 负责调试、评审、规划和高层决策，Claude Code 负责执行，task.md 作为共享记忆，git worktree 用于并行探索；复杂任务会先让两者各自出计划。作者自述的个人偏好。

> "task.md = shared memory"

原则：[P01](/compare/evidence#p01) [P08](/compare/evidence#p08) [P11](/compare/evidence#p11) [P18](/compare/evidence#p18)

### XA-012 · Boris Cherny 的头号建议：开 auto mode，同时跑多个 Claude {#xa-012}
**作者**：Boris Cherny（@bcherny）｜**日期**：2026-05-24｜[原帖](https://x.com/bcherny/status/2058519809214607704)｜♥ 4972

Boris Cherny 说他现在的头号建议是使用 auto mode：不再弹权限确认，这是「multi-clauding」的基础——启动一个会话，在它运行时并行处理另一个会话。厂商自报；与安全章节讨论的权限取舍相关。

> "It is the key building block for multi-clauding"

原则：[P11](/compare/evidence#p11) [P15](/compare/evidence#p15)

### XA-013 · 动态工作流：规划、扇出到大量子智能体、验证、迭代收敛 {#xa-013}
**作者**：Ado（@adocomplete）｜**日期**：2026-05-28｜[原帖](https://x.com/adocomplete/status/2060089787923784043)｜♥ 1316

Anthropic 的 Ado 介绍动态工作流：Claude 规划任务，扇出给数十到数百个并行子智能体，验证它们的工作，并迭代直到结果收敛为一个协调一致的答案。厂商自报。

> "verifies their work, and iterates until the results converge into one coordinated answer"

原则：[P06](/compare/evidence#p06) [P10](/compare/evidence#p10) [P11](/compare/evidence#p11)

### XA-014 · 动态工作流：先生成编排计划，再严格按计划执行 {#xa-014}
**作者**：cat（@_catwu）｜**日期**：2026-05-28｜[原帖](https://x.com/_catwu/status/2060054180379689074)｜♥ 7766

Claude Code 产品负责人 Cat Wu 介绍动态工作流：在提示中提到「workflow」，Claude 会动态生成编排计划并严格遵循，确保即使跨数百个智能体，每个阶段也按正确顺序进行。厂商自报。

> "Claude will dynamically create an orchestration plan that it strictly follows"

原则：[P01](/compare/evidence#p01)

### XA-015 · 43 分钟演示：worktree + 并行智能体的完整流程 {#xa-015}
**作者**：Avthar Sewrathan（@avthar）｜**日期**：2026-06-01｜[原帖](https://x.com/avthar/status/2061252916397163002)｜♥ 82

Avthar Sewrathan 发布多智能体 Claude Code 工作流的完整演示：准备、终端设置、git worktree、构建、多智能体技巧，以及合并与清理 worktree 的方法。帖中的「10 倍」为作者自述。

> "Featuring git worktrees, parallel agents, and Agent View."

原则：[P08](/compare/evidence#p08) [P10](/compare/evidence#p10) [P11](/compare/evidence#p11)

### XA-016 · 让 Opus 自主运行数小时到数天的五条建议 {#xa-016}
**作者**：Boris Cherny（@bcherny）｜**日期**：2026-06-08｜[原帖](https://x.com/bcherny/status/2063792263067754658)｜♥ 3468

Boris Cherny 给出长时间自主运行的建议：权限用 auto mode，避免反复请求批准；用动态工作流让 Claude 编排大量智能体；用 /goal 或 /loop 促使它持续推进直到完成；在云端运行 Claude Code，这样可以合上电脑；并确保 Claude 有办法自行验证结果。厂商自报。

> "Use /goal or /loop, to nudge Claude to keep going until it’s done"

原则：[P06](/compare/evidence#p06) [P14](/compare/evidence#p14) [P15](/compare/evidence#p15) [P18](/compare/evidence#p18)

### XA-017 · 在多个智能体和项目之间共享笔记与计划 {#xa-017}
**作者**：Ian Nuttall（@iannuttall）｜**日期**：2026-08-13｜[原帖](https://x.com/iannuttall/status/2087825738342998239)｜♥ 58

Ian Nuttall 重写了一个工具，在他使用的所有智能体和项目之间共享笔记和规划，这样可以让智能体「查看笔记，从上次停下的地方继续」，也能让另一个模型评审这些想法。作者自述，也是其自有工具。

> "check the notes in keep and pick up where we left off"

原则：[P01](/compare/evidence#p01) [P08](/compare/evidence#p08) [P18](/compare/evidence#p18)

### XA-018 · Orca：给每个编码智能体一条独立泳道 {#xa-018}
**作者**：Dan Kornas（@DanKornas）｜**日期**：2026-09-02｜[原帖](https://x.com/DanKornas/status/2095274056039739753)｜♥ 15

Dan Kornas 介绍开源的 Orca：让多个 CLI 编码智能体并排运行，每个放在隔离的 Git worktree 中，便于比较并行尝试而不混淆各自改动。

> "putting agents in isolated Git worktrees"

原则：[P08](/compare/evidence#p08) [P11](/compare/evidence#p11)

### XA-019 · 官方团队技巧：并行最提效，上下文爆满先查 /context {#xa-019}
**作者**：IvesFeng（@FengIves）｜**日期**：2026-10-20｜[原帖](https://x.com/FengIves/status/2112523509859823619)｜♥ 0

IvesFeng 摘要 Anthropic 公开的 Claude Code 团队效率技巧：并行是最大的提效来源（3–5 个会话加 git worktree），Plan mode 先规划后执行，配合 hooks 与定时任务；一条反直觉建议是上下文爆满时先用 /context 查看内容，别急着怪模型。二手摘要。

> "上下文爆满先查 /context，别怪模型"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P11](/compare/evidence#p11) [P12](/compare/evidence#p12)

### XA-020 · Anthropic 拆解智能体记忆：边干边记，再靠「做梦」整理 {#xa-020}
**作者**：宝玉（@dotey）｜**日期**：2026-11-08｜[原帖](https://x.com/dotey/status/2119269064543445168)｜♥ 240

宝玉转述 Anthropic 工程文章：难点在于 Claude 必须当下决定什么值得记。他们加入名为「做梦」的后台步骤，会话结束后回看原始记录、修正记错的笔记并重新整理。文中给出新旧模型使用记忆的对比数据，均为厂商自报。

> "会话结束后，让 Claude 回头翻原始对话记录，改掉记错的笔记"

原则：[P01](/compare/evidence#p01) [P02](/compare/evidence#p02) [P06](/compare/evidence#p06) [P11](/compare/evidence#p11) [P16](/compare/evidence#p16) [P18](/compare/evidence#p18) [P19](/compare/evidence#p19)

### XA-021 · 新一代模型能承担大量并行工作，前提是云端沙箱 {#xa-021}
**作者**：Guillermo Rauch（@rauchg）｜**日期**：2026-11-09｜[原帖](https://x.com/rauchg/status/2119878364794372162)｜♥ 2257

Vercel CEO Guillermo Rauch 在试用新模型后称，这一代模型能承担前所未有规模的并行工作；要用好它需要云端沙箱，因为模型能委派和编排的任务远超一台电脑的承载能力。厂商自报，且 Vercel 本身提供沙箱产品。

> "To actually seize this intelligence, you need cloud sandboxes."

原则：[P06](/compare/evidence#p06) [P11](/compare/evidence#p11) [P13](/compare/evidence#p13) [P15](/compare/evidence#p15) [P18](/compare/evidence#p18)

### XA-022 · Devin bots：多智能体团队的做法 {#xa-022}
**作者**：swyx（@swyx）｜**日期**：2026-11-17｜[原帖](https://x.com/swyx/status/2122746401482592549)｜♥ 340

swyx 转述 Walden Yan 在 AIE 的预告：Devin bots 常驻且主动（按 ROI 调节），对结果而非任务负责，管理子智能体团队并自我审查，用交互式产物而非长对话汇报进度。厂商预告，尚无公开效果数据。

> "manages teams of subagents (and reviews itself)"

原则：[P05](/compare/evidence#p05) [P08](/compare/evidence#p08) [P10](/compare/evidence#p10) [P11](/compare/evidence#p11)

### XA-023 · 智能体集群是下一个扩展维度 {#xa-023}
**作者**：Amjad Masad（@amasad）｜**日期**：2026-11-17｜[原帖](https://x.com/amasad/status/2122809964649459861)｜♥ 140

Amjad Masad 认为除了训练更大的模型、给更多思考时间之外，另一个扩展维度是并行运行大量智能体：探索不同方案、相互挑战、协作解决单个智能体做不到的问题。厂商观点。

> "Agent swarms are the next scaling frontier for AI."

原则：[P11](/compare/evidence#p11)
