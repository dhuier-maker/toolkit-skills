# UI 状态模板（加载/空态/错误态）

> BI 大屏 3 种异常态模板：加载态、空态、错误态。每种含完整 CSS + Vue 组件代码，6 主题配色适配。

---

## 一、加载态

### 视觉规范

- 旋转圆环 + 主题色光点
- 半透明遮罩覆盖面板内容区
- 15s 显示"加载较慢"提示，60s 强制停止显示错误态

### CSS

```scss
.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 120px;
  gap: var(--space-3);

  &__spinner {
    width: 32px;
    height: 32px;
    border: 3px solid rgba(var(--color-primary-rgb), 0.15);
    border-top-color: var(--color-primary);
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
  }

  &__text {
    color: var(--color-text-muted);
    font-size: 12px;
  }

  &__slow {
    color: var(--color-warning);
    font-size: 11px;
    margin-top: calc(var(--space-1) * -1);
  }
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

### Vue 组件

```vue
<template>
  <div class="loading-state">
    <div class="loading-state__spinner"></div>
    <span class="loading-state__text">加载中…</span>
    <span v-if="isSlow" class="loading-state__slow">加载较慢，请稍候</span>
  </div>
</template>

<script>
export default {
  name: 'LoadingState',
  data() {
    return { isSlow: false, slowTimer: null }
  },
  mounted() {
    this.slowTimer = setTimeout(() => { this.isSlow = true }, 15000)
  },
  beforeDestroy() {
    clearTimeout(this.slowTimer)
  }
}
</script>
```

### 使用方式

```vue
<div v-if="loading" class="panel-content">
  <LoadingState />
</div>
<div v-else-if="error" class="panel-content">
  <ErrorState :message="errorMessage" @retry="fetchData" />
</div>
<div v-else-if="list.length === 0" class="panel-content">
  <EmptyState title="暂无数据" description="当前没有相关数据" />
</div>
<div v-else class="panel-content">
  <!-- 正常内容 -->
</div>
```

---

## 二、空态

### 视觉规范

- 64px 空数据插图（SVG 内联）
- 标题 + 说明文字
- 可选操作按钮

### CSS

```scss
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 150px;
  gap: var(--space-2);
  padding: var(--space-5);

  &__icon {
    width: 64px;
    height: 64px;
    opacity: 0.4;
  }

  &__title {
    color: var(--color-text);
    font-size: 14px;
    font-weight: 500;
  }

  &__description {
    color: var(--color-text-muted);
    font-size: 12px;
    text-align: center;
    max-width: 200px;
  }

  &__action {
    margin-top: var(--space-2);
    padding: 4px 16px;
    background: var(--btn-primary-bg);
    color: var(--btn-primary-text);
    border: none;
    border-radius: 4px;
    font-size: 12px;
    cursor: pointer;
  }
}
```

### Vue 组件

```vue
<template>
  <div class="empty-state">
    <svg class="empty-state__icon" viewBox="0 0 64 64" fill="none">
      <rect x="8" y="12" width="48" height="40" rx="4" :stroke="mutedColor" stroke-width="2" stroke-dasharray="4 2" />
      <line x1="20" y1="28" x2="44" y2="28" :stroke="mutedColor" stroke-width="2" stroke-linecap="round" />
      <line x1="24" y1="36" x2="40" y2="36" :stroke="mutedColor" stroke-width="2" stroke-linecap="round" />
    </svg>
    <span class="empty-state__title">{{ title }}</span>
    <span v-if="description" class="empty-state__description">{{ description }}</span>
    <button v-if="actionText" class="empty-state__action" @click="$emit('action')">{{ actionText }}</button>
  </div>
</template>

<script>
export default {
  name: 'EmptyState',
  props: {
    title: { type: String, default: '暂无数据' },
    description: { type: String, default: '' },
    actionText: { type: String, default: '' },
  },
  computed: {
    mutedColor() {
      return getComputedStyle(document.documentElement).getPropertyValue('--color-text-muted').trim() || '#6B7FA3'
    }
  }
}
</script>
```

### 空态 3 类型

| 类型 | 标题 | 说明 | 操作 |
|------|------|------|------|
| 首次空 | "暂无数据" | "当前没有相关数据" | 主CTA按钮 |
| 无结果 | "未找到结果" | "未找到「{query}」相关数据" | "清除筛选" |
| 已清空 | "列表已清空" | — | — |

---

## 三、错误态

### 视觉规范

- 48px 感叹号图标
- 红色/警告色错误描述
- 次要按钮"重试"

### CSS

```scss
.error-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 150px;
  gap: var(--space-2);
  padding: var(--space-5);

  &__icon {
    width: 48px;
    height: 48px;

    circle {
      fill: rgba(255, 77, 79, 0.1);
      stroke: var(--color-danger);
      stroke-width: 2;
    }

    text {
      fill: var(--color-danger);
      font-size: 24px;
      font-weight: bold;
      text-anchor: middle;
      dominant-baseline: central;
    }
  }

  &__message {
    color: var(--color-danger);
    font-size: 13px;
    font-weight: 500;
  }

  &__reason {
    color: var(--color-text-muted);
    font-size: 12px;
  }

  &__retry {
    margin-top: var(--space-2);
    padding: 4px 16px;
    background: transparent;
    color: var(--color-primary);
    border: 1px solid var(--btn-secondary-border);
    border-radius: 4px;
    font-size: 12px;
    cursor: pointer;
    transition: all var(--duration-fast) var(--ease-default);

    &:hover {
      background: var(--btn-hover-overlay);
    }
  }
}
```

### Vue 组件

```vue
<template>
  <div class="error-state">
    <svg class="error-state__icon" viewBox="0 0 48 48">
      <circle cx="24" cy="24" r="20" />
      <text x="24" y="24">!</text>
    </svg>
    <span class="error-state__message">{{ message || '数据加载失败' }}</span>
    <span v-if="reason" class="error-state__reason">{{ reason }}</span>
    <button class="error-state__retry" @click="$emit('retry')">重试</button>
  </div>
</template>

<script>
export default {
  name: 'ErrorState',
  props: {
    message: { type: String, default: '数据加载失败' },
    reason: { type: String, default: '' },
  }
}
</script>
```

### 错误态三要素

| 要素 | 示例 | 说明 |
|------|------|------|
| 发生了什么 | "数据加载失败" | 不是"出错了" |
| 为什么（如可知） | "网络连接异常" | 可选 |
| 用户能做什么 | "重试"按钮 | 必须有操作 |

---

## 四、6 主题状态色差异

| 主题 | 加载光点色 | 空态图标色 | 错误警告色 | 重试按钮色 |
|------|----------|----------|----------|----------|
| techBlue | #00D4FF | #6B7FA3 | #FF6B6B | #00D4FF |
| ecoGreen | #00E5C3 | #5A8A7A | #FF6B6B | #00E5C3 |
| partyRed | #FFD700 | #8A6A6A | #FF4D4F | #FFD700 |
| warmOrange | #FF8C42 | #8A7A6A | #FF6B6B | #FF8C42 |
| deepPurple | #A855F7 | #7A6A8A | #FF6B6B | #A855F7 |
| lightBusiness | #1890FF | #8C8C8C | #FF4D4F | #1890FF |

> 所有状态组件均通过 CSS 变量自动适配当前主题，无需手动切换。
