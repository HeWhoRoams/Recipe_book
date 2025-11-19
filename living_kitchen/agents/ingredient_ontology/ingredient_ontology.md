# Agent: Ingredient Ontology

## Role
Defines canonical ingredients, sourcing, substitution logic, and cultural guidance for the Optimized Short Rib & Multi-Chile Chili.

## Inputs
- Dish concept ingredient inventory.

## Outputs
- Structured ontology table.

## Rules
1. Follow template column order.
2. Substitutions limited to two entries per ingredient.
3. Provide deterministic IDs.

## Workflow
1. Assign IDs sequentially.
2. Populate sourcing data and substitutions.
3. Record dietary flags and notes.

## Acceptance Criteria
- All mandatory ingredients represented.
- Substitution confidence 0–100 integers.
- Notes specify tags and cultural integrity.

## Failure Conditions
- Missing fields or duplicate IDs.
- Confidence outside range.

## Determinism Requirements
- IDs increment by one.
- Notes concise.

---

## Ontology Table
| Canonical ID | Name | Category | Sourcing Tier | Region Note | Primary Substitution | Sub Confidence | Secondary Substitution | Sub Confidence | Dietary Flags (veg/vegan/dairyfree/keto) | Notes |
|--------------|------|----------|---------------|-------------|---------------------|----------------|------------------------|----------------|------------------------------------------|-------|
| ING-001 | Short ribs | Protein | premium | West Texas pasture-raised suppliers | Vegetarian/Vegan: smoked king oyster mushroom burnt ends | 68 | Keto/Dairyfree: beef cheek burnt ends | 92 | no/no/yes/yes | Tags: protein, meat, umami. Substitutions—Veg: smoked king oyster; Vegan: jackfruit burnt ends; Dairyfree: cut is naturally dairyfree; Keto: beef cheek. Cultural integrity: honors Tex-Mex meat dominance. |
| ING-002 | Kidney beans | Legume | standard | Borderland dry bean cooperatives | Vegetarian/Vegan: pinto beans | 94 | Keto: black soy beans | 60 | yes/yes/yes/no | Tags: legume, starch, body. Dairyfree substitute same as default. Cultural integrity: staple bean for Tex-Mex chili with inclusive swap guidance. |
| ING-003 | Ancho chile | Dried chile | seasonal | Puebla growers shipped via El Paso markets | Pasilla negro | 85 | Mulato chile | 82 | yes/yes/yes/yes | Tags: capsaicin, fruity, smoky. Substitutions—Veg/Vegan: dried pasilla; Dairyfree: inherent; Keto: inherent. Cultural integrity: anchors Mexican sweetness. |
| ING-004 | Pasilla/Mulato chile | Dried chile | seasonal | Central Mexican import stalls | Ancho chile | 84 | Guajillo chile | 78 | yes/yes/yes/yes | Tags: capsaicin, bitter-sweet. Substitutions maintain borderland chile mix identity. |
| ING-005 | New Mexico chile | Dried chile | seasonal | Hatch valley brokers | Guajillo chile | 80 | California chile | 76 | yes/yes/yes/yes | Tags: capsaicin, earthy. Cultural integrity: keeps Southwest terroir. |
| ING-006 | Cascabel/Arbol/Pequin blend | Dried chile blend | seasonal | Northern Mexico spice traders | Chile de árbol only | 74 | Pequín only | 70 | yes/yes/yes/yes | Tags: capsaicin, high heat. Cultural integrity: honors layered heat tradition. |
| ING-007 | Cumin seeds | Spice | standard | Chihuahua spice distributors | Toasted caraway seeds | 65 | Ground coriander-cumin mix | 72 | yes/yes/yes/yes | Tags: spice, earthy. Substitutions respect Tex-Mex spice core. |
| ING-008 | Coriander seeds | Spice | standard | Sonoran spice markets | Toasted cilantro seed powder | 81 | Mexican oregano seed mix | 60 | yes/yes/yes/yes | Tags: citrus spice. Cultural integrity: brightens chile base. |
| ING-009 | Cloves | Spice | standard | Veracruz spice trade | Allspice berries | 70 | Star anise shard | 58 | yes/yes/yes/yes | Tags: warm spice, aromatic. Keeps mole-style depth. |
| ING-010 | Star anise | Spice | premium | Pacific trade distributors via Houston | Chinese five-spice pinch | 62 | Fennel seed | 55 | yes/yes/yes/yes | Tags: licorice spice. Cultural note: use sparingly to mimic border mole inflection. |
| ING-011 | Tomato paste | Pantry concentrate | standard | California processing plants | Sun-dried tomato puree | 77 | Roasted red pepper puree | 65 | yes/yes/yes/yes | Tags: umami, acid, body. Maintains Tex-Mex tomato backbone. |
| ING-012 | Unsweetened chocolate | Pantry | premium | Oaxacan chocolate cooperatives | Mexican drinking chocolate tablet (sugar adjusted) | 73 | Cocoa nib + coffee oil paste | 69 | yes/yes/yes/yes | Tags: bitter, Maillard booster. Cultural integrity: nod to mole tradition. |
| ING-013 | Finely ground coffee | Pantry | standard | Chiapas/Veracruz roasters | Espresso powder | 88 | Chicory-coffee blend | 74 | yes/yes/yes/yes | Tags: bitter, roast depth. Cultural note: modern Tex-Mex Maillard amplifier. |
| ING-014 | Anchovy fillets | Umami booster | premium | Mediterranean cured supply via Gulf ports | Vegetarian: white miso paste | 75 | Vegan: kombu-soy reduction | 72 | no/no/yes/yes | Tags: umami, seafood. Dairyfree default. Cultural integrity: stealth umami reminiscent of pitmaster tricks. |
| ING-015 | Soy sauce | Condiment | standard | Japanese-Tex border pantry staples | Tamari (gluten-free) | 85 | Coconut aminos | 70 | yes/yes/yes/yes | Tags: saline umami. Cultural note: respects modern Tex-Mex pantry mashup. |
| ING-016 | Marmite | Condiment | premium | British import shelves in Austin | Vegemite | 80 | Nutritional yeast paste | 68 | yes/yes/yes/yes | Tags: umami, yeast. Cultural integrity: used sparingly to boost savoriness while acknowledging fusion boundaries. |
| ING-017 | Onions | Aromatic | standard | South Texas sweet onion farms | Leeks (veg/vegan) | 86 | Keto: charred fennel bulb | 62 | yes/yes/yes/no | Tags: aromatic, allium. Cultural integrity: base of Tex-Mex sofrito. |
| ING-018 | Garlic | Aromatic | standard | California garlic network | Asafoetida pinch (veg/vegan) | 60 | Scallion whites | 72 | yes/yes/yes/yes | Tags: aromatic, pungent. Cultural note: essential for chili paste. |
| ING-019 | Chicken broth | Liquid | standard | Texas Hill Country stock producers | Vegetarian: roasted vegetable stock | 78 | Vegan/Dairyfree: kombu-mushroom broth | 74 | no/no/no/yes | Tags: liquid, umami. Keto-friendly if unsweetened. Cultural integrity: keeps border stew mouthfeel. |
| ING-020 | Cider vinegar | Acid | standard | Midwestern apple processors distributed south | Red wine vinegar | 70 | Tamarind vinegar | 68 | yes/yes/yes/yes | Tags: acid, brightener. Cultural note: balances chile richness. |
| ING-021 | Brown sugar | Sweetener | standard | Louisiana cane refineries | Piloncillo cone | 90 | Keto: allulose-brown blend | 58 | yes/yes/yes/no | Tags: sweetener, caramel. Cultural integrity: use sparingly to avoid sweet chili drift. |
| ING-022 | Vegetable oil | Fat | standard | Gulf coast neutral oil producers | Beef tallow (keto/dairyfree) | 82 | Avocado oil | 88 | yes/yes/yes/yes | Tags: fat, searing medium. Cultural note: supports triple sear. |
| ING-023 | Crushed tomatoes | Pantry | standard | California-Sonora processors | Fire-roasted diced tomatoes | 84 | Charred tomatillo puree | 66 | yes/yes/yes/yes | Tags: acid, body. Cultural integrity: respects Tex-Mex tomato-chile ratio. |
| ING-024 | Bay leaves | Herb | standard | Mediterranean herb merchants | Mexican oregano sprig | 67 | Avocado leaves | 72 | yes/yes/yes/yes | Tags: herbaceous, aromatic. Cultural note: adds Southwest herbal thread. |
| ING-025 | Oregano (Mexican) | Herb | standard | Oaxaca herb co-ops | Marjoram | 60 | Epazote (caution) | 65 | yes/yes/yes/yes | Tags: herb, aromatic. Cultural integrity: essential Mexican herb. |
| ING-026 | Fresh chiles (Thai bird/Jalapeño) | Fresh chile | seasonal | Texas farmers markets | Serrano | 83 | Fresno chile | 78 | yes/yes/yes/yes | Tags: capsaicin, freshness. Cultural note: adds fresh heat sparkle. |
| ING-027 | Vodka/Bourbon | Deglazing spirit | premium | Kentucky barrel partners | Non-alcoholic: charred apple cider | 64 | Tequila reposado splash | 70 | no/no/yes/yes | Tags: alcohol, solvent, Maillard booster. Cultural integrity: bourbon nods to Texas smokehouse traditions. |
| ING-028 | Hot sauce | Condiment | standard | Regional Texas ferments | Chili vinegar | 76 | Fermented habanero mash | 82 | yes/yes/yes/yes | Tags: acid, heat finisher. Cultural note: finishers must align with border-style ferments. |
