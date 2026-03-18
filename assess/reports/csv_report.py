"""CSV report generation."""

import csv
import io

from ..config import CHECKS
from ..engine import readiness_level


def generate_csv(all_results):
    code_results = [r for r in all_results if r.get("overall_score") is not None]
    noncode_results = [r for r in all_results if r.get("overall_score") is None]
    results = sorted(code_results, key=lambda r: r["overall_score"], reverse=True)
    buf = io.StringIO()
    check_ids = list(CHECKS.keys())
    headers = ["repo", "overall_score", "level", "verify_avg", "verify_gate", "languages"] + [CHECKS[cid]["name"] for cid in check_ids]
    writer = csv.writer(buf)
    writer.writerow(headers)
    for r in results:
        level, _ = readiness_level(r["overall_score"])
        row = [
            r["repo"],
            round(r["overall_score"]),
            level,
            r.get("verify_avg", ""),
            r.get("verify_gate") or "",
            ";".join(r["languages"]),
        ]
        for cid in check_ids:
            row.append(round(r["checks"][cid]["score"]))
        writer.writerow(row)
    for r in sorted(noncode_results, key=lambda x: x["repo"]):
        row = [r["repo"], "N/A", "Not Applicable", "", "", ";".join(r["languages"])]
        for cid in check_ids:
            row.append("")
        writer.writerow(row)
    return buf.getvalue()
