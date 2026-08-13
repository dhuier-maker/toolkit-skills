# 主题系统（明暗切换）

使用 CSS 变量 + `body.light-mode` class 切换模式，**禁止使用 Tailwind `dark:` 前缀**（因为 `dark:` 只响应 `prefers-color-scheme` 媒体查询，无法通过 JS 手动切换）。

## 架构规则

1. **所有颜色必须走 CSS 变量** — 禁止在组件 CSS 类或内联样式中硬编码颜色值
2. **组件样式提取为 CSS 类** — `.stat-card`、`.data-table`、`.modal-content` 等，统一管理主题
3. **弹窗/模态框必须使用主题类** — `class="modal-content"`，禁止内联 `style="background: ..."`
4. **固定暗色视图必须隔离** — BI 大屏等永远暗色的视图，用 `body.light-mode #view-bi { ... }` 重置变量
5. **批量替换注意幂等性** — 用精确选择器避免二次替换破坏已有代码

## 变量体系（按视图分组）

```css
:root {
  /* 品牌色 */
  --brand-primary: #2563eb;
  --brand-primary-hover: #1d4ed8;

  /* 管理后台 */
  --admin-bg: #060b14;
  --admin-bg-card: rgba(12, 21, 36, 0.8);
  --admin-bg-input: rgba(12, 21, 36, 0.6);
  --admin-bg-modal: #0f172a;
  --admin-text: #e2e8f0;
  --admin-text-heading: #e8d48b;
  --admin-text-muted: #94a3b8;
  --admin-border: rgba(200, 164, 78, 0.2);
  --admin-table-head-bg: rgba(0, 212, 255, 0.05);
  --admin-table-hover: rgba(0, 212, 255, 0.05);

  /* 移动端 */
  --mobile-bg: linear-gradient(180deg, #0c1524 0%, #060b14 100%);
  --mobile-header-bg: rgba(12,21,36,0.95);
  --mobile-card-bg: rgba(12,21,36,0.8);

  /* BI 大屏（固定暗色） */
  --bi-bg: #060b14;
  --bi-card-bg: rgba(0, 212, 255, 0.05);
  --bi-text: #e2e8f0;
  --bi-text-muted: #94a3b8;
}

/* 亮色模式覆盖 */
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

  --mobile-bg: #f1f5f9;
  --mobile-header-bg: #ffffff;
  --mobile-card-bg: #ffffff;
}

/* 固定暗色视图 — 亮色模式也不受影响 */
body.light-mode #view-bi {
  --bi-text: #e2e8f0;
  --bi-text-muted: #94a3b8;
}
```

## 组件 CSS 类（使用变量）

```css
.stat-card { background: var(--admin-bg-card); border: 1px solid var(--admin-border); }
.card { background: var(--admin-bg-card); border: 1px solid var(--admin-border); }
.data-table th { color: var(--admin-text-heading); border-bottom: 1px solid var(--admin-border); }
.data-table td { color: var(--admin-text); border-bottom: 1px solid var(--admin-border); }
.btn-secondary { background: var(--admin-bg-input); color: var(--admin-text); border: 1px solid var(--admin-border); }
.input-field { background: var(--admin-bg-input); color: var(--admin-text); border: 1px solid var(--admin-border); }
.page-btn { background: var(--admin-bg-input); color: var(--admin-text); border: 1px solid var(--admin-border); }

.modal-content { background: var(--admin-bg-modal); border: 1px solid var(--admin-border); }
body.light-mode .modal-content { background: #ffffff; }

.btn-primary { background: linear-gradient(135deg, var(--brand-primary) 0%, var(--brand-primary-hover) 100%); color: white; }
```

## 亮色模式补充覆盖

对于 Tailwind 工具类（如 `text-slate-300`、`hover:bg-white/5`）在亮色模式下需要覆盖：

```css
body.light-mode #view-admin .text-slate-300,
body.light-mode #view-admin .text-slate-400 { color: #64748b !important; }
body.light-mode #view-admin .hover\:bg-white\/5:hover { background-color: #f1f5f9 !important; }
body.light-mode .border-white\/10 { border-color: #e2e8f0 !important; }
body.light-mode .border-white\/5 { border-color: #f1f5f9 !important; }
```

## 主题切换按钮

```html
<button onclick="toggleAdminTheme()" class="p-2 rounded-lg transition-colors duration-200"
  style="background: var(--admin-bg-input); border: 1px solid var(--admin-border);">
  <svg id="theme-icon-sun" style="display:none; width:20px; height:20px; color:#f59e0b;" fill="currentColor" viewBox="0 0 20 20">
    <path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0z..." clip-rule="evenodd"/>
  </svg>
  <svg id="theme-icon-moon" style="width:20px; height:20px; color: var(--admin-text-muted);" fill="currentColor" viewBox="0 0 20 20">
    <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/>
  </svg>
</button>

<script>
function toggleAdminTheme() {
  const body = document.body;
  const sunIcon = document.getElementById('theme-icon-sun');
  const moonIcon = document.getElementById('theme-icon-moon');
  body.classList.toggle('light-mode');
  const isLight = body.classList.contains('light-mode');
  sunIcon.style.display = isLight ? '' : 'none';
  moonIcon.style.display = isLight ? 'none' : '';
}
</script>
```

## 关键反模式（避免）

| 反模式 | 正确做法 |
|--------|----------|
| 组件 CSS 中硬编码 `background: rgba(12,21,36,0.8)` | `background: var(--admin-bg-card)` |
| 弹窗内联 `style="background: #0f172a"` | `class="modal-content"` |
| 用 `dark:` 前缀做主题切换 | 用 `body.light-mode` + CSS 变量 |
| BI 大屏受亮色模式影响 | `body.light-mode #view-bi { }` 重置关键变量 |
| 批量正则替换 `-50` → `-500/10` | 只匹配目标属性，避免二次替换 |
