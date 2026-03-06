"""Assessment engine — orchestrates checks and computes scores."""

import hashlib
import json
import os
import random
from datetime import datetime
from pathlib import Path

from .checks import CHECK_FUNCTIONS
from .config import CHECKS, RECOMMENDATIONS
from .utils import detect_languages


def assess_repo(repo_path, agentready_results_dir=None):
    """Run all checks on a repository."""
    repo_name = Path(repo_path).name
    random.seed(int(hashlib.md5(repo_name.encode()).hexdigest(), 16) % (2**32))
    results = {
        "repo": repo_name,
        "repo_path": str(repo_path),
        "timestamp": datetime.now().isoformat(),
        "checks": {},
        "languages": detect_languages(repo_path),
    }

    total_weighted = 0
    total_weight = 0
    verify_scores = []

    for check_id, check_info in CHECKS.items():
        func = CHECK_FUNCTIONS[check_id]
        score, evidence = func(repo_path)
        weight = check_info["weight"]

        recommendation = None
        if score < 60 and check_id in RECOMMENDATIONS:
            recommendation = RECOMMENDATIONS[check_id]

        results["checks"][check_id] = {
            "name": check_info["name"],
            "category": check_info["category"],
            "weight": weight,
            "score": score,
            "evidence": evidence,
            "recommendation": recommendation,
        }

        total_weighted += score * weight
        total_weight += weight

        if check_info["category"] == "Verify":
            verify_scores.append(score)

    base_score = total_weighted / total_weight if total_weight > 0 else 0

    # Verify phase gate: smooth multiplier from 0.4 (verify_avg=0) to 1.0 (verify_avg>=50)
    verify_avg = sum(verify_scores) / len(verify_scores) if verify_scores else 0
    if verify_avg >= 50:
        final_score = base_score
        results["verify_gate"] = None
    else:
        gate_multiplier = 0.4 + (verify_avg / 50) * 0.6
        final_score = base_score * gate_multiplier
        severity = "severe" if verify_avg < 15 else "moderate" if verify_avg < 30 else "mild"
        results["verify_gate"] = f"{severity} (x{gate_multiplier:.2f}) - verify avg {verify_avg:.0f}/100"

    results["overall_score"] = round(final_score, 1)
    results["verify_avg"] = round(verify_avg, 1)

    # Load AgentReady score if available
    if agentready_results_dir:
        ar_json = os.path.join(agentready_results_dir, repo_name, "assessment-latest.json")
        if os.path.exists(ar_json):
            with open(ar_json) as f:
                ar = json.load(f)
            results["agentready_score"] = ar.get("overall_score", 0)
            results["agentready_level"] = ar.get("certification_level", "N/A")
        else:
            results["agentready_score"] = None
            results["agentready_level"] = None
    else:
        results["agentready_score"] = None
        results["agentready_level"] = None

    return results


def readiness_level(score):
    rounded = round(score)
    if rounded >= 80:
        return "Ready", "#10B981"
    if rounded >= 60:
        return "Partially Ready", "#F59E0B"
    if rounded >= 40:
        return "Needs Work", "#F97316"
    return "Not Ready", "#EF4444"
