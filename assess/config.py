"""Configuration constants for AI Bug Automation Readiness Assessment."""

import re

# ---------------------------------------------------------------------------
# Generated / non-human file patterns to exclude from analysis
# ---------------------------------------------------------------------------
GENERATED_FILE_PATTERNS = re.compile(
    r"(zz_generated|_generated\.go|\.pb\.go|openapi_generated|"
    r"generated\.deepcopy|mock_.*\.go|_mock\.go|clientset/|informers/|listers/)",
    re.IGNORECASE,
)

GENERATED_HEADER_MARKERS = [
    "// Code generated",
    "// DO NOT EDIT",
    "# Code generated",
    "# DO NOT EDIT",
    "AUTO-GENERATED",
]

EXCLUDE_DIRS = frozenset({
    ".git", "vendor", "node_modules", "third_party", "__pycache__",
    "testdata", ".terraform", "dist", "build",
})

# ---------------------------------------------------------------------------
# Source code file extensions (shared across checks)
# ---------------------------------------------------------------------------
SOURCE_EXTS = frozenset({
    ".go", ".py", ".js", ".ts", ".tsx", ".jsx", ".java", ".rs",
    ".rb", ".cpp", ".c", ".h",
})

# ---------------------------------------------------------------------------
# Weights (must sum to 100)
# ---------------------------------------------------------------------------
CHECKS = {
    "agent_context":      {"name": "AI Context Files",              "weight":  5, "category": "Understand"},
    "bug_template":       {"name": "Bug Report Template Quality",   "weight": 12, "category": "Understand"},
    "structured_logging": {"name": "Structured Logging / Errors",   "weight":  5, "category": "Understand"},
    "code_navigability":  {"name": "Code Navigability",             "weight":  8, "category": "Navigate"},
    "generated_code":     {"name": "Generated Code Ratio",          "weight":  5, "category": "Navigate"},
    "codeowners":         {"name": "Code Ownership (CODEOWNERS)",   "weight":  3, "category": "Submit"},
    "test_ratio":         {"name": "Test-to-Source Ratio",          "weight": 17, "category": "Verify"},
    "test_execution":     {"name": "One-Command Test Execution",    "weight": 12, "category": "Verify"},
    "coverage_config":    {"name": "Coverage Configuration",        "weight":  5, "category": "Verify"},
    "ci_runs_tests":      {"name": "CI Runs Tests on PRs",         "weight": 10, "category": "Verify"},
    "pr_template":        {"name": "PR Template",                   "weight":  3, "category": "Submit"},
    "linting_in_ci":      {"name": "Linting / Formatting in CI",   "weight":  5, "category": "Submit"},
    "contributing_guide": {"name": "Contributing / Dev Guide",      "weight":  5, "category": "Submit"},
    "test_isolation":     {"name": "Test Isolation (unit vs e2e)",  "weight":  5, "category": "Verify"},
}

# ---------------------------------------------------------------------------
# Recommendations per check (shown when score < threshold)
# ---------------------------------------------------------------------------
RECOMMENDATIONS = {
    "agent_context": "Create an AGENTS.md at the repo root describing architecture, how to build, test, and debug. For Claude users, a CLAUDE.md is also supported. Other recognized files: COPILOT.md, .cursorrules, CONTEXT.md.",
    "bug_template": "Add .github/ISSUE_TEMPLATE/bug_report.yml with required fields: reproduction steps, expected/actual behavior, environment, and error logs.",
    "structured_logging": "Adopt a structured logging library (e.g., logr/zap for Go, structlog for Python) and wrap errors with context.",
    "code_navigability": "Break large files (>500 lines) into smaller, focused modules. Exclude generated files from linting.",
    "generated_code": "Add '// Code generated' headers to generated files and document which files are auto-generated in CLAUDE.md.",
    "codeowners": "Create a .github/CODEOWNERS file mapping directories to team members for automated PR review assignment.",
    "test_ratio": "Add unit tests for critical code paths. Aim for at least 1 test file per 2 source files.",
    "test_execution": "Add a 'make test' or 'make unittest' target that runs unit tests without external dependencies.",
    "coverage_config": "Configure coverage reporting (e.g., -coverprofile for Go, pytest-cov for Python) and add a Codecov or Coveralls integration.",
    "ci_runs_tests": "Ensure CI workflows triggered by pull_request events include a step that runs tests.",
    "pr_template": "Add .github/PULL_REQUEST_TEMPLATE.md with a testing checklist.",
    "linting_in_ci": "Add a linting step (golangci-lint, eslint, ruff) to your CI pipeline.",
    "contributing_guide": "Add CONTRIBUTING.md with build, test, and debug instructions.",
    "test_isolation": "Separate unit tests (no external deps) from integration/e2e tests using build tags or directory structure.",
}
