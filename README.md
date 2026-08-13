# Toolkit Skills

一套面向 Codex 的通用项目技能工具箱，包含 27 个可独立使用的 Skill，覆盖需求分析、架构设计、前后端开发、代码审查、测试、DevOps、UI 原型、BI 大屏、图表、演示文稿、提示词和 MCP 开发等场景。

## 目录结构

```text
toolkit-skills/
├── toolkit-skills/ # 27 个 Codex Skill 候选包
└── tools/          # 转换和中文化工具
```

每个 Skill 通常包含：

- `SKILL.md`：中文触发描述和操作说明
- `agents/openai.yaml`：Codex 界面元数据和默认提示
- `references/`：按需读取的详细领域说明
- `scripts/`：可选执行脚本
- `assets/`：可选模板、图标和素材

## 使用方式

### 项目级安装

将需要的 Skill 目录复制到目标项目的：

```text
<项目根目录>/.agents/skills/
```

例如：

```text
<项目根目录>/.agents/skills/toolkit-code-reviewer/
```

项目级 Skill 只对该项目生效。

### 用户级安装

将需要的 Skill 目录复制到：

```text
~/.agents/skills/
```

用户级 Skill 可供本机所有 Codex 项目使用。

### 调用示例

```text
$toolkit-code-reviewer 审查当前项目代码
```

```text
$toolkit-requirements-analyst 把这个产品想法整理成 PRD
```

```text
$toolkit-delivery-workflow 完整开发并验证这个功能
```

## Skill 清单

完整清单和说明见 [Codex Skill 转换报告](toolkit-skills/CONVERSION_REPORT.md)。

## 注意事项

- 建议按项目需要选择 Skill，不必一次启用全部 27 个。
- 部分 Skill 带有 Python、Node.js 或外部工具依赖，使用前应检查对应脚本和当前运行环境。
- 目录名和 `$toolkit-*` 调用名保持英文，面向用户的说明采用中文。
- 各子目录中已有的许可证文件应随对应 Skill 一并保留。
