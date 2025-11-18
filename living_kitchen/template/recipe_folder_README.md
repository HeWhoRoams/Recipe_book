# Recipe Folder README — Living Kitchen v5.0

## Required Files
Each dish folder must follow this structure:
```
recipes/<dish>/
  original.md
  baseline.md
  weeknight.md
  marriage.md
  vegetarian.md
  vegan.md
  dairyfree.md
  keto.md
.livingkitchen/<dish>/
  flavor_profile.md
  ontology_patch.md
  critic_report.md
  harmonizer_report.md
  audit_report.md
  memory_log.md
  variant_logs/
    weeknight.md
    marriage.md
    vegetarian.md
    vegan.md
    dairyfree.md
    keto.md
```
- No filenames contain version suffixes; versioning appears only in YAML frontmatter.

## Frontmatter Template
```
---
name: <file role>
version: <int>
timestamp: <ISO8601>
source_files:
  - <relative path>
---
```

## Recipe Requirements
1. Sections (in order): frontmatter, Overview, Ingredient Table/List, Mise en Place (if needed), Equipment (if needed), Procedure, Special Notes / Variant Log, `### Macro Estimate (per serving)`.
2. Every instruction step includes explicit quantities and units for all ingredients referenced.
3. Macro section lists Calories, Protein (g), Fat (g), Carbohydrates (g), Net carbs (g), Fiber (g), Sodium (mg), Serving size (g).
4. All macros must be derived from `living_kitchen/global_memory/global_macro_reference.json`.

## System Artifact Rules
- All critic/audit/harmonizer/memory reports, flavor profiles, ontology patches, and variant logs live under `.livingkitchen/<dish>/`.
- Reports also include YAML frontmatter with version/timestamp/source files.

## Elevation Mode
- Variant agents must record compliance decisions in their logs and in the human-facing recipe when `Baseline-Compliance: true`, adding sections `Compliance Reasoning` and `Elevation Enhancements`.

## Versioning
- `version_manifest.json` tracks hashes and versions; filenames remain static.
- Increment `version` inside frontmatter when a file is regenerated.
