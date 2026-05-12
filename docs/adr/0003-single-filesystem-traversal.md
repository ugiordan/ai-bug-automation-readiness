# ADR 0003: Single filesystem traversal per repository

## Status

Accepted

## Context

The assessment engine runs 20 checks per repository. Many checks need to inspect the same files (e.g., test ratio and test isolation both need to enumerate test files, navigability and generated code ratio both traverse source files).

In early implementations, each check performed its own filesystem traversal. Scanning large repos (10k+ files) repeatedly caused noticeable slowdowns, especially in batch mode.

## Decision

Perform a single filesystem traversal per repository during the scan initialization phase. Cache the results in a shared data structure (`assess/engine.py:FileCache`) that all checks can query.

The cache stores:
- All file paths (relative to repo root)
- File extensions
- File sizes
- Basic file type categorization (source, test, generated, config)

Checks receive the cache and query it via utility functions instead of calling `os.walk()` or `pathlib.Path.glob()` directly.

## Consequences

- 3-5x faster batch scans observed in practice (100-repo scan drops from ~90s to ~20s).
- Memory usage increases slightly (cache holds full file list in memory), but this is negligible for typical repos (<50k files).
- Check functions must use shared cache queries instead of arbitrary filesystem traversal patterns.
- Cache invalidation is not needed because scans are read-only snapshots.
- Thread safety: each repo gets its own cache instance, so parallel batch scans remain safe.
