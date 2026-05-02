#!/usr/bin/env python3
"""
Extract election entries from docs/elections-library.md into per-election
files at skills/tax-elections-library/references/elections/<slug>.md.
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "docs" / "elections-library.md"
OUT_DIR = ROOT / "skills" / "tax-elections-library" / "references" / "elections"

ELECTION_HEADER = re.compile(r"^## ([A-H]\d+)\.\s+(.+)$")
PART_HEADER = re.compile(r"^# Part [A-H]\.")
END_MARKER = re.compile(r"^# Implementation notes")

# Slugs map per build plan
SLUG_MAP = {
    "A1": "section-351-formation-attachment",
    "A2": "llc-late-c-corp-election",
    "A3": "s-corp-late-election",
    "B1": "section-83b-election",
    "B2": "section-10t-home-equity",
    "C1": "section-266-carrying-cost",
    "C2": "de-minimis-safe-harbor-263a-1f",
    "C3": "section-179-qualifying-property",
    "D1": "section-469-grouping",
    "D2": "reps-rental-aggregation",
    "E1": "section-754-step-up",
    "F1": "s-corp-elections-master-grid",
    "F2": "qsst-election",
    "F3": "esbt-election",
    "F4": "section-1377a2-closing-of-books",
    "F5": "reg-1367-1-basis-reduction-ordering",
    "F6": "reg-1368-1f2-ep-before-aaa",
    "F7": "reg-1368-1f3-deemed-dividend",
    "F8": "s-corp-revocation",
    "F9": "shareholder-consent-revocation",
    "G1": "section-213c-decedent-medical",
    "G2": "portability-waiver",
    "H1": "section-451d-crop-insurance",
    "H2": "section-451e-forced-livestock",
}

def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    text = SRC.read_text(encoding="utf-8").splitlines()
    boundaries: list[tuple[int, str, str]] = []
    end_line = len(text)
    for i, line in enumerate(text):
        if END_MARKER.match(line):
            end_line = i
            break
        m = ELECTION_HEADER.match(line)
        if m:
            boundaries.append((i, m.group(1), m.group(2)))
    written = 0
    for idx, (line_no, code, title) in enumerate(boundaries):
        next_line = boundaries[idx + 1][0] if idx + 1 < len(boundaries) else end_line
        # Walk back from next_line to skip trailing PART header if present
        body_end = next_line
        while body_end > line_no + 1 and (
            PART_HEADER.match(text[body_end - 1]) or text[body_end - 1].strip() == ""
        ):
            body_end -= 1
        body = "\n".join(text[line_no:body_end]).rstrip() + "\n"
        slug = SLUG_MAP.get(code)
        if not slug:
            print(f"WARN: no slug mapped for {code}")
            continue
        # Prepend YAML frontmatter for consistency with other reference files
        clean_title = title.strip()
        frontmatter = (
            "---\n"
            f"election_code: {code}\n"
            f"slug: {slug}\n"
            f"title: \"{clean_title.replace(chr(34), chr(39))}\"\n"
            "status: draft\n"
            "---\n\n"
        )
        target = OUT_DIR / f"{slug}.md"
        target.write_text(frontmatter + body, encoding="utf-8")
        written += 1
        print(f"  {code} -> {slug}.md")
    print(f"\nWrote {written} election files to {OUT_DIR}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
