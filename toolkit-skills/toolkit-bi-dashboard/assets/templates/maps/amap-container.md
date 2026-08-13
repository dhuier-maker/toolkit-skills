# 高德地图组件 (AmapView.vue)

> 高德地图容器，支持分类打点、SVG图标标记、脉冲动画、自定义InfoWindow弹窗。基于 `@amap/amap-jsapi-loader` 加载。

---

## 依赖安装

```bash
npm install @amap/amap-jsapi-loader@1.0.1 --save
```

---

## 组件模板

```vue
<template>
  <div class="amap-container" ref="mapContainer"></div>
</template>

<script>
import AMapLoader from '@amap/amap-jsapi-loader'

// 分类配色配置：每个分类对应一个颜色、背景色和SVG图标
// 可根据业务需求扩展新分类
const CATEGORY_CONFIG = {
  '文化朝圣': {
    color: '#4ecdc4',
    bg: 'rgba(78,205,196,0.15)',
    svg: '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M3 21h18M6 21V10l6-7 6 7v11" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M10 21v-5h4v5" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg>'
  },
  '自然风光': {
    color: '#7ed957',
    bg: 'rgba(126,217,87,0.15)',
    svg: '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M2 20c2-2 4-2 6 0s4 2 6 0 4-2 6 0" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M12 4v10M9 7l3-3 3 3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M7 14h10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>'
  },
  '餐饮美食': {
    color: '#ffa940',
    bg: 'rgba(255,169,64,0.15)',
    svg: '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8 2h8l-1 10H9L8 2z" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M9 12c0 3 1.5 5 3 5s3-2 3-5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><path d="M18 5h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1h-1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>'
  },
  '购物商圈': {
    color: '#b37feb',
    bg: 'rgba(179,127,235,0.15)',
    svg: '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M1 1h4l2.5 13h11" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M6 5h15l-2 8H8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><circle cx="9" cy="19" r="2" stroke="currentColor" stroke-width="1.5"/><circle cx="17" cy="19" r="2" stroke="currentColor" stroke-width="1.5"/></svg>'
  },
  '演艺演出': {
    color: '#ffd700',
    bg: 'rgba(255,215,0,0.15)',
    svg: '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.8"/><path d="M9 10a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zM15 10a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z" fill="currentColor"/><path d="M8 15c1 1.5 3 2 4 2s3-.5 4-2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>'
  },
  '交通枢纽': {
    color: '#ff6b6b',
    bg: 'rgba(255,107,107,0.15)',
    svg: '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4 18c1.5-1.5 3-1.5 4.5 0s3 1.5 4.5 0 3-1.5 4.5 0 3 1.5 4.5 0" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M12 4v8M9 7l3-3 3 3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M7 12h10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>'
  },
}

const DEFAULT_CFG = {
  color: '#4ecdc4',
  bg: 'rgba(78,205,196,0.15)',
  svg: '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.8"/><path d="M12 7v5l3 2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
}

export default {
  name: 'AmapView',
  emits: ['spot-click'],
  props: {
    // 高德地图 Key（必须配置，从高德开放平台申请）
    mapKey: { type: String, default: '' },
    // 高德地图安全密钥（2.0版本必须配置）
    securityJsCode: { type: String, default: '' },
    // 地图中心点 [经度, 纬度]
    center: { type: Array, default: () => [119.128, 25.075] },
    // 缩放级别
    zoom: { type: Number, default: 13 },
    // 地图样式：amap://styles/blue（深蓝）/ amap://styles/dark（暗黑）/ amap://styles/normal（标准）
    mapStyle: { type: String, default: 'amap://styles/blue' },
    // 打点数据，每项包含 name/category/lat/lng/desc/content/image
    spots: { type: Array, default: () => [] },
    // 分类配色配置（可覆盖默认 CATEGORY_CONFIG）
    categoryConfig: { type: Object, default: null },
  },
  data() {
    return {
      map: null,
      infoWindow: null,
    }
  },
  computed: {
    mergedCategoryConfig() {
      return this.categoryConfig
        ? { ...CATEGORY_CONFIG, ...this.categoryConfig }
        : CATEGORY_CONFIG
    }
  },
  mounted() {
    this.$nextTick(() => {
      setTimeout(() => this.initMap(), 300)
    })
  },
  beforeDestroy() {
    if (this.infoWindow) {
      try { this.infoWindow.close(); } catch(e) {}
      this.infoWindow = null
    }
    if (this.map) {
      try { this.map.destroy(); } catch(e) {}
      this.map = null
    }
  },
  methods: {
    getCategoryConfig(category) {
      return this.mergedCategoryConfig[category] || DEFAULT_CFG
    },

    async initMap() {
      try {
        const key = this.mapKey || window.AMAP_KEY || ''
        const securityCode = this.securityJsCode || window.AMAP_SECURITY_CODE || ''
        if (!key) {
          console.error('请配置高德地图 Key（mapKey prop 或 window.AMAP_KEY）')
          return
        }

        window._AMapSecurityConfig = {
          securityJsCode: securityCode,
        }

        const AMap = await AMapLoader.load({
          key: key,
          version: '2.0',
          plugins: ['AMap.ToolBar'],
        })

        this.map = new AMap.Map(this.$refs.mapContainer, {
          zoom: this.zoom,
          center: this.center,
          mapStyle: this.mapStyle,
          resizeEnable: true,
          logoControl: false,
          copyrightControl: false,
          viewMode: '2D',
        })

        // 移除默认控件
        try {
          const controls = this.map.getControls()
          if (controls && controls.length) {
            controls.forEach(c => this.map.removeControl(c))
          }
        } catch(e) {}

        // 创建自定义 InfoWindow
        this.infoWindow = new AMap.InfoWindow({
          isCustom: true,
          offset: new AMap.Pixel(0, -26),
          autoMove: true,
        })

        // 点击地图空白区域关闭弹窗
        this.map.on('click', () => {
          this.infoWindow.close()
        })

        // 添加标记点
        this.spots.forEach(spot => this.addMarker(spot, AMap))
      } catch (e) {
        console.error('高德地图加载失败:', e)
      }
    },

    addMarker(spot, AMap) {
      const cfg = this.getCategoryConfig(spot.category)
      const color = cfg.color

      // SVG图标内嵌到标记HTML中（提取svg标签内部内容）
      const svgInner = cfg.svg.replace(/<svg[^>]*>/, '').replace(/<\/svg>/, '')

      const content = `
        <div class="amap-marker-custom" style="position:relative;display:flex;flex-direction:column;align-items:center;cursor:pointer;">
          <div style="width:18px;height:18px;border-radius:50%;background:radial-gradient(circle,${color}dd 0%,${color}88 60%,transparent 100%);display:flex;align-items:center;justify-content:center;position:relative;z-index:2;border:1.5px solid rgba(255,255,255,0.5);box-shadow:0 0 8px ${color}80;color:${color};">
            <svg viewBox="0 0 24 24" fill="none" style="width:11px;height:11px;">${svgInner}</svg>
          </div>
          <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:26px;height:26px;border-radius:50%;border:1.5px solid ${color};opacity:0.4;animation:amapPulse 2.5s ease-out infinite;"></div>
          <div style="margin-top:1px;font-size:10px;color:#fff;white-space:nowrap;text-shadow:0 0 4px rgba(0,0,0,1),0 0 8px rgba(0,0,0,0.8);font-family:Microsoft YaHei,sans-serif;pointer-events:none;background:linear-gradient(90deg,${color}40,transparent);padding:0 4px;border-radius:2px;">${spot.name}</div>
        </div>
      `

      const marker = new AMap.Marker({
        position: [spot.lng, spot.lat],
        content,
        offset: new AMap.Pixel(-20, -14),
      })

      this.map.add(marker)

      const self = this
      marker.on('click', function() {
        self.openInfoWindow(spot, marker)
        self.$emit('spot-click', spot)
      })
    },

    openInfoWindow(spot, marker) {
      const cfg = this.getCategoryConfig(spot.category)
      const color = cfg.color
      const bg = cfg.bg
      const svgInner = cfg.svg.replace(/<svg[^>]*>/, '').replace(/<\/svg>/, '')

      // 图片区域：有图片时展示，无图片时不占位
      const imageSection = spot.image
        ? `<div style="width:100%;height:120px;border-radius:6px 6px 0 0;overflow:hidden;background:#0a1e2d;"><img src="${spot.image}" style="width:100%;height:100%;object-fit:cover;" onerror="this.parentElement.style.display='none'" /></div>`
        : ''

      // 内容截断：超过80字截断显示
      const contentStr = spot.content
        ? spot.content.length > 80
          ? spot.content.substring(0, 80) + '...'
          : spot.content
        : ''

      const html = `
        <div style="width:320px;background:linear-gradient(135deg,rgba(10,30,45,0.97),rgba(15,40,60,0.97));border:1px solid ${color}50;border-radius:8px;overflow:hidden;box-shadow:0 8px 32px rgba(0,0,0,0.6),0 0 16px ${color}20;backdrop-filter:blur(10px);font-family:Microsoft YaHei,sans-serif;">
          <div style="position:relative;">
            ${imageSection}
            <div style="position:absolute;top:8px;right:8px;z-index:3;width:24px;height:24px;border-radius:50%;background:rgba(0,0,0,0.5);border:1px solid rgba(255,255,255,0.2);cursor:pointer;display:flex;align-items:center;justify-content:center;color:#fff;font-size:14px;line-height:1;" onclick="document.querySelector('.amap-info').remove()">×</div>
            <div style="padding:${spot.image ? '12px 16px' : '16px 16px 8px'};">
              <div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;">
                <span style="display:inline-flex;align-items:center;gap:4px;padding:2px 10px;border-radius:12px;font-size:11px;color:${color};background:${bg};border:1px solid ${color}30;">
                  <svg viewBox="0 0 24 24" fill="none" style="width:14px;height:14px;">${svgInner}</svg>
                  ${spot.category}
                </span>
              </div>
              <div style="font-size:16px;font-weight:bold;color:#fff;margin-bottom:6px;text-shadow:0 0 8px ${color}40;">${spot.name}</div>
              <div style="font-size:12px;color:rgba(255,255,255,0.75);line-height:1.6;">${spot.desc}</div>
            </div>
          </div>
          ${contentStr ? `
          <div style="padding:0 16px 12px;">
            <div style="font-size:11px;color:rgba(255,255,255,0.55);line-height:1.7;border-top:1px solid rgba(255,255,255,0.08);padding-top:10px;">${contentStr}</div>
          </div>
          ` : ''}
          <div style="height:3px;background:linear-gradient(90deg,transparent,${color}80,transparent);"></div>
        </div>
      `

      this.infoWindow.setContent(html)
      this.infoWindow.open(this.map, marker.getPosition())
    },
  }
}
</script>

<style lang="scss" scoped>
.amap-container {
  width: 100%;
  height: 100%;
  overflow: hidden;
}

/* 隐藏高德地图默认元素 */
::v-deep .amap-logo,
::v-deep .amap-copyright {
  display: none !important;
}

::v-deep .amap-toolbar {
  display: none !important;
}

::v-deep .amap-map {
  background: #0a1e2d !important;
}

/* InfoWindow 自定义样式：隐藏默认边框/阴影/关闭按钮 */
::v-deep .amap-info {
  padding: 0;
  background: transparent;
  border: none;
  box-shadow: none;
}

::v-deep .amap-info-sharp {
  display: none;
}

::v-deep .amap-info-content {
  padding: 0;
  background: transparent;
}

::v-deep .amap-info-close {
  display: none;
}
</style>

/* 脉冲动画（非scoped，全局生效） */
<style>
@keyframes amapPulse {
  0% { transform: translate(-50%, -50%) scale(0.8); opacity: 0.5; }
  100% { transform: translate(-50%, -50%) scale(2.2); opacity: 0; }
}
</style>
```

