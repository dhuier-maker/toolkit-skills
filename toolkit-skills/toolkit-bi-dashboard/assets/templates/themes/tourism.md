# 文旅主题模板

> 适用于旅游景区、文旅大数据、客流分析等场景的 BI 大屏主题。
> 触发词：文旅大数据、景区大屏、游客分析大屏、旅游大屏、客流分析大屏

---

**配色方案**：
- 主色：`#00b894`（翡翠绿）
- 辅色：`#00cec9`（青绿）
- 强调色：`#fdcb6e`（金色）
- 背景色：`#0a1a1a`（深墨绿）
- 风格：国潮/绿色生态

---

## 一、主题配置（themes/index.js 中 ecoGreen 部分）

青绿生态主题的 JS 配置见 [dark-tech.md](dark-tech.md) 中 `themes` 对象的 `ecoGreen` 字段。

```javascript
// ========== 文旅主题 ==========
tourism: {
  name: '文旅主题',
  nameEn: 'Tourism',
  description: '适用于旅游景区、文旅大数据、客流分析等场景',

  colors: {
    // 背景色（深墨绿）
    bgPrimary: '#0a1a1a',
    bgSecondary: '#0f2626',
    bgPanel: 'rgba(10, 35, 30, 0.75)',
    bgCard: 'rgba(0, 30, 25, 0.5)',

    // 主色（翡翠绿）
    primary: '#00b894',
    primaryDark: '#00856a',
    primaryLight: '#00e6b0',

    // 点缀色（国潮金）
    accent: '#fdcb6e',
    accentDark: '#e0a800',
    accentLight: '#ffeaa7',

    // 状态色
    success: '#00b894',
    warning: '#fdcb6e',
    danger: '#e17055',
    info: '#00cec9',

    // 文字色
    textPrimary: '#ffffff',
    textSecondary: '#81ecec',
    textMuted: 'rgba(255, 255, 255, 0.6)',

    // 边框色
    border: '#00b894',
    borderLight: 'rgba(0, 184, 148, 0.3)',
    borderGlow: 'rgba(0, 230, 176, 0.3)',

    // 图表色板（翡翠绿+青绿+金色+珊瑚+粉紫）
    chartColors: ['#00b894', '#00cec9', '#fdcb6e', '#e17055', '#fd79a8', '#6c5ce7'],
  },

  panel: {
    borderRadius: '4px',
    borderWidth: '1px',
    borderStyle: 'solid',
    cornerDecoration: 'wave',
    headerStyle: 'waveLine',
    headerBackground: 'rgba(0, 184, 148, 0.1)',
    headerBorderColor: 'rgba(0, 230, 176, 0.2)',
    shadow: '0 0 10px rgba(0, 184, 148, 0.3)',
  },

  map: {
    areaColor: '#0a2a22',
    borderColor: '#00e6b0',
    borderWidth: 1,
    emphasisAreaColor: '#1a4a3a',
    emphasisBorderColor: '#fdcb6e',
  },

  chart: {
    backgroundColor: 'transparent',
    textColor: '#ffffff',
    axisLineColor: 'rgba(255, 255, 255, 0.1)',
    splitLineColor: 'rgba(0, 230, 176, 0.1)',
  },
},
```

---

## 二、青绿生态主题样式 (themes/eco-green.scss)

