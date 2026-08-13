# 适配后的来源指南

# Smart UI Designer - 智能 UI 设计开发助手

## Prerequisites

检查 Python 是否已安装：

```bash
python --version || python --version
```

---

## How to Use This Skill

此 Skill 适用于以下场景：

| 场景 | 触发示例 | 开始步骤 |
|------|----------|----------|
| **后台管理系统** | "创建后台管理系统"、"后台管理模板" | Step 1 → Step 2 |
| **BI 大屏** | "BI 大屏"、"数据可视化大屏"、"驾驶舱" | Step 1 → Step 2 |
| **移动端应用** | "移动端 UI"、"小程序页面"、"H5 页面" | Step 1 → Step 2 |
| **原型设计** | "原型页面"、"Demo 页面"、"演示页面" | Step 1 → Step 2 |
| **组件开发** | "创建表格组件"、"表单组件" | Step 3 (domain: component) |
| **设计系统** | "生成设计系统"、"配色方案" | Step 2 |
| **参考网站风格提取** | "像 Linear 这种风格"、"从这个URL提取设计语言" | Step 2.5 |
| **技术栈指南** | "Vue3 最佳实践"、"Uni-app 开发规范" | Step 4 (stack search) |

---

## Workflow

### Step 1: 分析需求

从用户请求中提取关键信息：
- **项目类型**: 后台管理 / BI 大屏 / 移动端 / 原型
- **技术栈**: Vue3 / Uni-app / React / HTML+Tailwind
- **风格关键词**: 现代简约 / 科技暗黑 / 极简移动
- **功能需求**: 表格 / 表单 / 图表 / 导航

### Step 2: 生成设计系统 (推荐)

使用 `--design-system` 生成完整设计系统：

```bash
python skills/toolkit-ui-system-designer/scripts/search.py "<项目描述>" --design-system [-p "项目名称"] [-s <技术栈>]
```

**示例：**
```bash
# 后台管理系统
python skills/toolkit-ui-system-designer/scripts/search.py "后台管理系统 用户管理" --design-system -p "用户管理后台" -s vue3

# BI 大屏
python skills/toolkit-ui-system-designer/scripts/search.py "智慧城市大屏 数据监控" --design-system -p "智慧城市监控" -s vue3

# 移动端应用
python skills/toolkit-ui-system-designer/scripts/search.py "移动端 电商小程序" --design-system -p "电商小程序" -s uniapp
```

### Step 2.5: 从参考 URL 提取设计语言并扩充本地模板库

当用户给出参考网站，或表达“想要某个网站/品牌那种风格”且本地 `style` / `color` 检索不够贴切时，使用 extract 模式把网页设计语言沉淀为可复用模板：

```bash
python skills/toolkit-ui-system-designer/scripts/search.py extract --url <URL> --name "<模板名称>" --tags "<关键词1>,<关键词2>"
```

**产物位置：**
- `data/extracted/<slug>/tokens.json`：颜色、字体、圆角、间距、阴影、检测到的组件。
- `data/extracted/<slug>/components.html`：用于人工复核的组件预览页。
- `data/extracted/styles.csv` / `colors.csv`：自动追加到本地模板库，后续 `--domain style/color` 和 `--design-system` 会自动命中。

**管理命令：**
```bash
# 预览提取结果但不落库
python skills/toolkit-ui-system-designer/scripts/search.py extract --url <URL> --dry-run

# 查看已提取模板
python skills/toolkit-ui-system-designer/scripts/search.py extract --list

# 删除某个提取模板
python skills/toolkit-ui-system-designer/scripts/search.py extract --remove <slug>
```

**使用原则：**
- extract 适合提取“视觉语言”（色板、字体、圆角、阴影、组件气质），不等于拥有品牌资产授权。
- 生成生产页面前仍需人工复核 `components.html`，特别是颜色对比度、Logo/产品图、版权素材。
- 如果提取结果偏弱，优先补充 `--tags`，再用 `--domain style/color` 检索确认是否能命中。

### Step 3: 领域搜索 (补充)

根据需要搜索特定领域：

```bash
python skills/toolkit-ui-system-designer/scripts/search.py "<关键词>" --domain <domain> [-n <结果数>]
```

