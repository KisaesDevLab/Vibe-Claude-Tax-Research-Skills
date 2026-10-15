#!/usr/bin/env python3
"""Build a single claude.ai skill ZIP containing the whole Vibe CPA pack.

claude.ai installs skills one ZIP at a time. This script folds all 46
skills into one skill whose SKILL.md is the cpa-pack-index dispatcher;
each specialist becomes a WORKFLOW.md file the dispatcher reads on
demand (progressive disclosure).

Bundle layout (paths inside the ZIP):

    vibe-cpa-pack/
      SKILL.md                         dispatcher (only frontmatter in the bundle)
      LICENSE, DISCLAIMER.md
      shared/                          rules of the road, unchanged
      skills/INDEX.md                  catalog: name -> workflow path + "use when"
      skills/<name>/WORKFLOW.md        specialist SKILL.md, frontmatter stripped
      skills/<name>/references/...     unchanged

Keeping `shared/` and `skills/<name>/` at their repo-relative paths means
cross-references such as `shared/compliance.md` or
`skills/tax-research-state-income/references/states/CA.md` resolve
without rewriting.

Usage: python3 scripts/build-claude-ai-bundle.py [--out dist]
Exit code is non-zero if a referenced path is missing or a limit fails.
"""

import argparse
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUNDLE_NAME = "vibe-cpa-pack"
DISPATCHER = "cpa-pack-index"

DESCRIPTION = (
    "Complete Vibe CPA Skills pack (46 workflows) for licensed CPAs, EAs, "
    "and tax attorneys. Routes each request to a specialist workflow: "
    "federal, entity, payroll, international, procedure, estate/gift and "
    "51-jurisdiction state income and sales/use tax research; predictions "
    "(worker classification, hobby loss, reasonable comp, material "
    "participation, QBI, 1031, economic substance, R&D credit); 1040 and "
    "entity return summaries; IRS notice responses; tax planning and a "
    "strategy library; S-corp and Schedule C catalogs; elections; IRC / "
    "Treas. Reg. / Public Law lookups (TCJA, IRA, OBBBA, SECURE 2.0); due "
    "dates; penalty and interest; SSTS / Circular 230; AICPA Code, SSARS, "
    "SAS, SSAE / SOC, SQMS; engagement letters; workpapers; FASB ASC, ASC "
    "740, 606, 842. Enforces citation discipline, confidence bands, and a "
    "verification checklist. Use when the user asks a tax, accounting, "
    "audit, attest, or GAAP question, pastes an IRS notice or return, or "
    "asks which skill to use."
)

PREAMBLE = """\
# Vibe CPA Pack — single-skill bundle

This one skill contains the entire Vibe CPA Skills pack. The body
below is the pack dispatcher (`cpa-pack-index`). Every specialist
skill the dispatcher names lives in this bundle as a workflow file.

## How to run a specialist inside this bundle

1. **Read the shared rules first.** The `shared/` folder sits next to
   this file. Read the files listed in "Read before output" below
   before every substantive answer.
2. **Resolve skill names to files.** Whenever this file, a workflow,
   or a shared file says to route or hand off to a skill named
   `<name>` (e.g. `tax-research-federal`), read
   `skills/<name>/WORKFLOW.md` and follow it as if that skill had
   been invoked. The full catalog with "use when" summaries is in
   `skills/INDEX.md`; consult it when the routing table below is not
   decisive. `cpa-pack-index` (and `skills/cpa-pack-index/SKILL.md`)
   means this file.
3. **Resolve relative references.** Inside a workflow, a path that
   starts with `references/` is relative to that workflow's own
   folder: `references/case-law.md` in
   `skills/predict-worker-classification/WORKFLOW.md` means
   `skills/predict-worker-classification/references/case-law.md`.
   Paths that start with `shared/` or `skills/` are relative to this
   bundle's root.
4. **Do not print the routing card when the answer is obvious.**
   When the request clearly maps to one workflow, load it silently
   and answer; mention the workflow name in one line at the top.
   Show the routing card only when the request is ambiguous or the
   user asks which skill to use.
5. **Keep the output contract.** Every specialist answer ends with
   the verification checklist (`shared/compliance.md`), the
   follow-up-routing block (`shared/follow-up-routing.md`), and the
   JSON sidecar (`shared/output-schema.json`). When the user replies
   to the follow-up block, run the destination workflow from this
   bundle.
6. **Live sources.** Canonical primary-source URLs are in
   `shared/live-sources.md` and `shared/sources.json`. Retrieve with
   web search / fetch when available. If retrieval is unavailable,
   use the `[CITATION NEEDED — search: <query>]` sentinel; never
   fabricate a citation.

---

"""


