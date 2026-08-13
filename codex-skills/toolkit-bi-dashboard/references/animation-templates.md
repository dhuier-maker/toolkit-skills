# 动画模板库 (animation-templates.md)

> BI 大屏常用动画代码片段，涵盖入场动画、持续动画、交互动画三类。

---

## 一、入场动画

### 1.1 面板依次淡入

```scss
// 各面板依次入场，100ms 间隔
.panel-frame {
  opacity: 0;
  transform: translateY(20px);
  animation: panelFadeIn 0.5s ease forwards;

  &:nth-child(1) { animation-delay: 0s; }
  &:nth-child(2) { animation-delay: 0.1s; }
  &:nth-child(3) { animation-delay: 0.2s; }
  &:nth-child(4) { animation-delay: 0.3s; }
  &:nth-child(5) { animation-delay: 0.4s; }
  &:nth-child(6) { animation-delay: 0.5s; }
}

@keyframes panelFadeIn {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

### 1.2 数字 countUp 滚动

```vue
<template>
  <span class="count-up">{{ displayValue }}</span>
</template>

<script>
export default {
  name: 'CountUp',
  props: {
    value: { type: Number, default: 0 },
    duration: { type: Number, default: 1000 },
    decimals: { type: Number, default: 0 },
    separator: { type: Boolean, default: true },
  },
  data() {
    return {
      displayValue: 0,
      startTime: null,
      rafId: null,
    }
  },
  watch: {
    value() { this.startCount() },
  },
  mounted() { this.startCount() },
  beforeDestroy() { if (this.rafId) cancelAnimationFrame(this.rafId) },
  methods: {
    startCount() {
      this.startTime = null
      const from = this.displayValue
      const to = this.value
      const step = (timestamp) => {
        if (!this.startTime) this.startTime = timestamp
        const progress = Math.min((timestamp - this.startTime) / this.duration, 1)
        const eased = 1 - Math.pow(1 - progress, 3) // easeOutCubic
        this.displayValue = from + (to - from) * eased
        if (progress < 1) {
          this.rafId = requestAnimationFrame(step)
        } else {
          this.displayValue = to
        }
      }
      this.rafId = requestAnimationFrame(step)
    },
  },
}
</script>
```

---

## 二、持续动画

### 2.1 呼吸光效

```scss
@keyframes breathe {
  0%, 100% {
    box-shadow: 0 0 8px var(--border-glow);
    border-color: var(--border-panel);
  }
  50% {
    box-shadow: 0 0 20px var(--border-glow);
    border-color: var(--color-primary);
  }
}

.panel-breathe {
  animation: breathe 3s ease-in-out infinite;
}
```

### 2.2 边框流光

```scss
// 边框上流动的亮点效果
@keyframes borderFlow {
  0% { background-position: 0% 50%; }
  100% { background-position: 200% 50%; }
}

.panel-flow-border {
  position: relative;
  &::before {
    content: '';
    position: absolute;
    inset: -1px;
    border-radius: inherit;
    padding: 1px;
    background: linear-gradient(
      90deg,
      transparent 0%,
      var(--color-primary) 25%,
      transparent 50%
    );
    background-size: 200% 100%;
    animation: borderFlow 3s linear infinite;
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
  }
}
```

### 2.3 扫描线

```scss
@keyframes scanLine {
  0% { top: -2px; opacity: 1; }
  100% { top: 100%; opacity: 0; }
}

.scan-line::after {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--color-primary), transparent);
  animation: scanLine 4s linear infinite;
  pointer-events: none;
}
```

### 2.4 数据点呼吸

```scss
@keyframes dotBreathe {
  0%, 100% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(1.5);
    opacity: 0.6;
  }
}

