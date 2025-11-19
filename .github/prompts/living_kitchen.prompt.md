# Living Kitchen Framework v5.0 — Master Prompt

## Mission
Operate the Living Kitchen multi-agent system so that each run produces clean, human-facing recipes in `recipes/<dish>/` while storing all system artifacts inside `.livingkitchen/<dish>/`. Every output must contain units-in-every-step, macro estimates derived from shared global memory, and YAML frontmatter metadata (version, ISO8601 timestamp, source_files). Variant agents must detect dietary compliance and switch to Elevation Mode when the baseline already satisfies their constraints.

## Directory Model
- `recipes/<dish>/` holds only: `original.md`, `baseline.md`, `weeknight.md`, `marriage.md`, `vegetarian.md`, `vegan.md`, `dairyfree.md`, `keto.md`. No suffixes.
- `.livingkitchen/<dish>/` holds system artifacts (`flavor_profile.md`, `ontology_patch.md`, `critic_report.md`, `harmonizer_report.md`, `audit_report.md`, `memory_log.md`, `variant_logs.md`, etc.). Filenames have no version suffix; versioning lives in frontmatter.
- When migrating legacy folders, move every `*_vX.md` or system artifact into `.livingkitchen/<dish>/` and rewrite filenames accordingly.

## Global Behaviors
1. **Frontmatter Metadata** — All generated Markdown files must begin with:
   ```yaml
   ---
   name: <file role>
   version: <int>
   timestamp: <ISO8601>
   source_files:
     - <paths>
   ---
   ```
2. **Units Requirement** — Every instruction step restates the exact measured quantity + unit for each ingredient used in that step.
3. **Macro Section** — Each recipe ends with `### Macro Estimate (per serving)` listing Calories, Protein (g), Fat (g), Carbohydrates (g), Net carbs (g), Fiber (g), Sodium (mg), Serving size (g). Values derived from `global_macro_reference.json`.
4. **Global Memory** — Before producing outputs, all agents load every file under `living_kitchen/global_memory/` plus the schema document. Memory Keeper applies deltas (±0.01–0.05) only after compliance passes.
5. **Version Tracking** — Version Manager updates manifest metadata, but filenames remain stable. Agents increment `version` in frontmatter when regenerating files.
6. **Variant Elevation Mode** — Weeknight, Marriage, Vegetarian, Vegan, Dairy-Free, Keto agents must first evaluate baseline compliance. If baseline already satisfies the diet, they produce an enhancement variant (Baseline-Compliance: true) instead of substitutions.

## Phase Pipeline
1. **Phase -1 – Change Detection**
   - Version Manager loads/creates `recipes/<dish>/version_manifest.json`.
   - Compute hash of truth-source file (`original.md` or orchestrator-selected baseline).
   - If manifest absent or hash differs → schedule full pipeline, increment versions in frontmatter.
   - If hash unchanged → orchestrator may run maintenance (e.g., compliance + memory) without bump.
2. **Phase 0 – Global Memory Load & Modeling**
   - Load global files, confirm schema compliance.
   - Update `.livingkitchen/<dish>/flavor_profile.md` and `ontology_patch.md` (no suffixes).
3. **Phase 1 – Chef↔Critic Loop**
   - Chef outputs `recipes/<dish>/baseline.md`. Critic writes `.livingkitchen/<dish>/critic_report.md`.
   - Iterate max three times or until improvement <5%.
4. **Phase 2 – Variant Generation**
   - Weeknight, Marriage, Vegetarian, Vegan, Dairy-Free, Keto produce recipes in `recipes/<dish>/`.
   - Each variant also writes a structured log to `.livingkitchen/<dish>/variant_logs/<variant>.md`.
5. **Phase 3 – Harmonizer**
   - Emits `.livingkitchen/<dish>/harmonizer_report.md`; validates section order, units, macros, elevation decisions.
6. **Phase 4 – Auditor**
   - Writes `.livingkitchen/<dish>/audit_report.md`. Computes flavor similarity, structural scores, macro completeness, and Elevation Mode compliance.
7. **Phase 5 – Memory Keeper**
   - Records `.livingkitchen/<dish>/memory_log.md` and prepares global deltas; updates global files post-compliance.
8. **Phase 6 – Compliance Agent**
   - Confirms human-facing files contain frontmatter, required sections, measurements, macro blocks. Failure halts run.
9. **Phase 7 – Manifest Update**
   - Version Manager refreshes `version_manifest.json` with new versions, timestamps, and size/hashes.
   - Orchestrator outputs `LIVINGKITCHEN RUN COMPLETE`.

## Variant Elevation Logic
- **Compliance Test Inputs**: baseline recipe, FlavorProfile, IngredientOntology, global substitution map, macro data.
- **Standard Mode**: baseline fails diet → perform substitutions, document map, ensure macros/FlavorProfile alignment.
- **Elevation Mode**: baseline passes diet → no substitutions; produce enhanced variant with sections:
  - `Baseline-Compliance: true`
  - `Compliance Reasoning`
  - `Elevation Enhancements`
  - Full recipe body with upgraded techniques and macros.
- Harmonizer/Auditor must confirm compliance detection accuracy and mention in reports.

## Failure Handling
- Missing frontmatter, section ordering, units, or macro block in any human-facing recipe triggers Compliance failure.
- Global memory writes blocked until compliance passes.
- Orchestrator stops immediately when Auditor/Harmonizer/Compliance detect issues; reports stored in `.livingkitchen/<dish>/`.
