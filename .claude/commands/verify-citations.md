---
description: Verify citations in a SKILL.md or reference file
argument-hint: [path]
allowed-tools: Read Grep Bash(jq:*) WebFetch
---
For file $1:
1. Extract every citation (IRC §, Treas. Reg., case cite, Rev. Rul.,
   PLR, Form, IRM, etc.).
2. For each, confirm the canonical URL in `shared/sources.json`
   resolves and that the cited text is present.
3. Flag any `[CITATION NEEDED — search: ...]` sentinels — these
   block phase tick-off unless intentional in template files.
4. State stub files at references/states/ use `TODO:` markers; do not
   flag those.
5. For each authority_type used in the file, confirm it appears in
   the enumeration in shared/citation-discipline.md (and in the
   authority_type enum in shared/output-schema.json).
6. Report a summary: ok, suspect, sentinel, unverifiable, taxonomy_drift.