| 需求 | Domain | 示例 |
|------|--------|------|
| 设计风格 | `style` | `--domain style "科技暗黑"` |
| 配色方案 | `color` | `--domain color "商务蓝"` |
| 后台模板 | `admin` | `--domain admin "表单密集"` |
| BI 模板 | `bi` | `--domain bi "智慧城市"` |
| 移动端规范 | `mobile` | `--domain mobile "触摸目标"` |
| 组件库 | `component` | `--domain component "表格"` |
| 布局模式 | `pattern` | `--domain pattern "侧边栏"` |
| UX 规范 | `ux` | `--domain ux "无障碍"` |

### Step 4: 技术栈指南

获取技术栈特定最佳实践：

```bash
python skills/toolkit-ui-system-designer/scripts/search.py "<关键词>" --stack <stack>
```

| 技术栈 | Stack | 适用场景 |
|--------|-------|----------|
| Vue 3 | `vue3` | 后台管理、Web 应用 |
| Uni-app | `uniapp` | 小程序、H5、跨端应用 |
| React | `react` | Web 应用、SPA |
| HTML+Tailwind | `html-tailwind` | 原型、静态页面 |

---

## When to Apply

当任务涉及 **UI 设计、前端开发、组件创建、布局实现** 时，应使用此 Skill。

### Must Use

- 设计新的页面（后台管理、BI 大屏、移动端应用）
- 创建或重构 UI 组件（按钮、表单、表格、图表等）
- 选择配色方案、字体系统、间距规范
- 审查 UI 代码的用户体验、可访问性
- 实现导航结构、动效或响应式行为

### Skip

- 纯后端逻辑开发
- 仅涉及 API 或数据库设计
- 与界面无关的性能优化

---

## Quick Reference

### 1. 项目类型识别

| 关键词 | 项目类型 | 默认风格 | 默认配色 |
|--------|----------|----------|----------|
| 后台、管理、admin、CMS | 后台管理系统 | 现代简约 | 商务蓝 #1890ff |
| 大屏、BI、dashboard、驾驶舱 | BI 数据大屏 | 科技暗黑 | 科技青 #00d4ff |
| 移动端、小程序、H5、app | 移动端应用 | 极简移动 | 自然绿 #07c160 |
| 原型、demo、演示 | 原型设计 | 原型线框 | 专业灰 #6b7280 |

### 2. 设计风格速查

| 风格 | 适用场景 | 关键词 |
|------|----------|--------|
| 现代简约 | 后台管理、企业应用 | 简约、干净、专业 |
| 科技暗黑 | BI 大屏、监控系统 | 科技、数据、可视化 |
| 玻璃拟态 | 移动端、展示页面 | 玻璃、透明、模糊 |
| 极简移动 | 小程序、H5 | 移动、轻量、快速 |

### 3. 布局模式速查

| 模式 | 适用场景 | 结构 |
|------|----------|------|
| 侧边栏导航 | 后台管理 | Sidebar + Header + Content |
| 顶部导航 | 功能较少的管理系统 | Header + Content |
| 三栏布局 | BI 大屏 | Left + Center + Right |
| Tab 导航 | 移动端应用 | Header + Content + TabBar |

### 4. 组件速查

| 组件 | 用途 | 关键 Props |
|------|------|------------|
| Table | 数据展示 | data, columns, pagination |
| Form | 数据录入 | model, rules, label-width |
| Modal | 弹窗反馈 | visible, title, width |
| Select | 下拉选择 | value, options, multiple |
| DatePicker | 日期选择 | value, type, format |

### 5. 无障碍规范 (CRITICAL)

| 规范 | 要求 | 检查方法 |
|------|------|----------|
| 颜色对比度 | >= 4.5:1 | 使用对比度检查工具 |
| 焦点状态 | 必须可见 | Tab 键导航测试 |
| 触摸目标 | >= 44x44px | 移动端点击测试 |
| 屏幕阅读器 | 提供描述 | VoiceOver/TalkBack 测试 |

### 6. 响应式断点

