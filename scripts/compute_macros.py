#!/usr/bin/env python3
"""
Compute per-recipe and per-serving macros using the project's macro reference.
No external dependencies required (uses only the Python stdlib).

Usage:
  python scripts/compute_macros.py \ 
    --macro-ref living_kitchen/global_memory/global_macro_reference.json \
    --ingredients recipes/optimized_short_rib_multi_chile_chili/ingredients_mapping.json \
    [--servings 8]

The ingredients mapping file should be a JSON object keyed by canonical macro keys
(or a short synonym) with values in grams. See example mapping file included.
"""
import argparse
import json
import os
from decimal import Decimal, ROUND_HALF_UP


def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def round_sig(x, sig=3):
    # Round to sig significant digits but keep as float for printing convenience
    d = Decimal(str(x))
    shift = -int(d.adjusted()) + (sig - 1)
    res = d.quantize(Decimal('1e{}'.format(-shift)), rounding=ROUND_HALF_UP)
    return float(res)


def compute_totals(macro_ref, ingredients_map):
    totals = { 'kcal': 0.0, 'protein': 0.0, 'fat': 0.0, 'carb': 0.0, 'fiber': 0.0, 'sodium': 0.0 }
    missing = []
    for name, grams in ingredients_map.items():
        if grams is None or grams == 0:
            continue
        key = name
        if key not in macro_ref:
            # try simple normalization
            key_norm = key.lower().replace(' ', '_')
            if key_norm in macro_ref:
                key = key_norm
            else:
                missing.append(key)
                continue
        ref = macro_ref[key]
        totals['kcal'] += ref.get('kcal_per_g', 0.0) * grams
        totals['protein'] += ref.get('protein_per_g', 0.0) * grams
        totals['fat'] += ref.get('fat_per_g', 0.0) * grams
        totals['carb'] += ref.get('carb_per_g', 0.0) * grams
        totals['fiber'] += ref.get('fiber_per_g', 0.0) * grams
        totals['sodium'] += ref.get('sodium_per_g', 0.0) * grams
    return totals, missing


def main():
    p = argparse.ArgumentParser(description='Compute recipe macros (no external deps)')
    p.add_argument('--macro-ref', required=True, help='Path to global_macro_reference.json')
    p.add_argument('--ingredients', required=True, help='Path to ingredients mapping JSON (name -> grams)')
    p.add_argument('--servings', type=float, default=1.0, help='Number of servings to divide totals by')
    p.add_argument('--output', help='Optional output file path (JSON) to write results')
    args = p.parse_args()

    macro_data = load_json(args.macro_ref)
    macro_ref = macro_data.get('ingredients', {})
    ingredients_map = load_json(args.ingredients)

    totals, missing = compute_totals(macro_ref, ingredients_map)
    per_serving = { k: (v / args.servings) for k, v in totals.items() }

    # Round for readability
    totals_rounded = { k: round_sig(v, 4) for k, v in totals.items() }
    per_serv_rounded = { k: round_sig(v, 4) for k, v in per_serving.items() }

    result = {
        'servings': args.servings,
        'totals': totals_rounded,
        'per_serving': per_serv_rounded,
        'missing_macro_keys': missing,
    }

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2)
        print('Wrote results to', args.output)
    else:
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
