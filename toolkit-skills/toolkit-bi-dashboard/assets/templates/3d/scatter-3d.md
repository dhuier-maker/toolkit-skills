# 3D 散点图组件 (Scatter3D.vue)

> 基于 ECharts-GL 的 3D 散点图，三维数据分布可视化。

---

```vue
<template>
  <div class="scatter-3d">
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
  name: 'Scatter3D',
  props: {
    // 数据 [{ name, x, y, z, value }]
    data: {
      type: Array,
      default: () => [
        { name: 'A', x: 10, y: 20, z: 30, value: 50 },
        { name: 'B', x: 20, y: 30, z: 40, value: 70 },
        { name: 'C', x: 30, y: 10, z: 50, value: 90 },
        { name: 'D', x: 40, y: 50, z: 20, value: 60 },
        { name: 'E', x: 50, y: 40, z: 10, value: 80 },
        { name: 'F', x: 15, y: 35, z: 25, value: 45 },
        { name: 'G', x: 35, y: 25, z: 35, value: 75 },
        { name: 'H', x: 25, y: 45, z: 45, value: 55 },
        { name: 'I', x: 45, y: 15, z: 15, value: 65 },
        { name: 'J', x: 55, y: 55, z: 55, value: 95 }
      ]
    },
    // 数值范围（用于 visualMap）
    minValue: { type: Number, default: 0 },
    maxValue: { type: Number, default: 100 },
    // 符号大小
    symbolSize: { type: Number, default: 12 }
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

      const scatterData = this.data.map(item => ({
        value: [item.x, item.y, item.z, item.value || 0],
        name: item.name
      }))

      const option = {
        backgroundColor: 'transparent',
        tooltip: {
          backgroundColor: 'rgba(13, 27, 42, 0.9)',
          borderColor: 'rgba(0, 212, 255, 0.3)',
          textStyle: { color: '#fff' },
          formatter: (params) => {
            return `${params.name}<br/>X: ${params.value[0]}<br/>Y: ${params.value[1]}<br/>Z: ${params.value[2]}<br/>值: ${params.value[3]}`
          }
        },
        visualMap: {
          show: true,
          min: this.minValue,
          max: this.maxValue,
          dimension: 3,
          inRange: {
            color: ['#1e3a5f', '#00d4ff', '#00ff88', '#ffd700', '#ff6b6b']
          },
          textStyle: { color: '#87ceeb' },
          left: 10,
          bottom: 10
        },
        xAxis3D: {
          type: 'value',
          name: 'X',
          nameTextStyle: { color: '#87ceeb' },
          axisLabel: { color: '#87ceeb' },
          axisLine: { lineStyle: { color: '#1e3a5f' } }
        },
        yAxis3D: {
          type: 'value',
          name: 'Y',
          nameTextStyle: { color: '#87ceeb' },
          axisLabel: { color: '#87ceeb' },
          axisLine: { lineStyle: { color: '#1e3a5f' } }
        },
        zAxis3D: {
          type: 'value',
          name: 'Z',
          nameTextStyle: { color: '#87ceeb' },
          axisLabel: { color: '#87ceeb' },
          axisLine: { lineStyle: { color: '#1e3a5f' } }
        },
        grid3D: {
          viewControl: {
            autoRotate: true,
            autoRotateSpeed: 8,
            distance: 200,
            alpha: 20,
            beta: 30
          },
          light: {
            main: { intensity: 1.2, shadow: true },
            ambient: { intensity: 0.3 }
          }
        },
        series: [{
          type: 'scatter3D',
          data: scatterData,
          symbolSize: (val) => Math.max(6, val[3] / 10),
          itemStyle: {
            opacity: 0.8,
            borderWidth: 1,
            borderColor: '#fff'
          },
          emphasis: {
            itemStyle: { opacity: 1 }
          }
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
.scatter-3d {
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
| data | Array | (预设示例) | 数据 [{name, x, y, z, value}] |
| minValue | Number | 0 | visualMap 最小值 |
| maxValue | Number | 100 | visualMap 最大值 |
| symbolSize | Number | 12 | 符号大小基准值 |

---

## 数据格式

```javascript
scatter3DData: [
  { name: 'A', x: 10, y: 20, z: 30, value: 50 },
  { name: 'B', x: 20, y: 30, z: 40, value: 70 }
]
```

---

## 依赖

```bash
npm install echarts echarts-gl --save
```
