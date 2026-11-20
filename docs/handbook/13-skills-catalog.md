# 13 · Skills 生态：官方与高星仓库清单

[[toc]]

## 要点

- **格式已经统一。** Agent Skills（一个文件夹 + `SKILL.md`）由 Anthropic 发起，现在是开放规范，2026-11-04 起由 LF Projects 托管。Claude Code、Codex、Gemini CLI、GitHub Copilot、Cursor、OpenCode、Kiro 等都按同一格式加载，差别主要在目录位置与调用方式。
- **找 skill 先看厂商官方。** Anthropic、OpenAI、Google、Microsoft、Hugging Face 以及 Vercel、Cloudflare、AWS、Supabase 等都有官方仓库。它们最大的价值是补上模型对新版 API 的知识滞后。
- **社区高星仓库多是「工作方法」。** Superpowers、Matt Pocock、Addy Osmani 等提供的是计划、TDD、评审一类流程，适合借鉴后改成自己的版本，不适合整套照搬。
- **星标只说明关注度。** 本章所有星标数都是 2026-11-20 从 GitHub API 实时读取的，不代表质量。许多仓库创建于 2026 年，星标增长很快。
- **第三方 skill 就是第三方代码。** 脚本以你的权限运行，`SKILL.md` 本身也是会被执行的指令。引入前要审查、扫描、锁版本，并放进沙箱（§6、[第 09 章](./09-security)）。

