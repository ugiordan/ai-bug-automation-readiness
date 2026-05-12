"""AI Bug Automation Readiness Assessment."""

from typing import Any

from .engine import assess_repo, readiness_level
from .reports.csv_report import generate_csv
from .reports.html import generate_html
from .reports.markdown import generate_markdown

__all__ = [
    "assess_repo",
    "readiness_level",
    "generate_html",
    "generate_markdown",
    "generate_csv",
    "generate_docx",
]


def generate_docx(*args: Any, **kwargs: Any) -> Any:
    """Lazy import -- requires python-docx: pip install python-docx."""
    from .reports.docx_report import generate_docx as _generate_docx

    return _generate_docx(*args, **kwargs)
