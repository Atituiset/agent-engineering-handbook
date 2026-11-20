# 11 · 速查表

[[toc]]

## 要点

- 本章只收**可直接复制**的清单与模板，理由与证据都在对应章节，每条后面的编号可回查来源。
- 新仓库从第 1 节「第一周清单」开始；写规则前先用第 5 节判断它该放在哪一层。
- 流水线与合并门禁看第 11 节（摘自第 12 章），引入第三方 skill 看第 12 节（摘自第 13 章）。
- 每换一代模型，用第 10 节复盘 harness，删掉不再需要的东西。

> 可直接复制使用的清单与模板。每条后面的编号可回查来源。

## 1. 新仓库接入智能体：第一周清单

- [ ] 测试、lint、类型检查、构建都能**一条命令**跑通，且足够快（[X04](/sources/x-posts#x04)）
- [ ] 应用能在本地/worktree 一键启动，日志可读（[OA01](/sources/openai#oa01)、[PR17](/sources/practitioners#pr17)）
- [ ] 写一份不超过约 100 行的 AGENTS.md：命令、边界、非标准约定、坑点、文档索引（[OA01](/sources/openai#oa01)、[VD19](/sources/vendors#vd19)）
- [ ] 格式化与 lint 用 hook 自动执行（[AN03](/sources/anthropic#an03)）
- [ ] 受保护文件（CI、lint 配置、架构测试、迁移）禁止智能体修改（[AN18](/sources/anthropic#an18)）
- [ ] 把最重要的 3–5 条架构规则写成可执行检查（[OS13](/sources/open-source#os13)、[OS14](/sources/open-source#os14)、[OS15](/sources/open-source#os15)）
- [ ] 沙箱：工作区外只读、网络白名单（[AN27](/sources/anthropic#an27)）
- [ ] 指定一名负责人维护 harness（[X04](/sources/x-posts#x04)）

## 2. AGENTS.md 模板

```markdown
# AGENTS.md

## 命令
- 安装：pnpm install
- 测试：pnpm test            # 改动后必须通过
- 单测某文件：pnpm test path/to/file
- Lint + 类型：pnpm check
- 启动：pnpm dev             # 日志见 ./logs/dev.log

## 边界
- 总是：改动后运行 pnpm check 与相关测试
- 先问：新增依赖；修改公共 API；数据库迁移
- 绝不：修改 ci/、.eslintrc*、tests/architecture/；提交密钥

## 非标准约定（模型不可能猜到的）
- 领域层禁止直接 import 基础设施层，经 ports/ 接口访问（由 tests/architecture 强制）
- 金额一律用 Money 类型，禁止 number
- 时间统一 UTC，展示层再转换

## 坑点
- orders 模块的 legacyStatus 字段仍被外部系统读取，不能删
- 本地测试需要先启动 docker compose up db

## 更多文档（按需阅读）
- 架构总览：docs/architecture.md
- ADR：docs/adr/
- 领域术语：docs/glossary.md
```

依据：命令前置、边界三级（[BT16](/sources/bigtech#bt16)）；只写非标准实践（[RS06](/sources/research#rs06)）；地图而非百科（[OA01](/sources/openai#oa01)）；坑点优先（[X07](/sources/x-posts#x07)）。

## 3. 任务说明模板

```markdown
## Goal
（要达成什么，用户可见的结果）

## Context
- 相关文件：
- 报错 / 截图：
- 参考：

## Constraints
- 不改动：
- 必须遵守：
- 不做（范围外）：

## Done when
- [ ] 测试 xxx 通过（先写失败测试，确认红，再实现）
- [ ] pnpm check 通过
- [ ] 本地启动后，在 /path 能看到 xxx
- [ ] 附手工验证记录
```

依据：Goal / Context / Constraints / Done when（[OA04](/sources/openai#oa04)）；red/green（[PR09](/sources/practitioners#pr09)）；手工验证（[PR13](/sources/practitioners#pr13)）。

## 4. 选流程：任务规模速查

| 任务 | 流程 |
| --- | --- |
| 改文案、小 bug、明确的单文件修改 | 直接一段提示 + Done when |
| 常规功能（几个文件） | Plan Mode → 人审计划 → 新上下文执行 → 自证 |
| 跨模块功能 / 存量大代码库 | 研究 → 计划 → 实现，每阶段产物人审（[VD20](/sources/vendors#vd20)） |
| 长程 / 绿地大项目 | 规格 + 里程碑 + 进度文件 + 功能清单（[OA06](/sources/openai#oa06)、[AN17](/sources/anthropic#an17)） |
| 批量迁移 | 人写迁移手册与样例 → 智能体并行执行 → 差分测试（[VD08](/sources/vendors#vd08)、[AN18](/sources/anthropic#an18)） |

## 5. 规则该放哪儿

```text
这条规则能被机器判定吗？
├─ 能 → 必须无例外吗？
│       ├─ 是 → lint / 结构测试 / hook / CI（硬门禁）
│       └─ 否 → lint 警告 + 观察模式
└─ 不能 → 每个任务都需要吗？
        ├─ 是 → AGENTS.md（一行，必要时链接文档）
        └─ 否 → skill / 子目录规则 / docs 按需
写进去之后仍反复被违反？→ 尝试机械化；做不到 → 升级为人工评审重点
换了新模型？→ 逐条验证是否还需要，删掉多余的
```

依据：[AN01](/sources/anthropic#an01)、[TW01](/sources/thoughtworks#tw01)、[TW20](/sources/thoughtworks#tw20)、[AN18](/sources/anthropic#an18)。

## 6. 提交 PR 前自查（作者）

- [ ] 我运行过，亲眼看到它工作（[PR04](/sources/practitioners#pr04)）
- [ ] 测试先失败后通过；没有删除、跳过、放宽任何测试（[PR09](/sources/practitioners#pr09)、[PR15](/sources/practitioners#pr15)）
- [ ] 没有修改 CI、lint 配置、架构测试
- [ ] 没有新增未经确认的依赖（[SC04](/sources/security#sc04)）
- [ ] diff 足够小；无关改动已拆出（[PR12](/sources/practitioners#pr12)）
- [ ] 我理解每一处改动，能回答评审者的问题（[X04](/sources/x-posts#x04)、[PR27](/sources/practitioners#pr27)）
- [ ] PR 描述我读过并修改过；附验证证据
- [ ] 已用 AI 评审自查一轮并处理（[CN01](/sources/chinese#cn01)）

## 7. 评审者速查（按风险）

| 风险 | 看什么 |
| --- | --- |
| 低 | 自动检查是否全绿；范围是否符合描述 |
| 中 | 是否符合计划与架构约定；测试是否真的断言了行为（变异测试分数）；有无重复抽象 |
| 高 | 前置方案是否评审过；逐行；失败模式与回滚方案；安全与数据影响 |

依据：[TW26](/sources/thoughtworks#tw26)、[TW16](/sources/thoughtworks#tw16)、[AN19](/sources/anthropic#an19)、[TW23](/sources/thoughtworks#tw23)。

## 8. 会话卫生

- 一个任务一个会话；新任务开新会话（[CN11](/sources/chinese#cn11)）
- 走错路就回溯，不要追加纠正（[CN11](/sources/chinese#cn11)）
- 计划确认后在新上下文中执行（[X08](/sources/x-posts#x08)）
- 噪声大的工作交给子智能体（[TW28](/sources/thoughtworks#tw28)）
- 上下文接近一半就考虑把进展写成文件、重开（[VD20](/sources/vendors#vd20)）

## 9. 安全基线

- [ ] 至少切断致命三要素中的一条边（[SC01](/sources/security#sc01)）
- [ ] 沙箱 + 网络白名单（[AN27](/sources/anthropic#an27)、[TW24](/sources/thoughtworks#tw24)）
- [ ] 专用、最小权限、短期凭据；机密不进上下文
- [ ] 规则文件 / hooks / MCP 配置纳入代码评审（[TW12](/sources/thoughtworks#tw12)）
- [ ] 新增依赖人工确认（[SC03](/sources/security#sc03)）
- [ ] 危险命令 deny 规则

## 10. 每季度（或每换一代模型）的 harness 复盘

- [ ] 用 10–20 个代表任务组成的回归集跑一遍（[AN31](/sources/anthropic#an31)）
- [ ] 逐条检查 AGENTS.md / skills / hooks：它解决的失败还会发生吗？（[TW20](/sources/thoughtworks#tw20)、[AN30](/sources/anthropic#an30)）
- [ ] 删除过时文档与计划文件（[TW31](/sources/thoughtworks#tw31)）
- [ ] 看指标：回滚率、缺陷逃逸、评审等待、规则违规趋势（[TW32](/sources/thoughtworks#tw32)）
- [ ] 把反复出现的评审意见升级为机械检查（[OA01](/sources/openai#oa01)）

## 11. CI 与合并门禁（摘自第 12 章）

- [ ] 主分支规则集：必需检查 + 至少一位人工批准 + 禁止绕过；智能体账号不在可批准者之列，发起任务的人也不能批准该 PR（[QT15](/sources/quality/tools#qt15)、[QT16](/sources/quality/tools#qt16)）
- [ ] 测试改动守卫 + CODEOWNERS：删测试、断言变少、快照被批量重写时要求指定的人批准（[第 12 章示例 B](./12-quality-cicd#example-b)）
- [ ] CI 回合数设上限，超过就交回人（[QB01](/sources/quality/bigtech#qb01)）
- [ ] AI 评审以建议性方式运行，只报高严重度问题，记录解决率（[QT10](/sources/quality/tools#qt10)、[QT21](/sources/quality/tools#qt21)）
- [ ] prompts、skills、agent 配置的改动触发回归评测（[第 12 章示例 C](./12-quality-cicd#example-c)）
- [ ] CI 里的 AI 步骤不在 `pull_request_target` 中拿密钥，fork PR 不给密钥（[QT05](/sources/quality/tools#qt05)、[QT06](/sources/quality/tools#qt06)）
- [ ] 开启合并队列（[QT17](/sources/quality/tools#qt17)）

完整清单（第一周 / 第一个月 / 每季度）见 [第 12 章 §5](./12-quality-cicd#checklist)。

## 12. 引入第三方 skill（摘自第 13 章）

- [ ] 先问：这个 skill 解决的是哪一个反复出现的失败？说不出来就不装（[第 13 章 §5](./13-skills-catalog#choose)）
- [ ] 读完所有文件，不只看 `SKILL.md`；把 `allowed-tools` 当作权限申请来审
- [ ] 扫描器过一遍并进 CI；扫描只能降低风险，不能证明安全
- [ ] 从官方仓库安装，固定 commit；更新时重新审 diff
- [ ] 在沙箱中运行，不把密钥放进环境变量；skill 目录加 CODEOWNERS（[第 09 章 §3](./09-security#_3-供应链-新的攻击面)）
- [ ] 换模型时重新评估，确认它仍会被调用、仍有帮助（[XC-021](/sources/x/context#xc-021)）

逐项说明与公开的恶意 skill 数据见 [第 13 章 §6](./13-skills-catalog#security)。

## 与传统软件工程认知的对比

这些清单里大部分条目并不新：一键构建、快速测试、小 PR、最小权限、代码评审、ADR、度量交付结果——都是经典的工程纪律。新增的只有三类：

1. **面向智能体的上下文管理**（AGENTS.md 写法、会话卫生、按需加载）；
2. **保护检查本身**（受保护文件、规则从基础分支读取、监视作弊）；
3. **harness 的定期删减**（progression testing）。

**选择理由**：如果你的团队已经有扎实的工程基础，接入智能体的大部分工作是「把已有纪律机械化并对智能体可读」；如果没有，智能体会以更快的速度放大这些缺失（[RS03](/sources/research#rs03)）。先补基础，再谈提效。
