# Toolkit Skills

面向 Codex 的前端研发 Skill 工具箱。当前版本聚焦前端实现、UI/UX、数据大屏、代码审查、QA 和交付，共包含 13 个可独立安装的 Skill。

仓库地址：https://github.com/dhuier-maker/toolkit-skills

## 能力范围

| Skill | 作用 |
|---|---|
| `toolkit-frontend-engineer` | 按当前技术栈实现和重构前端页面、组件、路由、状态及接口调用 |
| `toolkit-experience-designer` | 评审交互体验、信息层级、响应式表现和可访问性 |
| `toolkit-ui-system-designer` | 建立和维护颜色、字体、间距、布局及组件状态规范 |
| `toolkit-rapid-ui-prototyper` | 将需求快速转换为可运行的前端原型 |
| `toolkit-bi-dashboard` | 构建运营驾驶舱、数据大屏和监控看板 |
| `toolkit-bi-widget` | 开发图表、地图、KPI 卡片等可复用可视化组件 |
| `toolkit-visual-asset-generator` | 生成前端需要的图标、背景、PNG 和 SVG 素材 |
| `toolkit-code-reviewer` | 审查前端正确性、安全性、性能、可维护性和回归风险 |
| `toolkit-qa-tester` | 设计并执行页面、交互、兼容性和回归测试 |
| `toolkit-test-coordinator` | 协调缺陷分类、修复、复测和退出条件 |
| `toolkit-delivery-workflow` | 组织从任务拆解到构建、验证和发布的前端交付流程 |
| `toolkit-coding-guidelines` | 提供谨慎、可验证的通用编码准则 |
| `toolkit-codex-project-bootstrap` | 为前端仓库建立项目级 Codex 协作说明 |

后端、Spring、MCP、提示词、演示文稿、通用图表和文档站等非前端 Skill 已从当前成品包移除。

## 目录

```text
toolkit-skills/
├── toolkit-skills/       # 13 个前端研发 Skill
├── tools/                # 转换与中文化工具
├── INSTALL.md            # 安装、更新和卸载说明
├── RELEASE.md            # 版本与发布规范
└── CHANGELOG.md          # 版本变更记录
```

## 快速安装

项目级安装只对当前项目生效。以代码审查 Skill 为例：

```powershell
New-Item -ItemType Directory -Force .agents\skills | Out-Null
Copy-Item -Recurse toolkit-skills\toolkit-code-reviewer .agents\skills\
```

在 Codex 中调用：

```text
$toolkit-code-reviewer 审查当前前端改动，并按严重程度输出问题和验证建议。
```

完整安装和更新方式见 [INSTALL.md](INSTALL.md)。建议按任务选择 Skill，不要无差别安装全部目录。

## 版本

当前整理版本：`0.2.0`。发布规则见 [RELEASE.md](RELEASE.md)，变更见 [CHANGELOG.md](CHANGELOG.md)。
