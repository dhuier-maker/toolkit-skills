# Table Component

表格组件模板。支持斑马纹行、排序指示器、操作列、空状态等。

> **强制**：必须使用主题变量版，禁止硬编码。

---

## 主题变量版 CSS

```css
.data-table { min-width: 100%; border-collapse: collapse; }

.data-table th {
  color: var(--admin-text-heading);
  border-bottom: 2px solid var(--admin-border);
  background: var(--admin-table-head-bg);
  padding: 12px 16px;
  text-align: left;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.data-table td {
  color: var(--admin-text);
  border-bottom: 1px solid var(--admin-border);
  padding: 12px 16px;
  font-size: 0.875rem;
}

.data-table tbody tr {
  transition: background 0.15s;
}

.data-table tbody tr:hover {
  background: var(--admin-table-hover);
}

/* 斑马纹行（可选） */
.data-table-striped tbody tr:nth-child(even) {
  background: var(--admin-table-stripe);
}

.data-table-striped tbody tr:nth-child(even):hover {
  background: var(--admin-table-hover);
}
```

---

## 主题变量版 HTML

```html
<!-- 基础表格 -->
<div style="overflow-x: auto;">
  <table class="data-table">
    <thead>
      <tr>
        <th>姓名</th>
        <th>邮箱</th>
        <th>角色</th>
        <th>状态</th>
        <th>操作</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="font-medium">张小明</td>
        <td style="color: var(--admin-text-muted);">zhangxm@example.com</td>
        <td>
          <span class="badge badge-info">管理员</span>
        </td>
        <td>
          <span class="badge badge-success">
            <span class="w-1.5 h-1.5 rounded-full bg-[var(--brand-success)] mr-1.5"></span>
            活跃
          </span>
        </td>
        <td>
          <div class="flex items-center gap-2">
            <button class="text-sm font-medium transition-colors hover:opacity-70" style="color: var(--brand-primary);">编辑</button>
            <button class="text-sm font-medium transition-colors hover:opacity-70" style="color: var(--brand-danger);">删除</button>
          </div>
        </td>
      </tr>
      <tr>
        <td class="font-medium">李小红</td>
        <td style="color: var(--admin-text-muted);">lixh@example.com</td>
        <td>
          <span class="badge badge-neutral">普通用户</span>
        </td>
        <td>
          <span class="badge badge-warning">
            <span class="w-1.5 h-1.5 rounded-full bg-[var(--brand-warning)] mr-1.5"></span>
            待激活
          </span>
        </td>
        <td>
          <div class="flex items-center gap-2">
            <button class="text-sm font-medium transition-colors hover:opacity-70" style="color: var(--brand-primary);">编辑</button>
            <button class="text-sm font-medium transition-colors hover:opacity-70" style="color: var(--brand-danger);">删除</button>
          </div>
        </td>
      </tr>
      <tr>
        <td class="font-medium">王大力</td>
        <td style="color: var(--admin-text-muted);">wangdl@example.com</td>
        <td>
          <span class="badge badge-info">编辑</span>
        </td>
        <td>
          <span class="badge badge-danger">
            <span class="w-1.5 h-1.5 rounded-full bg-[var(--brand-danger)] mr-1.5"></span>
            已禁用
          </span>
        </td>
        <td>
          <div class="flex items-center gap-2">
            <button class="text-sm font-medium transition-colors hover:opacity-70" style="color: var(--brand-primary);">编辑</button>
            <button class="text-sm font-medium transition-colors hover:opacity-70" style="color: var(--brand-danger);">删除</button>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
</div>

<!-- 空状态 -->
<div class="flex flex-col items-center justify-center py-16" style="color: var(--admin-text-muted);">
  <svg class="w-16 h-16 mb-4 opacity-30" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
  </svg>
  <p class="text-sm">暂无数据</p>
</div>

<!-- 带排序指示器的表头 -->
<table class="data-table">
  <thead>
    <tr>
      <th>
        <div class="flex items-center gap-1 cursor-pointer hover:opacity-80">
          姓名
          <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 24 24">
            <path d="M12 5l-7 7h14l-7-7z"/>
          </svg>
        </div>
      </th>
      <th>
        <div class="flex items-center gap-1 cursor-pointer hover:opacity-80">
          邮箱
          <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 24 24">
            <path d="M12 19l-7-7h14l-7 7z"/>
          </svg>
        </div>
      </th>
    </tr>
  </thead>
  <!-- ... -->
</table>
```

---

## 使用说明

1. 表格始终包裹在 `overflow-x: auto` 容器中，确保窄屏可横向滚动
2. 操作列保持在最右侧
3. 状态列使用 `badge` 组件展示
4. 文本截断使用 `truncate` 类 + `max-width`
5. 斑马纹行通过 `data-table-striped` 类控制，不是默认行为
