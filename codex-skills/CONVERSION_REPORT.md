# Codex Skill 转换报告

原始的 `skills/` 和 `说明手册/` 目录未被修改。

## Skill 清单

| Codex Skill | 中文名称 |
|---|---|
| `toolkit-backend-architect` | 后端架构师 |
| `toolkit-bi-dashboard` | BI 大屏构建器 |
| `toolkit-bi-widget` | BI 组件开发器 |
| `toolkit-code-reviewer` | 代码审查专家 |
| `toolkit-codex-project-bootstrap` | Codex 项目初始化 |
| `toolkit-coding-guidelines` | 编码行为准则 |
| `toolkit-delivery-workflow` | 软件交付工作流 |
| `toolkit-devops-engineer` | DevOps 工程师 |
| `toolkit-diagram-generator` | 专业图表生成器 |
| `toolkit-editable-presentation` | 可编辑演示文稿 |
| `toolkit-experience-designer` | 体验设计师 |
| `toolkit-frontend-engineer` | 前端工程师 |
| `toolkit-html-doc-site` | HTML 文档站生成器 |
| `toolkit-image-prompt-writer` | 图片提示词编写器 |
| `toolkit-mcp-builder` | MCP 服务构建器 |
| `toolkit-prompt-optimizer` | 提示词优化器 |
| `toolkit-prompt-writer` | 提示词编写器 |
| `toolkit-qa-tester` | QA 测试工程师 |
| `toolkit-rapid-ui-prototyper` | 快速 UI 原型器 |
| `toolkit-requirements-analyst` | 需求分析师 |
| `toolkit-skill-evaluator` | Skill 评估器 |
| `toolkit-skill-workbench` | Skill 工作台 |
| `toolkit-spring-module` | Spring 模块构建器 |
| `toolkit-test-coordinator` | 测试协调器 |
| `toolkit-ui-system-designer` | UI 设计系统专家 |
| `toolkit-visual-asset-generator` | 视觉素材生成器 |
| `toolkit-visual-presentation` | 视觉型演示文稿 |

## 设计说明

- 所有 Skill 使用中性的 `toolkit-` 命名空间，以降低名称冲突风险。
- 固定公司和项目假设已转换为可由当前项目配置的约定。
- 其他代理平台的专属说明已转换为 Codex 概念。
- 每个 Skill 都保留了详细来源指南和可复用资源。
- Skill 的目录名和 `$toolkit-*` 调用名保持英文，以确保稳定识别；面向用户的说明已中文化。
- 这些目录是可移植候选包，目前没有安装到用户级 Skill 目录。
