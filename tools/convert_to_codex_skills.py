from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / "海川参考" / "skills"
OUTPUT = ROOT / "codex-skills"
INIT = Path(r"C:\Users\林圣颖\.codex\skills\.system\skill-creator\scripts\init_skill.py")


SKILLS = {
    "backend-architect": ("toolkit-backend-architect", "Backend Architect", "Design APIs, data models, service boundaries, and production backend implementations. Use for backend architecture, Spring Boot services, database design, API contracts, or server-side implementation."),
    "cc-design": ("toolkit-experience-designer", "Experience Designer", "Create high-fidelity HTML prototypes, interaction demos, visual explorations, and motion design artifacts. Use for UI mockups, interactive prototypes, design variants, or animated product demonstrations."),
    "code-reviewer": ("toolkit-code-reviewer", "Code Reviewer", "Review code for correctness, security, performance, maintainability, and regressions. Use for pull-request review, pre-release inspection, risk analysis, or actionable code-quality feedback."),
    "demand-analyzer": ("toolkit-requirements-analyst", "Requirements Analyst", "Turn rough product ideas into structured, testable requirements and PRDs. Use for requirements discovery, scope definition, acceptance criteria, user stories, or ambiguity resolution."),
    "devops-engineer": ("toolkit-devops-engineer", "DevOps Engineer", "Create and review deployment, container, CI/CD, observability, and operations configurations. Use for Docker, pipelines, Kubernetes, environment configuration, monitoring, or release automation."),
    "diagram": ("toolkit-diagram-generator", "Diagram Generator", "Create professional technical diagrams and data visualizations using PlantUML, Graphviz, Vega-Lite, HTML, Canvas, or infographic syntax. Use for architecture, UML, network, process, dependency, and data diagrams."),
    "frontend-engineer": ("toolkit-frontend-engineer", "Frontend Engineer", "Implement maintainable production frontends from requirements and API contracts. Use for Vue, React, TypeScript, component architecture, API integration, state handling, and responsive interfaces."),
    "gpt-image-prompt-generator": ("toolkit-image-prompt-writer", "Image Prompt Writer", "Write detailed production-ready prompts for image-generation models without generating the image. Use for photography, posters, products, characters, UI concepts, illustrations, or infographic prompts."),
    "hc-bi-dashboard": ("toolkit-bi-dashboard", "BI Dashboard Builder", "Build reusable data dashboards and large-screen visualization pages for the project's existing frontend stack. Use for BI dashboards, monitoring walls, GIS views, operational cockpits, or 1920x1080 data displays."),
    "hc-bi-widget-developer": ("toolkit-bi-widget", "BI Widget Developer", "Build configurable reusable visualization widgets for an existing dashboard framework. Use for charts, maps, KPI cards, progress views, text widgets, 3D scenes, interactions, or configuration panels."),
    "hc-quick-backend-module": ("toolkit-spring-module", "Spring Module Builder", "Scaffold configurable Spring Boot modules and generate conventional business-layer code. Use for new Java modules, CRUD services, DTOs, validation, persistence mappings, Feign clients, jobs, and environment configuration."),
    "html-doc-generator": ("toolkit-html-doc-site", "HTML Documentation Site", "Convert Markdown collections into portable static HTML documentation sites. Use for offline docs, browsable manuals, knowledge bases, or zero-server documentation delivery."),
    "image-gen": ("toolkit-visual-asset-generator", "Visual Asset Generator", "Produce visual asset files such as PNG, SVG, charts, icons, covers, banners, and dashboard backgrounds. Use when the requested deliverable is an actual image or vector asset rather than prompt text."),
    "karpathy-guidelines": ("toolkit-coding-guidelines", "Coding Guidelines", "Apply cautious, precise coding practices that minimize unnecessary complexity, expose assumptions, define verification targets, and avoid silent failure. Use while implementing, refactoring, or reviewing code."),
    "mcp-builder": ("toolkit-mcp-builder", "MCP Builder", "Design, implement, and evaluate Model Context Protocol servers in Python or TypeScript. Use for exposing APIs, data sources, or services as MCP tools and resources."),
    "ppt-engine": ("toolkit-visual-presentation", "Visual Presentation Builder", "Create image-led presentation decks through an end-to-end visual pipeline. Use for launch decks, pitch decks, brand presentations, or slides where visual impact matters more than editable text."),
    "ppt-master": ("toolkit-editable-presentation", "Editable Presentation Builder", "Create editable vector-based presentation decks from documents, URLs, or Markdown with precise SVG layouts and speaker notes. Use for PPTX delivery where text editability and structured layout matter."),
    "project-bootstrap": ("toolkit-codex-project-bootstrap", "Codex Project Bootstrap", "Initialize a repository for effective Codex collaboration by creating or improving AGENTS.md and project-scoped guidance. Use for first-time workspace setup, repository onboarding, or project instruction configuration."),
    "prompt-master": ("toolkit-prompt-writer", "Prompt Writer", "Create a new clear and executable prompt from a rough goal for LLMs, coding agents, image tools, or other AI systems. Use when writing a prompt from scratch rather than revising an existing prompt."),
    "prompt-optimizer": ("toolkit-prompt-optimizer", "Prompt Optimizer", "Analyze and improve an existing prompt using an appropriate prompting framework. Use when refining clarity, constraints, structure, reliability, or output formatting of a supplied prompt."),
    "qa-tester": ("toolkit-qa-tester", "QA Tester", "Design and execute focused black-box test cases and produce evidence-based QA reports. Use for page, API, performance, acceptance, regression, and pre-release verification."),
    "skill-creator": ("toolkit-skill-workbench", "Skill Workbench", "Create or revise portable Codex skills with concise instructions, reusable resources, UI metadata, validation, and iterative evaluation. Use for authoring or structurally improving a skill."),
    "skill-evaluator": ("toolkit-skill-evaluator", "Skill Evaluator", "Evaluate existing skills for trigger quality, structure, usability, conflicts, and output effectiveness. Use for scoring, comparing, auditing, or recommending improvements to skills without rewriting them by default."),
    "smart-ui-designer": ("toolkit-ui-system-designer", "UI System Designer", "Define reusable UI design systems, color and typography rules, layouts, component guidance, and reference-site design language. Use before implementation when a coherent visual system is needed."),
    "test-coordinator": ("toolkit-test-coordinator", "Test Coordinator", "Coordinate iterative test, defect triage, fix, and regression cycles across frontend and backend work. Use for end-to-end QA workflows that continue until exit criteria are met."),
    "vibe-design-coder": ("toolkit-rapid-ui-prototyper", "Rapid UI Prototyper", "Turn natural-language product requirements into runnable UI prototypes quickly. Use for early-stage Vue, React, or HTML prototypes, layout exploration, forms, admin pages, mobile views, and dashboards."),
    "workflow-controller": ("toolkit-delivery-workflow", "Delivery Workflow Controller", "Coordinate an end-to-end software delivery workflow across requirements, architecture, prototyping, implementation, review, testing, fixes, and handoff. Use when a user requests a complete project or multi-stage feature delivery."),
}


