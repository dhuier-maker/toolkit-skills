# Form Page Template

表单页面模板。包含多字段表单、字段验证、提交处理。可嵌入到顶部导航或侧边栏布局中使用。

> 本模板的验证逻辑从 `references/component-library.md` 的 Form with Validation 提取并扩展为完整页面。

---

## 完整 HTML

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>表单 - Admin</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --brand-primary: #2563eb;
      --brand-primary-hover: #1d4ed8;
      --brand-success: #10b981;
      --brand-danger: #ef4444;

      --admin-bg: #060b14;
      --admin-bg-card: rgba(12, 21, 36, 0.8);
      --admin-bg-input: rgba(12, 21, 36, 0.6);
      --admin-text: #e2e8f0;
      --admin-text-heading: #e8d48b;
      --admin-text-muted: #94a3b8;
      --admin-border: rgba(200, 164, 78, 0.2);
    }

    body.light-mode {
      --admin-bg: #f1f5f9;
      --admin-bg-card: #ffffff;
      --admin-bg-input: #ffffff;
      --admin-text: #1e293b;
      --admin-text-heading: #1e293b;
      --admin-text-muted: #64748b;
      --admin-border: #e2e8f0;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: 'Inter', system-ui, sans-serif;
      background: var(--admin-bg);
      color: var(--admin-text);
      min-height: 100vh;
      padding: 40px 24px;
      transition: background 0.3s, color 0.3s;
    }

    .form-container {
      max-width: 720px;
      margin: 0 auto;
      background: var(--admin-bg-card);
      border: 1px solid var(--admin-border);
      border-radius: 16px;
      padding: 32px;
      transition: background 0.3s;
    }

    .form-section {
      padding-bottom: 24px;
      margin-bottom: 24px;
      border-bottom: 1px solid var(--admin-border);
    }

    .form-section:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }

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

    .input-field.input-error { border-color: var(--brand-danger); }
    .input-field.input-success { border-color: var(--brand-success); }

    .input-field::placeholder { color: var(--admin-text-muted); }

    .btn-primary {
      background: linear-gradient(135deg, var(--brand-primary) 0%, var(--brand-primary-hover) 100%);
      color: white;
      transition: all 0.2s;
    }
    .btn-primary:hover { opacity: 0.9; }
    .btn-primary:active { transform: scale(0.98); }

    .btn-secondary {
      background: var(--admin-bg-input);
      color: var(--admin-text);
      border: 1px solid var(--admin-border);
      transition: all 0.2s;
    }
    .btn-secondary:hover { background: var(--admin-table-hover); }

    .error-msg { color: var(--brand-danger); font-size: 0.75rem; display: none; margin-top: 4px; }
    .error-msg.show { display: block; }

    .success-msg { color: var(--brand-success); font-size: 0.75rem; display: none; margin-top: 4px; }
    .success-msg.show { display: block; }

    label { color: var(--admin-text); }
  </style>
