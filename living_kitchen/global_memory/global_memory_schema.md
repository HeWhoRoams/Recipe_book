# Global Memory Schemas — Living Kitchen Framework

version: 1
timestamp: T0

## Merge Rules
- Memory Keeper is the only agent permitted to write global memory files.
- Adjustments must stay within ±0.01–0.05 per run for confidence/ratio fields.
- Never delete keys; extend by adding new entries.
- All timestamps recorded as ISO8601 strings (UTC).
- When merging, load existing JSON, apply deltas, then reserialize with stable key ordering.

## Schemas

### 1. `global_ingredient_confidence.json`
```json
{
  "ingredients": {
    "<ING_ID_or_name>": {
      "base_confidence": 0.0,
      "substitutions": {
        "<sub_name>": {
          "confidence": 0.0,
          "last_updated": "YYYY-MM-DDTHH:MM:SSZ",
          "evidence_count": 0
        }
      }
    }
  }
}
```
- Purpose: track canonical ingredient reliability and substitution performance.

### 2. `global_substitution_map.json`
```json
{
  "<ingredient>": {
    "vegetarian": ["sub1", "sub2"],
    "vegan": ["subA", "subB"],
    "dairyfree": ["subX"],
    "keto": ["subY"],
    "notes": "string"
  }
}
```
- Purpose: deterministic lookup of candidate substitutes per dietary axis.

### 3. `global_cultural_rules.md`
- Markdown document partitioned by cuisine headings (e.g., `## Tex-Mex Chili`).
- Each section lists authenticity notes and “Hard No” rules (prohibited substitutions or techniques).
- Append-only; mention source feedback for new rules.

### 4. `global_flavor_trends.json`
```json
{
  "flavor_axes": {
    "sweet": { "avg": 4.3, "trend": "down" },
    "sour": { "avg": 5.1, "trend": "up" },
    "bitter": { "avg": 3.0, "trend": "flat" },
    "salty": { "avg": 5.5, "trend": "flat" },
    "umami": { "avg": 7.8, "trend": "up" },
    "heat": { "avg": 6.2, "trend": "up" }
  }
}
```
- Purpose: inform FlavorProfile adjustments.

### 5. `global_method_success_rates.json`
```json
{
  "methods": {
    "pressure_cook": { "success_score": 0.93, "sample_size": 24 },
    "sous_vide": { "success_score": 0.88, "sample_size": 15 },
    "triple_sear": { "success_score": 0.96, "sample_size": 30 }
  }
}
```
- Purpose: gauge reliability of techniques and adjust warnings/timings.

### 6. `global_macro_bias.json`
```json
{
  "baseline": { "target_fat_pct": 0.45, "target_protein_pct": 0.30, "target_carb_pct": 0.25 },
  "keto": { "target_fat_pct": 0.70, "max_net_carbs": 8 },
  "weeknight": { "target_cal_per_serving": 650 },
  "vegetarian": { "target_protein_pct": 0.25 },
  "vegan": { "target_protein_pct": 0.23 },
  "marriage": { "target_cal_per_serving": 520 },
  "dairyfree": { "target_fat_pct": 0.40 }
}
```
- Purpose: establish macro expectations per variant category.
