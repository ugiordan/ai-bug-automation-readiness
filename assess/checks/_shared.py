"""Shared constants and helpers used across check modules."""

from pathlib import Path

from ..config import SOURCE_EXTS
from ..utils import is_generated_file

TEST_FILE_PATTERNS = ["_test.", "test_", "_spec.", ".spec.", ".test.", ".cy.", "Test.", "Tests."]

TEST_HELPER_PATTERNS = [
    "conftest",
    "helper",
    "helpers",
    "utils",
    "util",
    "fixture",
    "fixtures",
    "factory",
    "factories",
    "common",
    "setup",
    "base",
    "shared",
    "support",
    "mock",
    "mocks",
    "matchers",
    "scheme",
    "types",
    "testutil",
    "testutils",
]


def _source_files_from(all_files: list[Path]) -> list[Path]:
    """Filter to non-generated source files."""
    return [f for f in all_files if f.is_file() and f.suffix.lower() in SOURCE_EXTS and not is_generated_file(f)]


def _is_test_file(path: Path) -> bool:
    """Check if a file is a test file (not a test helper)."""
    name = path.name.lower()
    in_test_dir = "__tests__" in path.parts or "tests" in path.parts or "test" in path.parts
    is_helper = any(name.startswith(hp) or f"_{hp}" in name for hp in TEST_HELPER_PATTERNS)
    return any(tp in name for tp in TEST_FILE_PATTERNS) or (in_test_dir and not is_helper)
