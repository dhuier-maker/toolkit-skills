# Admin Theme Template

管理后台主题变量模板。支持亮暗模式切换，默认暗色，`body.light-mode` 切换为亮色。

---

## 基础变量定义

```css
:root {
  /* ===== 管理后台（默认暗色） ===== */
  --admin-bg: #060b14;                    /* 页面背景 */
  --admin-bg-card: rgba(12, 21, 36, 0.8); /* 卡片背景 */
  --admin-bg-input: rgba(12, 21, 36, 0.6);/* 输入框背景 */
  --admin-bg-modal: #0f172a;              /* 弹窗背景 */
  --admin-sidebar-bg: rgba(12, 21, 36, 0.95);  /* 侧栏背景 */
  --admin-header-bg: rgba(12, 21, 36, 0.9);    /* 顶栏背景 */

  --admin-text: #e2e8f0;                  /* 正文颜色 */
  --admin-text-heading: #e8d48b;           /* 标题颜色（金色） */
  --admin-text-muted: #94a3b8;             /* 次要文字 */

  --admin-border: rgba(200, 164, 78, 0.2);      /* 边框（金色半透明） */
  --admin-table-head-bg: rgba(0, 212, 255, 0.05);  /* 表头背景 */
  --admin-table-hover: rgba(0, 212, 255, 0.05);    /* 行悬停背景 */
  --admin-table-stripe: rgba(0, 212, 255, 0.02);   /* 斑马纹背景（可选） */
}
```

---

## 亮色模式覆盖

```css
body.light-mode {
  --admin-bg: #f1f5f9;
  --admin-bg-card: #ffffff;
  --admin-bg-input: #ffffff;
  --admin-bg-modal: #ffffff;
  --admin-sidebar-bg: #ffffff;
  --admin-header-bg: #ffffff;

  --admin-text: #1e293b;
  --admin-text-heading: #1e293b;
  --admin-text-muted: #64748b;

  --admin-border: #e2e8f0;
  --admin-table-head-bg: #f8fafc;
  --admin-table-hover: #f1f5f9;
  --admin-table-stripe: #fafbfc;
}
```

---

## 亮色模式 Tailwind 覆盖（补充）

对于直接使用的 Tailwind 工具类颜色，在亮色模式下需要额外覆盖：

```css
body.light-mode #view-admin .text-slate-300,
body.light-mode #view-admin .text-slate-400 {
  color: #64748b !important;
}

body.light-mode #view-admin .hover\\:bg-white\\/5:hover {
  background-color: #f1f5f9 !important;
}

body.light-mode .border-white\\/10 {
  border-color: #e2e8f0 !important;
}

body.light-mode .border-white\\/5 {
  border-color: #f1f5f9 !important;
}

body.light-mode .bg-white\\/5 {
  background-color: #f1f5f9 !important;
}
```

---

## 主题切换按钮

```html
<button onclick="toggleAdminTheme()" class="p-2 rounded-lg transition-colors duration-200"
  style="background: var(--admin-bg-input); border: 1px solid var(--admin-border);">
  <!-- 太阳图标（亮色模式显示） -->
  <svg id="theme-icon-sun" style="display:none; width:20px; height:20px; color:#f59e0b;" fill="currentColor" viewBox="0 0 20 20">
    <path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0z..." clip-rule="evenodd"/>
  </svg>
  <!-- 月亮图标（暗色模式显示） -->
  <svg id="theme-icon-moon" style="width:20px; height:20px; color: var(--admin-text-muted);" fill="currentColor" viewBox="0 0 20 20">
    <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/>
  </svg>
</button>

<script>
function toggleAdminTheme() {
  var body = document.body;
  var sunIcon = document.getElementById('theme-icon-sun');
  var moonIcon = document.getElementById('theme-icon-moon');
  body.classList.toggle('light-mode');
  var isLight = body.classList.contains('light-mode');
  sunIcon.style.display = isLight ? '' : 'none';
  moonIcon.style.display = isLight ? 'none' : '';
}
</script>
```

---

## 使用示例

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Admin Page</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    :root {
      /* 品牌色 */
      --brand-primary: #2563eb;
      --brand-primary-hover: #1d4ed8;

      /* 管理后台（暗色默认） */
      --admin-bg: #060b14;
      --admin-bg-card: rgba(12, 21, 36, 0.8);
      --admin-text: #e2e8f0;
      --admin-text-muted: #94a3b8;
      --admin-border: rgba(200, 164, 78, 0.2);
    }

    body.light-mode {
      --admin-bg: #f1f5f9;
      --admin-bg-card: #ffffff;
      --admin-text: #1e293b;
      --admin-text-muted: #64748b;
      --admin-border: #e2e8f0;
    }

    body {
      background: var(--admin-bg);
      color: var(--admin-text);
      font-family: 'Inter', system-ui, sans-serif;
      transition: background 0.3s, color 0.3s;
    }
  </style>
</head>
<body>
  <div id="view-admin">
    <h1 style="color: var(--admin-text-heading);">管理后台</h1>
    <div class="card" style="background: var(--admin-bg-card); border: 1px solid var(--admin-border);">
      <p>卡片内容</p>
    </div>
  </div>
</body>
</html>
```
