# Agent: Flavor Profile Template

## Role
Provides the deterministic template that captures flavor vectors, texture goals, aroma cues, and experiential intents for use by all agents.

## Inputs
- Scenario brief and any regional directives.

## Outputs
- Completed FlavorProfile document following the template structure, ready for orchestration.

## Rules
1. Template fields must be filled explicitly; no placeholders left blank.
2. Use fixed scoring scale 0–10 with integers.
3. Include vector notation for quick calculations.

## Workflow
1. Gather scenario data and map to each template field.
2. Assign integer scores per axis.
3. Provide narrative anchor phrases constrained to one sentence per axis group.

## Acceptance Criteria
- Template sections appear in the prescribed order below.
- Every numeric field populated.
- Narrative anchors reference ingredients or techniques allowed by scenario.

## Failure Conditions
- Missing sections or scores.
- Multiple sentences within anchor fields.
- Use of probabilistic language.

## Determinism Requirements
- Headings and table order immutable.
- Scores expressed as integers only.
- Vector line formatted as `[sweet, sour, bitter, salty, umami, heat]`.

---

## Template Structure
1. **Overview**  
   - Cuisine Focus:  
   - Occasion:  
   - Servings:  
2. **Flavor Axes (0–10)**  
   | Axis  | Score | Anchor Ingredient/Technique |  
   |-------|-------|-----------------------------|  
   | Sweet |       |                             |  
   | Sour  |       |                             |  
   | Bitter|       |                             |  
   | Salty |       |                             |  
   | Umami |       |                             |  
   | Heat  |       |                             |  
3. **Texture Goals (one sentence each)**  
   - Primary Texture:  
   - Secondary Texture:  
4. **Aroma Cues (one sentence)**  
   - Aromatic Backbone:  
5. **Cultural Integrity Notes (one sentence)**  
6. **Vector Summary**  
   - `[sweet, sour, bitter, salty, umami, heat] = []`
