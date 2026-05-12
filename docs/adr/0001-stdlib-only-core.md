# ADR 0001: stdlib-only core modules

## Status

Accepted

## Context

This tool assesses repositories for AI agent readiness. It needs to run in CI environments and on developer machines without complex dependency management. The assessment logic (checks, engine, config, profiles) must be reliable and fast.

## Decision

Core modules (`assess/checks.py`, `assess/engine.py`, `assess/config.py`, `assess/profiles.py`, `assess/utils.py`, `assess/cli.py`) use only the Python standard library. External dependencies are limited to optional report formats: `python-docx` for DOCX output, lazy-imported so the tool works without it.

## Consequences

- The tool can run with zero `pip install` for the default text/json/html/csv/markdown output formats.
- Check functions are constrained to stdlib regex, file I/O, and path manipulation. No AST parsing, no external linters, no HTTP calls.
- Report generators for optional formats (DOCX) are isolated in their own modules with lazy imports.
- Dev dependencies (ruff, mypy, pytest) are separate from runtime.
