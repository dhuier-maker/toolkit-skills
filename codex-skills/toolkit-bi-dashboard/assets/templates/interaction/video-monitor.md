# 视频监控面板模板 (VideoMonitor)

> 视频监控展示组件，含视频占位、状态指示、标题栏，6 主题适配。

---

## Props

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| title | String | '' | 监控点名称 |
| status | String | 'online' | 状态：online/offline/recording |
| src | String | '' | 视频流地址（RTSP/HLS/FLV） |
| poster | String | '' | 封面图 |

---

## Vue 组件代码

```vue
<template>
  <div class="video-monitor" :class="[`video-monitor--${status}`]">
    <div class="video-monitor__header">
      <span class="video-monitor__title">{{ title }}</span>
      <ChartBadge :status="badgeStatus" size="small" :text="badgeText" />
    </div>
    <div class="video-monitor__viewport">
      <video v-if="src" :src="src" :poster="poster" muted autoplay class="video-monitor__video" />
      <div v-else class="video-monitor__placeholder">
        <svg viewBox="0 0 48 48" width="48" height="48">
          <rect x="4" y="8" width="40" height="28" rx="3" fill="none" stroke="currentColor" stroke-width="2" />
          <polygon points="18,17 18,27 30,22" fill="currentColor" />
          <line x1="16" y1="40" x2="32" y2="40" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
        </svg>
      </div>
      <div v-if="status === 'recording'" class="video-monitor__rec">
        <span class="video-monitor__rec-dot" />REC
      </div>
    </div>
  </div>
</template>

<script>
import ChartBadge from './ChartBadge.vue'

export default {
  name: 'VideoMonitor',
  components: { ChartBadge },
  props: {
    title: { type: String, default: '' },
    status: { type: String, default: 'online' },
    src: { type: String, default: '' },
    poster: { type: String, default: '' },
  },
  computed: {
    badgeStatus() {
      return { online: 'normal', offline: 'danger', recording: 'warning' }[this.status] || 'normal'
    },
    badgeText() {
      return { online: '在线', offline: '离线', recording: '录制中' }[this.status] || ''
    },
  },
}
</script>
```

---

## CSS

```scss
.video-monitor {
  border-radius: 6px;
  overflow: hidden;
  border: 1px solid rgba(var(--color-primary-rgb), 0.15);
  background: var(--bg-panel);

  &__header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 6px 10px;
    background: rgba(var(--color-primary-rgb), 0.06);
  }

  &__title {
    font-size: 12px; color: var(--color-text);
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  }

  &__viewport {
    position: relative;
    aspect-ratio: 16 / 9;
    background: rgba(0, 0, 0, 0.3);
  }

  &__video {
    width: 100%; height: 100%; object-fit: cover;
  }

  &__placeholder {
    position: absolute; inset: 0;
    display: flex; align-items: center; justify-content: center;
    color: var(--color-text-muted); opacity: 0.4;
  }

  &__rec {
    position: absolute; top: 8px; right: 8px;
    display: flex; align-items: center; gap: 4px;
    padding: 2px 8px; border-radius: 4px;
    background: rgba(255, 77, 79, 0.8);
    color: #fff; font-size: 10px; font-weight: bold;
  }

  &__rec-dot {
    width: 6px; height: 6px; border-radius: 50%;
    background: #fff;
    animation: recBlink 1s ease-in-out infinite;
  }

  /* 离线状态 */
  &--offline &__viewport { opacity: 0.5; }
}

@keyframes recBlink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.3; }
}
```

---

## 使用示例

```vue
<!-- 4 宫格监控 -->
<div class="monitor-grid">
  <VideoMonitor
    v-for="cam in cameras"
    :key="cam.id"
    :title="cam.name"
    :status="cam.status"
    :src="cam.streamUrl"
  />
</div>

<style>
.monitor-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
}
</style>
```
