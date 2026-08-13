# 3D 柱状图组件 (Bar3D.vue)

> 基于 ECharts-GL 的 3D 柱状图，支持多维度数据展示、自动旋转。

---

```vue
<template>
  <div class="bar-3d">
    <div v-if="loading" class="chart-loading">
      <i class="el-icon-loading"></i>
    </div>
    <div ref="chartRef" class="chart-container"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts'
import 'echarts-gl'

export default {
  name: 'Bar3D',
  props: {
    data: {
      type: Array,
      default: () => [
        { x: 'Q1', y: '产品A', value: 80 },
        { x: 'Q2', y: '产品A', value: 95 },
        { x: 'Q3', y: '产品A', value: 70 },
        { x: 'Q4', y: '产品A', value: 85 },
        { x: 'Q1', y: '产品B', value: 65 },
        { x: 'Q2', y: '产品B', value: 75 },
        { x: 'Q3', y: '产品B', value: 90 },
        { x: 'Q4', y: '产品B', value: 60 },
        { x: 'Q1', y: '产品C', value: 55 },
        { x: 'Q2', y: '产品C', value: 70 },
        { x: 'Q3', y: '产品C', value: 80 },
        { x: 'Q4', y: '产品C', value: 75 }
      ]
    },
    xData: { type: Array, default: () => ['Q1', 'Q2', 'Q3', 'Q4'] },
    yData: { type: Array, default: () => ['产品A', '产品B', '产品C'] }
  },
  data() {
    return { chart: null, loading: true }
  },
  mounted() {
    this.$nextTick(() => { this.initChart() })
  },
  beforeDestroy() {
    if (this.chart) { this.chart.dispose(); this.chart = null }
    window.removeEventListener('resize', this.handleResize)
  },
  methods: {
    initChart() {
      const container = this.$refs.chartRef
      if (!container || container.clientWidth === 0 || container.clientHeight === 0) {
        this.loading = false
        return
      }
      this.chart = echarts.init(container)
      this.updateChart()
      window.addEventListener('resize', this.handleResize)
      this.loading = false
    },

    updateChart() {
      if (!this.chart) return

      const data = []
      this.xData.forEach((x, xi) => {
        this.yData.forEach((y, yi) => {
          const item = this.data.find(d => d.x === x && d.y === y)
          data.push([xi, yi, item ? item.value : 0])
        })
      })

      const option = {
        backgroundColor: 'transparent',
        tooltip: {
          backgroundColor: 'rgba(13, 27, 42, 0.9)',
          borderColor: 'rgba(0, 212, 255, 0.3)',
          textStyle: { color: '#fff' }
        },
        visualMap: {
          show: true,
          min: 0, max: 100,
          inRange: { color: ['#1e3a5f', '#00d4ff', '#00ff88', '#ffd700'] },
          textStyle: { color: '#87ceeb' },
          left: 10, bottom: 10
        },
        xAxis3D: {
          type: 'category',
          data: this.xData,
          axisLabel: { color: '#87ceeb', fontSize: 11 },
          axisLine: { lineStyle: { color: '#1e3a5f' } }
        },
        yAxis3D: {
          type: 'category',
          data: this.yData,
          axisLabel: { color: '#87ceeb', fontSize: 11 },
          axisLine: { lineStyle: { color: '#1e3a5f' } }
        },
        zAxis3D: {
          type: 'value',
          axisLabel: { color: '#87ceeb' },
          axisLine: { lineStyle: { color: '#1e3a5f' } }
        },
        grid3D: {
          boxWidth: 80, boxDepth: 50, boxHeight: 40,
          viewControl: {
            autoRotate: true, autoRotateSpeed: 5,
            distance: 180, alpha: 25, beta: 40
          },
          light: {
            main: { intensity: 1.2, shadow: true },
            ambient: { intensity: 0.3 }
          }
        },
        series: [{
          type: 'bar3D',
          data: data,
          shading: 'realistic',
          realisticMaterial: { roughness: 0.5, metalness: 0 },
          label: { show: false },
          emphasis: { itemStyle: { color: '#ffd700' } }
        }]
      }

      this.chart.setOption(option, true)
    },

    handleResize() {
      this.chart?.resize()
    }
  },
  watch: {
    data: { handler() { this.updateChart() }, deep: true }
  }
}
</script>

<style lang="scss" scoped>
.bar-3d {
  width: 100%;
  height: 100%;
  min-height: 300px;
  position: relative;
}

.chart-container { width: 100%; height: 100%; }

.chart-loading {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  color: #87ceeb;
  font-size: 24px;
}
</style>
```

---

## Props

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| data | Array | (预设示例) | 数据 [{x, y, value}] |
| xData | Array | ['Q1','Q2','Q3','Q4'] | X 轴分类 |
| yData | Array | ['产品A','产品B','产品C'] | Y 轴分类 |

---

## 数据格式

```javascript
bar3DData: [
  { x: 'Q1', y: '产品A', value: 80 },
  { x: 'Q2', y: '产品A', value: 95 }
]
```

---

## 依赖

```bash
npm install echarts echarts-gl --save
```
