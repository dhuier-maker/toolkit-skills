# 上中下三段布局模板

> 适用于数据分析类大屏，顶部KPI + 中间主图表 + 底部辅助图表/列表。

---

## 布局结构

```
┌─────────────────────────────────────────────────────────────┐
│                      顶部标题栏 (8%)                         │
├─────────────────────────────────────────────────────────────┤
│  [KPI1]  [KPI2]  [KPI3]  [KPI4]  [KPI5]    (顶部 12%)      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│              中间主图表区域 (中间 50%)                        │
│              (大折线图/柱状图/组合图)                         │
│                                                             │
├─────────────────────┬───────────────────────────────────────┤
│   底部左图表 (30%)  │       底部右图表 (70%)    (底部 30%)   │
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

    <!-- KPI 横条 -->
    <div class="kpi-strip">
      <div class="kpi-item" v-for="item in kpiData" :key="item.label">
        <span class="kpi-num">{{ formatNumber(item.value) }}</span>
        <span class="kpi-label">{{ item.label }}</span>
      </div>
    </div>

    <!-- 中间主图表 -->
    <div class="middle-section">
      <div class="panel-frame main-chart">
        <div class="panel-title panel-title-variant-a"><span>{{ mainChart.title }}</span></div>
        <div class="chart-wrapper">
          <component :is="mainChart.component" v-bind="mainChart.props" />
        </div>
      </div>
    </div>

    <!-- 底部辅助区 -->
    <div class="bottom-section">
      <div class="bottom-left">
        <div class="panel-frame">
          <div class="panel-title panel-title-variant-a"><span>{{ bottomLeft.title }}</span></div>
          <div class="chart-wrapper">
            <component :is="bottomLeft.component" v-bind="bottomLeft.props" />
          </div>
        </div>
      </div>
      <div class="bottom-right">
        <div class="panel-frame">
          <div class="panel-title panel-title-variant-a"><span>{{ bottomRight.title }}</span></div>
          <div class="chart-wrapper">
            <component :is="bottomRight.component" v-bind="bottomRight.props" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { formatNumber } from '@/utils/number-format'
import ChartBar from '@/components/ChartBar.vue'
import ChartLine from '@/components/ChartLine.vue'
import ChartPie from '@/components/ChartPie.vue'

export default {
  name: 'Dashboard',
  components: { ChartBar, ChartLine, ChartPie },
  data() {
    return {
      title: '数据分析大屏',
      currentTime: '',
      kpiData: [
        { label: '总营收', value: 328560000 },
        { label: '月活用户', value: 1285600 },
        { label: '转化率', value: 85.3 },
        { label: '客单价', value: 356 },
        { label: '增长率', value: 12.5 },
      ],
      mainChart: { title: '月度趋势', component: 'ChartLine', props: {} },
      bottomLeft: { title: '分类占比', component: 'ChartPie', props: {} },
      bottomRight: { title: '对比分析', component: 'ChartBar', props: {} },
    }
  },
  methods: { formatNumber },
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

.kpi-strip {
  display: flex;
  justify-content: space-around;
  padding: 10px 24px;
  background: var(--bg-panel);
  border-bottom: 1px solid var(--border-panel);
  flex-shrink: 0;
}

.kpi-item { text-align: center; }
.kpi-num {
  display: block;
  font-size: 22px;
  font-weight: bold;
  color: var(--color-highlight);
  font-family: var(--font-data);
}
.kpi-label {
  font-size: 12px;
  color: var(--color-text-muted);
}

.middle-section {
  flex: 5;
  padding: 12px 16px;
  min-height: 0;
}

.main-chart {
  height: 100%;
  display: flex;
  flex-direction: column;
}

.bottom-section {
  flex: 3;
  display: flex;
  gap: 12px;
  padding: 0 16px 16px;
  min-height: 0;
}

.bottom-left { flex: 3; }
.bottom-right { flex: 7; }

.panel-frame {
  height: 100%;
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

## 触发词

| 触发词 | 布局 |
|--------|------|
| 数据分析大屏、报表大屏、三段大屏、趋势大屏 | 上中下三段 |
