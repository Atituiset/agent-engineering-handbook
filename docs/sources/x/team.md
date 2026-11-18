# X 精选 · 团队、成本与组织

> 21 条精选帖子，按发帖日期（UTC）排序。每条都有原帖链接；摘要忠于原文，引文为原帖逐字摘录。**作者自述**为个人经验，厂商员工谈自家产品时请视为**厂商自报**。原则标签为关键词自动归类，见 [共识度/佐证](/compare/evidence)。

[[toc]]

### XM-001 · Claude Code 的消耗：一个月 3600 多美元 {#xm-001}
**作者**：Ky Tomita（@kylantomita）｜**日期**：2025-07-22｜[原帖](https://x.com/kylantomita/status/1947493414167273519)｜♥ 0

Ky Tomita 公开自己的 Claude Code 消耗：单日约 230 美元，当月约 3640 美元（实际工作约两周半），并按额度窗口安排作息。个人自述，反映重度使用下的成本量级（按 API 计价换算）。

> "my Claude Code burn rate is getting absurd"

原则：[P01](/compare/evidence#p01) [P05](/compare/evidence#p05) [P10](/compare/evidence#p10) [P11](/compare/evidence#p11) [P17](/compare/evidence#p17)

### XM-002 · 「2026 年的生产力恐慌」：工具省下的时间变成了更高的期望 {#xm-002}
**作者**：Architect Aliy（@architect_aliy）｜**日期**：2026-03-06｜[原帖](https://x.com/architect_aliy/status/2029761556045590758)｜♥ 1

作者引用彭博社「The Great Productivity Panic of 2026」的说法：编码智能体本应解放工程师，但公司反而提高了要求，期待更短的开发周期和更高产出。属转述与评论。

> "The tool that was supposed to give you afternoons off gave your manager a reason to expect more."

原则：[P05](/compare/evidence#p05) [P16](/compare/evidence#p16)

### XM-003 · Codex 自动给 PR 标题加 [codex] 前缀引发不满 {#xm-003}
**作者**：Onur Solmaz（@onusoz）｜**日期**：2026-04-05｜[原帖](https://x.com/onusoz/status/2040761244697641250)｜♥ 32

Onur Solmaz 抱怨 Codex 自动安装的 GitHub skill 会在每个 PR 标题前加上 [codex]，类似 Claude 把自己加为共同提交者，他认为这是「游击营销」；而且相关仓库不接受组织外的 PR，他无法提交修改。这提醒团队审视智能体默认写进提交与 PR 的内容。

> "now causes it to prepend [codex] to each PR title"

原则：[P03](/compare/evidence#p03) [P08](/compare/evidence#p08) [P13](/compare/evidence#p13) [P19](/compare/evidence#p19)

### XM-004 · /insights：让 Claude 分析你的用法并建议更新 CLAUDE.md、hooks、skills {#xm-004}
**作者**：Taylor Poindexter（@engineering_bae）｜**日期**：2026-04-10｜[原帖](https://x.com/engineering_bae/status/2042687351978356916)｜♥ 57

Taylor Poindexter 推荐 Claude Code 的 /insights 命令：分析你的使用方式，建议更新 CLAUDE.md、增加 hooks 和 skills，并给出提示建议。这是工具层面支持「从使用中沉淀规则」。

> "suggested updates to my CLAUDE.md files, suggested hooks and skills"

原则：[P03](/compare/evidence#p03) [P12](/compare/evidence#p12) [P13](/compare/evidence#p13)

### XM-005 · Ethan Mollick：关于自主编码工具的生产力，我们几乎没有好的研究 {#xm-005}
**作者**：Ethan Mollick（@emollick）｜**日期**：2026-05-26｜[原帖](https://x.com/emollick/status/2059118330472972331)｜♥ 685

Ethan Mollick 指出，据他所知，对 2025 年 12 月以来出现的自主编码工具，还没有好的生产力影响研究；现有论文都早于 Claude Code/Codex 的这波变化。这是理解本手册证据强度时的重要提醒。

> "We have, as far as I can tell, no good tests of the productivity impact of the autonomous coding tools"

原则：[P06](/compare/evidence#p06)

### XM-006 · Salesforce 的智能体化迁移：估 231 天，13 天交付 {#xm-006}
**作者**：Boris Cherny（@bcherny）｜**日期**：2026-05-29｜[原帖](https://x.com/bcherny/status/2060390852619272526)｜♥ 3680

Boris Cherny 转述 Salesforce 关于全面采用 Claude Code 的文章：一个原估 231 天的迁移 13 天完成，一个 PR 交付 21 个端点且测试覆盖率 100%。厂商转述的客户案例，原文细节需查阅 Salesforce 文章。

> "A migration they'd scoped at 231 days shipped in 13."

原则：[P06](/compare/evidence#p06) [P08](/compare/evidence#p08)

### XM-007 · Thrifty：强模型规划、便宜模型执行、关卡验证 {#xm-007}
**作者**：harper 🤯（@harper）｜**日期**：2026-06-09｜[原帖](https://x.com/harper/status/2064456570251919810)｜♥ 19

harper 团队为 Claude Code 做了一个控制成本的 skill，思路是更好的分工：强模型做计划，便宜模型执行，由关卡（gate）验证结果。作者自有项目。

> "strong model plans → cheap model executes → gate verifies"

原则：[P06](/compare/evidence#p06) [P13](/compare/evidence#p13) [P17](/compare/evidence#p17)

### XM-008 · Replit「自动驾驶公司」：代码产出近三倍，评审时间持平 {#xm-008}
**作者**：Amjad Masad（@amasad）｜**日期**：2026-07-16｜[原帖](https://x.com/amasad/status/2077802290304684404)｜♥ 2783

Replit CEO Amjad Masad 撰文称，过去六个月 Replit 工程师的代码产出接近三倍，评审时间保持不变，回滚与线上事故持平，质量指标改善，发布加快。数据为厂商自报，未给出公开的度量方法。

> "engineers at Replit have nearly tripled code output. Review times held steady."

原则：[P02](/compare/evidence#p02) [P08](/compare/evidence#p08) [P11](/compare/evidence#p11) [P16](/compare/evidence#p16)

### XM-009 · 5 个省 token 的实测技巧 {#xm-009}
**作者**：婷（@shijianzhongg）｜**日期**：2026-07-16｜[原帖](https://x.com/shijianzhongg/status/2077566980719309178)｜♥ 0

作者分享省 token 方法：把项目背景、技术栈、命名规范写进 AGENTS.md 或 CLAUDE.md，不必每次重复；要求回复简洁、不要客套和分析过程等。帖中节省数字为作者自估。

> "用 AGENTS.md 代替每次重复"

原则：[P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P06](/compare/evidence#p06) [P10](/compare/evidence#p10) [P11](/compare/evidence#p11) [P14](/compare/evidence#p14) [P17](/compare/evidence#p17)

### XM-010 · 写代码变便宜后，稀缺的是「把判断固化下来」 {#xm-010}
**作者**：matokulay（@matokulay）｜**日期**：2026-07-16｜[原帖](https://x.com/matokulay/status/2077710839243846127)｜♥ 0

作者看到有人把高手习惯做成 agent skill：哪些检查不能省、哪些坑要提前绕、生成后怎么验。他认为过去靠师傅带、review 和踩坑积累的经验，今后会变成可安装的工作流，反复交给 Codex/Claude Code 执行。

> "AI 让写代码变便宜后，稀缺的会是“把判断固化下来”。"

原则：[P08](/compare/evidence#p08) [P13](/compare/evidence#p13)

### XM-011 · 智能体会话记录是金矿：归档、复盘、脱敏 {#xm-011}
**作者**：dfkai（@joinlearn_com）｜**日期**：2026-10-02｜[原帖](https://x.com/joinlearn_com/status/2106030128216060157)｜♥ 0

作者建议保存智能体会话：按项目归档导出的会话记录；每周挑出关键会话，标注成功路径和踩坑点，整理成团队可搜索的笔记；敏感内容脱敏后再存。他认为不存会话就是把最好的工作流样本扔掉。帖中引用的厂商做法为转述。

> "每周挑关键会话，标出成功路径和踩坑点，做成团队可搜的笔记"

原则：[P02](/compare/evidence#p02)

### XM-012 · EvoSkill：把执行经验系统化地变成可复用 skill {#xm-012}
**作者**：Slatro（@slatro_eth）｜**日期**：2026-10-02｜[原帖](https://x.com/slatro_eth/status/2105977047818362985)｜♥ 44

作者介绍 EvoSkill：分析智能体执行记录，生成 skill 和提示词修改，在留出的验证任务上评估，表现更好的修改被带入下一轮迭代，全程无需重新训练模型。这是「把错误沉淀为规则」的自动化版本，评估结论来自项目方。

> "evaluates the resulting agent programs on held-out validation tasks"

原则：[P13](/compare/evidence#p13) [P19](/compare/evidence#p19)

### XM-013 · Anthropic 自建版本控制系统：代码变更越来越自主时的思路 {#xm-013}
**作者**：dex（@dexhorthy）｜**日期**：2026-10-13｜[原帖](https://x.com/dexhorthy/status/2110080282279719187)｜♥ 899

HumanLayer 的 dex 评论 Anthropic 自建的版本控制系统：Git 的设计让任何客户端都能离线服务仓库，开发期工具不处在运行期部署的关键路径上；而新系统不支持离线。他认为如果接受「改代码会越来越自主、越来越快」，这种取舍就说得通。属个人解读。

> "if you buy that changing code happens more and more autonomously"

原则：[P08](/compare/evidence#p08) [P20](/compare/evidence#p20)

### XM-014 · 别让每次会话从零开始：建立从错误中学习的记忆 {#xm-014}
**作者**：MAIL（@RealMarvelX）｜**日期**：2026-10-14｜[原帖](https://x.com/RealMarvelX/status/2110329130780623247)｜♥ 8

作者指出多数人反复纠正同样的错误、重复同样的指令和偏好；建议给 AI 编码智能体一个记录「哪里错了、什么有效、下次怎么做」的机制，使工作流随时间改进。

> "stop starting every AI coding session from zero"

原则：[P03](/compare/evidence#p03) [P05](/compare/evidence#p05) [P08](/compare/evidence#p08) [P18](/compare/evidence#p18)

### XM-015 · 让智能体学到的团队规则可审查、可版本化 {#xm-015}
**作者**：Dan Kornas（@DanKornas）｜**日期**：2026-10-18｜[原帖](https://x.com/DanKornas/status/2111615485053661420)｜♥ 14

Dan Kornas 介绍开源项目 Evolving Agents：从 CLAUDE.md 和项目记忆中学习团队工作规则，把指令编译成小的关联语句，并把每条被接受的经验记录为带版本的补丁，使「智能体学到了什么」可检查。

> "recording each accepted lesson as a versioned patch"

原则：[P01](/compare/evidence#p01) [P03](/compare/evidence#p03) [P18](/compare/evidence#p18)

### XM-016 · 额度烧得太快：每任务新会话、写 handoff.md、关掉不用的 MCP {#xm-016}
**作者**：Dmytro Neriom 🎲（@000xdi）｜**日期**：2026-10-31｜[原帖](https://x.com/000xdi/status/2116490946896433438)｜♥ 2

作者给出省额度技巧：每个任务开新会话；每步后 /compact；写 handoff.md 后重新开始；用 /context 看什么在吃 token；关闭不用的 MCP 服务器；提示里点名具体文件和函数，而不是说「那段代码」。

> "write handoff.md, start fresh"

原则：[P02](/compare/evidence#p02) [P14](/compare/evidence#p14) [P18](/compare/evidence#p18)

### XM-017 · 智能体时代，难相处的人会更难 {#xm-017}
**作者**：DHH（@dhh）｜**日期**：2026-11-02｜[原帖](https://x.com/dhh/status/2117241303704432901)｜♥ 7440

DHH 认为智能体时代对大多数程序员很好，但对脾气古怪的人会很艰难：专门知识和稀有技能不再能让难相处的人免于后果，最好学点基本的人际技能。

> "Specialized knowledge and rare skills will no longer offer immunity for those who are a pain to work with."

原则：[P13](/compare/evidence#p13)

### XM-018 · AI Coding 面试：工具使用边界模糊 {#xm-018}
**作者**：宝玉（@dotey）｜**日期**：2026-11-10｜[原帖](https://x.com/dotey/status/2120064894376558646)｜♥ 547

宝玉转述 Reddit 上一位候选人的大厂「AI 代码库面试」经历：在陌生的大型 Django 代码库上限时完成功能，面试官没有说明允许用多少 AI；他用 planning mode 和 ask mode 逐个推进，通过了部分测试仍被拒，并指出 AI 辅助需要阅读大量生成内容。二手转述。

> "关于 AI 工具的使用边界非常模糊。"

原则：[P01](/compare/evidence#p01) [P05](/compare/evidence#p05) [P06](/compare/evidence#p06)

### XM-019 · 把两周踩坑做成开源 Skill，别人少走弯路 {#xm-019}
**作者**：铁锤人（@lxfater）｜**日期**：2026-11-15｜[原帖](https://x.com/lxfater/status/2121947751743205383)｜♥ 18

铁锤人介绍有人把两周的 AI 视频创作踩坑经验做成开源 Skill：包含镜头块、招式表、踩坑表和提交前的检查脚本，装进 Claude Code/Codex 就能照这些经验工作。他认为 Skills 最值得做的就是这种经验沉淀。

> "一个人花两周试出来的东西，别人下次做同样的事，就能少走一段弯路。"

原则：[P13](/compare/evidence#p13)

### XM-020 · 用好新模型的缓存：稳定前缀放前面，历史只追加 {#xm-020}
**作者**：鸡骑猫（@mspd4100）｜**日期**：2026-11-18｜[原帖](https://x.com/mspd4100/status/2122986811400352080)｜♥ 37

鸡骑猫整理 OpenAI 迁移文档与开发者反馈：稳定的系统指令应放进 input 的第一条 developer 消息，否则缓存可能失效、每轮工具调用都付全价；多轮对话不要改历史前缀，要一直往后追加，否则会丢掉推理状态。这说明上下文布局直接影响成本。内容为作者整理，含论坛转述。

> "多轮对话千万别改历史前缀，永远往后追加"

原则：[P06](/compare/evidence#p06) [P10](/compare/evidence#p10) [P14](/compare/evidence#p14) [P15](/compare/evidence#p15) [P17](/compare/evidence#p17) [P18](/compare/evidence#p18)

### XM-021 · 一份以省 token 为目标的 AGENTS.md 规则 {#xm-021}
**作者**：govin.eth ／ G哥（@goan999999）｜**日期**：2026-11-18｜[原帖](https://x.com/goan999999/status/2122989430009204744)｜♥ 28

作者分享写进 AGENTS.md 的省 token 规则：只分析任务涉及的文件，不无目的扫描整个代码库；复用已有上下文；先定位根因再最小范围修改，不重构无关代码；只跑覆盖本次修改的测试，通过后立即停止。帖中「省 41%」为作者自称，未给出测量方法。

> "先定位问题根因，再进行最小范围修改，不要重构无关代码"

原则：[P02](/compare/evidence#p02) [P03](/compare/evidence#p03) [P06](/compare/evidence#p06) [P09](/compare/evidence#p09) [P14](/compare/evidence#p14)
