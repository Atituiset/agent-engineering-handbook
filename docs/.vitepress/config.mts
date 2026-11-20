import { defineConfig } from 'vitepress'

// ⬇️ 部署到 GitHub Pages 时的仓库名：只需改这一处（例如 '/my-repo/'；若用自定义域名或 <user>.github.io 仓库则改为 '/'）
const REPO_NAME = 'agent-engineering-handbook'
const BASE = REPO_NAME ? `/${REPO_NAME}/` : '/'

const handbookSidebar = [
  {
    text: '实践手册',
    items: [
      { text: '总览：一页读懂', link: '/handbook/' },
      { text: '一页纸推荐：先读·先做·先别做', link: '/handbook/00-one-page' },
      { text: '01 心智模型：能力边界', link: '/handbook/01-mental-model' },
      { text: '02 上下文工程', link: '/handbook/02-context-engineering' },
      { text: '03 规格驱动与计划先行', link: '/handbook/03-spec-and-plan' },
      { text: '04 架构约束如何落地', link: '/handbook/04-architecture-constraints' },
      { text: '05 验证与测试', link: '/handbook/05-verification' },
      { text: '06 代码评审与人机协作', link: '/handbook/06-review-collaboration' },
      { text: '07 工具与 Harness', link: '/handbook/07-harness-tools' },
      { text: '08 团队、流程与度量', link: '/handbook/08-team-process' },
      { text: '09 安全', link: '/handbook/09-security' },
      { text: '10 反模式与踩坑清单', link: '/handbook/10-anti-patterns' },
      { text: '11 速查表与 Checklist', link: '/handbook/11-checklists' },
      { text: '12 质量保障：测试、CI/CD 与评审', link: '/handbook/12-quality-cicd' },
      { text: '13 Skills 生态：官方与高星仓库清单', link: '/handbook/13-skills-catalog' },
      { text: '14 异步与后台智能体', link: '/handbook/14-async-agents' },
      { text: '15 落地起步套件：Python / TS / C++ 模板', link: '/handbook/15-starter-kit' }
    ]
  }
]

const sourcesSidebar = [
  {
    text: '原始报告',
    items: [
      { text: '说明与索引', link: '/sources/' },
      { text: 'Anthropic / Claude Code', link: '/sources/anthropic' },
      { text: 'OpenAI / Codex', link: '/sources/openai' },
      { text: 'Google · Meta · Microsoft/GitHub', link: '/sources/bigtech' },
      { text: '工具厂商与创业公司', link: '/sources/vendors' },
      { text: 'Martin Fowler 网站与 Thoughtworks', link: '/sources/thoughtworks' },
      { text: '独立工程师与意见领袖', link: '/sources/practitioners' },
      { text: 'X（v1 精选）', link: '/sources/x-posts' },
      { text: 'Hacker News 高热讨论', link: '/sources/hackernews' },
      { text: '中文互联网', link: '/sources/chinese' },
      { text: 'GitHub 开源项目与规范', link: '/sources/open-source' },
      { text: '研究、调查与社区讨论', link: '/sources/research' },
      { text: '安全专题', link: '/sources/security' }
    ]
  },
  {
    text: 'X 精选（按主题）',
    collapsed: false,
    items: [
      { text: '总览', link: '/sources/x/' },
      { text: '工作流与心智模型', link: '/sources/x/workflow' },
      { text: '上下文与说明文件', link: '/sources/x/context' },
      { text: '计划与规格', link: '/sources/x/plan' },
      { text: '测试与验证', link: '/sources/x/verify' },
      { text: '评审与代码质量', link: '/sources/x/review' },
      { text: '约束与架构', link: '/sources/x/constraints' },
      { text: 'Hooks、Skills、子智能体与 MCP', link: '/sources/x/tools' },
      { text: '并行与长任务', link: '/sources/x/parallel' },
      { text: '安全与权限', link: '/sources/x/security' },
      { text: '团队、成本与组织', link: '/sources/x/team' },
      { text: '失败与反思', link: '/sources/x/failures' }
    ]
  },
  {
    text: '质量与 CI/CD 专题',
    collapsed: false,
    items: [
      { text: '说明与索引', link: '/sources/quality/' },
      { text: '大厂与平台团队实践', link: '/sources/quality/bigtech' },
      { text: '工具与官方文档', link: '/sources/quality/tools' },
      { text: '一线工程师与方法论', link: '/sources/quality/practitioners' },
      { text: '研究与数据', link: '/sources/quality/research' },
      { text: '开源项目政策与工具', link: '/sources/quality/oss' },
      { text: '中文互联网', link: '/sources/quality/chinese' },
      { text: 'X 精选', link: '/sources/quality/x' },
      { text: 'Hacker News 讨论精选', link: '/sources/quality/hn' }
    ]
  },
]

