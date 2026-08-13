# Template Library Index

模板分类索引，按使用场景快速定位需要的模板。

> **主题系统约定**：所有模板遵循 SKILL.md 中的主题系统约定。颜色使用 CSS 变量（`var(--admin-*)` / `var(--brand-*)` / `var(--mobile-*)` / `var(--bi-*)`），明暗切换使用 `body.light-mode` class，禁止使用 Tailwind `dark:` 前缀。

---

## 目录结构

```
templates/
├── _index.md                      # 本文件 — 模板目录 + 分类说明
├── themes/                        # 主题变量模板（仅 CSS 变量定义）
│   ├── README.md                  # 主题变量说明
│   ├── brand-colors.md            # 品牌色变量
│   ├── admin-theme.md             # 管理后台主题变量（含亮色模式覆盖）
│   ├── mobile-theme.md            # 移动端主题变量
│   └── bi-theme.md                # BI 大屏固定暗色主题变量（不受亮色模式影响）
├── layouts/                       # 布局模板（完整 HTML 结构）
│   ├── README.md                  # 布局模式说明
│   ├── sidebar-nav.md             # 侧边栏导航布局
│   ├── top-nav.md                 # 顶部导航布局
│   └── mobile-bottom-tab.md       # 移动端底部 Tab 导航布局
├── components/                    # 基础组件模板（含主题变量版）
│   ├── README.md                  # 基础组件说明
│   ├── button.md                  # 按钮组件
│   ├── input.md                   # 输入框组件
│   ├── card.md                    # 卡片组件
│   ├── badge.md                   # 徽章组件
│   ├── table.md                   # 表格组件
│   ├── modal.md                   # 弹窗组件
│   └── pagination.md              # 分页组件
└── pages/                         # 页面模板（完整 HTML，含样式和交互）
    ├── README.md                  # 页面模板说明
    ├── login.md                   # 登录页（含表单验证）
    ├── admin-dashboard.md         # 管理后台首页（统计卡片 + 图表 + 表格）
    ├── form-page.md               # 表单页
    └── list-detail.md             # 列表 + 详情页
```

---

## 分类说明

### themes/ — 主题变量

仅包含 CSS 变量定义，不涉及具体组件。用于快速为项目建立主题体系。

| 文件 | 适用场景 | 是否受亮色模式影响 |
|------|----------|-------------------|
| `brand-colors.md` | 所有视图共享的品牌色 | 否 |
| `admin-theme.md` | 管理后台、Web 应用 | 是（body.light-mode 覆盖） |
| `mobile-theme.md` | 移动端 H5 页面 | 是（body.light-mode 覆盖） |
| `bi-theme.md` | BI 大屏、数据可视化 | 否（永远暗色） |

### layouts/ — 布局结构

完整的页面骨架，包含导航栏、内容区、页脚等。选择布局后，在其中填充组件和内容。

| 文件 | 适用场景 | 响应式 |
|------|----------|--------|
| `sidebar-nav.md` | 后台管理、仪表盘 | 桌面优先，移动端侧栏折叠 |
| `top-nav.md` | 官网、SaaS 应用、文档站 | 全设备 |
| `mobile-bottom-tab.md` | 移动端 App、H5 | 移动端专用 |

### components/ — 基础组件

可复用的 UI 组件片段。每种组件提供主题变量版和硬编码版两种形态。

| 文件 | 主题变量版 | 硬编码版 | 特殊要求 |
|------|-----------|---------|---------|
| `button.md` | 是 | 是 | 品牌色渐变主按钮 |
| `input.md` | 是 | 是 | focus 环、验证状态 |
| `card.md` | 是 | 是 | 悬停上浮效果 |
| `badge.md` | 是 | 是 | 状态色（success/warning/danger/info） |
| `table.md` | 是 | 否 | 斑马纹行可选 |
| `modal.md` | 是（强制） | 否 | 必须使用 `.modal-content` 主题类 |
| `pagination.md` | 是（强制） | 否 | 活跃页使用品牌色 |

### pages/ — 页面模板

完整的页面 HTML，可直接使用或组合修改。

| 文件 | 包含内容 | 交互功能 |
|------|---------|---------|
| `login.md` | 登录表单 + 验证 + 主题切换 | 表单验证、密码显示切换 |
| `admin-dashboard.md` | 侧栏 + 顶栏 + 统计卡片 + 图表 + 表格 | 主题切换、图表渲染 |
| `form-page.md` | 多字段表单 + 验证 + 提交 | 表单验证、提交处理 |
| `list-detail.md` | 数据表格 + 搜索 + 详情弹窗 | 搜索筛选、弹窗详情、分页 |

---

## 使用指南

### 快速开始

1. **新建项目**：从 `themes/` 选择需要的主题模板复制到 `<style>` 中
2. **搭建骨架**：从 `layouts/` 选择布局模板
3. **填充组件**：从 `components/` 选择组件组合到布局中
4. **组装页面**：参考 `pages/` 中的完整示例

### 多视图页面

当生成包含多个视图（如管理后台 + BI 大屏）的单页应用时：

```html
<body>
  <!-- 管理后台视图 -->
  <div id="view-admin">
    <!-- admin 系列变量 + body.light-mode 切换 -->
  </div>

  <!-- BI 大屏视图（固定暗色） -->
  <div id="view-bi">
    <!-- bi 系列变量，不受亮色模式影响 -->
  </div>
</body>
```

### 主题切换逻辑

```javascript
// 单视图切换（管理后台或移动端）
document.body.classList.toggle('light-mode');

// 多视图切换（管理后台切换，BI 大屏保持不变）
var adminView = document.getElementById('view-admin');
adminView.classList.toggle('light-mode');
// 注意：此时 CSS 选择器为 body.light-mode #view-admin，
// 或者使用 body #view-admin.light-mode，根据需求选择
```

---

## 模板命名规范

- 文件名：`kebab-case.md`
- 目录名：`kebab-case`
- 每个文件的标题使用 `#` 一级标题
- 代码块标注语言（html/css/javascript）
- 可选部分标注 `（可选）`
- 强制要求标注 `（强制）`
- 警告信息使用 `> **警告**` 格式
