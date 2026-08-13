# 饼图组件 (ChartPie.vue)

> 基于 ECharts 5.x，支持饼图/环形图，内嵌标签。

---

```vue
<template>
  <div class="chart-pie">
    <div v-if="title" class="chart-title">{{ title }}</div>
    <div ref="chartRef" class="chart-container"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  name: 'ChartPie',
  props: {
    title: { type: String, default: '' },
    // 数据 [{ name, value }]
    data: { type: Array, default: () => [] },
    // 环形半径，默认环形图：['35%', '65%']，实心饼图：['0%', '65%']
    radius: { type: Array, default: () => ['35%', '65%'] },
    showLabel: { type: Boolean, default: true }
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
      const option = {
        tooltip: {
          trigger: 'item',
          backgroundColor: 'rgba(13, 27, 42, 0.9)',
          borderColor: 'rgba(0, 210, 255, 0.3)',
          textStyle: { color: '#fff' },
          formatter: '{b}: {c} ({d}%)'
        },
        legend: {
          show: this.showLabel,
          orient: 'horizontal',
          bottom: '5%',
          left: 'center',
          textStyle: { color: '#87ceeb', fontSize: 11 },
          itemWidth: 10,
          itemHeight: 10
        },
        series: [{
          type: 'pie',
          radius: this.radius,
          center: ['50%', '45%'],
          avoidLabelOverlap: false,
          itemStyle: {
            borderRadius: 4,
            borderColor: '#0a0e17',
            borderWidth: 2
          },
          label: {
            show: this.showLabel,
            position: 'inside',
            formatter: '{b}\n{d}%',
            color: '#fff',
            fontSize: 10
          },
          labelLine: { show: false },
          emphasis: {
            label: { show: true, fontSize: 12, fontWeight: 'bold' },
            itemStyle: { shadowBlur: 10, shadowOffsetX: 0, shadowColor: 'rgba(0, 0, 0, 0.5)' }
          },
          data: this.data,
          color: ['#00d2ff', '#00ff88', '#f5a623', '#9b59b6', '#e91e63', '#1abc9c']
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
.chart-pie { width: 100%; height: 100%; }
.chart-title { font-size: 16px; font-weight: 600; color: var(--text-primary); margin-bottom: 12px; }
.chart-container { width: 100%; height: calc(100% - 40px); }
</style>
```

---

## 使用方式

```vue
<template>
  <div class="panel-frame">
    <div class="panel-title">各品类占比</div>
    <ChartPie :data="pieData" />
  </div>
</template>

<script>
import ChartPie from '@/components/ChartPie.vue'

export default {
  components: { ChartPie },
  data() {
    return {
      pieData: [
        { name: '分类A', value: 35 },
        { name: '分类B', value: 25 },
        { name: '分类C', value: 20 },
        { name: '分类D', value: 15 },
        { name: '其他', value: 5 }
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
  { name: '分类B', value: 25 }
]
```
