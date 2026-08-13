# Mobile Theme Template

移动端主题变量模板。专为 H5 移动端页面设计，支持亮暗模式切换。默认暗色，`body.light-mode` 切换为亮色。

---

## 基础变量定义

```css
:root {
  /* ===== 移动端（默认暗色） ===== */
  --mobile-bg: linear-gradient(180deg, #0c1524 0%, #060b14 100%);  /* 页面背景渐变 */
  --mobile-header-bg: rgba(12, 21, 36, 0.95);    /* 顶部导航栏背景 */
  --mobile-card-bg: rgba(12, 21, 36, 0.8);       /* 卡片背景 */
  --mobile-input-bg: rgba(12, 21, 36, 0.6);      /* 输入框背景 */
  --mobile-text: #e2e8f0;                          /* 正文颜色 */
  --mobile-text-heading: #e8d48b;                  /* 标题颜色 */
  --mobile-text-muted: #94a3b8;                    /* 次要文字 */
  --mobile-border: rgba(200, 164, 78, 0.15);       /* 边框 */
  --mobile-tab-bar-bg: rgba(12, 21, 36, 0.98);     /* 底部 Tab 栏背景 */
  --mobile-safe-top: env(safe-area-inset-top, 0px);   /* 安全区域上 */
  --mobile-safe-bottom: env(safe-area-inset-bottom, 0px); /* 安全区域下 */
}
```

---

## 亮色模式覆盖

```css
body.light-mode {
  --mobile-bg: #f1f5f9;
  --mobile-header-bg: #ffffff;
  --mobile-card-bg: #ffffff;
  --mobile-input-bg: #ffffff;
  --mobile-text: #1e293b;
  --mobile-text-heading: #1e293b;
  --mobile-text-muted: #64748b;
  --mobile-border: #e2e8f0;
  --mobile-tab-bar-bg: #ffffff;
}
```

---

## 完整示例

```html
<style>
  :root {
    /* 品牌色 */
    --brand-primary: #2563eb;
    --brand-primary-hover: #1d4ed8;

    /* 移动端暗色 */
    --mobile-bg: linear-gradient(180deg, #0c1524 0%, #060b14 100%);
    --mobile-header-bg: rgba(12, 21, 36, 0.95);
    --mobile-card-bg: rgba(12, 21, 36, 0.8);
    --mobile-text: #e2e8f0;
    --mobile-text-heading: #e8d48b;
    --mobile-text-muted: #94a3b8;
    --mobile-border: rgba(200, 164, 78, 0.15);
    --mobile-tab-bar-bg: rgba(12, 21, 36, 0.98);
    --mobile-safe-top: env(safe-area-inset-top, 0px);
    --mobile-safe-bottom: env(safe-area-inset-bottom, 0px);
  }

  body.light-mode {
    --mobile-bg: #f1f5f9;
    --mobile-header-bg: #ffffff;
    --mobile-card-bg: #ffffff;
    --mobile-text: #1e293b;
    --mobile-text-heading: #1e293b;
    --mobile-text-muted: #64748b;
    --mobile-border: #e2e8f0;
    --mobile-tab-bar-bg: #ffffff;
  }

  body {
    margin: 0;
    padding: 0;
    background: var(--mobile-bg);
    color: var(--mobile-text);
    font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;
    -webkit-font-smoothing: antialiased;
    transition: background 0.3s, color 0.3s;
  }

  .mobile-header {
    padding-top: var(--mobile-safe-top);
  }

  .mobile-tab-bar {
    padding-bottom: var(--mobile-safe-bottom);
  }
</style>
```

> **提示**：移动端通常与移动端底部 Tab 布局模板（`layouts/mobile-bottom-tab.md`）配合使用，也可单独用于页面头部和列表卡片。