const librarySidebar = [
  {
    text: '全量库',
    items: [
      { text: '说明与在线筛选', link: '/library/' },
      { text: 'X · 上下文与说明文件', link: '/library/x-context' },
      { text: 'X · 计划与规格', link: '/library/x-plan' },
      { text: 'X · 测试与验证', link: '/library/x-verify' },
      { text: 'X · 评审与代码质量', link: '/library/x-review' },
      { text: 'X · 约束与架构', link: '/library/x-constraints' },
      { text: 'X · Hooks、Skills、子智能体与 MCP（1/3）', link: '/library/x-tools-1' },
      { text: 'X · Hooks、Skills、子智能体与 MCP（2/3）', link: '/library/x-tools-2' },
      { text: 'X · Hooks、Skills、子智能体与 MCP（3/3）', link: '/library/x-tools-3' },
      { text: 'X · 并行与长任务（1/2）', link: '/library/x-parallel-1' },
      { text: 'X · 并行与长任务（2/2）', link: '/library/x-parallel-2' },
      { text: 'X · 安全与权限', link: '/library/x-security' },
      { text: 'X · 团队、成本与组织', link: '/library/x-team' },
      { text: 'X · 失败与反思', link: '/library/x-failures' },
      { text: 'Hacker News 讨论（1/3）', link: '/library/hn-1' },
      { text: 'Hacker News 讨论（2/3）', link: '/library/hn-2' },
      { text: 'Hacker News 讨论（3/3）', link: '/library/hn-3' },
      { text: 'GitHub 仓库（1/3）', link: '/library/github-1' },
      { text: 'GitHub 仓库（2/3）', link: '/library/github-2' },
      { text: 'GitHub 仓库（3/3）', link: '/library/github-3' },
      { text: '精选条目与中文网页（1/3）', link: '/library/curated-1' },
      { text: '精选条目与中文网页（2/3）', link: '/library/curated-2' },
      { text: '精选条目与中文网页（3/3）', link: '/library/curated-3' }
    ]
  },
  {
    text: '质量与 CI/CD 专题',
    items: [
      { text: 'X 帖子（1/3）', link: '/library/q-x-1' },
      { text: 'X 帖子（2/3）', link: '/library/q-x-2' },
      { text: 'X 帖子（3/3）', link: '/library/q-x-3' },
      { text: 'Hacker News 讨论', link: '/library/q-hn' },
      { text: 'GitHub 仓库（1/2）', link: '/library/q-github-1' },
      { text: 'GitHub 仓库（2/2）', link: '/library/q-github-2' },
      { text: '精选条目与网页', link: '/library/q-curated' }
    ]
  },
]

export default defineConfig({
  lang: 'zh-CN',
  title: '驾驭 Agent 实践手册',
  description: '如何驾驭当前大模型与编码智能体：一线大厂与优秀工程师的实践手册与原始资料报告',
  base: BASE,
  cleanUrls: true,
  lastUpdated: true,
  head: [['meta', { name: 'theme-color', content: '#3c8772' }]],
  markdown: {
    lineNumbers: false
  },
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '实践手册', link: '/handbook/' },
      { text: '原始报告', link: '/sources/' },
      { text: '全量库', link: '/library/' },
      { text: '对比与取舍', link: '/compare/' },
      { text: '关于', link: '/about' }
    ],
    sidebar: {
      '/handbook/': handbookSidebar,
      '/sources/': sourcesSidebar,
      '/library/': librarySidebar,
      '/compare/': [
        {
          text: '对比与取舍',
          items: [
            { text: '传统工程 vs Agent 时代：总表', link: '/compare/' },
            { text: '决策指南：什么时候用什么', link: '/compare/decision-guide' },
            { text: '共识度/佐证', link: '/compare/evidence' }
          ]
        }
      ]
    },
    outline: { level: [2, 3], label: '本页目录' },
    search: {
      provider: 'local',
      options: {
        // 全量库页面只是元数据表格（另有在线筛选），不进搜索索引，以保持索引小、加载快
        _render(src, env, md) {
          if (env.relativePath.startsWith('library/')) return ''
          return md.render(src, env)
        },
        translations: {
          button: { buttonText: '搜索', buttonAriaLabel: '搜索' },
          modal: {
            noResultsText: '没有找到结果',
            resetButtonTitle: '清除',
            footer: { selectText: '选择', navigateText: '切换', closeText: '关闭' }
          }
        }
      }
    },
    socialLinks: [{ icon: 'github', link: 'https://github.com/Atituiset' }],
    docFooter: { prev: '上一页', next: '下一页' },
    lastUpdated: { text: '最后更新' },
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '菜单',
    darkModeSwitchLabel: '外观',
    footer: {
      message: '原创文字以 CC BY 4.0 发布；摘要与引文版权归原作者所有，请以原文为准。',
      copyright: '© 2026 Atituiset'
    }
  }
})
