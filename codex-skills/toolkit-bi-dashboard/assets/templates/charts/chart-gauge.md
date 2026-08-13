# 仪表盘组件 (ChartGauge.vue)

> ECharts 仪表盘组件，支持半圆/整圆、指针/弧形进度、中心数字，6主题CSS变量驱动。

---

## 组件模板

```vue
<template>
  <div class="chart-gauge">
    <div ref="chartRef" class="chart-container"></div>
    <div v-if="centerText" class="gauge-center">
      <div class="gauge-value" :style="{ color: 'var(--color-highlight)' }">{{ displayValue }}</div>
      <div class="gauge-label" :style="{ color: 'var(--color-text-muted)' }">{{ centerText }}</div>
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  name: 'ChartGauge',
  props: {
    // 当前值
    value: { type: Number, default: 0 },
    // 最大值
    max: { type: Number, default: 100 },
    // 仪表盘类型：half（半圆）/ full（整圆）
    type: { type: String, default: 'half' },
    // 中心文字
    centerText: { type: String, default: '' },
    // 单位
    unit: { type: String, default: '%' },
    // 起始角度（半圆默认225°，整圆默认90°）
    startAngle: { type: Number, default: null },
    // 结束角度（半圆默认-45°，整圆默认-270°）
    endAngle: { type: Number, default: null },
    // 是否显示指针
    showPointer: { type: Boolean, default: true },
    // 分段数（0表示不分段）
    splitNumber: { type: Number, default: 0 },
    // 分段颜色（如 [{ min: 0, max: 60, color: '#44FFAA' }, ...]）
    splitColors: { type: Array, default: () => [] },
  },
  data() {
    return {
      chart: null,
    }
  },
  computed: {
    displayValue() {
      if (this.value >= 10000) return (this.value / 10000).toFixed(1) + '万'
      return this.value.toFixed(this.value % 1 === 0 ? 0 : 1)
    },
    resolvedStartAngle() {
      if (this.startAngle !== null) return this.startAngle
      return this.type === 'half' ? 225 : 90
    },
    resolvedEndAngle() {
      if (this.endAngle !== null) return this.endAngle
      return this.type === 'half' ? -45 : -270
    },
  },
  watch: {
    value() { this.updateChart() },
  },
  mounted() {
    this.initChart()
    window.addEventListener('resize', this.handleResize)
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.handleResize)
    if (this.chart) {
      this.chart.dispose()
      this.chart = null
    }
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$refs.chartRef)
      this.updateChart()
    },
    updateChart() {
      if (!this.chart) return
      const primary = getComputedStyle(document.documentElement).getPropertyValue('--color-primary').trim() || '#00D4FF'
      const secondary = getComputedStyle(document.documentElement).getPropertyValue('--color-secondary').trim() || '#0088FF'
      const textMuted = getComputedStyle(document.documentElement).getPropertyValue('--color-text-muted').trim() || '#6B7FA3'

      const axisLine = {
        lineStyle: {
          width: 12,
          color: this.splitColors.length > 0
            ? this.splitColors
            : [
                [0.6, primary],
                [0.8, '#FFD93D'],
                [1, '#FF6B6B'],
              ],
        },
      }

      const option = {
        series: [{
          type: 'gauge',
          startAngle: this.resolvedStartAngle,
          endAngle: this.resolvedEndAngle,
          min: 0,
          max: this.max,
          splitNumber: this.splitNumber || (this.type === 'half' ? 5 : 10),
          axisLine,
          pointer: {
            show: this.showPointer,
            length: '60%',
            width: 4,
            itemStyle: { color: primary },
          },
          axisTick: {
            distance: -18,
            length: 4,
            lineStyle: { color: textMuted, width: 1 },
          },
          splitLine: {
            distance: -20,
            length: 10,
            lineStyle: { color: textMuted, width: 2 },
          },
          axisLabel: {
            distance: -28,
            color: textMuted,
            fontSize: 10,
          },
          detail: {
            show: false,
          },
          data: [{ value: this.value }],
          progress: {
            show: !this.showPointer,
            width: 12,
            itemStyle: { color: primary },
          },
          anchor: {
            show: this.showPointer,
            size: 12,
            itemStyle: {
              borderColor: primary,
              borderWidth: 2,
              color: 'var(--bg-panel-solid, #0C1A3A)',
            },
          },
        }],
      }

      this.chart.setOption(option, true)
    },
    handleResize() {
      if (this.chart) this.chart.resize()
    },
  },
}
</script>

<style lang="scss" scoped>
.chart-gauge {
  width: 100%;
  height: 100%;
  position: relative;
}

.chart-container {
  width: 100%;
  height: 100%;
}

.gauge-center {
  position: absolute;
  bottom: 18%;
  left: 50%;
  transform: translateX(-50%);
  text-align: center;
  pointer-events: none;
}

.gauge-value {
  font-size: 28px;
  font-weight: bold;
  font-family: var(--font-data, 'DIN Alternate', 'Roboto-Bold', sans-serif);
  line-height: 1.2;
}

.gauge-label {
  font-size: 12px;
  margin-top: 2px;
}
</style>
```

---

## Props

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| value | Number | 0 | 当前值 |
| max | Number | 100 | 最大值 |
| type | String | 'half' | 仪表盘类型：half（半圆）/ full（整圆） |
| centerText | String | '' | 中心文字标签 |
| unit | String | '%' | 单位 |
| startAngle | Number | null | 起始角度（null时自动：半圆225°，整圆90°） |
| endAngle | Number | null | 结束角度（null时自动：半圆-45°，整圆-270°） |
| showPointer | Boolean | true | 是否显示指针 |
| splitNumber | Number | 0 | 分段数（0自动） |
| splitColors | Array | [] | 分段颜色配置 |

---

## 使用示例

```vue
<!-- 半圆仪表盘（默认） -->
<ChartGauge :value="78.5" center-text="完成率" />

<!-- 整圆仪表盘 -->
<ChartGauge :value="92" type="full" center-text="健康指数" />

<!-- 弧形进度（无指针） -->
<ChartGauge :value="65" :show-pointer="false" center-text="CPU使用率" unit="%" />

<!-- 自定义分段颜色 -->
<ChartGauge
  :value="45"
  :split-colors="[
    { min: 0, max: 60, color: '#44FFAA' },
    { min: 60, max: 80, color: '#FFD93D' },
    { min: 80, max: 100, color: '#FF6B6B' },
  ]"
/>
```
