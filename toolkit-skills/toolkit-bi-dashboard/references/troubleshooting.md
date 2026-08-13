## 常见问题与解决方案（踩坑记录）

### 1. 地图数据加载问题

**问题**：地图不显示，控制台无报错

**原因**：
- 地图 GeoJSON 数据加载失败（跨域、网络问题）
- 异步加载后图表初始化时机错误
- 自己编写的简化版地图数据不准确

**解决方案**：

```vue
<template>
  <div class="map-container">
    <!-- 加载状态提示 -->
    <div v-if="loading" class="map-loading">地图加载中...</div>
    <!-- 错误提示 -->
    <div v-if="error" class="map-error">{{ error }}</div>
    <!-- 地图容器 -->
    <div ref="chartRef" class="map-chart" v-show="mapLoaded"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      chart: null,
      mapLoaded: false,
      loading: true,
      error: null
    }
  },
  async mounted() {
    await this.loadMap()
  },
  methods: {
    async loadMap() {
      try {
        this.loading = true
        // 使用阿里 DataV 地图数据（稳定可靠）
        const response = await fetch('https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json')
        if (!response.ok) throw new Error(`HTTP ${response.status}`)
        const geoJson = await response.json()
        echarts.registerMap('china', geoJson)
        this.mapLoaded = true
        this.loading = false
        
        // 等待 DOM 更新后再初始化图表
        this.$nextTick(() => {
          this.chart = echarts.init(this.$refs.chartRef)
          this.updateChart()
        })
      } catch (err) {
        this.loading = false
        this.error = '地图加载失败: ' + err.message
      }
    }
  }
}
</script>
```

**推荐地图数据源**：

| 地图类型 | 数据源 URL |
|---------|-----------|
| 中国地图 | `https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json` |
| 省份地图 | `https://geo.datav.aliyun.com/areas_v3/bound/{adcode}_full.json` |
| 世界地图 | `https://geo.datav.aliyun.com/areas_v3/bound/world.json` |

### 2. 3D地球纹理加载失败

**问题**：3D地球显示为白色球体，或纹理加载报错

**原因**：
- 外部纹理资源（如 echarts-maps.github.io）网络不稳定
- 跨域问题导致纹理加载失败

**解决方案**：

**方案一：使用本地生成的纹理**（推荐）

```javascript
// 用 Canvas 生成科技感地球纹理
generateEarthTexture() {
  const canvas = document.createElement('canvas')
  const ctx = canvas.getContext('2d')
  canvas.width = 2048
  canvas.height = 1024
  
  // 绘制深海背景
  ctx.fillStyle = '#0a1f3a'
  ctx.fillRect(0, 0, canvas.width, canvas.height)
  
  // 绘制经纬网格
  ctx.strokeStyle = 'rgba(0, 212, 255, 0.1)'
  for (let i = 0; i <= 24; i++) {
    ctx.beginPath()
    ctx.moveTo((canvas.width / 24) * i, 0)
    ctx.lineTo((canvas.width / 24) * i, canvas.height)
    ctx.stroke()
  }
  
  return canvas.toDataURL('image/png')
}
```

**方案二：使用可靠的 CDN 资源**

```javascript
globe: {
  // 使用更稳定的 CDN
  baseTexture: 'https://unpkg.com/echarts-gl/map/world.topo.bathy.200401.jpg',
  // 或使用本地资源
  // baseTexture: require('@/assets/earth-texture.jpg')
}
```

### 3. scatter3D 数据点飘在天上

**问题**：3D地球上的城市点悬浮在空中，没有贴在球面上

**原因**：scatter3D 的数据格式为 `[经度, 纬度, 高度]`，第三个值被当作高度

**错误写法**：
```javascript
// 第三个值是业务数值，被误当作高度
data: scatterData.map(item => ({
  name: item.name,
  value: item.value  // [116.46, 39.92, 90] → 高度90！
}))
```

**正确写法**：
```javascript
// 散点贴在球面，高度设为0
data: scatterData.map(item => ({
  name: item.name,
  value: [item.value[0], item.value[1], 0]  // 高度为0
}))

// 如果需要光柱效果，使用 bar3D 单独配置
{
  type: 'bar3D',
  coordinateSystem: 'globe',
  data: scatterData.map(item => ({
    value: [item.value[0], item.value[1], item.value[2] / 20]  // 高度按比例
  }))
}
```

### 4. 飞线效果不可见

**问题**：飞线看不见或效果不明显

**解决方案**：增强飞线视觉效果

