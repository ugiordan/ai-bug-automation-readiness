"""Filesystem and language detection utilities."""

import sys
from functools import lru_cache
from pathlib import Path

from .config import EXCLUDE_DIRS, GENERATED_FILE_PATTERNS, GENERATED_HEADER_MARKERS, SOURCE_EXTS


def find_files(repo_path, pattern, exclude_dirs=None):
    exclude = exclude_dirs or EXCLUDE_DIRS
    results = []
    for p in Path(repo_path).rglob(pattern):
        if not any(ex in p.parts for ex in exclude):
            results.append(p)
    return results


def find_all_files_cached(repo_path):
    """Single directory traversal per repo — returns all non-excluded files."""
    return find_files(repo_path, "*")


@lru_cache(maxsize=8192)
def is_generated_file(path):
    """Check if a file is auto-generated (cached)."""
    path = Path(path)
    if GENERATED_FILE_PATTERNS.search(str(path)):
        return True
    try:
        with open(path, "r", errors="ignore") as f:
            header = f.read(500)
        return any(marker in header for marker in GENERATED_HEADER_MARKERS)
    except PermissionError:
        print(f"  Warning: Permission denied reading {path}", file=sys.stderr)
        return False
    except OSError:
        return False


def read_file_safe(path, max_bytes=50000):
    try:
        with open(path, "r", errors="ignore") as f:
            return f.read(max_bytes)
    except PermissionError:
        print(f"  Warning: Permission denied reading {path}", file=sys.stderr)
        return ""
    except OSError:
        return ""


def count_lines_fast(path):
    """Count lines without reading full file into memory."""
    try:
        with open(path, "rb") as f:
            return sum(1 for _ in f)
    except OSError:
        return 0


def detect_languages(repo_path, all_files=None):
    """Detect languages sorted by file count (primary first)."""
    files = all_files if all_files is not None else find_all_files_cached(repo_path)
    exts = {}
    for f in files:
        if f.is_file() and not is_generated_file(f):
            ext = f.suffix.lower()
            exts[ext] = exts.get(ext, 0) + 1
    lang_map = {
        ".go": "Go", ".py": "Python", ".js": "JavaScript", ".ts": "TypeScript",
        ".tsx": "TypeScript", ".jsx": "JavaScript",
        ".java": "Java", ".rs": "Rust", ".rb": "Ruby", ".cpp": "C++", ".c": "C",
    }
    langs = [(name, exts.get(ext, 0)) for ext, name in lang_map.items() if exts.get(ext, 0) > 2]
    merged = {}
    for name, count in langs:
        merged[name] = merged.get(name, 0) + count
    return [name for name, _ in sorted(merged.items(), key=lambda x: x[1], reverse=True)] or ["Unknown"]
