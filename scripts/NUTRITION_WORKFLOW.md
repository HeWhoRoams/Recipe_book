Ingredient Nutrition Population Workflow

Goal
- Aggregate ingredient candidates from generated recipes, populate nutrient-per-gram data from a trusted provider, and update recipe macro blocks deterministically.

Steps
1. Aggregate
   - `python scripts/aggregate_ingredients.py --recipes-dir recipes --output .livingkitchen/ingredient_candidates.json`
   - Produces `.livingkitchen/ingredient_candidates.json` listing candidate ingredient names and occurrences.

2. Fetch nutrition
   - Dry-run to inspect matches: `python scripts/fetch_nutrition_template.py --input .livingkitchen/ingredient_candidates.json --dry-run`
   - To fetch, configure provider credentials (Edamam / USDA FDC) and run with `--provider`.
   - Output example: `living_kitchen/global_memory/nutrition_populated.json` with `ingredients` mapping to per-gram macros.

3. Update recipes
   - Run: `python scripts/update_recipe_macros.py --nutrition living_kitchen/global_memory/nutrition_populated.json --mapping recipes/<dish>/ingredients_mapping.json --servings 8 --recipe recipes/<dish>/baseline.md --write`
   - The script will compute totals and insert a `## Macro Estimate (per serving)` block at the end of the recipe (replacing any existing block).

Provider considerations
- Use a trusted source: USDA FoodData Central (FDC) or Edamam Nutrition API are common options.
- Map provider nutrient names (kcal per 100 g, protein g per 100 g, etc.) to the per-gram fields used in this repo.
- Implement unit conversions carefully (per 100 g → per g).

CSV-based alternative (no API keys)
- Download a bulk CSV from a trusted source (USDA FDC / SR Legacy). The FDC bulk data includes CSV files you can extract; pick the file with nutrient per-100g fields.
- Run the CSV lookup tool:
```powershell
python .\scripts\lookup_nutrition_from_csv.py --csv data\fdc_sample.csv --candidates .livingkitchen\ingredient_candidates.json --output living_kitchen\global_memory\nutrition_from_csv.json
```
- The script will fuzzy-match candidate names to CSV descriptions and write `nutrition_from_csv.json`. Review matches (the script prints candidate → match lines) before using.

Safety
- Do not commit API keys. Use environment variables or a secrets manager.
- Manual review required: auto-populated nutrition should be spot-checked before replacing existing recorded macros.

CI Integration
- Add a job to run `compute_macros.py` and compare results to `## Macro Estimate` blocks; fail if drift > X%.

Notes
- The scripts are intentionally minimal and require some human-in-the-loop mapping for ambiguous ingredient names (e.g., "short ribs" vs "boneless short ribs").
- For reproducibility, commit the ingredient mapping files alongside recipe edits.
