# Agent: Flavor Profile

## Role
Provides the deterministic flavor, texture, aroma, and cultural targets for “Optimized Short Rib & Multi-Chile Chili.”

## Inputs
- Dish concept brief.

## Outputs
- Completed FlavorProfile document for orchestration use.

## Rules
1. All numeric scores are integers 0–10.
2. Anchor statements limited to one sentence.
3. Cultural note references Tex-Mex/Mexican integrity.

## Workflow
1. Interpret dish concept and flavor cues.
2. Assign scores aligned with short rib richness, multi-chile depth, Maillard focus, and balanced acidity.
3. Record vector summary.

## Acceptance Criteria
- Every field filled deterministically.
- Narrative anchors reference actual ingredients or techniques.

## Failure Conditions
- Blank fields or multi-sentence anchors.
- Scores misaligned with dish intent.

## Determinism Requirements
- Maintain template order.
- Vector summary formatting `[sweet, sour, bitter, salty, umami, heat] = []`.

---

## Template Structure
1. **Overview**  
   - Cuisine Focus: Tex-Mex stew with Northern Mexican influences  
   - Occasion: Cold-weather centerpiece or competitive chili cook-off  
   - Servings: 8  
2. **Flavor Axes (0–10)**  
   | Axis  | Score | Anchor Ingredient/Technique |  
   |-------|-------|-----------------------------|  
   | Sweet | 4     | Dark brown sugar bloom to round chile heat |  
   | Sour  | 5     | Fire-roasted tomato plus apple cider vinegar finish |  
   | Bitter| 3     | Espresso-ground coffee and toasted cacao nib nuance |  
   | Salty | 6     | Reduced soy sauce and kosher salt layering |  
   | Umami | 9     | Anchovy paste, marmite, and triple-seared short rib fond |  
   | Heat  | 7     | Cascabel, arbol, and pequin blend for climbing heat |  
3. **Texture Goals (one sentence each)**  
   - Primary Texture: Spoon-coating gravy with tender shred-on-demand rib strands.  
   - Secondary Texture: Suspended creamy beans with occasional chile flecks for contrast.  
4. **Aroma Cues (one sentence)**  
   - Aromatic Backbone: Smoldering dried chile perfume layered with allium-sautéed fat and toasted spices.  
5. **Cultural Integrity Notes (one sentence)**  
   - Maintain Tex-Mex authenticity through dried chile trinity, bean inclusion, and restrained sweeteners respecting borderland chili traditions.  
6. **Vector Summary**  
   - `[sweet, sour, bitter, salty, umami, heat] = [4,5,3,6,9,7]`
