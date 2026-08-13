# 中国地图组件 (ChinaMap.vue)

> 基于 ECharts 5.x，中国地图 + 飞线 + 散点，多 CDN 兜底加载。

---

```vue
<template>
  <div class="china-map">
    <div v-if="loading" class="map-loading">
      <i class="el-icon-loading"></i>
      <span>地图加载中...</span>
    </div>
    <div v-if="error" class="map-error">
      <i class="el-icon-warning"></i>
      <span>{{ error }}</span>
    </div>
    <div ref="chartRef" class="chart-container" :style="{ opacity: loading ? 0 : 1 }"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts'

export default {
  name: 'ChinaMap',
  props: {
    scatterData: { type: Array, default: () => [] },
    linesData: { type: Array, default: () => [] },
    center: { type: Array, default: () => [104, 36] },
    zoom: { type: Number, default: 1.2 },
    showLines: { type: Boolean, default: true },
    showScatter: { type: Boolean, default: true }
  },
  data() {
    return { chart: null, loading: true, error: null }
  },
  async mounted() {
    await this.initChart()
  },
  beforeDestroy() {
    if (this.chart) { this.chart.dispose(); this.chart = null }
    window.removeEventListener('resize', this.handleResize)
  },
  methods: {
    async initChart() {
      try {
        this.loading = true
        this.error = null
        const chinaGeoJson = await this.loadChinaMap()
        if (!chinaGeoJson) throw new Error('地图数据加载失败')
        echarts.registerMap('china', chinaGeoJson)
        this.chart = echarts.init(this.$refs.chartRef)
        this.updateChart()
        window.addEventListener('resize', this.handleResize)
        this.loading = false
      } catch (e) {
        console.error('地图初始化失败:', e)
        this.error = e.message || '地图加载失败'
        this.loading = false
      }
    },

    async loadChinaMap() {
      const urls = [
        'https://fastly.jsdelivr.net/npm/@jiaminghi/china-map-geojson@1.0.0/china.json',
        'https://cdn.jsdelivr.net/npm/@jiaminghi/china-map-geojson@1.0.0/china.json',
        'https://unpkg.com/@jiaminghi/china-map-geojson@1.0.0/china.json'
      ]
      for (const url of urls) {
        try {
          const response = await fetch(url)
          if (response.ok) return await response.json()
        } catch (e) {
          console.warn(`地图数据源 ${url} 加载失败:`, e)
        }
      }
      return null
    },

    updateChart() {
      if (!this.chart) return

      const series = []

      // 地图基础层
      series.push({
        type: 'map',
        map: 'china',
        roam: true,
        zoom: this.zoom,
        center: this.center,
        itemStyle: {
          areaColor: '#0d1b2a',
          borderColor: '#00d4ff',
          borderWidth: 1
        },
        emphasis: {
          itemStyle: { areaColor: '#1e3a5f', borderColor: '#00d4ff', borderWidth: 2 },
          label: { show: true, color: '#fff' }
        },
        label: { show: false }
      })

      // 散点层
      if (this.showScatter && this.scatterData.length > 0) {
        series.push({
          type: 'effectScatter',
          coordinateSystem: 'geo',
          data: this.scatterData.map(item => ({
            name: item.name,
            value: [item.lng, item.lat, item.value || 0],
            itemStyle: { color: item.color || '#00d4ff' }
          })),
          symbolSize: (val) => Math.max(8, Math.min(val[2] / 10, 20)),
          rippleEffect: { period: 4, brushType: 'stroke', scale: 4 },
          label: {
            show: true,
            position: 'right',
            formatter: '{b}',
            fontSize: 11,
            color: '#fff'
          }
        })
      }

      // 飞线层
      if (this.showLines && this.linesData.length > 0) {
        series.push({
          type: 'lines',
          coordinateSystem: 'geo',
          zlevel: 2,
          effect: {
            show: true, period: 4, trailLength: 0.6,
            symbol: 'arrow', symbolSize: 8, color: '#ffd700'
          },
          lineStyle: {
            color: '#00d4ff', width: 1.5, curveness: 0.3, opacity: 0.7
          },
          data: this.linesData.map(line => ({
            fromName: line.fromName, toName: line.toName,
            coords: [line.fromCoords, line.toCoords],
            value: line.value
          }))
        })

        // 飞线端点
        const pointsData = []
        this.linesData.forEach(line => {
          pointsData.push({ name: line.fromName, value: [...line.fromCoords, line.value || 0], itemStyle: { color: '#00d4ff' } })
          pointsData.push({ name: line.toName, value: [...line.toCoords, line.value || 0], itemStyle: { color: '#ffd700' } })
        })

        series.push({
          type: 'effectScatter',
          coordinateSystem: 'geo',
          zlevel: 2,
          rippleEffect: { period: 4, brushType: 'stroke', scale: 3 },
          symbol: 'circle',
          symbolSize: 6,
          data: pointsData
        })
      }

      const option = {
        backgroundColor: 'transparent',
        tooltip: {
          trigger: 'item',
          backgroundColor: 'rgba(13, 27, 42, 0.9)',
          borderColor: 'rgba(0, 212, 255, 0.3)',
          textStyle: { color: '#fff' }
        },
        geo: {
          map: 'china',
          roam: true,
          zoom: this.zoom,
          center: this.center,
          itemStyle: { areaColor: '#0d1b2a', borderColor: '#00d4ff', borderWidth: 1 },
          emphasis: { itemStyle: { areaColor: '#1e3a5f' } }
        },
        series
      }

      this.chart.setOption(option, true)
    },

    handleResize() {
      if (this.chart) this.chart.resize()
    }
  },
  watch: {
    scatterData() { this.updateChart() },
    linesData() { this.updateChart() }
  }
}
</script>

<style lang="scss" scoped>
.china-map {
  width: 100%;
  height: 100%;
  position: relative;
}

.chart-container {
  width: 100%;
  height: 100%;
  transition: opacity 0.3s;
}

.map-loading, .map-error {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  color: #87ceeb;
  font-size: 14px;
  i { font-size: 32px; }
}

.map-error { color: #ff6b6b; }
</style>
```

---

## Props

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| scatterData | Array | [] | 散点数据 [{name, value, lng, lat, color}] |
| linesData | Array | [] | 飞线数据 [{fromName, toName, fromCoords, toCoords, value}] |
| center | Array | [104, 36] | 地图中心点 |
| zoom | Number | 1.2 | 缩放级别 |
| showLines | Boolean | true | 是否显示飞线 |
| showScatter | Boolean | true | 是否显示散点 |

---

## 数据格式

```javascript
// 散点数据
scatterData: [
  { name: '北京', lng: 116.405, lat: 39.905, value: 100, color: '#00d4ff' },
  { name: '上海', lng: 121.474, lat: 31.230, value: 90 }
]

// 飞线数据
linesData: [
  { fromName: '北京', toName: '上海', fromCoords: [116.405, 39.905], toCoords: [121.474, 31.230], value: 95 }
]
```
