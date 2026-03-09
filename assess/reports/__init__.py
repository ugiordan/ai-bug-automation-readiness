"""Report generators — shared data preparation."""

from ..config import CHECKS, RECOMMENDATIONS
from ..engine import readiness_level


def prepare_report_data(all_results, org=None):
    """Compute shared metrics used by all report generators.

    Returns a dict with: sorted_results, avg, tier_counts, cat_avgs, cat_weights,
    worst_checks, quick_wins, ready_repos, partially_ready, needs_work, not_ready,
    ready_count, biggest_gap, org_prefix.
    """
    sorted_results = sorted(all_results, key=lambda r: r["overall_score"], reverse=True)
    avg = sum(r["overall_score"] for r in sorted_results) / len(sorted_results) if sorted_results else 0

    org_prefix = f"{org}/" if org else ""

    tier_counts = {"Ready": 0, "Partially Ready": 0, "Needs Work": 0, "Not Ready": 0}
    for r in sorted_results:
        level, _ = readiness_level(r["overall_score"])
        tier_counts[level] += 1

    # Phase averages
    cat_scores = {}
    for r in sorted_results:
        for c in r["checks"].values():
            cat_scores.setdefault(c["category"], []).append(c["score"])
    cat_avgs = {cat: sum(s) / len(s) for cat, s in cat_scores.items()}

    cat_weights = {}
    for c in CHECKS.values():
        cat_weights[c["category"]] = cat_weights.get(c["category"], 0) + c["weight"]

    # Check averages
    check_avgs = {}
    for r in sorted_results:
        for cid, c in r["checks"].items():
            check_avgs.setdefault(cid, {"name": c["name"], "scores": [], "weight": c["weight"]})
            check_avgs[cid]["scores"].append(c["score"])
    worst_checks = sorted(
        [(cid, info["name"], sum(info["scores"]) / len(info["scores"]), info["weight"])
         for cid, info in check_avgs.items()],
        key=lambda x: x[2],
    )

    # Quick wins — sorted by estimated lift (gap * weight) for consistency
    quick_wins = []
    for cid, name, avg_score, weight in worst_checks:
        if avg_score < 50:
            repos_below = sum(1 for s in check_avgs[cid]["scores"] if s < 40)
            est_lift = (60 - avg_score) * weight / 100
            rec = RECOMMENDATIONS.get(cid, "")
            quick_wins.append((name, repos_below, est_lift, rec, weight))
    quick_wins.sort(key=lambda x: x[2], reverse=True)

    # Tier lists
    ready_repos = [r for r in sorted_results if round(r["overall_score"]) >= 80]
    partially_ready = [r for r in sorted_results if 60 <= round(r["overall_score"]) < 80]
    needs_work = [r for r in sorted_results if 40 <= round(r["overall_score"]) < 60]
    not_ready = [r for r in sorted_results if round(r["overall_score"]) < 40]

    ready_count = len(ready_repos) + len(partially_ready)
    biggest_gap = worst_checks[0] if worst_checks else ("", "", 0, 0)

    return {
        "sorted_results": sorted_results,
        "avg": avg,
        "tier_counts": tier_counts,
        "cat_avgs": cat_avgs,
        "cat_weights": cat_weights,
        "check_avgs": check_avgs,
        "worst_checks": worst_checks,
        "quick_wins": quick_wins,
        "ready_repos": ready_repos,
        "partially_ready": partially_ready,
        "needs_work": needs_work,
        "not_ready": not_ready,
        "ready_count": ready_count,
        "biggest_gap": biggest_gap,
        "org_prefix": org_prefix,
    }
