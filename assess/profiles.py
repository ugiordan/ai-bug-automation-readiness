# assess/profiles.py
"""Profile resolution for check exclusions."""

import json
import sys
from collections import namedtuple
from pathlib import Path

from .config import CHECKS

ResolvedProfile = namedtuple("ResolvedProfile", ["name", "excluded_checks", "source"])

_BUILTIN_PATH = Path(__file__).parent / "profiles.json"


def load_central_profiles(path=None):
    """Load profiles.json. Returns default structure if file is missing/invalid."""
    p = Path(path) if path else _BUILTIN_PATH
    if not p.exists():
        print(f"  Warning: profiles config not found at {p}, using defaults", file=sys.stderr)
        return {"profiles": {"default": {"description": "All checks", "exclude": []}}, "repos": {}}
    try:
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, KeyError) as e:
        print(f"  Warning: invalid profiles config at {p}: {e}, using defaults", file=sys.stderr)
        return {"profiles": {"default": {"description": "All checks", "exclude": []}}, "repos": {}}


def _validate_check_ids(check_ids, source_label):
    """Return only valid check IDs. Warn on unknown ones."""
    valid = set()
    for cid in check_ids:
        if cid in CHECKS:
            valid.add(cid)
        else:
            print(f"  Warning: unknown check '{cid}' in {source_label}, ignoring", file=sys.stderr)
    return valid


def _validate_category_coverage(excluded):
    """Rule 8: cannot exclude ALL checks in any single category."""
    from .config import CHECKS
    categories = {}
    for cid, info in CHECKS.items():
        categories.setdefault(info["category"], set()).add(cid)
    for cat, cat_checks in categories.items():
        if cat_checks <= excluded:
            sys.exit(f"Error: all {cat} checks would be excluded. At least one check per category must remain.")


def _validate_max_exclusions(excluded, max_allowed=5):
    """Rule 9: max N checks excludable per repo."""
    if len(excluded) > max_allowed:
        sys.exit(f"Error: {len(excluded)} checks excluded, maximum is {max_allowed}.")


def resolve_profile(repo_path, cli_profile=None, cli_exclude_checks=None, central_path=None, org=None):
    """Resolve the effective set of excluded checks for a repo."""
    central = load_central_profiles(central_path)
    repo_name = Path(repo_path).name
    excluded = set()
    source = "default"
    profile_name = "default"

    # Layer 1: central profiles.json repo entry
    # Try qualified org/repo key first, then bare repo name
    repo_entry = None
    if org:
        repo_entry = central.get("repos", {}).get(f"{org}/{repo_name}")
    if not repo_entry:
        repo_entry = central.get("repos", {}).get(repo_name)
    if repo_entry:
        source = "profiles.json"
        entry_profile = repo_entry.get("profile", "default")
        profile_def = central.get("profiles", {}).get(entry_profile)
        if profile_def:
            profile_name = entry_profile
            excluded |= _validate_check_ids(profile_def.get("exclude", []), f"profile '{entry_profile}'")
        else:
            print(f"  Warning: profile '{entry_profile}' not found for {repo_name}, using default", file=sys.stderr)

        # exclude_also (additive) -- Rule 3: must not duplicate profile excludes, Rule 5: reason required
        if "exclude_also" in repo_entry:
            if "reason" not in repo_entry:
                print(f"  Warning: 'reason' missing for exclude_also in {repo_name}", file=sys.stderr)
            also = _validate_check_ids(repo_entry["exclude_also"], f"exclude_also for {repo_name}")
            redundant = also & excluded
            if redundant:
                print(f"  Warning: exclude_also {redundant} already excluded by profile '{entry_profile}' in {repo_name}", file=sys.stderr)
            excluded |= also

        # include_back (subtractive) -- Rule 2: must exist in profile's exclude list, Rule 5: reason required
        if "include_back" in repo_entry:
            if "reason" not in repo_entry:
                print(f"  Warning: 'reason' missing for include_back in {repo_name}", file=sys.stderr)
            include_back = _validate_check_ids(repo_entry["include_back"], f"include_back for {repo_name}")
            profile_excludes = set(_validate_check_ids(profile_def.get("exclude", []), "")) if profile_def else set()
            invalid_back = include_back - profile_excludes
            if invalid_back:
                print(f"  Warning: include_back {invalid_back} not in profile '{entry_profile}' exclude list for {repo_name}", file=sys.stderr)
            excluded -= include_back

    # Layer 2: CLI --profile override (replaces JSON profile, not additive)
    if cli_profile:
        profile_def = central.get("profiles", {}).get(cli_profile)
        if profile_def:
            profile_name = cli_profile
            # Reset excluded to CLI profile's excludes (override, not union)
            cli_excludes = _validate_check_ids(profile_def.get("exclude", []), f"CLI profile '{cli_profile}'")
            # Keep exclude_also from repo entry but replace profile excludes
            repo_also = set()
            if repo_entry and "exclude_also" in repo_entry:
                repo_also = _validate_check_ids(repo_entry["exclude_also"], f"exclude_also for {repo_name}")
            excluded = cli_excludes | repo_also
            source = "cli"
        else:
            print(f"  Warning: profile '{cli_profile}' not found, using default", file=sys.stderr)
            profile_name = "default"

    # Layer 3: CLI --exclude-checks (additive)
    if cli_exclude_checks:
        excluded |= _validate_check_ids(cli_exclude_checks, "CLI --exclude-checks")
        source = "cli"

    # Apply profile from profiles.json if no repo entry and no CLI override
    if not repo_entry and not cli_profile and not cli_exclude_checks:
        profile_name = "default"
        source = "default"

    # Validations
    remaining = set(CHECKS.keys()) - excluded
    if not remaining:
        sys.exit(f"Error: all checks excluded for {repo_name}. At least one check must remain.")
    _validate_category_coverage(excluded)
    _validate_max_exclusions(excluded)

    return ResolvedProfile(
        name=profile_name,
        excluded_checks=frozenset(excluded),
        source=source,
    )
