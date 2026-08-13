#!/usr/bin/env python3
"""
Generate a human-readable diagnostic report from workflow-status.json.

Usage:
    python scripts/generate_workflow_report.py
    python scripts/generate_workflow_report.py -o doc/diagnostic-report.md
"""

import json
import os
import sys
import argparse
from datetime import datetime, timezone


def load_status(path):
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def iso_to_local(iso_str):
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except (ValueError, AttributeError):
        return iso_str or "N/A"


def format_duration(seconds):
    if seconds is None:
        return "N/A"
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    if hours > 0:
        return f"{hours}h {minutes}m"
    return f"{minutes}m"


def phase_name_cn(phase):
    mapping = {
        "config-init": "配置初始化",
        "demand-confirm": "需求分析",
        "architecting": "架构设计",
        "prototyping": "UI原型",
        "backend-dev": "后端开发",
        "frontend-dev": "前端开发",
        "code-review": "代码审查",
        "testing": "测试验证",
        "bugfix": "BUG修复",
        "delivered": "已交付",
    }
    return mapping.get(phase, phase)


def generate_report(status, workspace_root):
    lines = []
    lines.append(f"# 工作流诊断报告")
    lines.append(f"")
    lines.append(f"> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"> 工作目录: {workspace_root}")
    lines.append(f"")

    project = status.get("config", {}).get("projectName", "N/A")
    lines.append(f"## 项目信息")
    lines.append(f"")
    lines.append(f"| 属性 | 值 |")
    lines.append(f"|------|----|")
    lines.append(f"| 项目名称 | {project} |")
    lines.append(f"| 开发模式 | {status.get('mode', 'full')} |")
    lines.append(f"| 项目类型 | {status.get('projectType', 'general')} |")
    lines.append(f"| 启动时间 | {iso_to_local(status.get('startTime', ''))} |")
    lines.append(f"")
    lines.append(f"## 阶段进展")
    lines.append(f"")
    lines.append(f"| 阶段 | 状态 | 完成时间 |")
    lines.append(f"|------|------|----------|")
    for entry in status.get("phaseHistory", []):
        phase_cn = phase_name_cn(entry.get("phase", ""))
        status_tag = entry.get("status", "N/A")
        time_str = iso_to_local(entry.get("time", ""))
        lines.append(f"| {phase_cn} | {status_tag} | {time_str} |")
    lines.append(f"")
    lines.append(f"**当前阶段**: {phase_name_cn(status.get('currentPhase', 'N/A'))}")
    lines.append(f"")

    lines.append(f"## 开发进度")
    lines.append(f"")
    dp = status.get("developmentProgress")
    if dp and dp.get("totalModules", 0) > 0:
        total = dp["totalModules"]
        completed = dp["completedModules"]
        pct = int(completed / total * 100) if total > 0 else 0
        lines.append(f"- **总体**: {completed}/{total} ({pct}%)")
        current = dp.get("currentModule", "")
        if current:
            lines.append(f"- **当前模块**: {current}")
        lines.append(f"")
        for layer in ("backend", "frontend"):
            layer_data = dp.get(layer, {})
            modules = layer_data.get("modules", [])
            if modules:
                lines.append(f"### {layer.replace('backend', '后端').replace('frontend', '前端')}")
                lines.append(f"")
                lines.append(f"| 模块 | 状态 | 完成时间 |")
                lines.append(f"|------|------|----------|")
                for m in modules:
                    name = m.get("name", "?")
                    status = m.get("status", "?")
                    completed_at = iso_to_local(m.get("completedAt", "")) if m.get("status") == "done" else "-"
                    icon = {"done": "✅", "in-progress": "🔄", "pending": "⏳"}.get(status, "❓")
                    lines.append(f"| {icon} {name} | {status} | {completed_at} |")
                lines.append(f"")
    else:
        lines.append(f"*（未启用模块级进度追踪或尚未开始开发）*")
        lines.append(f"")

    lines.append(f"## 问题追踪")
    lines.append(f"")

    bugs_found = status.get("bugsFound", 0)
    bugs_fixed = status.get("bugsFixed", 0)
    remaining = status.get("bugsRemaining", {})
    lines.append(f"| 类别 | 数量 |")
    lines.append(f"|------|------|")
    lines.append(f"| 发现 BUG | {bugs_found} |")
    lines.append(f"| 已修复 | {bugs_fixed} |")
    lines.append(f"| 剩余 Critical | {remaining.get('critical', 0)} |")
    lines.append(f"| 剩余 Warning | {remaining.get('warning', 0)} |")
    lines.append(f"| 剩余 Info | {remaining.get('info', 0)} |")
    lines.append(f"")

    findings = status.get("reviewFindings", {})
    lines.append(f"| 代码审查 | 数量 |")
    lines.append(f"|----------|------|")
    lines.append(f"| Critical | {findings.get('critical', 0)} |")
    lines.append(f"| Warning | {findings.get('warning', 0)} |")
    lines.append(f"| Info | {findings.get('info', 0)} |")
    lines.append(f"| 阻塞状态 | {'阻塞' if status.get('reviewBlocked') else '通过'} |")
    lines.append(f"")

    lines.append(f"### 修复历史")
    lines.append(f"")
    history = status.get("bugFixHistory", [])
    if history:
        lines.append(f"| 轮次 | 发现 | 修复 | 剩余 | 时间 |")
        lines.append(f"|------|------|------|------|------|")
        for entry in history:
            r = entry.get("round", "?")
            f = entry.get("found", "?")
            fix = entry.get("fixed", "?")
            rem = entry.get("remaining", "?")
            t = iso_to_local(entry.get("time", ""))
            lines.append(f"| {r} | {f} | {fix} | {rem} | {t} |")
    else:
        lines.append(f"*（暂无修复历史）*")
    lines.append(f"")

    lines.append(f"## 降级状态")
    lines.append(f"")

    review_fix = status.get("reviewFix")
    if review_fix:
        npc = review_fix.get("noProgressCount", 0)
        lines.append(f"### Code Review 修复降级")
        lines.append(f"")
        lines.append(f"| 指标 | 值 |")
        lines.append(f"|------|----|")
        lines.append(f"| 无进步轮次 | {npc}/3 |")
        lines.append(f"| 当前迭代 | {review_fix.get('iteration', 0)} |")
        summary = review_fix.get("lastFixSummary", {})
        lines.append(f"| 上轮结果 | {summary.get('result', 'N/A')} |")
        if npc >= 1:
            lines.append(f"| ⚠️ 降级级别 | {'自动 defer' if npc == 1 else ('简化方案' if npc == 2 else '用户干预')} |")
        lines.append(f"")

    bugfix_rem = status.get("bugFixRemediation")
    if bugfix_rem:
        npc = bugfix_rem.get("noProgressCount", 0)
        lines.append(f"### BUG 修复降级")
        lines.append(f"")
        lines.append(f"| 指标 | 值 |")
        lines.append(f"|------|----|")
        lines.append(f"| 无进步轮次 | {npc}/3 |")
        summary = bugfix_rem.get("lastFixSummary", {})
        lines.append(f"| 上轮结果 | {summary.get('result', 'N/A')} |")
        lines.append(f"| 推迟BUG数 | {summary.get('deferredCount', 0)} |")
        lines.append(f"| 简化BUG数 | {summary.get('simplifiedCount', 0)} |")
        if npc >= 1:
            lines.append(f"| ⚠️ 降级级别 | {'自动 defer' if npc == 1 else ('简化方案' if npc == 2 else '用户干预')} |")
        lines.append(f"")

    if (not review_fix or review_fix.get("noProgressCount", 0) == 0) and \
       (not bugfix_rem or bugfix_rem.get("noProgressCount", 0) == 0):
        lines.append(f"*（未触发降级，修复进展正常）*")
    lines.append(f"")

    lines.append(f"## 事件记录")
    lines.append(f"")

    rollbacks = status.get("rollbackHistory", [])
    if rollbacks:
        lines.append(f"### 阶段回退")
        lines.append(f"")
        lines.append(f"| 从 | 回退到 | 原因 | 时间 |")
        lines.append(f"|----|--------|------|------|")
        for rb in rollbacks:
            lines.append(f"| {rb.get('from', '?')} | {rb.get('to', '?')} | {rb.get('reason', '?')} | {iso_to_local(rb.get('time', ''))} |")
        lines.append(f"")

    retries = status.get("retryHistory", [])
    if retries:
        lines.append(f"### 重试记录")
        lines.append(f"")
        lines.append(f"| Skill | 错误 | 重试次数 | 时间 |")
        lines.append(f"|-------|------|----------|------|")
        for rt in retries:
            lines.append(f"| {rt.get('skill', '?')} | {rt.get('error', '?')} | {rt.get('retries', '?')} | {iso_to_local(rt.get('time', ''))} |")
        lines.append(f"")

    if not rollbacks and not retries:
        lines.append(f"*（无回退或重试记录）*")
        lines.append(f"")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate diagnostic report from workflow status")
    parser.add_argument("--status-file", default="doc/workflow-status.json",
                        help="Path to workflow-status.json")
    parser.add_argument("--output", "-o",
                        help="Output file path (prints to stdout if omitted)")
    parser.add_argument("--workspace", "-w", default=".",
                        help="Workspace root directory (default: cwd)")
    args = parser.parse_args()

    workspace = os.path.abspath(args.workspace)
    status_path = os.path.join(workspace, args.status_file)

    if not os.path.isfile(status_path):
        print(f"ERROR: workflow-status.json not found at {status_path}")
        sys.exit(1)

    status = load_status(status_path)
    if status is None:
        print(f"ERROR: Failed to read {status_path}")
        sys.exit(1)

    report = generate_report(status, workspace)

    if args.output:
        output_path = os.path.join(workspace, args.output)
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"Report written to: {output_path}")
    else:
        print(report)


if __name__ == "__main__":
    main()
