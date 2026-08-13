from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "toolkit-skills"


SKILLS = {
    "toolkit-backend-architect": ("后端架构师", "设计 API、数据模型、服务边界并实现生产级后端。适用于后端架构、Spring Boot 服务、数据库设计、API 契约和服务端开发任务。", "设计后端架构、API、数据模型和生产级服务端实现"),
    "toolkit-bi-dashboard": ("BI 大屏构建器", "基于当前项目的前端技术栈构建可复用的数据仪表盘和大屏页面。适用于 BI 大屏、监控看板、GIS 可视化、运营驾驶舱和 1920×1080 数据展示。", "构建 BI 大屏、监控看板、GIS 和运营驾驶舱"),
    "toolkit-bi-widget": ("BI 组件开发器", "为现有仪表盘框架开发可配置、可复用的可视化组件。适用于图表、地图、KPI 卡片、进度视图、文本组件、3D 场景、交互和配置面板。", "开发可配置、可复用的 BI 可视化组件"),
    "toolkit-code-reviewer": ("代码审查专家", "从正确性、安全性、性能、可维护性和回归风险等方面审查代码。适用于拉取请求审查、上线前检查、风险分析和可执行的代码质量反馈。", "审查代码的正确性、安全性、性能和回归风险"),
    "toolkit-codex-project-bootstrap": ("Codex 项目初始化", "通过创建或完善 AGENTS.md 和项目级说明，为代码仓库建立高效的 Codex 协作环境。适用于首次配置工作区、仓库接入和项目指令初始化。", "创建 AGENTS.md 并初始化 Codex 项目协作规范"),
    "toolkit-coding-guidelines": ("编码行为准则", "在编码、重构和审查时采用谨慎、精确的工程实践，减少不必要的复杂度，明确假设和验证目标，并避免静默失败。", "用谨慎、精确、可验证的原则指导编码和重构"),
    "toolkit-delivery-workflow": ("软件交付工作流", "协调需求、架构、原型、实现、审查、测试、修复和交付的端到端软件流程。适用于完整项目开发或需要多个阶段协同完成的功能交付。", "协调需求到交付的端到端软件开发流程"),
    "toolkit-devops-engineer": ("DevOps 工程师", "创建和审查部署、容器、CI/CD、可观测性和运维配置。适用于 Docker、流水线、Kubernetes、环境配置、监控和发布自动化。", "处理容器、CI/CD、部署、监控和发布自动化"),
    "toolkit-diagram-generator": ("专业图表生成器", "使用 PlantUML、Graphviz、Vega-Lite、HTML、Canvas 或信息图语法创建专业技术图和数据可视化。适用于架构图、UML、网络图、流程图、依赖图和数据图表。", "生成架构图、UML、流程图和数据可视化"),
    "toolkit-editable-presentation": ("可编辑演示文稿", "从文档、URL 或 Markdown 创建基于 SVG 的可编辑演示文稿，支持精确排版和演讲备注。适用于要求文字可编辑、结构清晰的 PPTX 交付。", "创建文字可编辑、基于 SVG 的高质量 PPTX"),
    "toolkit-experience-designer": ("体验设计师", "创建高保真 HTML 原型、交互演示、视觉探索和动效设计产物。适用于 UI 模型、交互原型、设计变体和动态产品演示。", "创建高保真 HTML 原型、交互演示和动效设计"),
    "toolkit-frontend-engineer": ("前端工程师", "根据需求和 API 契约实现可维护的生产级前端。适用于 Vue、React、TypeScript、组件架构、接口对接、状态管理和响应式页面开发。", "实现 Vue、React 和 TypeScript 生产级前端"),
    "toolkit-html-doc-site": ("HTML 文档站生成器", "将 Markdown 文档集合转换为便携的静态 HTML 文档站。适用于离线文档、可浏览手册、知识库和无需服务器的文档交付。", "把 Markdown 文档集转换为离线静态 HTML 站点"),
    "toolkit-image-prompt-writer": ("图片提示词编写器", "为图片生成模型编写详细、可直接使用的专业提示词，但不实际生成图片。适用于摄影、海报、商品、角色、UI 概念、插画和信息图提示词。", "为图片生成模型编写专业、可直接使用的提示词"),
    "toolkit-mcp-builder": ("MCP 服务构建器", "使用 Python 或 TypeScript 设计、实现并评估模型上下文协议（MCP）服务器。适用于将 API、数据源或业务服务封装为 MCP 工具和资源。", "使用 Python 或 TypeScript 构建和评估 MCP 服务"),
    "toolkit-prompt-optimizer": ("提示词优化器", "使用合适的提示框架分析和改进已有提示词。适用于提升提示词的清晰度、约束完整性、结构、可靠性和输出格式。", "分析并优化已有提示词的结构、约束和可靠性"),
    "toolkit-prompt-writer": ("提示词编写器", "根据粗略目标为大语言模型、编码代理、图片工具或其他 AI 系统创建清晰、可执行的新提示词。适用于从零编写提示词，不用于优化已有提示词。", "根据粗略目标从零编写清晰、可执行的提示词"),
    "toolkit-qa-tester": ("QA 测试工程师", "设计并执行聚焦的黑盒测试用例，输出基于证据的 QA 报告。适用于页面、API、性能、验收、回归和上线前验证。", "设计并执行黑盒测试，输出基于证据的 QA 报告"),
    "toolkit-rapid-ui-prototyper": ("快速 UI 原型器", "将自然语言产品需求快速转换为可运行的 UI 原型。适用于早期 Vue、React 或 HTML 原型、布局探索、表单、管理页面、移动端页面和仪表盘。", "把产品需求快速转换为可运行的 UI 原型"),
    "toolkit-requirements-analyst": ("需求分析师", "将粗略的产品想法整理为结构化、可测试的需求和 PRD。适用于需求澄清、范围定义、验收标准、用户故事和歧义消除。", "把模糊想法整理为结构化、可测试的 PRD"),
    "toolkit-skill-evaluator": ("Skill 评估器", "评估已有 Skill 的触发质量、结构、可用性、冲突和输出效果。适用于评分、对比、审计和提出改进建议，默认不直接重写 Skill。", "评估 Skill 的触发、结构、冲突和输出效果"),
    "toolkit-skill-workbench": ("Skill 工作台", "创建或修改可移植的 Codex Skill，包括精简说明、复用资源、界面元数据、验证和迭代评估。适用于编写 Skill 或改进其结构。", "创建、修改并验证可移植的 Codex Skill"),
    "toolkit-spring-module": ("Spring 模块构建器", "搭建可配置的 Spring Boot 模块并生成常规业务层代码。适用于新建 Java 模块、CRUD 服务、DTO、参数校验、持久层映射、Feign 客户端、任务调度和环境配置。", "搭建 Spring Boot 模块并生成常规业务代码"),
    "toolkit-test-coordinator": ("测试协调器", "协调前后端的测试、缺陷分类、修复和回归循环。适用于持续推进直到满足退出条件的端到端 QA 工作流。", "协调测试、缺陷分类、修复和回归验证循环"),
    "toolkit-ui-system-designer": ("UI 设计系统专家", "定义可复用的 UI 设计系统，包括配色、字体、布局、组件规范和参考网站设计语言。适用于实现前先建立统一的视觉体系。", "定义配色、字体、布局和组件等 UI 设计规范"),
    "toolkit-visual-asset-generator": ("视觉素材生成器", "生成 PNG、SVG、图表、图标、封面、横幅和大屏背景等视觉文件。适用于交付实际图片或向量素材，而不是只编写提示词。", "生成 PNG、SVG、图表、图标和背景等视觉素材"),
    "toolkit-visual-presentation": ("视觉型演示文稿", "通过端到端视觉流程创建以整页图片为主的演示文稿。适用于发布会、路演、品牌展示及视觉冲击力比文字可编辑性更重要的幻灯片。", "创建视觉冲击力优先的图片型演示文稿"),
}


