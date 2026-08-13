#!/usr/bin/env python3
"""
Validate that each workflow phase's output artifacts exist.

Usage:
    python scripts/validate_phase_output.py                    # check all phases
    python scripts/validate_phase_output.py --phase 4           # check specific phase
    python scripts/validate_phase_output.py --json             # JSON output
"""

import json
import os
import sys
import argparse
import glob as glob_mod


PHASE_CHECKS = {
    "1": {
        "name": "需求分析",
        "artifacts": [
            {"path": "doc/PRD.md", "minSize": 100, "desc": "PRD文档"}
        ]
    },
    "2": {
        "name": "架构设计",
        "artifacts": [
            {"path": "doc/API.md", "minSize": 100, "desc": "API总览文档"},
            {"path": "doc/api/", "type": "dir_nonempty", "desc": "API详细规范目录"},
        ]
    },
    "3": {
        "name": "UI原型",
        "optional": True,
        "artifacts": [
            {"path": "prototypes/", "type": "dir_nonempty", "desc": "原型文件目录"},
        ]
    },
    "4": {
        "name": "后端开发",
        "artifacts": [
            {"path": "src/main/java", "type": "dir_with_java", "desc": "后端Java代码目录"},
        ]
    },
    "5": {
        "name": "前端开发",
        "artifacts": [
            {"path": "src/", "type": "dir_with_frontend", "desc": "前端代码目录"},
        ]
    },
    "6": {
        "name": "代码审查",
        "artifacts": [
            {"path": "doc/code-review-report.md", "minSize": 50, "desc": "代码审查报告"},
        ]
    },
    "7": {
        "name": "测试验证",
        "artifacts": [
            {"path": "doc/QA_Report.md", "minSize": 50, "desc": "测试报告"},
        ]
    },
}


def check_file(path, min_size=None):
    if not os.path.isfile(path):
        return False, f"file not found"
    if min_size is not None:
        size = os.path.getsize(path)
        if size < min_size:
            return False, f"file too small ({size} bytes, expected >= {min_size})"
    return True, "ok"


def check_dir_nonempty(path):
    if not os.path.isdir(path):
        return False, f"directory not found"
    entries = [e for e in os.listdir(path) if not e.startswith(".")]
    if not entries:
        return False, f"directory is empty"
    return True, f"{len(entries)} entries"


def check_dir_with_java(path):
    if not os.path.isdir(path):
        return False, f"directory not found"
    java_files = glob_mod.glob(os.path.join(path, "**", "*.java"), recursive=True)
    if not java_files:
        return False, f"no .java files found"
    return True, f"{len(java_files)} .java files"


def check_dir_with_frontend(path):
    if not os.path.isdir(path):
        return False, f"directory not found"
    patterns = ["**/*.vue", "**/*.tsx", "**/*.jsx", "**/*.ts", "**/*.js"]
    found = False
    for pattern in patterns:
        files = glob_mod.glob(os.path.join(path, pattern), recursive=True)
        if files:
            found = True
            break
    if not found:
        return False, f"no .vue/.tsx/.jsx/.ts/.js files found"
    return True, "ok"


TYPE_CHECKERS = {
    "dir_nonempty": check_dir_nonempty,
    "dir_with_java": check_dir_with_java,
    "dir_with_frontend": check_dir_with_frontend,
}


def validate_artifact(artifact, workspace):
    path = os.path.join(workspace, artifact["path"])
    typ = artifact.get("type", "file")
    if typ in TYPE_CHECKERS:
        ok, detail = TYPE_CHECKERS[typ](path)
    else:
        ok, detail = check_file(path, artifact.get("minSize"))
    return ok, detail


def load_status(workspace):
    path = os.path.join(workspace, "doc", "workflow-status.json")
    if not os.path.isfile(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def get_completed_phases(status_data):
    phases = set()
    for entry in status_data.get("phaseHistory", []):
        if entry.get("status") == "completed":
            phase_name = entry.get("phase", "")
            mapping = {
                "demand-confirm": "1",
                "architecting": "2",
                "prototyping": "3",
                "backend-dev": "4",
                "frontend-dev": "5",
                "code-review": "6",
                "testing": "7",
            }
            if phase_name in mapping:
                phases.add(mapping[phase_name])
    return phases


def main():
    parser = argparse.ArgumentParser(description="Validate workflow phase output artifacts")
    parser.add_argument("--phase", "-p",
                        help="Check a specific phase (1-7)")
    parser.add_argument("--workspace", "-w", default=".",
                        help="Workspace root directory (default: cwd)")
    parser.add_argument("--json", action="store_true",
                        help="Output results as JSON")
    args = parser.parse_args()

    workspace = os.path.abspath(args.workspace)
    status = load_status(workspace)
    completed_phases = get_completed_phases(status) if status else set()

    results = {}
    all_ok = True

    if args.phase:
        phases_to_check = {args.phase: PHASE_CHECKS[args.phase]}
    else:
        phases_to_check = PHASE_CHECKS
        if status:
            current = status.get("currentPhase", "")
            if args.json is False:
                print(f"Workspace: {workspace}")
                print(f"Current phase: {current or 'N/A'}")
                if completed_phases:
                    print(f"Completed phases: {', '.join(sorted(completed_phases))}")
                print()

    for phase_key, phase_def in phases_to_check.items():
        artifacts = phase_def.get("artifacts", [])
        is_optional = phase_def.get("optional", False)
        phase_ok = True
        artifact_results = []

        for artifact in artifacts:
            ok, detail = validate_artifact(artifact, workspace)
            if not ok and is_optional:
                phase_ok = True
                artifact_results.append({
                    "artifact": artifact["desc"],
                    "status": "SKIPPED (optional)",
                    "detail": detail
                })
            elif not ok:
                phase_ok = False
                all_ok = False
                artifact_results.append({
                    "artifact": artifact["desc"],
                    "status": "FAIL",
                    "detail": detail
                })
            else:
                artifact_results.append({
                    "artifact": artifact["desc"],
                    "status": "PASS",
                    "detail": detail
                })

        results[phase_key] = {
            "name": phase_def["name"],
            "optional": is_optional,
            "passed": phase_ok,
            "artifacts": artifact_results
        }

    if args.json:
        output = {
            "workspace": workspace,
            "status": "PASS" if all_ok else "FAIL",
            "phases": results
        }
        print(json.dumps(output, indent=2, ensure_ascii=False))
    else:
        for phase_key, result in results.items():
            optional_tag = " (可选)" if result["optional"] else ""
            status_tag = "PASS" if result["passed"] else "FAIL"
            if result["passed"]:
                print(f"[{status_tag}] Phase {phase_key}: {result['name']}{optional_tag}")
            else:
                print(f"[{status_tag}] Phase {phase_key}: {result['name']}{optional_tag}")
            for a in result["artifacts"]:
                icon = "  ✓" if "PASS" in a["status"] else ("  -" if "SKIPPED" in a["status"] else "  ✗")
                print(f"  {icon} {a['artifact']}: {a['status']} ({a['detail']})")
            print()

        if all_ok:
            print("Overall: PASS — all required artifacts present")
            sys.exit(0)
        else:
            print("Overall: FAIL — some artifacts missing or incomplete")
            sys.exit(1)


if __name__ == "__main__":
    main()
