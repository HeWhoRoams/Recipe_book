#!/usr/bin/env python3
"""
Update recipe markdown with computed Macro Estimate block using a populated nutrition reference.

Usage (dry-run):
 python scripts/update_recipe_macros.py --nutrition living_kitchen/global_memory/nutrition_populated.json --mapping recipes/optimized_short_rib_multi_chile_chili/ingredients_mapping.json --servings 8 --recipe recipes/optimized_short_rib_multi_chile_chili/baseline.md --dry-run

Usage (write):
 python scripts/update_recipe_macros.py --nutrition living_kitchen/global_memory/nutrition_populated.json --mapping recipes/optimized_short_rib_multi_chile_chili/ingredients_mapping.json --servings 8 --recipe recipes/optimized_short_rib_multi_chile_chili/baseline.md --write
"""
import argparse
import json
import re
import os


def compute_from_populated(nutrition_ref, mapping):
    totals = { 'kcal':0.0, 'protein':0.0, 'fat':0.0, 'carb':0.0, 'fiber':0.0, 'sodium':0.0 }
    for name, grams in mapping.items():
        key = name
        if key not in nutrition_ref:
            key = key.lower().replace(' ', '_')
        if key not in nutrition_ref:
            continue
        r = nutrition_ref[key]
        totals['kcal'] += r.get('kcal_per_g',0.0) * grams
        totals['protein'] += r.get('protein_per_g',0.0) * grams
        totals['fat'] += r.get('fat_per_g',0.0) * grams
        totals['carb'] += r.get('carb_per_g',0.0) * grams
        totals['fiber'] += r.get('fiber_per_g',0.0) * grams
        totals['sodium'] += r.get('sodium_per_g',0.0) * grams
    return totals


def format_macro_block(per_serv):
    block = []
    block.append('## Macro Estimate (per serving)')
    block.append(f"- Calories: {per_serv['kcal']:.0f} kcal")
    block.append(f"- Protein (g): {per_serv['protein']:.1f} g")
    block.append(f"- Fat (g): {per_serv['fat']:.1f} g")
    block.append(f"- Carbohydrates (g): {per_serv['carb']:.1f} g")
    block.append(f"- Net Carbs (g): {max(per_serv['carb'] - per_serv['fiber'], 0):.1f} g")
    block.append(f"- Fiber (g): {per_serv['fiber']:.1f} g")
    block.append(f"- Sodium (mg): {per_serv['sodium']*1000:.0f} mg")
    block.append(f"- Serving size (g): {int(per_serv.get('serving_size_g',0)) or 'N/A'}")
    return '\n'.join(block)


def insert_block_into_recipe(recipe_path, block_text):
    with open(recipe_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Remove existing Macro Estimate section if present
    content_new = re.sub(r"## Macro Estimate \(per serving\)[\s\S]*?\n\n", '', content)
    # Append block at end
    content_new = content_new.strip() + '\n\n' + block_text + '\n'
    with open(recipe_path, 'w', encoding='utf-8') as f:
        f.write(content_new)
    print('Updated', recipe_path)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--nutrition', required=True)
    p.add_argument('--mapping', required=True)
    p.add_argument('--servings', type=float, default=1.0)
    p.add_argument('--recipe', required=True)
    p.add_argument('--write', action='store_true')
    p.add_argument('--dry-run', action='store_true')
    args = p.parse_args()

    nutrition = json.load(open(args.nutrition, 'r', encoding='utf-8'))
    nutrition_ref = nutrition.get('ingredients', {}) if 'ingredients' in nutrition else nutrition
    mapping = json.load(open(args.mapping, 'r', encoding='utf-8'))

    totals = compute_from_populated(nutrition_ref, mapping)
    per_serv = { k: totals[k]/args.servings for k in totals }
    per_serv['serving_size_g'] = sum(mapping.values())/args.servings

    block = format_macro_block(per_serv)

    if args.dry_run or not args.write:
        print(block)
    if args.write:
        insert_block_into_recipe(args.recipe, block)

if __name__ == '__main__':
    main()
