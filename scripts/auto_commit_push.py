#!/usr/bin/env python3
"""
auto_commit_push.py — commit + push every change in THIS repo, non-blocking.

Wired to a Claude Code Stop hook so the second brain is committed and pushed
"all the time" (per user instruction 2026-05-30). Design rules:

- **Shell-agnostic**: all git work via subprocess, so it runs identically under
  cmd / PowerShell / bash. The hook only needs `python <this file>`.
- **Non-blocking**: ALWAYS exits 0. A failed push (offline, auth, conflict) must
  never block the session or lose the local commit — the commit still lands and
  pushes on the next turn.
- **No empty commits**: does nothing if the tree is clean.
- **Self-locating**: targets the repo this file lives in, regardless of the
  session's working directory.

Manual use: `python scripts/auto_commit_push.py`
"""
from __future__ import annotations

import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def git(*args: str, check: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(REPO), *args],
        capture_output=True, text=True, check=check,
    )


def main() -> int:
    # Are we even in a git repo?
    if git("rev-parse", "--is-inside-work-tree").returncode != 0:
        print("auto_commit_push: not a git repo, skipping")
        return 0

    # Stage everything (respects .gitignore).
    git("add", "-A")

    # Anything to commit?
    if not git("status", "--porcelain").stdout.strip():
        print("auto_commit_push: clean tree, nothing to commit")
        return 0

    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit = git("commit", "-m", f"auto: session checkpoint {stamp}")
    if commit.returncode != 0:
        # e.g. nothing staged after all, or a hook rejected it — don't block.
        print(f"auto_commit_push: commit skipped ({commit.stderr.strip()[:120]})")
        return 0
    print(f"auto_commit_push: committed @ {stamp}")

    # Determine current branch and push it.
    branch = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip() or "main"
    push = git("push", "origin", branch)
    if push.returncode == 0:
        print(f"auto_commit_push: pushed {branch} -> origin")
    else:
        # Offline / auth / non-fast-forward: keep the local commit, retry next turn.
        print(f"auto_commit_push: push failed, commit kept locally "
              f"({push.stderr.strip()[:160]})")
    return 0


if __name__ == "__main__":
    # Never propagate a non-zero exit to the hook runner.
    try:
        sys.exit(main())
    except Exception as e:  # pragma: no cover - safety net
        print(f"auto_commit_push: error, ignored ({e})")
        sys.exit(0)