def split_frontmatter(text):
    """Return (frontmatter_dict_of_raw_strings, body)."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.index("\n---", 4)
    fm_text = text[4:end]
    body = text[end + 4:].lstrip("\n")
    fm = {}
    key = None
    for line in fm_text.splitlines():
        m = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if m:
            key = m.group(1)
            val = m.group(2).strip()
            fm[key] = "" if val in ("|", ">") else val
        elif key and line.startswith(" "):
            fm[key] = (fm[key] + " " + line.strip()).strip()
    return fm, body


def rewrite_routing_rows(body, names):
    """In table rows, point `skill-name` at its WORKFLOW.md path."""
    pattern = re.compile(r"`(" + "|".join(map(re.escape, names)) + r")`")
    out = []
    for line in body.splitlines():
        if line.lstrip().startswith("|"):
            line = pattern.sub(lambda m: f"`{m.group(1)}` (`skills/{m.group(1)}/WORKFLOW.md`)", line)
        out.append(line)
    return "\n".join(out) + "\n"


def check_references(bundle):
    """Every concrete shared/... or skills/<name>/... path cited must exist."""
    path_re = re.compile(r"(?<![\w/.-])((?:shared|skills/[a-z0-9-]+)/[A-Za-z0-9_./-]*[A-Za-z0-9_-]\.(?:md|json))")
    missing = set()
    for f in bundle.rglob("*.md"):
        for m in path_re.finditer(f.read_text(encoding="utf-8")):
            ref = m.group(1)
            if ref.startswith(f"skills/{DISPATCHER}/"):
                continue  # the dispatcher is the bundle's root SKILL.md
            if ref.endswith("/SKILL.md"):
                ref = ref[: -len("SKILL.md")] + "WORKFLOW.md"
            if not (bundle / ref).exists():
                missing.add((ref, str(f.relative_to(bundle))))
    return sorted(missing)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "dist"))
    args = ap.parse_args()

    out_dir = Path(args.out)
    stage = out_dir / BUNDLE_NAME
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir(parents=True)

    skill_dirs = sorted(p for p in (ROOT / "skills").iterdir() if (p / "SKILL.md").is_file())
    names = [p.name for p in skill_dirs]
    errors = []

    shutil.copytree(ROOT / "shared", stage / "shared")
    for extra in ("LICENSE", "DISCLAIMER.md"):
        shutil.copy2(ROOT / extra, stage / extra)

    catalog = ["# Skill catalog\n",
               "Each entry: workflow file to read, then the original skill's",
               "\"use when\" description. Skill names in any file resolve to",
               "`skills/<name>/WORKFLOW.md`.\n"]
    dispatcher_body = None
    for sd in skill_dirs:
        fm, body = split_frontmatter((sd / "SKILL.md").read_text(encoding="utf-8"))
        if sd.name == DISPATCHER:
            dispatcher_body = body
            continue
        dest = stage / "skills" / sd.name
        if (sd / "references").is_dir():
            shutil.copytree(sd / "references", dest / "references")
        else:
            dest.mkdir(parents=True)
        for extra in sd.iterdir():
            if extra.is_file() and extra.name != "SKILL.md":
                shutil.copy2(extra, dest / extra.name)
        desc = fm.get("description", "").strip()
        header = (f"<!-- Bundled workflow: originally skills/{sd.name}/SKILL.md. "
                  f"`references/...` paths are relative to skills/{sd.name}/. -->\n\n")
        if desc:
            header += f"> **Use when:** {desc}\n\n"
        (dest / "WORKFLOW.md").write_text(header + body, encoding="utf-8")
        catalog.append(f"## `{sd.name}`\n\nWorkflow: `skills/{sd.name}/WORKFLOW.md`\n\n{desc}\n")

    if dispatcher_body is None:
        sys.exit(f"dispatcher skills/{DISPATCHER}/SKILL.md not found")
    (stage / "skills" / "INDEX.md").write_text("\n".join(catalog), encoding="utf-8")

    specialists = [n for n in names if n != DISPATCHER]
    body = PREAMBLE + rewrite_routing_rows(dispatcher_body, specialists)
    quoted = '"' + DESCRIPTION.replace("\\", "\\\\").replace('"', '\\"') + '"'
    skill_md = (f"---\nname: {BUNDLE_NAME}\ndescription: {quoted}\n"
                f"license: BUSL-1.1\n---\n\n{body}")
    (stage / "SKILL.md").write_text(skill_md, encoding="utf-8")

    # --- checks ---
    if len(DESCRIPTION) > 1024:
        errors.append(f"description is {len(DESCRIPTION)} chars (> 1024)")
    if re.search(r"anthropic|claude", BUNDLE_NAME):
        errors.append("bundle name uses a reserved word")
    body_lines = len(body.splitlines())
    if body_lines > 500:
        errors.append(f"SKILL.md body is {body_lines} lines (> 500)")
    nested = [p for p in stage.rglob("SKILL.md") if p != stage / "SKILL.md"]
    if nested:
        errors.append(f"nested SKILL.md files remain: {nested}")
    for ref, src in check_references(stage):
        errors.append(f"missing path {ref} (cited in {src})")

    zip_path = out_dir / f"{BUNDLE_NAME}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(stage.rglob("*")):
            if f.is_file():
                zf.write(f, f.relative_to(out_dir))

    n_files = sum(1 for f in stage.rglob("*") if f.is_file())
    print(f"bundle: {zip_path}")
    print(f"workflows: {len(specialists)} + dispatcher; files: {n_files}; "
          f"zip size: {zip_path.stat().st_size / 1024:.0f} KB; "
          f"description: {len(DESCRIPTION)} chars; SKILL.md body: {body_lines} lines")
    if errors:
        print("ERRORS:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print("checks: ok")


if __name__ == "__main__":
    main()
