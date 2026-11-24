# 驾驭 Agent 实践手册

如何驾驭当前大模型与编码智能体：一线大厂与优秀工程师的实践手册与原始资料报告。基于 [VitePress](https://vitepress.dev/) 构建，部署在 GitHub Pages。

## 内容

- `docs/handbook/` 实践手册（16 章）：心智模型、上下文工程、规格驱动与计划先行、架构约束落地、验证与测试、代码评审与人机协作、工具与 harness、团队与流程、安全、反模式、速查表、质量保障（测试、CI/CD 与评审）、Skills 生态（官方与高星仓库清单）、异步与后台智能体、落地起步套件、智能体评测。每章都包含「与传统软件工程认知的对比」。
- `docs/sources/` 原始报告：约 740 条精选资料（X 精选按主题放在 `docs/sources/x/`；质量与 CI/CD 专题放在 `docs/sources/quality/`；另有 Hacker News 与中文互联网），每条附原文链接、中文摘要与证据性质标注。
- `docs/library/` 全量库：3,215 条资料的分页表格与在线筛选（质量专题的分页为 `q-*.md`；可按公司筛选腾讯、阿里、字节相关条目）；数据文件在 `docs/public/data/sources.json` 与 `sources.csv`。
- `docs/compare/evidence.md` 共识度/佐证：20 条原则的独立支持数与异议；质量专题 13 条原则（Q01–Q13）的统计在 `docs/handbook/12-quality-cicd.md`。
- `docs/compare/` 对比与取舍：传统工程 vs Agent 时代总表、决策指南、共识度/佐证。
- `examples/evals/`：第 16 章「智能体评测」的可运行示例（多次试验的评测 harness、隔离评分、回归门禁、LLM 裁判校准、配对漏洞评测，以及 promptfoo 与 Inspect 版本），全部使用模拟智能体，不需要 API key；CI 见 `.github/workflows/agent-evals.yml`。
- 分支 `starter/python`、`starter/typescript`、`starter/cpp`、`starter/java`、`starter/rust`、`starter/c`、`starter/go`：第 15 章「落地起步套件」的七个示例项目。它们是 orphan 分支，与 `main` 没有共同历史，可以直接 `git clone --branch starter/<语言> --single-branch` 当模板用；文档站只从 `main` 构建。

## 本地运行

需要 Node.js 20 及以上。

```bash
npm install
npm run docs:dev      # 本地预览 http://localhost:5173/agent-engineering-handbook/
npm run docs:build    # 构建到 docs/.vitepress/dist
npm run docs:preview  # 预览构建结果
```

## 部署到 GitHub Pages

1. 仓库名默认为 `agent-engineering-handbook`。若使用其他仓库名，修改 `docs/.vitepress/config.mts` 顶部的 `REPO_NAME` 常量；若部署到 `<用户名>.github.io` 仓库或使用自定义域名，把它设为空字符串 `''`。
2. 推送到 `main` 分支，`.github/workflows/deploy.yml` 会自动构建并发布。
3. 首次部署如未自动启用 Pages，到仓库 **Settings → Pages**，把 **Source** 设为 **GitHub Actions**。

## 贡献

发现错误、失效链接或遗漏的重要来源，欢迎提 issue 或 PR。新增来源请遵循：只收录实际打开核对过的链接；摘要忠于原文；不编造日期、数字与引文；标注「厂商自报 / 作者自述」等证据性质。

## 许可

- 原创文字（手册正文、对比分析、摘要的中文表述）以 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 发布。
- 原始报告中的摘要与引文仅用于评论与研究，链接指向原文，权利归原作者所有，请以原文为准。

作者：[Atituiset](https://github.com/Atituiset)
