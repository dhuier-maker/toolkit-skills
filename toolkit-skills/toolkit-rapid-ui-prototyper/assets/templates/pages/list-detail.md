# List + Detail Page Template

列表 + 详情页模板。包含搜索筛选、数据表格、分页、详情弹窗。适用于数据管理场景。

---

## 完整 HTML

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>用户管理 - Admin</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --brand-primary: #2563eb;
      --brand-primary-hover: #1d4ed8;
      --brand-success: #10b981;
      --brand-danger: #ef4444;
      --brand-warning: #f59e0b;

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
    }

    body.light-mode {
      --admin-bg: #f1f5f9;
      --admin-bg-card: #ffffff;
      --admin-bg-input: #ffffff;
      --admin-bg-modal: #ffffff;
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
      min-height: 100vh;
      padding: 32px 24px;
      transition: background 0.3s, color 0.3s;
    }

    .page-header {
      display: flex; align-items: center; justify-content: space-between;
      margin-bottom: 24px; flex-wrap: wrap; gap: 12px;
    }

    /* ===== Search Bar ===== */
    .search-bar {
      display: flex; align-items: center; gap: 12px; flex-wrap: wrap;
      margin-bottom: 20px;
    }

    .input-field {
      background: var(--admin-bg-input);
      color: var(--admin-text);
      border: 1px solid var(--admin-border);
      transition: all 0.2s;
    }

    .input-field:focus {
      outline: none;
      border-color: var(--brand-primary);
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
    }

    .btn-primary {
      background: linear-gradient(135deg, var(--brand-primary) 0%, var(--brand-primary-hover) 100%);
      color: white; transition: all 0.2s;
    }
    .btn-primary:hover { opacity: 0.9; }

    .btn-secondary {
      background: var(--admin-bg-input);
      color: var(--admin-text);
      border: 1px solid var(--admin-border);
      transition: all 0.2s;
    }
    .btn-secondary:hover { background: var(--admin-table-hover); }

    /* ===== Table ===== */
    .table-wrapper {
      background: var(--admin-bg-card);
      border: 1px solid var(--admin-border);
      border-radius: 12px;
      overflow: hidden;
      transition: background 0.3s;
    }

    .table-scroll { overflow-x: auto; }

    .data-table { width: 100%; border-collapse: collapse; }
    .data-table th {
      color: var(--admin-text-heading);
      border-bottom: 2px solid var(--admin-border);
      background: var(--admin-table-head-bg);
      padding: 12px 16px; text-align: left;
      font-size: 0.75rem; font-weight: 600; text-transform: uppercase;
      white-space: nowrap;
    }
    .data-table td {
      color: var(--admin-text);
      border-bottom: 1px solid var(--admin-border);
      padding: 12px 16px; font-size: 0.875rem;
    }
    .data-table tbody tr { transition: background 0.15s; }
    .data-table tbody tr:hover { background: var(--admin-table-hover); }
    .data-table tbody tr:last-child td { border-bottom: none; }

    /* ===== Badge ===== */
    .badge { display: inline-flex; align-items: center; padding: 2px 10px; border-radius: 9999px; font-size: 0.75rem; font-weight: 500; }
    .badge-success { background: rgba(16, 185, 129, 0.15); color: var(--brand-success); }
    .badge-warning { background: rgba(245, 158, 11, 0.15); color: var(--brand-warning); }
    .badge-danger { background: rgba(239, 68, 68, 0.15); color: var(--brand-danger); }

    /* ===== Page Button ===== */
    .page-btn {
      background: var(--admin-bg-input); color: var(--admin-text);
      border: 1px solid var(--admin-border);
    }
    .page-btn:hover { background: var(--admin-table-hover); }
    .page-btn.active { background: var(--brand-primary) !important; color: white; border-color: var(--brand-primary); }
    .page-btn:disabled { opacity: 0.3; cursor: not-allowed; }

    /* ===== Modal (detail) ===== */
    .modal-content { background: var(--admin-bg-modal); border: 1px solid var(--admin-border); }
    body.light-mode .modal-content { background: #ffffff; }

    @keyframes slideUp {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .animate-slide-up { animation: slideUp 0.3s ease-out; }

    @media (max-width: 768px) {
      body { padding: 16px; }
      .search-bar { flex-direction: column; align-items: stretch; }
    }
  </style>
</head>
<body>
  <!-- ===== 页面头部 ===== -->
  <div class="page-header">
    <div>
      <h1 style="color: var(--admin-text-heading);" class="text-2xl font-bold">用户管理</h1>
      <p style="color: var(--admin-text-muted);" class="text-sm mt-1">管理系统中的所有用户</p>
    </div>
    <div class="flex items-center gap-3">
      <button onclick="toggleTheme()" class="btn-secondary px-3 py-1.5 rounded-lg text-xs">
        切换主题
      </button>
      <button class="btn-primary px-4 py-2 rounded-lg text-sm font-medium">
        + 添加用户
      </button>
    </div>
  </div>

  <!-- ===== 搜索栏 ===== -->
  <div class="search-bar">
    <input type="text" id="searchInput" class="input-field px-3 py-2 rounded-lg text-sm w-full sm:w-64" placeholder="搜索姓名或邮箱...">
    <select id="statusFilter" class="input-field px-3 py-2 rounded-lg text-sm">
      <option value="">全部状态</option>
      <option value="active">活跃</option>
      <option value="pending">待激活</option>
      <option value="disabled">已禁用</option>
    </select>
    <button onclick="filterTable()" class="btn-primary px-4 py-2 rounded-lg text-sm">搜索</button>
  </div>

  <!-- ===== 表格 ===== -->
  <div class="table-wrapper">
    <div class="table-scroll">
      <table class="data-table" id="userTable">
        <thead>
          <tr>
            <th>姓名</th>
            <th>邮箱</th>
            <th>角色</th>
            <th>状态</th>
            <th>注册时间</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody id="tableBody">
          <!-- 由 JavaScript 渲染 -->
        </tbody>
      </table>
    </div>

    <!-- ===== 分页 ===== -->
    <div class="flex flex-col sm:flex-row items-center justify-between gap-4 px-6 py-4" style="border-top: 1px solid var(--admin-border);">
      <span style="color: var(--admin-text-muted);" class="text-sm" id="pageInfo">共 0 条记录</span>
      <div class="flex items-center gap-1" id="pagination">
        <!-- 由 JavaScript 渲染 -->
      </div>
    </div>
  </div>

  <!-- ===== 详情弹窗 ===== -->
  <div id="detailModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50" style="display: none;" onclick="if(event.target===this) closeDetail();">
    <div class="modal-content rounded-xl shadow-xl w-full max-w-lg mx-4 animate-slide-up">
      <div class="flex items-center justify-between px-6 py-4" style="border-bottom: 1px solid var(--admin-border);">
        <h3 style="color: var(--admin-text-heading);" class="text-lg font-semibold">用户详情</h3>
        <button onclick="closeDetail()" class="p-1 rounded-lg transition-colors" style="color: var(--admin-text-muted);">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </button>
      </div>
      <div class="p-6" id="detailContent">
        <!-- 由 JavaScript 填充 -->
      </div>
      <div class="flex justify-end px-6 py-4" style="border-top: 1px solid var(--admin-border);">
        <button onclick="closeDetail()" class="btn-secondary px-4 py-2 rounded-lg text-sm transition-colors">关闭</button>
      </div>
    </div>
  </div>

  <script>
    // ===== 模拟数据 =====
    var mockData = [
      { id: 1, name: '张小明', email: 'zhangxm@example.com', role: '管理员', status: 'active', date: '2024-01-15', avatar: 'ZX', bio: '系统管理员，负责日常运维。' },
      { id: 2, name: '李小红', email: 'lixh@example.com', role: '编辑', status: 'pending', date: '2024-01-14', avatar: 'LX', bio: '内容编辑，负责文章审核。' },
      { id: 3, name: '王大力', email: 'wangdl@example.com', role: '普通用户', status: 'active', date: '2024-01-13', avatar: 'WD', bio: '资深用户。' },
      { id: 4, name: '赵思涵', email: 'zhaosh@example.com', role: '编辑', status: 'disabled', date: '2024-01-10', avatar: 'ZS', bio: '内容编辑。' },
      { id: 5, name: '陈明辉', email: 'chenmh@example.com', role: '管理员', status: 'active', date: '2024-01-08', avatar: 'CM', bio: '超级管理员。' },
      { id: 6, name: '刘芳', email: 'liuf@example.com', role: '普通用户', status: 'active', date: '2024-01-05', avatar: 'LF', bio: '新注册用户。' }
    ];

    var currentPage = 1;
    var pageSize = 3;
    var filteredData = [];

    // ===== 过滤数据 =====
    function filterTable() {
      var keyword = document.getElementById('searchInput').value.toLowerCase();
      var status = document.getElementById('statusFilter').value;

      filteredData = mockData.filter(function(item) {
        var matchKeyword = !keyword || item.name.toLowerCase().includes(keyword) || item.email.toLowerCase().includes(keyword);
        var matchStatus = !status || item.status === status;
        return matchKeyword && matchStatus;
      });

      currentPage = 1;
      renderTable();
    }

    // ===== 渲染表格 =====
    function renderTable() {
      var start = (currentPage - 1) * pageSize;
      var end = start + pageSize;
      var pageData = filteredData.slice(start, end);
      var tbody = document.getElementById('tableBody');

      if (pageData.length === 0) {
        tbody.innerHTML = '<tr><td colspan="6" class="text-center py-12" style="color: var(--admin-text-muted);">暂无数据</td></tr>';
      } else {
        tbody.innerHTML = pageData.map(function(item) {
          var statusBadge = '';
          if (item.status === 'active') statusBadge = '<span class="badge badge-success"><span class="w-1.5 h-1.5 rounded-full bg-[var(--brand-success)] mr-1.5"></span>活跃</span>';
          else if (item.status === 'pending') statusBadge = '<span class="badge badge-warning"><span class="w-1.5 h-1.5 rounded-full bg-[var(--brand-warning)] mr-1.5"></span>待激活</span>';
          else statusBadge = '<span class="badge badge-danger"><span class="w-1.5 h-1.5 rounded-full bg-[var(--brand-danger)] mr-1.5"></span>已禁用</span>';

          return '<tr>' +
            '<td class="font-medium">' + item.name + '</td>' +
            '<td style="color: var(--admin-text-muted);">' + item.email + '</td>' +
            '<td>' + item.role + '</td>' +
            '<td>' + statusBadge + '</td>' +
            '<td style="color: var(--admin-text-muted);">' + item.date + '</td>' +
            '<td>' +
              '<button onclick="showDetail(' + item.id + ')" class="text-sm font-medium mr-3 hover:opacity-70" style="color: var(--brand-primary);">详情</button>' +
              '<button class="text-sm font-medium hover:opacity-70" style="color: var(--brand-danger);">删除</button>' +
            '</td>' +
          '</tr>';
        }).join('');
      }

      renderPagination();
    }

    // ===== 渲染分页 =====
    function renderPagination() {
      var total = filteredData.length;
      var totalPages = Math.ceil(total / pageSize) || 1;
      document.getElementById('pageInfo').textContent = '共 ' + total + ' 条记录，第 ' + currentPage + '/' + totalPages + ' 页';

      var html = '';
      html += '<button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors" onclick="goPage(' + (currentPage - 1) + ')" ' + (currentPage <= 1 ? 'disabled' : '') + '>' +
        '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>' +
      '</button>';

      for (var i = 1; i <= totalPages; i++) {
        html += '<button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors ' + (i === currentPage ? 'active' : '') + '" onclick="goPage(' + i + ')">' + i + '</button>';
      }

      html += '<button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors" onclick="goPage(' + (currentPage + 1) + ')" ' + (currentPage >= totalPages ? 'disabled' : '') + '>' +
        '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>' +
      '</button>';

      document.getElementById('pagination').innerHTML = html;
    }

    // ===== 翻页 =====
    function goPage(page) {
      var totalPages = Math.ceil(filteredData.length / pageSize) || 1;
      if (page < 1 || page > totalPages) return;
      currentPage = page;
      renderTable();
    }

    // ===== 详情弹窗 =====
    function showDetail(id) {
      var user = mockData.find(function(item) { return item.id === id; });
      if (!user) return;

      document.getElementById('detailContent').innerHTML =
        '<div class="flex items-center gap-4 mb-6">' +
          '<div class="w-16 h-16 rounded-full bg-gradient-to-br from-indigo-400 to-purple-500 flex items-center justify-center text-white text-xl font-bold">' + user.avatar + '</div>' +
          '<div>' +
            '<h4 style="color: var(--admin-text-heading);" class="text-lg font-semibold">' + user.name + '</h4>' +
            '<p style="color: var(--admin-text-muted);" class="text-sm">' + user.email + '</p>' +
          '</div>' +
        '</div>' +
        '<div class="grid grid-cols-2 gap-4 text-sm">' +
          '<div><span style="color: var(--admin-text-muted);">角色</span><p style="color: var(--admin-text);" class="font-medium mt-0.5">' + user.role + '</p></div>' +
          '<div><span style="color: var(--admin-text-muted);">注册时间</span><p style="color: var(--admin-text);" class="font-medium mt-0.5">' + user.date + '</p></div>' +
          '<div class="col-span-2"><span style="color: var(--admin-text-muted);">个人简介</span><p style="color: var(--admin-text);" class="font-medium mt-0.5">' + user.bio + '</p></div>' +
        '</div>';

      document.getElementById('detailModal').style.display = 'flex';
      document.body.style.overflow = 'hidden';
    }

    function closeDetail() {
      document.getElementById('detailModal').style.display = 'none';
      document.body.style.overflow = '';
    }

    // ESC 关闭弹窗
document.addEventListener('keydown', function(e) {
if (e.key === 'Escape') closeDetail();
});

    // ===== 主题切换 =====
    function toggleTheme() {
      document.body.classList.toggle('light-mode');
    }

    // ===== 初始化 =====
    filterTable();
  </script>
</body>
</html>
```

---

## 功能说明

| 功能 | 实现方式 |
|------|---------|
| 搜索筛选 | 按姓名/邮箱关键词 + 状态下拉框，实时过滤 |
| 数据表格 | 动态渲染，含状态徽章、操作按钮 |
| 分页 | 每页 3 条（可配置 `pageSize`），上下页按钮 |
| 详情弹窗 | 使用 `.modal-content` 类，头像+字段信息 |
| 主题切换 | `body.light-mode`，所有颜色走 CSS 变量 |

---

## 自定义

- **修改数据**：替换 `mockData` 数组
- **修改列**：调整 `<thead>` 的 th 和 `renderTable()` 中的 td 渲染
- **修改每页条数**：调整 `pageSize` 变量
- **嵌入布局**：将 `<body>` 内容放入布局的 `page-content` 中