---

## Props

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| mapKey | String | '' | 高德地图 Key（必须，从高德开放平台申请）|
| securityJsCode | String | '' | 高德地图安全密钥（2.0版本必须）|
| center | Array | [119.128, 25.075] | 地图中心点 [经度, 纬度] |
| zoom | Number | 13 | 缩放级别 |
| mapStyle | String | 'amap://styles/blue' | 地图样式：blue/dark/normal |
| spots | Array | [] | 打点数据（见下方数据格式）|
| categoryConfig | Object | null | 自定义分类配色（覆盖默认配置）|

---

## 数据格式

### 打点数据（spots）

```javascript
spots: [
  {
    name: '妈祖祖庙',           // 景点名称（必填）
    category: '文化朝圣',       // 分类（必填，对应 CATEGORY_CONFIG 的 key）
    lat: 25.090098,            // 纬度（必填）
    lng: 119.145495,           // 经度（必填）
    desc: '全球妈祖信仰发源地', // 简短描述（必填）
    content: '详细内容...',     // 详细内容（可选，InfoWindow中截断显示）
    image: ''                  // 图片URL（可选，空值时不占位）
  }
]
```

### 分类配色（categoryConfig）

```javascript
// 默认6个分类，可通过 prop 覆盖或新增
categoryConfig: {
  '文化朝圣': { color: '#4ecdc4', bg: 'rgba(78,205,196,0.15)', svg: '<svg>...' },
  '自然风光': { color: '#7ed957', bg: 'rgba(126,217,87,0.15)', svg: '<svg>...' },
  '餐饮美食': { color: '#ffa940', bg: 'rgba(255,169,64,0.15)', svg: '<svg>...' },
  '购物商圈': { color: '#b37feb', bg: 'rgba(179,127,235,0.15)', svg: '<svg>...' },
  '演艺演出': { color: '#ffd700', bg: 'rgba(255,215,0,0.15)', svg: '<svg>...' },
  '交通枢纽': { color: '#ff6b6b', bg: 'rgba(255,107,107,0.15)', svg: '<svg>...' },
  // 可新增自定义分类
  '医疗健康': { color: '#36cfc9', bg: 'rgba(54,207,201,0.15)', svg: '<svg>...' },
}
```

