# 柱状图组件 (ChartBar.vue)

> 基于 ECharts 5.x，支持横向/纵向柱状图，渐变配色。

---

```vue
<template>
  <div class="chart-bar">
    <div ref="chartRef" class="chart-container"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  name: 'ChartBar',
  props: {
    // 数据 [{ name, value }]
    data: { type: Array, default: () => [] },
    // 是否横向
    horizontal: { type: Boolean, default: true }
  },
  data() {
    return { chart: null }
  },
  watch: {
    data() { this.updateChart() }
  },
  mounted() {
    this.chart = echarts.init(this.$refs.chartRef)
    this.updateChart()
    window.addEventListener('resize', this.handleResize)
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.handleResize)
    if (this.chart) this.chart.dispose()
  },
  methods: {
    updateChart() {
      if (!this.chart) return
      const names = this.data.map(d => d.name)
      const values = this.data.map(d => d.value)

      const option = {
        tooltip: {
          trigger: 'axis',
          axisPointer: { type: 'shadow' },
          backgroundColor: 'rgba(13, 27, 42, 0.9)',
          borderColor: 'rgba(0, 210, 255, 0.3)',
          textStyle: { color: '#fff' }
        },
        grid: {
          left: '3%', right: '12%', top: '3%', bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'value',
          axisLine: { show: false },
          axisTick: { show: false },
          axisLabel: { color: 'rgba(255, 255, 255, 0.5)', fontSize: 10 },
          splitLine: { lineStyle: { color: 'rgba(0, 212, 255, 0.1)' } }
        },
        yAxis: {
          type: 'category',
          data: names,
          axisLine: { show: false },
          axisTick: { show: false },
          axisLabel: { color: '#87ceeb', fontSize: 11 }
        },
        series: [{
          type: 'bar',
          data: values,
          barWidth: 14,
          itemStyle: {
            borderRadius: [0, 4, 4, 0],
            color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
              { offset: 0, color: 'rgba(0, 212, 255, 0.3)' },
              { offset: 1, color: 'rgba(0, 212, 255, 0.9)' }
            ])
          },
          label: {
            show: true, position: 'right',
            color: '#00d4ff', fontSize: 11,
            fontFamily: 'JetBrains Mono, monospace'
          }
        }]
      }
      this.chart.setOption(option)
    },
    handleResize() {
      if (this.chart) this.chart.resize()
    }
  }
}
</script>

<style lang="scss" scoped>
.chart-bar, .chart-container { width: 100%; height: 100%; }
</style>
```

---

## 使用方式

```vue
<template>
  <div class="panel-frame">
    <div class="panel-title">数据分布</div>
    <ChartBar :data="barData" />
  </div>
</template>

<script>
import ChartBar from '@/components/ChartBar.vue'

export default {
  components: { ChartBar },
  data() {
    return {
      barData: [
        { name: '分类A', value: 120 },
        { name: '分类B', value: 80 },
        { name: '分类C', value: 60 },
        { name: '分类D', value: 40 }
      ]
    }
  }
}
</script>
```

## 数据格式

```javascript
[
  { name: '分类名称', value: 数值 },
  { name: '分类B', value: 80 }
]
```
