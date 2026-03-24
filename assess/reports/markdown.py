"""Markdown report generation."""

from datetime import datetime

from ..config import CHECKS
from ..engine import readiness_level
from . import prepare_report_data


def _escape_pipe(text):
    """Escape pipe characters for markdown table cells."""
    return text.replace("|", "\\|")


def generate_markdown(all_results, title="AI Bug Automation Readiness Report", org=None):
    if not all_results:
        return "# No repositories found to assess.\n"

    d = prepare_report_data(all_results, org=org)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    org_prefix = d["org_prefix"]

    lines = []
    lines.append(f"# {title}\n")
    lines.append(f"*{len(d['sorted_results'])} repositories assessed -- {now}*\n")

    # Executive summary
    lines.append(f"> {d['ready_count']} of {len(d['sorted_results'])} repositories are partially ready or above for AI-assisted bug fixing. "
                 f"The ecosystem averages {d['avg']:.0f}/100. "
                 f"The biggest gap is \"{d['biggest_gap'][1]}\" (avg {d['biggest_gap'][2]:.0f}/100).\n")

    # How Scoring Works
    lines.append("## How Scoring Works\n")
    lines.append(f"**Overall score** = weighted average of {len(CHECKS)} checks, each scored 0-100.\n")
    lines.append(f"**Phases**: Understand ({d['cat_weights'].get('Understand',0)}%), Navigate ({d['cat_weights'].get('Navigate',0)}%), "
                 f"Verify ({d['cat_weights'].get('Verify',0)}%), Submit ({d['cat_weights'].get('Submit',0)}%).\n")
    lines.append("**Verify phase gate:** If the average Verify score is below 50, the overall score receives a smooth "
                 "penalty multiplier that scales linearly from x0.4 (verify avg = 0) to x1.0 (verify avg = 50).\n")
    lines.append("| Level | Score | Meaning |")
    lines.append("|---|---|---|")
    lines.append("| Ready | 80+ | Strong test infrastructure, good context, CI validates fixes |")
    lines.append("| Partially Ready | 60-79 | Workable but has gaps that may cause AI agent failures |")
    lines.append("| Needs Work | 40-59 | Missing key capabilities; fix gaps before AI bug bash |")
    lines.append("| Not Ready | <40 | Fundamental gaps in test infrastructure or code structure |\n")

    # Summary cards
    lines.append("## Summary\n")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    lines.append(f"| Average Score | {d['avg']:.0f}/100 |")
    lines.append(f"| Ready (80+) | {d['tier_counts']['Ready']} |")
    lines.append(f"| Partially Ready (60-79) | {d['tier_counts']['Partially Ready']} |")
    lines.append(f"| Needs Work (40-59) | {d['tier_counts']['Needs Work']} |")
    lines.append(f"| Not Ready (<40) | {d['tier_counts']['Not Ready']} |\n")

    # Phase averages
    lines.append("## Phase Scores (Ecosystem Average)\n")
    lines.append("| Phase | Weight | Average |")
    lines.append("|---|---|---|")
    for phase in ["Understand", "Navigate", "Verify", "Submit"]:
        pavg = d["cat_avgs"].get(phase, 0)
        lines.append(f"| {phase} | {d['cat_weights'].get(phase, 0)}% | {pavg:.0f}/100 |")
    lines.append("")

    # Bug bash shortlist
    lines.append("## Bug Bash Shortlist\n")

    lines.append(f"### Ready (80+) -- {len(d['ready_repos'])} repos\n")
    if d["ready_repos"]:
        for r in d["ready_repos"]:
            link = f"[{r['repo']}](https://github.com/{org_prefix}{r['repo']})" if org else r["repo"]
            lines.append(f"- {link} ({round(r['overall_score'])})")
    else:
        lines.append("- None yet")
    lines.append("")

    lines.append(f"### Partially Ready (60-79) -- {len(d['partially_ready'])} repos\n")
    if d["partially_ready"]:
        for r in d["partially_ready"]:
            link = f"[{r['repo']}](https://github.com/{org_prefix}{r['repo']})" if org else r["repo"]
            checks_sorted = sorted([(k, v) for k, v in r["checks"].items() if not v.get("excluded")], key=lambda x: (100 - x[1]["score"]) * x[1]["weight"], reverse=True)
            top_gap = checks_sorted[0][1]["name"] if checks_sorted else ""
            lines.append(f"- {link} ({round(r['overall_score'])}) -- top gap: {top_gap}")
    else:
        lines.append("- None")
    lines.append("")

    lines.append(f"### Needs Work (40-59) -- {len(d['needs_work'])} repos\n")
    if d["needs_work"]:
        for r in d["needs_work"]:
            link = f"[{r['repo']}](https://github.com/{org_prefix}{r['repo']})" if org else r["repo"]
            checks_sorted = sorted([(k, v) for k, v in r["checks"].items() if not v.get("excluded")], key=lambda x: (100 - x[1]["score"]) * x[1]["weight"], reverse=True)
            top_gap = checks_sorted[0][1]["name"] if checks_sorted else ""
            lines.append(f"- {link} ({round(r['overall_score'])}) -- top gap: {top_gap}")
    else:
        lines.append("- None")
    lines.append("")

    lines.append(f"### Not Ready (<40) -- {len(d['not_ready'])} repos\n")
    if d["not_ready"]:
        for r in d["not_ready"]:
            link = f"[{r['repo']}](https://github.com/{org_prefix}{r['repo']})" if org else r["repo"]
            lines.append(f"- {link} ({round(r['overall_score'])})")
    else:
        lines.append("- None")
    lines.append("")

    # Repository scores table
    lines.append("## Repository Scores\n")
    lines.append("| Repository | Score | Level | Languages |")
    lines.append("|---|---|---|---|")
    for r in d["sorted_results"]:
        level, _ = readiness_level(r["overall_score"])
        langs = ", ".join(r["languages"][:3])
        gate = " (verify gate)" if r.get("verify_gate") else ""
        repo_label = f"[{r['repo']}](https://github.com/{org_prefix}{r['repo']})" if org else r["repo"]
        lines.append(f"| {repo_label}{gate} | {round(r['overall_score'])}/100 | {level} | {langs} |")
    lines.append("")

    # Quick wins
    if d["quick_wins"]:
        lines.append("## Quick Wins (Highest Impact Actions)\n")
        lines.append("| Action | Repos Below 40 | Weight | How to Fix |")
        lines.append("|---|---|---|---|")
        for name, repos_below, lift, rec, weight in d["quick_wins"][:7]:
            lines.append(f"| {_escape_pipe(name)} | {repos_below} repos | {weight}% | {_escape_pipe(rec)} |")
        lines.append("")

    # All checks ranked
    lines.append("## All Checks Ranked by Average Score\n")
    lines.append("| Check | Avg Score | Weight |")
    lines.append("|---|---|---|")
    for cid, name, avg_score, weight in d["worst_checks"]:
        lines.append(f"| {_escape_pipe(name)} | {avg_score:.0f}/100 | {weight}% |")
    lines.append("")

    # Per-repo details
    lines.append("## Per-Repository Details\n")
    check_ids = list(CHECKS.keys())
    for r in d["sorted_results"]:
        level, _ = readiness_level(r["overall_score"])
        lines.append(f"### {r['repo']} -- {round(r['overall_score'])}/100 ({level})\n")
        lines.append("| Check | Phase | Weight | Score | Evidence |")
        lines.append("|---|---|---|---|---|")
        for cid in check_ids:
            c = r["checks"][cid]
            if c.get("excluded"):
                lines.append(f"| {_escape_pipe(c['name'])} | {c['category']} | {c['weight']}% | N/A | *Excluded by profile* |")
            else:
                ev_text = "; ".join(c["evidence"])
                if c.get("recommendation"):
                    ev_text += f" *Rec: {c['recommendation']}*"
                lines.append(f"| {_escape_pipe(c['name'])} | {c['category']} | {c['weight']}% | {c['score']:.0f} | {_escape_pipe(ev_text)} |")
        lines.append("")

    lines.append(f"---\n*AI Bug Automation Readiness Report -- Generated {now}*\n")
    return "\n".join(lines)
