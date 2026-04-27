---
description: Add an eval case to a skill's eval JSON
argument-hint: [skill-name] [case-name]
allowed-tools: Read Edit Write Bash(jq:*) Glob
---
Append an eval case named "$2" to `evals/<family>/$1.json`. If the
file does not exist, create it with the schema:
{ "skill_name": "$1", "evals": [ ... ] }
Each eval must have: id, prompt, expected_output, expectations[].
Keep prompts realistic — actual phrasings a CPA would use.
Validate JSON parses: `jq . evals/<family>/$1.json`.
