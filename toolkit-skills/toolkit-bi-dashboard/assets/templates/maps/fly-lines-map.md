# 飞线地图组件 (FlyLinesMap.vue)

> 基于 ECharts 5.x，OD 流向可视化，端点脉冲动画。

---

```vue
<template>
  <div class="fly-lines-map">
    <div v-if="loading" class="map-loading">
      <i class="el-icon-loading"></i>
      <span>加载中...</span>
    </div>
    <div ref="chartRef" class="chart-container"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  name: 'FlyLinesMap',
  props: {
    lines: {
      type: Array,
      default: () => [
        { fromName: '北京', toName: '上海', fromCoords: [116.4551, 40.2539], toCoords: [121.4648, 31.2891], value: 95 },
        { fromName: '北京', toName: '广州', fromCoords: [116.4551, 40.2539], toCoords: [113.5107, 23.2196], value: 90 },
        { fromName: '北京', toName: '深圳', fromCoords: [116.4551, 40.2539], toCoords: [114.0710, 22.5431], value: 80 },
        { fromName: '上海', toName: '成都', fromCoords: [121.4648, 31.2891], toCoords: [103.9526, 30.7617], value: 70 },
        { fromName: '广州', toName: '杭州', fromCoords: [113.5107, 23.2196], toCoords: [119.5313, 29.8773], value: 60 }
      ]
    },
    center: { type: Array, default: () => [104, 36] },
    zoom: { type: Number, default: 1.2 }
  },
  data() {
    return { chart: null, loading: true }
  },
  async mounted() {
    await this.initChart()
  },
  beforeDestroy() {
    if (this.chart) { this.chart.dispose() }
    window.removeEventListener('resize', this.handleResize)
  },
  methods: {
    async initChart() {
      try {
        this.loading = true
        const geoJson = await this.loadMapData()
        echarts.registerMap('china', geoJson)
        this.chart = echarts.init(this.$refs.chartRef)
        this.updateChart()
        window.addEventListener('resize', this.handleResize)
        this.loading = false
      } catch (e) {
        console.error('飞线地图初始化失败:', e)
        this.loading = false
      }
    },

    async loadMapData() {
      const urls = [
        'https://fastly.jsdelivr.net/npm/@jiaminghi/china-map-geojson@1.0.0/china.json',
        'https://cdn.jsdelivr.net/npm/@jiaminghi/china-map-geojson@1.0.0/china.json'
      ]
      for (const url of urls) {
        try {
          const res = await fetch(url)
          if (res.ok) return await res.json()
        } catch (e) { console.warn('加载失败:', url) }
      }
      return null
    },

    updateChart() {
      if (!this.chart || !this.lines.length) return

      const linesData = this.lines.map(line => ({
        fromName: line.fromName, toName: line.toName,
        coords: [line.fromCoords, line.toCoords], value: line.value
      }))

      const pointsData = []
      const addedPoints = new Set()
      this.lines.forEach(line => {
        const fromKey = `${line.fromCoords[0]}-${line.fromCoords[1]}`
        const toKey = `${line.toCoords[0]}-${line.toCoords[1]}`
        if (!addedPoints.has(fromKey)) {
          pointsData.push({ name: line.fromName, value: [...line.fromCoords, line.value || 0], itemStyle: { color: '#00d4ff' } })
          addedPoints.add(fromKey)
        }
        if (!addedPoints.has(toKey)) {
          pointsData.push({ name: line.toName, value: [...line.toCoords, line.value || 0], itemStyle: { color: '#ffd700' } })
          addedPoints.add(toKey)
        }
      })

      const option = {
        backgroundColor: 'transparent',
        tooltip: {
          trigger: 'item',
          backgroundColor: 'rgba(13, 27, 42, 0.9)',
          borderColor: 'rgba(0, 212, 255, 0.3)',
          textStyle: { color: '#fff' },
          formatter: (params) => {
            if (params.data.fromName) {
              return `${params.data.fromName} → ${params.data.toName}<br/>流量: ${params.data.value}`
            }
            return params.name
          }
        },
        geo: {
          map: 'china',
          roam: true,
          zoom: this.zoom,
          center: this.center,
          itemStyle: { areaColor: '#0d1b2a', borderColor: '#1e3a5f', borderWidth: 1 },
          emphasis: { itemStyle: { areaColor: '#1e3a5f', borderColor: '#00d4ff' } },
          label: { show: false }
        },
        series: [
          {
            type: 'lines', coordinateSystem: 'geo', zlevel: 2,
            effect: { show: true, period: 6, trailLength: 0.7, symbol: 'arrow', symbolSize: 10, color: '#ffd700', loop: true },
            lineStyle: { color: '#00d4ff', width: 1.5, curveness: 0.3, opacity: 0.6 },
            data: linesData
          },
          {
            type: 'effectScatter', coordinateSystem: 'geo', zlevel: 2,
            rippleEffect: { period: 4, brushType: 'stroke', scale: 4 },
            label: { show: true, position: 'right', formatter: '{b}', fontSize: 11, color: '#fff' },
            symbol: 'circle',
            symbolSize: (val) => Math.max(6, Math.min(val[2] / 15, 12)),
            data: pointsData
          }
        ]
      }

      this.chart.setOption(option, true)
    },

    handleResize() {
      this.chart?.resize()
    }
  },
  watch: {
    lines: { handler() { this.updateChart() }, deep: true }
  }
}
</script>

<style lang="scss" scoped>
.fly-lines-map {
  width: 100%;
  height: 100%;
  position: relative;
}

.chart-container { width: 100%; height: 100%; }

.map-loading {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  color: #87ceeb;
  i { font-size: 32px; }
}
</style>
```

---

## Props

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| lines | Array | (预设示例) | 飞线数据 [{fromName, toName, fromCoords, toCoords, value}] |
| center | Array | [104, 36] | 地图中心点 |
| zoom | Number | 1.2 | 缩放级别 |

---

## 数据格式

```javascript
lines: [
  {
    fromName: '北京',
    toName: '上海',
    fromCoords: [116.4551, 40.2539],
    toCoords: [121.4648, 31.2891],
    value: 95
  }
]
```
