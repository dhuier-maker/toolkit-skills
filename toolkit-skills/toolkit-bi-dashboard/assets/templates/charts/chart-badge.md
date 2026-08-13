# Badge 体系模板 (ChartBadge)

> 状态标记组件，6 种状态色 × 深浅背景 + 4 种尺寸 + 地图标注点脉冲动画。

---

## 功能

- 6 种状态色（正常绿/异常红/预警黄/进行中蓝/已完成绿/已关闭灰）
- 深色/浅色背景自动适配
- 4 种尺寸（小圆点 8px / 小标签 18px / 默认 22px / 大标签 26px）
- 地图标注点脉冲动画（2s/1.5s/1s/无）

---

## Props

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| status | String | 'normal' | 状态：normal/danger/warning/info/completed/closed |
| text | String | '' | 标签文字（空则显示圆点） |
| size | String | 'default' | 尺寸：dot/small/default/large |
| pulse | Boolean | false | 是否显示脉冲动画（地图标记场景） |

---

## 状态色定义

### 深色背景（5 深色主题）

| 状态 | 色值 | CSS 变量 | 用途 |
|------|------|----------|------|
| normal | #52C41A | --badge-success | 正常/在线/健康 |
| danger | #FF4D4F | --badge-danger | 异常/离线/超限 |
| warning | #FAAD14 | --badge-warning | 预警/接近阈值 |
| info | #1890FF | --badge-info | 进行中/处理中 |
| completed | #52C41A | --badge-completed | 已完成 |
| closed | rgba(255,255,255,0.35) | --badge-closed | 已关闭/不活跃 |

### 浅色背景（lightBusiness）

| 状态 | 色值 | 用途 |
|------|------|------|
| normal | #52C41A | 正常 |
| danger | #F5222D | 异常 |
| warning | #FAAD14 | 预警 |
| info | #1890FF | 进行中 |
| completed | #52C41A | 已完成 |
| closed | rgba(0,0,0,0.25) | 已关闭 |

---

## 尺寸规范

| 尺寸 | 宽高 | 字号 | 用途 |
|------|------|------|------|
| dot | 8px | — | 纯圆点指示器 |
| small | 18px | 10px | 紧凑标签 |
| default | 22px | 11px | 标准标签 |
| large | 26px | 12px | 强调标签 |

---

## Vue 组件代码

```vue
<template>
  <span
    class="chart-badge"
    :class="[`chart-badge--${status}`, `chart-badge--${size}`, { 'chart-badge--pulse': pulse }]"
  >
    <span v-if="size !== 'dot'" class="chart-badge__text">{{ text || statusLabel }}</span>
  </span>
</template>

<script>
const STATUS_LABELS = {
  normal: '正常',
  danger: '异常',
  warning: '预警',
  info: '进行中',
  completed: '已完成',
  closed: '已关闭',
}

export default {
  name: 'ChartBadge',
  props: {
    status: { type: String, default: 'normal' },
    text: { type: String, default: '' },
    size: { type: String, default: 'default' },
    pulse: { type: Boolean, default: false },
  },
  computed: {
    statusLabel() {
      return STATUS_LABELS[this.status] || this.status
    },
  },
}
</script>
```

---

## CSS

```scss
.chart-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  white-space: nowrap;

  /* 尺寸 */
  &--dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
  }
  &--small {
    height: 18px;
    padding: 0 6px;
    .chart-badge__text { font-size: 10px; }
  }
  &--default {
    height: 22px;
    padding: 0 8px;
    .chart-badge__text { font-size: 11px; }
  }
  &--large {
    height: 26px;
    padding: 0 10px;
    border-radius: 13px;
    .chart-badge__text { font-size: 12px; }
  }

  /* 状态色 — 深色背景 */
  &--normal { background: rgba(82, 196, 26, 0.15); color: #52C41A; }
  &--danger { background: rgba(255, 77, 79, 0.15); color: #FF4D4F; }
  &--warning { background: rgba(250, 173, 20, 0.15); color: #FAAD14; }
  &--info { background: rgba(24, 144, 255, 0.15); color: #1890FF; }
  &--completed { background: rgba(82, 196, 26, 0.15); color: #52C41A; }
  &--closed { background: rgba(255, 255, 255, 0.06); color: rgba(255, 255, 255, 0.35); }

  /* 圆点模式 */
  &--dot.chart-badge--normal { background: #52C41A; }
  &--dot.chart-badge--danger { background: #FF4D4F; }
  &--dot.chart-badge--warning { background: #FAAD14; }
  &--dot.chart-badge--info { background: #1890FF; }
  &--dot.chart-badge--completed { background: #52C41A; }
  &--dot.chart-badge--closed { background: rgba(255, 255, 255, 0.35); }

  /* 脉冲动画 */
  &--pulse {
    animation: badgePulse 2s ease-out infinite;
    &.chart-badge--warning { animation-duration: 1.5s; }
    &.chart-badge--danger { animation-duration: 1s; }
    &.chart-badge--closed { animation: none; }
  }
}

@keyframes badgePulse {
  0% { box-shadow: 0 0 0 0 currentColor; opacity: 1; }
  70% { box-shadow: 0 0 0 8px transparent; opacity: 0.7; }
  100% { box-shadow: 0 0 0 0 transparent; opacity: 1; }
}

/* 浅色主题覆盖 */
:root[data-theme="light-business"] {
  .chart-badge--closed { background: rgba(0, 0, 0, 0.04); color: rgba(0, 0, 0, 0.25); }
  .chart-badge--dot.chart-badge--closed { background: rgba(0, 0, 0, 0.25); }
}
```

---

## 使用示例

```vue
<!-- 状态标签 -->
<ChartBadge status="normal" text="在线" />
<ChartBadge status="danger" text="离线" />
<ChartBadge status="warning" size="small" text="预警" />

<!-- 纯圆点 -->
<ChartBadge status="normal" size="dot" />

<!-- 地图标记脉冲 -->
<ChartBadge status="danger" size="dot" :pulse="true" />
```
