"""CSV report generation."""

import csv
import io

from ..config import CHECKS
from ..engine import readiness_level


def generate_csv(all_results):
    all_results.sort(key=lambda r: r["overall_score"], reverse=True)
    buf = io.StringIO()
    check_ids = list(CHECKS.keys())
    headers = ["repo", "overall_score", "level", "verify_avg", "verify_gate", "languages"] + [CHECKS[cid]["name"] for cid in check_ids]
    writer = csv.writer(buf)
    writer.writerow(headers)
    for r in all_results:
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
    return buf.getvalue()
