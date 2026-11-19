<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { withBase } from 'vitepress'

type Row = { n: number; s: string; c: string; t: string; a: string; d: string; u: string; u2: string; th: string; p: string[]; k: string; m: string; tp?: string; co?: string }
const rows = ref<Row[]>([])
const loading = ref(true)
const error = ref('')
const q = ref('')
const src = ref('')
const theme = ref('')
const pr = ref('')
const onlyPick = ref(false)
const topic = ref('')
const TOPICS: Record<string, string> = { 'quality-cicd': '质量与 CI/CD 专题', 'cn-bigtech': '国内大厂专题（全部）', 'cn:腾讯': '国内大厂 · 腾讯', 'cn:阿里': '国内大厂 · 阿里（含蚂蚁）', 'cn:字节': '国内大厂 · 字节' }
const topicOk = (r: Row) => !topic.value || (topic.value.startsWith('cn:') ? r.tp === 'cn-bigtech' && r.co === topic.value.slice(3) : r.tp === topic.value)
const page = ref(1)
const PER = 50
const THEMES: Record<string, string> = {
  workflow: '工作流与心智模型', context: '上下文与说明文件', plan: '计划与规格', verify: '测试与验证',
  review: '评审与代码质量', constraints: '约束与架构', tools: 'Hooks、Skills、子智能体与 MCP',
  parallel: '并行与长任务', security: '安全与权限', team: '团队、成本与组织', failures: '失败与反思', quality: '质量保障与 CI/CD', '': '未归类'
}
const PS = [
  ...Array.from({ length: 20 }, (_, i) => 'P' + String(i + 1).padStart(2, '0')),
  ...Array.from({ length: 13 }, (_, i) => 'Q' + String(i + 1).padStart(2, '0'))
]
const plink = (p: string) => withBase((p.startsWith('Q') ? '/handbook/12-quality-cicd#' : '/compare/evidence#') + p.toLowerCase())

onMounted(async () => {
  try {
    const r = await fetch(withBase('/data/sources.json'))
    rows.value = await r.json()
    const t = new URLSearchParams(window.location.search).get('topic')
    if (t && TOPICS[t]) topic.value = t
  } catch (e) {
    error.value = '数据加载失败，请改用下方的分页表格。'
  } finally {
    loading.value = false
  }
})
const sources = computed(() => Array.from(new Set(rows.value.map(r => r.s))))
const filtered = computed(() => {
  const kw = q.value.trim().toLowerCase()
  return rows.value.filter(r =>
    (!src.value || r.s === src.value) &&
    (!theme.value || r.th === (theme.value === '-' ? '' : theme.value)) &&
    (!pr.value || r.p.includes(pr.value)) &&
    (!onlyPick.value || !!r.k) &&
    topicOk(r) &&
    (!kw || (r.t + ' ' + r.a + ' ' + r.c).toLowerCase().includes(kw))
  )
})
const pages = computed(() => Math.max(1, Math.ceil(filtered.value.length / PER)))
const shown = computed(() => filtered.value.slice((page.value - 1) * PER, page.value * PER))
watch([q, src, theme, pr, onlyPick, topic], () => { page.value = 1 })
const distinctAuthors = computed(() => new Set(filtered.value.map(r => r.a)).size)
</script>

<template>
  <div class="se">
    <div class="se-controls">
      <input v-model="q" placeholder="关键词（标题、作者）" />
      <select v-model="src"><option value="">全部来源</option><option v-for="s in sources" :key="s" :value="s">{{ s }}</option></select>
      <select v-model="theme"><option value="">全部主题</option><option v-for="(v, k) in THEMES" :key="k" :value="k === '' ? '-' : k">{{ v }}</option></select>
      <select v-model="pr"><option value="">全部原则</option><option v-for="p in PS" :key="p" :value="p">{{ p }}</option></select>
      <select v-model="topic"><option value="">全部专题</option><option v-for="(v, k) in TOPICS" :key="k" :value="k">{{ v }}</option></select>
      <label><input type="checkbox" v-model="onlyPick" /> 只看精选</label>
    </div>
    <p v-if="loading">加载中…</p>
    <p v-else-if="error">{{ error }}</p>
    <template v-else>
      <p class="se-sum">匹配 {{ filtered.length }} 条（约 {{ distinctAuthors }} 个不同作者）· 第 {{ page }}/{{ pages }} 页</p>
      <table>
        <thead><tr><th>#</th><th>标题 / 摘录</th><th>作者</th><th>日期</th><th>原则</th><th>链接</th></tr></thead>
        <tbody>
          <tr v-for="r in shown" :key="r.n">
            <td>{{ r.n }}</td>
            <td>{{ r.t }}<br /><small>{{ r.c }} · {{ THEMES[r.th] }}<template v-if="r.co"> · {{ r.co }}</template></small></td>
            <td>{{ r.a }}</td>
            <td>{{ r.d }}</td>
            <td><a v-for="p in r.p" :key="p" :href="plink(p)">{{ p }} </a></td>
            <td>
              <a :href="r.u" target="_blank" rel="noopener">原文</a>
              <template v-if="r.u2"> · <a :href="r.u2" target="_blank" rel="noopener">文章</a></template>
              <template v-if="r.k"> · <a :href="withBase(r.k)">精选</a></template>
              <small> {{ r.m }}</small>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="se-pager">
        <button :disabled="page <= 1" @click="page--">上一页</button>
        <span>{{ page }} / {{ pages }}</span>
        <button :disabled="page >= pages" @click="page++">下一页</button>
      </div>
    </template>
  </div>
</template>

<style scoped>
.se-controls { display: flex; flex-wrap: wrap; gap: 8px; margin: 12px 0; }
.se-controls input[type='text'], .se-controls input:not([type]), .se-controls select {
  border: 1px solid var(--vp-c-divider); border-radius: 6px; padding: 4px 8px; background: var(--vp-c-bg-soft);
}
.se-sum { color: var(--vp-c-text-2); font-size: 14px; }
.se table { font-size: 13px; }
.se-pager { display: flex; gap: 12px; align-items: center; margin-top: 8px; }
.se-pager button { border: 1px solid var(--vp-c-divider); border-radius: 6px; padding: 2px 10px; }
.se-pager button:disabled { opacity: .4; }
</style>
