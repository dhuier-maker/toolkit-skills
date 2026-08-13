# Pagination Component

分页组件模板。支持页码导航、上下页、跳转输入、总记录数显示。

> **强制**：必须使用主题变量版，禁止硬编码。

---

## 主题变量版 CSS

```css
.page-btn {
  background: var(--admin-bg-input);
  color: var(--admin-text);
  border: 1px solid var(--admin-border);
}

.page-btn:hover {
  background: var(--admin-table-hover);
}

.page-btn.active,
.page-btn.active:hover {
  background: var(--brand-primary) !important;
  color: white;
  border-color: var(--brand-primary);
}

.page-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.page-size-select {
  background: var(--admin-bg-input);
  color: var(--admin-text);
  border: 1px solid var(--admin-border);
}
```

---

## 基础分页

```html
<div class="flex flex-col sm:flex-row items-center justify-between gap-4 mt-6">
  <!-- 左侧：总记录数 -->
  <span style="color: var(--admin-text-muted);" class="text-sm">
    共 <strong style="color: var(--admin-text);">156</strong> 条记录
  </span>

  <!-- 右侧：分页按钮 -->
  <div class="flex items-center gap-1">
    <!-- 上一页 -->
    <button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors disabled:opacity-30 disabled:cursor-not-allowed" disabled>
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
      </svg>
    </button>

    <!-- 页码 -->
    <button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors active">1</button>
    <button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors">2</button>
    <button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors">3</button>
    <button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors">4</button>
    <button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors">5</button>

    <!-- 省略号 -->
    <span style="color: var(--admin-text-muted);" class="px-1 text-sm">...</span>

    <!-- 最后一页 -->
    <button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors">16</button>

    <!-- 下一页 -->
    <button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
      </svg>
    </button>
  </div>
</div>
```

---

## 完整分页（含跳转和每页条数）

```html
<div class="flex flex-col sm:flex-row items-center justify-between gap-4 mt-6">
  <!-- 左侧：每页条数 -->
  <div class="flex items-center gap-2">
    <span style="color: var(--admin-text-muted);" class="text-sm">每页</span>
    <select class="page-size-select px-2 py-1 rounded-lg text-sm">
      <option>10</option>
      <option selected>20</option>
      <option>50</option>
      <option>100</option>
    </select>
    <span style="color: var(--admin-text-muted);" class="text-sm">条</span>
    <span style="color: var(--admin-text-muted);" class="text-sm ml-4">
      共 156 条，第 1/16 页
    </span>
  </div>

  <!-- 中间：页码 -->
  <div class="flex items-center gap-1">
    <button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors disabled:opacity-30 disabled:cursor-not-allowed" disabled title="上一页">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
      </svg>
    </button>
    <button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors active">1</button>
    <button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors">2</button>
    <button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors">3</button>
    <span style="color: var(--admin-text-muted);" class="px-1 text-sm">...</span>
    <button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors">16</button>
    <button class="page-btn w-8 h-8 rounded-lg flex items-center justify-center transition-colors" title="下一页">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
      </svg>
    </button>
  </div>

  <!-- 右侧：跳转 -->
  <div class="flex items-center gap-2">
    <span style="color: var(--admin-text-muted);" class="text-sm">跳至</span>
    <input type="number" min="1" max="16" value="1"
      class="page-btn w-16 px-2 py-1 rounded-lg text-sm text-center"
      onkeydown="if(event.key==='Enter') goToPage(this.value)">
    <span style="color: var(--admin-text-muted);" class="text-sm">页</span>
  </div>
</div>
```

---

## JavaScript 交互

```javascript
var currentPage = 1;
var totalPages = 16;

function goToPage(page) {
  page = parseInt(page);
  if (isNaN(page) || page < 1 || page > totalPages) return;
  currentPage = page;
  renderPagination();
  // 触发数据加载
  loadPageData(page);
}

function renderPagination() {
  // 更新所有页码按钮的 active 状态
  document.querySelectorAll('.page-btn').forEach(function(btn) {
    if (btn.textContent.trim() === String(currentPage)) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });
  // 更新上下页禁用状态
  var prevBtn = document.querySelector('.page-btn:first-child');
  var nextBtn = document.querySelector('.page-btn:last-child');
  if (prevBtn) prevBtn.disabled = currentPage <= 1;
  if (nextBtn) nextBtn.disabled = currentPage >= totalPages;
}

function loadPageData(page) {
  // TODO: 发送 AJAX 请求加载第 page 页的数据
  console.log('Loading page', page);
}
```

---

## 关键规则

1. 上一页/下一页使用 SVG 左右箭头图标（`M15 19l-7-7 7-7` / `M9 5l7 7-7 7`）
2. 当前页码使用 `class="page-btn active"`，背景色使用 `var(--brand-primary)`
3. 超过 7 页显示省略号（`...`）
4. 第一页时上一页按钮 `disabled`，最后一页时下一页按钮 `disabled`
5. 跳转输入框监听 Enter 键触发跳转
6. 分页组件通常位于表格下方
