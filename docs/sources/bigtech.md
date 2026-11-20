# Google · Meta · Microsoft/GitHub

> 三家美国大厂的官方工程博客、文档与论文。涉及内部采纳率、效率等数字均为 **「厂商自报、尚未独立验证」**。链接于 2026-11-18 核对。

[[toc]]

## Google

### BT01 · Gemini CLI（开源仓库） {#bt01}
**机构**：Google｜**日期**：持续更新｜[原文](https://github.com/google-gemini/gemini-cli)

Google 开源的终端编码智能体。仓库文档覆盖 GEMINI.md 上下文文件、MCP 扩展、检查点、沙箱、可信目录等机制，是研究「大厂 harness 默认如何设计权限与上下文」的一手资料。

### BT02 · Provide context with GEMINI.md files {#bt02}
**机构**：Google（Gemini CLI 文档）｜**日期**：2026-06 更新｜[原文](https://geminicli.com/docs/cli/gemini-md/)

GEMINI.md 支持全局、工作区与子目录三级自动加载，可用 `/memory show` 查看实际注入了什么、`/memory reload` 刷新。建议写入技术栈、风格、测试与架构规则及明确的「不要做」，保持简洁并定期更新。

`厂商文档`

### BT03 · Conductor: Introducing context-driven development for Gemini CLI {#bt03}
**机构**：Google Developers Blog｜**日期**：2025-12-17｜[原文](https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/)

Conductor 把项目认知从「易逝的聊天记录」搬进仓库里的持久文件：先建立产品、准则、技术栈与工作流文档，再为每项工作创建 track（含 `spec.md` 与 `plan.md`），人审批计划后执行并跟踪进度。本质是 Google 版的规格驱动开发。

### BT04 · Conductor Update: Introducing Automated Reviews {#bt04}
**机构**：Google Developers Blog｜**日期**：2026-02-13｜[原文](https://developers.googleblog.com/conductor-update-introducing-automated-reviews/)

为 Conductor 增加「verify」步骤：智能体完成任务后，自动检查代码是否符合计划与准则、风格是否一致、并执行安全检查，让 AI 辅助开发「更安全、更可预期」。

### BT05 · gemini-cli-extensions/conductor（开源仓库） {#bt05}
**机构**：Google｜**日期**：持续更新｜[原文](https://github.com/gemini-cli-extensions/conductor)

Conductor 的实现与模板，可直接参考其 product/guidelines/tech-stack/workflow 文件结构来设计自己的规格与计划模板。

### BT06 · Agent Development Kit（ADK）文档 {#bt06}
**机构**：Google｜**日期**：持续更新｜[原文](https://google.github.io/adk-docs/)

Google 的开源智能体开发框架文档，涵盖智能体、工具、会话/状态/记忆、多智能体编排、评测与部署。

### BT07 · Architecting efficient context-aware multi-agent framework for production {#bt07}
**机构**：Google Developers Blog（ADK 团队）｜**日期**：2025-12-04｜[原文](https://developers.googleblog.com/en/architecting-efficient-context-aware-multi-agent-framework-for-production/)

反对「靠更大的上下文窗口硬塞」：把**持久状态（Session）**与**每次调用的视图（working context）**分开，分层管理会话、记忆与制品（artifacts），多智能体之间默认最小化共享上下文（scope by default）。这是把上下文当作「架构关注点」而非提示技巧的代表文章。

### BT08 · AI in software engineering at Google: Progress and the path ahead {#bt08}
**作者**：Satish Chandra、Maxim Tabachnyk（Google）｜**日期**：2024-06-06｜[原文](https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/)

回顾 Google 内部 AI 辅助编码的进展：代码补全被工程师接受率约 37%，辅助完成了约 50% 的代码字符；强调改进来自模型、上下文构建启发式、基于真实接受/拒绝日志的调优与 UX 的共同作用，并展望从补全走向更大粒度任务。

`厂商自报`

### BT21 · How is Google using AI for internal code migrations? {#bt21}
**机构**：Google｜**日期**：2025-01｜[原文](https://arxiv.org/abs/2501.06972)

Google 用 LLM 做内部代码迁移的经验报告。作者明确说这不是对照研究，没有与其他方法比较，而是分享在企业环境中多个迁移案例的经验。结论是 LLM 可以显著缩短迁移所需时间，并降低启动和完成迁移项目的门槛。

`经验报告（团队自报）`

## Meta

### BT09 · Revolutionizing software testing: LLM-powered bug catchers（ACH） {#bt09}
**机构**：Engineering at Meta｜**日期**：2025-02-05｜[原文](https://engineering.fb.com/2025/02/05/security/revolutionizing-software-testing-llm-powered-bug-catchers-meta-ach/)

ACH 是「变异引导的 LLM 测试生成」：针对某类关注点（如隐私回归）先生成未被现有测试发现的缺陷（mutants），再用这些 mutants 生成能抓住它们的测试。思路对 AI 时代很关键：**用变异来检验测试是否真的有效**，而不是只看覆盖率。

### BT10 · Automated Unit Test Improvement using LLMs at Meta（TestGen-LLM） {#bt10}
**作者**：Alshahwan 等（Meta）｜**日期**：2024-02（arXiv）｜[原文](https://arxiv.org/abs/2402.09171)

TestGen-LLM 自动改进已有人工测试，并让每个生成的测试类通过一组过滤器（能构建、稳定通过、确实提升覆盖），以此「消除幻觉问题」。核心思想是：**LLM 产出只有经过确定性过滤才被采纳**，这与今天的「验证回路」一脉相承。

### BT11 · How Meta Used AI to Map Tribal Knowledge in Large-Scale Data Pipelines {#bt11}
**机构**：Engineering at Meta｜**日期**：2026-04-06｜[原文](https://engineering.fb.com/2026/04/06/developer-tools/how-meta-used-ai-to-map-tribal-knowledge-in-large-scale-data-pipelines/)

AI 助手只与它对代码库的理解一样好。Meta 用 50 多个专门智能体系统性阅读一个大型数据管线的每个文件，产出 59 份精炼的上下文文件，把隐性的「部落知识」显性化；初步测试显示每个任务的智能体工具调用减少约 40%，且知识层与模型无关。

`厂商自报、尚未独立验证`

### BT12 · How Meta Built Forum With AI-Native Engineering {#bt12}
**机构**：Engineering at Meta｜**日期**：2026-10-15｜[原文](https://engineering.fb.com/2026/10/15/ml-applications/how-meta-built-forum-ai-native-engineering/)

小团队从零构建 Forum App，把智能体当作工程流程的参与者而非「更快的打字机」。成功的定义不是代码量，而是「能构建、过测试、经得起评审」的已验证结果；把完成标准从「能编译」提高到「自动化测试与视觉检查通过」；把规划当作技术规格来写，因为人能凭直觉消化的歧义会直接导致智能体失败；工程师的职责从执行步骤变为「拥有结果、守住质量线」。

> "Compiling isn’t the finish line — a task is complete only once automated tests and visual checks have passed."

## Microsoft / GitHub

### BT13 · Adding repository custom instructions for GitHub Copilot {#bt13}
**机构**：GitHub Docs｜**日期**：持续更新｜[原文](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions)

说明 `.github/copilot-instructions.md`（仓库级）、`.github/instructions/*.instructions.md`（按路径生效）以及对 AGENTS.md 的支持，建议写入技术栈、项目结构、编码与测试规范、构建命令。

`厂商文档`

### BT14 · Best practices for using GitHub Copilot to work on tasks {#bt14}
**机构**：GitHub Docs｜**日期**：持续更新｜[原文](https://docs.github.com/en/copilot/tutorials/coding-agent/get-the-best-results)

把分配给 coding agent 的 issue 当作提示：写清问题、验收标准与涉及文件；适合交给智能体的是范围清晰的任务，而复杂、跨仓库、需要深厚领域知识或涉及生产关键/安全敏感逻辑的任务更适合人自己做。还建议配置开发环境与仓库指令。

`厂商文档`

### BT15 · Spec-driven development with AI: Get started with a new open source toolkit {#bt15}
**机构**：The GitHub Blog｜**日期**：2025-09-02｜[原文](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)

发布 Spec Kit（见 [OS03](./open-source#os03)）：把规格作为「可执行的事实源」，按 Specify → Plan → Tasks → Implement 分阶段推进，每阶段都有人工检查点，可配合任意 AI 编码工具使用。

### BT16 · How to write a great agents.md: Lessons from over 2,500 repositories {#bt16}
**机构**：The GitHub Blog｜**日期**：2025-11-19｜[原文](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)

基于对 2,500 多个仓库 agents.md 的分析给出写法建议：把可执行命令放在前面、用代码示例代替长段解释、明确技术栈与版本、写清边界（总是做 / 先询问 / 绝不做）、覆盖命令、测试、项目结构、代码风格、Git 流程等关键领域。

### BT17 · WRAP up your backlog with GitHub Copilot coding agent {#bt17}
**机构**：The GitHub Blog｜**日期**：2025-12-26｜[原文](https://github.blog/ai-and-ml/github-copilot/wrap-up-your-backlog-with-github-copilot-coding-agent/)

用 WRAP 助记法使用 coding agent：写好 issue（Write effective issues）、打磨指令（Refine your instructions）、拆成原子任务（Atomic tasks）、与智能体结对（Pair with the coding agent）。

### BT18 · From one-off prompts to workflows: custom agents in GitHub Copilot CLI {#bt18}
**机构**：The GitHub Blog｜**日期**：2026-06-09｜[原文](https://github.blog/ai-and-ml/github-copilot/from-one-off-prompts-to-workflows-how-to-use-custom-agents-in-github-copilot-cli/)

介绍用自定义智能体（`.github/agents/*.agent.md`）让 Copilot CLI 理解团队技术栈与流程，把一次性的终端提示变成可复用、可评审的流程。

### BT19 · Custom agents（GitHub Docs） {#bt19}
**机构**：GitHub Docs｜**日期**：持续更新｜[原文](https://docs.github.com/en/copilot/concepts/customizations/custom-agents)

自定义智能体配置文件可声明用途、指令、护栏与有限的工具白名单，适合为评审、测试、文档等反复出现的专门角色建立「岗位说明书」。

`厂商文档`

### BT22 · GitHub Copilot code referencing：与公开代码匹配时的提示 {#bt22}
**机构**：GitHub Docs｜**日期**：持续更新（2026-11 核对）｜[原文](https://docs.github.com/en/copilot/concepts/completions/code-referencing)

Copilot 生成的代码可能与 GitHub 公开仓库中的代码相同。按账户或组织的策略，匹配的建议可以被拦截，或附上匹配代码的位置与检测到的许可证；云端委派任务的会话日志里也会附上匹配详情。文档称匹配通常出现在不到 1% 的行内建议中（厂商自报）。

### BT20 · GitHub Copilot 云端会话：客户端、会话与环境 {#bt20}
**机构**：GitHub Docs｜**日期**：持续更新（2026-11 核对）｜[原文](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent)

把 Copilot 云端智能体拆成三个概念：客户端（网页、IDE、手机、CLI）、会话（提示与智能体的活动记录）、环境（云端沙箱、GitHub Actions runner 或远程自定义环境）。2026-10-28 起付费用户可用新的「Copilot in the cloud」体验，会话可以在不同客户端之间接续。委派的任务可使用自定义智能体、agent skills、仓库级 MCP 服务器，hooks 可在智能体工作中运行命令做校验或记录；跨会话的 Copilot Memory 与单次会话的上下文分开。护栏与风险缓解见 [QT15](./quality/tools#qt15)。

`厂商文档`

