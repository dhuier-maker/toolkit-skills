# 组织架构图模板 (ChartOrg)

> ECharts 5.x 树形/组织架构图组件，支持节点交互、6 主题配色。

---

## Props

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| data | Object | {} | 树形数据 |
| orient | String | 'vertical' | 方向：vertical / horizontal |
| labelField | String | 'name' | 节点名称字段 |

---

## 数据格式

```javascript
orgData: {
  name: '总裁办',
  children: [
    {
      name: '技术部',
      children: [
        { name: '前端组' },
        { name: '后端组' },
        { name: '测试组' },
      ]
    },
    {
      name: '运营部',
      children: [
        { name: '市场组' },
        { name: '客服组' },
      ]
    },
  ]
}
```

---

## Vue 组件代码

```vue
<template>
  <div ref="chartRef" class="chart-org" :style="{ height: height }"></div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  name: 'ChartOrg',
  props: {
    data: { type: Object, default: () => ({}) },
    orient: { type: String, default: 'vertical' },
    labelField: { type: String, default: 'name' },
    height: { type: String, default: '100%' },
  },
  data() { return { chart: null } },
  watch: { data: { handler() { this.render() }, deep: true } },
  mounted() {
    this.chart = echarts.init(this.$refs.chartRef)
    this.render()
    window.addEventListener('resize', this.handleResize)
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.handleResize)
    this.chart?.dispose()
  },
  methods: {
    render() {
      if (!this.chart) return
      const root = getComputedStyle(document.documentElement)
      const pv = (n) => root.getPropertyValue(n).trim()
      const primaryColor = pv('--color-primary') || '#00D4FF'

      this.chart.setOption({
        tooltip: {
          trigger: 'item',
          backgroundColor: pv('--bg-panel-solid') || '#0C1A3A',
          borderColor: pv('--border-panel') || 'rgba(0,212,255,0.3)',
          textStyle: { color: pv('--color-text') || '#E0E8FF', fontSize: 12 },
        },
        series: [{
          type: 'tree',
          data: [this.data],
          orient: this.orient,
          top: '5%', bottom: '5%', left: '10%', right: '10%',
          symbol: 'rect',
          symbolSize: [80, 30],
          initialTreeDepth: 2,
          animationDurationUpdate: 500,
          label: {
            show: true,
            fontSize: 11,
            color: pv('--color-text') || '#E0E8FF',
            formatter: (params) => params.data[this.labelField] || params.name,
          },
          itemStyle: {
            color: pv('--bg-card') || 'rgba(0, 20, 40, 0.5)',
            borderColor: primaryColor,
            borderWidth: 1,
            borderRadius: 4,
          },
          lineStyle: {
            color: rgba(var('--color-primary-rgb'), 0.3),
            width: 1,
            curveness: 0.5,
          },
          emphasis: {
            itemStyle: {
              borderColor: primaryColor,
              borderWidth: 2,
              shadowBlur: 8,
              shadowColor: `rgba(${pv('--color-primary-rgb') || '0,212,255'}, 0.3)`,
            },
          },
          leaves: {
            label: { fontSize: 10 },
          },
        }],
      }, true)
    },
    handleResize() { this.chart?.resize() },
  },
}
</script>

<style scoped>
.chart-org { width: 100%; min-height: 300px; }
</style>
```

---

## 使用示例

```vue
<template>
  <div class="panel-frame">
    <div class="panel-title"><span class="title-bar"></span><span>组织架构</span></div>
    <ChartOrg :data="orgData" orient="vertical" />
  </div>
</template>
```
