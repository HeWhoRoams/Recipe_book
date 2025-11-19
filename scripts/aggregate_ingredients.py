#!/usr/bin/env python3
"""
Aggregate ingredient names from all recipe markdown files into a single JSON file.

This script is intentionally tolerant: it extracts lines under an "## Ingredients" heading
and normalizes simple bullet and table lines into candidate ingredient names.

Output: .livingkitchen/ingredient_candidates.json with structure:
{
  "ingredient": {
     "occurrences": ["recipes/.../baseline.md:line...", ...]
  }
}

Run:
 python scripts/aggregate_ingredients.py --recipes-dir recipes --output .livingkitchen/ingredient_candidates.json

The output is intended for use as input to a nutrition-fetcher script which will consult
an external data provider to populate per-gram nutrient rows.
"""
import argparse
import json
import os
import re

ING_SECTION_RE = re.compile(r'^#{2,}\s*Ingredients', re.IGNORECASE)
HEADING_RE = re.compile(r'^#{2,}\s*')
BULLET_RE = re.compile(r'^\s*[-*+]\s+(.*)')
TABLE_ROW_RE = re.compile(r'^\|')


def normalize_name(s):
    # Strip measurements and common em-dash separators
    s = s.strip()
    # If line contains — or -- or — treat left side as ingredient name
    parts = re.split(r'\s+[—\-–]\s+', s, maxsplit=1)
    name = parts[0]
    # Remove quantity parentheticals and trailing measurement tokens
    name = re.sub(r"\([^)]*\)", "", name)
    # Remove leading quantities like '1.1 kg', '2 tbsp', '1 cup', etc.
    name = re.sub(r'^\s*[0-9]+(?:\.[0-9]+)?\s*(?:kg|g|tbsp|tsp|cup|cups|each|oz|lb|ml|l)\b', '', name, flags=re.IGNORECASE)
    name = name.strip(' -:,.')
    return name


def extract_from_file(path):
    ing = []
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    in_ing = False
    for i, line in enumerate(lines):
        if ING_SECTION_RE.match(line):
            in_ing = True
            continue
        if in_ing and HEADING_RE.match(line):
            # next heading starts, stop
            break
        if not in_ing:
            continue
        # bullets
        m = BULLET_RE.match(line)
        if m:
            name = normalize_name(m.group(1))
            if name:
                ing.append((name, i+1))
            continue
        # table row: look for first column after header row
        if TABLE_ROW_RE.match(line):
            # attempt naive split
            cols = [c.strip() for c in line.strip().split('|') if c.strip()]
            if cols:
                # if looks like header or separator skip
                if set(cols[0]) == set('-:'):
                    continue
                name = normalize_name(cols[0])
                if name:
                    ing.append((name, i+1))
            continue
        # fallback: lines that look like ingredient lines with commas
        if ',' in line and len(line.strip()) < 120:
            name = normalize_name(line.split(',')[0])
            if name:
                ing.append((name, i+1))
    return ing


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--recipes-dir', default='recipes')
    p.add_argument('--output', default='.livingkitchen/ingredient_candidates.json')
    args = p.parse_args()

    candidates = {}
    for root, dirs, files in os.walk(args.recipes_dir):
        for fn in files:
            if not fn.endswith('.md'):
                continue
            path = os.path.join(root, fn)
            items = extract_from_file(path)
            for name, lineno in items:
                key = name.strip()
                if not key:
                    continue
                entry = candidates.setdefault(key, { 'occurrences': [] })
                entry['occurrences'].append(f'{path}:{lineno}')

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(candidates, f, indent=2, ensure_ascii=False)
    print('Wrote', args.output)

if __name__ == '__main__':
    main()
