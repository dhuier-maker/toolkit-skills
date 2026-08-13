#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Smart UI Designer - Design System Generator
Generates comprehensive design system recommendations
"""

import csv
import json
import os
from datetime import datetime
from pathlib import Path
from core import search, DATA_DIR

# ============ CONFIGURATION ============
SEARCH_CONFIG = {
    "style": {"max_results": 2},
    "color": {"max_results": 1},
    "component": {"max_results": 3},
    "pattern": {"max_results": 1}
}

# Project type detection rules
PROJECT_RULES = {
    "admin": {
        "keywords": ["后台", "管理", "admin", "cms", "erp", "crm", "管理系统"],
        "default_style": "Modern Clean",
        "default_pattern": "Sidebar + Header + Content",
        "primary_color": "#1890ff"
    },
    "bi": {
        "keywords": ["大屏", "bi", "dashboard", "数据可视化", "驾驶舱", "监控"],
        "default_style": "Tech Dark",
        "default_pattern": "Grid Layout",
        "primary_color": "#00d4ff"
    },
    "mobile": {
        "keywords": ["移动端", "手机", "app", "小程序", "h5", "mobile"],
        "default_style": "Minimal Mobile",
        "default_pattern": "Tab Bar Navigation",
        "primary_color": "#07c160"
    },
    "landing": {
        "keywords": ["落地页", "官网", "landing", "首页", "宣传页"],
        "default_style": "Hero Centric",
        "default_pattern": "Hero + Features + CTA",
        "primary_color": "#2563eb"
    },
    "prototype": {
        "keywords": ["原型", "prototype", "demo", "演示"],
        "default_style": "Wireframe",
        "default_pattern": "Simple Layout",
        "primary_color": "#6b7280"
    }
}


class DesignSystemGenerator:
    """Generates design system recommendations"""

    def __init__(self):
        self.project_rules = PROJECT_RULES

    def detect_project_type(self, query: str) -> dict:
        """Detect project type from query"""
        query_lower = query.lower()

        for ptype, rule in self.project_rules.items():
            for kw in rule["keywords"]:
                if kw in query_lower:
                    return {"type": ptype, **rule}

        return {
            "type": "general",
            "default_style": "Modern Clean",
            "default_pattern": "Standard Layout",
            "primary_color": "#1890ff"
        }

    def generate(self, query: str, project_name: str = None, stack: str = "vue3") -> dict:
        """Generate complete design system recommendation"""
        # Step 1: Detect project type
        project_info = self.detect_project_type(query)

        # Step 2: Multi-domain search
        search_results = {}
        for domain, config in SEARCH_CONFIG.items():
            search_results[domain] = search(query, domain, config["max_results"])

        # Step 3: Extract best matches
        style_results = search_results["style"].get("results", [])
        color_results = search_results["color"].get("results", [])
        component_results = search_results["component"].get("results", [])
        pattern_results = search_results["pattern"].get("results", [])

        best_style = style_results[0] if style_results else {
            "Style Name": project_info["default_style"],
            "Category": "General",
            "Keywords": "现代简约",
            "Colors": "#1890ff, #52c41a, #faad14",
            "Effects": "平滑过渡动画",
            "Best For": "通用项目",
            "Complexity": "中等",
            "Accessibility": "良好"
        }

        best_color = color_results[0] if color_results else {
            "Theme Name": "默认主题",
            "Primary": project_info["primary_color"],
            "Secondary": "#52c41a",
            "Accent": "#faad14",
            "Background": "#ffffff",
            "Foreground": "#1f2937",
            "Border": "#e5e7eb",
            "Notes": "通用配色方案"
        }

        best_pattern = pattern_results[0] if pattern_results else {
            "Pattern Name": project_info["default_pattern"],
            "Category": "Layout",
            "Use Case": query,
            "Structure": "Header + Main + Footer",
            "Best Practices": "保持简洁，突出重点",
            "Anti Patterns": "避免过度装饰"
        }

        # Step 4: Build design system
        return {
            "project_name": project_name or query,
            "project_type": project_info["type"],
            "stack": stack,
            "style": {
                "name": best_style.get("Style Name", "Modern Clean"),
                "category": best_style.get("Category", "General"),
                "keywords": best_style.get("Keywords", ""),
                "colors": best_style.get("Colors", ""),
                "effects": best_style.get("Effects", ""),
                "best_for": best_style.get("Best For", ""),
                "complexity": best_style.get("Complexity", "中等"),
                "accessibility": best_style.get("Accessibility", "良好")
            },
            "colors": {
                "primary": best_color.get("Primary", "#1890ff"),
                "secondary": best_color.get("Secondary", "#52c41a"),
                "accent": best_color.get("Accent", "#faad14"),
                "background": best_color.get("Background", "#ffffff"),
                "foreground": best_color.get("Foreground", "#1f2937"),
                "border": best_color.get("Border", "#e5e7eb"),
                "notes": best_color.get("Notes", "")
            },
            "pattern": {
                "name": best_pattern.get("Pattern Name", "Standard Layout"),
                "category": best_pattern.get("Category", "Layout"),
                "structure": best_pattern.get("Structure", "Header + Main + Footer"),
                "best_practices": best_pattern.get("Best Practices", ""),
                "anti_patterns": best_pattern.get("Anti Patterns", "")
            },
            "components": component_results[:5] if component_results else [],
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }


# ============ OUTPUT FORMATTERS ============
def format_ascii_box(ds: dict) -> str:
    """Format design system as ASCII box"""
    lines = []
    w = 80

    lines.append("╔" + "═" * (w-2) + "╗")
    lines.append(f"║  Smart UI Designer - 设计系统: {ds['project_name']}".ljust(w-1) + "║")
    lines.append("╚" + "═" * (w-2) + "╝")
    lines.append("┌" + "─" * (w-2) + "┐")

    # Project Info
    lines.append(f"│  项目类型: {ds['project_type']}  |  技术栈: {ds['stack']}".ljust(w-1) + "│")
    lines.append("├" + "─" * (w-2) + "┤")

    # Style
    lines.append("│  【设计风格】".ljust(w-1) + "│")
    lines.append(f"│    名称: {ds['style']['name']}".ljust(w-1) + "│")
    lines.append(f"│    关键词: {ds['style']['keywords']}".ljust(w-1) + "│")
    lines.append(f"│    适用: {ds['style']['best_for']}".ljust(w-1) + "│")
    lines.append("├" + "─" * (w-2) + "┤")

    # Colors
    lines.append("│  【配色方案】".ljust(w-1) + "│")
    lines.append(f"│    主色: {ds['colors']['primary']}".ljust(w-1) + "│")
    lines.append(f"│    辅色: {ds['colors']['secondary']}".ljust(w-1) + "│")
    lines.append(f"│    强调: {ds['colors']['accent']}".ljust(w-1) + "│")
    lines.append(f"│    背景: {ds['colors']['background']}".ljust(w-1) + "│")
    lines.append("├" + "─" * (w-2) + "┤")

    # Pattern
    lines.append("│  【布局模式】".ljust(w-1) + "│")
    lines.append(f"│    名称: {ds['pattern']['name']}".ljust(w-1) + "│")
    lines.append(f"│    结构: {ds['pattern']['structure']}".ljust(w-1) + "│")
    lines.append("├" + "─" * (w-2) + "┤")

    # Components
    if ds['components']:
        lines.append("│  【推荐组件】".ljust(w-1) + "│")
        for comp in ds['components'][:3]:
            comp_name = comp.get('Component Name', 'Unknown')
            lines.append(f"│    - {comp_name}".ljust(w-1) + "│")

    lines.append("└" + "─" * (w-2) + "┘")

    return "\n".join(lines)


def format_markdown(ds: dict) -> str:
    """Format design system as Markdown"""
    lines = []

    lines.append(f"# 设计系统: {ds['project_name']}")
    lines.append("")
    lines.append(f"> 项目类型: **{ds['project_type']}** | 技术栈: **{ds['stack']}**")
    lines.append(f"> 生成时间: {ds['generated_at']}")
    lines.append("")

    # Style
    lines.append("## 设计风格")
    lines.append("")
    lines.append(f"- **名称:** {ds['style']['name']}")
    lines.append(f"- **关键词:** {ds['style']['keywords']}")
    lines.append(f"- **适用场景:** {ds['style']['best_for']}")
    lines.append(f"- **复杂度:** {ds['style']['complexity']}")
    lines.append(f"- **无障碍:** {ds['style']['accessibility']}")
    lines.append("")

    # Colors
    lines.append("## 配色方案")
    lines.append("")
    lines.append("| 角色 | 色值 | CSS 变量 |")
    lines.append("|------|------|----------|")
    lines.append(f"| 主色 | `{ds['colors']['primary']}` | `--color-primary` |")
    lines.append(f"| 辅色 | `{ds['colors']['secondary']}` | `--color-secondary` |")
    lines.append(f"| 强调 | `{ds['colors']['accent']}` | `--color-accent` |")
    lines.append(f"| 背景 | `{ds['colors']['background']}` | `--color-background` |")
    lines.append(f"| 前景 | `{ds['colors']['foreground']}` | `--color-foreground` |")
    lines.append(f"| 边框 | `{ds['colors']['border']}` | `--color-border` |")
    if ds['colors']['notes']:
        lines.append("")
        lines.append(f"*{ds['colors']['notes']}*")
    lines.append("")

    # Pattern
    lines.append("## 布局模式")
    lines.append("")
    lines.append(f"- **名称:** {ds['pattern']['name']}")
    lines.append(f"- **结构:** {ds['pattern']['structure']}")
    if ds['pattern']['best_practices']:
        lines.append(f"- **最佳实践:** {ds['pattern']['best_practices']}")
    if ds['pattern']['anti_patterns']:
        lines.append(f"- **避免:** {ds['pattern']['anti_patterns']}")
    lines.append("")

    # Components
    if ds['components']:
        lines.append("## 推荐组件")
        lines.append("")
        for comp in ds['components']:
            name = comp.get('Component Name', 'Unknown')
            category = comp.get('Category', '')
            stack = comp.get('Stack', '')
            lines.append(f"- **{name}** ({category}) - {stack}")
        lines.append("")

    return "\n".join(lines)


def generate_design_system(query: str, project_name: str = None, stack: str = "vue3",
                           output_format: str = "ascii", persist: bool = False,
                           output_dir: str = None) -> str:
    """
    Main entry point for design system generation.

    Args:
        query: Search query (e.g., "后台管理系统", "BI大屏")
        project_name: Optional project name
        stack: Tech stack (vue3, uniapp, react, html-tailwind)
        output_format: "ascii" or "markdown"
        persist: If True, save to design-system/ folder
        output_dir: Optional output directory

    Returns:
        Formatted design system string
    """
    generator = DesignSystemGenerator()
    ds = generator.generate(query, project_name, stack)

    if persist:
        persist_design_system(ds, output_dir)

    if output_format == "markdown":
        return format_markdown(ds)
    return format_ascii_box(ds)


def persist_design_system(ds: dict, output_dir: str = None):
    """Persist design system to files"""
    base_dir = Path(output_dir) if output_dir else Path.cwd()
    design_system_dir = base_dir / "design-system"
    design_system_dir.mkdir(parents=True, exist_ok=True)

    master_file = design_system_dir / "MASTER.md"
    content = format_markdown(ds)

    with open(master_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return str(master_file)


# ============ CLI SUPPORT ============
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Smart UI Designer - 设计系统生成器")
    parser.add_argument("query", help="搜索查询 (如: '后台管理系统', 'BI大屏')")
    parser.add_argument("--project-name", "-p", type=str, default=None, help="项目名称")
    parser.add_argument("--stack", "-s", choices=AVAILABLE_STACKS, default="vue3", help="技术栈")
    parser.add_argument("--format", "-f", choices=["ascii", "markdown"], default="ascii", help="输出格式")
    parser.add_argument("--persist", action="store_true", help="保存到 design-system/ 目录")

    args = parser.parse_args()

    result = generate_design_system(args.query, args.project_name, args.stack, args.format, args.persist)
    print(result)
