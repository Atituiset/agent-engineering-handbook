import DefaultTheme from 'vitepress/theme'
import SourceExplorer from './SourceExplorer.vue'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('SourceExplorer', SourceExplorer)
  }
}
