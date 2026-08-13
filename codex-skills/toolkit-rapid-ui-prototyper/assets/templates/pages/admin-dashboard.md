# Admin Dashboard Page Template

管理后台首页模板。包含统计卡片、ECharts 图表、数据表格，使用侧边栏布局。

> 本模板依赖 ECharts（通过 CDN 引入），也可替换为其他图表库。颜色全部使用 CSS 变量。

---

## 完整 HTML

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dashboard - Admin</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --brand-primary: #2563eb;
      --brand-primary-hover: #1d4ed8;
      --brand-success: #10b981;
      --brand-danger: #ef4444;

      --admin-bg: #060b14;
      --admin-bg-card: rgba(12, 21, 36, 0.8);
      --admin-bg-input: rgba(12, 21, 36, 0.6);
      --admin-sidebar-bg: rgba(12, 21, 36, 0.95);
      --admin-header-bg: rgba(12, 21, 36, 0.9);
      --admin-text: #e2e8f0;
      --admin-text-heading: #e8d48b;
      --admin-text-muted: #94a3b8;
      --admin-border: rgba(200, 164, 78, 0.2);
      --admin-table-head-bg: rgba(0, 212, 255, 0.05);
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
      --admin-table-head-bg: #f8fafc;
      --admin-table-hover: #f1f5f9;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: 'Inter', system-ui, sans-serif;
      background: var(--admin-bg);
      color: var(--admin-text);
      transition: background 0.3s, color 0.3s;
    }

    /* ===== Sidebar (same as sidebar-nav.md) ===== */
    .sidebar {
      position: fixed; left: 0; top: 0; bottom: 0; width: 260px;
      background: var(--admin-sidebar-bg);
      border-right: 1px solid var(--admin-border);
      z-index: 40; display: flex; flex-direction: column;
      transition: background 0.3s;
    }
    .sidebar-logo { padding: 20px 24px; border-bottom: 1px solid var(--admin-border); }
    .sidebar-logo h1 { color: var(--admin-text-heading); font-size: 1.25rem; font-weight: 700; }
    .sidebar-nav { flex: 1; padding: 16px 12px; overflow-y: auto; }
    .sidebar-nav .nav-label {
      color: var(--admin-text-muted); font-size: 0.7rem; text-transform: uppercase;
      letter-spacing: 0.05em; padding: 8px 12px 4px;
    }
    .sidebar-nav a {
      display: flex; align-items: center; padding: 10px 12px; margin-bottom: 2px;
      border-radius: 8px; color: var(--admin-text-muted); text-decoration: none;
      font-size: 0.875rem; transition: all 0.2s;
    }
    .sidebar-nav a:hover { background: var(--admin-table-hover); color: var(--admin-text); }
    .sidebar-nav a.active {
      background: rgba(37, 99, 235, 0.1); color: var(--brand-primary);
      border-right: 3px solid var(--brand-primary);
    }
    .sidebar-nav a svg { width: 20px; height: 20px; margin-right: 12px; flex-shrink: 0; }

    .main-content { margin-left: 260px; min-height: 100vh; }
    .top-header {
      position: sticky; top: 0; z-index: 30;
      background: var(--admin-header-bg);
      border-bottom: 1px solid var(--admin-border);
      padding: 12px 24px; display: flex; align-items: center;
      justify-content: space-between; transition: background 0.3s;
    }
    .page-content { padding: 24px; }

    /* ===== Stats Cards ===== */
    .stat-card {
      background: var(--admin-bg-card);
      border: 1px solid var(--admin-border);
      border-radius: 12px; padding: 20px;
      transition: all 0.2s;
    }
    .stat-card:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(0,0,0,0.15); }

    /* ===== Chart Container ===== */
    .chart-container {
      background: var(--admin-bg-card);
      border: 1px solid var(--admin-border);
      border-radius: 12px; padding: 20px;
    }
    .chart-box { width: 100%; height: 300px; }

    /* ===== Table ===== */
    .data-table { width: 100%; border-collapse: collapse; }
    .data-table th {
      color: var(--admin-text-heading); border-bottom: 2px solid var(--admin-border);
      background: var(--admin-table-head-bg);
      padding: 12px 16px; text-align: left;
      font-size: 0.75rem; font-weight: 600; text-transform: uppercase;
    }
    .data-table td {
      color: var(--admin-text); border-bottom: 1px solid var(--admin-border);
      padding: 12px 16px; font-size: 0.875rem;
    }
    .data-table tbody tr:hover { background: var(--admin-table-hover); }

    /* ===== Badges ===== */
    .badge-success { background: rgba(16, 185, 129, 0.15); color: var(--brand-success); }
    .badge-warning { background: rgba(245, 158, 11, 0.15); color: var(--brand-warning); }
    .badge-danger { background: rgba(239, 68, 68, 0.15); color: var(--brand-danger); }
    .badge-info { background: rgba(59, 130, 246, 0.15); color: var(--brand-info); }
    .badge { display: inline-flex; align-items: center; padding: 2px 10px; border-radius: 9999px; font-size: 0.75rem; font-weight: 500; }

    @media (max-width: 768px) {
      .sidebar { display: none; }
      .main-content { margin-left: 0; }
    }
  </style>
