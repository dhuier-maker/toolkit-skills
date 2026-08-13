# 数据格式化工具 (number-format.js)

> BI 大屏数字格式化规范，覆盖千分位、万/亿单位、百分比、增长率等场景。

---

## 格式化规则

| 数据量级 | 格式化方式 | 示例 |
|---------|-----------|------|
| < 10,000 | 千分位分隔 | `9,876` |
| ≥ 10,000 且 < 1亿 | ÷10000，单位"万"，1位小数 | `1.5万`、`98.6万` |
| ≥ 1亿 | ÷1亿，单位"亿"，2位小数 | `3.28亿` |
| 百分比 | 1位小数 + `%` | `85.3%` |
| 增长率 | `+`/`-` 前缀 + 1位小数 + `%` | `+12.5%`、`-3.2%` |
| 货币 | 千分位 + `¥` 前缀 | `¥1,234,567` |

---

## 工具函数

```javascript
/**
 * BI 大屏数据格式化工具
 */

// 通用数字格式化（自动选择万/亿单位）
export function formatNumber(value, options = {}) {
  const { decimals, unit, separator = true } = options
  if (value == null || isNaN(value)) return '--'

  const abs = Math.abs(value)
  const sign = value < 0 ? '-' : ''

  // 有明确单位时直接格式化
  if (unit === '万') return sign + (abs / 10000).toFixed(decimals ?? 1) + '万'
  if (unit === '亿') return sign + (abs / 100000000).toFixed(decimals ?? 2) + '亿'

  // 自动选择单位
  if (abs >= 100000000) {
    return sign + (abs / 100000000).toFixed(decimals ?? 2) + '亿'
  }
  if (abs >= 10000) {
    return sign + (abs / 10000).toFixed(decimals ?? 1) + '万'
  }

  // 小于1万：千分位分隔
  const fixed = abs % 1 === 0 ? String(abs) : abs.toFixed(decimals ?? 0)
  return sign + (separator ? Number(fixed).toLocaleString() : fixed)
}

// 百分比格式化
export function formatPercent(value, decimals = 1) {
  if (value == null || isNaN(value)) return '--'
  return value.toFixed(decimals) + '%'
}

// 增长率格式化（带正负号）
export function formatGrowth(value, decimals = 1) {
  if (value == null || isNaN(value)) return '--'
  const sign = value > 0 ? '+' : ''
  return sign + value.toFixed(decimals) + '%'
}

// 货币格式化
export function formatCurrency(value, prefix = '¥') {
  if (value == null || isNaN(value)) return '--'
  return prefix + Math.abs(value).toLocaleString()
}

// KPI 卡片数字格式化（大数字精简 + 趋势箭头）
export function formatKpi(value, options = {}) {
  const { showTrend, trendValue } = options
  let text = formatNumber(value)

  if (showTrend && trendValue != null) {
    const arrow = trendValue > 0 ? '↑' : trendValue < 0 ? '↓' : '→'
    const color = trendValue > 0 ? '#44FFAA' : trendValue < 0 ? '#FF6B6B' : '#6B7FA3'
    text += ` <span style="color:${color};font-size:12px">${arrow}${Math.abs(trendValue).toFixed(1)}%</span>`
  }

  return text
}

// 时间格式化
export function formatTime(date, format = 'YYYY年MM月DD日 HH:mm:ss') {
  const d = date instanceof Date ? date : new Date(date)
  if (isNaN(d.getTime())) return '--'

  const pad = (n) => String(n).padStart(2, '0')
  return format
    .replace('YYYY', d.getFullYear())
    .replace('MM', pad(d.getMonth() + 1))
    .replace('DD', pad(d.getDate()))
    .replace('HH', pad(d.getHours()))
    .replace('mm', pad(d.getMinutes()))
    .replace('ss', pad(d.getSeconds()))
}
```

---

## Vue 组件中使用

```javascript
import { formatNumber, formatPercent, formatGrowth, formatCurrency, formatKpi, formatTime } from '@/utils/number-format'

export default {
  data() {
    return {
      kpiData: [
        { label: '总营收', value: 123456789, trend: 12.5 },
        { label: '游客数', value: 98654, trend: -3.2 },
        { label: '好评率', value: 95.8, trend: 1.3 },
      ],
    }
  },
  methods: {
    formatNumber,
    formatPercent,
    formatGrowth,
    formatKpi,
  },
  computed: {
    currentTime() {
      return formatTime(new Date())
    },
  },
}
```

---

## 模板中使用

```vue
<!-- KPI 卡片 -->
<div class="data-value" v-html="formatKpi(item.value, { showTrend: true, trendValue: item.trend })"></div>

<!-- 简单数字 -->
<div class="data-value">{{ formatNumber(item.value) }}</div>

<!-- 百分比 -->
<div class="data-value">{{ formatPercent(item.rate) }}</div>

<!-- 增长率 -->
<div class="data-value" :style="{ color: item.trend > 0 ? '#44FFAA' : '#FF6B6B' }">
  {{ formatGrowth(item.trend) }}
</div>
```

---

## 数字颜色规范

| 场景 | 颜色 | CSS 变量 |
|------|------|---------|
| 正向增长 | `#44FFAA` | `var(--color-success)` |
| 负向增长 | `#FF6B6B` | `var(--color-danger)` |
| 高亮数据 | `#FFD93D` | `var(--color-highlight)` |
| 普通数据 | `#E0E8FF` | `var(--color-text)` |
| 辅助数据 | `#6B7FA3` | `var(--color-text-muted)` |
