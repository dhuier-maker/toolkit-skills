# Codex Skill 前端化整理报告

原始“海川”资料未修改。本仓库已从 27 个通用候选 Skill 收敛为 13 个前端研发 Skill。

## 保留清单

| Skill | 分类 |
|---|---|
| `toolkit-frontend-engineer` | 前端开发 |
| `toolkit-experience-designer` | UI/UX |
| `toolkit-ui-system-designer` | 设计系统 |
| `toolkit-rapid-ui-prototyper` | UI 原型 |
| `toolkit-bi-dashboard` | 数据大屏 |
| `toolkit-bi-widget` | 可视化组件 |
| `toolkit-visual-asset-generator` | 前端视觉素材 |
| `toolkit-code-reviewer` | 代码审查 |
| `toolkit-qa-tester` | QA 测试 |
| `toolkit-test-coordinator` | 缺陷与回归协调 |
| `toolkit-delivery-workflow` | 前端交付 |
| `toolkit-coding-guidelines` | 编码准则 |
| `toolkit-codex-project-bootstrap` | 项目接入 |

## 已移除范围

后端架构、Spring 模块、DevOps、MCP、提示词、演示文稿、通用图表、HTML 文档站、需求分析和 Skill 开发评估等不直接服务于前端研发主流程的候选 Skill 已移出成品目录。

## 兼容原则

- Skill 名保持稳定的 `toolkit-` 命名空间。
- 说明使用中文，路径和触发名使用英文。
- 不绑定单一业务项目；先读取当前仓库的真实技术栈与约定。
- 对 Vue 2、React、Vue 3 及遗留工程均要求复用项目既有架构，不擅自升级框架。
- 每个 Skill 可独立复制到项目的 `.agents/skills/`。