> 本章先给出全书视角的定位与推荐起步组合（§0），再给完整清单（§4）。skill 机制本身怎么用、什么时候不该用，见 [第 07 章 §4](./07-harness-tools#_4-skills-按需加载的专业知识) 与 [第 02 章 §4](./02-context-engineering#_4-渐进式披露)。

## 0. 从全书视角看 Skills {#book-view}

**一句话定位**：skill 属于 [第 04 章](./04-architecture-constraints#_3-guides-与-sensors-一个完整的分类框架) 所说的「推理型 Guide（前馈）」，是其中按需加载的那一层。它让智能体**知道怎么做**，但不保证它**一定照做**。必须做到的事要靠 hook、lint 和 CI 来保证（第 04、12 章），做没做对要靠验证来证明（第 05 章）。

### 0.1 skill 在各章中的位置 {#book-map}

| 章 | 该章怎么说 | 对 skill 的含义 |
| --- | --- | --- |
| [01 心智模型](./01-mental-model) | 「靠谱」主要来自环境；skills 是需要掌握的新抽象层之一 | skill 是环境的一部分，不是让模型变聪明的捷径 |
| [02 上下文工程](./02-context-engineering#_4-渐进式披露) | 渐进式披露；高频且必需 → 常驻索引，低频或专项 → skill | 先决定一条知识该常驻还是按需，再决定要不要做成 skill |
| [03 计划先行](./03-spec-and-plan) | 先计划后编码，按任务规模选流程 | 流程类 skill（如 Superpowers）能把计划先行落地，但小任务不必套用 |
| [04 架构约束](./04-architecture-constraints#_3-guides-与-sensors-一个完整的分类框架) | 能用计算型就不用推理型；skills 属于非确定性指令 | skill 只适合放需要判断的知识，机械规则交给 linter 和结构测试 |
| [05 验证](./05-verification#_8-评测-为团队的-harness-建回归) | 用 `verify` skill 固化验证流程；改 skills 要跑 harness 回归集 | 最值得写的第一个 skill 往往是 verify；改 skill 也要评测 |
| [07 工具与 Harness](./07-harness-tools#_4-skills-按需加载的专业知识) | skills 负责按需知识与流程；从朴素开始；先确认它会被调用 | 数量宁少勿多，每个 skill 对应一个具体失败 |
| [08 团队](./08-team-process#_1-组织级推进-openai-的清单) | 把做过的事写成 skills 提交到共享仓库；先人人对齐，再人机对齐 | 团队 skill 是共识的固化，不是从外部引入的现成答案 |
| [09 安全](./09-security#_3-供应链-新的攻击面) | skills 是供应链的一部分，要像代码一样评审 | 第三方 skill 要先审查、锁版本，再放进沙箱运行（本章 §6） |
| [10 反模式](./10-anti-patterns#_17-由人手动编排的-skill「金字塔」) | 由人手动编排的 skill「金字塔」是反模式 | 不要用 skill 搭人工流水线 |
| [12 质量](./12-quality-cicd#q08) | Evals 即 CI；`skills/**` 的变更要触发评测 | skill 是会回归的代码，变更要能拦下 |

### 0.2 推荐起步组合（按采用路径排列） {#starter-set}

从本章 71 个仓库中挑出 11 组（共 14 个仓库）。**必装**：每个团队都应该有；**按需**：符合场景时再装；**参考**：读懂后改写成自己的，不要原样安装。

| 阶段 | 仓库 | 标记 | 为什么选它（对应章节） |
| --- | --- | --- | --- |
| ① 个人起步 | [anthropics/skills](https://github.com/anthropics/skills) | 参考 | 格式发起方的官方范例，看「一个 skill 只做一类事」该怎么写；文档类 skill 可以直接用（07） |
| ① 个人起步 | 你所用技术栈的厂商官方 skill，例如 [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)、[cloudflare/skills](https://github.com/cloudflare/skills)、[supabase/agent-skills](https://github.com/supabase/agent-skills)（B/C/D 组） | 按需 | 补上模型对新版 API 的知识滞后，正是 02 章所说「模型读不到、猜不到」的知识；只装正在用的产品 |
| ① 个人起步 | [mattpocock/skills](https://github.com/mattpocock/skills) | 参考 | 小而可组合，作者明确不接管流程，符合 07 章「从朴素开始」 |
| ① 个人起步 | [obra/superpowers](https://github.com/obra/superpowers) | 参考 | 把计划先行、子智能体评审、red/green TDD 串成流程（03、05）；整套用于小任务就是 10 章反模式 13 |
| ② 团队采用 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 参考 | 按定义 → 计划 → 构建 → 验证 → 评审 → 发布组织，与本书 03 → 05 → 06 → 12 的顺序对应；适合用来搭团队自己的骨架 |
| ② 团队采用 | [vercel-labs/skills](https://github.com/vercel-labs/skills)（`npx skills`） | 按需 | 团队同时用多种工具时，一次装到多个目录（§3）；装好后仍要提交进仓库，不要自动更新 |
| ② 团队采用 | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 参考 | 找厂商官方 skill 的索引，用来查找，不用来批量安装 |
| ③ 自己写 | [agentskills/agentskills](https://github.com/agentskills/agentskills) | 必装 | 写 skill 前对照规范，用 `skills-ref validate` 把格式校验放进 CI（12） |
| ③ 自己写 | [alibaba/skill-up](https://github.com/alibaba/skill-up) 或 [microsoft/waza](https://github.com/microsoft/waza) | 按需 | 给 skill 建回归评测：会不会被触发、用了是否更好（05 §8、12 Q08） |
| ④ 审查与安全 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | 必装 | 第三方 skill 引入前先扫描并进 CI；扫描只能降低风险，人工审查仍不可少（09、§6） |
| ④ 审查与安全 | [Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) | 按需 | 需要把 skill、MCP 与智能体放在一个平台里统一做安全检查时用（09） |

**最小组合**：个人用户先装一个技术栈对应的厂商官方 skill，再自己写一个 `verify` skill（05 章）。团队在此基础上加规范校验（agentskills）、扫描（SkillSpector）和评测（skill-up 或 waza），并把 skill 目录纳入 CODEOWNERS。

### 0.3 不要这样做 {#dont}

| 不要 | 为什么（对应章节） | 改为 |
| --- | --- | --- |
| 把「必须遵守」的规则只写进 skill | skill 不保证被调用，遵守也由模型决定（04、[10 · 反模式 1](./10-anti-patterns#_1-把规则写进提示-就以为它会被遵守)） | 改成 hook、lint 或 CI 门禁 |
| 整包安装 awesome 列表或上千个 skill 的大合集 | 描述越多，误调用与上下文成本越高，等于指令膨胀（[10 · 反模式 2](./10-anti-patterns#_2-指令膨胀)） | 按失败驱动，一次加一个 |
| 搭一层层 skill，靠人按顺序逐个调用 | [10 · 反模式 17](./10-anti-patterns#_17-由人手动编排的-skill「金字塔」)；换模型后旧 skill 可能让效果变差 | 少量自包含的 skill，必要时用命令显式触发 |
| 每个任务都套用完整的流程类 skill | [10 · 反模式 13](./10-anti-patterns#_13-对所有任务套用完整-sdd-流程)；03 章：按任务规模选流程 | 小改动直接做，大任务才走计划与评审 |
| 按星标挑选，或让第三方 skill 自动更新 | 星标只反映关注度；注册表已遭投毒（09、§6） | 只从组织官方仓库安装，固定 commit，看 diff 后再更新 |
| 改了 skill 或换了模型却不复测 | harness 会过期（07 §8）；没有评测只能「等投诉」（05 §8） | 维护 10–20 个任务的 harness 回归集，并接入 CI |
| 用 skill 代替团队共识 | 08 章：先人人对齐，再人机对齐 | 先在团队内讨论定下规范，再写成 skill |

## 1. 先分清四个概念 {#concepts}

| 机制 | 何时进入上下文 | 典型位置 | 本章怎么处理 |
| --- | --- | --- | --- |
| 规则文件（AGENTS.md / CLAUDE.md / Cursor rules） | 每次会话常驻 | 仓库根、子目录、`.cursor/rules/` | 只收高星来源（G 组），写法见 [第 02 章](./02-context-engineering) |
| Skill | 启动时只读名称与描述，任务匹配时才读全文 | `.claude/skills/`、`.agents/skills/` 等（§3） | **本章主体** |
| 插件（plugin） | 一次安装多种组件 | 各工具的插件市场 | 许多官方 skill 以插件形式分发，一并收录 |
| MCP 服务器 | 工具定义按需或常驻 | MCP 配置 | 不单列，见 [OS12](/sources/open-source#os12) |

名字里带「skills」的仓库不一定是 skill。比如 `andrej-karpathy-skills` 实际是一个 CLAUDE.md 文件。

## 2. 格式规范：SKILL.md 长什么样 {#spec}

规范与文档在 [agentskills.io](https://agentskills.io/specification)，源码在 [agentskills/agentskills](https://github.com/agentskills/agentskills)。根据该仓库的 GOVERNANCE.md，项目自 2026-11-04 起作为 LF Projects 下的项目运作，规范采用 Apache-2.0 许可，文档采用 CC BY 4.0。

```
my-skill/
├── SKILL.md          # 必需：YAML frontmatter + Markdown 指令
├── scripts/          # 可选：可执行脚本
├── references/       # 可选：按需读取的参考文档
└── assets/           # 可选：模板、数据等资源
```

| frontmatter 字段 | 必需 | 约束 |
| --- | --- | --- |
| `name` | 是 | ≤64 字符，小写字母、数字、连字符，须与目录名一致 |
| `description` | 是 | ≤1024 字符，写清「做什么」和「什么时候用」，**决定它会不会被调用** |
| `license` | 否 | 许可证名或随附的许可证文件 |
| `compatibility` | 否 | ≤500 字符，环境要求（目标产品、系统依赖、网络） |
| `metadata` | 否 | 任意键值对 |
| `allowed-tools` | 否 | 预先放行的工具列表（实验性，各工具支持程度不一） |

**渐进式披露**的三层：元数据约 100 token，启动时全部加载；`SKILL.md` 正文建议少于 5,000 token、不超过 500 行，激活时加载；`scripts/`、`references/` 等资源用到时才读。校验工具是 `skills-ref validate ./my-skill`。

各工具会在标准之上加扩展字段。例如 Claude Code 有 `disable-model-invocation`，可禁止模型自动调用，还能让 skill 在子智能体里运行；Codex 可以在 `agents/openai.yaml` 里关闭隐式调用。这些扩展字段在别的工具里会被忽略。

## 3. 跨工具兼容：谁会加载 SKILL.md {#compat}

下表的路径与行为来自各工具官方文档（2026-11-20 打开核对）。

| 工具 | 项目级目录 | 用户级目录 | 调用方式与要点 | 文档 |
| --- | --- | --- | --- | --- |
| Claude Code | `.claude/skills/`（支持子目录嵌套） | `~/.claude/skills/`；另有企业托管目录 | 按描述自动调用，也可用 `/skill-name` 显式调用；旧的 `.claude/commands/` 已并入 skills；插件可打包 skills | [链接](https://code.claude.com/docs/en/skills) |
| OpenAI Codex | `.agents/skills`（从当前目录逐级扫描到仓库根） | `$HOME/.agents/skills`；另有管理员级与系统级 | `/skills` 或 `$` 提及显式调用，也可按描述隐式调用；内置 skill-installer | [链接](https://developers.openai.com/codex/skills/) |
| Gemini CLI | `.gemini/skills/`、`.agents/skills/` | `~/.gemini/skills/`、`~/.agents/skills/` | 模型通过 `activate_skill` 工具激活，**激活前弹窗征求同意**；`/skills enable/disable` | [链接](https://geminicli.com/docs/cli/skills/) |
| GitHub Copilot | `.github/skills`、`.claude/skills`、`.agents/skills` | `~/.copilot/skills`、`~/.agents/skills` | 可用 `gh skill` 从 GitHub 仓库发现并安装 | [链接](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) |
| Cursor | `.agents/skills/`、`.cursor/skills/`（支持子目录）；兼容 `.claude/skills/`、`.codex/skills/` | `~/.agents/skills/`、`~/.cursor/skills/`；兼容 `~/.claude/skills/`、`~/.codex/skills/` | 按描述自动加载 | [链接](https://cursor.com/docs/context/skills) |
| OpenCode | `.opencode/skills/`、`.agents/skills`、`.claude/skills` | `~/.agents/skills`、`~/.claude/skills` | `disable-model-invocation` 或 `opencode/autoinvoke: false` 可把 skill 移出模型可见列表 | [链接](https://opencode.ai/docs/skills/) |
| Kiro | `.kiro/skills/` | `~/.kiro/skills/` | 按描述自动激活，或输入 `/` 当斜杠命令用；自定义智能体默认不加载，需要用 `skill://` 显式引入 | [链接](https://kiro.dev/docs/skills/) |

**互通结论**：`.agents/skills/` 能被 Codex、Gemini CLI、Copilot、Cursor、OpenCode 读取，agentskills.io 的客户端实现指南也推荐把它作为跨客户端约定。`.claude/skills/` 能被 Claude Code、Copilot、Cursor、OpenCode 读取。按上述文档，Claude Code 只列出 `.claude/skills/`。需要同时支持多个工具时，可以用 [`npx skills`](https://github.com/vercel-labs/skills) 一次装到多个目录，或者在仓库里保留一份源目录，再用脚本同步。

截至 2026-11-20，agentskills.io 的[客户端展示页](https://agentskills.io/clients)数据列出 46 个支持该格式的产品，除上表外还有 TRAE、JetBrains Junie、Roo Code、Goose、Amp、OpenHands、Spring AI、Databricks、Snowflake Cortex Code 等（厂商自报）。

## 4. 仓库清单 {#catalog}

**收录口径**

- 只收录 2026-11-20 通过 GitHub API 确认存在、且 README 已打开核对的仓库。星标数取自同日的 GitHub REST API，之后会变化。
- 「官方」指仓库属于该公司的 GitHub 组织。
- 「内容」根据 README 概括，其中的数量（例如「1000+ skills」）都是仓库自述，未逐一清点。
- 「许可证」是 GitHub API 识别出的 SPDX 标识。识别不到时标「仓库未声明」，如果 README 另有声明会注明。**没有许可证的仓库默认保留所有权利**，复制或修改前先确认授权。
- 同组内按「先官方/规范、再按星标」大致排序。

| 分组 | 收录数 |
| --- | ---: |
| A. 规范、注册表与安装工具 | 5 |
| B. 模型与 AI 平台厂商官方 | 14 |
| C. 开发者工具与云服务厂商官方 | 17 |
| D. 中国厂商官方 | 11 |
| E. 社区高星技能集 | 7 |
| F. Awesome 列表与目录 | 8 |
| G. 规则文件：CLAUDE.md、Cursor rules 与 AGENTS.md | 4 |
| H. 安全扫描与评测工具 | 5 |
| **合计** | **71** |

### A. 规范、注册表与安装工具 {#g-spec}

先弄清「格式是什么、从哪装」。这一组不是 skill 本身，而是让 skill 能被发现、安装与校验的基础设施。

| 仓库 | 维护方 | ★（2026-11-20） | 内容 | 适用场景 | 许可证 |
| --- | --- | ---: | --- | --- | --- |
| [agentskills/agentskills](https://github.com/agentskills/agentskills) | Agent Skills 项目（2026-11-04 起由 LF Projects 托管） | 27,465 | Agent Skills 格式规范、agentskills.io 文档源码，以及校验工具 `skills-ref` | 写自己的 skill 前对照规范；用 `skills-ref validate` 做 CI 校验 | Apache-2.0 |
| [agentsmd/agents.md](https://github.com/agentsmd/agents.md) | AGENTS.md 开放格式（多家厂商共同支持） | 25,609 | AGENTS.md 格式说明与 agents.md 官网源码 | 常驻规则文件的写法参照；与 skill 互补（常驻 vs 按需） | MIT |
| [vercel-labs/skills](https://github.com/vercel-labs/skills) | Vercel Labs | 40,096 | `npx skills` 命令行：从 GitHub 仓库挑选 skill 安装到多个智能体的目录，带锁文件与内容哈希；目录站 skills.sh | 跨工具批量安装、更新 skill；README 自称支持 OpenCode、Claude Code、Codex、Cursor 等数十种智能体（厂商自报） | MIT |
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | OpenClaw | 9,559 | OpenClaw 的公共 skill 注册表：发布、版本、向量检索与审核钩子 | OpenClaw 用户检索 skill；**也是 2026 年多起恶意 skill 事件的发生地**，见 §6 | MIT |
| [cloudflare/agent-skills-discovery-rfc](https://github.com/cloudflare/agent-skills-discovery-rfc) | Cloudflare | 381 | 草案：通过 `/.well-known/` URI 发布与发现 skills，含索引、完整性校验与归档分发 | 想在自己域名上发布 skill 的团队；了解「skill 分发协议」的方向 | Apache-2.0 |

### B. 模型与 AI 平台厂商官方 {#g-ai-vendors}

格式的发起方与主要采用方。优先从这里找文档类、平台类 skill，也是写 skill 的最佳范例来源。

| 仓库 | 维护方 | ★（2026-11-20） | 内容 | 适用场景 | 许可证 |
| --- | --- | ---: | --- | --- | --- |
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic | 197,706 | 官方示例 skill（创意设计、开发技术、企业沟通、文档处理 docx/pdf/pptx/xlsx）、规范副本与模板；可作为 Claude Code 插件市场添加 | 学习 skill 写法；直接用文档类 skill 生成 Office/PDF 文件 | 仓库未声明统一许可证；README 称多数 skill 为 Apache 2.0，以各目录 LICENSE 为准 |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Anthropic | 47,733 | Anthropic 官方 Claude Code 插件目录（插件可打包 skills、命令、子智能体、hooks、MCP） | 在 Claude Code 中一次装好一组能力；README 提醒安装前须信任插件来源 | Apache-2.0 |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Anthropic | 36,573 | 面向知识工作者的插件（按岗位与团队组织），主要用于 Claude Cowork，也兼容 Claude Code | 非编码场景：销售、财务、法务、研究等工作流 | Apache-2.0 |
| [openai/skills](https://github.com/openai/skills) | OpenAI | 28,845 | Codex skill 目录，**README 已标注弃用**，新示例迁到 openai/plugins | 仅作历史参考；新项目看下一行 | 仓库未声明统一许可证；每个 skill 目录内有 LICENSE.txt |
| [openai/plugins](https://github.com/openai/plugins) | OpenAI | 8,022 | Codex 插件示例：每个插件含 `.codex-plugin/plugin.json`，可带 skills、MCP、命令、hooks；示例有 Figma、Notion、iOS/macOS/Web 开发等 | Codex 用户安装官方插件；学习「skill-only 插件」的打包方式 | 仓库未声明许可证 |
| [google/skills](https://github.com/google/skills) | Google | 24,456 | Google 产品与技术的 skills，以 Google Cloud 为主（入门、IAM、方案架构、部署智能体等） | 在 Google Cloud 上搭建与运维；可按项目或全局安装 | Apache-2.0 |
| [google-gemini/gemini-skills](https://github.com/google-gemini/gemini-skills) | Google（Gemini 团队） | 4,527 | Gemini API、SDK 与模型交互的 skills，用来弥补模型对自身新 API 的知识滞后 | 调用 Gemini API 的应用开发 | Apache-2.0 |
| [android/skills](https://github.com/android/skills) | Google（Android 团队） | 10,665 | 依据 developer.android.com 最佳实践写成的模块化 Android 开发 skills | Android 原生开发、迁移与最佳实践落地 | Apache-2.0 |
| [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | Google Labs | 10,717 | 配合 Stitch MCP 服务器的设计、构建与工具类 skills/插件 | 用 Google Stitch 做 UI 设计到代码 | Apache-2.0 |
| [microsoft/skills](https://github.com/microsoft/skills) | Microsoft | 3,227 | 面向 Azure SDK 与 Microsoft Foundry 的 skills、自定义智能体、AGENTS.md 模板与 MCP 配置（README 标注 Work in Progress） | 用 Python/.NET/TS/Java/Rust 调 Azure SDK | MIT |
| [microsoft/azure-skills](https://github.com/microsoft/azure-skills) | Microsoft | 1,659 | Azure Skills 插件：skills + Azure MCP Server + Foundry MCP 一次安装 | Azure 选型、部署前校验与运维 | MIT |
| [MicrosoftDocs/Agent-Skills](https://github.com/MicrosoftDocs/Agent-Skills) | Microsoft Docs | 817 | 基于 Microsoft Learn 文档整理的 Azure skills 集合 | 希望 skill 内容跟随官方文档更新的 Azure 团队 | CC-BY-4.0 |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | GitHub | 41,362 | 社区贡献、GitHub 维护的 Copilot 资源：自定义智能体、instructions、skills、hooks、工作流与插件，另有检索网站 | GitHub Copilot 用户找现成配置 | MIT |
| [huggingface/skills](https://github.com/huggingface/skills) | Hugging Face | 11,364 | AI/ML 任务的 skills：数据集创建、模型训练与评测；以 `hf-cli` skill 为入口按需安装其他 skill | 在 Hugging Face Hub 上做训练、评测与发布 | Apache-2.0 |

### C. 开发者工具与云服务厂商官方 {#g-dev-vendors}

「谁的 API 谁来写 skill」：由产品团队维护，最能弥补模型对新版本 API 的知识滞后。按你的技术栈挑，别全装。

| 仓库 | 维护方 | ★（2026-11-20） | 内容 | 适用场景 | 许可证 |
| --- | --- | ---: | --- | --- | --- |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | Vercel | 34,549 | Vercel 官方 skills：React 最佳实践、Web 设计规范、写作规范、React Native、部署到 Vercel、项目优化审计等 | React/Next.js 前端与 Vercel 部署 | API 未识别许可证；README 声明 MIT |
| [vercel-labs/next-skills](https://github.com/vercel-labs/next-skills) | Vercel | 992 | **已迁移**：Next.js skills 现位于 [vercel/next.js 仓库的 skills 目录](https://github.com/vercel/next.js/tree/canary/skills)，与框架版本同步 | Next.js 项目改从新位置安装 | 仓库未声明许可证 |
| [cloudflare/skills](https://github.com/cloudflare/skills) | Cloudflare | 3,405 | Cloudflare 开发者平台 skills（Workers、Agents SDK、各框架部署等），可连同 Cloudflare MCP 服务器一起以插件安装 | 在 Cloudflare 上构建与部署 | Apache-2.0 |
| [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | AWS | 3,526 | AWS 官方的 MCP 服务器、skills、插件与规则文件合集 | 在 AWS 上构建、部署与管理应用 | Apache-2.0 |
| [supabase/agent-skills](https://github.com/supabase/agent-skills) | Supabase | 3,108 | Supabase skills，支持 `.well-known` 发现 | Supabase 数据库、认证与 Postgres 实践 | MIT |
| [expo/skills](https://github.com/expo/skills) | Expo | 4,194 | 构建、部署、升级、调试 Expo 应用的 skills；README 强调 Expo 文档与 CLI 仍是事实来源 | Expo / React Native 应用与 EAS | MIT |
| [hashicorp/agent-skills](https://github.com/hashicorp/agent-skills) | HashiCorp | 934 | Terraform（16 个）与 Packer（4 个）skills 及产品插件包（数量为仓库自述） | 基础设施即代码 | MPL-2.0 |
| [getsentry/skills](https://github.com/getsentry/skills) | Sentry | 1,186 | Sentry 团队内部开发用的 skills 与子智能体；面向用户的接入 skill 在 getsentry/sentry-for-ai | 参考一家公司如何组织内部 skills 仓库 | Apache-2.0 |
| [langchain-ai/langchain-skills](https://github.com/langchain-ai/langchain-skills) | LangChain | 1,349 | Deep Agents、LangGraph、LangChain 的开发 skills 与 LangSmith 评测（README 标注早期开发） | LangChain 生态的智能体开发与评测 | MIT |
| [callstackincubator/agent-skills](https://github.com/callstackincubator/agent-skills) | Callstack | 1,714 | React Native 生产实践 skills：性能、导航、升级、测试与迁移 | React Native 应用 | MIT |
| [elastic/agent-skills](https://github.com/elastic/agent-skills) | Elastic | 610 | Elastic 官方 skills（技术预览），README 有安全注意事项一节 | Elasticsearch / Kibana / 可观测性 | Apache-2.0 |
| [mongodb/agent-skills](https://github.com/mongodb/agent-skills) | MongoDB | 206 | MongoDB 官方 skills（查询、建模、优化、Atlas Search）+ Atlas MCP 插件 | MongoDB / Atlas 开发 | Apache-2.0 |
| [remotion-dev/skills](https://github.com/remotion-dev/skills) | Remotion | 7,576 | Remotion 视频项目的最佳实践、创建、渲染、字幕等 skills | 用代码生成视频 | 仓库未声明许可证 |
| [obsidianmd/obsidian-skills](https://github.com/obsidianmd/obsidian-skills) | Obsidian | 53,247 | 让智能体使用 Obsidian CLI 与开放格式（Markdown、Bases、JSON Canvas）的 skills | 个人知识库自动化 | MIT |
| [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | GreenSock（GSAP） | 18,768 | GSAP 官方 skills：核心 API、时间线、ScrollTrigger、各框架集成与性能 | Web 动画 | MIT |
| [trailofbits/skills](https://github.com/trailofbits/skills) | Trail of Bits | 8,300 | 安全研究与审计 skills/插件：智能合约、代码审计、恶意软件分析、逆向、移动安全等 | 安全审计与漏洞研究（安全公司官方维护） | CC-BY-SA-4.0 |
| [JetBrains/skills](https://github.com/JetBrains/skills) | JetBrains | 399 | JetBrains 筛选并验证的上游 skills 快照：129 个 skill、15 个上游仓库，每个 SKILL.md 保留来源链接，含安全扫描说明（数字为仓库自述） | 想要「经过二次筛选」的通用 skill 集 | 仓库未声明许可证；各 skill 沿用上游许可证 |

### D. 中国厂商官方 {#g-cn-vendors}

只收录在 GitHub 上有公开仓库、且由厂商官方组织维护的项目。整体规模明显小于海外，多数是「自家模型或云产品的接入 skill」。

| 仓库 | 维护方 | ★（2026-11-20） | 内容 | 适用场景 | 许可证 |
| --- | --- | ---: | --- | --- | --- |
| [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MiniMax | 13,877 | 开发类 skills（前端、全栈、Android、iOS、Flutter、React Native、Shader）与文档类 skills（PDF、PPTX、XLSX）；README 标注 Beta | 多端应用开发；Office 文档生成 | MIT |
| [zai-org/GLM-skills](https://github.com/zai-org/GLM-skills) | 智谱（Z.ai） | 478 | GLM 系列官方 skills：GLM-V 多模态、GLM-OCR、GLM-Image 等 | 在智能体里调用 GLM 多模态与 OCR 能力 | Apache-2.0 |
| [XiaomiMiMo/MiMo-Skills](https://github.com/XiaomiMiMo/MiMo-Skills) | 小米 MiMo | 103 | MiMo 系列 skills，如 MiMo V2.5 TTS 语音合成 | 需要 MiMo 语音能力的智能体 | MIT |
| [aliyun/alibabacloud-aiops-skills](https://github.com/aliyun/alibabacloud-aiops-skills) | 阿里云 | 299 | 阿里云官方 Agent Skills 合集（产品能力与通用工具） | 在阿里云上运维与开发 | API 未识别许可证；README 声明 Apache-2.0 |
| [aliyun/alibabacloud-ecs-troubleshoot-skills](https://github.com/aliyun/alibabacloud-ecs-troubleshoot-skills) | 阿里云 | 148 | 4 个 ECS 排障 skill：Linux/Windows 系统排障、用户态入侵排查、内核 CVE 检测 | 云主机故障诊断与安全排查 | Apache-2.0 |
| [agentscope-ai/skills](https://github.com/agentscope-ai/skills) | AgentScope（阿里巴巴通义实验室 SysML 团队，据其 pyproject 作者字段） | 135 | AgentScope 生态与 QwenPaw 应用的 skills | 用 AgentScope 开发多智能体应用 | Apache-2.0 |
| [larksuite/cli](https://github.com/larksuite/cli) | 飞书 / Lark | 18,162 | 官方 `lark-cli`：200+ 命令覆盖消息、文档、多维表格、日历等，附 26 个 Agent Skills（数量为厂商自报） | 让智能体操作飞书 | MIT |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 字节跳动 | 85,529 | DeerFlow 2.0：基于 LangGraph 的长程「超级智能体 harness」，内置 skills、子智能体、记忆与沙箱 | 研究 skill 在 harness 中的加载方式；深度研究类任务 | MIT |
| [TencentCloudBase/CloudBase-AI-Toolkit](https://github.com/TencentCloudBase/CloudBase-AI-Toolkit) | 腾讯云 CloudBase | 1,168 | CloudBase 接入层：插件 + skills + MCP，让智能体操作数据库、云函数、存储与部署 | 在腾讯云 CloudBase 上做全栈应用 | MIT |
| [TencentCloudBase/skills](https://github.com/TencentCloudBase/skills) | 腾讯云 CloudBase | 81 | 从上面的 Toolkit 中抽取的独立 skills 目录 | 只想要 skill、不要插件的场景 | MIT |
| [NetEase/skills](https://github.com/NetEase/skills) | 网易云音乐 | 267 | 基于 `ncm-cli` 的网易云音乐 skills（安装配置、音乐操作、推荐助手） | 让智能体搜索、管理歌单 | 仓库未声明许可证 |

### E. 社区高星技能集 {#g-community}

个人或小团队维护、主打「工作方法」的 skill 集。星标最高的一组，也是最需要你自己判断取舍的一组。

| 仓库 | 维护方 | ★（2026-11-20） | 内容 | 适用场景 | 许可证 |
| --- | --- | ---: | --- | --- | --- |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Matt Pocock（个人） | 328,157 | 作者日常工程用的小型、可组合 skills（工程与效率两类），强调不接管流程 | 想要轻量、可自行修改的工程类 skill | MIT |
| [obra/superpowers](https://github.com/obra/superpowers) | Jesse Vincent（个人） | 322,075 | 一整套「开发方法论」skills：先头脑风暴澄清需求 → 写计划 → 子智能体逐任务执行并评审 → 强制 TDD；README 给出 Claude Code、Codex、Cursor、Gemini CLI、Copilot CLI 等十多种工具的安装方式 | 希望智能体按固定流程（计划 + TDD + 评审）工作的团队 | MIT |
| [garrytan/gstack](https://github.com/garrytan/gstack) | Garry Tan（个人） | 142,136 | 23 个带强烈个人风格的命令/skill，把智能体分成 CEO、工程经理、设计、评审、QA、安全、发布等角色 | 参考「角色化」工作流；整套照搬前先评估 | MIT |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Addy Osmani（个人） | 119,182 | 26 个工程 skill，按定义→计划→构建→验证→评审→发布组织，配 10 个斜杠命令 | 按开发生命周期组织 skill 的范例 | MIT |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | K-Dense | 57,852 | 科研类 skills（原名 claude-scientific-skills），覆盖多个学科的数据库、分析与工作流 | 科研与数据分析 | MIT |
| [wshobson/agents](https://github.com/wshobson/agents) | Seth Hobson（个人） | 42,709 | 插件、子智能体、skills 与命令的大合集；用 Claude Code 插件格式编写，再通过适配器生成 Codex、Cursor、OpenCode、Copilot 等格式 | 多工具团队共享一套组件；参考跨 harness 适配做法 | MIT |
| [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | Muratcan Koylan（个人） | 18,382 | 上下文工程与 harness 工程主题的 skills：上下文管理、多智能体架构、评测 | 构建智能体系统本身（而不是用智能体写业务代码） | MIT |

### F. Awesome 列表与目录 {#g-awesome}

用来「找」，不是用来「装」。列表只做收录，几乎不审查内容；条目多不代表质量高。

| 仓库 | 维护方 | ★（2026-11-20） | 内容 | 适用场景 | 许可证 |
| --- | --- | ---: | --- | --- | --- |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Composio | 79,897 | 按类别整理的 Claude skills 列表（README 自称 1000+），附 Composio MCP 网关推广 | 按场景找 skill 的入口 | 仓库未声明许可证 |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | hesreallyhim（个人） | 58,386 | Claude Code 资源精选：skills、子智能体、hooks、斜杠命令、状态栏、插件 | 找 Claude Code 周边组件 | 非标准许可证（见仓库 LICENSE） |
| [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | sickn33（个人） | 50,002 | 3,000+ 个可安装 SKILL.md（自述）及本地检索工具 AAS Core，覆盖 Claude Code、Codex、Cursor、Gemini CLI | 大规模检索；数量多，逐个审查成本高 | MIT |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | VoltAgent | 37,359 | 收录各开发团队官方 skills 与社区 skills（README 强调人工挑选），附各工具 skill 路径表与安全提示 | **找厂商官方 skill 的首选索引** | MIT |
| [composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills) | Composio 社区 | 17,367 | 面向 Codex CLI 与 API 的 skills 列表 | Codex 用户 | 仓库未声明许可证 |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | Travis（个人） | 15,880 | Claude skills 精选：官方 skills、社区 skills、工具与教程 | 入门导读 | 仓库未声明许可证 |
| [heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills) | Hailey Cheng（个人） | 6,412 | 多语言（含简体中文）的 skills 教程、指南与目录索引 | 中文读者入门 | MIT |
| [Piebald-AI/awesome-gemini-cli](https://github.com/Piebald-AI/awesome-gemini-cli) | Piebald | 645 | Gemini CLI 的工具、扩展与资源列表 | Gemini CLI 用户 | CC0-1.0 |

### G. 规则文件：CLAUDE.md、Cursor rules 与 AGENTS.md {#g-rules}

常驻规则文件与 skill 是两种机制（[第 07 章 §1](./07-harness-tools#_1-术语-harness-由什么组成)）。这一组是「规则」的高星来源，常被误称为 skills；AGENTS.md 规范本身见 A 组。

| 仓库 | 维护方 | ★（2026-11-20） | 内容 | 适用场景 | 许可证 |
| --- | --- | ---: | --- | --- | --- |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Multica（Jiayuan） | 234,497 | **单个 CLAUDE.md 文件**：根据 Karpathy 对 LLM 编码坑点的观察写成的四条原则（先想后写、简单优先、外科手术式修改、目标驱动） | 给规则文件找起点；名字带 skills，实际是常驻规则 | API 未识别许可证；README 声明 MIT |
| [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) | Patrick JS（个人） | 41,172 | 按框架与语言整理的 Cursor 规则（`.cursor/rules/*.mdc`） | Cursor 用户找技术栈规则 | CC0-1.0 |
| [sanjeed5/awesome-cursor-rules-mdc](https://github.com/sanjeed5/awesome-cursor-rules-mdc) | sanjeed5（个人） | 3,588 | 用检索 + LLM 批量生成的 Cursor MDC 规则及生成器；README 声明非 Cursor 官方 | 参考生成方式；生成内容须人工复核 | CC0-1.0 |
| [steipete/agent-rules](https://github.com/steipete/agent-rules) | Peter Steinberger（个人） | 5,668 | 作者 2025 年中使用的规则与知识文件；README 已说明过时，新内容在 agent-scripts | 历史参考 | MIT |

### H. 安全扫描与评测工具 {#g-security}

第三方 skill 的「门禁」。装之前扫一遍，改之后评一遍。

| 仓库 | 维护方 | ★（2026-11-20） | 内容 | 适用场景 | 许可证 |
| --- | --- | ---: | --- | --- | --- |
| [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | NVIDIA | 26,955 | skill 安全扫描器：检测提示注入、恶意模式与漏洞，支持 LLM 分析与 MCP 服务器模式 | 引入第三方 skill 前扫描；放进 CI | Apache-2.0 |
| [Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) | 腾讯朱雀实验室 | 7,580 | AI 红队平台 A.I.G：含 Skill Scan、MCP Scan、Agent Scan 与基础设施漏洞扫描 | 团队级的 skill/MCP/智能体安全检查 | Apache-2.0 |
| [alibaba/skill-up](https://github.com/alibaba/skill-up) | 阿里巴巴 | 1,501 | skill 评测 CLI：用声明式用例跑智能体，评分回答与工作区变更，支持本地与 CI，可比较多次运行 | 验证 skill 是否真的有效、改动有无回归 | Apache-2.0 |
| [microsoft/waza](https://github.com/microsoft/waza) | Microsoft | 1,515 | Go 写的评测 CLI：为工作流、skills 与自定义智能体编写场景、跑多次评分试验 | skill 的回归评测 | MIT |
| [huggingface/upskill](https://github.com/huggingface/upskill) | Hugging Face | 770 | 从智能体轨迹生成并评测 skill：用强模型写 skill，让便宜模型使用 | 把一次成功经验沉淀成 skill 并验证 | Apache-2.0 |

## 5. 怎么挑：五步法 {#choose}

1. **先确认真的需要。** 一个 skill 应该对应一个反复出现的具体失败。Vercel 的评测里，AGENTS.md 中的常驻索引胜过 skill，56% 的用例里 skill 根本没被调用（[VD11](/sources/vendors#vd11)、[HN15](/sources/hackernews#hn15)）。高频且必需的知识应放进常驻规则，低频或专项的才做成 skill（[第 02 章 §4](./02-context-engineering#_4-渐进式披露)）。
2. **按来源排优先级。** 自己团队写的 > 你所用产品的厂商官方 skill（B、C、D 组，能跟上 API 版本）> 安全公司或知名工程团队的（Trail of Bits、Sentry 等）> 社区方法论（E 组，借鉴后改写）> 大合集里的单个条目（F 组）。
3. **看维护信号，而不是星标。** 维护方是不是组织账号；最近一次推送的时间；是否标注了 Beta、Technical Preview、deprecated（例如 `openai/skills` 已弃用，`vercel-labs/next-skills` 已迁移）；有没有测试或评测；许可证是否清楚；是否附带脚本。
4. **少装，收进仓库，锁定版本。** 把选中的 skill 复制进仓库，或固定到某个 commit，纳入代码评审与 CODEOWNERS，不要让它跟着上游自动更新。数量宁少勿多，否则描述越多，误调用和上下文开销越大（[第 07 章「2026-11 新证据」](./07-harness-tools#new-evidence)）。
5. **用评测确认它有效。** 检查两件事：该用时会不会被触发，用了之后结果是否更好。可以用 H 组的 skill-up、waza、upskill，也可以用自己的 evals。换模型时重新跑一遍，参见 [第 12 章](./12-quality-cicd) 中 Evals 进 CI 的做法。

## 6. 安全：第三方 skill 的供应链风险 {#security}

skill 同时带有两类风险。一是代码风险：`scripts/` 里的脚本以你的权限运行。二是提示风险：`SKILL.md` 正文就是给模型的指令，`description` 还决定它会不会被选中。已有的公开数据如下（数字都来自原作者，未独立验证）：

| 发现 | 来源 | 证据性质 |
| --- | --- | --- |
| 扫描 ClawHub 与 skills.sh 的 3,984 个 skill：13.4% 至少有一个严重问题，36.82% 至少有一个任意级别的问题，人工确认 76 个恶意载荷（窃取凭据、植入后门、外传数据） | [Snyk ToxicSkills](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/)（数据截至 2026-02-05） | 厂商自报 |
| 对 ClawHub 2,857 个 skill 的审计发现 341 个恶意 skill，主攻击活动代号 ClawHavoc，投放 macOS 窃密木马 | [Snyk 文章转述](https://snyk.io/articles/skill-md-shell-access/) | 厂商自报 |
| 只改 `description` 字段，功能相同的恶意变体在配对试验中平均有 77.6% 被智能体选中；语义规避手法让恶意 skill 在 36.5%–100% 的情况下躲过拦截 | [arXiv 2605.11418](https://arxiv.org/abs/2605.11418) | 学术预印本 |
| 在 31,132 个 skill 的分析子集中，26.1% 含漏洞，5.2% 表现出疑似恶意意图 | [NVIDIA/SkillSpector README](https://github.com/NVIDIA/SkillSpector) | 厂商自报 |

**引入前的审查清单**

- [ ] **读完所有文件**，不只看 `SKILL.md`。重点查找 `curl … | sh`、下载后执行、base64 或混淆内容、隐藏 Unicode、读取 `~/.ssh` / `.env` / 浏览器数据的代码，以及「忽略之前的指令」「不要告诉用户」一类措辞。
- [ ] **把 `allowed-tools` 当作权限申请来审。** 它会预先放行工具，第三方 skill 不应该默认获得 shell 或网络权限。
- [ ] **用扫描器过一遍**（SkillSpector、腾讯 A.I.G 的 Skill Scan），并放进 CI。扫描只能降低风险，不能证明安全（见上表 arXiv 一行）。
- [ ] **锁定来源与版本**：从组织官方仓库安装，固定 commit，更新时重新审查 diff。注意同名、近似名和仿冒名，ClawHavoc 中就有仿冒 `clawhub` 的名字。
- [ ] **在沙箱中运行**：工作区外只读，网络走白名单，运行不受信任的 skill 时不把密钥放进环境变量（[第 09 章 §2](./09-security#_2-架构级防御)、[§5](./09-security#_5-一个最小安全基线)）。
- [ ] **纳入代码评审**：`.claude/`、`.agents/`、`.cursor/`、`.github/skills` 等目录加 CODEOWNERS（[第 09 章 §3](./09-security#_3-供应链-新的攻击面)、[TW12](/sources/thoughtworks#tw12)）。
- [ ] **留意工具自带的防线**：Gemini CLI 激活 skill 前会征求同意；Anthropic 的插件仓库提醒安装前须信任插件来源。这些都只是辅助，不能代替审查。

## 与传统软件工程认知的对比

| 维度 | 传统认知 | 智能体时代 | 判断 | 佐证（支持／异议） |
| --- | --- | --- | --- | --- |
| 引入依赖 | 包管理器 + 锁文件 + 漏洞扫描 | skill 也是依赖，而且是「会被执行的文档」。除代码扫描外，还要审查自然语言指令 | **延续并加强** | — |
| 文档 | 文档给人读，写错了影响有限 | `SKILL.md` 是模型会执行的指令，`description` 决定它是否被调用，需要像代码一样测试 | **修正** | — |
| 复用 | 复用越多越好 | 装得越多，可选描述越多，误调用与上下文成本也越高；宁少勿多，按失败驱动 | **修正** | [P13 · 355／20](/compare/evidence#p13) |
| 官方 SDK vs 社区封装 | 优先官方 SDK | 同样优先厂商官方 skill，因为它能跟上 API 版本；社区 skill 当参考 | **延续** | — |
| 流行度 | 星标多 ≈ 可靠 | 2026 年新仓库星标增长极快，注册表也遭到投毒；星标只反映关注度 | **谨慎** | — |

> 「佐证」列口径见 [共识度/佐证](/compare/evidence)；本章新增的判断尚未纳入全量库统计，用「—」表示。

**选择理由**：skill 生态的形态，很像早期的包管理生态：格式先统一，注册表随后爆发，接着就出现投毒与仿冒。传统供应链安全的做法（固定来源、锁版本、扫描、评审、最小权限）可以直接沿用。新增的部分是「自然语言也是攻击面」，所以审查时除了看代码，还要读指令。

**证据强度**：格式规范与各工具的加载路径来自官方文档，属于**事实**；星标与许可证是 2026-11-20 的 API 快照；仓库内容的数量与效果描述是**厂商自报 / 作者自述**；安全数据来自安全厂商报告与学术预印本，属于**待验证**；「宁少勿多、先确认会被调用」是**共识**，异议见第 07 章。

## 本章小结 {#summary}

- **定位**：skill 是按需加载的推理型 Guide，补的是「知道怎么做」。「一定做」靠第 04、12 章的确定性门禁，「做对了」靠第 05 章的验证。
- **怎么起步**：先用厂商官方 skill 和自己写的 `verify` skill；社区方法论（Superpowers、Matt Pocock、Addy Osmani）读懂后改写成团队自己的版本（§0.2）。
- **怎么维护**：数量宁少勿多，每个 skill 对应一个具体失败；放进仓库、纳入评审；变更和换模型时都要跑评测（第 05、07、12 章）。
- **怎么防**：第三方 skill 按依赖对待，审查、扫描、锁版本，并在沙箱中运行（§6、第 09 章）。
- **怎么用这份清单**：§4 用来查找，§0.2 用来起步。表中的星标是 2026-11-20 的快照，不代表质量。
