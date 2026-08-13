# Input Component

输入框组件模板。提供文本输入、邮箱、密码、下拉选择、文本域等变体，以及验证状态。

---

## 主题变量版 CSS

```css
.input-field {
  background: var(--admin-bg-input);
  color: var(--admin-text);
  border: 1px solid var(--admin-border);
}

.input-field:focus {
  outline: none;
  ring: 2px solid var(--brand-primary);
  border-color: var(--brand-primary);
}

.input-field::placeholder {
  color: var(--admin-text-muted);
}

.input-error {
  border-color: var(--brand-danger) !important;
}

.input-success {
  border-color: var(--brand-success) !important;
}

.input-label {
  color: var(--admin-text);
}

.input-helper {
  color: var(--admin-text-muted);
}
```

---

## 主题变量版 HTML

```html
<!-- 文本输入框 -->
<div class="space-y-1.5">
  <label class="input-label block text-sm font-medium">用户名</label>
  <input type="text" class="input-field w-full px-3 py-2 rounded-lg transition-colors duration-200" placeholder="请输入用户名">
</div>

<!-- 邮箱输入框 + 帮助文字 -->
<div class="space-y-1.5">
  <label class="input-label block text-sm font-medium">邮箱地址</label>
  <input type="email" class="input-field w-full px-3 py-2 rounded-lg transition-colors duration-200" placeholder="you@example.com">
  <p class="input-helper text-xs">请输入有效的邮箱地址</p>
</div>

<!-- 密码输入框（含显示/隐藏切换） -->
<div class="space-y-1.5">
  <label class="input-label block text-sm font-medium">密码</label>
  <div class="relative">
    <input id="password-input" type="password" class="input-field w-full px-3 py-2 pr-10 rounded-lg transition-colors duration-200" placeholder="至少8位字符">
    <button type="button" onclick="togglePassword()" class="absolute right-2 top-1/2 -translate-y-1/2 p-1" style="color: var(--admin-text-muted);">
      <svg id="eye-icon" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
      </svg>
    </button>
  </div>
</div>

<!-- 带错误状态的输入框 -->
<div class="space-y-1.5">
  <label class="input-label block text-sm font-medium">邮箱</label>
  <input type="email" class="input-field input-error w-full px-3 py-2 rounded-lg transition-colors duration-200" value="invalid-email" placeholder="you@example.com">
  <p style="color: var(--brand-danger);" class="text-xs">请输入有效的邮箱地址</p>
</div>

<!-- 带成功状态的输入框 -->
<div class="space-y-1.5">
  <label class="input-label block text-sm font-medium">用户名</label>
  <input type="text" class="input-field input-success w-full px-3 py-2 rounded-lg transition-colors duration-200" value="john_doe" placeholder="请输入用户名">
  <p style="color: var(--brand-success);" class="text-xs">用户名可用</p>
</div>

<!-- 下拉选择框 -->
<div class="space-y-1.5">
  <label class="input-label block text-sm font-medium">角色</label>
  <select class="input-field w-full px-3 py-2 rounded-lg transition-colors duration-200">
    <option value="">请选择</option>
    <option value="admin">管理员</option>
    <option value="user">普通用户</option>
  </select>
</div>

<!-- 文本域 -->
<div class="space-y-1.5">
  <label class="input-label block text-sm font-medium">描述</label>
  <textarea class="input-field w-full px-3 py-2 rounded-lg transition-colors duration-200" rows="4" placeholder="请输入描述..."></textarea>
</div>

<!-- 带前缀/后缀图标的输入框 -->
<div class="space-y-1.5">
  <label class="input-label block text-sm font-medium">搜索</label>
  <div class="relative">
    <svg class="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4" style="color: var(--admin-text-muted);" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
    </svg>
    <input type="text" class="input-field w-full pl-10 pr-3 py-2 rounded-lg transition-colors duration-200" placeholder="搜索...">
  </div>
</div>
```

---

## 硬编码版（单主题快速参考）

```html
<div class="space-y-1">
  <label class="block text-sm font-medium text-gray-700">邮箱</label>
  <input type="email" class="mt-1 block w-full rounded-lg border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 px-3 py-2" placeholder="you@example.com">
  <p class="mt-1 text-sm text-gray-500">帮助文字</p>
</div>

<div>
  <label class="block text-sm font-medium text-red-600">邮箱（错误）</label>
  <input type="email" required value="invalid" class="mt-1 block w-full rounded-lg border-red-300 text-red-900 placeholder-red-300 focus:border-red-500 focus:ring-red-500 px-3 py-2">
  <p class="mt-1 text-sm text-red-600">请输入有效的邮箱地址</p>
</div>
```

---

## 密码显示切换脚本

```javascript
function togglePassword() {
  var input = document.getElementById('password-input');
  var icon = document.getElementById('eye-icon');
  if (input.type === 'password') {
    input.type = 'text';
    // 切换到"闭眼"图标
    icon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"/>';
  } else {
    input.type = 'password';
    // 切换到"睁眼"图标
    icon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>';
  }
}
```

> **注意**：硬编码版仅适用于单主题/快速原型场景。多视图/明暗切换页面必须使用主题变量版。
