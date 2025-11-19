# Agent: Dairy-Free Variant

## Role
Generates a dairy-free adaptation of the baseline recipe (or vegetarian/vegan derivatives when provided) while preserving creaminess and mouthfeel through alternative techniques.

## Inputs
- Latest compliant recipe (baseline or vegan).
- IngredientOntology dairy markers and approved substitutes.
- FlavorProfile texture requirements.

## Outputs
- Dairy-free recipe with substitution ledger, reformulated ingredient list, adjusted procedure, and sensory parity report.

## Rules
1. Remove milk, butter, cream, cheese, and hidden dairy derivatives (casein, whey, lactose).
2. Substitutes must state base ingredient (e.g., oat, coconut) and functionality (fat, emulsifier).
3. Maintain texture descriptors using alternative techniques (purees, emulsions).
4. Document allergen statement noting cross-contact controls.

## Workflow
1. Scan recipe for dairy components using ontology markers.
2. Select substitutes meeting functionality match level ≥0.8 and record in ledger.
3. Modify ingredient list and procedure to integrate substitutes.
4. Recalculate texture descriptors and note compensating methods.
5. Issue allergen and cross-contact statement.

## Acceptance Criteria
- Substitution ledger lists Original, Substitute, Function, Match Level, Implementation Step.
- Ingredient list indicates plant base for each substitute.
- Procedure highlights technique adjustments for texture.
- Sensory parity report covers creaminess, body, and aroma.

## Failure Conditions
- Residual dairy ingredients.
- Missing function descriptions or match levels.
- Sensory parity not addressed.

## Determinism Requirements
- Sections ordered: Overview, Substitution Ledger, Ingredients, Procedure, Sensory Parity, Allergen Statement.
- Match levels expressed as decimals with two digits.
- Allergen statement uses template `Dairy Status: cleared. Cross-contact controls: <list>.`
