"""AI Bug Automation Readiness Assessment."""

from .engine import assess_repo, readiness_level
from .reports.html import generate_html
from .reports.markdown import generate_markdown
from .reports.csv_report import generate_csv

__all__ = [
    "assess_repo",
    "readiness_level",
    "generate_html",
    "generate_markdown",
    "generate_csv",
    "generate_docx",
]


def generate_docx(*args, **kwargs):
    """Lazy import — requires python-docx: pip install python-docx."""
    from .reports.docx_report import generate_docx as _generate_docx
    return _generate_docx(*args, **kwargs)
