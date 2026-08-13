# 2D 散点图模板 (ChartScatter)

> ECharts 5.x 2D 散点图组件，支持气泡大小映射、坐标轴规范、6 主题配色。

---

## 功能

- 2D 散点/气泡图
- 气泡大小映射（symbolSize 函数）
- 坐标轴统一规范（轴线/刻度/分割线）
- 多系列对比
- 自动响应窗口 resize

---

## Props

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| data | Array | [] | 散点数据 |
| xName | String | '' | X 轴名称 |
| yName | String | '' | Y 轴名称 |
| symbolSize | [Number, Function] | 10 | 散点大小，支持函数 |
| showLabel | Boolean | false | 是否显示标签 |
| splitNumber | Number | 5 | Y 轴分割段数 |

---

## 数据格式

```javascript
// 单系列
scatterData: [
  { name: '项目A', x: 10, y: 20, size: 30 },
  { name: '项目B', x: 25, y: 45, size: 15 },
]

// 多系列
seriesData: [
  { name: '分类1', data: [{ x: 10, y: 20, size: 30 }] },
  { name: '分类2', data: [{ x: 15, y: 35, size: 20 }] },
]
```

---

## Vue 组件代码

```vue
<template>
  <div ref="chartRef" class="chart-scatter" :style="{ height: height }"></div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  name: 'ChartScatter',
  props: {
    data: { type: Array, default: () => [] },
    seriesData: { type: Array, default: () => [] },
    height: { type: String, default: '100%' },
    xName: { type: String, default: '' },
    yName: { type: String, default: '' },
    symbolSize: { type: [Number, Function], default: 10 },
    showLabel: { type: Boolean, default: false },
    splitNumber: { type: Number, default: 5 },
  },
  data() {
    return { chart: null }
  },
  computed: {
    themeColors() {
      const palette = getComputedStyle(document.documentElement).getPropertyValue('--chart-palette')?.trim()
      return palette ? palette.split(',') : ['#00D4FF', '#0088FF', '#FF6B6B', '#FFD93D', '#44FFAA', '#A855F7']
    },
  },
  watch: {
    data: { handler() { this.render() }, deep: true },
    seriesData: { handler() { this.render() }, deep: true },
  },
  mounted() {
    this.initChart()
    window.addEventListener('resize', this.handleResize)
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.handleResize)
    if (this.chart) { this.chart.dispose(); this.chart = null }
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$refs.chartRef)
      this.render()
    },
    render() {
      if (!this.chart) return
      const root = getComputedStyle(document.documentElement)
      const pv = (n) => root.getPropertyValue(n).trim()

      const series = this.seriesData.length > 0
        ? this.seriesData.map((s, i) => ({
            name: s.name,
            type: 'scatter',
            data: s.data.map(d => [d.x, d.y, d.size || 10]),
            symbolSize: typeof this.symbolSize === 'function'
              ? (val) => this.symbolSize(val[2])
              : this.symbolSize,
            itemStyle: { color: this.themeColors[i % this.themeColors.length] },
            label: {
              show: this.showLabel,
              formatter: '{b}',
              color: pv('--color-text-muted') || '#6B7FA3',
              fontSize: 10,
              position: 'top',
            },
          }))
        : [{
            type: 'scatter',
            data: this.data.map(d => [d.x, d.y, d.size || 10]),
            symbolSize: typeof this.symbolSize === 'function'
              ? (val) => this.symbolSize(val[2])
              : this.symbolSize,
            itemStyle: { color: this.themeColors[0] },
            label: {
              show: this.showLabel,
              formatter: (p) => this.data[p.dataIndex]?.name || '',
              color: pv('--color-text-muted') || '#6B7FA3',
              fontSize: 10,
              position: 'top',
            },
          }]

      this.chart.setOption({
        tooltip: {
          trigger: 'item',
          backgroundColor: pv('--bg-panel-solid') || '#0C1A3A',
          borderColor: pv('--border-panel') || 'rgba(0,212,255,0.3)',
          textStyle: { color: pv('--color-text') || '#E0E8FF', fontSize: 12 },
        },
        grid: { left: 50, right: 20, top: 30, bottom: 40 },
        xAxis: {
          type: 'value',
          name: this.xName,
          nameTextStyle: { color: pv('--color-text-muted') || '#6B7FA3', fontSize: 11 },
          axisLine: { lineStyle: { color: pv('--chart-axis-line') || 'rgba(0,212,255,0.3)', width: 1 } },
          axisTick: { show: false },
          axisLabel: { color: pv('--color-text-muted') || '#6B7FA3', fontSize: 11 },
          splitLine: { show: false },
        },
        yAxis: {
          type: 'value',
          name: this.yName,
          nameTextStyle: { color: pv('--color-text-muted') || '#6B7FA3', fontSize: 11 },
          axisLine: { show: false },
          axisTick: { show: false },
          axisLabel: { color: pv('--color-text-muted') || '#6B7FA3', fontSize: 11 },
          splitLine: { lineStyle: { color: pv('--chart-split-line') || 'rgba(0,212,255,0.08)', type: 'dashed' } },
          splitNumber: this.splitNumber,
        },
        series,
      }, true)
    },
    handleResize() {
      this.chart?.resize()
    },
  },
}
</script>

<style scoped>
.chart-scatter { width: 100%; min-height: 200px; }
</style>
```

---

## 使用示例

```vue
<template>
  <div class="panel-frame">
    <div class="panel-title"><span class="title-bar"></span><span>区域分布</span></div>
    <ChartScatter
      :data="scatterData"
      x-name="经度"
      y-name="纬度"
      :symbol-size="symbolFn"
      show-label
    />
  </div>
</template>

<script>
import ChartScatter from '@/components/ChartScatter.vue'

export default {
  components: { ChartScatter },
  data() {
    return {
      scatterData: [
        { name: '区域A', x: 10, y: 20, size: 30 },
        { name: '区域B', x: 25, y: 45, size: 15 },
        { name: '区域C', x: 40, y: 30, size: 25 },
      ],
    }
  },
  methods: {
    symbolFn(val) {
      return Math.max(6, val * 0.5)
    },
  },
}
</script>
```
