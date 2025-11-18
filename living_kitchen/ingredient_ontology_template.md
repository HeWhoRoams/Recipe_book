# Agent: Ingredient Ontology Template

## Role
Defines the canonical ingredient taxonomy, substitution pathways, sourcing tiers, and confidence metrics required by Living Kitchen agents.

## Inputs
- Ingredient research notes, sourcing data, and substitution experiments.

## Outputs
- Completed ontology table capturing canonical IDs, categories, sourcing, substitutions, and confidence scores.

## Rules
1. Every ingredient entry must include a unique canonical ID `ING-###`.
2. Confidence scores expressed 0.00–1.00 with two decimals.
3. Substitutions list max two options with justification.

## Workflow
1. Assign canonical IDs and base categories.
2. Document sourcing tier (standard, premium, seasonal) with region notes.
3. Determine substitution options and associated confidence.
4. Record dietary flags (vegan, vegetarian, dairy-free, keto suitability).

## Acceptance Criteria
- Template completed with no blank mandatory fields.
- Substitution justifications concise (≤12 words).
- Dietary flags use `yes/no`.

## Failure Conditions
- Duplicate IDs.
- Confidence outside range.
- Missing substitution reasoning.

## Determinism Requirements
- Maintain column order exactly as provided.
- IDs increment sequentially.
- No narrative text beyond table cells.

---

## Ontology Table
| Canonical ID | Name | Category | Sourcing Tier | Region Note | Primary Substitution | Sub Confidence | Secondary Substitution | Sub Confidence | Dietary Flags (veg/vegan/dairyfree/keto) | Notes |
|--------------|------|----------|---------------|-------------|---------------------|----------------|------------------------|----------------|------------------------------------------|-------|
