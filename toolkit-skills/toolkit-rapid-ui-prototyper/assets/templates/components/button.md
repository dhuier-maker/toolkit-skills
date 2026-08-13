# Button Component

按钮组件模板。提供主按钮、次按钮、幽灵按钮、图标按钮、加载按钮等变体。

---

## 主题变量版 CSS

```css
.btn-primary {
  background: linear-gradient(135deg, var(--brand-primary) 0%, var(--brand-primary-hover) 100%);
  color: white;
}

.btn-secondary {
  background: var(--admin-bg-input);
  color: var(--admin-text);
  border: 1px solid var(--admin-border);
}

.btn-ghost {
  background: transparent;
  color: var(--admin-text-muted);
  border: 1px solid transparent;
}

.btn-ghost:hover {
  background: var(--admin-table-hover);
  color: var(--admin-text);
}

.btn-danger {
  background: var(--brand-danger);
  color: white;
}

.btn-sm { padding: 6px 12px; font-size: 0.75rem; }
.btn-md { padding: 8px 16px; font-size: 0.875rem; }
.btn-lg { padding: 12px 24px; font-size: 1rem; }
```

---

## 主题变量版 HTML

```html
<!-- Primary Button（主按钮） -->
<button class="btn-primary btn-md rounded-lg font-medium transition-all duration-200 hover:opacity-90 active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed">
  主操作
</button>

<!-- Secondary Button（次按钮） -->
<button class="btn-secondary btn-md rounded-lg font-medium transition-colors duration-200 hover:brightness-110">
  次操作
</button>

<!-- Ghost Button（幽灵按钮） -->
<button class="btn-ghost btn-md rounded-lg font-medium transition-colors duration-200">
  取消
</button>

<!-- Danger Button（危险按钮） -->
<button class="btn-danger btn-md rounded-lg font-medium transition-all duration-200 hover:opacity-90">
  删除
</button>

<!-- Icon Button（图标按钮） -->
<button class="p-2 rounded-lg transition-colors duration-200"
  style="color: var(--admin-text-muted); background: var(--admin-bg-input); border: 1px solid var(--admin-border);">
  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
  </svg>
</button>

<!-- Link Button（链接按钮） -->
<button class="btn-md font-medium transition-colors duration-200"
  style="color: var(--brand-primary); background: none; border: none; cursor: pointer;">
  链接操作
</button>

<!-- Loading Button（加载按钮） -->
<button class="btn-primary btn-md rounded-lg font-medium transition-all duration-200 disabled:opacity-70" disabled>
  <svg class="animate-spin -ml-1 mr-2 h-4 w-4 inline" fill="none" viewBox="0 0 24 24">
    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/>
    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"/>
  </svg>
  处理中...
</button>

<!-- 按钮组 -->
<div class="inline-flex rounded-lg overflow-hidden" style="border: 1px solid var(--admin-border);">
  <button class="px-4 py-2 text-sm font-medium transition-colors" style="background: var(--brand-primary); color: white;">
    日
  </button>
  <button class="px-4 py-2 text-sm font-medium transition-colors" style="background: var(--admin-bg-input); color: var(--admin-text);">
    周
  </button>
  <button class="px-4 py-2 text-sm font-medium transition-colors" style="background: var(--admin-bg-input); color: var(--admin-text);">
    月
  </button>
</div>
```

---

## 硬编码版（单主题快速参考）

```html
<!-- Primary -->
<button class="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200">
  Primary
</button>

<!-- Secondary -->
<button class="px-4 py-2 bg-white text-gray-700 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors duration-200">
  Secondary
</button>

<!-- Ghost -->
<button class="px-4 py-2 text-gray-600 hover:bg-gray-100 rounded-lg transition-colors duration-200">
  Cancel
</button>

<!-- Danger -->
<button class="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors duration-200">
  Delete
</button>

<!-- Disabled -->
<button disabled class="px-4 py-2 bg-gray-300 text-gray-500 rounded-lg cursor-not-allowed">
  Disabled
</button>
```
