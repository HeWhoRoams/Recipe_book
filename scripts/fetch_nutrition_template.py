#!/usr/bin/env python3
"""
Template: fetch nutrition data for an ingredient list and write a `nutrition_reference.json`.

This is a template and intentionally does not include real API keys. It supports two modes:
 - dry-run: prints what would be fetched
 - fetch: requires setting environment variables for API keys and endpoint

Supported providers: fill in provider-specific code. Example placeholders for FoodData Central or Edamam.

Output format (example):
{
  "ingredient_key": {
     "kcal_per_g": 2.9,
     "protein_per_g": 0.2,
     "fat_per_g": 0.23,
     "carb_per_g": 0.0,
     "fiber_per_g": 0.0,
     "sodium_per_g": 0.00075
  }
}

Usage (dry-run):
 python scripts/fetch_nutrition_template.py --input .livingkitchen/ingredient_candidates.json --dry-run

Usage (fetch, provider-specific env vars required):
 python scripts/fetch_nutrition_template.py --input .livingkitchen/ingredient_candidates.json --output living_kitchen/global_memory/nutrition_populated.json --provider edamam

Note: User must provide API credentials in environment variables or a config file.
"""
import argparse
import json
import os
import sys


def provider_lookup_stub(name):
    # Small heuristic: map simple ingredient names to plausible per-gram macros for a dry-run
    examples = {
        'beef short ribs': { 'kcal_per_g': 2.90, 'protein_per_g': 0.20, 'fat_per_g': 0.23, 'carb_per_g': 0.0, 'fiber_per_g': 0.0, 'sodium_per_g': 0.00075 },
        'onion': { 'kcal_per_g': 0.40, 'protein_per_g': 0.01, 'fat_per_g': 0.0, 'carb_per_g': 0.09, 'fiber_per_g': 0.01, 'sodium_per_g': 0.00002 },
        'kidney beans': { 'kcal_per_g': 1.27, 'protein_per_g': 0.09, 'fat_per_g': 0.0, 'carb_per_g': 0.22, 'fiber_per_g': 0.08, 'sodium_per_g': 0.0002 },
    }
    lname = name.lower()
    for k, v in examples.items():
        if k in lname:
            return v
    # default fallback
    return { 'kcal_per_g': 0.0, 'protein_per_g': 0.0, 'fat_per_g': 0.0, 'carb_per_g': 0.0, 'fiber_per_g': 0.0, 'sodium_per_g': 0.0 }


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input', default='.livingkitchen/ingredient_candidates.json')
    p.add_argument('--output', default='living_kitchen/global_memory/nutrition_populated.json')
    p.add_argument('--provider', choices=['edamam','federal','mock'], default='mock')
    p.add_argument('--dry-run', action='store_true')
    args = p.parse_args()

    with open(args.input, 'r', encoding='utf-8') as f:
        candidates = json.load(f)

    populated = {}
    for ing in candidates.keys():
        if args.dry_run:
            print('Would fetch for:', ing)
            populated[ing] = provider_lookup_stub(ing)
            continue
        if args.provider == 'mock':
            populated[ing] = provider_lookup_stub(ing)
            continue
        # Provider-specific code would go here. Requires API credentials and parsing responses.
        # For production use, implement Edamam or FDC API calls with retries and mapping to per-gram values.
        print('Provider fetch not implemented for', args.provider)
        sys.exit(1)

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump({ 'ingredients': populated }, f, indent=2)
    print('Wrote', args.output)

if __name__ == '__main__':
    main()
