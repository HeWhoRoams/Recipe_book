# Agent: Harmonizer (v5.0)

## Role
Normalize all human-facing recipes (`baseline.md`, `weeknight.md`, `marriage.md`, `vegetarian.md`, `vegan.md`, `dairyfree.md`, `keto.md`) and verify Elevation Mode decisions. Produce `.livingkitchen/<dish>/harmonizer_report.md`.

## Inputs
- Recipes from `recipes/<dish>/`
- Variant logs from `.livingkitchen/<dish>/variant_logs/*.md`
- Global memory (macro reference/bias, cultural rules, flavor trends)

## Outputs
- `harmonizer_report.md` with frontmatter and sections: Overview, Structure Check, Elevation Compliance, Normalization Dictionary, Macro & Flavor Alignment, Deviations, Recommendations.

## Rules
1. Confirm every recipe includes frontmatter, required sections, unitized instructions, macro block.
2. Compute conformity percentage = matched sections ÷ total sections (expressed with two decimals). Must be ≥95% or report failure.
3. Validate Elevation Mode declarations: ensure compliance reasoning present when `Baseline-Compliance: true` and no substitutions applied; cross-check variant logs.
4. Verify macro values using `global_macro_reference.json`; note deviations >10%.
5. Build normalization dictionary mapping inconsistent terms to standard ones; sort alphabetically.
6. Store report at `.livingkitchen/<dish>/harmonizer_report.md`.

## Workflow
1. Load all recipes/logs and global memory.
2. Check section order + measurement compliance.
3. Evaluate Elevation Mode vs Standard Mode decisions.
4. Compute macro alignment and flavor vector cosine (≥0.85).
5. Record deviations with references (file + section).

## Acceptance Criteria
- Report documents conformity percentage, macro/ flavor alignment, and Elevation Mode validation.
- Deviations list includes issue code and corrective action.

## Failure Conditions
- Missing mention of Elevation Mode validation.
- Conformity <95% without failure status.
