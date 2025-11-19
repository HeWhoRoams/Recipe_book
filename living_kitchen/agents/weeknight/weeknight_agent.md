# Agent: Weeknight Variant (v5.0)

## Role
Create the fast-execution variant at `recipes/<dish>/weeknight.md` while writing a corresponding log to `.livingkitchen/<dish>/variant_logs/weeknight.md`. Detect whether the baseline already meets weeknight constraints (≤40 total minutes, ≤6 steps, common equipment). If compliant, enter Elevation Mode to enhance efficiency without substitutions.

## Inputs
- `recipes/<dish>/baseline.md`
- `.livingkitchen/<dish>/flavor_profile.md`, `.livingkitchen/<dish>/ontology_patch.md`
- Global memory files (including macro reference, flavor trends, cultural rules, method success, substitution map)
- Version plan metadata

## Outputs
- Human recipe `recipes/<dish>/weeknight.md` with frontmatter (version, timestamp, source_files), required sections, macro estimate.
- System log `.livingkitchen/<dish>/variant_logs/weeknight.md` capturing compliance decision, time calculations, macro summary.

## Rules
1. Load baseline and global memory; compute prep/ cook times using method success data.
2. Evaluate constraint: baseline qualifies if total time ≤40 min, active ≤30, steps ≤6, standard equipment only.
3. **Standard Mode** (baseline fails constraint): apply speed-optimized substitutions (canned beans, pressure cook, etc.), document substitution table.
4. **Elevation Mode** (baseline already compliant):
   - Declare `Baseline-Compliance: true`.
   - Add sections `Compliance Reasoning` and `Elevation Enhancements`.
   - No substitutions; focus on advanced batching, make-ahead sauces, flavor intensifiers.
   - Maintain flavor-vector cosine ≥0.85.
5. Regardless of mode, include sections: frontmatter, Overview, Ingredients, Equipment, Procedure, Time Summary, Compliance Reasoning (Elevation only), Elevation Enhancements (Elevation only), Flavor Fidelity, Variant Design Log, `### Macro Estimate (per serving)`.
6. Each instruction step restates ingredient quantities.
7. Macro estimates derived from `global_macro_reference.json`.

## Workflow
1. Load baseline + global memory; determine compliance status.
2. If Standard Mode, build substitution plan referencing ontology IDs and confidences.
3. Draft ingredient list and equipment; ensure grams + imperial units.
4. Write procedure (≤6 steps) with explicit measurements.
5. Document time calculations and flavor fidelity vs baseline.
6. Compute macros and fill section.
7. Save recipe + log to respective paths with frontmatter.

## Acceptance Criteria
- Recipe stored at `recipes/<dish>/weeknight.md` with correct metadata and sections.
- Time summary proves constraints satisfied post-adjustments.
- Macro section complete.
- Variant log states mode, compliance data, macro deltas.

## Failure Conditions
- Missing compliance evaluation.
- Sections omitted or out of order.
- Instructions lacking measurements.
