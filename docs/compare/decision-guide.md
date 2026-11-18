# 决策指南：什么时候用什么

> 当一线实践者意见不一时，如何根据你的情况做选择。每个决策给出「选 A 的条件」「选 B 的条件」与本手册的默认建议。

[[toc]]

## 1. 规则写进上下文，还是写成检查？

| 写进上下文（AGENTS.md / skill） | 写成检查（lint / 测试 / hook / CI） |
| --- | --- |
| 需要判断，无法机械判定 | 可以机械判定 |
| 允许有例外 | 不允许例外 |
| 偏好、风格倾向 | 架构不变量、安全约束 |

**默认**：能写成检查就写成检查；上下文只放「判断题」和指向文档的链接。来源：[AN01](/sources/anthropic#an01)、[VD19](/sources/vendors#vd19)、[OA01](/sources/openai#oa01)。

## 2. 知识常驻上下文，还是做成 skill？

| 常驻（AGENTS.md 索引） | 按需（skill / 子目录规则） |
| --- | --- |
| 几乎每个任务都需要 | 只有特定任务需要 |
| 模型训练数据里没有（新框架 API） | 篇幅大、细节多 |
| 必须保证被看到 | 允许模型判断是否需要 |

**默认**：高频必需 → 常驻索引；低频专项 → skill；**必须执行的流程不要只靠 skill**。来源：[VD11](/sources/vendors#vd11)、[TW18](/sources/thoughtworks#tw18)、[AN14](/sources/anthropic#an14)。

## 3. 要不要写规格？写多少？

| 轻量（提示 + Done when） | Plan Mode 计划 | 完整 SDD（spec-anchored） |
| --- | --- | --- |
| 单文件、明确的小改动 | 常规功能、几个文件 | 长程任务、跨模块、需长期维护的功能 |
| 失败成本低 | 中等 | 高 |

**默认**：按规模与风险升级；计划文件用完归档或删除。来源：[TW06](/sources/thoughtworks#tw06)、[PR28](/sources/practitioners#pr28)、[OA06](/sources/openai#oa06)。

## 4. 单智能体还是多智能体？

| 单智能体 + 子智能体 | 多智能体 |
| --- | --- |
| 大多数编码任务 | 天然可并行：批量迁移、广度调研、多视角评审 |
| 写操作集中在一处 | 有清晰的编排者与评判者 |
| 预算有限 | 任务价值足以覆盖数倍 token 成本 |

**默认**：单智能体 + 子智能体；多智能体时读并行、写单线程。来源：[VD05](/sources/vendors#vd05)、[VD06](/sources/vendors#vd06)、[AN12](/sources/anthropic#an12)、[VD03](/sources/vendors#vd03)。

## 5. TDD 要不要让智能体做？

| 让智能体 red/green | 人写关键测试 |
| --- | --- |
| 约束智能体先想清楚预期、防止过度实现 | 验收测试、核心业务规则、安全边界 |
| 测试质量由变异测试兜底 | 测试本身就是需求的权威表达 |

**默认**：两者结合——人写或审验收测试，智能体按 red/green 实现，变异测试检验测试质量。来源：[PR09](/sources/practitioners#pr09)、[TW04](/sources/thoughtworks#tw04)、[TW23](/sources/thoughtworks#tw23)。

## 6. 人要不要评审每一行？

| 逐行人工评审 | 自动检查 + 抽样 | 自动合并 |
| --- | --- | --- |
| 高影响、难回滚、难检测 | 中等风险，测试覆盖良好 | 低风险，失败易发现易回滚 |

**默认**：按概率 × 影响 × 可检测性分级；无论哪级，都有一个人对合并负责。来源：[TW16](/sources/thoughtworks#tw16)、[TW26](/sources/thoughtworks#tw26)、[AN19](/sources/anthropic#an19)、[X04](/sources/x-posts#x04)。

## 7. MCP 还是 CLI？

| CLI / 脚本 | MCP |
| --- | --- |
| 内部工具，人也要用 | 需要认证的第三方 SaaS |
| 需要组合、管道、脚本化 | 供应商已提供官方服务器 |
| 想节省上下文 | 跨多个智能体客户端复用 |

**默认**：内部能力优先 CLI；外部集成用 MCP，并纳入安全评审。来源：[PR18](/sources/practitioners#pr18)、[AN15](/sources/anthropic#an15)、[OS12](/sources/open-source#os12)、[X11](/sources/x-posts#x11)。

## 8. 门禁严一点还是松一点？

| 严（阻断） | 松（事后修正） |
| --- | --- |
| 架构不变量、安全、数据迁移 | 流程性等待（人工审批排队） |
| 低吞吐、回滚困难 | 极高吞吐、修正便宜、回滚容易 |

**默认**：不变量永远硬阻断；flaky test 不掩盖；流程性门禁随吞吐量与回滚能力调整。来源：[OA01](/sources/openai#oa01)、[AN18](/sources/anthropic#an18)。

## 9. 自建智能体还是用现成的？

| 用现成编码智能体 + 定制 harness | 自建智能体 |
| --- | --- |
| 软件开发场景 | 嵌入自有产品、特殊工作流 |
| 团队不想维护智能体循环 | 需要完全掌控上下文与控制流 |

**默认**：开发场景用现成工具；自建时拥有你的提示、上下文与控制流，谨慎依赖高层框架抽象。来源：[OS02](/sources/open-source#os02)、[PR19](/sources/practitioners#pr19)、[OA07](/sources/openai#oa07)、[AN09](/sources/anthropic#an09)。

## 10. 规则越来越多了，删哪些？

每条规则问三个问题：

1. 它针对的失败最近还发生吗？（在当前模型上去掉它跑一遍回归集）
2. 它能被机械检查替代吗？
3. 它与其他规则冲突吗？

**默认**：每换一代模型做一次 progression testing。来源：[TW20](/sources/thoughtworks#tw20)、[X07](/sources/x-posts#x07)、[AN30](/sources/anthropic#an30)。
