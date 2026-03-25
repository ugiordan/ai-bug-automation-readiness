#!/usr/bin/env python3
"""Read scan-config.json and clone repos into nested org/repo layout."""
import subprocess
import sys
from pathlib import Path

# Allow importing assess package from repo root
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from assess.scan_config import load_scan_config


def main():
    config_path = sys.argv[1] if len(sys.argv) > 1 else "scan-config.json"
    dest = Path(sys.argv[2] if len(sys.argv) > 2 else "/tmp/repos")

    config = load_scan_config(config_path)

    for org, org_cfg in config["orgs"].items():
        org_dir = dest / org
        org_dir.mkdir(parents=True, exist_ok=True)

        if org_cfg["mode"] == "all":
            result = subprocess.run(
                ["gh", "repo", "list", org, "--limit", "300",
                 "--json", "name,isArchived",
                 "-q", '.[] | select(.isArchived == false) | .name'],
                capture_output=True, text=True, check=True
            )
            repos = [r for r in result.stdout.strip().split('\n') if r]
            exclude = set(org_cfg.get("exclude", []))
            repos = [r for r in repos if r not in exclude]
        else:
            repos = org_cfg["repos"]

        print(f"Cloning {len(repos)} repos from {org}...")
        for repo in repos:
            target = org_dir / repo
            if target.exists():
                continue
            r = subprocess.run(
                ["gh", "repo", "clone", f"{org}/{repo}", str(target),
                 "--", "--depth", "1", "--single-branch"],
                capture_output=True
            )
            if r.returncode == 0:
                print(f"  Cloned {org}/{repo}")
            else:
                print(f"  SKIP {org}/{repo} (clone failed)", file=sys.stderr)


if __name__ == "__main__":
    main()
