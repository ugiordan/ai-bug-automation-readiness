"""Scan configuration loader and validator."""

import json
import re


_ORG_PATTERN = re.compile(r'^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?$')


def load_scan_config(path="scan-config.json"):
    """Load and validate scan-config.json. Returns config dict.

    Raises FileNotFoundError if path doesn't exist.
    Raises ValueError on validation failure.
    """
    with open(path, "r", encoding="utf-8") as f:
        config = json.load(f)

    _validate(config)
    return config


def _validate(config):
    """Validate scan config against rules 1-6 from spec."""
    if not isinstance(config.get("orgs"), dict) or not config["orgs"]:
        raise ValueError("'orgs' must be a non-empty dict")

    for org_name, org_cfg in config["orgs"].items():
        if not _ORG_PATTERN.match(org_name):
            raise ValueError(f"Invalid org name: '{org_name}'. Must be alphanumeric with hyphens.")

        mode = org_cfg.get("mode")
        if mode not in ("all", "include"):
            raise ValueError(f"Org '{org_name}': mode must be 'all' or 'include', got '{mode}'")

        if mode == "all":
            if "repos" in org_cfg:
                raise ValueError(f"Org '{org_name}': 'repos' key is forbidden with mode 'all'")
            exclude = org_cfg.get("exclude", [])
            if not isinstance(exclude, list) or not all(isinstance(r, str) for r in exclude):
                raise ValueError(f"Org '{org_name}': 'exclude' must be a list of strings")

        elif mode == "include":
            if "exclude" in org_cfg:
                raise ValueError(f"Org '{org_name}': 'exclude' key is forbidden with mode 'include'")
            repos = org_cfg.get("repos")
            if not isinstance(repos, list) or not repos:
                raise ValueError(f"Org '{org_name}': 'repos' must be a non-empty list with mode 'include'")
            if not all(isinstance(r, str) for r in repos):
                raise ValueError(f"Org '{org_name}': all repo names must be strings")
            for r in repos:
                if "/" in r:
                    raise ValueError(f"Org '{org_name}': repo name '{r}' must not contain slashes")

        for r in org_cfg.get("exclude", []):
            if "/" in r:
                raise ValueError(f"Org '{org_name}': exclude name '{r}' must not contain slashes")