.data-dot {
  animation: dotBreathe 2s ease-in-out infinite;
}
```

---

## 三、交互动画

### 3.1 面板 hover 边框亮

```scss
.panel-frame {
  transition: border-color 0.3s, box-shadow 0.3s;
  &:hover {
    border-color: var(--color-primary);
    box-shadow: 0 0 16px var(--border-glow);
  }
}
```

### 3.2 弹窗入场动画

```scss
@keyframes popupIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.detail-panel {
  animation: popupIn 0.3s ease forwards;
}
```

### 3.3 列表项入场

```scss
@keyframes listItemIn {
  from {
    opacity: 0;
    transform: translateX(-10px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.list-item {
  animation: listItemIn 0.3s ease forwards;
}
```

---

## 动效强度控制

通过主题变量 `--animation-intensity` 控制动效开关：

| 值 | 呼吸 | 流光 | 扫描 | 粒子 | 飞线 |
|----|------|------|------|------|------|
| strong | ✓ | ✓ | ✓ | ✓ | ✓ |
| medium | ✓ | ✓ | ✗ | ✗ | ✓ |
| light | ✓ | ✗ | ✗ | ✗ | ✗ |
| minimal | ✗ | ✗ | ✗ | ✗ | ✗ |

```scss
// 条件性应用动画
@mixin animation-if($intensity, $threshold) {
  $levels: (minimal: 0, light: 1, medium: 2, strong: 3);
  @if map-get($levels, var(--animation-intensity)) >= map-get($levels, $threshold) {
    @content;
  }
}
```

---

## 四、过渡时长 Token

### 5 级时长定义

| Token | CSS 变量 | 值 | 用途 |
|-------|----------|-----|------|
| fast | `--duration-fast` | 150ms | 颜色变化、开关切换 |
| normal | `--duration-normal` | 200ms | hover 效果、面板切换 |
| slow | `--duration-slow` | 300ms | 弹窗入场、列表展开 |
| slower | `--duration-slower` | 500ms | 页面切换、复杂过渡 |
| slowest | `--duration-slowest` | 800ms | 全屏动画、数据刷新 |

### 4 种缓动曲线

| Token | CSS 变量 | 值 | 用途 |
|-------|----------|-----|------|
| default | `--ease-default` | `cubic-bezier(0.4, 0, 0.2, 1)` | 通用过渡 |
| in | `--ease-in` | `cubic-bezier(0.4, 0, 1, 1)` | 元素退出 |
| out | `--ease-out` | `cubic-bezier(0, 0, 0.2, 1)` | 元素入场 |
| bounce | `--ease-bounce` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | 弹性反馈 |

### CSS 变量定义

```css
:root {
  --duration-fast: 150ms;
  --duration-normal: 200ms;
  --duration-slow: 300ms;
  --duration-slower: 500ms;
  --duration-slowest: 800ms;

  --ease-default: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-in: cubic-bezier(0.4, 0, 1, 1);
  --ease-out: cubic-bezier(0, 0, 0.2, 1);
  --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

### 通用过渡类

```scss
.transition-colors {
  transition: color var(--duration-fast) var(--ease-default),
              background-color var(--duration-fast) var(--ease-default),
              border-color var(--duration-fast) var(--ease-default);
}

.transition-all {
  transition: all var(--duration-normal) var(--ease-default);
}

.transition-transform {
  transition: transform var(--duration-normal) var(--ease-out);
}
```

### 弹窗/面板展开预设

```scss
// 弹窗入场
.modal-enter-active {
  transition: opacity var(--duration-slow) var(--ease-out),
              transform var(--duration-slow) var(--ease-out);
}
.modal-leave-active {
  transition: opacity var(--duration-normal) var(--ease-in),
              transform var(--duration-normal) var(--ease-in);
}

// 面板展开
.panel-expand {
  transition: max-height var(--duration-slower) var(--ease-default),
              opacity var(--duration-normal) var(--ease-default);
}
```

---

## 五、地图标记脉冲动画

### 4 种状态脉冲

| 状态 | 脉冲周期 | 颜色 | 用途 |
|------|---------|------|------|
| 正常 | 2s | --badge-success (#52C41A) | 在线/正常节点 |
| 预警 | 1.5s | --badge-warning (#FAAD14) | 接近阈值 |
| 异常 | 1s | --badge-danger (#FF4D4F) | 超限/离线 |
| 静默 | 无 | --badge-closed (rgba) | 已关闭/不活跃 |

```scss
@keyframes markerPulse {
  0% {
    box-shadow: 0 0 0 0 rgba(var(--marker-color-rgb), 0.5);
  }
  70% {
    box-shadow: 0 0 0 10px rgba(var(--marker-color-rgb), 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(var(--marker-color-rgb), 0);
  }
}

.map-marker {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--marker-color);

  &--normal {
    --marker-color: #52C41A;
    --marker-color-rgb: 82, 196, 26;
    animation: markerPulse 2s ease-out infinite;
  }

  &--warning {
    --marker-color: #FAAD14;
    --marker-color-rgb: 250, 173, 20;
    animation: markerPulse 1.5s ease-out infinite;
  }

  &--danger {
    --marker-color: #FF4D4F;
    --marker-color-rgb: 255, 77, 79;
    animation: markerPulse 1s ease-out infinite;
  }

  &--silent {
    --marker-color: rgba(255, 255, 255, 0.3);
    animation: none;
  }
}
```
