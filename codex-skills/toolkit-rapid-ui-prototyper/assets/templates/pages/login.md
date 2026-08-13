# Login Page Template

登录页面模板。居中卡片式布局，包含邮箱/密码登录、表单验证、密码显示切换、主题切换功能。

---

## 完整 HTML

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>登录 - Admin</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --brand-primary: #2563eb;
      --brand-primary-hover: #1d4ed8;

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
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.3s, color 0.3s;
    }

    .login-card {
      background: var(--admin-bg-card);
      border: 1px solid var(--admin-border);
      border-radius: 16px;
      padding: 40px;
      width: 100%;
      max-width: 420px;
      margin: 20px;
      transition: background 0.3s;
    }

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

    .input-field.input-error {
      border-color: var(--brand-danger);
    }

    .btn-primary {
      background: linear-gradient(135deg, var(--brand-primary) 0%, var(--brand-primary-hover) 100%);
      color: white;
      transition: all 0.2s;
    }

    .btn-primary:hover { opacity: 0.9; }
    .btn-primary:active { transform: scale(0.98); }

    .error-msg { color: var(--brand-danger); font-size: 0.75rem; display: none; }
    .error-msg.show { display: block; }
  </style>
</head>
<body>
  <div class="login-card">
    <!-- Logo / 品牌 -->
    <div class="text-center mb-8">
      <div class="w-14 h-14 rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center mx-auto mb-4">
        <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
        </svg>
      </div>
      <h1 style="color: var(--admin-text-heading);" class="text-2xl font-bold">欢迎回来</h1>
      <p style="color: var(--admin-text-muted);" class="text-sm mt-1">请登录您的账户</p>
    </div>

    <!-- 登录表单 -->
    <form id="loginForm" onsubmit="return handleLogin(event)" class="space-y-5">
      <!-- 邮箱 -->
      <div class="space-y-1.5">
        <label style="color: var(--admin-text);" class="block text-sm font-medium">邮箱地址</label>
        <input id="email" type="email" class="input-field w-full px-4 py-2.5 rounded-lg" placeholder="you@example.com" required>
        <p id="emailError" class="error-msg">请输入有效的邮箱地址</p>
      </div>

      <!-- 密码 -->
      <div class="space-y-1.5">
        <label style="color: var(--admin-text);" class="block text-sm font-medium">密码</label>
        <div class="relative">
          <input id="password" type="password" class="input-field w-full px-4 py-2.5 pr-10 rounded-lg" placeholder="请输入密码" required minlength="6">
          <button type="button" onclick="togglePassword()" class="absolute right-3 top-1/2 -translate-y-1/2" style="color: var(--admin-text-muted);">
            <svg id="eyeIcon" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
            </svg>
          </button>
        </div>
        <p id="passwordError" class="error-msg">密码至少需要 6 个字符</p>
      </div>

      <!-- 记住我与忘记密码 -->
      <div class="flex items-center justify-between text-sm">
        <label class="flex items-center gap-2 cursor-pointer" style="color: var(--admin-text-muted);">
          <input type="checkbox" class="rounded" style="accent-color: var(--brand-primary);">
          记住我
        </label>
        <a href="#" style="color: var(--brand-primary);" class="hover:underline">忘记密码？</a>
      </div>

      <!-- 提交按钮 -->
      <button type="submit" class="btn-primary w-full py-2.5 rounded-lg font-semibold text-sm">
        登录
      </button>
    </form>

    <!-- 注册链接 -->
    <p style="color: var(--admin-text-muted);" class="text-center text-sm mt-6">
      还没有账户？
      <a href="#" style="color: var(--brand-primary);" class="font-medium hover:underline">立即注册</a>
    </p>

    <!-- 主题切换 -->
    <div class="flex justify-center mt-6">
      <button onclick="toggleLoginTheme()" class="px-3 py-1.5 rounded-lg text-xs transition-colors"
        style="background: var(--admin-bg-input); border: 1px solid var(--admin-border); color: var(--admin-text-muted);">
        <span id="themeLabel">切换到亮色模式</span>
      </button>
    </div>
  </div>

  <script>
    // 密码显示切换
    function togglePassword() {
      var input = document.getElementById('password');
      var icon = document.getElementById('eyeIcon');
      if (input.type === 'password') {
        input.type = 'text';
        icon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"/>';
      } else {
        input.type = 'password';
        icon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>';
      }
    }

    // 表单验证
    function handleLogin(event) {
      event.preventDefault();
      var email = document.getElementById('email');
      var password = document.getElementById('password');
      var emailError = document.getElementById('emailError');
      var passwordError = document.getElementById('passwordError');
      var isValid = true;

      emailError.classList.remove('show');
      passwordError.classList.remove('show');
      email.classList.remove('input-error');
      password.classList.remove('input-error');

      if (!email.value || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
        emailError.classList.add('show');
        email.classList.add('input-error');
        isValid = false;
      }

      if (!password.value || password.value.length < 6) {
        passwordError.classList.add('show');
        password.classList.add('input-error');
        isValid = false;
      }

      if (isValid) {
        // 模拟登录
        var btn = event.target.querySelector('button[type="submit"]');
        btn.textContent = '登录中...';
        btn.disabled = true;
        setTimeout(function() {
          btn.textContent = '登录成功 ✓';
          btn.style.background = 'var(--brand-success)';
        }, 1500);
      }

      return false;
    }

    // 主题切换
    function toggleLoginTheme() {
      document.body.classList.toggle('light-mode');
      var label = document.getElementById('themeLabel');
      label.textContent = document.body.classList.contains('light-mode') ? '切换到暗色模式' : '切换到亮色模式';
    }
  </script>
</body>
</html>
```

---

## 提取到布局中

如果登录页需要嵌入到某个布局（例如顶部导航布局）中，只需要提取 `<div class="login-card">` 的内容，将其放置到布局的 `page-content` 区域即可。需要保留对应的样式和 JavaScript。

## 可定制项

| 内容 | 位置 | 修改方式 |
|------|------|---------|
| Logo | `<div class="w-14 h-14...">` | 替换 SVG 或图片 |
| 标题 | `<h1>` 标签 | 修改文本 |
| 品牌色 | `--brand-primary` | 修改 CSS 变量 |
| 注册链接 | 底部 `<a>` 标签 | 修改 href 和文本 |
| 第三方登录 | 表单下方 | 添加社交按钮 |