```scss
// 青绿生态主题样式
// 适用于旅游景区、文旅大数据、客流分析等场景
// 风格：国潮/绿色生态

// ========== 颜色变量 ==========
$bg-primary: #0a1a1a;
$bg-secondary: #0f2626;
$bg-panel: rgba(10, 35, 30, 0.75);
$bg-card: rgba(0, 30, 25, 0.5);

$primary: #00b894;
$primary-dark: #00856a;
$primary-light: #00e6b0;

$accent: #fdcb6e;
$accent-dark: #e0a800;
$accent-light: #ffeaa7;

$success: #00b894;
$warning: #fdcb6e;
$danger: #e17055;
$info: #00cec9;

$text-primary: #ffffff;
$text-secondary: #81ecec;
$text-muted: rgba(255, 255, 255, 0.6);

$border: #00b894;
$border-light: rgba(0, 184, 148, 0.3);

// ========== 波浪装饰动画 ==========
@keyframes wave {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(100%);
  }
}

@keyframes float {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-5px);
  }
}

@keyframes shimmer {
  0% {
    background-position: -200% center;
  }
  100% {
    background-position: 200% center;
  }
}

// ========== 面板样式 ==========
.panel-frame {
  background: $bg-panel;
  border: 1px solid $border-light;
  border-radius: 4px;
  box-shadow: 0 0 10px rgba(0, 184, 148, 0.3);
  padding: 14px;
  position: relative;
  overflow: hidden;

  // 底部波浪装饰线
  &::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, $primary, $accent, transparent);
    opacity: 0.5;
  }
}

.panel-header {
  display: flex;
  align-items: center;
  padding: 12px 16px;
  background: rgba(0, 184, 148, 0.1);
  border-bottom: 1px solid $border-light;
  position: relative;

  // 顶部波浪线装饰
  &::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg,
      transparent 0%,
      $primary 20%,
      $accent 40%,
      $primary 60%,
      $accent 80%,
      transparent 100%
    );
    background-size: 200% 2px;
    animation: shimmer 3s linear infinite;
    opacity: 0.8;
  }
}

.panel-title {
  display: flex;
  align-items: center;
  font-size: 16px;
  color: $text-primary;

  .title-bar {
    width: 3px;
    height: 16px;
    background: linear-gradient(180deg, $primary, $accent);
    margin-right: 8px;
    border-radius: 2px;
  }

  .title-icon {
    margin-right: 8px;
    font-size: 18px;
  }
}

// ========== 标题栏样式 ==========
.bi-header {
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(180deg, rgba(10, 26, 26, 0.95) 0%, rgba(10, 26, 26, 0.8) 100%);
  border-bottom: 1px solid $border-light;
  position: relative;

  // 两侧绿色光带
  &::before, &::after {
    content: '';
    position: absolute;
    top: 50%;
    width: 200px;
    height: 2px;
    background: linear-gradient(90deg, transparent, $primary-light, $accent, transparent);
  }

  &::before { left: 15%; }
  &::after { right: 15%; }
}

.header-title {
  font-size: 28px;
  font-weight: bold;
  color: $text-primary;
  letter-spacing: 4px;
  text-shadow: 0 0 20px rgba(0, 184, 148, 0.5);
}

.header-subtitle {
  font-size: 14px;
  color: $text-secondary;
  margin-left: 16px;
  letter-spacing: 2px;
}

// ========== 数据卡片样式（悬浮动画） ==========
.data-card {
  display: flex;
  align-items: flex-start;
  padding: 16px;
  background: $bg-card;
  border: 1px solid $border-light;
  border-radius: 8px;
  transition: all 0.3s;

  &:hover {
    border-color: $primary;
    transform: translateY(-3px);
    box-shadow: 0 6px 16px rgba(0, 184, 148, 0.3);
  }

  .data-card-icon {
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(0, 184, 148, 0.15);
    border-radius: 8px;
    font-size: 22px;
    margin-right: 12px;
  }
}

.data-value {
  font-size: 28px;
  font-weight: bold;
  color: $primary-light;
  font-family: 'JetBrains Mono', 'Courier New', monospace;
}

.data-label {
  font-size: 14px;
  color: $text-secondary;
}

.data-unit {
  font-size: 14px;
  color: $accent;
  margin-left: 2px;
}

// ========== 特色装饰元素 ==========
// 山脉/波浪装饰线
.mountain-decoration {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 40px;
  opacity: 0.1;

  svg {
    width: 100%;
    height: 100%;
    fill: $primary;
  }
}

// 游客标签徽章
.tourist-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 12px;
  background: linear-gradient(135deg, $primary, $info);
  border-radius: 12px;
  color: #ffffff;
  font-size: 12px;
  font-weight: 500;
}

// 热门标签（金色）
.hot-tag {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 2px 8px;
  background: rgba($accent, 0.2);
  border: 1px solid $accent;
  border-radius: 4px;
  color: $accent;
  font-size: 11px;
}

// ========== 图表样式 ==========
.chart-container {
  background: transparent;
}

.chart-axis-line {
  stroke: rgba(255, 255, 255, 0.1);
}

.chart-split-line {
  stroke: rgba(0, 230, 176, 0.1);
}

.chart-text {
  fill: $text-secondary;
}

// ========== 呼吸动画（翡翠色） ==========
@keyframes breathe-emerald {
  0%, 100% {
    box-shadow: 0 0 8px rgba(0, 184, 148, 0.15);
    border-color: rgba(0, 184, 148, 0.18);
  }
  50% {
    box-shadow: 0 0 20px rgba(0, 184, 148, 0.35);
    border-color: rgba(0, 184, 148, 0.35);
  }
}

.panel-breathe {
  animation: breathe-emerald 3s ease-in-out infinite;
}
```

---

## 三、CSS 变量

通过 `generateCssVariables(tourism)` 生成文旅主题的 CSS 变量：

```css
:root[data-theme="tourism"] {
  /* 背景色 */
  --bg-primary: #0a1a1a;
  --bg-secondary: #0f2626;
  --bg-panel: rgba(10, 35, 30, 0.75);
  --bg-card: rgba(0, 30, 25, 0.5);

  /* 主色 */
  --primary: #00b894;
  --primary-dark: #00856a;
  --primary-light: #00e6b0;

  /* 点缀色 */
  --accent: #fdcb6e;
  --accent-dark: #e0a800;
  --accent-light: #ffeaa7;

  /* 状态色 */
  --success: #00b894;
  --warning: #fdcb6e;
  --danger: #e17055;
  --info: #00cec9;

  /* 文字色 */
  --text-primary: #ffffff;
  --text-secondary: #81ecec;
  --text-muted: rgba(255, 255, 255, 0.6);

  /* 边框色 */
  --border: #00b894;
  --border-light: rgba(0, 184, 148, 0.3);
  --border-glow: rgba(0, 230, 176, 0.3);

  /* 面板样式 */
  --panel-border-radius: 4px;
  --panel-border-width: 1px;
  --panel-shadow: 0 0 10px rgba(0, 184, 148, 0.3);

  /* 地图样式 */
  --map-area-color: #0a2a22;
  --map-border-color: #00e6b0;

  /* 图表样式 */
  --chart-bg: transparent;
  --chart-text: #ffffff;
}
```

---

## 四、ThemeProvider 和 ThemeSelector

ThemeProvider 和 ThemeSelector 组件参考 [dark-tech.md](dark-tech.md) 中的实现。

在 ThemeSelector 中增加文旅主题预览：

```scss
&.preview-tourism {
  background: linear-gradient(135deg, #0a1a1a, #00b894);
}
```

---

## 五、使用方式

```vue
<template>
  <ThemeProvider theme="ecoGreen">
    <Dashboard />
  </ThemeProvider>
</template>
```

---

## 六、触发词配置

在 SKILL.md 中增加文旅主题触发词：

```
| 触发词 | 生成的主题 |
|--------|------------|
| 文旅大数据、景区大屏、游客分析大屏、旅游大屏、客流分析大屏 | tourism |
```
