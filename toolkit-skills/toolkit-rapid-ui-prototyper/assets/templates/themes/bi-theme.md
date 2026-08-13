# BI Dashboard Theme Template

BI 大屏 / 数据可视化主题变量模板。永远固定暗色，不受 `body.light-mode` 影响。

> **关键规则**：BI 大屏视图必须使用 `#view-bi` id 容器隔离，并在 `body.light-mode #view-bi` 选择器中重置关键变量，确保亮色模式不会影响 BI 大屏的暗色风格。

---

## 基础变量定义

```css
:root {
  /* ===== BI 大屏（固定暗色，不受亮色模式影响） ===== */
  --bi-bg: #060b14;                    /* 大屏背景 */
  --bi-bg-dark: #040810;               /* 更深层背景（用于图表区域） */
  --bi-card-bg: rgba(0, 212, 255, 0.05);   /* 卡片/面板背景（科技蓝半透明） */
  --bi-card-border: rgba(0, 212, 255, 0.15); /* 卡片边框 */

  --bi-text: #e2e8f0;                  /* 正文颜色 */
  --bi-text-heading: #e8d48b;           /* 标题颜色（金色） */
  --bi-text-muted: #94a3b8;             /* 次要文字 */
  --bi-text-accent: #00d4ff;            /* 强调文字（科技蓝） */

  --bi-border: rgba(0, 212, 255, 0.1);  /* 边框颜色 */

  /* 图表相关 */
  --bi-chart-grid: rgba(0, 212, 255, 0.08); /* 图表网格线 */
  --bi-chart-axis: rgba(0, 212, 255, 0.3);  /* 图表轴线 */

  /* 装饰 */
  --bi-glow: 0 0 20px rgba(0, 212, 255, 0.15);  /* 发光效果 */
  --bi-glow-strong: 0 0 30px rgba(0, 212, 255, 0.3); /* 强发光效果 */

  /* 数字翻牌器 */
  --bi-number-color: #00d4ff;           /* 数字颜色 */
  --bi-number-shadow: 0 0 10px rgba(0, 212, 255, 0.5); /* 数字发光 */

  /* 动画 */
  --bi-animation-duration: 0.3s;
}
```

---

## 固定暗色 — 亮色模式隔离

```css
/* 确保亮色模式下 BI 大屏仍然保持暗色 */
body.light-mode #view-bi {
  --bi-bg: #060b14;
  --bi-bg-dark: #040810;
  --bi-card-bg: rgba(0, 212, 255, 0.05);
  --bi-card-border: rgba(0, 212, 255, 0.15);
  --bi-text: #e2e8f0;
  --bi-text-heading: #e8d48b;
  --bi-text-muted: #94a3b8;
  --bi-text-accent: #00d4ff;
  --bi-border: rgba(0, 212, 255, 0.1);
  --bi-chart-grid: rgba(0, 212, 255, 0.08);
  --bi-number-color: #00d4ff;
  --bi-number-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
}
```

---

## 完整使用示例

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BI Dashboard</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
  <style>
    :root {
      /* 品牌色 */
      --brand-primary: #2563eb;

      /* BI 大屏暗色变量 */
      --bi-bg: #060b14;
      --bi-card-bg: rgba(0, 212, 255, 0.05);
      --bi-text: #e2e8f0;
      --bi-text-heading: #e8d48b;
      --bi-text-muted: #94a3b8;
      --bi-text-accent: #00d4ff;
      --bi-border: rgba(0, 212, 255, 0.1);
    }

    /* 亮色模式隔离 */
    body.light-mode #view-bi {
      --bi-bg: #060b14;
      --bi-card-bg: rgba(0, 212, 255, 0.05);
      --bi-text: #e2e8f0;
      --bi-text-heading: #e8d48b;
      --bi-text-muted: #94a3b8;
      --bi-text-accent: #00d4ff;
      --bi-border: rgba(0, 212, 255, 0.1);
    }

    #view-bi {
      background: var(--bi-bg);
      color: var(--bi-text);
      min-height: 100vh;
    }

    .bi-card {
      background: var(--bi-card-bg);
      border: 1px solid var(--bi-border);
      border-radius: 12px;
    }

    .bi-number {
      color: var(--bi-number-color);
      text-shadow: var(--bi-number-shadow);
      font-size: 2rem;
      font-weight: 700;
    }
  </style>
</head>
<body>
  <div id="view-bi">
    <div class="bi-card p-6">
      <h2 style="color: var(--bi-text-heading);">数据概览</h2>
      <p style="color: var(--bi-text-muted);">BI 大屏固定暗色显示</p>
      <span class="bi-number">12,345</span>
    </div>
  </div>
</body>
</html>
```

---

## 多视图共存示例（管理后台 + BI 大屏）

```html
<body>
  <!-- 视图切换按钮 -->
  <div style="position: fixed; top: 16px; right: 16px; z-index: 999;">
    <button onclick="toggleView()" class="px-4 py-2 rounded-lg text-sm"
      style="background: var(--brand-primary); color: white;">
      切换视图
    </button>
    <button onclick="toggleAdminTheme()" class="px-4 py-2 rounded-lg text-sm"
      style="background: var(--admin-bg-input); border: 1px solid var(--admin-border);">
      切换主题
    </button>
  </div>

  <!-- 管理后台视图（可切换亮暗） -->
  <div id="view-admin" style="display: block;">
    <!-- ... -->
  </div>

  <!-- BI 大屏视图（固定暗色） -->
  <div id="view-bi" style="display: none;">
    <!-- ... -->
  </div>

  <script>
    function toggleView() {
      var admin = document.getElementById('view-admin');
      var bi = document.getElementById('view-bi');
      var isAdmin = admin.style.display !== 'none';
      admin.style.display = isAdmin ? 'none' : 'block';
      bi.style.display = isAdmin ? 'block' : 'none';
    }

    function toggleAdminTheme() {
      document.body.classList.toggle('light-mode');
    }
  </script>
</body>
```

> **警告**：BI 大屏的卡片组件不要使用 `class="card"`（可能被 `--admin-bg-card` 影响），应使用独立的 `class="bi-card"` 类。