OPERATING_RULES = """## 操作规则

1. 执行前检查当前工作区，并读取适用范围内的 `AGENTS.md`。
2. 从本地上下文确认交付物、约束、现有技术栈和验收证据。只有缺失信息会实质改变结果时才询问用户。
3. 执行本 Skill 前完整阅读 `references/adapted-source-guide.md`。将其作为详细领域指南，但以下 Codex 兼容规则具有更高优先级。
4. 复用项目已有约定和依赖。如果仓库已定义框架、包名前缀、目录结构或技术选型，不得强行套用固定方案。
5. 将改动限制在用户授权的工作区内，保留无关修改，并根据风险程度验证结果。
6. 交付时先说明结果，再列出验证情况、遗留限制和生成文件的直接链接。

## Codex 兼容规则

- 使用 Codex 的计划、工作区工具、浏览器控制和受支持的多代理能力，不使用其他代理平台专属的斜杠命令或任务语法。
- 将旧框架名称视为可选示例。包名、模块前缀、路径、端口、主题和构建命令必须从当前仓库或用户明确输入中确定。
- 优先使用跨平台命令；在 Windows 上使用 PowerShell 原生文件操作和可用的工作区运行时。
- 在实际确认可用之前，不得声称外部工具、API、凭据或 MCP 服务已经存在。
- 处理特殊文件格式时，如当前环境已有兼容的 Codex 专用 Skill，应优先使用它完成文件操作，并用本 Skill 的领域资源补充项目规范。

## 内置资源
"""


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def resource_lines(skill_dir: Path) -> str:
    labels = {
        "scripts": "可执行脚本；仅在任务需要确定性处理或重复操作时使用。",
        "references": "参考说明；只读取当前任务需要的文件。",
        "assets": "模板和素材；按当前项目约定选择并复用。",
    }
    return "\n".join(
        f"- `{name}/`：{label}"
        for name, label in labels.items()
        if (skill_dir / name).exists()
    )


