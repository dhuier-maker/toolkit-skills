# Top Navigation Layout Template

顶部导航布局模板。适用于官网、SaaS 应用、文档站、门户等场景。

> **主题变量**：使用 `--admin-*` 系列变量（顶部导航使用 `--admin-header-bg`），支持 `body.light-mode` 亮暗切换。

---

## 布局结构

```
┌─────────────────────────────────────────┐
│  Logo   导航1  导航2  导航3    搜索 头像  │
├─────────────────────────────────────────┤
│  Page Content（全宽主要内容区）          │
│                                         │
└─────────────────────────────────────────┘
```

---

## 完整 HTML

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Top Navigation Layout</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --brand-primary: #2563eb;
      --brand-primary-hover: #1d4ed8;

      --admin-bg: #060b14;
      --admin-bg-card: rgba(12, 21, 36, 0.8);
      --admin-header-bg: rgba(12, 21, 36, 0.95);
      --admin-text: #e2e8f0;
      --admin-text-heading: #e8d48b;
      --admin-text-muted: #94a3b8;
      --admin-border: rgba(200, 164, 78, 0.2);
      --admin-table-hover: rgba(0, 212, 255, 0.05);
    }

    body.light-mode {
      --admin-bg: #f1f5f9;
      --admin-bg-card: #ffffff;
      --admin-header-bg: #ffffff;
      --admin-text: #1e293b;
      --admin-text-heading: #1e293b;
      --admin-text-muted: #64748b;
      --admin-border: #e2e8f0;
      --admin-table-hover: #f1f5f9;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: 'Inter', system-ui, sans-serif;
      background: var(--admin-bg);
      color: var(--admin-text);
      transition: background 0.3s, color 0.3s;
    }

    /* ===== 顶部导航 ===== */
    .top-nav {
      position: sticky;
      top: 0;
      z-index: 50;
      background: var(--admin-header-bg);
      border-bottom: 1px solid var(--admin-border);
      backdrop-filter: blur(12px);
      transition: background 0.3s;
    }

    .top-nav-inner {
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 24px;
      height: 64px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .top-nav .logo {
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--admin-text-heading);
      text-decoration: none;
    }

    .top-nav .nav-links {
      display: flex;
      align-items: center;
      gap: 4px;
    }

    .top-nav .nav-links a {
      padding: 8px 16px;
      border-radius: 8px;
      color: var(--admin-text-muted);
      text-decoration: none;
      font-size: 0.875rem;
      font-weight: 500;
      transition: all 0.2s;
    }

    .top-nav .nav-links a:hover {
      background: var(--admin-table-hover);
      color: var(--admin-text);
    }

    .top-nav .nav-links a.active {
      color: var(--brand-primary);
      background: rgba(37, 99, 235, 0.1);
    }

    .top-nav .nav-right {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    /* ===== 汉堡菜单（移动端） ===== */
    .hamburger { display: none; }

    @media (max-width: 768px) {
      .top-nav .nav-links {
        display: none;
        position: absolute;
        top: 64px;
        left: 0;
        right: 0;
        background: var(--admin-header-bg);
        border-bottom: 1px solid var(--admin-border);
        flex-direction: column;
        padding: 8px 16px;
      }

      .top-nav .nav-links.open { display: flex; }
      .top-nav .nav-links a { width: 100%; padding: 12px 16px; }

      .hamburger { display: block; }
    }

    /* ===== 页面内容 ===== */
    .page-content {
      max-width: 1280px;
      margin: 0 auto;
      padding: 32px 24px;
      min-height: calc(100vh - 64px);
    }
  </style>
</head>
<body>
  <!-- ===== 顶部导航栏 ===== -->
  <nav class="top-nav">
    <div class="top-nav-inner">
      <a href="#" class="logo">MyApp</a>

      <div class="nav-links" id="navLinks">
        <a href="#" class="active">Dashboard</a>
        <a href="#">Features</a>
        <a href="#">Pricing</a>
        <a href="#">Docs</a>
        <a href="#">Support</a>
      </div>

      <div class="nav-right">
        <!-- 主题切换 -->
        <button onclick="toggleTheme()" class="p-2 rounded-lg transition-colors"
          style="background: var(--admin-bg-card); border: 1px solid var(--admin-border);">
          <svg id="sun-icon" style="display:none; width:18px; height:18px; color:#f59e0b;" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd"/>
          </svg>
          <svg id="moon-icon" style="width:18px; height:18px; color: var(--admin-text-muted);" fill="currentColor" viewBox="0 0 20 20">
            <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/>
          </svg>
        </button>

        <!-- 头像 -->
        <div class="w-8 h-8 rounded-full bg-gradient-to-br from-indigo-400 to-purple-500 flex items-center justify-center text-white text-sm font-medium cursor-pointer">
          A
        </div>
      </div>

      <!-- 汉堡菜单按钮 -->
      <button class="hamburger p-2 rounded-lg" onclick="document.getElementById('navLinks').classList.toggle('open')"
        style="color: var(--admin-text-muted);">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
        </svg>
      </button>
    </div>
  </nav>

  <!-- ===== 页面内容 ===== -->
  <main class="page-content">
    <!-- 子页面内容插槽 — 由具体页面模板填充 -->
  </main>

  <script>
    function toggleTheme() {
      var body = document.body;
      var sunIcon = document.getElementById('sun-icon');
      var moonIcon = document.getElementById('moon-icon');
      body.classList.toggle('light-mode');
      var isLight = body.classList.contains('light-mode');
      sunIcon.style.display = isLight ? '' : 'none';
      moonIcon.style.display = isLight ? 'none' : '';
    }
  </script>
</body>
</html>
```

---

## 组件填充指南

将 `page-content` 内部替换为目标页面内容：

| 页面类型 | 参考模板 |
|---------|---------|
| 首页/Hero | 自定义内容 |
| 功能列表 | 卡片组件（`components/card.md`） |
| 价格页 | 卡片组件 + 按钮 |
| 文档内容 | 自定义排版 |
