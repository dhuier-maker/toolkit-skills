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

## Command Reference

```bash
# 生成设计系统
python scripts/search.py "<描述>" --design-system -p "<项目名>"

# 领域搜索
python scripts/search.py "<关键词>" --domain <domain>

# 技术栈指南
python scripts/search.py "<关键词>" --stack <stack>

# 列出可用数据
python scripts/search.py --list
```