def localize_skill(name: str, title: str, description: str, short: str) -> None:
    skill_dir = SKILLS_ROOT / name
    body = f"""---
name: {name}
description: {description}
---

# {title}

{OPERATING_RULES}

{resource_lines(skill_dir)}
"""
    write_text(skill_dir / "SKILL.md", body)

    prompt = f"使用 ${name}，按照当前项目约定帮我完成这项任务。"
    yaml = f'''interface:
  display_name: "{title}"
  short_description: "{short}"
  default_prompt: "{prompt}"
'''
    write_text(skill_dir / "agents" / "openai.yaml", yaml)

    guide = skill_dir / "references" / "adapted-source-guide.md"
    if guide.exists():
        content = guide.read_text(encoding="utf-8")
        content = re.sub(r"\A# Adapted source guide", "# 适配后的来源指南", content)
        write_text(guide, content)


def write_report() -> None:
    lines = [
        "# Codex Skill 转换报告",
        "",
        "原始的 `skills/` 和 `说明手册/` 目录未被修改。",
        "",
        "## Skill 清单",
        "",
        "| Codex Skill | 中文名称 |",
        "|---|---|",
    ]
    lines.extend(f"| `{name}` | {title} |" for name, (title, _, _) in SKILLS.items())
    lines.extend([
        "",
        "## 设计说明",
        "",
        "- 所有 Skill 使用中性的 `toolkit-` 命名空间，以降低名称冲突风险。",
        "- 固定公司和项目假设已转换为可由当前项目配置的约定。",
        "- 其他代理平台的专属说明已转换为 Codex 概念。",
        "- 每个 Skill 都保留了详细来源指南和可复用资源。",
        "- Skill 的目录名和 `$toolkit-*` 调用名保持英文，以确保稳定识别；面向用户的说明已中文化。",
        "- 这些目录是可移植候选包，目前没有安装到用户级 Skill 目录。",
        "",
    ])
    write_text(SKILLS_ROOT / "CONVERSION_REPORT.md", "\n".join(lines))


def main() -> None:
    missing = [name for name in SKILLS if not (SKILLS_ROOT / name / "SKILL.md").exists()]
    if missing:
        raise SystemExit(f"缺少 Skill 目录：{', '.join(missing)}")
    for name, (title, description, short) in SKILLS.items():
        localize_skill(name, title, description, short)
    write_report()
    print(f"已中文化 {len(SKILLS)} 个 Skill 的说明文件。")


if __name__ == "__main__":
    main()