</head>
<body>
  <!-- ===== Sidebar ===== -->
  <aside class="sidebar">
    <div class="sidebar-logo"><h1>Admin Panel</h1></div>
    <nav class="sidebar-nav">
      <div class="nav-label">Main</div>
      <a href="#" class="active">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
        Dashboard
      </a>
      <a href="#">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
        Users
      </a>
      <a href="#">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
        Reports
      </a>
    </nav>
  </aside>

  <!-- ===== Main Content ===== -->
  <div class="main-content">
    <!-- Top Header -->
    <header class="top-header">
      <h2 style="color: var(--admin-text-heading);" class="text-xl font-semibold">Dashboard</h2>
      <div class="flex items-center gap-3">
        <button onclick="toggleTheme()" class="px-3 py-1.5 rounded-lg text-xs transition-colors"
          style="background: var(--admin-bg-input); border: 1px solid var(--admin-border); color: var(--admin-text-muted);">
          <span id="themeLabel">亮色模式</span>
        </button>
        <div class="w-8 h-8 rounded-full bg-gradient-to-br from-indigo-400 to-purple-500 flex items-center justify-center text-white text-sm font-medium">A</div>
      </div>
    </header>

    <!-- Page Content -->
    <div class="page-content space-y-6">
      <!-- Stats Cards -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <div class="stat-card">
          <p style="color: var(--admin-text-muted);" class="text-sm">总收入</p>
          <p style="color: var(--admin-text-heading);" class="text-2xl font-bold mt-1">¥128,450</p>
          <span style="color: var(--brand-success);" class="text-xs font-medium">↑ 12.5%</span>
        </div>
        <div class="stat-card">
          <p style="color: var(--admin-text-muted);" class="text-sm">活跃用户</p>
          <p style="color: var(--admin-text-heading);" class="text-2xl font-bold mt-1">2,847</p>
          <span style="color: var(--brand-success);" class="text-xs font-medium">↑ 8.2%</span>
        </div>
        <div class="stat-card">
          <p style="color: var(--admin-text-muted);" class="text-sm">订单数</p>
          <p style="color: var(--admin-text-heading);" class="text-2xl font-bold mt-1">356</p>
          <span style="color: var(--brand-success);" class="text-xs font-medium">↑ 3.1%</span>
        </div>
        <div class="stat-card">
          <p style="color: var(--admin-text-muted);" class="text-sm">跳出率</p>
          <p style="color: var(--admin-text-heading);" class="text-2xl font-bold mt-1">24.8%</p>
          <span style="color: var(--brand-danger);" class="text-xs font-medium">↑ 2.4%</span>
        </div>
      </div>

      <!-- Charts Row -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div class="chart-container">
          <h3 style="color: var(--admin-text-heading);" class="text-base font-semibold mb-4">月度收入趋势</h3>
          <div id="trendChart" class="chart-box"></div>
        </div>
        <div class="chart-container">
          <h3 style="color: var(--admin-text-heading);" class="text-base font-semibold mb-4">用户分布</h3>
          <div id="pieChart" class="chart-box"></div>
        </div>
      </div>

      <!-- Recent Orders Table -->
      <div class="chart-container">
        <h3 style="color: var(--admin-text-heading);" class="text-base font-semibold mb-4">最新订单</h3>
        <div style="overflow-x: auto;">
          <table class="data-table">
            <thead>
              <tr>
                <th>订单号</th>
                <th>客户</th>
                <th>金额</th>
                <th>状态</th>
                <th>时间</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="font-medium">#ORD-001</td>
                <td style="color: var(--admin-text-muted);">张小明</td>
                <td>¥1,280</td>
                <td><span class="badge badge-success">已完成</span></td>
                <td style="color: var(--admin-text-muted);">2024-01-15</td>
              </tr>
              <tr>
                <td class="font-medium">#ORD-002</td>
                <td style="color: var(--admin-text-muted);">李小红</td>
                <td>¥3,450</td>
                <td><span class="badge badge-warning">处理中</span></td>
                <td style="color: var(--admin-text-muted);">2024-01-14</td>
              </tr>
              <tr>
                <td class="font-medium">#ORD-003</td>
                <td style="color: var(--admin-text-muted);">王大力</td>
                <td>¥560</td>
                <td><span class="badge badge-success">已完成</span></td>
                <td style="color: var(--admin-text-muted);">2024-01-14</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>

  <script>
    // 主题切换
    function toggleTheme() {
      document.body.classList.toggle('light-mode');
      var label = document.getElementById('themeLabel');
      label.textContent = document.body.classList.contains('light-mode') ? '暗色模式' : '亮色模式';
      // 图表重绘（主题色变化后可能需要）
      renderCharts();
    }

    // ECharts 渲染
    function renderCharts() {
      var isLight = document.body.classList.contains('light-mode');
      var textColor = isLight ? '#64748b' : '#94a3b8';
      var axisColor = isLight ? '#e2e8f0' : 'rgba(200,164,78,0.15)';

      // 收入趋势折线图
      var trendChart = echarts.init(document.getElementById('trendChart'));
      trendChart.setOption({
        tooltip: { trigger: 'axis' },
        grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
        xAxis: { type: 'category', data: ['1月','2月','3月','4月','5月','6月'], axisLabel: { color: textColor }, axisLine: { lineStyle: { color: axisColor } } },
        yAxis: { type: 'value', axisLabel: { color: textColor }, splitLine: { lineStyle: { color: axisColor } } },
        series: [{
          type: 'line', smooth: true,
          data: [120, 200, 150, 280, 180, 340],
          lineStyle: { color: '#2563eb', width: 3 },
          areaStyle: { color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1, colorStops: [{ offset: 0, color: 'rgba(37,99,235,0.3)' }, { offset: 1, color: 'rgba(37,99,235,0.02)' }] } },
          symbol: 'circle', symbolSize: 8
        }]
      });

      // 用户分布饼图
      var pieChart = echarts.init(document.getElementById('pieChart'));
      pieChart.setOption({
        tooltip: { trigger: 'item' },
        series: [{
          type: 'pie', radius: ['40%', '70%'], center: ['50%', '50%'],
          data: [
            { value: 1048, name: '管理员', itemStyle: { color: '#2563eb' } },
            { value: 735, name: '编辑', itemStyle: { color: '#10b981' } },
            { value: 580, name: '普通用户', itemStyle: { color: '#f59e0b' } },
            { value: 484, name: '访客', itemStyle: { color: '#94a3b8' } }
          ],
          label: { color: textColor },
          emphasis: { itemStyle: { shadowBlur: 10, shadowOffsetX: 0, shadowColor: 'rgba(0,0,0,0.5)' } }
        }]
      });

      // 窗口大小变化时自适应
      window.addEventListener('resize', function() {
        trendChart.resize();
        pieChart.resize();
      });
    }

    renderCharts();
  </script>
</body>
</html>
```

---

## 使用说明

1. **统计卡片**：修改 `grid-cols-4` 中的卡片数量和内容
2. **图表**：修改 `renderCharts()` 中的 ECharts option 配置
3. **表格**：替换 tbody 中的行数据
4. **侧栏菜单**：修改 `sidebar-nav` 中的链接
5. **CDN**：可替换为本地资源或 npm 包

## 注意事项

- 图表的文字颜色（axisLabel、label）根据 `body.light-mode` 动态适配
- 窗口 resize 时图表自动 resize
- 主题切换后调用 `renderCharts()` 重绘图表，确保颜色更新
- 移动端侧栏自动隐藏（`@media (max-width: 768px)`）
