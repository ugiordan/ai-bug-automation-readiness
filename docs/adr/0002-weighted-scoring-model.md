# ADR 0002: Weighted scoring model with verify gate multiplier

## Status

Accepted

## Context

Repositories vary widely in their suitability for AI-assisted bug fixing. A simple binary pass/fail or unweighted checklist would treat documentation gaps the same as missing test infrastructure, even though the latter is fundamentally blocking for autonomous bug fixes.

Additionally, a repo with perfect documentation but zero tests shouldn't score 80%. The ability to verify a fix is non-negotiable for autonomous bug fixing.

## Decision

The scoring system uses:

1. **Fixed weighted checks** across 4 phases: Understand (24%), Navigate (17%), Verify (46%), Submit (13%)
2. **Verify phase gate multiplier**: if the average Verify phase score is below 50, apply a smooth linear penalty from x0.4 (verify avg = 0) to x1.0 (verify avg = 50)
3. **No user-configurable weights** to prevent gaming and ensure comparable scores across repos

The Verify phase carries 46% of the total weight because test infrastructure is the critical path for autonomous bug fixing. The gate multiplier eliminates edge cases where strong documentation inflates scores despite absent test infrastructure.

## Consequences

- Repos cannot score above 60% without basic test infrastructure (verify avg >= 50).
- Weights are transparent and consistent across all scanned repos.
- Weight configuration is centralized in `assess/config.py` and cannot be overridden per-repo.
- The multiplier uses a smooth linear scale (not step functions) to avoid cliff effects and ensure small improvements are reflected in the score.
