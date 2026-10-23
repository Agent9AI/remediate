#!/usr/bin/env python3
"""Check repository documentation presence and relative file links.

Uses only the Python standard library. Does not test the application, external
websites, anchor rendering, security effectiveness, or claimed performance.
"""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md", "AGENTS.md", "CONTRIBUTING.md", "SECURITY.md", "LICENSE",
    "docs/BUILD_PLAN.md", "docs/PROJECT_STATE.md", "docs/ROADMAP.md",
    "docs/ARCHITECTURE.md", "docs/DECISIONS.md", "docs/TENABLE.md",
    "docs/VALIDATION.md", "docs/DEMO.md", "docs/SUBMISSION.md",
    "docs/DEPENDENCIES.md", "docs/SESSION_LOG.md",
    "docs/reference/Agent9-Remediate-SWARM-Build-Plan-2026-10-23.docx",
)


def main():
    failures = []
    for name in REQUIRED:
        path = ROOT / name
        if not path.is_file() or path.stat().st_size == 0:
            failures.append(f"Missing or empty required file: {name}")

    files = sorted(ROOT.rglob("*.md"))
    links = 0
    for path in files:
        if ".git" in path.parts:
            continue
        body = path.read_text(encoding="utf-8")
        body = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", body, flags=re.M | re.S)
        for match in re.finditer(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", body):
            target = match.group(1).strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            dest = (path.parent / unquote(parsed.path)).resolve()
            links += 1
            if not dest.is_relative_to(ROOT):
                failures.append(f"{path.relative_to(ROOT)}: link leaves repository: {target}")
            elif not dest.exists():
                failures.append(f"{path.relative_to(ROOT)}: missing target: {target}")

    if failures:
        print("Documentation checks failed:")
        print("\n".join(f"- {item}" for item in failures))
        return 1
    print(f"Documentation checks passed: {len(REQUIRED)} required files; {len(files)} Markdown files; {links} relative file links.")
    print("Scope: file presence and relative file links only. Application validation is not performed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