| 断点 | 宽度 | 设备 |
|------|------|------|
| xs | < 640px | 手机 |
| sm | >= 640px | 大屏手机 |
| md | >= 768px | 平板 |
| lg | >= 1024px | 桌面 |
| xl | >= 1280px | 大屏桌面 |

### 7. 技术栈选择

| 场景 | 推荐技术栈 | 原因 |
|------|------------|------|
| 后台管理系统 | Vue3 + TypeScript | 组件生态丰富 |
| 小程序 | Uni-app | 跨端开发效率高 |
| Web 应用 | React / Vue3 | 生态成熟 |
| 快速原型 | HTML + Tailwind | 开发速度快 |

---

## Available Domains

| Domain | 数据文件 | 内容 |
|--------|----------|------|
| `style` | styles.csv + extracted/styles.csv | 10 种内置设计风格 + URL 提取模板 |
| `color` | colors.csv + extracted/colors.csv | 10 种内置配色方案 + URL 提取模板 |
| `admin` | admin-templates.csv | 8 种后台模板 |
| `bi` | bi-templates.csv | 8 种 BI 大屏模板 |
| `mobile` | mobile-specs.csv | 10 条移动端规范 |
| `component` | components.csv | 20 个常用组件 |
| `pattern` | patterns.csv | 10 种布局模式 |
| `ux` | ux-guidelines.csv | 22 条 UX 规范 |

---

## Available Stacks

| Stack | 数据文件 | 规范数量 |
|-------|----------|----------|
| `vue3` | stacks/vue3.csv | 16 条 |
| `uniapp` | stacks/uniapp.csv | 16 条 |
| `react` | stacks/react.csv | 15 条 |
| `html-tailwind` | stacks/html-tailwind.csv | 20 条 |

---

## Command Reference

```bash
# 生成设计系统
python skills/toolkit-ui-system-designer/scripts/search.py "<描述>" --design-system -p "<项目名>"

# 领域搜索
python skills/toolkit-ui-system-designer/scripts/search.py "<关键词>" --domain <domain>

# 技术栈指南
python skills/toolkit-ui-system-designer/scripts/search.py "<关键词>" --stack <stack>

# 提取参考网站设计语言
python skills/toolkit-ui-system-designer/scripts/search.py extract --url <URL> --name "<模板名称>" --tags "<关键词>"

# 查看已提取模板
python skills/toolkit-ui-system-designer/scripts/search.py extract --list

# 列出可用数据
python skills/toolkit-ui-system-designer/scripts/search.py --list
```

---

## Pre-Delivery Checklist

在交付 UI 代码前，验证以下项目：

### 视觉质量
- [ ] 无障碍性：颜色对比度 >= 4.5:1
- [ ] 焦点状态：所有交互元素有可见焦点
- [ ] 触摸目标：移动端 >= 44x44px
- [ ] 响应式：支持 375px / 768px / 1024px / 1440px

### 交互体验
- [ ] 加载状态：操作 > 1s 显示加载
- [ ] 错误处理：提供清晰错误信息和恢复方案
- [ ] 表单验证：实时验证，错误位置明确

### 代码规范
- [ ] 组件命名：PascalCase (Vue/React)
- [ ] 响应式单位：rpx (Uni-app) / rem (Web)
- [ ] 状态管理：ref/reactive (Vue) / useState (React)

---

## 注意事项

1. **URL 提取版权** — extract 模式仅提取视觉语言（色板、字体、圆角），不等于拥有品牌资产授权；生产页面使用前需人工复核 `components.html` 中的 Logo/产品图/版权素材
2. **颜色对比度** — 生成的配色方案必须满足 WCAG 2.1 AA 标准（文本对比度 >= 4.5:1），深色背景尤其需验证
3. **技术栈一致性** — 同一项目内技术栈选择后不再切换（如选定 Vue3 则不混入 React 写法），避免风格碎片
4. **模板数据路径** — 脚本中 `skills/toolkit-ui-system-designer/scripts/` 为相对路径，需确保工作目录正确或使用绝对路径
5. **设计系统输出** — `--design-system` 生成的设计规范需与 toolkit-rapid-ui-prototyper 的 `:root` 变量体系对齐，避免两套配色冲突
