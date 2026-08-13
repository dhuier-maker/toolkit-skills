# 工程设计规范

> BI 大屏工程规范汇总：阴影体系、Z-index 层级、间距刻度、交互状态、滚动条样式。

---

## 一、阴影体系

### 5 级阴影定义

| 层级 | CSS 变量 | 用途 | 说明 |
|------|----------|------|------|
| 面板 | `--shadow-panel` | `.panel-frame` 默认阴影 | 深色：主题色微光；浅色：灰色投影 |
| 悬停 | `--shadow-hover` | 面板/卡片 hover 时 | 面板阴影 ×1.5 强度 |
| 卡片 | `--shadow-card` | `.data-card` 阴影 | 介于面板与悬停之间 |
| 弹窗 | `--shadow-modal` | 弹窗/对话框 | 最强阴影，突出层级 |
| 地图浮层 | `--shadow-map-overlay` | InfoWindow/浮动面板 | 中等强度 + 主题色微光 |

### 6 主题阴影色值

| 主题 | --shadow-panel | --shadow-hover | --shadow-card | --shadow-modal | --shadow-map-overlay |
|------|---------------|----------------|---------------|----------------|---------------------|
| techBlue | `0 2px 12px rgba(0,212,255,0.08)` | `0 4px 20px rgba(0,212,255,0.15)` | `0 2px 8px rgba(0,212,255,0.06)` | `0 8px 32px rgba(0,212,255,0.2)` | `0 4px 16px rgba(0,212,255,0.12)` |
| ecoGreen | `0 2px 12px rgba(0,229,195,0.08)` | `0 4px 20px rgba(0,229,195,0.15)` | `0 2px 8px rgba(0,229,195,0.06)` | `0 8px 32px rgba(0,229,195,0.2)` | `0 4px 16px rgba(0,229,195,0.12)` |
| partyRed | `0 2px 12px rgba(255,215,0,0.08)` | `0 4px 20px rgba(255,215,0,0.15)` | `0 2px 8px rgba(255,215,0,0.06)` | `0 8px 32px rgba(255,215,0,0.2)` | `0 4px 16px rgba(255,215,0,0.12)` |
| warmOrange | `0 2px 12px rgba(255,140,66,0.08)` | `0 4px 20px rgba(255,140,66,0.15)` | `0 2px 8px rgba(255,140,66,0.06)` | `0 8px 32px rgba(255,140,66,0.2)` | `0 4px 16px rgba(255,140,66,0.12)` |
| deepPurple | `0 2px 12px rgba(168,85,247,0.08)` | `0 4px 20px rgba(168,85,247,0.15)` | `0 2px 8px rgba(168,85,247,0.06)` | `0 8px 32px rgba(168,85,247,0.2)` | `0 4px 16px rgba(168,85,247,0.12)` |
| lightBusiness | `0 2px 8px rgba(0,0,0,0.06)` | `0 4px 16px rgba(0,0,0,0.1)` | `0 2px 6px rgba(0,0,0,0.04)` | `0 8px 24px rgba(0,0,0,0.15)` | `0 4px 12px rgba(0,0,0,0.08)` |

> 浅色主题使用灰色投影，深色5主题使用主题色发光阴影。

### CSS 使用

```scss
.panel-frame {
  box-shadow: var(--shadow-panel);
  transition: box-shadow var(--duration-normal) var(--ease-default);

  &:hover {
    box-shadow: var(--shadow-hover);
  }
}

.data-card {
  box-shadow: var(--shadow-card);
}

.modal-overlay {
  box-shadow: var(--shadow-modal);
}

.map-info-window {
  box-shadow: var(--shadow-map-overlay);
}
```

---

## 二、Z-index 层级

### 10 级定义

| 层级 | CSS 变量 | 值 | 用途 |
|------|----------|-----|------|
| 0 | `--z-bg` | 0 | 背景层（bg-bottom、粒子） |
| 1 | `--z-content` | 5 | 内容层（面板、图表） |
| 2 | `--z-map` | 10 | 地图容器 |
| 3 | `--z-map-overlay` | 20 | 地图叠加（图例、控制面板） |
| 4 | `--z-map-float` | 30 | 地图浮层（InfoWindow、标记弹窗） |
| 5 | `--z-tooltip` | 45 | 全局 Tooltip |
| 6 | `--z-header` | 55 | 顶部标题栏 |
| 7 | `--z-mask` | 65 | 遮罩层 |
| 8 | `--z-modal` | 70 | 弹窗/对话框 |
| 9 | `--z-notify` | 90 | 通知/Toast |

### CSS 变量定义

```css
:root {
  --z-bg: 0;
  --z-content: 5;
  --z-map: 10;
  --z-map-overlay: 20;
  --z-map-float: 30;
  --z-tooltip: 45;
  --z-header: 55;
  --z-mask: 65;
  --z-modal: 70;
  --z-notify: 90;
}
```

### 使用规则

- 面板内弹窗：使用 `--z-modal`，不受父容器 z-index 限制
- 地图 InfoWindow：使用 `--z-map-float`，不超过标题栏
- 多层弹窗叠加：`z-index: calc(var(--z-modal) + 层级差 * 5)`
- 禁止硬编码 z-index 值，统一使用 CSS 变量

---

## 三、间距刻度

### 4px 基数 8 级刻度

| Token | 值 | 用途 |
|-------|-----|------|
| `--space-1` | 4px | 图标与文字间距、紧凑内边距 |
| `--space-2` | 8px | 小组件内边距、标签间距 |
| `--space-3` | 12px | 面板内边距、元素间距 |
| `--space-4` | 16px | 面板间距(gap)、卡片内边距 |
| `--space-5` | 20px | 区域间距 |
| `--space-6` | 24px | 大面板内边距 |
| `--space-7` | 32px | 区块间距 |
| `--space-8` | 40px | 大区块间距、页面级间距 |

