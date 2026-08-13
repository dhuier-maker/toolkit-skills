# 排名列表组件 (ChartRank.vue)

> 带序号 + 进度条 + 自动滚动的排名列表，支持金银铜高亮，6主题CSS变量驱动。

---

## 组件模板

```vue
<template>
  <div class="chart-rank" ref="rankContainer">
    <div
      class="rank-list"
      :style="{ transform: `translateY(-${scrollOffset}px)`, transition: scrolling ? 'transform 0.5s ease' : 'none' }"
      @mouseenter="pauseScroll"
      @mouseleave="resumeScroll"
    >
      <div
        v-for="(item, index) in displayList"
        :key="item.name + index"
        class="rank-item"
        @click="$emit('item-click', item)"
      >
        <span :class="['rank-badge', rankClass(index)]">{{ index + 1 }}</span>
        <span class="rank-name">{{ item.name }}</span>
        <div class="rank-bar-wrapper">
          <div
            class="rank-bar"
            :style="{ width: barWidth(item.value) + '%', background: barColor(index) }"
          ></div>
        </div>
        <span class="rank-value">{{ formatValue(item.value) }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChartRank',
  emits: ['item-click'],
  props: {
    // 排名数据 [{ name, value }]
    data: { type: Array, default: () => [] },
    // 最大显示条数
    maxVisible: { type: Number, default: 5 },
    // 是否自动滚动
    autoScroll: { type: Boolean, default: true },
    // 滚动间隔(ms)
    scrollInterval: { type: Number, default: 3000 },
    // 数值单位
    unit: { type: String, default: '' },
  },
  data() {
    return {
      scrollOffset: 0,
      currentIndex: 0,
      scrolling: true,
      timer: null,
      itemHeight: 40,
    }
  },
  computed: {
    sortedData() {
      return [...this.data].sort((a, b) => b.value - a.value)
    },
    maxValue() {
      if (!this.sortedData.length) return 1
      return this.sortedData[0].value
    },
    displayList() {
      return this.sortedData
    },
  },
  watch: {
    data() {
      this.currentIndex = 0
      this.scrollOffset = 0
    },
    autoScroll(val) {
      if (val) this.startScroll()
      else this.stopScroll()
    },
  },
  mounted() {
    this.$nextTick(() => {
      const firstItem = this.$refs.rankContainer?.querySelector('.rank-item')
      if (firstItem) this.itemHeight = firstItem.offsetHeight || 40
    })
    if (this.autoScroll && this.data.length > this.maxVisible) {
      this.startScroll()
    }
  },
  beforeDestroy() {
    this.stopScroll()
  },
  methods: {
    rankClass(index) {
      if (index === 0) return 'gold'
      if (index === 1) return 'silver'
      if (index === 2) return 'bronze'
      return ''
    },
    barWidth(value) {
      return Math.max(2, (value / this.maxValue) * 100)
    },
    barColor(index) {
      const primary = getComputedStyle(document.documentElement).getPropertyValue('--color-primary').trim() || '#00D4FF'
      if (index === 0) return 'linear-gradient(90deg, #f5a623, #ffd700)'
      if (index === 1) return 'linear-gradient(90deg, #c0c0c0, #e8e8e8)'
      if (index === 2) return 'linear-gradient(90deg, #cd7f32, #e5a668)'
      return `linear-gradient(90deg, ${primary}66, ${primary})`
    },
    formatValue(value) {
      if (value >= 100000000) return (value / 100000000).toFixed(2) + '亿'
      if (value >= 10000) return (value / 10000).toFixed(1) + '万'
      return value.toLocaleString()
    },
    startScroll() {
      this.stopScroll()
      this.timer = setInterval(() => {
        if (this.currentIndex < this.data.length - this.maxVisible) {
          this.currentIndex++
          this.scrollOffset = this.currentIndex * this.itemHeight
          this.scrolling = true
        } else {
          this.currentIndex = 0
          this.scrollOffset = 0
        }
      }, this.scrollInterval)
    },
    stopScroll() {
      if (this.timer) {
        clearInterval(this.timer)
        this.timer = null
      }
    },
    pauseScroll() {
      this.stopScroll()
      this.scrolling = false
    },
    resumeScroll() {
      if (this.autoScroll && this.data.length > this.maxVisible) {
        this.startScroll()
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.chart-rank {
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.rank-list {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.rank-item {
  display: flex;
  align-items: center;
  height: 36px;
  padding: 0 8px;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.2s;

  &:hover {
    background: rgba(var(--color-primary-rgb, 0, 212, 255), 0.06);
  }
}

.rank-badge {
  width: 22px;
  height: 22px;
  line-height: 22px;
  text-align: center;
  border-radius: 4px;
  font-size: 12px;
  font-weight: bold;
  margin-right: 10px;
  background: rgba(var(--color-primary-rgb, 0, 212, 255), 0.15);
  color: var(--color-primary, #00D4FF);
  flex-shrink: 0;

  &.gold {
    background: linear-gradient(135deg, #f5a623, #ffd700);
    color: #000;
  }
  &.silver {
    background: linear-gradient(135deg, #c0c0c0, #e8e8e8);
    color: #000;
  }
  &.bronze {
    background: linear-gradient(135deg, #cd7f32, #e5a668);
    color: #000;
  }
}

.rank-name {
  font-size: 13px;
  color: var(--color-text, #E0E8FF);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  width: 80px;
  flex-shrink: 0;
}

.rank-bar-wrapper {
  flex: 1;
  height: 8px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 4px;
  margin: 0 10px;
  overflow: hidden;
}

.rank-bar {
  height: 100%;
  border-radius: 4px;
  transition: width 0.6s ease;
}

.rank-value {
  font-size: 13px;
  font-weight: 500;
  color: var(--color-highlight, #FFD93D);
  font-family: var(--font-data, 'DIN Alternate', 'Roboto-Bold', sans-serif);
  white-space: nowrap;
  min-width: 50px;
  text-align: right;
}
</style>
```

---

## Props

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| data | Array | [] | 排名数据，每项 { name, value } |
| maxVisible | Number | 5 | 最大显示条数（超出自动滚动） |
| autoScroll | Boolean | true | 是否自动滚动 |
| scrollInterval | Number | 3000 | 滚动间隔(ms) |
| unit | String | '' | 数值单位 |

---

## 数据格式

```javascript
rankData: [
  { name: '北京', value: 12856 },
  { name: '上海', value: 11234 },
  { name: '广州', value: 9876 },
  { name: '深圳', value: 8654 },
  { name: '成都', value: 7432 },
  { name: '杭州', value: 6210 },
]
```

---

## 使用示例

```vue
<!-- 基础排名列表 -->
<ChartRank :data="rankData" />

<!-- 不自动滚动 -->
<ChartRank :data="rankData" :auto-scroll="false" />

<!-- 点击事件 -->
<ChartRank :data="rankData" @item-click="handleRankClick" />
```
