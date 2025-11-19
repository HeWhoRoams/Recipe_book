# Agent: Keto Variant (v5.0)

## Role
Create the ketogenic-compliant recipe at `recipes/<dish>/keto.md` and log `.livingkitchen/<dish>/variant_logs/keto.md`. Detect whether the baseline already satisfies keto rules (net carbs ≤8 g, ≥70% calories from fat, dairy-free status per baseline) and apply Elevation Mode if compliant.

## Inputs
- `recipes/<dish>/baseline.md`
- FlavorProfile and ontology patch
- Global memory assets (substitution map, ingredient confidences, macro reference/bias, method success rates, electrolyte guidelines)
- Version metadata

## Outputs
- Keto recipe with sections: frontmatter, Overview, Macro Table, Compliance Reasoning or Substitution Log, Ingredients, Procedure, Electrolyte Guidance, Elevation Enhancements (if applicable), Variant Design Log, Macro Estimate.
- Variant log detailing compliance decision, macro calculations, electrolyte plan, substitution confidences.

## Rules
1. Compliance evaluation: calculate macros from baseline using `global_macro_reference.json`; verify net carbs ≤8 g, fat ≥70% calories, carbs within macro bias; confirm ingredient ontology lacks high-carb components.
2. Standard Mode (baseline fails):
   - Provide substitution log referencing baseline ingredient IDs → keto substitutes, with reasons/confidence.
   - Update ingredient list/procedure accordingly.
3. Elevation Mode (baseline compliant):
   - Set `Baseline-Compliance: true`.
   - Include `Compliance Reasoning` and `Elevation Enhancements` describing fat-stabilization methods, fasting-friendly service, electrolyte optimization—all without substitutions.
4. Macro table must show grams, calories, percentages for fat/protein/net carbs.
5. Electrolyte guidance includes sodium/potassium/magnesium amounts per serving.
6. All instructions contain explicit measurements; macros derived from `global_macro_reference.json`.

## Workflow
1. Load baseline and global memory; run compliance calculation.
2. Depending on mode, create substitution log or elevation narrative.
3. Draft ingredient list and procedure with measurement enforcement.
4. Compute macro table + final macro estimate; log thresholds.
5. Document electrolyte guidance referencing global data.
6. Save recipe/log with frontmatter metadata.

## Acceptance Criteria
- Recipe stored at `recipes/<dish>/keto.md` with required sections, macros, compliance reasoning/elevation info.
- Variant log states mode and macro math.
- Elevation Mode avoids substitutions.

## Failure Conditions
- Macro table or electrolyte guidance missing.
- Compliance check omitted or incorrect.
