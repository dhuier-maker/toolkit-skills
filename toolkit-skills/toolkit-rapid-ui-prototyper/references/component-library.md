# Component Library

Tailwind CSS 组件模板参考，按需使用。

> **主题系统约定**：多视图/多主题页面中，所有颜色必须走 CSS 变量（`var(--admin-*)`），禁止在组件 CSS 类或内联样式中硬编码颜色值。主题切换使用 `body.light-mode` class，禁止使用 Tailwind `dark:` 前缀。

---

## Button（按钮）

### 硬编码版（单主题/无主题切换）

```html
<!-- Primary Button -->
<button class="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed">
  Primary
</button>

<!-- Secondary Button -->
<button class="px-4 py-2 bg-white text-gray-700 border border-gray-300 rounded-lg hover:bg-gray-50">
  Secondary
</button>

<!-- Ghost Button -->
<button class="px-4 py-2 text-gray-600 hover:bg-gray-100 rounded-lg">
  Ghost
</button>

<!-- Icon Button -->
<button class="p-2 text-gray-500 hover:bg-gray-100 rounded-full">
  <svg class="w-5 h-5">...</svg>
</button>
```

### 主题变量版（多主题/明暗切换）

```html
<!-- Primary Button — 使用品牌色变量 -->
<button class="btn-primary px-4 py-2 rounded-lg text-sm font-medium transition-all duration-200 hover:opacity-90 active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed">
  Primary
</button>

<!-- Secondary Button — 使用管理后台变量 -->
<button class="btn-secondary px-4 py-2 rounded-lg text-sm transition-colors duration-200 hover:brightness-110">
  Secondary
</button>
```

```css
.btn-primary { background: linear-gradient(135deg, var(--brand-primary) 0%, var(--brand-primary-hover) 100%); color: white; }
.btn-secondary { background: var(--admin-bg-input); color: var(--admin-text); border: 1px solid var(--admin-border); }
```

---

## Input（输入框）

### 主题变量版

```html
<div class="space-y-1">
  <label style="color: var(--admin-text);" class="block text-sm font-medium">Email</label>
  <input type="email" class="input-field w-full px-3 py-2 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-colors duration-200" placeholder="you@example.com">
  <p style="color: var(--admin-text-muted);" class="text-sm">We'll never share your email.</p>
</div>
```

```css
.input-field { background: var(--admin-bg-input); color: var(--admin-text); border: 1px solid var(--admin-border); }
```

---

## Card（卡片）

### 硬编码版

```html
<div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow">
  <h3 class="text-lg font-semibold text-gray-900">Card Title</h3>
  <p class="mt-2 text-gray-600">Card content goes here.</p>
</div>
```

### 主题变量版

```html
<div class="card rounded-xl p-6 hover:shadow-md transition-shadow">
  <h3 style="color: var(--admin-text-heading);" class="text-lg font-semibold">Card Title</h3>
  <p style="color: var(--admin-text-muted);" class="mt-2">Card content goes here.</p>
</div>
```

```css
.card { background: var(--admin-bg-card); border: 1px solid var(--admin-border); }
```

---

## Badge（徽章）

```html
<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800">
  Active
</span>
```

---

## Table（表格）

### 主题变量版

```html
<table class="data-table min-w-full">
  <thead>
    <tr style="background: var(--admin-table-head-bg);">
      <th class="px-6 py-3 text-left text-xs font-medium uppercase">Name</th>
      <th class="px-6 py-3 text-left text-xs font-medium uppercase">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr class="transition-colors duration-150" style="border-bottom: 1px solid var(--admin-border);">
      <td class="px-6 py-4">John Doe</td>
      <td><span class="badge-active">Active</span></td>
    </tr>
  </tbody>
</table>
```

```css
.data-table th { color: var(--admin-text-heading); border-bottom: 1px solid var(--admin-border); }
.data-table td { color: var(--admin-text); border-bottom: 1px solid var(--admin-border); }
```

---

## Modal（弹窗）⚠️ 必须使用主题类

弹窗背景**禁止内联写死**，必须使用 `.modal-content` 类：

```html
<!-- 弹窗遮罩 -->
<div id="myModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50" style="display: none;">
  <!-- 弹窗内容 — 使用 modal-content 类 -->
  <div class="modal-content rounded-xl shadow-xl w-full max-w-md mx-4 overflow-hidden animate-slide-up">
    <div class="flex items-center justify-between px-6 py-4" style="border-bottom: 1px solid var(--admin-border);">
      <h3 style="color: var(--admin-text-heading);" class="text-lg font-semibold">弹窗标题</h3>
      <button onclick="closeModal('myModal')" class="p-1 rounded-lg transition-colors" style="color: var(--admin-text-muted);">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
      </button>
    </div>
    <div class="p-6" style="color: var(--admin-text);">
      弹窗内容区域
    </div>
    <div class="flex justify-end gap-3 px-6 py-4" style="border-top: 1px solid var(--admin-border);">
      <button onclick="closeModal('myModal')" class="btn-secondary px-4 py-2 rounded-lg text-sm transition-colors">取消</button>
      <button class="btn-primary px-4 py-2 rounded-lg text-sm transition-all">确认</button>
    </div>
  </div>
</div>
```

```css
.modal-content { background: var(--admin-bg-modal); border: 1px solid var(--admin-border); }
body.light-mode .modal-content { background: #ffffff; }
```

