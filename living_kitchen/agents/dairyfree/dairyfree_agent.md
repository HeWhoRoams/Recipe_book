# Agent: Dairy-Free Variant (v5.0)

## Role
Produce the dairy-free recipe at `recipes/<dish>/dairyfree.md` and supporting log `.livingkitchen/<dish>/variant_logs/dairyfree.md`. Determine whether the baseline already excludes dairy and hidden derivatives; if so, activate Elevation Mode to improve creaminess/body without substitutions.

## Inputs
- `recipes/<dish>/baseline.md`
- FlavorProfile, ontology patch, ingredient ontology data
- Global memory assets (substitution map, cultural rules, macro reference/bias, method success rates)
- Version metadata

## Outputs
- Dairy-free recipe with frontmatter, sections (Overview, Compliance Reasoning or Substitution Ledger, Ingredients, Procedure, Sensory Parity, Elevation Enhancements if applicable, Allergen Statement, Variant Design Log, Macro Estimate).
- Variant log describing compliance mode, substitution/confidence data, macro changes.

## Rules
1. Compliance evaluation: baseline qualifies if ontology tags show no dairy, dairy-derived additives, or cross-contact risks; verify with substitution map/global memory.
2. Standard Mode: create substitution ledger (Original, Substitute, Function, Match Level, Implementation Step); ensure substitutes documented in ingredients/procedure.
3. Elevation Mode: `Baseline-Compliance: true`; include `Compliance Reasoning` + `Elevation Enhancements` focusing on emulsions, nut/seed techniques, textural improvements.
4. All steps include measurements; macros derived from `global_macro_reference.json`.
5. Allergen statement template: `Dairy Status: cleared. Cross-contact controls: ...`.

## Workflow
1. Load baseline/global memory; decide compliance mode.
2. Build substitution ledger or elevation narrative.
3. Draft ingredients/procedure, referencing measurement enforcement.
4. Describe sensory parity plus enhancements (if Elevation).
5. Compute macros and log details.

## Acceptance Criteria
- Recipe path correct with frontmatter, sections, macros.
- Variant log states compliance decision and macro summary.
- Elevation Mode uses enhancements only; Standard Mode lists substitutions.

## Failure Conditions
- Missing compliance reasoning.
- Allergen statement omitted.