TEXT_REPLACEMENTS = {
    "Claude Code": "Codex",
    "CLAUDE.md": "AGENTS.md",
    ".claudeignore": ".gitignore",
    "Claude": "Codex",
    "chrome-devtools MCP": "the available browser-control capability",
    "chrome-devtools": "browser-control tools",
    "Task tool": "multi-agent tools when explicitly requested or permitted",
    "Agent tool": "multi-agent tools when explicitly requested or permitted",
    "run_in_background=true": "an available asynchronous execution mechanism",
    "/goal": "an explicit completion objective",
    "海川后端微服务模块": "Spring Boot service module",
    "海川后端": "Spring Boot backend",
    "海川框架": "the project's existing framework",
    "海川项目": "the current project",
    "海川大屏框架": "the project's dashboard framework",
    "海川": "project-specific",
    "vue-bigscreen-widgets": "the project's visualization component library",
    "fjpark-backend-{module-name}": "{backend-prefix}-{module-name}",
    "fjpark": "project",
}


def adapted(text: str) -> str:
    for old, new in TEXT_REPLACEMENTS.items():
        text = text.replace(old, new)
    for old, (new, _, _) in SKILLS.items():
        text = re.sub(rf"(?<![\w-]){re.escape(old)}(?![\w-])", new, text)
    text = text.replace("python3 ", "python ")
    return text


def split_frontmatter(text: str) -> str:
    match = re.match(r"\A---\s*\r?\n.*?\r?\n---\s*\r?\n", text, flags=re.S)
    return text[match.end():] if match else text


def resource_dirs(source_dir: Path) -> list[str]:
    allowed = [name for name in ("scripts", "references", "assets") if (source_dir / name).exists()]
    # Preserve template and workflow libraries as output assets/references after initialization.
    if any((source_dir / name).exists() for name in ("templates", "workflows", "data", "evals", "demos", "agents", "architecture", "canvas", "examples", "graphviz", "infocard", "infographic", "stencils", "vega")):
        if "assets" not in allowed:
            allowed.append("assets")
    return allowed


def write_utf8(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def copy_resources(source_dir: Path, dest_dir: Path) -> None:
    for item in source_dir.iterdir():
        if item.name in {"SKILL.md", "README.md", "README.en.md", "agents"}:
            continue
        target_parent = dest_dir
        if item.name in {"templates", "workflows", "data", "evals", "demos", "architecture", "canvas", "examples", "graphviz", "infocard", "infographic", "stencils", "vega"}:
            target_parent = dest_dir / "assets"
        target = target_parent / item.name
        if target.exists():
            shutil.rmtree(target) if target.is_dir() else target.unlink()
        if item.is_dir():
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)

    # Adapt text resources without touching binaries.
    text_exts = {".md", ".txt", ".py", ".js", ".mjs", ".sh", ".json", ".yaml", ".yml", ".html", ".java", ".xml"}
    for path in dest_dir.rglob("*"):
        if path.is_file() and path.suffix.lower() in text_exts:
            try:
                write_utf8(path, adapted(path.read_text(encoding="utf-8")))
            except UnicodeDecodeError:
                pass


