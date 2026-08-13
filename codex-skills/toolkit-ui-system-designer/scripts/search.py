#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Smart UI Designer - CLI Entry Point
Usage:
    python search.py "<query>" --domain <domain>
    python search.py "<query>" --design-system
    python search.py "<query>" --stack <stack>
    python search.py extract --url <url> --name <template-name>
"""

import argparse
import sys
import io
import json
from core import CSV_CONFIG, AVAILABLE_STACKS, MAX_RESULTS, search, search_stack, list_available_data
from generator import generate_design_system
from extractor import main as extractor_main

# Force UTF-8 for stdout/stderr on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if sys.stderr.encoding and sys.stderr.encoding.lower() != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def format_output(result):
    """Format results for AI consumption"""
    if "error" in result:
        return f"错误: {result['error']}"

    output = []

    if result.get("stack"):
        output.append(f"## Smart UI Designer - 技术栈指南")
        output.append(f"**技术栈:** {result['stack']} | **查询:** {result['query']}")
    else:
        output.append(f"## Smart UI Designer - 搜索结果")
        output.append(f"**领域:** {result['domain']} | **查询:** {result['query']}")
    output.append(f"**数据源:** {result['file']} | **找到:** {result['count']} 条结果\n")

    for i, row in enumerate(result['results'], 1):
        output.append(f"### 结果 {i}")
        for key, value in row.items():
            value_str = str(value)
            if len(value_str) > 300:
                value_str = value_str[:300] + "..."
            output.append(f"- **{key}:** {value_str}")
        output.append("")

    return "\n".join(output)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "extract":
        sys.exit(extractor_main(sys.argv[2:]))

    parser = argparse.ArgumentParser(
        description="Smart UI Designer - 智能 UI 设计助手",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python search.py "后台管理系统" --design-system
  python search.py "BI大屏" --design-system -p "智慧城市大屏"
  python search.py "表格组件" --domain component
  python search.py "表单验证" --stack vue3
  python search.py extract --url https://example.com --name "参考风格" --tags "SaaS,极简"
  python search.py extract --list
  python search.py --list
        """
    )

    parser.add_argument("query", nargs="?", help="搜索查询")
    parser.add_argument("--domain", "-d", choices=list(CSV_CONFIG.keys()), help="搜索领域")
    parser.add_argument("--stack", "-s", choices=AVAILABLE_STACKS, help="技术栈搜索")
    parser.add_argument("--max-results", "-n", type=int, default=MAX_RESULTS, help="最大结果数")
    parser.add_argument("--json", action="store_true", help="JSON 输出")
    parser.add_argument("--list", "-l", action="store_true", help="列出可用数据")

    # Design system generation
    parser.add_argument("--design-system", "-ds", action="store_true", help="生成设计系统")
    parser.add_argument("--project-name", "-p", type=str, default=None, help="项目名称")
    parser.add_argument("--format", "-f", choices=["ascii", "markdown"], default="ascii", help="输出格式")
    parser.add_argument("--persist", action="store_true", help="保存到 design-system/ 目录")

    args = parser.parse_args()

    # List available data
    if args.list:
        print("## Smart UI Designer - 可用数据\n")
        available = list_available_data()
        for domain, info in available.items():
            status = info.get('status', '✅')
            count = info['count']
            extracted_count = info.get('extracted_count', 0)
            suffix = f"，含提取模板 {extracted_count} 条" if extracted_count else ""
            print(f"- **{domain}**: {info['file']} ({count} 条记录{suffix}) {status}")
        print(f"\n**可用技术栈:** {', '.join(AVAILABLE_STACKS)}")
        sys.exit(0)

    # Require query for other operations
    if not args.query:
        parser.print_help()
        sys.exit(1)

    # Design system generation
    if args.design_system:
        result = generate_design_system(
            args.query,
            args.project_name,
            stack=args.stack or "vue3",
            output_format=args.format,
            persist=args.persist
        )
        print(result)
        if args.persist:
            print("\n✅ 设计系统已保存到 design-system/MASTER.md")
        sys.exit(0)

    # Stack search
    if args.stack:
        result = search_stack(args.query, args.stack, args.max_results)
        if args.json:
            import json
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(format_output(result))
        sys.exit(0)

    # Domain search
    result = search(args.query, args.domain, args.max_results)
    if args.json:
        import json
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(format_output(result))
