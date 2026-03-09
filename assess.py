#!/usr/bin/env python3
"""AI Bug Automation Readiness Assessment.

Evaluates whether repositories are ready for AI agents to autonomously
find, fix, and verify bugs. Focuses on what actually matters for that
workflow: can the agent understand the bug, navigate the code, verify
a fix with tests, and submit it properly?

Usage:
    python assess.py /path/to/repo                     # Single repo, text output
    python assess.py /path/to/repo --format json       # JSON output
    python assess.py --batch /path/to/repos --format html  # Batch scan, HTML report
"""

from assess.cli import main

if __name__ == "__main__":
    main()
