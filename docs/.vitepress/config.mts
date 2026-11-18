import { defineConfig } from 'vitepress'

// ⬇️ 部署到 GitHub Pages 时的仓库名：只需改这一处（例如 '/my-repo/'；若用自定义域名或 <user>.github.io 仓库则改为 '/'）
const REPO_NAME = 'agent-engineering-handbook'
const BASE = REPO_NAME ? `/${REPO_NAME}/` : '/'

const handbookSidebar = [
  {
    text: '实践手册',
    items: [
      { text: '总览：一页读懂', link: '/handbook/' },
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
      { text: '11 速查表与 Checklist', link: '/handbook/11-checklists' }
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
      { text: 'X（Twitter）上的一线声音', link: '/sources/x-posts' },
      { text: '中文互联网', link: '/sources/chinese' },
      { text: 'GitHub 开源项目与规范', link: '/sources/open-source' },
      { text: '研究、调查与社区讨论', link: '/sources/research' },
      { text: '安全专题', link: '/sources/security' }
    ]
  }
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
      { text: '对比与取舍', link: '/compare/' },
      { text: '关于', link: '/about' }
    ],
    sidebar: {
      '/handbook/': handbookSidebar,
      '/sources/': sourcesSidebar,
      '/compare/': [
        {
          text: '对比与取舍',
          items: [
            { text: '传统工程 vs Agent 时代：总表', link: '/compare/' },
            { text: '决策指南：什么时候用什么', link: '/compare/decision-guide' }
          ]
        }
      ]
    },
    outline: { level: [2, 3], label: '本页目录' },
    search: {
      provider: 'local',
      options: {
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