```javascript
{
  type: 'lines',
  coordinateSystem: 'geo',
  effect: {
    show: true,
    period: 3,           // 动画周期缩短
    trailLength: 0.6,    // 尾迹加长
    symbol: 'arrow',
    symbolSize: 8,       // 箭头加大
    color: '#ffd700'     // 鲜艳颜色
  },
  lineStyle: {
    color: '#00d4ff',
    width: 2,            // 线条加粗
    curveness: 0.3,      // 曲线弧度
    opacity: 0.8         // 提高透明度
  }
}
```

### 5. ECharts 5.x label 配置问题

**问题**：控制台警告 `textStyle hierarchy in label has been removed since 4.0`

**错误写法**（ECharts 4.x 语法）：
```javascript
label: {
  show: true,
  textStyle: {        // ❌ 已废弃
    color: '#fff',
    fontSize: 12
  }
}
```

**正确写法**（ECharts 5.x 语法）：
```javascript
label: {
  show: true,
  color: '#fff',      // ✅ 直接配置
  fontSize: 12
}
```

### 6. 图表组件销毁内存泄漏

**问题**：切换页面后图表未正确销毁，导致内存泄漏

**解决方案**：

```javascript
export default {
  data() {
    return { chart: null }
  },
  mounted() {
    this.chart = echarts.init(this.$refs.chartRef)
    window.addEventListener('resize', this.handleResize)
  },
  beforeDestroy() {
    // 必须移除事件监听
    window.removeEventListener('resize', this.handleResize)
    // 必须销毁图表实例
    if (this.chart) {
      this.chart.dispose()
      this.chart = null
    }
  }
}
```

### 7. 地图数据格式选择

**问题**：自己编写的简化版地图数据不准确，省份边界错误

**最佳实践**：

| 场景 | 推荐方案 |
|------|---------|
| 中国地图 | 使用阿里 DataV GeoJSON API |
| 省份地图 | 使用 DataV 对应 adcode 的数据 |
| 世界地图 | 使用 DataV world.json 或 ECharts 内置 |
| 自定义区域 | 使用 geojson.io 绘制后导出 |

**不要自己编写 GeoJSON**，除非是极简的示意性地图。

### 8. 中文智能引号导致 Vue 编译失败

**问题**：页面白屏，控制台报 `SyntaxError: Unexpected identifier`，Vue Router 提示 `Failed to resolve async component`

**原因**：数据中的中文智能引号 `""`（U+201C/U+201D）被 Vue 模板编译器误解析为 JavaScript 字符串分隔符，导致语法错误。常见于景点名称、描述等中文文本中。

**示例**：
```javascript
// ❌ 智能引号导致编译失败
{ name: ""飞戟洞"", desc: "内有网红打卡点"飞戟洞"" }
// Vue 编译器将 " 视为字符串开始，后面的中文变成 unexpected identifier

// ✅ 使用方括号引号替代
{ name: "「飞戟洞」", desc: "内有网红打卡点「飞戟洞」" }
```

**排查方法**：在 data() 中的字符串数据里搜索 `“` 和 `”` 字符。

**预防措施**：
- 数据录入时统一使用 `「」` 或普通引号
- 在 VS Code 中开启 Unicode 字符高亮
- 用脚本扫描：`content.match(/[""]/g)` 检测智能引号

### 9. v-if/v-else 链断裂导致空状态误显示

**问题**：列表有数据但仍显示"暂无数据"或空状态提示

**原因**：独立的 `v-if` 不在主条件链中，其配对的 `v-else` 在非预期条件下触发。

**示例**：
```vue
<!-- ❌ 两个独立的 v-if，v-else 与第二个 v-if 配对 -->
<template v-if="detailLevel === 1">列表内容</template>
<template v-if="detailLevel === 2">详情内容</template>
<div v-else>暂无数据</div>
<!-- 当 detailLevel === 1 时，第二个 v-if=false，v-else 触发，显示"暂无数据" -->

<!-- ✅ 用 v-else-if 连成一条链 -->
<template v-if="detailLevel === 1">列表内容</template>
<template v-else-if="detailLevel === 2">详情内容</template>
<div v-else-if="!detailLoading && detailList.length === 0">暂无数据</div>
```

**关键原则**：
- `v-if` / `v-else-if` / `v-else` 必须在同一层级、同一父元素下形成完整链
- 空状态的 `v-else` 必须加精确条件（如 `!loading && list.length === 0`），避免在 loading 或其他中间状态误触发

### 10. flex 子容器不滚动（scrollHeight === clientHeight）

