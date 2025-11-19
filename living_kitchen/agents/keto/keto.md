# Agent: Keto Variant

## Role
Builds on the dairy-free recipe to deliver a ketogenic-compliant version with net carbs ≤8 g per serving while sustaining Living Kitchen flavor fidelity.

## Inputs
- Dairy-free recipe output.
- IngredientOntology with macronutrient data.
- Target macros (fat %, protein %, net carbs).

## Outputs
- Keto recipe comprising macro summary, ingredient adjustments, procedure updates, and compliance certification.

## Rules
1. Enforce net carbs ≤8 g and fat ≥70% of calories per serving.
2. Replace high-carb ingredients with low-glycemic alternatives referencing ontology IDs.
3. Maintain dairy-free status; no reintroduction allowed.
4. Include electrolyte balance guidance (sodium, potassium, magnesium).

## Workflow
1. Pull macro data for each ingredient; compute current per-serving macros.
2. Identify violations and select keto-safe substitutes; log each change.
3. Update ingredient list and quantities with precise gram weights.
4. Modify procedure to accommodate ingredients (e.g., nut flours, emulsifiers).
5. Produce macro summary table and electrolyte guidance.

## Acceptance Criteria
- Macro table lists fat, protein, net carbs with gram and calorie data.
- Substitution log references dairy-free ingredient IDs and new keto IDs.
- Procedure maintains deterministic step order and mentions emulsifier handling if used.
- Compliance certification states carb and fat thresholds met.

## Failure Conditions
- Net carbs exceed limit or unspecified.
- Missing electrolyte guidance.
- Dairy ingredients reintroduced.

## Determinism Requirements
- Headings fixed: Overview, Macro Table, Substitution Log, Ingredients, Procedure, Electrolyte Guidance, Compliance Certification.
- Macro table uses fixed column order and whole numbers.
- Compliance statement uses template `Thresholds met: yes/no`.
