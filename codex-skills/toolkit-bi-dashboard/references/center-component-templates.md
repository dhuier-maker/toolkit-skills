## 中间区域组件模板

> **注意**: GIS 地图组件 (ChinaMap.vue) 的完整实现见 [templates/gis-map-templates.md](../templates/gis-map-templates.md)，此处仅保留引用。

### ChinaMap.vue（中国地图 + 飞线）- 引用

```vue
<!-- 完整实现见 templates/gis-map-templates.md -->
<template>
  <ChinaMap :data="cityData" :lines="flyLines" />
</template>
```

**组件功能**：
- 中国地图渲染（ECharts-GL）
- 城市散点标注
- 飞线动画效果
- 数据驱动更新
  async mounted() {
    await this.loadMap()
    window.addEventListener('resize', this.handleResize)
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.handleResize)
    if (this.chart) this.chart.dispose()
  },
  methods: {
    async loadMap() {
      try {
        this.loading = true
        const response = await fetch('https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json')
        if (!response.ok) throw new Error(`HTTP ${response.status}`)
        const geoJson = await response.json()
        echarts.registerMap('china', geoJson)
        this.mapLoaded = true
        this.loading = false
        this.$nextTick(() => {
          this.chart = echarts.init(this.$refs.chartRef)
          this.updateChart()
        })
      } catch (err) {
        this.loading = false
        this.error = '地图加载失败: ' + err.message
      }
    },
    updateChart() {
      if (!this.chart || !this.mapLoaded) return
      
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
          zoom: 1.2,
          center: [104, 35],
          label: { show: false },
          itemStyle: {
            areaColor: '#0a2a4a',
            borderColor: '#00d4ff',
            borderWidth: 1
          },
          emphasis: {
            itemStyle: {
              areaColor: '#1a4a7a',
              borderColor: '#ffd700',
              borderWidth: 2
            },
            label: { show: true, color: '#fff' }
          }
        },
        series: [
          // 飞线层
          {
            type: 'lines',
            coordinateSystem: 'geo',
            zlevel: 2,
            effect: {
              show: true,
              period: 3,
              trailLength: 0.6,
              symbol: 'arrow',
              symbolSize: 8,
              color: '#ffd700'
            },
            lineStyle: {
              color: '#00d4ff',
              width: 2,
              curveness: 0.3,
              opacity: 0.8
            },
            data: this.lines.map(line => ({
              fromName: line.fromName,
              toName: line.toName,
              coords: line.coords
            }))
          },
          // 城市散点层
          {
            type: 'effectScatter',
            coordinateSystem: 'geo',
            zlevel: 3,
            rippleEffect: {
              brushType: 'stroke',
              scale: 4,
              period: 4
            },
            symbol: 'circle',
            symbolSize: 10,
            itemStyle: {
              color: '#ffd700',
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: true,
              position: 'right',
              formatter: '{b}',
              color: '#fff',
              fontSize: 12,
              backgroundColor: 'rgba(0, 20, 40, 0.8)',
              padding: [3, 6],
              borderRadius: 3
            },
            data: this.data.map(item => ({
              name: item.name,
              value: [item.lng || item.value[0], item.lat || item.value[1]]
            }))
          }
        ]
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
.map-container {
  width: 100%;
  height: 100%;
  position: relative;
}
.map-loading, .map-error {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #00d4ff;
  font-size: 16px;
}
.map-error { color: #ff6b6b; }
.map-chart {
  width: 100%;
  height: 100%;
}
</style>
```

### 数据格式规范

```javascript
// 城市数据
cityData: [
  { name: '北京', lng: 116.46, lat: 39.92 },
  { name: '上海', lng: 121.48, lat: 31.22 },
  // 或
  { name: '广州', value: [113.23, 23.16] }
]

// 飞线数据
flyLines: [
  { fromName: '北京', toName: '上海', coords: [[116.46, 39.92], [121.48, 31.22]] },
  { fromName: '上海', toName: '广州', coords: [[121.48, 31.22], [113.23, 23.16]] }
]
```

---

