#!/usr/bin/env python3
"""Append the Phase 10a follow-up-routing instruction to every
skills/*/SKILL.md (idempotent — skips files that already reference
shared/follow-up-routing.md).

The dispatcher (skills/cpa-pack-index/SKILL.md) is edited separately
because its appendix has different boilerplate; it is excluded here.
"""
from __future__ import annotations
from pathlib import Path

ADDENDUM = (
    "\n"
    "After the verification checklist, emit the follow-up-routing block\n"
    "per `shared/follow-up-routing.md` (Phase 10a). The block offers the\n"
    "user two orthogonal handoffs — package the result (`memo` or\n"
    "`open-point`) and carry the conclusion forward (`plan` | `workpaper`\n"
    "| `resolution` | `return`) — and the dispatcher routes the user's\n"
    "reply to the destination skill.\n"
)

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPO_ROOT / "skills"
EXCLUDE = {"cpa-pack-index"}  # handled by hand

def main() -> int:
    updated = skipped = 0
    for skill_md in sorted(SKILLS_ROOT.glob("*/SKILL.md")):
        if skill_md.parent.name in EXCLUDE:
            skipped += 1
            continue
        text = skill_md.read_text(encoding="utf-8")
        if "follow-up-routing.md" in text:
            skipped += 1
            continue
        if not text.endswith("\n"):
            text += "\n"
        text += ADDENDUM
        skill_md.write_text(text, encoding="utf-8")
        updated += 1
        print(f"updated: {skill_md.relative_to(REPO_ROOT).as_posix()}")
    print(f"\nDone. updated={updated} skipped={skipped}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
