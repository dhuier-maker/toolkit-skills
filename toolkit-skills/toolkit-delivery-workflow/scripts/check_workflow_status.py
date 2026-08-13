#!/usr/bin/env python3
"""
Check workflow-status.json structural integrity.

Usage:
    python scripts/check_workflow_status.py
    python scripts/check_workflow_status.py --status-file doc/workflow-status.json
    python scripts/check_workflow_status.py --json
"""

import json
import os
import sys
import argparse
from datetime import datetime

VALID_PHASES = {
    "config-init", "demand-confirm", "architecting", "prototyping",
    "backend-dev", "frontend-dev", "code-review", "testing", "bugfix", "delivered"
}
VALID_MODULE_STATUSES = {"pending", "in-progress", "done"}
VALID_TASK_STATUSES = {"pending", "in_progress", "completed", "failed"}

REQUIRED_TOP_FIELDS = ["currentPhase", "phaseHistory", "config"]


def load_status(path):
    if not os.path.exists(path):
        return None, f"File not found: {path}"
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data, None
    except json.JSONDecodeError as e:
        return None, f"Invalid JSON: {e}"
    except Exception as e:
        return None, f"Read error: {e}"


def check_required_fields(data, errors):
    for field in REQUIRED_TOP_FIELDS:
        if field not in data:
            errors.append(f"[MISSING] Top-level field '{field}' is required")


def check_current_phase(data, errors):
    phase = data.get("currentPhase")
    if phase and phase not in VALID_PHASES:
        errors.append(
            f"[INVALID] currentPhase '{phase}' is not a valid value. "
            f"Expected one of: {', '.join(sorted(VALID_PHASES))}"
        )


def check_phase_history(data, errors):
    history = data.get("phaseHistory", [])
    if not isinstance(history, list):
        errors.append("[TYPE] phaseHistory must be a list")
        return
    last_time = None
    for i, entry in enumerate(history):
        if not isinstance(entry, dict):
            errors.append(f"[TYPE] phaseHistory[{i}] must be an object")
            continue
        ts = entry.get("time", "")
        try:
            current_time = datetime.fromisoformat(ts.replace("Z", "+00:00"))
            if last_time and current_time < last_time:
                errors.append(
                    f"[ORDER] phaseHistory[{i}] time '{ts}' is earlier than "
                    f"previous entry '{history[i-1].get('time')}'"
                )
            last_time = current_time
        except (ValueError, AttributeError):
            errors.append(f"[FORMAT] phaseHistory[{i}] time '{ts}' is not valid ISO 8601")


def check_bug_counts_consistency(data, errors):
    bugs_found = data.get("bugsFound", 0)
    bugs_fixed = data.get("bugsFixed", 0)
    remaining = data.get("bugsRemaining", {})
    if remaining:
        total_remaining = sum(remaining.values())
        expected_found = bugs_fixed + total_remaining
        if bugs_found != expected_found:
            errors.append(
                f"[CONSISTENCY] bugsFound({bugs_found}) != "
                f"bugsFixed({bugs_fixed}) + sum(bugsRemaining)({total_remaining}) = {expected_found}"
            )


def check_review_findings_consistency(data, errors):
    findings = data.get("reviewFindings", {})
    review_blocked = data.get("reviewBlocked", False)
    critical = findings.get("critical", 0)
    if critical > 0 and not review_blocked:
        errors.append(
            f"[CONSISTENCY] reviewFindings.critical={critical} > 0 but reviewBlocked=False"
        )
    if critical == 0 and review_blocked:
        errors.append(
            "[CONSISTENCY] reviewFindings.critical=0 but reviewBlocked=True"
        )


