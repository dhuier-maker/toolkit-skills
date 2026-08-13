# 顶部卡片+网格布局模板

> 适用于多指标监控、KPI仪表盘场景。顶部KPI卡片行 + 下方2×2或2×3网格图表。

---

## 布局结构

```
┌─────────────────────────────────────────────────────────────┐
│                      顶部标题栏 (8%)                         │
├─────────────────────────────────────────────────────────────┤
│  [KPI卡片1]  [KPI卡片2]  [KPI卡片3]  [KPI卡片4]   (12%)     │
├─────────────────────┬───────────────────────────────────────┤
│                     │                                       │
│    图表1 (50%)      │          图表2 (50%)                  │
│                     │                                       │
├─────────────────────┼───────────────────────────────────────┤
│                     │                                       │
│    图表3 (50%)      │          图表4 (50%)                  │
│                     │                                       │
└─────────────────────┴───────────────────────────────────────┘
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

    <!-- KPI 卡片行 -->
    <div class="kpi-row">
      <div class="kpi-card" v-for="item in kpiData" :key="item.label">
        <div class="kpi-icon-wrap">
          <div class="kpi-icon">{{ item.icon }}</div>
        </div>
        <div class="kpi-info">
          <div class="kpi-value" v-html="formatKpi(item.value, { showTrend: true, trendValue: item.trend })"></div>
          <div class="kpi-label">{{ item.label }}</div>
        </div>
      </div>
    </div>

    <!-- 图表网格 -->
    <div class="chart-grid">
      <div class="chart-cell" v-for="(chart, index) in charts" :key="index">
        <div class="panel-frame">
          <div class="panel-title panel-title-variant-a"><span>{{ chart.title }}</span></div>
          <div class="chart-wrapper">
            <component :is="chart.component" v-bind="chart.props" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { formatKpi, formatTime } from '@/utils/number-format'
import ChartBar from '@/components/ChartBar.vue'
import ChartLine from '@/components/ChartLine.vue'
import ChartPie from '@/components/ChartPie.vue'
import ChartGauge from '@/components/ChartGauge.vue'
import ChartRank from '@/components/ChartRank.vue'

export default {
  name: 'Dashboard',
  components: { ChartBar, ChartLine, ChartPie, ChartGauge, ChartRank },
  data() {
    return {
      title: '数据监控大屏',
      currentTime: '',
      timer: null,
      kpiData: [
        { icon: '📊', label: '今日访问', value: 12856, trend: 12.5 },
        { icon: '💰', label: '营收总额', value: 3285.6, trend: 8.3 },
        { icon: '👤', label: '活跃用户', value: 9876, trend: -3.2 },
        { icon: '⭐', label: '好评率', value: 95.8, trend: 1.1 },
      ],
      charts: [
        { title: '趋势分析', component: 'ChartLine', props: { data: {} } },
        { title: '分类占比', component: 'ChartPie', props: { data: [] } },
        { title: '指标监控', component: 'ChartGauge', props: { value: 78 } },
        { title: '排名统计', component: 'ChartRank', props: { data: [] } },
      ],
    }
  },
  mounted() {
    this.updateTime()
    this.timer = setInterval(this.updateTime, 1000)
  },
  beforeDestroy() {
    if (this.timer) clearInterval(this.timer)
  },
  methods: {
    formatKpi,
    updateTime() {
      this.currentTime = formatTime(new Date(), 'HH:mm:ss')
    },
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

.kpi-row {
  display: flex;
  gap: 12px;
  padding: 12px 16px;
  flex-shrink: 0;
}

.kpi-card {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 16px;
  background: var(--bg-panel);
  border: 1px solid var(--border-panel);
  border-radius: 4px;
  transition: all 0.3s;
  &:hover { border-color: var(--color-primary); box-shadow: 0 0 12px var(--border-glow); }
}

.kpi-icon-wrap {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: rgba(var(--color-primary-rgb, 0, 212, 255), 0.12);
  border: 1px solid rgba(var(--color-primary-rgb, 0, 212, 255), 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.kpi-icon { font-size: 20px; }

.kpi-info { flex: 1; min-width: 0; }
.kpi-value { font-size: 24px; font-weight: bold; color: var(--color-title); font-family: var(--font-data); }
.kpi-label { font-size: 12px; color: var(--color-text-muted); margin-top: 2px; }

.chart-grid {
  flex: 1;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 12px;
  padding: 0 16px 16px;
  min-height: 0;
}

.chart-cell {
  min-height: 0;
  display: flex;
  flex-direction: column;
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

.chart-wrapper {
  flex: 1;
  min-height: 0;
}
</style>
```

---

## 网格变体

| 变体 | grid-template-columns | grid-template-rows | 说明 |
|------|----------------------|--------------------|------|
| 2×2 | `1fr 1fr` | `1fr 1fr` | 4个等大图表 |
| 2×3 | `1fr 1fr 1fr` | `1fr 1fr` | 6个等大图表 |
| 左大右小 | `2fr 1fr` | `1fr 1fr` | 左侧跨2行大图表 |

---

## 触发词

| 触发词 | 布局 |
|--------|------|
| 监控大屏、指标大屏、KPI大屏、卡片大屏 | 顶部卡片+网格 |
