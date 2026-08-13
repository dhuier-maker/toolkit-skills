# Card Component

卡片组件模板。提供基础卡片、统计卡片、带图卡片、悬停效果等变体。

---

## 主题变量版 CSS

```css
.card {
  background: var(--admin-bg-card);
  border: 1px solid var(--admin-border);
}

.stat-card {
  background: var(--admin-bg-card);
  border: 1px solid var(--admin-border);
}
```

---

## 主题变量版 HTML

```html
<!-- 基础卡片 -->
<div class="card rounded-xl p-6 transition-all duration-200 hover:shadow-lg">
  <h3 style="color: var(--admin-text-heading);" class="text-lg font-semibold">卡片标题</h3>
  <p style="color: var(--admin-text-muted);" class="mt-2">卡片内容区域，可以放置任意文本或组件。</p>
</div>

<!-- 统计卡片 -->
<div class="stat-card rounded-xl p-6 transition-all duration-200 hover:-translate-y-1 hover:shadow-lg">
  <p style="color: var(--admin-text-muted);" class="text-sm font-medium">总用户数</p>
  <div class="flex items-baseline gap-2 mt-1">
    <p style="color: var(--admin-text-heading);" class="text-3xl font-bold">12,345</p>
    <span style="color: var(--brand-success);" class="text-sm font-medium">+12.5%</span>
  </div>
  <div class="mt-3 w-full h-1.5 rounded-full" style="background: var(--admin-border);">
    <div class="h-1.5 rounded-full" style="width: 75%; background: linear-gradient(90deg, var(--brand-primary), var(--brand-primary-hover));"></div>
  </div>
  <p style="color: var(--admin-text-muted);" class="text-xs mt-2">较上月增长 1,234 人</p>
</div>

<!-- 带图标的统计卡片 -->
<div class="stat-card rounded-xl p-6 flex items-start justify-between transition-all duration-200 hover:-translate-y-1">
  <div>
    <p style="color: var(--admin-text-muted);" class="text-sm font-medium">总收入</p>
    <p style="color: var(--admin-text-heading);" class="text-3xl font-bold mt-1">¥128,450</p>
    <span style="color: var(--brand-success);" class="text-xs font-medium">↑ 8.2% 较上月</span>
  </div>
  <div class="p-3 rounded-lg" style="background: rgba(37, 99, 235, 0.15); color: var(--brand-primary);">
    <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
    </svg>
  </div>
</div>

<!-- 带图片的卡片 -->
<div class="card rounded-xl overflow-hidden transition-all duration-200 hover:-translate-y-1 hover:shadow-lg">
  <div class="h-48 bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center text-white text-2xl font-bold">
    封面图
  </div>
  <div class="p-6">
    <div class="flex items-center gap-2 mb-2">
      <span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium" style="background: rgba(37, 99, 235, 0.15); color: var(--brand-primary);">
        标签
      </span>
      <span style="color: var(--admin-text-muted);" class="text-xs">2024-01-15</span>
    </div>
    <h3 style="color: var(--admin-text-heading);" class="text-lg font-semibold">卡片标题</h3>
    <p style="color: var(--admin-text-muted);" class="mt-2 text-sm">卡片描述内容...</p>
    <div class="flex items-center justify-between mt-4">
      <div class="flex items-center gap-2">
        <div class="w-8 h-8 rounded-full bg-gradient-to-br from-indigo-400 to-purple-500"></div>
        <span style="color: var(--admin-text);" class="text-sm font-medium">作者</span>
      </div>
      <button class="text-sm font-medium transition-colors" style="color: var(--brand-primary);">查看详情 →</button>
    </div>
  </div>
</div>

<!-- 水平布局卡片（列表项风格） -->
<div class="card rounded-xl p-4 flex items-center gap-4 transition-all duration-200 hover:bg-[var(--admin-table-hover)] cursor-pointer">
  <div class="w-12 h-12 rounded-lg bg-gradient-to-br from-indigo-400 to-purple-500 flex items-center justify-center text-white font-bold flex-shrink-0">
    JD
  </div>
  <div class="flex-1 min-w-0">
    <p style="color: var(--admin-text);" class="text-sm font-medium truncate">John Doe</p>
    <p style="color: var(--admin-text-muted);" class="text-xs truncate">john@example.com</p>
  </div>
  <span style="color: var(--admin-text-muted);" class="text-xs flex-shrink-0">在线</span>
</div>
```

---

## 硬编码版（单主题快速参考）

```html
<div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6 hover:shadow-md transition-all duration-200">
  <h3 class="text-lg font-semibold text-gray-900">卡片标题</h3>
  <p class="mt-2 text-gray-600">卡片内容</p>
</div>

<div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6 transition-all duration-200 hover:-translate-y-1 hover:shadow-lg">
  <p class="text-sm text-gray-500">统计标签</p>
  <p class="text-2xl font-bold text-gray-900 mt-1">12,345</p>
  <span class="text-sm text-green-600">↑ 12.5%</span>
</div>
```

> **注意**：统计卡片的趋势箭头（↑↓）使用辅助色（`var(--brand-success)` 绿色、`var(--brand-danger)` 红色），不要硬编码。
