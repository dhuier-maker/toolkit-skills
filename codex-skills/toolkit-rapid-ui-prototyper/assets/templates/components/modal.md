# Modal Component

弹窗/模态框组件模板。提供基础弹窗、确认弹窗、表单弹窗等变体。

> **强制规则**：弹窗背景禁止内联写死，必须使用 `.modal-content` 主题类。弹窗的打开/关闭使用 JavaScript 控制 `display` 属性。

---

## 主题变量版 CSS

```css
.modal-content {
  background: var(--admin-bg-modal);
  border: 1px solid var(--admin-border);
}

body.light-mode .modal-content {
  background: #ffffff;
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-slide-up {
  animation: slideUp 0.3s ease-out;
}
```

---

## 基础弹窗

```html
<!-- 弹窗遮罩 -->
<div id="myModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50" style="display: none;" onclick="if(event.target===this) closeModal('myModal');">
  <!-- 弹窗内容 — 必须使用 modal-content 类 -->
  <div class="modal-content rounded-xl shadow-xl w-full max-w-md mx-4 overflow-hidden animate-slide-up">
    <!-- 标题栏 -->
    <div class="flex items-center justify-between px-6 py-4" style="border-bottom: 1px solid var(--admin-border);">
      <h3 style="color: var(--admin-text-heading);" class="text-lg font-semibold">弹窗标题</h3>
      <button onclick="closeModal('myModal')" class="p-1 rounded-lg transition-colors hover:bg-[var(--admin-table-hover)]" style="color: var(--admin-text-muted);">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
        </svg>
      </button>
    </div>

    <!-- 内容区 -->
    <div class="p-6" style="color: var(--admin-text);">
      <p>弹窗内容区域，可以放置任意文本、表单或组件。</p>
    </div>

    <!-- 底部操作栏 -->
    <div class="flex justify-end gap-3 px-6 py-4" style="border-top: 1px solid var(--admin-border);">
      <button onclick="closeModal('myModal')" class="btn-secondary px-4 py-2 rounded-lg text-sm transition-colors">取消</button>
      <button class="btn-primary px-4 py-2 rounded-lg text-sm transition-all hover:opacity-90">确认</button>
    </div>
  </div>
</div>

<!-- 触发按钮 -->
<button onclick="openModal('myModal')" class="btn-primary px-4 py-2 rounded-lg text-sm font-medium">打开弹窗</button>
```

---

## 确认弹窗（无标题栏）

```html
<div id="confirmModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50" style="display: none;" onclick="if(event.target===this) closeModal('confirmModal');">
  <div class="modal-content rounded-xl shadow-xl w-full max-w-sm mx-4 p-6 animate-slide-up">
    <div class="flex flex-col items-center text-center">
      <div class="w-12 h-12 rounded-full flex items-center justify-center mb-4" style="background: rgba(239, 68, 68, 0.15); color: var(--brand-danger);">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4.5c-.77-.833-1.964-.833-2.732 0L4.082 16.5c-.77.833.192 2.5 1.732 2.5z"/>
        </svg>
      </div>
      <h3 style="color: var(--admin-text-heading);" class="text-lg font-semibold">确认删除</h3>
      <p style="color: var(--admin-text-muted);" class="mt-2 text-sm">此操作不可撤销，确定要删除这条记录吗？</p>
      <div class="flex gap-3 mt-6 w-full">
        <button onclick="closeModal('confirmModal')" class="btn-secondary flex-1 px-4 py-2 rounded-lg text-sm transition-colors">取消</button>
        <button class="btn-danger flex-1 px-4 py-2 rounded-lg text-sm transition-all hover:opacity-90">确认删除</button>
      </div>
    </div>
  </div>
</div>
```

---

## 表单弹窗

```html
<div id="formModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50" style="display: none;" onclick="if(event.target===this) closeModal('formModal');">
  <div class="modal-content rounded-xl shadow-xl w-full max-w-lg mx-4 overflow-hidden animate-slide-up">
    <div class="flex items-center justify-between px-6 py-4" style="border-bottom: 1px solid var(--admin-border);">
      <h3 style="color: var(--admin-text-heading);" class="text-lg font-semibold">编辑用户</h3>
      <button onclick="closeModal('formModal')" class="p-1 rounded-lg transition-colors" style="color: var(--admin-text-muted);">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
        </svg>
      </button>
    </div>
    <div class="p-6 space-y-4">
      <div class="space-y-1.5">
        <label style="color: var(--admin-text);" class="block text-sm font-medium">姓名</label>
        <input type="text" class="input-field w-full px-3 py-2 rounded-lg transition-colors" placeholder="请输入姓名">
      </div>
      <div class="space-y-1.5">
        <label style="color: var(--admin-text);" class="block text-sm font-medium">邮箱</label>
        <input type="email" class="input-field w-full px-3 py-2 rounded-lg transition-colors" placeholder="you@example.com">
      </div>
      <div class="space-y-1.5">
        <label style="color: var(--admin-text);" class="block text-sm font-medium">角色</label>
        <select class="input-field w-full px-3 py-2 rounded-lg transition-colors">
          <option>管理员</option>
          <option>普通用户</option>
        </select>
      </div>
    </div>
    <div class="flex justify-end gap-3 px-6 py-4" style="border-top: 1px solid var(--admin-border);">
      <button onclick="closeModal('formModal')" class="btn-secondary px-4 py-2 rounded-lg text-sm transition-colors">取消</button>
      <button class="btn-primary px-4 py-2 rounded-lg text-sm transition-all hover:opacity-90">保存</button>
    </div>
  </div>
</div>
```

---

## JavaScript 控制脚本

```javascript
// 打开弹窗
function openModal(id) {
  document.getElementById(id).style.display = 'flex';
  // 可选：禁止页面滚动
  document.body.style.overflow = 'hidden';
}

// 关闭弹窗
function closeModal(id) {
  document.getElementById(id).style.display = 'none';
  // 恢复页面滚动
  document.body.style.overflow = '';
}

// ESC 键关闭
 document.addEventListener('keydown', function(e) {
   if (e.key === 'Escape') {
     document.querySelectorAll('[id$="Modal"]').forEach(function(el) {
       if (el.style.display === 'flex') {
         el.style.display = 'none';
       }
     });
     document.body.style.overflow = '';
   }
 });
```

---

## 关键规则

1. 遮罩使用 `bg-black/50`（Tailwind 半透明黑，不受主题影响）
2. **弹窗内容必须使用 `class="modal-content"`**，禁止内联 `style="background: ..."`
3. 点击遮罩关闭弹窗：`onclick="if(event.target===this) closeModal(...)"`
4. 弹窗打开时禁止页面滚动：`document.body.style.overflow = 'hidden'`
5. ESC 键关闭弹窗需监听全局 keyboard 事件
