# 动画规范

使用 Tailwind CSS 动画类或自定义 CSS 实现过渡效果。

## 预定义动画

| 动画名称 | Tailwind 类 | 适用场景 |
|----------|-------------|----------|
| fadeIn | `animate-fade-in` | 元素出现 |
| slideUp | `animate-slide-up` | 列表项、弹窗 |
| slideDown | `animate-slide-down` | 下拉菜单 |
| spin | `animate-spin` | Loading spinner |
| pulse | `animate-pulse` | 强调、等待 |
| bounce | `animate-bounce` | 提醒、欢呼 |

## 自定义动画（添加到 CSS 中）

```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes slideDown {
  from { opacity: 0; transform: translateY(-20px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-fade-in { animation: fadeIn 0.3s ease-out; }
.animate-slide-up { animation: slideUp 0.3s ease-out; }
.animate-slide-down { animation: slideDown 0.3s ease-out; }
```

## 过渡效果

使用 `transition-*` 类实现状态变化的平滑过渡：

```html
<!-- 按钮过渡 -->
<button class="px-4 py-2 bg-indigo-600 text-white rounded-lg transition-all duration-300 hover:bg-indigo-700 hover:scale-105">
  悬停放大
</button>

<!-- 卡片悬停 -->
<div class="bg-white rounded-xl shadow-sm p-6 transition-all duration-300 hover:shadow-lg hover:-translate-y-1">
  悬停上浮
</div>

<!-- 颜色过渡 -->
<div class="transition-colors duration-300" style="background: var(--admin-bg-card); color: var(--admin-text);">
  主题切换时平滑过渡（使用 CSS 变量，自然跟随主题变化）
</div>
```