def make_skill_md(old: str, new: str, title: str, description: str, source_dir: Path, dest_dir: Path) -> None:
    original = source_dir.joinpath("SKILL.md").read_text(encoding="utf-8")
    guide_body = adapted(split_frontmatter(original)).strip() + "\n"
    reference = dest_dir / "references" / "adapted-source-guide.md"
    write_utf8(reference, "# Adapted source guide\n\n" + guide_body)

    available = []
    for name in ("scripts", "references", "assets"):
        if (dest_dir / name).exists():
            available.append(f"- `{name}/`: inspect and use only the resources relevant to the current task.")
    resources = "\n".join(available)
    body = f'''---
name: {new}
description: {description}
---

# {title}

## Operating rules

1. Inspect the current workspace and read applicable `AGENTS.md` files before acting.
2. Confirm the requested deliverable, constraints, existing stack, and acceptance evidence from local context. Ask only when a missing choice would materially change the result.
3. Read `references/adapted-source-guide.md` completely before executing this skill. Treat this file as detailed domain guidance, while the Codex compatibility rules below take precedence.
4. Reuse the project's established conventions and dependencies. Do not impose a fixed company framework, package prefix, directory layout, or technology when the repository already defines one.
5. Keep changes inside the user-authorized workspace. Preserve unrelated edits and verify the result in proportion to risk.
6. Lead the handoff with the outcome, verification performed, remaining limitations, and direct links to generated files.

## Codex compatibility

- Use Codex plans, workspace tools, browser controls, and supported multi-agent features instead of Claude-specific slash commands or Task/Agent syntax.
- Treat references to legacy framework names as optional examples. Derive package names, module prefixes, paths, ports, themes, and build commands from the current repository or explicit user input.
- Prefer cross-platform commands. On Windows, use PowerShell-native filesystem operations and the available workspace runtime paths.
- Do not claim external tools, APIs, credentials, or MCP servers are available until they are actually present.
- For specialized artifact formats, use the installed Codex artifact skill when one is available and compatible; use this skill's domain resources to supply project-specific conventions.

## Bundled resources

{resources}
'''
    write_utf8(dest_dir / "SKILL.md", body)


def init_skill(old: str, new: str, title: str, description: str) -> Path:
    source_dir = SOURCE / old
    existing = OUTPUT / new
    if existing.exists():
        skill_text = existing.joinpath("SKILL.md").read_text(encoding="utf-8", errors="ignore") if existing.joinpath("SKILL.md").exists() else ""
        if "## Operating rules" in skill_text:
            return existing
        shutil.rmtree(existing)
    resources = resource_dirs(source_dir)
    short = description.split(". Use", 1)[0]
    if len(short) < 25:
        short = f"Reusable {title.lower()} workflow for Codex"
    short = short[:64].rstrip(" ,.;")
    prompt = f"Use ${new} to help me complete this task using the current project's conventions."
    cmd = [sys.executable, str(INIT), new, "--path", str(OUTPUT)]
    if resources:
        cmd.extend(["--resources", ",".join(resources)])
    cmd.extend(["--interface", f"display_name={title}"])
    cmd.extend(["--interface", f"short_description={short}"])
    cmd.extend(["--interface", f"default_prompt={prompt}"])
    subprocess.run(cmd, check=True)
    return OUTPUT / new


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for old, (new, title, description) in SKILLS.items():
        dest = init_skill(old, new, title, description)
        existing_text = dest.joinpath("SKILL.md").read_text(encoding="utf-8", errors="ignore")
        if "## Operating rules" in existing_text:
            rows.append((old, new))
            continue
        copy_resources(SOURCE / old, dest)
        make_skill_md(old, new, title, description, SOURCE / old, dest)
        rows.append((old, new))

    report = [
        "# Codex Skill Conversion Report",
        "",
        "The original `skills/` and `说明手册/` directories were not modified.",
        "",
        "## Name mapping",
        "",
        "| Source | Codex skill |",
        "|---|---|",
    ]
    report.extend(f"| `{old}` | `{new}` |" for old, new in rows)
    report.extend([
        "",
        "## Design choices",
        "",
        "- All skills use the neutral `toolkit-` namespace to avoid collisions.",
        "- Company-specific assumptions were converted into project-configurable conventions.",
        "- Claude-specific instructions were translated to Codex concepts.",
        "- Detailed source instructions and reusable resources were retained inside each converted skill.",
        "- These folders are portable packages; copy selected folders into the Codex skills directory to install them.",
        "",
    ])
    write_utf8(OUTPUT / "CONVERSION_REPORT.md", "\n".join(report))
    localizer = ROOT / "tools" / "localize_skill_docs_zh.py"
    if localizer.exists():
        subprocess.run([sys.executable, str(localizer)], check=True)
    print(f"Created {len(rows)} skills in {OUTPUT}")


if __name__ == "__main__":
    main()
