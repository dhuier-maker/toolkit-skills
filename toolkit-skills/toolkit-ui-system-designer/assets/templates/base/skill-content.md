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
python scripts/search.py "<项目描述>" --design-system [-p "项目名称"] [-s <技术栈>]
```

**示例：**
```bash
# 后台管理系统
python scripts/search.py "后台管理系统 用户管理" --design-system -p "用户管理后台" -s vue3

# BI 大屏
python scripts/search.py "智慧城市大屏 数据监控" --design-system -p "智慧城市监控" -s vue3

# 移动端应用
python scripts/search.py "移动端 电商小程序" --design-system -p "电商小程序" -s uniapp
```

### Step 3: 领域搜索 (补充)

根据需要搜索特定领域：

```bash
python scripts/search.py "<关键词>" --domain <domain> [-n <结果数>]
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
python scripts/search.py "<关键词>" --stack <stack>
```

| 技术栈 | Stack | 适用场景 |
|--------|-------|----------|
| Vue 3 | `vue3` | 后台管理、Web 应用 |
| Uni-app | `uniapp` | 小程序、H5、跨端应用 |
| React | `react` | Web 应用、SPA |
| HTML+Tailwind | `html-tailwind` | 原型、静态页面 |

---

## Available Domains

| Domain | 数据文件 | 内容 |
|--------|----------|------|
| `style` | styles.csv | 10 种设计风格 |
| `color` | colors.csv | 10 种配色方案 |
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

## Example Workflow

**用户请求：** "创建一个用户管理后台系统"

### Step 1: 分析需求
- 项目类型: 后台管理系统
- 技术栈: Vue3
- 功能: 用户管理 (表格 + 表单)

### Step 2: 生成设计系统

```bash
python scripts/search.py "后台管理系统 用户管理" --design-system -p "用户管理后台" -s vue3
```

### Step 3: 补充搜索

```bash
# 搜索后台模板
python scripts/search.py "表单密集" --domain admin

# 搜索表格组件
python scripts/search.py "表格" --domain component

# 搜索布局模式
python scripts/search.py "侧边栏" --domain pattern
```

### Step 4: 技术栈指南

```bash
python scripts/search.py "组件 Props" --stack vue3
```

---

## Output Formats

设计系统支持两种输出格式：

```bash
# ASCII 格式 (默认) - 终端显示
python scripts/search.py "后台管理" --design-system

# Markdown 格式 - 文档保存
python scripts/search.py "后台管理" --design-system -f markdown
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