</head>
<body>
  <div class="form-container">
    <!-- 标题 -->
    <div class="flex items-center justify-between mb-8">
      <div>
        <h1 style="color: var(--admin-text-heading);" class="text-2xl font-bold">添加用户</h1>
        <p style="color: var(--admin-text-muted);" class="text-sm mt-1">填写用户信息，标 * 的为必填项</p>
      </div>
      <button onclick="toggleFormTheme()" class="px-3 py-1.5 rounded-lg text-xs transition-colors"
        style="background: var(--admin-bg-input); border: 1px solid var(--admin-border); color: var(--admin-text-muted);">
        切换主题
      </button>
    </div>

    <form id="userForm" onsubmit="return handleFormSubmit(event)">
      <!-- Section 1: 基本信息 -->
      <div class="form-section">
        <h2 style="color: var(--admin-text-heading);" class="text-base font-semibold mb-4">基本信息</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="space-y-1.5">
            <label class="block text-sm font-medium">姓名 <span style="color: var(--brand-danger);">*</span></label>
            <input id="name" type="text" class="input-field w-full px-3 py-2 rounded-lg text-sm" placeholder="请输入姓名" required>
            <p id="nameError" class="error-msg">请输入姓名</p>
          </div>
          <div class="space-y-1.5">
            <label class="block text-sm font-medium">邮箱 <span style="color: var(--brand-danger);">*</span></label>
            <input id="email" type="email" class="input-field w-full px-3 py-2 rounded-lg text-sm" placeholder="you@example.com" required>
            <p id="emailError" class="error-msg">请输入有效的邮箱地址</p>
          </div>
          <div class="space-y-1.5">
            <label class="block text-sm font-medium">电话</label>
            <input id="phone" type="tel" class="input-field w-full px-3 py-2 rounded-lg text-sm" placeholder="请输入手机号">
          </div>
          <div class="space-y-1.5">
            <label class="block text-sm font-medium">角色 <span style="color: var(--brand-danger);">*</span></label>
            <select id="role" class="input-field w-full px-3 py-2 rounded-lg text-sm" required>
              <option value="">请选择角色</option>
              <option value="admin">管理员</option>
              <option value="editor">编辑</option>
              <option value="user">普通用户</option>
            </select>
            <p id="roleError" class="error-msg">请选择角色</p>
          </div>
        </div>
      </div>

      <!-- Section 2: 账户安全 -->
      <div class="form-section">
        <h2 style="color: var(--admin-text-heading);" class="text-base font-semibold mb-4">账户安全</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="space-y-1.5">
            <label class="block text-sm font-medium">密码 <span style="color: var(--brand-danger);">*</span></label>
            <input id="password" type="password" class="input-field w-full px-3 py-2 rounded-lg text-sm" placeholder="至少6位字符" required minlength="6">
            <p id="passwordError" class="error-msg">密码至少需要 6 个字符</p>
          </div>
          <div class="space-y-1.5">
            <label class="block text-sm font-medium">确认密码 <span style="color: var(--brand-danger);">*</span></label>
            <input id="confirmPwd" type="password" class="input-field w-full px-3 py-2 rounded-lg text-sm" placeholder="再次输入密码" required>
            <p id="confirmError" class="error-msg">两次密码不一致</p>
          </div>
        </div>
      </div>

      <!-- Section 3: 其他信息 -->
      <div class="form-section">
        <h2 style="color: var(--admin-text-heading);" class="text-base font-semibold mb-4">其他信息</h2>
        <div class="space-y-4">
          <div class="space-y-1.5">
            <label class="block text-sm font-medium">个人简介</label>
            <textarea id="bio" class="input-field w-full px-3 py-2 rounded-lg text-sm" rows="3" placeholder="请输入个人简介..."></textarea>
          </div>
          <div class="flex items-center gap-2">
            <input type="checkbox" id="active" class="rounded" style="accent-color: var(--brand-primary);" checked>
            <label for="active" style="color: var(--admin-text);" class="text-sm">立即激活账户</label>
          </div>
        </div>
      </div>

      <!-- 提交按钮 -->
      <div class="flex items-center justify-end gap-3 pt-4">
        <button type="reset" class="btn-secondary px-6 py-2.5 rounded-lg text-sm font-medium">重置</button>
        <button type="submit" id="submitBtn" class="btn-primary px-6 py-2.5 rounded-lg text-sm font-medium">
          提交
        </button>
      </div>
    </form>
  </div>

  <script>
    // 主题切换
    function toggleFormTheme() {
      document.body.classList.toggle('light-mode');
    }

    // 表单提交处理
    function handleFormSubmit(event) {
      event.preventDefault();

      // 清除所有错误
      document.querySelectorAll('.error-msg').forEach(function(el) { el.classList.remove('show'); });
      document.querySelectorAll('.input-field').forEach(function(el) { el.classList.remove('input-error'); });

      var isValid = true;

      // 姓名验证
      var name = document.getElementById('name');
      if (!name.value.trim()) {
        showError('name', 'nameError');
        isValid = false;
      }

      // 邮箱验证
      var email = document.getElementById('email');
      if (!email.value || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
        showError('email', 'emailError');
        isValid = false;
      }

      // 角色验证
      var role = document.getElementById('role');
      if (!role.value) {
        showError('role', 'roleError');
        isValid = false;
      }

      // 密码验证
      var password = document.getElementById('password');
      if (!password.value || password.value.length < 6) {
        showError('password', 'passwordError');
        isValid = false;
      }

      // 确认密码验证
      var confirmPwd = document.getElementById('confirmPwd');
      if (confirmPwd.value !== password.value) {
        showError('confirmPwd', 'confirmError');
        isValid = false;
      }

      if (isValid) {
        var btn = document.getElementById('submitBtn');
        btn.textContent = '提交中...';
        btn.disabled = true;
        setTimeout(function() {
          btn.textContent = '提交成功 ✓';
          btn.style.background = 'var(--brand-success)';
          setTimeout(function() {
            btn.textContent = '提交';
            btn.disabled = false;
            btn.style.background = '';
          }, 2000);
        }, 1500);
      }

      return false;
    }

    function showError(inputId, errorId) {
      document.getElementById(inputId).classList.add('input-error');
      document.getElementById(errorId).classList.add('show');
    }
  </script>
</body>
</html>
```

---

## 使用说明

### 字段自定义

| 字段 | ID | 验证规则 | 必填 |
|------|-----|---------|------|
| 姓名 | `name` | 非空 | 是 |
| 邮箱 | `email` | 邮箱格式 | 是 |
| 电话 | `phone` | 无（可选） | 否 |
| 角色 | `role` | 非空 | 是 |
| 密码 | `password` | 最小6位 | 是 |
| 确认密码 | `confirmPwd` | 与密码一致 | 是 |
| 简介 | `bio` | 无（可选） | 否 |

### 嵌入布局

将 `<div class="form-container">` 的内容放置在布局模板的 `page-content` 区域。

### 扩展

- 添加文件上传字段：`<input type="file">`
- 添加日期选择器：`<input type="date">`
- 添加多选框组：`<div>` 内嵌多个 checkbox
- 添加标签选择：使用 badge 组件