**问题**：列表容器设置了 `overflow-y: auto` 但内容不滚动，`scrollHeight === clientHeight`

**原因**：flex 子容器默认 `min-height: auto`（等于内容高度），导致容器随内容膨胀而非溢出滚动。

**解决方案**：
```scss
/* ❌ 容器随内容膨胀，不会溢出 */
.panel-guide {
  flex: 1;
  overflow: hidden;
}
.guide-scroll {
  overflow-y: auto;
  /* min-height 默认 auto → 容器撑满内容 */
}

/* ✅ 父容器 flex column + 子容器 min-height:0 */
.panel-guide {
  flex: 1;
  min-height: 280px;
  display: flex;          /* 关键 */
  flex-direction: column; /* 关键 */
}
.guide-scroll {
  overflow-y: auto;
  min-height: 0;          /* 关键：允许收缩而非膨胀 */
  flex: 1;
}
```

**通用规则**：在 flex 布局中，任何需要内部滚动的子容器都必须设置 `min-height: 0`（纵向）或 `min-width: 0`（横向），否则 flex 项会按内容尺寸膨胀而非溢出。

### 11. 高德地图 InfoWindow 自定义样式

**问题**：使用 `isCustom: true` 的 InfoWindow 仍显示默认边框、阴影、关闭按钮

**原因**：高德地图的 InfoWindow 即使设置 `isCustom`，仍会渲染默认的 `.amap-info` 容器结构，需要通过 CSS 全局隐藏。

**解决方案**：
```scss
/* 在全局样式（非 scoped）中隐藏 InfoWindow 默认元素 */
::v-deep .amap-info {
  padding: 0;
  background: transparent;
  border: none;
  box-shadow: none;
}
::v-deep .amap-info-sharp {  /* 默认底部尖角 */
  display: none;
}
::v-deep .amap-info-content {
  padding: 0;
  background: transparent;
}
::v-deep .amap-info-close {  /* 默认关闭按钮 */
  display: none;
}
```

**自定义关闭按钮**：在 InfoWindow HTML 内容中自行添加关闭按钮，通过 JS 关闭：
```javascript
// 方式1：调用 infoWindow.close()
onclick="document.querySelector('.amap-info').remove()"

// 方式2（更可靠）：通过 Vue 组件方法
this.infoWindow.close()
```

**注意事项**：
- `.amap-info` 相关样式必须写在非 scoped 的 `<style>` 块中，或使用 `::v-deep`
- InfoWindow 的 `offset` 需要根据自定义内容高度调整，默认偏移可能不合适
- 点击地图空白区域关闭 InfoWindow：`map.on('click', () => infoWindow.close())`

### 12. 高德地图组件未注册导致图表不渲染

**问题**：引入了新组件但页面上对应区域空白，无报错

**原因**：导入了组件但忘记在 `components` 中注册

**示例**：
```javascript
import ChartLine from '@/components/ChartLine.vue'

export default {
  // ❌ 忘记注册
  components: { ChartBar, ChartPie },
  
  // ✅ 必须注册
  components: { ChartBar, ChartPie, ChartLine },
}
```

**排查方法**：在浏览器 DevTools 中检查目标区域 DOM，若为空则大概率是组件未注册。

### 13. 地图打点点击触发多个弹窗

**问题**：点击地图标记同时弹出了 InfoWindow 和侧边详情面板

**原因**：marker 的 click 事件同时触发了 `openInfoWindow()` 和 `$emit('spot-click')`，父组件监听 `spot-click` 又打开了详情面板

**解决方案**：
```javascript
// 方案1：地图打点只用 InfoWindow，不 emit 事件
marker.on('click', function() {
  self.openInfoWindow(spot, marker)
  // 不调用 self.$emit('spot-click', spot)
})

// 方案2：父组件根据来源判断是否打开面板
handleSpotClick(spot) {
  // 地图打点只由 InfoWindow 处理，不再打开侧边详情
}
```

**原则**：一个交互入口只对应一个反馈，避免同一操作触发多个弹窗。

### 14. z-index 层叠冲突导致弹窗被遮挡

**问题**：弹窗或面板被其他同级元素遮挡

**原因**：多个 fixed/absolute 定位的弹窗使用了相同 z-index

**解决方案**：
```scss
.parking-popup { z-index: 10000; }
.item-detail-panel { z-index: 10001; }  // 比列表弹窗高一层
```

**原则**：弹窗层级按交互优先级递增：地图弹窗 < 列表弹窗 < 详情弹窗 < 全局遮罩。

---

