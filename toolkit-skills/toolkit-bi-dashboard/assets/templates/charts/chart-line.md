# 折线图组件 (ChartLine.vue)

> 基于 ECharts 5.x，支持平滑曲线、面积填充、symbol 控制。

---

```vue
<template>
  <div class="chart-line">
    <div v-if="title" class="chart-title">{{ title }}</div>
    <div ref="chartRef" class="chart-container"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  name: 'ChartLine',
  props: {
    title: { type: String, default: '' },
    // X轴数据 ['1月', '2月', ...]
    xData: { type: Array, default: () => [] },
    // Y轴数据 [10, 20, ...]
    yData: { type: Array, default: () => [] },
    yName: { type: String, default: '' },
    // 是否平滑曲线
    smooth: { type: Boolean, default: true },
    // 是否显示面积
    areaStyle: { type: Boolean, default: true },
    // 是否显示数据点
    showSymbol: { type: Boolean, default: false }
  },
  data() {
    return { chart: null }
  },
  watch: {
    xData() { this.updateChart() },
    yData() { this.updateChart() }
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
          trigger: 'axis',
          backgroundColor: 'rgba(13, 27, 42, 0.9)',
          borderColor: 'rgba(0, 210, 255, 0.3)',
          textStyle: { color: '#fff' }
        },
        grid: {
          left: '3%', right: '4%', top: '8%', bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          data: this.xData,
          boundaryGap: false,
          axisLine: { show: false },
          axisTick: { show: false },
          axisLabel: { color: 'rgba(255, 255, 255, 0.5)', fontSize: 11 }
        },
        yAxis: {
          type: 'value',
          name: this.yName,
          nameTextStyle: { color: '#87ceeb', fontSize: 11 },
          axisLine: { show: false },
          axisTick: { show: false },
          axisLabel: { color: 'rgba(255, 255, 255, 0.5)', fontSize: 11 },
          splitLine: { lineStyle: { color: 'rgba(0, 212, 255, 0.1)' } }
        },
        series: [{
          type: 'line',
          data: this.yData,
          smooth: this.smooth,
          symbol: this.showSymbol ? 'circle' : 'none',
          symbolSize: 6,
          lineStyle: { color: '#00d4ff', width: 2 },
          itemStyle: { color: '#00d4ff' },
          areaStyle: this.areaStyle ? {
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
              { offset: 0, color: 'rgba(0, 212, 255, 0.4)' },
              { offset: 1, color: 'rgba(0, 212, 255, 0.05)' }
            ])
          } : null
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
.chart-line { width: 100%; height: 100%; }
.chart-title { font-size: 16px; font-weight: 600; color: var(--text-primary); margin-bottom: 12px; }
.chart-container { width: 100%; height: calc(100% - 40px); }
</style>
```

---

## 使用方式

```vue
<template>
  <div class="panel-frame">
    <div class="panel-title">趋势分析</div>
    <ChartLine :x-data="months" :y-data="values" title="月度趋势" />
  </div>
</template>

<script>
import ChartLine from '@/components/ChartLine.vue'

export default {
  components: { ChartLine },
  data() {
    return {
      months: ['1月', '2月', '3月', '4月', '5月', '6月'],
      values: [120, 200, 150, 80, 70, 110]
    }
  }
}
</script>
```

## Props

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| title | String | '' | 图表标题 |
| xData | Array | [] | X轴数据 |
| yData | Array | [] | Y轴数据 |
| yName | String | '' | Y轴名称 |
| smooth | Boolean | true | 是否平滑曲线 |
| areaStyle | Boolean | true | 是否显示面积 |
| showSymbol | Boolean | false | 是否显示数据点 |
