# 图表配置规范

> ECharts 5.x 图表统一配置规范：坐标轴、图例、标签溢出、6 主题配色数组。

---

## 一、坐标轴规范

### 轴线

| 属性 | 值 | 说明 |
|------|-----|------|
| 轴线颜色 | `var(--chart-axis-line)` | 默认 `rgba(primary, 0.3)` |
| 轴线粗细 | 1 | 统一 1px |
| 轴线样式 | `'solid'` | X 轴实线 |
| Y 轴轴线 | 隐藏 | `show: false` |

### 刻度标签

| 属性 | 值 |
|------|-----|
| 颜色 | `var(--color-text-muted)` |
| 字号 | 11 |
| 旋转 | 0（超出时旋转 15°） |

### 分割线

| 属性 | 值 |
|------|-----|
| 显示 | 仅 Y 轴 `splitLine: { show: true }` |
| 颜色 | `var(--chart-split-line)` → `rgba(primary, 0.08)` |
| 样式 | `type: 'dashed'` |
| X 轴分割线 | 隐藏 `splitLine: { show: false }` |

### ECharts 配置代码

```javascript
// 坐标轴通用配置
const axisConfig = {
  xAxis: {
    type: 'category',
    axisLine: {
      lineStyle: { color: getComputedStyle(document.documentElement).getPropertyValue('--chart-axis-line').trim() || 'rgba(0,212,255,0.3)', width: 1 }
    },
    axisTick: { show: false },
    axisLabel: {
      color: getComputedStyle(document.documentElement).getPropertyValue('--color-text-muted').trim() || '#6B7FA3',
      fontSize: 11,
      rotate: 0
    },
    splitLine: { show: false }
  },
  yAxis: {
    type: 'value',
    axisLine: { show: false },
    axisTick: { show: false },
    axisLabel: {
      color: getComputedStyle(document.documentElement).getPropertyValue('--color-text-muted').trim() || '#6B7FA3',
      fontSize: 11
    },
    splitLine: {
      show: true,
      lineStyle: { color: getComputedStyle(document.documentElement).getPropertyValue('--chart-split-line').trim() || 'rgba(0,212,255,0.08)', type: 'dashed' }
    }
  }
}
```

---

## 二、图例规范

| 属性 | 值 | 说明 |
|------|-----|------|
| 位置 | `top: 10, right: 10` | 右上角 |
| 图标 | `'circle'` | 圆形图标 |
| 图标尺寸 | 8 | `itemWidth: 8, itemHeight: 8` |
| 间距 | 12 | `itemGap: 12` |
| 文字颜色 | `var(--color-text-muted)` | |
| 文字字号 | 11 | |

```javascript
legend: {
  show: true,
  top: 10,
  right: 10,
  icon: 'circle',
  itemWidth: 8,
  itemHeight: 8,
  itemGap: 12,
  textStyle: {
    color: getComputedStyle(document.documentElement).getPropertyValue('--color-text-muted').trim() || '#6B7FA3',
    fontSize: 11
  }
}
```

---

## 三、标签溢出截断策略

| 场景 | 策略 | 实现 |
|------|------|------|
| X 轴标签过长 | 旋转 15° + 截断 | `axisLabel: { rotate: 15, formatter: v => v.length > 6 ? v.slice(0, 6) + '…' : v }` |
| 饼图标签过长 | 引导线 + 截断 | `label: { formatter: params => params.name.length > 4 ? params.name.slice(0, 4) + '…' : params.name }` |
| Tooltip 标题过长 | 换行 | `tooltip: { formatter: params => { const name = params.name; return name.length > 10 ? name.match(/.{1,10}/g).join('<br/>') : name; } }` |
| 数值标签 | 超大数万/亿 | 使用 `formatNumber()` 工具函数 |

---

## 四、6 主题图表配色数组

