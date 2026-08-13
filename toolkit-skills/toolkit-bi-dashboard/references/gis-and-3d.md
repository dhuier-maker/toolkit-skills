# GIS 地图可视化 & Web 3D 可视化

## GIS 地图可视化

### 支持的地图引擎

| 引擎 | 特点 | 适用场景 |
|------|------|----------|
| 高德地图 (AMap) | 国内首选，中文支持好 | 国内城市、景区 |
| 百度地图 | POI 丰富 | 商业地图应用 |
| Leaflet | 开源轻量 | 简单地图展示 |
| MapboxGL | 炫酷效果 | 国际化、高端大屏 |
| ECharts-GL | 与图表统一 | 数据可视化地图 |

### 地图组件

| 组件 | 说明 | 文件 |
|------|------|------|
| AmapView.vue | 高德地图（分类打点+SVG图标+InfoWindow弹窗） | 支持6大分类配色、脉冲动画、自定义弹窗 |
| AMapContainer.vue | 高德地图容器（基础版） | 支持 2D/3D 切换 |
| EchartsMap3D.vue | ECharts 3D 地图 | 支持中国/世界/省份地图 |
| HeatmapLayer.vue | 热力图层 | 数据密度可视化 |
| FlyLinesLayer.vue | 飞线动画层 | OD 流向可视化 |

### 地图炫酷效果

| 效果 | 说明 | 实现方式 |
|------|------|----------|
| 分类标记 | 不同分类不同颜色+SVG图标 | CATEGORY_CONFIG + 自定义marker content |
| InfoWindow弹窗 | 深色毛玻璃弹窗，分类标签+描述+图片 | isCustom:true + 自定义HTML |
| 热力图 | 数据密度热力展示 | ECharts heatmap / 高德热力图插件 |
| 飞线动画 | OD 流向动态展示 | ECharts lines + effect |
| 标记脉冲 | 地标呼吸动画 | CSS animation @keyframes amapPulse |
| 区域闪烁 | 区域高亮闪烁 | ECharts emphasis |
| 3D 建筑 | 城市建筑立体展示 | Three.js / MapboxGL |

### 使用示例

```vue
<!-- 高德地图 -->
<AMapContainer
  :center="[119.08, 25.12]"
  :zoom="11"
  :markers="mapMarkers"
  :fly-lines="flyLines"
  :heatmap-data="heatmapData"
  @marker-click="handleMarkerClick"
/>

<!-- ECharts 3D 地图 -->
<EchartsMap3D
  map-type="china"
  :data="mapData"
  :lines-data="linesData"
  :enable3-d="true"
/>
```

### 地图数据结构

```javascript
// 标记点（基础版）
mapMarkers: [
  { lng: 119.08, lat: 25.12, name: '湄洲岛', icon: '🏝️', type: 'scenic' }
]

// 标记点（分类打点版，配合 AmapView.vue）
spots: [
  { name: '妈祖祖庙', category: '文化朝圣', lat: 25.09, lng: 119.14, desc: '全球妈祖信仰发源地' }
]

// 飞线数据
flyLines: [
  { from: [119.08, 25.12], to: [118.10, 24.47], fromLabel: '湄洲岛', toLabel: '厦门', color: '#00d4ff' }
]

// 热力图数据
heatmapData: [
  [119.08, 25.12, 80], // [lng, lat, value]
]
```

### 高德地图 Key 申请

1. 访问 [高德开放平台](https://lbs.amap.com/)
2. 注册账号并创建应用
3. 获取 Web 端 Key
4. 替换组件中的 `YOUR_AMAP_KEY`

---

## Web 3D 可视化

### 技术选型

| 技术 | 特点 | 适用场景 |
|------|------|----------|
| Three.js | 最强大的 Web3D 库 | 复杂 3D 场景、自定义模型 |
| ECharts-GL | 与 ECharts 无缝集成 | 数据可视化 3D 图表 |
| WebGL | 底层 API | 高性能定制需求 |
| CSS 3D | 简单 3D 变换 | 轻量级 3D 效果 |

### 3D 组件

| 组件 | 说明 | 特性 |
|------|------|------|
| Globe3D.vue | 3D 地球 | 自动旋转、数据点、光柱、大气层光晕 |
| Bar3D.vue | 3D 柱状图 | 多维度数据展示、自动旋转 |
| Scatter3D.vue | 3D 散点图 | 三维数据分布、回归面 |
| ParticleEffect.vue | 粒子特效 | 背景粒子、鼠标交互 |
| NumberRoll.vue | 数字滚动 | 数字动态递增效果 |

### 使用示例

```vue
<!-- 3D 地球 -->
<Globe3D :data="globeData" :auto-rotate="true" :radius="80" />

<!-- 3D 柱状图 -->
<Bar3D :data="bar3DData" :x-data="['Q1', 'Q2', 'Q3', 'Q4']" :y-data="['产品A', '产品B']" />

<!-- 粒子背景 -->
<ParticleEffect :count="150" color="#00d4ff" />

<!-- 数字滚动 -->
<NumberRoll :value="12345.67" unit="万元" />
```

### 3D 数据结构

```javascript
// 地球数据点
globeData: [
  { name: '北京', lat: 39.9, lng: 116.4, value: 85 },
  { name: '上海', lat: 31.2, lng: 121.5, value: 92 }
]

// 3D 柱状图数据
bar3DData: [
  { x: 'Q1', y: '产品A', value: 80 },
  { x: 'Q2', y: '产品A', value: 95 }
]
```
