"""CLI entry point for AI Bug Automation Readiness Assessment."""

import argparse
import json
import os
import sys
from pathlib import Path

from .engine import assess_repo, readiness_level
from .reports.html import generate_html
from .reports.markdown import generate_markdown
from .reports.csv_report import generate_csv


def main():
    parser = argparse.ArgumentParser(
        description="AI Bug Automation Readiness Assessment",
        epilog="Examples:\n"
               "  python assess.py /path/to/repo\n"
               "  python assess.py /path/to/repo --format json\n"
               "  python assess.py --batch /path/to/repos --format html --org opendatahub-io\n",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("repo", nargs="?", help="Path to repository")
    source.add_argument("--batch", help="Path to directory containing multiple repos")
    parser.add_argument("--format", choices=["text", "json", "html", "markdown", "csv", "docx"], default="text")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--org", help="GitHub org for report links")
    parser.add_argument("--agentready-results", help="Path to AgentReady results for comparison")
    parser.add_argument("--title", default="AI Bug Automation Readiness Report")
    parser.add_argument("--fail-under", type=int, metavar="N",
                        help="Exit with code 1 if any repo scores below N")
    args = parser.parse_args()

    if args.batch:
        repos_dir = args.batch
        if not os.path.isdir(repos_dir):
            parser.error(f"Batch directory does not exist: {repos_dir}")
        repos = sorted([
            os.path.join(repos_dir, d) for d in os.listdir(repos_dir)
            if os.path.isdir(os.path.join(repos_dir, d, ".git"))
        ])
    else:
        if not os.path.isdir(args.repo):
            parser.error(f"Repository path does not exist: {args.repo}")
        repos = [args.repo]

    all_results = []
    for repo_path in repos:
        repo_name = Path(repo_path).name
        print(f"  Assessing {repo_name}...", end="", flush=True, file=sys.stderr)
        result = assess_repo(repo_path, args.agentready_results)
        all_results.append(result)
        level, _ = readiness_level(result["overall_score"])
        print(f" {round(result['overall_score'])}/100 ({level})", file=sys.stderr)

    if not all_results:
        print("No repositories found to assess.", file=sys.stderr)
        sys.exit(1)

    if args.format == "json":
        output = json.dumps(all_results if len(all_results) > 1 else all_results[0], indent=2)
    elif args.format == "html":
        output = generate_html(all_results, title=args.title, org=args.org)
    elif args.format == "markdown":
        output = generate_markdown(all_results, title=args.title, org=args.org)
    elif args.format == "csv":
        output = generate_csv(all_results)
    elif args.format == "docx":
        try:
            from .reports.docx_report import generate_docx
        except ImportError:
            print("Error: DOCX format requires python-docx. Install with: pip install python-docx",
                  file=sys.stderr)
            sys.exit(1)
        docx_doc = generate_docx(all_results, title=args.title, org=args.org)
        out_path = args.output or "report.docx"
        docx_doc.save(out_path)
        print(f"\nDOCX report written to: {out_path}", file=sys.stderr)
        output = None
    else:
        # Text summary
        lines = [f"\nAI Bug Automation Readiness Assessment", f"{'=' * 50}"]
        for r in sorted(all_results, key=lambda x: x["overall_score"], reverse=True):
            level, _ = readiness_level(r["overall_score"])
            lines.append(f"  {r['repo']:45s} {round(r['overall_score']):3d}/100  {level}")
            if r.get("verify_gate"):
                lines.append(f"    {'':45s} (verify gate: {r['verify_gate']})")
            # Show per-check details for single-repo assessments
            if len(all_results) == 1:
                lines.append("")
                checks_by_cat = {}
                for cid, c in r["checks"].items():
                    checks_by_cat.setdefault(c["category"], []).append(c)
                for phase in ["Understand", "Navigate", "Verify", "Submit"]:
                    lines.append(f"  {phase}")
                    for c in checks_by_cat.get(phase, []):
                        icon = "+" if c["score"] >= 60 else "-"
                        lines.append(f"    [{icon}] {c['name']:40s} {c['score']:3.0f}/100 (weight: {c['weight']}%)")
                        if c.get("recommendation"):
                            lines.append(f"        -> {c['recommendation']}")
                    lines.append("")
        if len(all_results) > 1:
            avg = sum(r["overall_score"] for r in all_results) / len(all_results)
            lines.append(f"\n  {'Average':45s} {round(avg):3d}/100")
        output = "\n".join(lines)

    if output is not None:
        if args.output:
            with open(args.output, "w") as f:
                f.write(output)
            print(f"\nReport written to: {args.output}", file=sys.stderr)
        else:
            print(output)

    # Exit codes for CI gating
    if args.fail_under is not None:
        min_score = min(r["overall_score"] for r in all_results)
        if min_score < args.fail_under:
            sys.exit(1)
