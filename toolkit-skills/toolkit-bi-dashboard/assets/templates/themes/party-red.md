# 党建红金主题模板

> 适用于党建、政务等场景的 BI 大屏主题。
> 触发词：智慧党建、党建大屏、红色主题大屏、党政大屏、党建成效、廉政大屏

---

## 一、主题配置（themes/index.js 中 partyRed 部分）

党建红金主题的 JS 配置见 [dark-tech.md](dark-tech.md) 中 `themes` 对象的 `partyRed` 字段。

核心配色：

```javascript
colors: {
  bgPrimary: '#4a0e0e',           // 深红背景
  bgSecondary: '#6b1a1a',         // 次红背景
  primary: '#c41e3a',             // 主色（中国红）
  accent: '#ffd700',              // 点缀色（金色）
  info: '#48dbfb',                // 图表用青蓝色对比
  textPrimary: '#ffffff',
  textSecondary: '#ffb4a2',
  border: '#daa520',              // 金色边框
}

panel: {
  cornerDecoration: 'gold',       // 金色四角装饰
  headerStyle: 'partyIcon',       // 党徽图标头部
  shadow: '0 0 10px rgba(196, 30, 58, 0.3)',
}
```

---

## 二、党建红金主题样式 (themes/party-red.scss)

```scss
// 党建红金主题样式
// 适用于党建、政务等场景

// ========== 颜色变量 ==========
$bg-primary: #4a0e0e;
$bg-secondary: #6b1a1a;
$bg-panel: rgba(60, 10, 10, 0.7);
$bg-card: rgba(80, 20, 20, 0.5);

$primary: #c41e3a;
$primary-dark: #8b2020;
$primary-light: #e63946;

$accent: #ffd700;
$accent-dark: #daa520;
$accent-light: #ffed4a;

$success: #00c853;
$warning: #ffb703;
$danger: #ff5252;
$info: #48dbfb; // 青蓝色，红底图表对比色

$text-primary: #ffffff;
$text-secondary: #ffb4a2;
$text-muted: rgba(255, 255, 255, 0.6);

$border: #daa520;
$border-light: rgba(218, 165, 32, 0.3);

// ========== 面板样式（带四角装饰） ==========
.panel-frame {
  background: $bg-panel;
  border: 2px solid $border;
  border-radius: 4px;
  box-shadow: 0 0 10px rgba(196, 30, 58, 0.3);
  padding: 14px;
  position: relative;
}

// 四角装饰
.panel-corner {
  position: absolute;
  width: 20px;
  height: 20px;

  &::before, &::after {
    content: '';
    position: absolute;
    background: $accent;
  }

  &::before {
    width: 100%;
    height: 2px;
  }

  &::after {
    width: 2px;
    height: 100%;
  }

  &-tl { top: -2px; left: -2px; }
  &-tr { top: -2px; right: -2px;
    &::before { right: 0; }
    &::after { right: 0; }
  }
  &-bl { bottom: -2px; left: -2px;
    &::before { bottom: 0; }
    &::after { bottom: 0; }
  }
  &-br { bottom: -2px; right: -2px;
    &::before { bottom: 0; right: 0; }
    &::after { bottom: 0; right: 0; }
  }
}

.panel-header {
  display: flex;
  align-items: center;
  padding: 12px 16px;
  background: rgba(196, 30, 58, 0.2);
  border-bottom: 1px solid $border-light;
}

// 党徽图标
.party-icon {
  width: 24px;
  height: 24px;
  margin-right: 8px;
  fill: $accent;
}

.panel-title {
  font-size: 16px;
  color: $text-primary;
  font-weight: 500;
}

// ========== 标题栏样式 ==========
.bi-header {
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(180deg, rgba(74, 14, 14, 0.95) 0%, rgba(74, 14, 14, 0.8) 100%);
  border-bottom: 1px solid $border-light;
  position: relative;

  // 两侧红色光带装饰
  &::before, &::after {
    content: '';
    position: absolute;
    top: 50%;
    width: 200px;
    height: 2px;
    background: linear-gradient(90deg, transparent, $primary-light, transparent);
  }

  &::before { left: 20%; }
  &::after { right: 20%; }
}

.header-title {
  font-size: 28px;
  font-weight: bold;
  color: $accent;
  letter-spacing: 4px;
  text-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
}

// ========== 五角星中心节点 ==========
.star-center {
  width: 120px;
  height: 120px;
  position: relative;

  // 五角星 SVG
  svg {
    width: 100%;
    height: 100%;
    fill: $accent;
    filter: drop-shadow(0 0 20px rgba(255, 215, 0, 0.5));
  }

  .star-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 16px;
    font-weight: bold;
    color: $accent;
    text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
  }
}

// ========== 人员头像卡片（金色发光边框） ==========
.avatar-card {
  .avatar {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    border: 2px solid $accent;
    box-shadow: 0 0 15px rgba(255, 215, 0, 0.4);
  }

  .name {
    font-size: 14px;
    color: $text-primary;
    margin-top: 8px;
  }

  .position {
    font-size: 12px;
    color: $accent;
  }
}

// ========== 图表样式（青蓝色对比） ==========
.chart-series-main {
  fill: $info;
  stroke: $info;
}

.chart-bar-gradient {
  fill: url(#gradient-cyan);
}

// 渐变定义
.chart-defs {
  defs {
    linearGradient#gradient-cyan {
      stop:first-child { stop-color: rgba(72, 219, 251, 0.3); }
      stop:last-child { stop-color: rgba(72, 219, 251, 0.9); }
    }
  }
}
```

---

## 三、ThemeProvider 和 ThemeSelector

ThemeProvider 和 ThemeSelector 组件参考 [dark-tech.md](dark-tech.md) 中的实现，只需将 `defaultTheme` 改为 `partyRed`。

---

## 四、使用方式

```vue
<template>
  <ThemeProvider theme="partyRed">
    <Dashboard />
  </ThemeProvider>
</template>
```
