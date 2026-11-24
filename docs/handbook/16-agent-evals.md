# 16 · 智能体评测：从回归集到可信的分数

[[toc]]

## 要点

- **评测先管住评分器，再谈分数。** 智能体能改测试、读答案、钻评分脚本的空子。2026-11 的一项研究在移植基准时跑了 429 次攻击，原评分器放过了其中 230 次；把期望答案交给智能体碰不到的评分方之后，一次都没放过（[EV01](/sources/evals#ev01)，作者自报）。另一项审计在 10 个热门基准里找到 219 个缺陷，大多数基准不解决任务也能拿到接近满分（[EV02](/sources/evals#ev02)，作者自报）。
- **LLM 裁判是要校准的分类器。** 看 kappa 和「失败类」的召回率，不只看一致率；裁判换版本要先做锚点审计（[EV05](/sources/evals#ev05)）；两两比较要换位各问一次（[EV03](/sources/evals#ev03)）；裁判最好不要和被评的模型同源（[EV04](/sources/evals#ev04)）。
- **多跑几次，报区间。** 回归集看 pass^k（k 次全成功），能力集看 pass@k（k 次至少一次）。资源配置这类基础设施差异就能让同一模型的分数相差 6 个百分点，3 个百分点以内的榜单差距在配置对齐前都应存疑（[EV06](/sources/evals#ev06)，厂商自报）。
- **线上和线下是一个循环。** 生产 trace 抽样打分，失败的 trace 回流进数据集，变成下次 PR 必跑的用例（[EV16](/sources/evals#ev16)、[EV19](/sources/evals#ev19)）。美团、字节、阿里、蚂蚁的公开实践都是这个形状（§4）。
- **本章配了一套能跑的最小评测：[`examples/evals/`](https://github.com/Atituiset/agent-engineering-handbook/tree/main/examples/evals)。** 它用模拟智能体，不需要 API key，包括多次试验的 harness、隔离评分、回归门禁、裁判校准、配对漏洞评测，以及 promptfoo 和 Inspect 两个框架版本。所有输出都是 2026-11-24 在本机实测的（§7）。

## 0. 和前几章的关系 {#relation}

前面几章已经讲过评测的基本盘，这一章不重复，只往深处走：

| 已有内容 | 讲了什么 | 本章往下补什么 |
| --- | --- | --- |
| [第 05 章 §8](./05-verification#_8-评测-为团队的-harness-建回归) | 为团队的 harness 建 10–20 个任务的回归集；同时看结果和过程；pass@k 与 pass^k；别拿公开基准代替自己的评测 | 任务怎么设计、评分器怎么隔离（§1、§3），基准分数怎么读（§5） |
| [第 12 章 Q08](./12-quality-cicd#q08) 与 [示例 C](./12-quality-cicd#example-c) | Evals 即 CI：黄金集、回归集，裁判要对齐人工标签；一个 evals 工作流的骨架 | 裁判校准的具体指标与版本漂移（§2）；示例 C 里的 `run.py` / `compare.py` 的一个能跑的实现（§7） |
| [第 12 章 Q04](./12-quality-cicd#q04) | 防作弊：禁止删改测试，警惕 reward hacking | 评分器的权限分离，轨迹检查（§3） |
| [第 10 章 #18](./10-anti-patterns#_18-只信-ci-的绿灯、只看评测总分) | 只信 CI 绿灯、只看评测总分 | 逐题对比、置信区间、笨基线（§5、§8） |

## 1. 评测类型与设计 {#design}

### 1.1 先分清三种评测

| 类型 | 回答什么问题 | 典型指标 | 失败时怎么办 |
| --- | --- | --- | --- |
| **回归评测** | 改了提示词、skill、hook 或换了模型之后，原来会的还会不会 | pass^k、逐题 pass@1 不下降 | 阻止合并 |
| **能力评测** | 智能体能不能做到以前做不到的事 | pass@k、带置信区间的成功率 | 记录趋势，不阻止合并 |
| **线上评测** | 真实用户、真实分布下表现怎样 | 抽样打分、用户反馈、成本与延迟 | 告警，失败样本回流进回归集 |

Anthropic 把评测拆成任务、试验（trial）、评分器、过程记录（transcript）和最终结果（outcome），并区分能力评测和回归评测（[QT01](/sources/quality/tools#qt01)）。能力集里的题一旦稳定通过，就该「毕业」进回归集。评测本身也有两件完全不同的事：发现有哪些失败模式，以及度量每种失败有多常见（[QX16](/sources/quality/x#qx16)）。前者靠人看过程记录，后者才轮到自动评测。

### 1.2 任务从哪来

- **从真实失败里来。** 建议先攒 20–50 个（[QT01](/sources/quality/tools#qt01)）。每个任务写明来源，例如「哪次 PR 回滚」「哪条工单」，示例里的 `task.json` 有专门的 `source` 字段。
- **从生产录制里来。** 蚂蚁的做法是录制真实交互并回放，沉淀成可复用的评测集，让回归有真实分布的数据（[AL29](/sources/quality/chinese#al29)）。百度 Comate 从经人审核合入的真实提交里挖评测集（[CN40](/sources/chinese#cn40)）。
- **要有「不该做」的题。** 阿里的 AACR-Bench 除了 200 个真实 PR，还附了 155 个 PR 的负样本集，度量的是评审该不该保持沉默（[AL11](/sources/quality/research#al11)）。只有正样本的评测会奖励「多报」。
- **按领域建。** 支付宝的 PIBench 在真实支付集成任务上比较「带 skill / 不带 skill」两种条件的 rubric 通过率（[AL31](/sources/quality/research#al31)），这也是评估 skill 本身价值的思路（[第 13 章](./13-skills-catalog)）。

### 1.3 评分器：能确定性就确定性

按可靠程度排：

1. **确定性检查最终状态。** 隐藏测试、数据库状态、文件 diff。智能体说「修好了」不算，测试过了才算（[第 05 章 §8](./05-verification#_8-评测-为团队的-harness-建回归)）。
2. **带依据的模型评分。** 阿里 AgentLoop 让评估智能体调用工具去查证，再给出分数和依据，而不是只让 LLM 凭印象打分（[AL22](/sources/quality/chinese#al22)）。
3. **纯 LLM 裁判。** 用在开放性质量上，并且必须先校准（§2）。
4. **人工复核。** 用来给裁判定标签，以及抽查。

一个本手册的建议（不是哪篇来源的结论）：rubric 尽量拆成多个二元判断（「是否引用了出错行」「是否给出可执行的修复」），比 1–10 分的总分更容易校准，也更容易在版本漂移时发现问题。

### 1.4 多次试验与统计

- 每个任务跑 n 次，数出成功次数 c，用无偏估计算 pass@k = 1 − C(n−c, k) / C(n, k) 和 pass^k = C(c, k) / C(n, k)（后者来自 τ-bench，[RS10](/sources/research#rs10)）。示例的 `harness/metrics.py` 就是这两个公式，Inspect 内置的 `pass_at_{k}`、`pass_k_{k}` reducer 算出来的数一样（§7.4，[EV13](/sources/evals#ev13)）。
- 总成功率要附置信区间。示例用 Wilson 区间：30 次试验成功 26 次，点估计 86.7%，95% 区间是 70.3%–94.7%。区间这么宽，说明几十次试验只够发现大的退化。
- 同时记录成本、token 和延迟的分位数。只看成功率会奖励「多试几次总能对」的昂贵策略。

## 2. LLM 裁判：校准、偏差与漂移 {#judge}

### 2.1 校准：把裁判当分类器测

[第 12 章 Q08](./12-quality-cicd#q08) 已经说过：裁判本质是分类器，要对照人工标签测（[QX14](/sources/quality/x#qx14)、[QP12](/sources/quality/practitioners#qp12)）。具体看这几个数：

| 指标 | 为什么要看 |
| --- | --- |
| **失败类的召回率** | 评测是为了抓坏输出。裁判漏判失败的比例才是最要紧的 |
| **失败类的精确率** | 误判太多，团队就会开始忽略裁判 |
| **Cohen's kappa** | 扣掉偶然一致后的一致程度。失败样本少的时候，一致率会严重高估裁判 |
| **永远判「通过」的笨基线** | 给上面几个数一个参照。裁判必须明显好过它 |

示例里的 `judge/calibrate.py` 在 40 条人工标签上（其中 8 条失败，数据为人工构造）跑出来是这样：

```text
[always_pass (dumb baseline)] agreement=0.800 kappa=0.000 fail_recall=0.000 ...
[judge_v1] agreement=0.925 kappa=0.754 fail_recall=0.750 fail_precision=0.857 ...
[judge_v2] agreement=0.875 kappa=0.490 fail_recall=0.375 fail_precision=1.000 ...
```

永远判「通过」也有 80% 的一致率，但 kappa 是 0，一个失败都抓不到。judge_v2 的一致率 87.5% 看着还行，失败召回率却只剩 37.5%。示例的门禁按 kappa ≥ 0.6、失败召回率 ≥ 0.7 判定，v1 通过，v2 不通过。阈值是示例自己定的，你的团队要按「漏掉一个失败的代价」来定。

### 2.2 三种偏差

- **位置偏差与冗长偏差。** MT-Bench 的论文系统讨论了这些偏差，并给出一个保守做法：两个回答换位各问一次，两种顺序下都胜出才算赢，否则算平局（[EV03](/sources/evals#ev03)）。示例的 20 对两两比较里，换位后结论一致的有 15 对；不一致的 5 对中有 4 对都是「谁在前面谁赢」。
- **自我偏好。** 研究发现模型能认出自己的输出，自我识别能力越强，给自己打分的偏高程度越强（[EV04](/sources/evals#ev04)）。所以裁判最好不要和被评的生成模型同源；做不到的话，至少在报告里写清楚。
- **继承被评模型的问题。** LLM 生成的评估器会继承被评估 LLM 的问题（[QP15](/sources/quality/practitioners#qp15)）。

### 2.3 版本漂移：裁判换了，标准就变了

裁判模型升级时，不能默认「新裁判更严格」。一项预注册研究给同系列开源模型各升级一次：有的变宽松，有的变严格；Mistral-Small 3.1→3.2 均值看着变宽松了，但 93% 的分数都落在同一个值上，前 30% 的入选集合有 59% 换了人（[EV05](/sources/evals#ev05)，作者自报，评的是研究提案而不是代码）。作者把后果分成三类：整体平移、排序变化、分辨力丧失；只做全局的分数重新映射修不好后两类。

落到工程上：

- **把裁判的模型版本和提示词一起钉死**，像依赖版本一样写进配置。
- **换版本前先跑校准集。** 示例里 v1→v2 有 6/40（15%）条判决翻转，kappa 从 0.754 掉到 0.490，门禁直接拦下。研究里建议的规模是约 200 次调用的分层锚点审计（[EV05](/sources/evals#ev05)）。
- **基线要和裁判版本绑定。** 裁判换了，历史分数就不能直接比了。

## 3. 轨迹与工具调用：防作弊和评分器隔离 {#trajectory}

### 3.1 智能体会钻评分器的空子

- 能访问单元测试的智能体，可能会删掉失败的测试，而不是修 bug（[QR02](/sources/quality/research#qr02)）。
- OpenAI 用另一个模型监控思维链，能发现「颠覆测试」这类行为；但在训练里惩罚这些想法，模型会学会隐藏意图（[QT14](/sources/quality/tools#qt14)）。
- 「已解决」的补丁可能只是通过了不够穷尽的测试（[QR05](/sources/quality/research#qr05)）。
- BenchJack 在软件工程、网页、桌面、终端四类 10 个基准里归纳出 8 类缺陷，作者的判断是评测流水线还没有形成对抗思维（[EV02](/sources/evals#ev02)）。

### 3.2 权限分离：答案不进智能体的环境

SplitBench 的思路很直接：智能体的代码只在测试环境里运行，期望答案只在一个可信的评分方手里，测试环境就算被完全接管也伪造不出「通过」（[EV01](/sources/evals#ev01)）。论文报告的数字（作者自报）：

- 从 Terminal-Bench 2.0 和 DeepSWE v1.1 移植了 202 个任务中的 180 个，中位成本约每任务 10 美元，和原评分器在 98.7% 的尝试上结论一致。
- 资格检查的 429 次攻击中，原评分器放过了 230 次，SplitBench 一次也没放过。其中一次是在「修复代码漏洞」任务里直接删掉有漏洞的文件。
- 局限：需要计时、联网、跨多次运行的任务，这种方式判不了。

对团队自建评测，可以落地成三条：

1. **隐藏测试和评分脚本放在智能体的工作区之外**，评分时把智能体的产物拷到一个干净目录，再放入隐藏测试运行。示例用目录隔离演示，真实场景要放到另一个容器或机器上。
2. **受保护路径做哈希比对。** 测试目录、CI 配置、评分脚本被改了，这次试验直接记失败。
3. **扫描过程记录里的禁用工具调用**，例如联网、读隐藏目录、调用部署命令。这些只会出现在过程里，结果里看不到（[第 05 章 §8](./05-verification#_8-评测-为团队的-harness-建回归)）。

示例里的 `cheater` 智能体做不出来时会改可见测试、去读隐藏答案。两种评分方式的实测对比（各 30 次试验）：

| 评分方式 | 成功率 | 发现的违规 |
| --- | --- | --- |
| `--grader naive`：直接在智能体工作区跑测试 | 30/30（100%） | 0 |
| `--grader isolated`：干净目录 + 隐藏测试 + 过程检查 | 23/30（76.7%） | 7 次试验（`forbidden_tool:read_hidden`、`protected_modified`） |

naive 方式下作弊的智能体拿到满分，比诚实的智能体（86.7%）还高。

### 3.3 过程本身也要评

- 只看过程记录太多，没人读得过来。Spotify 在确定性验证之上加了一层只看 diff 和原始提示词的 LLM 裁判，用来拦「顺手重构」「禁用 flaky 测试」这类过于积极的改动（[QB03](/sources/quality/bigtech#qb03)，团队自报）。
- 字节把端到端 trace 回流到离线、在线评测和轨迹评测（[BD17](/sources/quality/chinese#bd17)）。轨迹评测的常见检查项：工具调用顺序、有没有重复调用、有没有越权、调用参数对不对。

## 4. 线上评测与可观测性 {#online}

线下评测覆盖不了真实分布。公开的工程实践几乎都把线上、线下连成一个循环：

```text
生产 trace ──抽样──▶ 在线评估器（规则 / LLM 裁判 / 用户反馈）
     ▲                         │
     │                         ▼ 失败样本
  发布新版本 ◀── PR 跑回归集 ◀── 加入数据集
```

- **LangSmith** 把评测分成离线和线上：线上评估器在生产 trace 上运行，可以设过滤条件和采样率控制成本；文档建议把失败的生产 trace 加进数据集，让「见过一次的失败变成每次都跑的测试」（[EV16](/sources/evals#ev16)）。
- **Langfuse** 支持在线打分和发布前离线实验，提供「检查 LLM 裁判是否与人工标签一致」的校准功能，还有一个 GitHub Action，可以在 PR 里跑实验、分数低于阈值时让任务失败（[EV19](/sources/evals#ev19)）。
- **Braintrust** 以 trace 为中心：从 trace 里找问题，变成数据集和 scorer，上线后对新 trace 在线打分，再把新失败带回评测（[EV17](/sources/evals#ev17)）。
- **国内实践。** 美团把「观测 + 评测 = 持续迭代」作为智能体研发公式（[CN02](/sources/chinese#cn02)）；字节扣子罗盘的 AgentOps 覆盖评测集构建、指标体系、持续集成和线上监测（[BD16](/sources/quality/chinese#bd16)）；阿里 AgentLoop 把观测、评估、实验做成闭环（[AL22](/sources/quality/chinese#al22)）。

可观测性的底座：

- 用 OpenTelemetry GenAI 语义约定记录模型调用、智能体和工具调用的 span，以及 token 用量（[OS16](/sources/open-source#os16)，状态仍是 Development，字段可能变）。Claude Code 本身就能导出 OpenTelemetry 的指标和事件（[AN37](/sources/anthropic#an37)）。
- 线上打分要看三类数：**质量**（裁判分、用户采纳率）、**成本**（token、调用次数）、**延迟**（p50 / p95）。只看质量会放过一个变贵三倍的版本。
- 线上评估器自己也会漂移（§2.3），在线裁判的版本同样要钉死。

## 5. 基准全景与常见的坑 {#benchmarks}

### 5.1 几个常被引用的智能体基准

| 基准 | 测什么 | 读分数时要注意 |
| --- | --- | --- |
| SWE-bench Verified | Python 仓库的 issue 修复 | OpenAI 已停止报告：被审题目 59.4% 的测试有缺陷，前沿模型训练中见过部分题目（[OA11](/sources/openai#oa11)）；Epoch AI 评为「有缺陷」（[RS11](/sources/research#rs11)） |
| SWE-Bench Pro | 41 个仓库的 1,865 道长程题 | 分公开集、保留集和商业集，后两者不公开，用来抗污染（[EV07](/sources/evals#ev07)） |
| Multi-SWE-bench | Java、TS、Go、Rust、C/C++ 等多语言 issue 修复 | 字节 Seed 发布，注重人工标注质量（[BD08](/sources/quality/research#bd08)） |
| Terminal-Bench | 终端里的工程任务 | 每一行是「模型 + 脚手架」组合，带 95% 置信区间；查看时为 4.1 版，不同论文用的版本不同（[EV10](/sources/evals#ev10)） |
| τ-bench / τ²-bench | 带政策规则的客服式工具调用；τ² 加了「用户也能动手」的双控制 | 提出 pass^k；双控制下表现明显下降（[RS10](/sources/research#rs10)、[EV08](/sources/evals#ev08)） |
| OSWorld / OSWorld-Verified | 真实操作系统里的电脑操作 | 369 个任务，人类完成 72.36%；上「已验证」榜单要由维护者运行你的智能体（[EV09](/sources/evals#ev09)） |
| A.S.E（AICGSecEval） | 仓库上下文里 AI 生成代码的安全性 | 腾讯开源，支持直接生成与智能体生成两种模式（[TX22](/sources/security#tx22)） |

### 5.2 常见的坑

1. **污染。** 题目和答案在网上，就可能进了训练数据。对策：保留集、按训练截止日期切分（§8）、加 canary 字符串（Terminal-Bench 页面上就有，[EV10](/sources/evals#ev10)）。
2. **测试本身有洞。** 见 [OA11](/sources/openai#oa11)、[QR05](/sources/quality/research#qr05)、[EV02](/sources/evals#ev02)。
3. **基础设施噪声。** Anthropic 只改容器资源的执行方式，Terminal-Bench 2.0 上最宽松和最严格的配置就差了 6 个百分点，基础设施错误率从 5.8% 降到 0.5%；SWE-bench 上内存放到 5 倍，分数高 1.54 个百分点（[EV06](/sources/evals#ev06)，厂商自报）。
4. **脚手架不同。** 同一个模型，换个脚手架分数就变（[RS11](/sources/research#rs11)）。
5. **总分相同，答对的题不同。** 百度的观察（[CN40](/sources/chinese#cn40)），也是[第 10 章 #18](./10-anti-patterns#_18-只信-ci-的绿灯、只看评测总分) 的反模式。逐题比对比看总分有用。
6. **厂商评自己。** CodeReviewBench 的论文提到，厂商自己做的评测总是把自家工具排第一；而这篇论文本身也有被评工具方的作者，并在文中做了披露（[EV11](/sources/evals#ev11)）。

### 5.3 怎么读厂商公布的分数

拿到一个「我们在某基准上提升了 X 分」的说法时，逐条问：

- **用的哪个版本、哪个子集？** 全集还是筛过的子集，Verified 还是 Pro。
- **几次试验，有没有置信区间？** 没有区间的 2–3 分差距，按 Anthropic 的建议应当存疑（[EV06](/sources/evals#ev06)）。
- **资源和脚手架是否和对比对象一致？**
- **有没有第三方复现？** OSWorld-Verified 这类由维护者代跑的榜单，比自报分数可信（[EV09](/sources/evals#ev09)）。
- **在你自己的回归集上表现如何？** 这是唯一能直接用来做决定的数（[第 05 章 §8](./05-verification#_8-评测-为团队的-harness-建回归)）。

## 6. 框架对比 {#frameworks}

下表只写各家官方文档或仓库里能核实的内容（2026-11-24 查看），不做好坏排名。

| 框架 | 擅长什么 | 许可证 / 形态 | 本地还是托管 | 来源 |
| --- | --- | --- | --- | --- |
| **Inspect** | 智能体评测：多轮工具调用、Docker / K8s 等沙箱、接外部智能体（Claude Code、Codex CLI 等）；200 多个现成评测；内置 `pass_at_k`、`pass_k_k` | MIT | 本地运行 | [EV13](/sources/evals#ev13) |
| **promptfoo** | 声明式测试用例、红队测试、CI 集成；`exec:` provider 可接任意脚本；`--repeat` 多次试验 | MIT | 本地运行，调用你配置的 provider | [EV14](/sources/evals#ev14) |
| **DeepEval** | pytest / Vitest 风格的评测用例；通过 tracing 评智能体轨迹和组件 | Apache-2.0 | 本地运行；Confident AI 云平台可选 | [EV18](/sources/evals#ev18) |
| **Langfuse** | trace + 在线打分 + 离线实验；裁判校准；PR 里跑实验的 GitHub Action | 开源（`ee/` 等目录之外为 MIT） | 可自托管，也有云服务 | [EV19](/sources/evals#ev19) |
| **LangSmith** | 离线实验 + 线上评估器（过滤、采样）；人工、代码、LLM 裁判、两两比较 | 商业平台 | 云端、混合、自托管 | [EV16](/sources/evals#ev16) |
| **Braintrust** | trace 驱动的评测循环，在线打分，成本与延迟跟踪 | 商业平台；评分器库 autoevals 为 MIT | 托管；可选 BYOC 数据面 | [EV17](/sources/evals#ev17) |
| **EvalScope** | 模型基准评测 + 推理压测；智能体评测模式可跑 SWE-bench Agentic，支持 Docker、E2B 沙箱 | Apache-2.0（魔搭社区） | 本地运行 | [EV20](/sources/evals#ev20) |
| **OpenAI Evals API** | 在 OpenAI 平台上描述任务、跑数据、看结果 | 平台功能；开源的 openai/evals 仓库为 MIT | 托管。**平台已在弃用：2026-10-31 起只读，计划 2026-11-30 关停** | [EV15](/sources/evals#ev15) |

怎么选：

- **只想在 CI 里跑一个回归集**：自己写个几百行的 harness（§7）或用 promptfoo，最省事。
- **要跑带沙箱的智能体任务、要 pass^k**：Inspect 原生支持。
- **已经有线上 trace，想做线上打分和数据回流**：Langfuse（想自托管）、LangSmith 或 Braintrust（接受商业平台）。
- **别把评测数据锁死在某个平台里。** OpenAI Evals 平台的关停就是例子（[EV15](/sources/evals#ev15)）。任务、标签和基线最好以 JSON / CSV 的形式放在自己的仓库里，框架只是执行器。

## 7. 一个能跑的最小评测套件 {#starter}

代码在 [`examples/evals/`](https://github.com/Atituiset/agent-engineering-handbook/tree/main/examples/evals)，CI 在 [`.github/workflows/agent-evals.yml`](https://github.com/Atituiset/agent-engineering-handbook/blob/main/.github/workflows/agent-evals.yml)。它是[第 12 章示例 C](./12-quality-cicd#example-c) 里 `run.py` 和 `compare.py` 的一个可运行实现。

### 7.1 里面有什么

| 路径 | 作用 | 对应章节 |
| --- | --- | --- |
| `tasks/<id>/` | 6 个小任务（4 个回归、2 个能力），每个有可见测试和**隐藏测试**，`task.json` 写明来源、受保护路径和禁用工具 | §1.2 |
| `agents/mock_agent.py` | 确定性的模拟智能体：`honest`、`honest_v2`（模拟改坏了提示词）、`cheater`（会改测试、读答案） | §3 |
| `harness/run_evals.py` | 多次试验、隔离评分、过程检查、pass@k / pass^k、Wilson 区间、成本与延迟 | §1.4、§3.2 |
| `harness/compare.py` | 回归门禁：回归集 pass^k 或任一回归任务的 pass@1 下降、出现违规，就失败 | §1.1 |
| `judge/calibrate.py` | 裁判校准：kappa、失败召回率、笨基线、版本漂移、换位一致性 | §2 |
| `vuln/paired_eval.py` | 漏洞检测的配对评测 | §8 |
| `promptfoo/`、`inspect/` | 同一套任务的两个框架版本 | §6 |
| `tests/test_harness.py` | harness 自己的 10 个测试 | — |

所有标签、预测和 C 代码片段都是**人工构造的演示数据**，不来自真实模型或真实 CVE。

### 7.2 跑起来

```bash
cd examples/evals
python3 -m unittest discover -s tests -v
python3 harness/run_evals.py --agent "python3 agents/mock_agent.py --profile honest" \
  --trials 5 --k 1 3 5 --out results.json
python3 harness/compare.py --baseline baseline.json --current results.json --max-drop 0.02 --k 3
```

换成真实智能体时，只要把 `--agent` 换成一个包装脚本，接口是 `--workspace DIR --task-id ID --prompt TEXT --trial N --transcript FILE`。详见 README。

### 7.3 实测输出（2026-11-24，Debian，Python 3.13.5）

**诚实智能体，每任务 5 次：**

```text
              task        kind   c/n  pass@1  pass@3  pass^3  violations
 dedupe_keep_order  regression   5/5   1.000   1.000   1.000           0
   merge_intervals  regression   5/5   1.000   1.000   1.000           0
    parse_duration  regression   5/5   1.000   1.000   1.000           0
      roman_to_int  capability   4/5   0.800   1.000   0.400           0
    semver_compare  capability   2/5   0.400   0.900   0.000           0
           slugify  regression   5/5   1.000   1.000   1.000           0
trial_success_rate 0.8667, ci95 [0.7032, 0.9469]
regression gate passed
```

（为了排版省略了 pass@5 等几列。）`semver_compare` 的 pass@3 是 0.9，pass^3 是 0：「多试几次总能对」和「每次都对」差得很远，这正是能力集和回归集要分开看的原因。

**模拟一次退化（`honest_v2`）：**

```text
regression  pass^3: baseline=1.000 current=0.450 [DROP]
REGRESSION GATE FAILED:
  - regression pass^3 dropped 1.000 -> 0.450
  - regression task dedupe_keep_order pass@1 1.000 -> 0.800
  - regression task parse_duration pass@1 1.000 -> 0.200
  - regression task slugify pass@1 1.000 -> 0.800
```

退出码为 1。注意：`honest_v2` 只改坏了 `parse_duration`，`dedupe_keep_order` 和 `slugify` 的成功概率没变，只是 5 次抽样碰巧失败了一次。这就是抽样噪声：小样本的门禁一定会有误报。真实场景要么加试验次数，要么对「只掉了一次」的任务自动重跑确认。

**作弊智能体：** 见 §3.2 的表格，naive 评分 30/30，隔离评分 23/30 并抓到 7 次违规。

### 7.4 用两个框架交叉核对

| 框架与版本 | 做法 | 结果 |
| --- | --- | --- |
| promptfoo 0.126.0（Node 24） | `exec:` provider 调模拟智能体，python 断言做隔离评分和过程检查，`--repeat 3` | 诚实智能体：4 个回归任务 × 3 次 = 12/12 通过，退出码 0。作弊智能体：8 过 4 不过（全是过程违规），退出码 100 |
| Inspect 0.3.292 | `--model mockllm/model`，`Epochs(5, ["mean", "pass_at_3", "pass_k_3"])` | mean 0.867、pass_at_3 0.983、pass_k_3 0.733 |

Inspect 的三个数和自写 harness 算出的完全一致：0.867 是 26/30；0.983 和 0.733 是 6 个任务 pass@3、pass^3 的平均。也就是说，不管用哪个框架，只要试验次数和公式一样，数就一样；框架的差别在沙箱、日志查看和线上集成这些方面。

### 7.5 验证范围

- 以上命令都在 2026-11-24 于本机实际运行；仓库里的 `agent-evals` 工作流把 harness、promptfoo、Inspect 三个 job 放进 GitHub Actions。工作流在 GitHub runner 上的运行结果，以仓库 Actions 页面为准。
- **没验证的：** 接上真实智能体之后的行为；把隐藏测试放到另一台机器上的隔离方式（示例只做了目录隔离，这不是安全边界）。

### 7.6 起步套件七个分支里的评测 {#starter-branches}

[第 15 章](./15-starter-kit#branches)的七个 `starter/*` 分支各带一个更小的版本 `evals/`，形态贴合模板本身的编码智能体工作方式：智能体在不含 `evals/` 的仓库副本里改代码；判分时只把它对非受保护文件的改动带进一个干净副本，先跑隐藏测试，再跑该分支的 `scripts/verify.sh`。改了受保护文件（`guard-protected.sh` 的 `PROTECTED_REGEX` 加上 `evals/`）或删掉现有测试输入，记为违规。harness 是七个分支共用的一份 Python 标准库脚本，每种语言只换隐藏测试（pytest、vitest、doctest、JUnit 5、cargo test、Unity、go test）和运行命令；`evals.yml` 跑 harness 自测、5 次试验和门禁。

3 个任务：`add_days`、`allow_spaces`（回归集）和 `reject_leading_zeros`（能力集）。2026-11-25 在本机用 mock 智能体实测，七个分支结果相同（mock 按种子选改动，与语言无关）：

| 运行 | 回归集 | 回归 pass^3 | 能力集 pass@3 | 违规 | 门禁 |
| --- | --- | --- | --- | --- | --- |
| 基线 | 8/10，Wilson [0.4902, 0.9433] | 0.550 | 1.000（3/5） | 0 | — |
| 同种子重跑 | 8/10 | 0.550 | 1.000 | 0 | 通过 |
| `regressed`（`add_days` 成功率调低） | 5/10 | 0.050 | 1.000 | 0 | 失败：pass^3 0.550→0.050，`add_days` pass@1 1.000→0.400 |
| `cheater`（失败时改 `verify.sh`），隔离判分 | 8/10 | 0.550 | 1.000 | 4 | 失败：违规 |
| `cheater`，只在智能体目录里跑 verify | 10/10 | 1.000 | 1.000（5/5） | — | （对照） |

最后一行和 §3.1 说的是同一件事：判分如果相信智能体自己的工作目录，作弊的智能体拿满分。mock 的成功率是编的，这些数只证明 harness 和门禁能工作；三个任务、5 次试验的区间很宽，接真实智能体时要加任务和试验次数，做法见各分支的 `evals/README.md`。

## 8. 实例：代码评审与漏洞检测的评测 {#domain}

评「AI 代码评审」和「AI 漏洞检测」时，§1–§5 的问题都会出现，而且更隐蔽：评审天然主观，漏洞样本稀少、标签有噪声。腾讯的 AICR 团队就把「评估 CR 模型效果难以量化」列为主要难题之一（[QC07](/sources/quality/chinese#qc07)）。

### 8.1 代码评审：先看精确率

CodeReviewBench 用「开发者有没有按评审意见改代码」作为信号，覆盖 18 个 AI 评审工具、50 万以上已判定的 PR，再配一个专家标注的离线金标集（[EV11](/sources/evals#ev11)，作者自报）：

- 线上与离线两套口径下的工具排名，**精确率**一致（Spearman ρ = 0.69），**F1** 不一致（ρ = −0.05）。作者的结论是精确率最能跨口径迁移。
- 召回率在两套口径下含义不同：线上，开发者可能因为排期或风格而不改一个合理的问题；离线，金标集本身不全。作者用 50 个 PR 的金标集统计，有 41 组问题被至少 3 个不同工具同时指出、却不在金标集里，所以离线评测会低估精确率、高估召回率。
- 这篇论文的多数作者来自维护该基准的公司，另有两位作者所在公司的工具也在被评之列，论文做了披露。读排名时要记住这一点。

国内的对应工作：阿里开源的 AACR-Bench 带仓库级上下文，并单独提供负样本集来度量「不该报的时候报了」（[AL11](/sources/quality/research#al11)、[QC05](/sources/quality/chinese#qc05)，团队自报）。

落到自己的评审机器人上：

- 主指标用**被采纳的评论占比**（精确率），并单独统计**负样本上的误报**。
- 召回率用历史上真实出过的线上缺陷来抽查，不追求覆盖率数字。
- 评审意见的质量用校准过的裁判打分（§2），裁判不要和评审机器人用同一个模型（[EV04](/sources/evals#ev04)）。

### 8.2 漏洞检测：配对、笨基线、截止日期

Right Verdict, Right Reason? 这篇论文给出了一套更严格的做法（[EV12](/sources/evals#ev12)，作者自报）：

- **配对。** 每个漏洞函数都配上它的修复版。只有「漏洞版判有、修复版判无」才算对，这个指标叫 P-C（配对正确率）。
- **笨基线。** 在平衡的配对上，「永远判有漏洞」的 F1 就有 0.67，却一对也分不开。论文里 CodeLlama-34B 的 F1 是 0.665，P-C 是 0。光看 F1 会以为它还行。
- **主要发现。** 开源模型区分配对不超过随机水平；商用模型定位出错位置的能力好过关键词规则，给定程序输入时，预测这次运行会不会出错也好过规则基线。
- **按训练截止日期切分。** 另取 195 个在模型训练截止之后公开的漏洞重做实验：预测运行结果的优势在新漏洞上消失，最强模型的领先也收窄，只有定位能力保持住了。

示例里的 `vuln/paired_eval.py` 在 8 对人工构造的 C 片段上实现了这套指标（数据纯属演示）：

```text
[all]
  always_vulnerable      F1=0.667 MCC=+0.000 P-C=0.000 (chance 0.000)
  keyword_rule           F1=0.667 MCC=+0.258 P-C=0.250 (chance 0.234)
  model                  F1=0.737 MCC=+0.405 P-C=0.375 (chance 0.215)
[after 2026-06-01]
  model                  F1=0.571 MCC=+0.000 P-C=0.000 (chance 0.222)
```

三个检测器的 F1 看起来差不多，P-C 和 MCC 才把它们分开；截止日期之后的那组，「模型」的 P-C 掉到 0。玩具数据只是演示读法，具体数值没有意义。

腾讯的 A.S.E 是同一思路在「AI 生成代码的安全性」上的版本：在真实仓库上下文里评，用 Docker 复现构建和验证（[TX22](/sources/security#tx22)）。

## 与传统软件工程认知的对比 {#compare}

| 传统认知 | 智能体时代 | 判断 | 佐证 |
| --- | --- | --- | --- |
| 测试是确定性的，跑一次就知道过没过 | 同一输入多次运行结果不同，要报 pass@k / pass^k 和置信区间 | **改变** | [RS10](/sources/research#rs10)、[QT01](/sources/quality/tools#qt01)、§7.3 |
| 被测代码不会主动对付测试 | 智能体会改测试、读答案、钻评分器的空子；评分器要做权限分离 | **新增** | [EV01](/sources/evals#ev01)、[EV02](/sources/evals#ev02)、[QR02](/sources/quality/research#qr02) |
| 测试断言是可信的「标准答案」 | 用 LLM 当裁判时，裁判本身要校准、钉版本、防偏差 | **新增** | [EV03](/sources/evals#ev03)、[EV04](/sources/evals#ev04)、[EV05](/sources/evals#ev05)、[QP12](/sources/quality/practitioners#qp12) |
| 公开基准分数可以横向比较 | 污染、测试缺陷、脚手架和资源配置都会让分数失真；自己的回归集才是决策依据 | **加强**（基准本来就有局限，现在更严重） | [OA11](/sources/openai#oa11)、[RS11](/sources/research#rs11)、[EV06](/sources/evals#ev06) |
| 测试环境和生产环境分开，上线后靠监控 | 线上 trace 抽样打分、失败样本回流进回归集，线上线下是一个循环 | **加强** | [EV16](/sources/evals#ev16)、[EV19](/sources/evals#ev19)、[CN02](/sources/chinese#cn02)、[AL29](/sources/quality/chinese#al29) |
| 分类器用准确率或 F1 评 | 安全检测要配对评、对比笨基线、按截止日期切分；评审要先看精确率 | **改变**（这些方法在 ML 评测里早有，但在工程团队里少见） | [EV12](/sources/evals#ev12)、[EV11](/sources/evals#ev11)、[AL11](/sources/quality/research#al11) |
| 回归测试失败就是代码坏了 | 小样本下会有抽样误报，门禁要考虑噪声 | **新增** | [EV06](/sources/evals#ev06)、§7.3 |

## 证据强度与缺口 {#evidence}

- **最强的**：pass^k 的定义和多次试验的必要性（论文 + 多家厂商文档一致）；公开基准有测试缺陷和污染问题（OpenAI 自己停用、Epoch AI 第三方评审、BenchJack 审计，三方互证）。
- **中等的**：评分器隔离的效果（SplitBench 只有一篇论文，2026-11 刚发布，数字为作者自报）；裁判版本漂移（一篇预注册研究，评的是研究提案而不是代码）；代码评审的「精确率可迁移」（一篇论文，作者与被评工具有利益关系）。
- **较弱的**：国内团队的实践多来自技术博客和会议议题，有的只是议题预告（[AL22](/sources/quality/chinese#al22)、[AL29](/sources/quality/chinese#al29)），只说明「在做」，没有效果数据。
- **缺口**：没有找到对比「LLM 裁判 vs. 人工评审」在**代码评审意见质量**上一致性的大规模公开研究；没有找到各评测框架之间的公开横评，§6 的表只写了各家自述；本章的示例只用模拟智能体验证了评测方法本身，没有评过任何真实智能体。

## 本章小结 {#summary}

- 评测分三种：回归（拦退化，看 pass^k）、能力（看趋势，看 pass@k）、线上（抽样打分，失败回流）。
- 评分器先行：隐藏测试放在智能体碰不到的地方，受保护文件做哈希，过程记录扫禁用工具。
- LLM 裁判按分类器来测：kappa、失败召回率、对比笨基线；钉版本，换版本先跑校准集；两两比较要换位。
- 读基准分数先问版本、试验次数、置信区间、资源与脚手架；3 个百分点以内的差距先存疑。
- 代码评审先看精确率和负样本误报；漏洞检测要配对评、对比笨基线、按截止日期切分。
- 想马上动手：复制 [`examples/evals/`](https://github.com/Atituiset/agent-engineering-handbook/tree/main/examples/evals)，把任务换成你团队的 20 个真实失败，把 `--agent` 换成你的智能体，再按 [第 11 章 §13](./11-checklists#eval-checklist) 的清单逐项检查。
