# Badge Component

徽章/标签组件模板。用于状态标识、分类标签、计数标记等。

---

## 主题变量版 CSS

```css
.badge {
  display: inline-flex;
  align-items: center;
  padding: 2px 10px;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 500;
  line-height: 1.25rem;
}

.badge-success { background: rgba(16, 185, 129, 0.15); color: var(--brand-success); }
.badge-warning { background: rgba(245, 158, 11, 0.15); color: var(--brand-warning); }
.badge-danger { background: rgba(239, 68, 68, 0.15); color: var(--brand-danger); }
.badge-info { background: rgba(59, 130, 246, 0.15); color: var(--brand-info); }
.badge-neutral { background: var(--admin-table-hover); color: var(--admin-text-muted); }
```

---

## 主题变量版 HTML

```html
<!-- 成功状态 -->
<span class="badge badge-success">
  <span class="w-1.5 h-1.5 rounded-full bg-[var(--brand-success)] mr-1.5"></span>
  已启用
</span>

<!-- 警告状态 -->
<span class="badge badge-warning">
  <span class="w-1.5 h-1.5 rounded-full bg-[var(--brand-warning)] mr-1.5"></span>
  待审核
</span>

<!-- 危险状态 -->
<span class="badge badge-danger">
  <span class="w-1.5 h-1.5 rounded-full bg-[var(--brand-danger)] mr-1.5"></span>
  已禁用
</span>

<!-- 信息状态 -->
<span class="badge badge-info">
  <span class="w-1.5 h-1.5 rounded-full bg-[var(--brand-info)] mr-1.5"></span>
  进行中
</span>

<!-- 中性状态 -->
<span class="badge badge-neutral">
  草稿
</span>

<!-- 纯色徽章（实心背景） -->
<span style="background: var(--brand-success); color: white;" class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium">
  通过
</span>

<span style="background: var(--brand-danger); color: white;" class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium">
  拒绝
</span>

<!-- 数字徽章（用于通知计数） -->
<span class="inline-flex items-center justify-center min-w-[20px] h-5 px-1.5 rounded-full text-xs font-bold"
  style="background: var(--brand-danger); color: white;">
  3
</span>

<!-- 带关闭按钮的标签 -->
<span class="inline-flex items-center gap-1 px-3 py-1 rounded-full text-xs font-medium"
  style="background: rgba(37, 99, 235, 0.15); color: var(--brand-primary);">
  Vue
  <button class="hover:opacity-70">
    <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
      <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"/>
    </svg>
  </button>
</span>

<!-- 大小变体 -->
<span class="badge badge-success text-[0.625rem]">小</span>
<span class="badge badge-success">中</span>
<span class="badge badge-success text-sm">大</span>
```

---

## 硬编码版（单主题快速参考）

```html
<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800">Active</span>
<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800">Pending</span>
<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800">Inactive</span>
<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">Info</span>
<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800">Draft</span>
```

> **注意**：状态点（小圆点）使用 `w-1.5 h-1.5 rounded-full bg-[var(--brand-*)]`，配合 `mr-1.5` 间距与文字区分。
