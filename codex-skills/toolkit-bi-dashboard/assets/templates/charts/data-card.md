# 数据卡片组件 (DataCard.vue)

> 带图标、数值、变化率、点击交互的数据卡片，适用于业务概览。

---

```vue
<template>
  <div class="data-card" :class="{ clickable: clickable }" @click="handleClick">
    <div class="data-card-icon">{{ icon }}</div>
    <div class="data-card-content">
      <div class="data-card-title">{{ title }}</div>
      <div class="data-card-value-row">
        <span class="data-card-value">{{ formatValue(value) }}</span>
        <span class="data-card-unit">{{ unit }}</span>
      </div>
      <div class="data-card-change" :class="changeClass">
        <span v-if="change !== null && change !== undefined">
          {{ change >= 0 ? '↑' : '↓' }} {{ Math.abs(change) }}%
        </span>
        <span v-if="changeLabel">{{ changeLabel }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DataCard',
  props: {
    icon: { type: String, default: '📊' },
    title: { type: String, default: '' },
    value: { type: [Number, String], default: 0 },
    unit: { type: String, default: '' },
    change: { type: Number, default: null },
    changeLabel: { type: String, default: '' },
    clickable: { type: Boolean, default: false }
  },
  computed: {
    changeClass() {
      if (this.change === null || this.change === undefined) return ''
      return this.change >= 0 ? 'up' : 'down'
    }
  },
  methods: {
    formatValue(val) {
      return typeof val === 'number' ? val.toLocaleString() : val
    },
    handleClick() {
      if (this.clickable) this.$emit('click')
    }
  }
}
</script>

<style lang="scss" scoped>
.data-card {
  display: flex;
  align-items: flex-start;
  padding: 16px;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  transition: all 0.3s;

  &.clickable {
    cursor: pointer;
    &:hover {
      border-color: var(--primary-light);
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(52, 152, 219, 0.3);
    }
  }
}

.data-card-icon {
  font-size: 32px;
  margin-right: 12px;
  line-height: 1;
}

.data-card-content {
  flex: 1;
  min-width: 0;
}

.data-card-title {
  font-size: 14px;
  color: var(--text-secondary);
  margin-bottom: 8px;
}

.data-card-value-row {
  display: flex;
  align-items: baseline;
}

.data-card-value {
  font-size: 28px;
  font-weight: bold;
  color: var(--text-primary);
  line-height: 1.2;
}

.data-card-unit {
  font-size: 14px;
  color: var(--text-secondary);
  margin-left: 4px;
}

.data-card-change {
  font-size: 12px;
  margin-top: 8px;
  &.up { color: var(--success-color); }
  &.down { color: var(--danger-color); }
}
</style>
```

---

## 使用方式

```vue
<template>
  <div class="panel-frame">
    <div class="panel-title">业务概览</div>
    <div class="panel-content data-grid">
      <DataCard
        icon="🏨"
        title="酒店民宿"
        :value="128"
        unit="家"
        :change="12"
        clickable
        @click="handleCardClick('hotel')"
      />
      <DataCard
        icon="🍜"
        title="餐饮美食"
        :value="256"
        unit="家"
        :change="-5"
        clickable
        @click="handleCardClick('catering')"
      />
    </div>
  </div>
</template>

<script>
import DataCard from '@/components/DataCard.vue'

export default {
  components: { DataCard },
  methods: {
    handleCardClick(type) {
      console.log('卡片点击:', type)
    }
  }
}
</script>
```

## Props

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| icon | String | '📊' | 图标（emoji 或 HTML） |
| title | String | '' | 卡片标题 |
| value | Number/String | 0 | 数值 |
| unit | String | '' | 单位 |
| change | Number | null | 变化率百分比（正数上升，负数下降） |
| changeLabel | String | '' | 变化补充说明 |
| clickable | Boolean | false | 是否可点击 |
