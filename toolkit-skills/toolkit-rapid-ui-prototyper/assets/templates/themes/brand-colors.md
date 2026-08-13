# Brand Colors Template

品牌色变量模板。所有视图共享，不参与亮暗模式切换。

---

## 默认品牌色（蓝色系）

```css
:root {
  /* ===== 品牌色 ===== */
  --brand-primary: #2563eb;           /* 主色 — 按钮、链接、活跃态 */
  --brand-primary-hover: #1d4ed8;     /* 主色悬停 */
  --brand-primary-light: rgba(37, 99, 235, 0.1);  /* 主色背景（浅色） */

  /* 辅助色 */
  --brand-success: #10b981;           /* 成功/绿色 */
  --brand-warning: #f59e0b;           /* 警告/琥珀色 */
  --brand-danger: #ef4444;            /* 危险/红色 */
  --brand-info: #3b82f6;              /* 信息/蓝色 */

  /* 字体 */
  --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;

  /* 间距系统（8px Grid） */
  --space-1: 0.25rem;    /* 4px */
  --space-2: 0.5rem;     /* 8px */
  --space-3: 0.75rem;    /* 12px */
  --space-4: 1rem;       /* 16px */
  --space-6: 1.5rem;     /* 24px */
  --space-8: 2rem;       /* 32px */
  --space-12: 3rem;      /* 48px */
  --space-16: 4rem;      /* 64px */

  /* 圆角 */
  --radius-sm: 0.25rem;   /* 4px */
  --radius-md: 0.5rem;    /* 8px */
  --radius-lg: 0.75rem;   /* 12px */
  --radius-xl: 1rem;      /* 16px */
  --radius-full: 9999px;  /* 圆形 */

  /* 阴影 */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.15);
}
```

---

## 绿色系品牌色

```css
:root {
  --brand-primary: #059669;
  --brand-primary-hover: #047857;
  --brand-primary-light: rgba(5, 150, 105, 0.1);
  --brand-success: #10b981;
  --brand-warning: #f59e0b;
  --brand-danger: #ef4444;
  --brand-info: #3b82f6;
}
```

---

## 紫色系品牌色

```css
:root {
  --brand-primary: #7c3aed;
  --brand-primary-hover: #6d28d9;
  --brand-primary-light: rgba(124, 58, 237, 0.1);
  --brand-success: #10b981;
  --brand-warning: #f59e0b;
  --brand-danger: #ef4444;
  --brand-info: #3b82f6;
}
```

---

## 使用示例

```css
.btn-primary {
  background: linear-gradient(135deg, var(--brand-primary) 0%, var(--brand-primary-hover) 100%);
  color: white;
}

.badge-success {
  background: var(--brand-success);
  color: white;
}
```

> **注意**：品牌色永远不参与亮暗模式切换。如需在亮色模式下调亮/调暗，可额外定义 `--brand-primary-lightmode` 等变量并手动管理。
