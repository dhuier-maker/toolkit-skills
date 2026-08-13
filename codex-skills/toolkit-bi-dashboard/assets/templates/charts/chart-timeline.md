# 时间轴组件模板 (ChartTimeline)

> 垂直时间轴组件，支持节点状态色、时间标签、内容卡片，6 主题适配。

---

## Props

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| data | Array | [] | 时间轴数据 |
| direction | String | 'vertical' | 方向：vertical / horizontal |

---

## 数据格式

```javascript
timelineData: [
  { time: '2026-05-20 10:00', title: '系统启动', status: 'completed', desc: '服务正常启动' },
  { time: '2026-05-20 10:05', title: '数据同步', status: 'normal', desc: '同步 1200 条记录' },
  { time: '2026-05-20 10:10', title: '告警触发', status: 'danger', desc: 'CPU 使用率超 90%' },
  { time: '2026-05-20 10:15', title: '处理中', status: 'info', desc: '自动扩容执行中' },
]
```

---

## Vue 组件代码

```vue
<template>
  <div class="chart-timeline" :class="[`chart-timeline--${direction}`]">
    <div v-for="(item, i) in data" :key="i" class="chart-timeline__item">
      <div class="chart-timeline__node">
        <span class="chart-timeline__dot" :class="[`chart-timeline__dot--${item.status || 'normal'}`]" />
        <span v-if="i < data.length - 1" class="chart-timeline__line" />
      </div>
      <div class="chart-timeline__content">
        <span class="chart-timeline__time">{{ item.time }}</span>
        <span class="chart-timeline__title">{{ item.title }}</span>
        <span v-if="item.desc" class="chart-timeline__desc">{{ item.desc }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChartTimeline',
  props: {
    data: { type: Array, default: () => [] },
    direction: { type: String, default: 'vertical' },
  },
}
</script>
```

---

## CSS

```scss
.chart-timeline {
  &--vertical { display: flex; flex-direction: column; }

  &__item {
    display: flex; gap: 12px;
    padding-bottom: 16px;

    &:last-child { padding-bottom: 0; }
  }

  &__node {
    display: flex; flex-direction: column; align-items: center;
    width: 16px; flex-shrink: 0;
  }

  &__dot {
    width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0;
    border: 2px solid; box-sizing: border-box;

    &--normal { background: #52C41A; border-color: #52C41A; }
    &--completed { background: #52C41A; border-color: #52C41A; }
    &--danger { background: #FF4D4F; border-color: #FF4D4F; }
    &--warning { background: #FAAD14; border-color: #FAAD14; }
    &--info { background: #1890FF; border-color: #1890FF; }
    &--closed { background: transparent; border-color: rgba(255,255,255,0.3); }
  }

  &__line {
    width: 2px; flex: 1;
    background: rgba(var(--color-primary-rgb), 0.15);
    margin-top: 4px;
  }

  &__content {
    display: flex; flex-direction: column; gap: 2px;
    padding-top: 0;
  }

  &__time {
    font-size: 11px; color: var(--color-text-muted);
    font-family: 'DIN Alternate', monospace;
  }

  &__title {
    font-size: 13px; color: var(--color-text); font-weight: 500;
  }

  &__desc {
    font-size: 11px; color: var(--color-text-muted);
    line-height: 1.4;
  }
}
```

---

## 使用示例

```vue
<template>
  <div class="panel-frame">
    <div class="panel-title"><span class="title-bar"></span><span>操作日志</span></div>
    <div class="panel-content" style="overflow-y: auto; max-height: 300px;">
      <ChartTimeline :data="logData" />
    </div>
  </div>
</template>
```
