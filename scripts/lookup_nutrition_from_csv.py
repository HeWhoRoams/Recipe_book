#!/usr/bin/env python3
"""
Lookup nutrition values from a local CSV and produce a per-ingredient per-gram JSON.

This script is an accessible alternative to using an API: download a bulk nutrition CSV
(e.g., USDA FoodData Central / SR Legacy extract or a vendor CSV) and run this script
which will fuzzy-match ingredient names to the CSV descriptions and extract per-gram
macros.

CSV expectations (flexible): must contain at least a description column and one or more
of energy/calories, protein, fat, carb, fiber, sodium columns. Prefer per-100g units.

Usage:
  python scripts/lookup_nutrition_from_csv.py --csv data/fdc_sample.csv --candidates .livingkitchen/ingredient_candidates.json --output living_kitchen/global_memory/nutrition_from_csv.json

Notes:
- Uses `difflib.get_close_matches` to find the best row for each candidate name.
- Prints matches and confidence for manual review; writes matched per-gram macro rows to output JSON.
- No external packages required.
"""
import argparse
import csv
import json
import os
import sys
from difflib import get_close_matches

PREFERRED_COLUMNS = [
    ('kcal', ['energy_kcal','energy_kcal_100g','kcal_per_100g','energy']),
    ('protein', ['protein_g','protein_g_100g','protein_per_100g']),
    ('fat', ['fat_g','fat_g_100g','fat_per_100g']),
    ('carb', ['carbohydrate_g','carb_g','carb_g_100g','carb_per_100g','carbohydrate_per_100g']),
    ('fiber', ['fiber_g','fiber_g_100g','fiber_per_100g']),
    ('sodium_mg', ['sodium_mg','sodium_mg_100g','sodium_per_100g','sodium'])
]


def find_columns(header):
    # Map our preferred names to CSV header names
    header_low = [h.lower() for h in header]
    mapping = {}
    for pref, candidates in PREFERRED_COLUMNS:
        found = None
        for c in candidates:
            if c.lower() in header_low:
                idx = header_low.index(c.lower())
                found = header[idx]
                break
        mapping[pref] = found
    # Also try to find a description column
    desc_candidates = ['description','food_name','name','long_description']
    desc_col = None
    for c in desc_candidates:
        if c in header_low:
            desc_col = header[header_low.index(c)]
            break
    return desc_col, mapping


def row_to_macros(row, desc_col, col_map):
    # Expect per-100g values; convert to per-g
    macros = {}
    for key, col in col_map.items():
        if not col:
            macros[key] = None
            continue
        val = row.get(col, '')
        try:
            v = float(val)
        except Exception:
            macros[key] = None
            continue
        if key == 'sodium_mg':
            # sodium in mg per 100g -> convert to g per g: mg/100g -> g/g = (mg/100)/1000
            macros['sodium'] = (v / 100.0) / 1000.0
        else:
            macros[key] = v / 100.0
    # normalize keys to expected output
    out = {
        'kcal_per_g': macros.get('kcal'),
        'protein_per_g': macros.get('protein'),
        'fat_per_g': macros.get('fat'),
        'carb_per_g': macros.get('carb'),
        'fiber_per_g': macros.get('fiber'),
        'sodium_per_g': macros.get('sodium')
    }
    return out


def load_csv_rows(csv_path):
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        desc_col, col_map = find_columns(header)
        rows = []
        for r in reader:
            desc = r.get(desc_col) if desc_col else None
            rows.append((desc, r))
    return header, desc_col, col_map, rows


def normalize_candidate(s):
    return s.lower().strip()


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--csv', required=True, help='Local CSV with nutrition data')
    p.add_argument('--candidates', required=True, help='Ingredient candidates JSON (from aggregate script)')
    p.add_argument('--output', default='living_kitchen/global_memory/nutrition_from_csv.json')
    p.add_argument('--top-n', type=int, default=3, help='How many top fuzzy matches to show for review')
    p.add_argument('--confirm', action='store_true', help='If set, write output without prompting')
    args = p.parse_args()

    header, desc_col, col_map, rows = load_csv_rows(args.csv)
    if not desc_col:
        print('CSV missing a detectable description column. Header:', header)
        sys.exit(1)

    with open(args.candidates, 'r', encoding='utf-8') as f:
        candidates = json.load(f)

    descriptions = [ (i, desc) for i,(desc,_) in enumerate(rows) if desc ]
    desc_texts = [ d for i,d in descriptions ]

    populated = {}
    for cand in candidates.keys():
        norm = normalize_candidate(cand)
        matches = get_close_matches(norm, desc_texts, n=args.top_n, cutoff=0.5)
        print('\nCandidate:', cand)
        if not matches:
            print('  No fuzzy matches found; manual mapping required')
            continue
        for m in matches:
            idx = desc_texts.index(m)
            desc, row = rows[descriptions[idx][0]]
            macros = row_to_macros(row, desc_col, col_map)
            # Compute an ad-hoc confidence score from sequence matching
            print(f'  Match: {desc}  -> kcal_per_g={macros.get("kcal_per_g")}, protein_per_g={macros.get("protein_per_g")}, sodium_per_g={macros.get("sodium_per_g")}')
        # Choose top match automatically for now
        top = matches[0]
        idx = desc_texts.index(top)
        desc, row = rows[descriptions[idx][0]]
        macros = row_to_macros(row, desc_col, col_map)
        populated[cand] = macros

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump({'ingredients': populated}, f, indent=2)
    print('\nWrote', args.output)

if __name__ == '__main__':
    main()
