# 左右对称布局模板

> 适用于纯数据对比分析场景，左右50%对称，无地图。

---

## 布局结构

```
┌─────────────────────────────────────────────────────────────┐
│                      顶部标题栏 (8%)                         │
├─────────────────────────────┬───────────────────────────────┤
│                             │                               │
│      左侧区域 (50%)         │       右侧区域 (50%)          │
│                             │                               │
│  面板1                      │   面板4                       │
│  面板2                      │   面板5                       │
│  面板3                      │   面板6                       │
│                             │                               │
└─────────────────────────────┴───────────────────────────────┘
```

---

## Dashboard.vue 核心模板

```vue
<template>
  <div class="bi-dashboard">
    <!-- 顶部标题 -->
    <header class="bi-header">
      <div class="wing-left"></div>
      <div class="diamond"></div>
      <h1 class="page-title">{{ title }}</h1>
      <div class="diamond"></div>
      <div class="wing-right"></div>
      <div class="header-time">{{ currentTime }}</div>
    </header>

    <!-- 对称双栏 -->
    <div class="split-content">
      <div class="split-half left-half">
        <div class="panel-frame" v-for="panel in leftPanels" :key="panel.title">
          <div class="panel-title panel-title-variant-b"><span>{{ panel.title }}</span></div>
          <div class="panel-body">
            <component :is="panel.component" v-bind="panel.props" />
          </div>
        </div>
      </div>
      <div class="split-divider"></div>
      <div class="split-half right-half">
        <div class="panel-frame" v-for="panel in rightPanels" :key="panel.title">
          <div class="panel-title panel-title-variant-b"><span>{{ panel.title }}</span></div>
          <div class="panel-body">
            <component :is="panel.component" v-bind="panel.props" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ChartBar from '@/components/ChartBar.vue'
import ChartLine from '@/components/ChartLine.vue'
import ChartPie from '@/components/ChartPie.vue'
import ChartRank from '@/components/ChartRank.vue'

export default {
  name: 'Dashboard',
  components: { ChartBar, ChartLine, ChartPie, ChartRank },
  data() {
    return {
      title: '数据分析大屏',
      currentTime: '',
      leftPanels: [
        { title: '趋势对比', component: 'ChartLine', props: {} },
        { title: '分类统计', component: 'ChartBar', props: {} },
      ],
      rightPanels: [
        { title: '占比分析', component: 'ChartPie', props: {} },
        { title: '排名数据', component: 'ChartRank', props: {} },
      ],
    }
  },
}
</script>

<style lang="scss" scoped>
.bi-dashboard {
  width: 1920px;
  height: 1080px;
  background: var(--bg-page);
  color: var(--color-text);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  font-family: var(--font-body);
}

.split-content {
  flex: 1;
  display: flex;
  gap: 0;
  padding: 12px 16px;
  min-height: 0;
}

.split-half {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 12px;
  min-height: 0;
  min-width: 0;
}

.split-divider {
  width: 1px;
  background: linear-gradient(180deg, transparent, var(--color-primary), transparent);
  margin: 0 8px;
  flex-shrink: 0;
}

.panel-frame {
  flex: 1;
  min-height: 0;
  display: flex;
  flex-direction: column;
  background: var(--bg-panel);
  border: 1px solid var(--border-panel);
  border-radius: 4px;
  padding: 14px;
}

.panel-body {
  flex: 1;
  min-height: 0;
}
</style>
```

---

## 触发词

| 触发词 | 布局 |
|--------|------|
| 对称大屏、对比大屏、数据分析大屏、左右对比 | 左右对称 |
