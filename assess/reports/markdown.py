"""Markdown report generation."""

from datetime import datetime

from ..config import CHECKS, RECOMMENDATIONS
from ..engine import readiness_level


def generate_markdown(all_results, title="AI Bug Automation Readiness Report", org=None):
    if not all_results:
        return "# No repositories found to assess.\n"
    all_results.sort(key=lambda r: r["overall_score"], reverse=True)
    avg = sum(r["overall_score"] for r in all_results) / len(all_results)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    org_prefix = f"{org}/" if org else ""

    tier_counts = {"Ready": 0, "Partially Ready": 0, "Needs Work": 0, "Not Ready": 0}
    for r in all_results:
        level, _ = readiness_level(r["overall_score"])
        tier_counts[level] += 1

    # Phase averages
    cat_scores = {}
    for r in all_results:
        for c in r["checks"].values():
            cat_scores.setdefault(c["category"], []).append(c["score"])
    cat_avgs = {cat: sum(s)/len(s) for cat, s in cat_scores.items()}

    cat_weights = {}
    for c in CHECKS.values():
        cat_weights[c["category"]] = cat_weights.get(c["category"], 0) + c["weight"]

    # Check averages
    check_avgs = {}
    for r in all_results:
        for cid, c in r["checks"].items():
            check_avgs.setdefault(cid, {"name": c["name"], "scores": [], "weight": c["weight"]})
            check_avgs[cid]["scores"].append(c["score"])
    worst_checks = sorted(
        [(cid, info["name"], sum(info["scores"])/len(info["scores"]), info["weight"])
         for cid, info in check_avgs.items()],
        key=lambda x: x[2]
    )

    # Quick wins
    quick_wins = []
    for cid, name, avg_score, weight in worst_checks:
        if avg_score < 50:
            repos_below = sum(1 for s in check_avgs[cid]["scores"] if s < 40)
            rec = RECOMMENDATIONS.get(cid, "")
            quick_wins.append((name, repos_below, rec, weight))
    quick_wins.sort(key=lambda x: x[3], reverse=True)

    # Shortlists
    ready_repos = [r for r in all_results if round(r["overall_score"]) >= 80]
    partially_ready = [r for r in all_results if 60 <= round(r["overall_score"]) < 80]
    needs_work = [r for r in all_results if 40 <= round(r["overall_score"]) < 60]
    not_ready = [r for r in all_results if round(r["overall_score"]) < 40]

    ready_count = len(ready_repos) + len(partially_ready)
    biggest_gap = worst_checks[0] if worst_checks else ("", "", 0, 0)

    lines = []
    lines.append(f"# {title}\n")
    lines.append(f"*{len(all_results)} repositories assessed -- {now}*\n")

    # Executive summary
    lines.append(f"> {ready_count} of {len(all_results)} repositories are partially ready or above for AI-assisted bug fixing. "
                 f"The ecosystem averages {avg:.0f}/100. "
                 f"The biggest gap is \"{biggest_gap[1]}\" (avg {biggest_gap[2]:.0f}/100).\n")

    # How Scoring Works
    lines.append("## How Scoring Works\n")
    lines.append(f"**Overall score** = weighted average of {len(CHECKS)} checks, each scored 0-100.\n")
    lines.append(f"**Phases**: Understand ({cat_weights.get('Understand',0)}%), Navigate ({cat_weights.get('Navigate',0)}%), "
                 f"Verify ({cat_weights.get('Verify',0)}%), Submit ({cat_weights.get('Submit',0)}%).\n")
    lines.append("**Verify phase gate:** If the average Verify score is below 15, the overall score is multiplied by 0.4. "
                 "If below 30, multiplied by 0.7.\n")
    lines.append("| Level | Score | Meaning |")
    lines.append("|---|---|---|")
    lines.append("| Ready | 80+ | Strong test infrastructure, good context, CI validates fixes |")
    lines.append("| Partially Ready | 60-79 | Workable but has gaps that may cause AI agent failures |")
    lines.append("| Needs Work | 40-59 | Missing key capabilities; fix gaps before AI bug bash |")
    lines.append("| Not Ready | <40 | Fundamental gaps in test infrastructure or code structure |\n")

    # Summary cards
    lines.append("## Summary\n")
    lines.append(f"| Metric | Value |")
    lines.append(f"|---|---|")
    lines.append(f"| Average Score | {avg:.0f}/100 |")
    lines.append(f"| Ready (80+) | {tier_counts['Ready']} |")
    lines.append(f"| Partially Ready (60-79) | {tier_counts['Partially Ready']} |")
    lines.append(f"| Needs Work (40-59) | {tier_counts['Needs Work']} |")
    lines.append(f"| Not Ready (<40) | {tier_counts['Not Ready']} |\n")

    # Phase averages
    lines.append("## Phase Scores (Ecosystem Average)\n")
    lines.append("| Phase | Weight | Average |")
    lines.append("|---|---|---|")
    for phase in ["Understand", "Navigate", "Verify", "Submit"]:
        pavg = cat_avgs.get(phase, 0)
        lines.append(f"| {phase} | {cat_weights.get(phase, 0)}% | {pavg:.0f}/100 |")
    lines.append("")

    # Bug bash shortlist
    lines.append("## Bug Bash Shortlist\n")

    lines.append(f"### Ready (80+) -- {len(ready_repos)} repos\n")
    if ready_repos:
        for r in ready_repos:
            link = f"[{r['repo']}](https://github.com/{org_prefix}{r['repo']})" if org else r["repo"]
            lines.append(f"- {link} ({round(r['overall_score'])})")
    else:
        lines.append("- None yet")
    lines.append("")

    lines.append(f"### Partially Ready (60-79) -- {len(partially_ready)} repos\n")
    if partially_ready:
        for r in partially_ready:
            link = f"[{r['repo']}](https://github.com/{org_prefix}{r['repo']})" if org else r["repo"]
            checks_sorted = sorted(r["checks"].items(), key=lambda x: (100 - x[1]["score"]) * x[1]["weight"], reverse=True)
            top_gap = checks_sorted[0][1]["name"] if checks_sorted else ""
            lines.append(f"- {link} ({round(r['overall_score'])}) -- top gap: {top_gap}")
    else:
        lines.append("- None")
    lines.append("")

    lines.append(f"### Needs Work (40-59) -- {len(needs_work)} repos\n")
    if needs_work:
        for r in needs_work:
            link = f"[{r['repo']}](https://github.com/{org_prefix}{r['repo']})" if org else r["repo"]
            checks_sorted = sorted(r["checks"].items(), key=lambda x: (100 - x[1]["score"]) * x[1]["weight"], reverse=True)
            top_gap = checks_sorted[0][1]["name"] if checks_sorted else ""
            lines.append(f"- {link} ({round(r['overall_score'])}) -- top gap: {top_gap}")
    else:
        lines.append("- None")
    lines.append("")

    lines.append(f"### Not Ready (<40) -- {len(not_ready)} repos\n")
    if not_ready:
        for r in not_ready:
            link = f"[{r['repo']}](https://github.com/{org_prefix}{r['repo']})" if org else r["repo"]
            lines.append(f"- {link} ({round(r['overall_score'])})")
    else:
        lines.append("- None")
    lines.append("")

    # Repository scores table
    lines.append("## Repository Scores\n")
    lines.append("| Repository | Score | Level | Languages |")
    lines.append("|---|---|---|---|")
    for r in all_results:
        level, _ = readiness_level(r["overall_score"])
        langs = ", ".join(r["languages"][:3])
        gate = " (verify gate)" if r.get("verify_gate") else ""
        repo_label = f"[{r['repo']}](https://github.com/{org_prefix}{r['repo']})" if org else r["repo"]
        lines.append(f"| {repo_label}{gate} | {round(r['overall_score'])}/100 | {level} | {langs} |")
    lines.append("")

    # Quick wins
    if quick_wins:
        lines.append("## Quick Wins (Highest Impact Actions)\n")
        lines.append("| Action | Repos Below 40 | Weight | How to Fix |")
        lines.append("|---|---|---|---|")
        for name, repos_below, rec, weight in quick_wins[:7]:
            lines.append(f"| {name} | {repos_below} repos | {weight}% | {rec} |")
        lines.append("")

    # All checks ranked
    lines.append("## All Checks Ranked by Average Score\n")
    lines.append("| Check | Avg Score | Weight |")
    lines.append("|---|---|---|")
    for cid, name, avg_score, weight in worst_checks:
        lines.append(f"| {name} | {avg_score:.0f}/100 | {weight}% |")
    lines.append("")

    # Per-repo details
    lines.append("## Per-Repository Details\n")
    check_ids = list(CHECKS.keys())
    for r in all_results:
        level, _ = readiness_level(r["overall_score"])
        lines.append(f"### {r['repo']} -- {round(r['overall_score'])}/100 ({level})\n")
        lines.append("| Check | Phase | Weight | Score | Evidence |")
        lines.append("|---|---|---|---|---|")
        for cid in check_ids:
            c = r["checks"][cid]
            ev_text = "; ".join(c["evidence"])
            if c.get("recommendation"):
                ev_text += f" *Rec: {c['recommendation']}*"
            lines.append(f"| {c['name']} | {c['category']} | {c['weight']}% | {c['score']:.0f} | {ev_text} |")
        lines.append("")

    lines.append(f"---\n*AI Bug Automation Readiness Report -- Generated {now}*\n")
    return "\n".join(lines)
