"""CLI entry point for AI Bug Automation Readiness Assessment."""

import argparse
import json
import os
import sys
from pathlib import Path

from .engine import assess_repo, readiness_level
from .profiles import resolve_profile, load_central_profiles
from .reports.html import generate_html
from .reports.markdown import generate_markdown
from .reports.csv_report import generate_csv

__version__ = "1.0.0"


def discover_repos(batch_dir, exclude_set):
    """Discover repos in batch dir. Supports flat and nested (org/repo) layouts.

    Returns list of (org, repo_name, repo_path) tuples.
    org is None for flat layout entries.
    """
    results = []
    for entry in sorted(os.listdir(batch_dir)):
        entry_path = os.path.join(batch_dir, entry)
        if not os.path.isdir(entry_path):
            continue

        # Flat layout: entry is a repo (has .git dir or .git marker file)
        if os.path.exists(os.path.join(entry_path, ".git")):
            if entry not in exclude_set:
                results.append((None, entry, entry_path))
            continue

        # Nested layout: entry is an org containing repos
        for sub in sorted(os.listdir(entry_path)):
            sub_path = os.path.join(entry_path, sub)
            if os.path.exists(os.path.join(sub_path, ".git")):
                if sub not in exclude_set and f"{entry}/{sub}" not in exclude_set:
                    results.append((entry, sub, sub_path))

    return results


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
    parser.add_argument("--profile", metavar="NAME",
                        help="Named profile (e.g., test-repo). Overrides profiles.json for all repos.")
    parser.add_argument("--exclude-checks", nargs="*", default=[], metavar="CHECK",
                        help="Check IDs to skip (e.g., coverage_config test_ratio)")
    parser.add_argument("--list-profiles", action="store_true",
                        help="List available profiles, then exit")
    args = parser.parse_args()

    # List checks mode
    if args.list_checks:
        from .config import CHECKS
        print(f"{'Check':<40s} {'Weight':>6s}  {'Category'}")
        print("-" * 65)
        for cid, info in CHECKS.items():
            print(f"{info['name']:<40s} {info['weight']:>5d}%  {info['category']}")
        return

    if args.list_profiles:
        data = load_central_profiles()
        for name, pdef in data.get("profiles", {}).items():
            desc = pdef.get("description", "")
            excl = ", ".join(pdef.get("exclude", [])) or "(none)"
            print(f"  {name:20s} {desc}")
            print(f"  {'':20s} excludes: {excl}\n")
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
        repo_tuples = discover_repos(repos_dir, exclude_set)
    else:
        if not os.path.isdir(args.repo):
            if os.path.exists(args.repo):
                parser.error(f"Not a directory: {args.repo}")
            parser.error(f"Repository path does not exist: {args.repo}")
        if not os.path.exists(os.path.join(args.repo, ".git")):
            if not args.quiet:
                print(f"  Warning: {args.repo} is not a git repository (no .git directory)", file=sys.stderr)
        repo_tuples = [(args.org, Path(args.repo).name, args.repo)]

    all_results = []
    total = len(repo_tuples)
    for i, (org, repo_name, repo_path) in enumerate(repo_tuples, 1):
        effective_org = org or args.org
        if not args.quiet:
            prefix = f"  [{i}/{total}] " if total > 1 else "  "
            print(f"{prefix}Assessing {repo_name}...", end="", flush=True, file=sys.stderr)
        profile_info = resolve_profile(
            repo_path,
            cli_profile=args.profile,
            cli_exclude_checks=args.exclude_checks or None,
            org=effective_org,
        )
        result = assess_repo(repo_path,
                             excluded_checks=profile_info.excluded_checks,
                             profile_info=profile_info)
        result["org"] = effective_org
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

    # Determine if multi-org (preserve None keys for single-repo without --org)
    from collections import defaultdict
    results_by_org = defaultdict(list)
    for result in all_results:
        results_by_org[result.get("org")].append(result)

    # Multi-org detection: only count orgs with actual names (not None)
    named_orgs = {k: v for k, v in results_by_org.items() if k is not None}
    use_multi = len(named_orgs) > 1

    if args.format == "json":
        output = json.dumps(all_results if len(all_results) > 1 else all_results[0], indent=2)
    elif args.format == "html":
        if use_multi:
            from .reports.html import generate_html_tabbed
            output = generate_html_tabbed(dict(named_orgs), title=args.title)
        else:
            effective_org = args.org or next((k for k in results_by_org if k is not None), None)
            output = generate_html(all_results, title=args.title, org=effective_org)
    elif args.format == "markdown":
        if use_multi:
            from .reports.markdown import generate_markdown_multi
            output = generate_markdown_multi(dict(named_orgs), title=args.title)
        else:
            effective_org = args.org or next((k for k in results_by_org if k is not None), None)
            output = generate_markdown(all_results, title=args.title, org=effective_org)
    elif args.format == "csv":
        output = generate_csv(all_results)
    elif args.format == "docx":
        from .reports.docx_report import generate_docx
        effective_org = args.org or next((k for k in results_by_org if k is not None), None)
        docx_doc = generate_docx(all_results, title=args.title, org=effective_org)
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
            profile_suffix = ""
            if r.get("profile", {}).get("name", "default") != "default":
                p = r["profile"]
                profile_suffix = f" (profile: {p['name']}, {len(p['excluded_checks'])} excluded)"
            lines.append(f"  {r['repo']:45s} {round(r['overall_score']):3d}/100  {level}{profile_suffix}")
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
                        if c.get("excluded"):
                            lines.append(f"    [N/A] {c['name']:40s}  --     (excluded by profile)")
                        else:
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