```javascript
const themeChartPalettes = {
  techBlue: {
    colors: ['#00D4FF', '#0088FF', '#FF6B6B', '#FFD93D', '#44FFAA', '#A855F7', '#FF8C42', '#FF69B4'],
    areaGradient: ['rgba(0,212,255,0.35)', 'rgba(0,212,255,0.02)'],
    mapAreaColor: '#0C2A5A',
    mapBorderColor: 'rgba(0,212,255,0.4)',
    mapEmphasisArea: '#1A4A8A',
    mapEmphasisBorder: '#00D4FF'
  },
  ecoGreen: {
    colors: ['#00E5C3', '#00FF88', '#FF6B6B', '#FFD93D', '#44CCFF', '#A855F7', '#FF8C42', '#FF69B4'],
    areaGradient: ['rgba(0,229,195,0.35)', 'rgba(0,229,195,0.02)'],
    mapAreaColor: '#0C2A2A',
    mapBorderColor: 'rgba(0,229,195,0.4)',
    mapEmphasisArea: '#1A4A4A',
    mapEmphasisBorder: '#00E5C3'
  },
  partyRed: {
    colors: ['#FF4D4F', '#FFD700', '#FF8C00', '#52C41A', '#1890FF', '#A855F7', '#FF69B4', '#44CCFF'],
    areaGradient: ['rgba(255,77,79,0.35)', 'rgba(255,77,79,0.02)'],
    mapAreaColor: '#3A1414',
    mapBorderColor: 'rgba(255,215,0,0.4)',
    mapEmphasisArea: '#5A2424',
    mapEmphasisBorder: '#FFD700'
  },
  warmOrange: {
    colors: ['#FF8C42', '#FFB347', '#FF6B6B', '#FFD93D', '#44FFAA', '#1890FF', '#A855F7', '#FF69B4'],
    areaGradient: ['rgba(255,140,66,0.35)', 'rgba(255,140,66,0.02)'],
    mapAreaColor: '#2A1A10',
    mapBorderColor: 'rgba(255,140,66,0.4)',
    mapEmphasisArea: '#4A2A1A',
    mapEmphasisBorder: '#FF8C42'
  },
  deepPurple: {
    colors: ['#A855F7', '#6366F1', '#C084FC', '#FF6B6B', '#FFD93D', '#44FFAA', '#FF8C42', '#FF69B4'],
    areaGradient: ['rgba(168,85,247,0.35)', 'rgba(168,85,247,0.02)'],
    mapAreaColor: '#1A1040',
    mapBorderColor: 'rgba(168,85,247,0.4)',
    mapEmphasisArea: '#2A1A60',
    mapEmphasisBorder: '#A855F7'
  },
  lightBusiness: {
    colors: ['#1890FF', '#52C41A', '#FF4D4F', '#FAAD14', '#722ED1', '#13C2C2', '#EB2F96', '#FA541C'],
    areaGradient: ['rgba(24,144,255,0.25)', 'rgba(24,144,255,0.02)'],
    mapAreaColor: '#E8F0FE',
    mapBorderColor: 'rgba(24,144,255,0.3)',
    mapEmphasisArea: '#D0E2FC',
    mapEmphasisBorder: '#1890FF'
  }
}
```

---

## 五、通用 ECharts 主题配置

```javascript
// 基于 CSS 变量的通用主题配置
function getEChartsTheme() {
  const root = getComputedStyle(document.documentElement)
  const pv = (name) => root.getPropertyValue(name).trim()

  return {
    color: pv('--chart-palette')?.split(',') || ['#00D4FF', '#0088FF', '#FF6B6B', '#FFD93D', '#44FFAA', '#A855F7', '#FF8C42', '#FF69B4'],
    backgroundColor: 'transparent',
    textStyle: { color: pv('--color-text') || '#E0E8FF', fontFamily: pv('--font-body') || 'DIN, sans-serif' },
    title: { textStyle: { color: pv('--color-title') || '#FFFFFF', fontSize: 16 } },
    legend: { textStyle: { color: pv('--color-text-muted') || '#6B7FA3', fontSize: 11 } },
    tooltip: {
      backgroundColor: pv('--bg-panel-solid') || '#0C1A3A',
      borderColor: pv('--border-panel') || 'rgba(0,212,255,0.3)',
      textStyle: { color: pv('--color-text') || '#E0E8FF', fontSize: 12 }
    }
  }
}
```
