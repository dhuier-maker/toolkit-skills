# Sidebar Navigation Layout Template

侧边栏导航布局模板。适用于管理后台、仪表盘等需要深度导航的场景。

> **主题变量**：使用 `--admin-*` 系列变量，支持 `body.light-mode` 亮暗切换。

---

## 布局结构

```
┌─────────┬──────────────────────────────────┐
│         │  Top Header                      │
│  侧栏   │  搜索 + 通知 + 头像 + 主题切换    │
│  Logo   ├──────────────────────────────────┤
│ 导航    │  Page Content（主要内容）         │
│ 菜单    │  统计卡片 / 图表 / 表格 / 表单    │
│         │                                  │
│ 用户    │                                  │
└─────────┴──────────────────────────────────┘
```

---

## 完整 HTML

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Admin Dashboard</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --brand-primary: #2563eb;
      --brand-primary-hover: #1d4ed8;

      --admin-bg: #060b14;
      --admin-bg-card: rgba(12, 21, 36, 0.8);
      --admin-bg-input: rgba(12, 21, 36, 0.6);
      --admin-sidebar-bg: rgba(12, 21, 36, 0.95);
      --admin-header-bg: rgba(12, 21, 36, 0.9);
      --admin-text: #e2e8f0;
      --admin-text-heading: #e8d48b;
      --admin-text-muted: #94a3b8;
      --admin-border: rgba(200, 164, 78, 0.2);
      --admin-table-hover: rgba(0, 212, 255, 0.05);
    }

    body.light-mode {
      --admin-bg: #f1f5f9;
      --admin-bg-card: #ffffff;
      --admin-bg-input: #ffffff;
      --admin-sidebar-bg: #ffffff;
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

    /* ===== 侧栏 ===== */
    .sidebar {
      position: fixed;
      left: 0;
      top: 0;
      bottom: 0;
      width: 260px;
      background: var(--admin-sidebar-bg);
      border-right: 1px solid var(--admin-border);
      z-index: 40;
      display: flex;
      flex-direction: column;
      transition: background 0.3s, transform 0.3s;
    }

    .sidebar-logo {
      padding: 20px 24px;
      border-bottom: 1px solid var(--admin-border);
    }

    .sidebar-logo h1 {
      color: var(--admin-text-heading);
      font-size: 1.25rem;
      font-weight: 700;
    }

    .sidebar-nav {
      flex: 1;
      padding: 16px 12px;
      overflow-y: auto;
    }

    .sidebar-nav .nav-label {
      color: var(--admin-text-muted);
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 8px 12px 4px;
    }

    .sidebar-nav a {
      display: flex;
      align-items: center;
      padding: 10px 12px;
      margin-bottom: 2px;
      border-radius: 8px;
      color: var(--admin-text-muted);
      text-decoration: none;
      font-size: 0.875rem;
      transition: all 0.2s;
    }

    .sidebar-nav a:hover {
      background: var(--admin-table-hover);
      color: var(--admin-text);
    }

    .sidebar-nav a.active {
      background: rgba(37, 99, 235, 0.1);
      color: var(--brand-primary);
      border-right: 3px solid var(--brand-primary);
    }

    .sidebar-nav a svg {
      width: 20px;
      height: 20px;
      margin-right: 12px;
      flex-shrink: 0;
    }

    .sidebar-footer {
      padding: 16px 12px;
      border-top: 1px solid var(--admin-border);
    }

    /* ===== 主内容区 ===== */
    .main-content {
      margin-left: 260px;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    .top-header {
      position: sticky;
      top: 0;
      z-index: 30;
      background: var(--admin-header-bg);
      border-bottom: 1px solid var(--admin-border);
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: background 0.3s;
    }

    .page-content {
      flex: 1;
      padding: 24px;
    }

    /* ===== 响应式 — 移动端折叠 ===== */
    @media (max-width: 768px) {
      .sidebar { transform: translateX(-100%); }
      .sidebar.open { transform: translateX(0); }
      .main-content { margin-left: 0; }

      .mobile-menu-btn { display: block !important; }
    }

    .mobile-menu-btn { display: none; }
  </style>
</head>
<body>
  <!-- ===== 侧栏 ===== -->
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-logo">
      <h1>Admin Panel</h1>
    </div>

    <nav class="sidebar-nav">
      <div class="nav-label">Main</div>
      <a href="#" class="active">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
        Dashboard
      </a>
      <a href="#">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
        Analytics
      </a>
      <a href="#">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
        Users
      </a>

      <div class="nav-label" style="margin-top: 16px;">System</div>
      <a href="#">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.066 2.573c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.573 1.066c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.066-2.573c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
        Settings
      </a>
    </nav>

    <div class="sidebar-footer">
      <a href="#" style="display: flex; align-items: center; padding: 8px 12px; border-radius: 8px; color: var(--admin-text-muted); text-decoration: none; font-size: 0.875rem;">
        <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"/></svg>
        Logout
      </a>
    </div>
  </aside>

  <!-- ===== 主内容区 ===== -->
  <div class="main-content">
    <!-- 顶栏 -->
    <header class="top-header">
      <div class="flex items-center gap-4">
        <!-- 移动端菜单按钮 -->
        <button class="mobile-menu-btn p-2 rounded-lg" onclick="document.getElementById('sidebar').classList.toggle('open')"
          style="background: var(--admin-bg-input); border: 1px solid var(--admin-border); color: var(--admin-text);">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
        </button>
        <h2 style="color: var(--admin-text-heading); font-size: 1.25rem; font-weight: 600;">Dashboard</h2>
      </div>

      <div class="flex items-center gap-3">
        <!-- 搜索 -->
        <div class="relative hidden sm:block">
          <input type="text" placeholder="Search..." class="pl-9 pr-3 py-1.5 rounded-lg text-sm"
            style="background: var(--admin-bg-input); color: var(--admin-text); border: 1px solid var(--admin-border);">
          <svg class="absolute left-2.5 top-2 w-4 h-4" style="color: var(--admin-text-muted);" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
        </div>

        <!-- 通知 -->
        <button class="relative p-2 rounded-lg" style="color: var(--admin-text-muted);">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/></svg>
          <span class="absolute -top-0.5 -right-0.5 w-4 h-4 bg-red-500 rounded-full text-white text-[10px] flex items-center justify-center">3</span>
        </button>

        <!-- 主题切换 -->
        <button onclick="toggleAdminTheme()" class="p-2 rounded-lg transition-colors"
          style="background: var(--admin-bg-input); border: 1px solid var(--admin-border);">
          <svg id="theme-icon-sun" style="display:none; width:18px; height:18px; color:#f59e0b;" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd"/>
          </svg>
          <svg id="theme-icon-moon" style="width:18px; height:18px; color: var(--admin-text-muted);" fill="currentColor" viewBox="0 0 20 20">
            <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/>
          </svg>
        </button>

        <!-- 头像 -->
        <div class="w-8 h-8 rounded-full bg-gradient-to-br from-indigo-400 to-purple-500 flex items-center justify-center text-white text-sm font-medium">
          A
        </div>
      </div>
    </header>

    <!-- 页面内容 -->
    <div class="page-content">
      <!-- 子页面内容插槽 — 由具体的页面模板填充 -->
    </div>
  </div>

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

    // 点击侧栏外部关闭移动端菜单
    document.addEventListener('click', function(e) {
      var sidebar = document.getElementById('sidebar');
      if (window.innerWidth <= 768 && sidebar.classList.contains('open')) {
        if (!sidebar.contains(e.target) && !e.target.closest('.mobile-menu-btn')) {
          sidebar.classList.remove('open');
        }
      }
    });
  </script>
</body>
</html>
```

---

## 组件填充指南

将侧栏内容区 `.page-content` 替换为目标页面内容：

| 页面类型 | 参考模板 |
|---------|---------|
| 仪表盘 | `pages/admin-dashboard.md` |
| 数据表格 | `pages/list-detail.md` |
| 表单 | `pages/form-page.md` |
| 登录 | `pages/login.md`（独立页面，不需侧栏） |
