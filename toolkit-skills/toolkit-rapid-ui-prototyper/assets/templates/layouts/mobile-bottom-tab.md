# Mobile Bottom Tab Layout Template

移动端底部 Tab 导航布局模板。适用于 H5 移动端 App 风格页面。

> **主题变量**：使用 `--mobile-*` 系列变量，支持 `body.light-mode` 亮暗切换。

---

## 布局结构

```
┌────────────────────────────────┐
│  Header（顶部标题栏 + 返回）    │
├────────────────────────────────┤
│                                │
│  Content（可滚动内容区域）      │
│                                │
│                                │
├────────────────────────────────┤
│  Tab1  Tab2  Tab3  Tab4        │
│  首页  分类  消息  我的        │
└────────────────────────────────┘
```

---

## 完整 HTML

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Mobile App</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    :root {
      --brand-primary: #2563eb;
      --brand-primary-hover: #1d4ed8;

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

    * { margin: 0; padding: 0; box-sizing: border-box; }
    html, body { height: 100%; overflow: hidden; }

    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Inter', sans-serif;
      -webkit-font-smoothing: antialiased;
      background: var(--mobile-bg);
      color: var(--mobile-text);
      transition: background 0.3s, color 0.3s;
    }

    /* ===== 移动端容器 ===== */
    .mobile-view {
      display: flex;
      flex-direction: column;
      height: 100vh;
      height: 100dvh; /* 动态视口高度 */
    }

    /* ===== 顶部导航栏 ===== */
    .mobile-header {
      flex-shrink: 0;
      background: var(--mobile-header-bg);
      border-bottom: 1px solid var(--mobile-border);
      padding: 12px 16px;
      padding-top: calc(12px + var(--mobile-safe-top));
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: background 0.3s;
    }

    .mobile-header h1 {
      font-size: 1.125rem;
      font-weight: 600;
      color: var(--mobile-text-heading);
    }

    .mobile-header .back-btn {
      padding: 4px;
      border-radius: 8px;
      color: var(--mobile-text-muted);
      background: none;
      border: none;
      cursor: pointer;
    }

    /* ===== 可滚动内容区 ===== */
    .mobile-content {
      flex: 1;
      overflow-y: auto;
      -webkit-overflow-scrolling: touch;
      padding: 16px;
      padding-bottom: calc(16px + 80px + var(--mobile-safe-bottom));
    }

    /* ===== 底部 Tab 栏 ===== */
    .mobile-tab-bar {
      flex-shrink: 0;
      background: var(--mobile-tab-bar-bg);
      border-top: 1px solid var(--mobile-border);
      padding: 8px 0;
      padding-bottom: calc(8px + var(--mobile-safe-bottom));
      display: flex;
      justify-content: space-around;
      align-items: flex-start;
      transition: background 0.3s;
    }

    .mobile-tab-bar a {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-decoration: none;
      color: var(--mobile-text-muted);
      font-size: 0.65rem;
      padding: 4px 12px;
      transition: color 0.2s;
      min-width: 56px;
    }

    .mobile-tab-bar a.active {
      color: var(--brand-primary);
    }

    .mobile-tab-bar a svg {
      width: 24px;
      height: 24px;
      margin-bottom: 2px;
    }
  </style>
</head>
<body>
  <div class="mobile-view">
    <!-- ===== 顶部导航栏 ===== -->
    <header class="mobile-header">
      <button class="back-btn" onclick="history.back()">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
        </svg>
      </button>
      <h1>首页</h1>
      <div class="flex items-center gap-3">
        <!-- 主题切换 -->
        <button onclick="toggleMobileTheme()" style="color: var(--mobile-text-muted); padding: 4px; background: none; border: none; cursor: pointer;">
          <svg id="m-sun" style="display:none; width:20px; height:20px; color:#f59e0b;" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd"/>
          </svg>
          <svg id="m-moon" style="width:20px; height:20px;" fill="currentColor" viewBox="0 0 20 20">
            <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/>
          </svg>
        </button>
      </div>
    </header>

    <!-- ===== 内容区 ===== -->
    <main class="mobile-content" id="pageContent">
      <!-- 子页面内容插槽 — 由具体页面模板填充 -->
    </main>

    <!-- ===== 底部 Tab 栏 ===== -->
    <nav class="mobile-tab-bar" id="tabBar">
      <a href="#" class="active" data-tab="home">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/>
        </svg>
        <span>首页</span>
      </a>
      <a href="#" data-tab="category">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/>
        </svg>
        <span>分类</span>
      </a>
      <a href="#" data-tab="messages">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/>
        </svg>
        <span>消息</span>
      </a>
      <a href="#" data-tab="profile">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
        </svg>
        <span>我的</span>
      </a>
    </nav>
  </div>

  <script>
    // Tab 切换
    document.getElementById('tabBar').addEventListener('click', function(e) {
      var link = e.target.closest('a');
      if (!link) return;
      e.preventDefault();
      this.querySelectorAll('a').forEach(function(a) { a.classList.remove('active'); });
      link.classList.add('active');
      document.querySelector('.mobile-header h1').textContent = link.querySelector('span').textContent;
    });

    // 主题切换
    function toggleMobileTheme() {
      var body = document.body;
      var sunIcon = document.getElementById('m-sun');
      var moonIcon = document.getElementById('m-moon');
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

将 `mobile-content` 内部替换为目标页面内容：

| 页面类型 | 参考模板 |
|---------|---------|
| 首页/Feed 流 | `components/card.md` 的移动端版本 |
| 列表页 | 卡片列表，每个卡片包含图标+文字+箭头 |
| 个人中心 | 头像卡片 + 功能列表项 |
| 详情页 | 自定义内容 + 底部操作栏 |

---

## 安全区域说明

`--mobile-safe-top` 和 `--mobile-safe-bottom` 使用 `env(safe-area-inset-*)` 适配 iPhone X+ 等全面屏设备。如果不需要安全区域适配，将这两个变量设为 `0px`。
