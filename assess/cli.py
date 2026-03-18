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

__version__ = "1.0.0"


def main():
    parser = argparse.ArgumentParser(
        description="AI Bug Automation Readiness Assessment",
        epilog="Examples:\n"
               "  python assess.py /path/to/repo\n"
               "  python assess.py /path/to/repo --format json\n"
               "  python assess.py --batch /path/to/repos --format html --org opendatahub-io\n"
               "\nExit codes: 0 = success, 1 = --fail-under triggered, 2 = error\n",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    source = parser.add_mutually_exclusive_group()
    source.add_argument("repo", nargs="?", help="Path to repository")
    source.add_argument("--batch", help="Path to directory containing multiple repos")
    parser.add_argument("--format", choices=["text", "json", "html", "markdown", "csv", "docx"], default="text")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--org", help="GitHub org for report links")
    parser.add_argument("--title", default="AI Bug Automation Readiness Report")
    parser.add_argument("--fail-under", type=int, metavar="N",
                        help="Exit with code 1 if any repo scores below N (0-100)")
    parser.add_argument("--exclude", nargs="*", default=[], metavar="REPO",
                        help="Repo names to skip in batch mode")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("--quiet", "-q", action="store_true",
                        help="Suppress progress output")
    parser.add_argument("--list-checks", action="store_true",
                        help="List all checks and their weights, then exit")
    args = parser.parse_args()

    # List checks mode
    if args.list_checks:
        from .config import CHECKS
        print(f"{'Check':<40s} {'Weight':>6s}  {'Category'}")
        print("-" * 65)
        for cid, info in CHECKS.items():
            print(f"{info['name']:<40s} {info['weight']:>5d}%  {info['category']}")
        return

    # Require repo or --batch unless --list-checks
    if not args.list_checks and not args.repo and not args.batch:
        parser.error("one of the arguments repo --batch is required")

    # Validate --fail-under range
    if args.fail_under is not None and not (0 <= args.fail_under <= 100):
        parser.error(f"--fail-under must be between 0 and 100, got {args.fail_under}")

    # Validate --output parent directory
    if args.output:
        out_dir = os.path.dirname(args.output) or "."
        if not os.path.isdir(out_dir):
            parser.error(f"Output directory does not exist: {out_dir}")

    # Check docx dependency early
    if args.format == "docx":
        try:
            from .reports.docx_report import generate_docx  # noqa: F401
        except ImportError:
            print("Error: DOCX format requires python-docx. Install with: pip install python-docx",
                  file=sys.stderr)
            sys.exit(2)

    exclude_set = set(args.exclude)

    if args.batch:
        repos_dir = args.batch
        if not os.path.isdir(repos_dir):
            parser.error(f"Batch directory does not exist: {repos_dir}")
        repos = sorted([
            os.path.join(repos_dir, d) for d in os.listdir(repos_dir)
            if os.path.isdir(os.path.join(repos_dir, d, ".git"))
            and d not in exclude_set
        ])
    else:
        if not os.path.isdir(args.repo):
            if os.path.exists(args.repo):
                parser.error(f"Not a directory: {args.repo}")
            parser.error(f"Repository path does not exist: {args.repo}")
        if not os.path.isdir(os.path.join(args.repo, ".git")):
            if not args.quiet:
                print(f"  Warning: {args.repo} is not a git repository (no .git directory)", file=sys.stderr)
        repos = [args.repo]

    all_results = []
    total = len(repos)
    for i, repo_path in enumerate(repos, 1):
        repo_name = Path(repo_path).name
        if not args.quiet:
            prefix = f"  [{i}/{total}] " if total > 1 else "  "
            print(f"{prefix}Assessing {repo_name}...", end="", flush=True, file=sys.stderr)
        result = assess_repo(repo_path)
        all_results.append(result)
        if not args.quiet:
            if result["overall_score"] is not None:
                level, _ = readiness_level(result["overall_score"])
                print(f" {round(result['overall_score'])}/100 ({level})", file=sys.stderr)
            else:
                print(f" N/A (non-code repo)", file=sys.stderr)

    if not all_results:
        print("No repositories found to assess.", file=sys.stderr)
        sys.exit(2)

    if args.format == "json":
        output = json.dumps(all_results if len(all_results) > 1 else all_results[0], indent=2)
    elif args.format == "html":
        output = generate_html(all_results, title=args.title, org=args.org)
    elif args.format == "markdown":
        output = generate_markdown(all_results, title=args.title, org=args.org)
    elif args.format == "csv":
        output = generate_csv(all_results)
    elif args.format == "docx":
        from .reports.docx_report import generate_docx
        docx_doc = generate_docx(all_results, title=args.title, org=args.org)
        out_path = args.output or "report.docx"
        docx_doc.save(out_path)
        if not args.quiet:
            print(f"\nDOCX report written to: {out_path}", file=sys.stderr)
        output = None
    else:
        # Text summary
        code_results = [r for r in all_results if r["overall_score"] is not None]
        noncode_results = [r for r in all_results if r["overall_score"] is None]
        lines = [f"\nAI Bug Automation Readiness Assessment", f"{'=' * 50}"]
        for r in sorted(code_results, key=lambda x: x["overall_score"], reverse=True):
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
        if noncode_results:
            lines.append(f"\n  Non-code repos (excluded from scoring):")
            for r in sorted(noncode_results, key=lambda x: x["repo"]):
                lines.append(f"    {r['repo']}")
        if len(code_results) > 1:
            avg = sum(r["overall_score"] for r in code_results) / len(code_results)
            lines.append(f"\n  {'Average':45s} {round(avg):3d}/100")
            lines.append(f"  {len(code_results)} code repos assessed, {len(noncode_results)} non-code repos excluded")
        output = "\n".join(lines)

    if output is not None:
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(output)
            if not args.quiet:
                print(f"\nReport written to: {args.output}", file=sys.stderr)
        else:
            print(output)

    # Exit codes for CI gating (only check code repos)
    if args.fail_under is not None:
        scored = [r["overall_score"] for r in all_results if r["overall_score"] is not None]
        min_score = min(scored) if scored else 0
        if min_score < args.fail_under:
            sys.exit(1)