```javascript
function openModal(id) { document.getElementById(id).style.display = 'flex'; }
function closeModal(id) { document.getElementById(id).style.display = 'none'; }
```

---

## Pagination（分页）⚠️ 必须使用主题类

```html
<div class="flex items-center justify-between mt-6">
  <span style="color: var(--admin-text-muted);" class="text-sm">共 156 条记录</span>
  <div class="flex items-center gap-1">
    <button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors disabled:opacity-30 disabled:cursor-not-allowed" disabled>
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
    </button>
    <button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors" style="background: var(--brand-primary); color: white;">1</button>
    <button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors">2</button>
    <button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors">3</button>
    <button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
    </button>
  </div>
</div>
```

```css
.page-btn { background: var(--admin-bg-input); color: var(--admin-text); border: 1px solid var(--admin-border); }
.page-btn:hover { background: var(--admin-table-hover); }
.page-btn.active { background: var(--brand-primary); color: white; border-color: var(--brand-primary); }
```

---

## Admin Dashboard（管理后台）

### 主题变量版（明暗切换）

```html
<div class="flex h-screen overflow-hidden">
  <!-- Sidebar -->
  <aside style="background: var(--admin-sidebar-bg); border-right: 1px solid var(--admin-border);">
    <nav class="p-4 space-y-1">
      <a href="#" class="sidebar-item active flex items-center px-4 py-2 rounded-lg transition-colors">
        <svg class="w-5 h-5 mr-3">...</svg>
        Dashboard
      </a>
    </nav>
  </aside>

  <!-- Main Content -->
  <main style="background: var(--admin-bg);" class="flex-1 overflow-auto">
    <header style="background: var(--admin-header-bg); border-bottom: 1px solid var(--admin-border);" class="sticky top-0 z-10 px-6 py-4">
      <h1 style="color: var(--admin-text-heading);" class="text-xl font-semibold">Dashboard</h1>
    </header>

    <div class="p-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <div class="stat-card rounded-xl p-6 transition-all duration-200 hover:-translate-y-1">
        <p style="color: var(--admin-text-muted);" class="text-sm">Total Revenue</p>
        <p style="color: var(--admin-text-heading);" class="text-2xl font-bold">$54,239</p>
        <span class="text-sm text-green-500">+12.5%</span>
      </div>
    </div>
  </main>
</div>
```

```css
.stat-card { background: var(--admin-bg-card); border: 1px solid var(--admin-border); }
.sidebar-item { color: var(--admin-text-muted); }
.sidebar-item:hover { background: var(--admin-table-hover); color: var(--admin-text); }
.sidebar-item.active { background-color: rgba(37, 99, 235, 0.1); color: var(--brand-primary); border-right: 3px solid var(--brand-primary); }
```

---

## Form with Validation（带验证的表单）

```html
<form class="space-y-4 max-w-md">
  <div>
    <label class="block text-sm font-medium text-gray-700">Email</label>
    <input type="email" required class="mt-1 block w-full rounded-lg border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500">
  </div>

  <div>
    <label class="block text-sm font-medium text-gray-700">Password</label>
    <input type="password" required minlength="8" class="mt-1 block w-full rounded-lg border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500">
    <p class="mt-1 text-sm text-gray-500">At least 8 characters</p>
  </div>

  <button type="submit" class="w-full flex justify-center py-2 px-4 border border-transparent rounded-lg shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700">
    Sign in
  </button>
</form>
```

---

## Mobile-First Patterns（移动端模式）

### 主题变量版

```html
<!-- 移动端页面容器 -->
<div class="mobile-view min-h-screen">
  <!-- 移动端头部 -->
  <header class="mobile-header sticky top-0 z-10 px-4 py-3 flex items-center justify-between">
    <h1 style="color: var(--mobile-text-heading);" class="text-lg font-semibold">Title</h1>
  </header>

  <!-- 卡片列表 -->
  <div class="space-y-3 p-4">
    <div class="mobile-card rounded-lg p-4 flex items-center space-x-3">
      <div class="w-12 h-12 rounded-full bg-gradient-to-br from-indigo-400 to-purple-500"></div>
      <div class="flex-1 min-w-0">
        <p style="color: var(--admin-text);" class="text-sm font-medium truncate">User Name</p>
        <p style="color: var(--admin-text-muted);" class="text-xs truncate">Last message...</p>
      </div>
    </div>
  </div>

  <!-- 底部导航 -->
  <nav class="mobile-tab-bar fixed bottom-0 left-0 right-0 px-4 py-2 flex justify-around">
    <a href="#" class="flex flex-col items-center" style="color: var(--brand-primary);">
      <svg class="w-6 h-6">...</svg>
      <span class="text-xs mt-1">Home</span>
    </a>
    <a href="#" class="flex flex-col items-center" style="color: var(--admin-text-muted);">
      <svg class="w-6 h-6">...</svg>
      <span class="text-xs mt-1">Search</span>
    </a>
  </nav>
</div>
```

```css
.mobile-view { background: var(--mobile-bg); }
.mobile-header { background: var(--mobile-header-bg); border-bottom: 1px solid var(--admin-border); }
.mobile-card { background: var(--mobile-card-bg); border: 1px solid var(--admin-border); }
.mobile-tab-bar { background: var(--mobile-header-bg); border-top: 1px solid var(--admin-border); }
```
