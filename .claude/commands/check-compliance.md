---
description: Verify every skill output template includes the SSTS / Circular 230 checklist
allowed-tools: Read Grep Glob
---
For every `skills/*/SKILL.md`, confirm the body includes:
- A reference to `shared/compliance.md`
- The five SSTS / Circular 230 checklist items (1.1, 2.3, 10.22,
  10.35, 10.37)
- The "Read before output" block linking the four core shared/ files
  (citation-discipline, authority-hierarchy, confidence-bands,
  compliance)
- For skills that touch recent Public Laws: a reference to
  shared/legislation-tracking.md
- The JSON sidecar emission step
- The negative-treatment-review residual-responsibility note for
  high-stakes positions
Report any skill that is missing items, with file path and line.
