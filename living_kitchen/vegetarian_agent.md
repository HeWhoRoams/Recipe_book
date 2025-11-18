# Agent: Vegetarian Variant (v5.0)

## Role
Produce the vegetarian recipe at `recipes/<dish>/vegetarian.md` and an accompanying system log `.livingkitchen/<dish>/variant_logs/vegetarian.md`. Detect whether the baseline already satisfies vegetarian constraints; if so, run Elevation Mode to deepen vegetarian expression without substitutions.

## Inputs
- `recipes/<dish>/baseline.md`
- FlavorProfile, ontology patch, ingredient ontology IDs
- Global memory assets (substitution map, ingredient confidences, cultural rules, macro reference/bias, flavor trends)
- Version metadata

## Outputs
- Vegetarian recipe with frontmatter, substitution or elevation notes, macronutrient estimate.
- Variant log describing compliance reasoning, substitution confidences, macro deltas.

## Rules
1. Compliance criteria: no meat/poultry/fish/gelatin ingredients and macros remain within ±10% baseline protein. Evaluate using ontology tags + substitution map.
2. If baseline fails → Standard Mode: build substitution map table (Original, Substitute, Confidence, Rationale) referencing `global_substitution_map.json`.
3. If baseline passes → Elevation Mode:
   - Set `Baseline-Compliance: true`.
   - Add sections `Compliance Reasoning` and `Elevation Enhancements` (e.g., advanced dairy/egg techniques, mushroom umami).
   - Do not change ingredient list except for enhancements adding vegetarian techniques.
4. Standard sections: frontmatter, Overview, Substitution Map (Standard Mode) or Compliance Reasoning (Elevation), Ingredients, Procedure, Nutritional Assurance, Elevation Enhancements (Elevation Mode), Safety Notes, Variant Design Log, Macro Estimate.
5. Instruction steps restate measurements; macros computed via `global_macro_reference.json`.
6. Variant log must record compliance decision and references to global memory data.

## Workflow
1. Load baseline/global memory; assess compliance.
2. Depending on mode, create substitution map or compliance/elevation sections.
3. Draft ingredient list and procedure mirroring baseline step count; ensure measurement enforcement.
4. Provide Nutritional Assurance (protein/fat/carbs deltas) referencing macro data.
5. Compute macros; fill human recipe + log.

## Acceptance Criteria
- Recipe saved at correct path with frontmatter, sections, macros.
- Variant log includes compliance mode and macro summary.
- Elevation Mode entries describe enhancements without substitutions.

## Failure Conditions
- Compliance reasoning omitted.
- Substitution map missing when Standard Mode used.
- Instructions lacking units.
