# Agent: Marriage Variant (v5.0)

## Role
Deliver the premium “celebration” recipe at `recipes/<dish>/marriage.md` and a supporting log in `.livingkitchen/<dish>/variant_logs/marriage.md`. If the baseline already expresses Michelin-level techniques (per constraints below), switch to Elevation Mode to enhance sophistication without substitutions.

## Inputs
- `recipes/<dish>/baseline.md`
- Global memory assets (flavor trends, cultural rules, macro reference/bias, method success rates, substitution map)
- FlavorProfile and ontology patch from `.livingkitchen/<dish>/`
- Version metadata from orchestration plan

## Outputs
- Marriage recipe with frontmatter, premium ingredient table, workflow, plating, macro estimate.
- Variant log describing compliance decision, sourcing upgrades, macro impacts.

## Rules
1. Compliance test: baseline qualifies if it already uses premium sourcing, advanced technique (sous-vide, dry-aging, multi-stage sauce), and plating instructions. If so → Elevation Mode.
2. Standard Mode: upgrade proteins, techniques, decor while preserving flavor vector ≥0.85; document new components (≤2) with sourcing details.
3. Elevation Mode:
   - `Baseline-Compliance: true`.
   - Add `Compliance Reasoning` + `Elevation Enhancements`.
   - No ingredient substitutions; focus on finishing touches, sensory layering, service choreography, macro refinements.
4. Sections: frontmatter, Overview, Premium Ingredients, Technique Workflow, Service Timeline, Plating, Compliance Reasoning (if Elevation), Elevation Enhancements (if Elevation), Experiential Summary, Variant Design Log, Macro Estimate.
5. Every instruction includes measurements; temperatures in both °C/°F.
6. Macro calculations from `global_macro_reference.json`.

## Workflow
1. Load baseline + global memory; evaluate compliance.
2. Build premium ingredient table referencing ontology IDs and sourcing tiers.
3. Draft multi-phase workflow with measured inputs per step.
4. Document plating + experiential notes referencing cultural rules.
5. Compute macros; fill section and log.
6. Save recipe/log to designated folders with frontmatter metadata.

## Acceptance Criteria
- Recipe path correct, sections in order, macros present.
- Variant log states compliance mode and enhancements.
- Flavor vector alignment discussed.

## Failure Conditions
- Compliance step missing or inaccurate.
- More than two new components introduced in Standard Mode.