每个分类配置包含：
- `color`：主色（标记圆点、InfoWindow边框、标签文字）
- `bg`：背景色（标签背景、标记文字底色）
- `svg`：SVG图标字符串（标记内和InfoWindow标签内使用）

---

## 使用方法

### 1. 申请高德地图 Key

1. 访问 [高德开放平台](https://lbs.amap.com/)
2. 注册账号并创建应用
3. 获取 Web 端 JS API Key 和安全密钥

### 2. 基础使用

```vue
<AmapView
  map-key="YOUR_AMAP_KEY"
  security-js-code="YOUR_AMAP_SECURITY_CODE"
  :center="[119.128, 25.075]"
  :zoom="13"
  :spots="mapSpots"
  @spot-click="handleSpotClick"
/>
```

### 3. 全局配置 Key（替代 prop）

```javascript
// main.js 中全局配置
window.AMAP_KEY = 'YOUR_AMAP_KEY'
window.AMAP_SECURITY_CODE = 'YOUR_AMAP_SECURITY_CODE'
```

### 4. 自定义分类配色

```vue
<AmapView
  map-key="YOUR_AMAP_KEY"
  security-js-code="YOUR_AMAP_SECURITY_CODE"
  :spots="mapSpots"
  :category-config="customCategoryConfig"
/>
```

```javascript
customCategoryConfig: {
  '景区': { color: '#4ecdc4', bg: 'rgba(78,205,196,0.15)', svg: '<svg viewBox="0 0 24 24">...</svg>' },
  '酒店': { color: '#ffa940', bg: 'rgba(255,169,64,0.15)', svg: '<svg viewBox="0 0 24 24">...</svg>' },
}
```

---

## 标记效果说明

| 效果 | 实现 | 说明 |
|------|------|------|
| 分类配色 | CATEGORY_CONFIG | 每个分类独立颜色 |
| SVG图标标记 | 内嵌SVG到marker content | 18px圆点+11pxSVG图标 |
| 脉冲光圈 | CSS @keyframes amapPulse | 26px扩散圈，2.5s循环 |
| 标签底色 | linear-gradient渐变 | 分类色40%→透明 |
| InfoWindow弹窗 | isCustom:true | 深色毛玻璃320px宽 |
| 分类标签 | SVG+文字 | 圆角标签，分类色边框 |
| 图片展示 | spot.image | 有值时展示120px图，空值不占位 |
| 内容截断 | 80字截断 | 防止弹窗过长 |

---

## 注意事项

1. **Key 必须配置**：`mapKey` 和 `securityJsCode` 必须通过 prop 或 `window.AMAP_KEY` / `window.AMAP_SECURITY_CODE` 提供，否则地图无法加载
2. **安全密钥**：高德地图 2.0 版本必须配置 `securityJsCode`，否则会报安全验证错误
3. **中文智能引号**：spots 数据中的中文文本不要使用 `""`（智能引号），会导致 Vue 编译失败，使用 `「」` 替代
4. **容器高度**：`.amap-container` 的父元素必须有明确高度
5. **InfoWindow 样式**：`.amap-info` 相关样式必须写在非 scoped 的 `<style>` 块中或使用 `::v-deep`
6. **地图样式**：大屏场景推荐 `amap://styles/blue`（深蓝）或 `amap://styles/dark`（暗黑）
7. **SVG图标格式**：categoryConfig 中的 svg 字段必须是完整的 `<svg>` 标签字符串，包含 `viewBox="0 0 24 24"` 和 `fill="none"`