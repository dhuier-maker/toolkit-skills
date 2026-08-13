# 分辨率适配方案 (screen-adaptation.js)

> 基于 1920×1080 设计稿的多分辨率适配方案，支持 scale 缩放和 rem+scale 混合模式。

---

## 适配策略

| 目标分辨率 | 适配策略 | scale 值 |
|-----------|---------|---------|
| 1920×1080 | 基准尺寸，1:1 还原 | 1.0 |
| 3840×2160 | scale(2) 整体缩放 | 2.0 |
| 2560×1440 | scale(1.333) | 1.333 |
| 1536×864 | scale(0.8) | 0.8 |
| 1366×768 | scale(0.712) | 0.712 |
| 非标准比例 | 宽度适配，高度滚动 | clientWidth/1920 |

---

## autoResize 方案（推荐）

```javascript
/**
 * 大屏自适应缩放
 * 基于 1920×1080 设计稿，取宽高比最小值保证不溢出
 */
export function autoResize(containerId = 'screen') {
  const designWidth = 1920
  const designHeight = 1080
  const el = document.getElementById(containerId)
  if (!el) return

  const clientWidth = document.documentElement.clientWidth
  const clientHeight = document.documentElement.clientHeight

  const scaleW = clientWidth / designWidth
  const scaleH = clientHeight / designHeight
  const scale = Math.min(scaleW, scaleH)

  el.style.width = designWidth + 'px'
  el.style.height = designHeight + 'px'
  el.style.transform = `scale(${scale})`
  el.style.transformOrigin = 'left top'

  // 居中（可选）
  const offsetX = (clientWidth - designWidth * scale) / 2
  const offsetY = (clientHeight - designHeight * scale) / 2
  el.style.marginLeft = offsetX + 'px'
  el.style.marginTop = offsetY + 'px'
}
```

### 在 App.vue 中使用

```vue
<template>
  <div id="screen" class="screen-wrapper">
    <ThemeProvider :theme="currentTheme">
      <Dashboard />
    </ThemeProvider>
  </div>
</template>

<script>
import { autoResize } from '@/utils/screen-adaptation'

export default {
  name: 'App',
  data() {
    return {
      currentTheme: 'techBlue',
    }
  },
  mounted() {
    autoResize()
    window.addEventListener('resize', this.handleResize)
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.handleResize)
  },
  methods: {
    handleResize() {
      autoResize()
    },
  },
}
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
  overflow: hidden;
  background: #000;
}

.screen-wrapper {
  position: fixed;
  top: 0;
  left: 0;
}
</style>
```

---

## rem + scale 混合方案（精细控制）

```javascript
/**
 * rem + scale 混合适配
 * 根元素 font-size 跟随视口宽度，配合 scale 处理高度
 */
export function initRemScale(containerId = 'screen') {
  const designWidth = 1920
  const designHeight = 1080
  const baseFontSize = 16 // 基准 font-size

  function adapt() {
    const clientWidth = document.documentElement.clientWidth
    const clientHeight = document.documentElement.clientHeight

    // rem 基于宽度
    const remScale = clientWidth / designWidth
    document.documentElement.style.fontSize = (baseFontSize * remScale) + 'px'

    // scale 基于高度微调
    const el = document.getElementById(containerId)
    if (!el) return

    const scaleH = clientHeight / designHeight
    if (scaleH < remScale) {
      // 高度不够，用 scale 微调
      const scale = scaleH / remScale
      el.style.transform = `scaleY(${scale})`
      el.style.transformOrigin = 'top center'
    } else {
      el.style.transform = 'none'
    }
  }

  adapt()
  return adapt
}
```

---

## 字体适配补充

| 分辨率 | 字号策略 |
|--------|---------|
| ≥2K（大屏） | 字号可上浮 10%~20% |
| 1080p（基准） | 标准 1:1 还原 |
| <1080p（小屏） | 字号不下调，靠整体缩放适配 |
| 移动端 | 不建议直接适配，做独立布局 |

---

## 全屏适配 CSS

```css
/* 全屏容器，无滚动条 */
html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: var(--bg-page, #0A0E27);
}

/* 大屏容器固定基准尺寸 */
#screen {
  width: 1920px;
  height: 1080px;
  position: fixed;
  top: 0;
  left: 0;
  transform-origin: left top;
}
```
