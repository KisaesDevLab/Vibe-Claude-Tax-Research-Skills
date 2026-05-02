#!/usr/bin/env python3
"""
Extract strategy files from docs/addendum-strategy-library-part-{2..10}-of-10.md.

Each part contains repeated blocks of:

    ## Strategy #N: <title>

    **File:** `references/strategies/<slug>.md`

    ```markdown
    <file content; may contain nested ```json / ```text fences>
    ```

The outer ```markdown fence wraps the whole file. We extract the inner
content and write it to skills/planning-strategy-library/references/strategies/<slug>.md.

Idempotent: overwrites existing files.

Strategies #1-7 (Part 1) are not provided; Parts 2-10 cover #8-94.
Existing 30 strategy files are NOT touched (per "keep both" direction).
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT_DIR = ROOT / "skills" / "planning-strategy-library" / "references" / "strategies"

PART_FILES = [DOCS / f"addendum-strategy-library-part-{n}-of-10.md" for n in range(2, 11)]

STRATEGY_HEADER = re.compile(r"^## Strategy #(\d+):")
FILE_LINE = re.compile(r"^\*\*File:\*\*\s+`references/strategies/([^`]+)`")
FENCE_OPEN_TAGGED = re.compile(r"^```[a-zA-Z][a-zA-Z0-9_-]*\s*$")
FENCE_BARE = re.compile(r"^```\s*$")

# Slugs that collide with existing curated 30-strategy library entries.
# For these, the addendum version is written to <slug>-extended.md, and
# internal cross-references inside ALL extracted addendum files are
# rewritten to point at the -extended variant so the addendum's mutual
# references stay internally consistent.
COLLISION_SLUGS = {
    "backdoor-roth",
    "cost-segregation",
    "real-estate-professional",
    "section-1202-qsbs",
}

def extract_from_part(path: Path) -> list[tuple[int, str, str]]:
    """Return list of (strategy_number, slug, content)."""
    lines = path.read_text(encoding="utf-8").splitlines()
    out: list[tuple[int, str, str]] = []
    i = 0
    n = len(lines)
    while i < n:
        m = STRATEGY_HEADER.match(lines[i])
        if not m:
            i += 1
            continue
        strat_num = int(m.group(1))
        # Walk forward until **File:** line
        j = i + 1
        slug = None
        while j < n and j < i + 10:
            fm = FILE_LINE.match(lines[j])
            if fm:
                slug = fm.group(1).removesuffix(".md")
                break
            j += 1
        if slug is None:
            print(f"WARN: no File: line near strategy #{strat_num} in {path.name}")
            i = j + 1
            continue
        # Walk forward until any tagged opening fence (```markdown,
        # ```permission, etc.). Source uses inconsistent tags.
        k = j + 1
        while k < n:
            stripped = lines[k].strip()
            if FENCE_OPEN_TAGGED.match(stripped):
                break
            # Stop if we hit the next strategy header without finding a fence
            if STRATEGY_HEADER.match(stripped):
                break
            k += 1
        if k >= n or not FENCE_OPEN_TAGGED.match(lines[k].strip()):
            print(f"WARN: no opening fence found for #{strat_num}")
            i = k + 1
            continue
        # Inside outer markdown fence; depth=1
        depth = 1
        body_start = k + 1
        m_idx = body_start
        while m_idx < n and depth > 0:
            line = lines[m_idx]
            if FENCE_BARE.match(line):
                depth -= 1
                if depth == 0:
                    break
            elif FENCE_OPEN_TAGGED.match(line):
                depth += 1
            m_idx += 1
        if depth != 0:
            print(f"WARN: unbalanced fences for strategy #{strat_num}")
            i = m_idx + 1
            continue
        body = "\n".join(lines[body_start:m_idx]) + "\n"
        out.append((strat_num, slug, body))
        i = m_idx + 1
    return out

def remap_collisions(body: str) -> str:
    """Rewrite internal references to collision slugs to their -extended form.

    Handles:
      - Backtick references like `cost-segregation` → `cost-segregation-extended`
      - Bare slug appearances are NOT rewritten (too noisy).
    """
    out = body
    for slug in COLLISION_SLUGS:
        # Only rewrite when wrapped in backticks (cross-ref convention).
        out = out.replace(f"`{slug}`", f"`{slug}-extended`")
    return out

def scrub_branding(body: str) -> str:
    """Remove Bradford / TaxSpeaker / similar branding mentions."""
    # No occurrences in addendum content per pre-scan, but defense in depth.
    replacements = [
        (re.compile(r"Bradford Tax Institute", re.IGNORECASE), "practitioner literature"),
        (re.compile(r"\bBradford\b", re.IGNORECASE), "practitioner"),
        (re.compile(r"TaxSpeaker", re.IGNORECASE), "CPE source"),
    ]
    out = body
    for pattern, repl in replacements:
        out = pattern.sub(repl, out)
    return out

def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written: list[tuple[int, str, Path]] = []
    seen_slugs: set[str] = set()
    for part in PART_FILES:
        if not part.exists():
            print(f"SKIP (missing): {part.name}")
            continue
        items = extract_from_part(part)
        for strat_num, slug, body in items:
            body = scrub_branding(body)
            body = remap_collisions(body)
            out_slug = f"{slug}-extended" if slug in COLLISION_SLUGS else slug
            target = OUT_DIR / f"{out_slug}.md"
            if out_slug in seen_slugs:
                print(f"WARN: duplicate slug across parts: {out_slug} (#{strat_num})")
            seen_slugs.add(out_slug)
            target.write_text(body, encoding="utf-8")
            written.append((strat_num, out_slug, target))
    written.sort()
    print(f"Wrote {len(written)} strategy files.")
    for s, slug, _ in written:
        print(f"  #{s:>2}  {slug}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