def check_development_progress(data, errors):
    dp = data.get("developmentProgress")
    if dp is None:
        return
    total = dp.get("totalModules", 0)
    completed = dp.get("completedModules", 0)
    if completed > total:
        errors.append(
            f"[CONSISTENCY] developmentProgress.completedModules({completed}) > "
            f"totalModules({total})"
        )
    for layer in ("backend", "frontend"):
        layer_data = dp.get(layer, {})
        modules = layer_data.get("modules", [])
        done_count = sum(1 for m in modules if m.get("status") == "done")
        if completed < done_count:
            errors.append(
                f"[CONSISTENCY] developmentProgress.completedModules({completed}) < "
                f"{layer}.done count({done_count})"
            )
        for m in modules:
            status = m.get("status", "")
            if status and status not in VALID_MODULE_STATUSES:
                errors.append(
                    f"[INVALID] module '{m.get('name', '?')}' has invalid status '{status}'"
                )


def check_remediation_fields(data, errors):
    review_fix = data.get("reviewFix")
    if review_fix:
        npc = review_fix.get("noProgressCount", 0)
        if not isinstance(npc, int) or npc < 0:
            errors.append(f"[TYPE] reviewFix.noProgressCount must be non-negative integer")
        if npc > 3:
            errors.append(f"[WARN] reviewFix.noProgressCount={npc} exceeds max degradation level (3)")

    bugfix_rem = data.get("bugFixRemediation")
    if bugfix_rem:
        npc = bugfix_rem.get("noProgressCount", 0)
        if not isinstance(npc, int) or npc < 0:
            errors.append(f"[TYPE] bugFixRemediation.noProgressCount must be non-negative integer")
        if npc > 3:
            errors.append(f"[WARN] bugFixRemediation.noProgressCount={npc} exceeds max degradation level (3)")


def check_config(data, errors):
    config = data.get("config", {})
    if config:
        dirs = config.get("directories", {})
        if "backend" not in dirs:
            errors.append("[MISSING] config.directories.backend is not defined")
        if "frontend" not in dirs:
            errors.append("[MISSING] config.directories.frontend is not defined")


def check_parallel_tasks(data, errors):
    pt = data.get("parallelTasks", {})
    if pt:
        for task_name in ("backend", "frontend"):
            task = pt.get(task_name, {})
            status = task.get("status", "")
            if status and status not in VALID_TASK_STATUSES:
                errors.append(f"[INVALID] parallelTasks.{task_name}.status '{status}' is not valid")


def main():
    parser = argparse.ArgumentParser(description="Check workflow-status.json integrity")
    parser.add_argument("--status-file", default="doc/workflow-status.json",
                        help="Path to workflow-status.json (default: doc/workflow-status.json)")
    parser.add_argument("--json", action="store_true",
                        help="Output results as JSON")
    args = parser.parse_args()

    status_path = os.path.join(os.getcwd(), args.status_file)
    data, load_error = load_status(status_path)

    if args.json:
        output = {"status": "PASS", "errors": []}

    if load_error:
        if args.json:
            output["status"] = "FAIL"
            output["errors"].append(load_error)
            print(json.dumps(output, indent=2, ensure_ascii=False))
        else:
            print(f"FAIL: {load_error}")
        sys.exit(1)

    errors = []
    check_required_fields(data, errors)
    check_current_phase(data, errors)
    check_phase_history(data, errors)
    check_bug_counts_consistency(data, errors)
    check_review_findings_consistency(data, errors)
    check_development_progress(data, errors)
    check_remediation_fields(data, errors)
    check_config(data, errors)
    check_parallel_tasks(data, errors)

    if args.json:
        output["errors"] = errors
        output["status"] = "PASS" if not errors else "FAIL"
        output["checkedFields"] = [
            "required_fields", "current_phase", "phase_history",
            "bug_counts", "review_findings", "development_progress",
            "remediation", "config", "parallel_tasks"
        ]
        print(json.dumps(output, indent=2, ensure_ascii=False))
    else:
        print(f"Checking: {status_path}")
        print(f"Current phase: {data.get('currentPhase', 'N/A')}")
        print(f"Phase history entries: {len(data.get('phaseHistory', []))}")
        print()
        if errors:
            print(f"FAIL — {len(errors)} issue(s) found:")
            for e in errors:
                print(f"  {e}")
            sys.exit(1)
        else:
            print("PASS — all checks passed")
            sys.exit(0)


if __name__ == "__main__":
    main()
