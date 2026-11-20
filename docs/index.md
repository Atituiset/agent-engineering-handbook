---
layout: home

hero:
  name: 驾驭 Agent 实践手册
  text: 让编码智能体守住工程与架构约束
  tagline: 以 X 一线声音为主，整理约 690 条精选资料与 3,195 条全量库，每条都附原文链接；统计每条实践的独立佐证数，并与传统软件工程认知逐项对照。
  actions:
    - theme: brand
      text: 阅读实践手册
      link: /handbook/
    - theme: alt
      text: 原始报告
      link: /sources/
    - theme: alt
      text: 共识度/佐证
      link: /compare/evidence
    - theme: alt
      text: 传统工程 vs Agent 时代
      link: /compare/

features:
  - title: 约束靠环境，不靠「告诉」
    details: 能机械判定的规则写成 lint、结构测试、hook 与 CI；只把需要判断的知识留给精简的上下文。（第 04 章）
    link: /handbook/04-architecture-constraints
  - title: 上下文是有限资源
    details: AGENTS.md 是地图不是百科；只写模型读不到、猜不到的东西；按需加载，定期删减。（第 02 章）
    link: /handbook/02-context-engineering
  - title: 验证决定你能放手多少
    details: 给智能体运行、观察、测试的手段；用 E2E、属性、差分与变异测试验证 AI 写的测试。（第 05 章）
    link: /handbook/05-verification
  - title: 按风险分配人的注意力
    details: 「有人读过代码」不是好指标；多层检查加风险分级，每段合并代码都要有人负责。（第 06 章）
    link: /handbook/06-review-collaboration
  - title: 经典纪律被重新定价
    details: 分层架构、属性测试、变异测试、ADR，过去「好但太贵」，现在成本骤降、价值骤升。（对比与取舍）
    link: /compare/
  - title: CI 是不会被说服的评审者
    details: 测试先行、测试改动守卫、必需检查与合并队列；AI 评审只做建议性初筛，Evals 进 CI，度量解决率与变更失败率。（第 12 章）
    link: /handbook/12-quality-cicd
  - title: 现成的 skills 去哪找、怎么审
    details: 厂商官方与 GitHub 高星 skills 仓库清单，附星标、许可证与各工具加载路径；第三方 skill 当作依赖审查。（第 13 章）
    link: /handbook/13-skills-catalog
  - title: 把任务交出去之后
    details: 云端与 CI 里的智能体：什么任务适合委派、环境决定能力上限、智能体与触发人都不能批准它的 PR、回合与预算设上限。（第 14 章）
    link: /handbook/14-async-agents
  - title: 证据与分歧并列
    details: 厂商自报、个人经验与对照研究分开标注；上下文文件有没有用、TDD、多智能体等争议如实呈现。
    link: /sources/
---
