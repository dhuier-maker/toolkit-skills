# 浅色商务主题模板

> 适用于街道治理、企业服务等场景的 BI 大屏主题。
> 触发词：智慧街道、浅色大屏、商务大屏、报表大屏、企业大屏、SaaS仪表盘

---

## 一、主题配置（themes/index.js 中 lightBusiness 部分）

浅色商务主题的 JS 配置见 [dark-tech.md](dark-tech.md) 中 `themes` 对象的 `lightBusiness` 字段。

核心配色：

```javascript
colors: {
  bgPrimary: '#ffffff',           // 白色背景
  bgSecondary: '#f5f7fa',         // 浅灰次背景
  primary: '#0099ff',             // 主色（移动蓝）
  accent: '#52c41a',              // 点缀色（绿色）
  textPrimary: '#333333',         // 深色文字
  textSecondary: '#666666',
  border: '#e8e8e8',              // 浅边框
}

panel: {
  cornerDecoration: 'none',
  headerStyle: 'gradient',        // 蓝色渐变头部
  headerBackground: 'linear-gradient(90deg, #4a90e2, #5b9bd5)',
  shadow: 'none',
}
```

---

## 二、浅色商务主题样式 (themes/light-business.scss)

```scss
// 浅色商务主题样式
// 适用于街道治理、企业服务等场景

// ========== 颜色变量 ==========
$bg-primary: #ffffff;
$bg-secondary: #f5f7fa;
$bg-panel: #ffffff;
$bg-card: #f5f7fa;

$primary: #0099ff;
$primary-dark: #0066cc;
$primary-light: #33adff;

$accent: #52c41a;
$accent-dark: #00c853;
$accent-light: #73d13d;

$success: #52c41a;
$warning: #ff9800;
$danger: #f5222d;

$text-primary: #333333;
$text-secondary: #666666;
$text-muted: #999999;

$border: #e8e8e8;
$border-light: #d9d9d9;

// ========== 面板样式（蓝色渐变头部） ==========
.panel-frame {
  background: $bg-panel;
  border: 1px solid $border;
  border-radius: 4px;
  overflow: hidden;
}

.panel-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 12px;
  background: linear-gradient(90deg, #4a90e2, #5b9bd5);

  .title {
    font-size: 14px;
    font-weight: 500;
    color: #ffffff;
  }

  .arrow-icon {
    color: #ffffff;
    margin-right: 8px;
  }
}

.panel-title {
  font-size: 14px;
  color: #ffffff;
  font-weight: 500;
}

.panel-content {
  padding: 12px;
}

// ========== 标签样式 ==========
.status-tag {
  display: inline-block;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 12px;
  color: #ffffff;

  &.success { background: $success; }
  &.warning { background: $warning; }
  &.danger { background: $danger; }
  &.info { background: $primary; }
}

.month-tag {
  background: $primary;
  color: #ffffff;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 12px;
}

// ========== 标题栏样式 ==========
.bi-header {
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: $bg-primary;
  border-bottom: 1px solid $border;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.header-title {
  font-size: 24px;
  font-weight: bold;
  color: $text-primary;
}

// ========== 数据卡片样式 ==========
.data-card {
  display: flex;
  align-items: flex-start;
  padding: 16px;
  background: $bg-card;
  border: 1px solid $border;
  border-radius: 8px;
  transition: all 0.3s;

  &:hover {
    border-color: $primary;
    box-shadow: 0 4px 12px rgba(0, 153, 255, 0.15);
  }
}

.data-value {
  font-size: 28px;
  font-weight: bold;
  color: $text-primary;
}

.data-label {
  font-size: 14px;
  color: $text-secondary;
}

// ========== AI 识别卡片 ==========
.ai-card {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  background: rgba(0, 153, 255, 0.1);
  border: 1px solid $border;
  border-radius: 8px;

  .ai-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: $primary;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #ffffff;
    font-weight: bold;
    font-size: 14px;
  }

  .card-label {
    font-size: 12px;
    color: $text-secondary;
  }

  .card-value {
    font-size: 18px;
    font-weight: bold;
    color: $text-primary;

    .current { color: $success; }
    .separator { color: $text-muted; margin: 0 4px; }
  }
}

// ========== 底部导航栏 ==========
.bottom-nav {
  display: flex;
  gap: 2px;
  background: linear-gradient(90deg, #4a90e2, #0066cc);
  border-radius: 24px;
  padding: 4px;

  .nav-btn {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 10px 24px;
    background: transparent;
    border: none;
    color: rgba(255, 255, 255, 0.7);
    border-radius: 20px;
    cursor: pointer;
    transition: all 0.3s;

    &:hover { color: #ffffff; }

    &.active {
      background: $accent;
      color: #ffffff;
      box-shadow: 0 0 20px rgba(82, 196, 26, 0.5);
    }

    .nav-icon { font-size: 18px; }
    .nav-label { font-size: 14px; }
  }
}

// ========== 图表样式 ==========
.chart-container {
  background: $bg-primary;
}

.chart-axis-line {
  stroke: $border;
}

.chart-split-line {
  stroke: #f0f0f0;
}

.chart-text {
  fill: $text-secondary;
}
```

---

## 三、ThemeProvider 和 ThemeSelector

ThemeProvider 和 ThemeSelector 组件参考 [dark-tech.md](dark-tech.md) 中的实现，只需将 `defaultTheme` 改为 `lightBusiness`。

---

## 四、使用方式

```vue
<template>
  <ThemeProvider theme="lightBusiness">
    <Dashboard />
  </ThemeProvider>
</template>
```