### 常见场景映射

| 场景 | Token | 值 |
|------|-------|-----|
| 面板内边距(padding) | --space-3 | 12px |
| 面板间距(gap) | --space-3 | 12px |
| KPI 卡片间距 | --space-4 | 16px |
| 标题栏高度 | 固定值 | 64px |
| 左右面板宽度 | 固定值 | 320px |
| 图表容器内边距 | --space-3 | 12px |
| 弹窗内边距 | --space-5 | 20px |
| 按钮组间距 | --space-2 | 8px |

---

## 四、交互状态

### 面板 3 态

| 状态 | 边框 | 背景 | 阴影 |
|------|------|------|------|
| Default | `var(--border-panel)` | `var(--bg-panel)` | `var(--shadow-panel)` |
| Hover | 边框透明度 ×1.5 | 叠加 `rgba(primary, 0.04)` | `var(--shadow-hover)` |
| Active/Selected | 边框透明度 ×2.0 | 叠加 `rgba(primary, 0.08)` | `var(--shadow-hover)` |

```scss
.panel-frame {
  border: 1px solid var(--border-panel);
  background: var(--bg-panel);
  box-shadow: var(--shadow-panel);
  transition: all var(--duration-normal) var(--ease-default);

  &:hover {
    border-color: var(--border-glow);  // ×1.5 透明度
    background: linear-gradient(var(--bg-panel), var(--bg-panel)),
                linear-gradient(var(--bg-panel), rgba(var(--color-primary-rgb), 0.04));
    box-shadow: var(--shadow-hover);
  }

  &.is-active,
  &.is-selected {
    border-color: var(--border-glow);  // ×2.0 透明度
    background: linear-gradient(var(--bg-panel), var(--bg-panel)),
                linear-gradient(var(--bg-panel), rgba(var(--color-primary-rgb), 0.08));
    box-shadow: var(--shadow-hover);
  }
}
```

### 列表项 3 态

| 状态 | 左侧指示 | 背景 |
|------|----------|------|
| Default | 无 | 透明 |
| Hover | 2px 主题色竖条 | `rgba(primary, 0.06)` |
| Active/Selected | 3px 主题色竖条 | `rgba(primary, 0.10)` |

```scss
.list-item {
  padding: var(--space-2) var(--space-3);
  border-left: 2px solid transparent;
  transition: all var(--duration-fast) var(--ease-default);

  &:hover {
    border-left-color: var(--color-primary);
    background: rgba(var(--color-primary-rgb), 0.06);
  }

  &.is-active {
    border-left-width: 3px;
    border-left-color: var(--color-primary);
    background: rgba(var(--color-primary-rgb), 0.10);
  }
}
```

### KPI 卡片微交互

| 状态 | 效果 |
|------|------|
| Hover | `transform: translateY(-2px)` |
| Active | `transform: scale(0.97)` |

```scss
.data-card {
  transition: transform var(--duration-fast) var(--ease-out);

  &:hover {
    transform: translateY(-2px);
  }

  &:active {
    transform: scale(0.97);
  }
}
```

### 地图区域 3 态

| 状态 | 区域填充 | 边界线 |
|------|----------|--------|
| Default | `areaColor` | `borderColor` 正常 |
| Hover | `areaColor` 亮度 +15% | `borderColor` 亮度 +20% |
| Selected | `areaColor` 亮度 +25% | `borderColor` 亮度 +30%，线宽 +1 |

```javascript
// ECharts 地图 region 配置
emphasis: {
  itemStyle: {
    areaColor: themeMap.hoverAreaColor,
    borderColor: themeMap.hoverBorderColor,
    borderWidth: 2
  }
},
select: {
  itemStyle: {
    areaColor: themeMap.selectedAreaColor,
    borderColor: themeMap.selectedBorderColor,
    borderWidth: 3
  }
}
```

---

## 五、滚动条样式

### 深色主题（techBlue / ecoGreen / partyRed / warmOrange / deepPurple）

```css
/* 自定义滚动条 — 深色5主题 */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background: rgba(var(--color-primary-rgb), 0.25);
  border-radius: 3px;

  &:hover {
    background: rgba(var(--color-primary-rgb), 0.40);
  }
}

/* Firefox */
.panel-content {
  scrollbar-width: thin;
  scrollbar-color: rgba(var(--color-primary-rgb), 0.25) transparent;
}
```

### 浅色主题（lightBusiness）

```css
/* 自定义滚动条 — 浅色主题 */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.04);
  border-radius: 3px;
}

::-webkit-scrollbar-thumb {
  background: rgba(0, 0, 0, 0.15);
  border-radius: 3px;

  &:hover {
    background: rgba(0, 0, 0, 0.25);
  }
}

/* Firefox */
.panel-content {
  scrollbar-width: thin;
  scrollbar-color: rgba(0, 0, 0, 0.15) rgba(0, 0, 0, 0.04);
}
```

### CSS 变量方案（统一）

| 变量 | 深色5主题 | 浅色主题 |
|------|----------|---------|
| `--scrollbar-width` | `6px` | `6px` |
| `--scrollbar-track` | `transparent` | `rgba(0,0,0,0.04)` |
| `--scrollbar-thumb` | `rgba(primary, 0.25)` | `rgba(0,0,0,0.15)` |
| `--scrollbar-thumb-hover` | `rgba(primary, 0.40)` | `rgba(0,0,0,0.25)` |
