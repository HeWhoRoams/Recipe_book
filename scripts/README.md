Standalone Macro Computation Script

What this is
- `compute_macros.py` is a tiny, dependency-free Python script that reads the project's
  `global_macro_reference.json` and an `ingredients_mapping.json` (ingredient keys -> grams)
  and prints totals and per-serving macros.

Why this is accessible
- No MCP or external LSP required — works with any Python 3.8+ installation.
- Input mapping is plain JSON so people can generate it from spreadsheets or other tools.

Quick usage (PowerShell)
```powershell
python .\scripts\compute_macros.py \
  --macro-ref .\living_kitchen\global_memory\global_macro_reference.json \
  --ingredients .\recipes\optimized_short_rib_multi_chile_chili\ingredients_mapping.json \
  --servings 8
```

Quick usage (Unix / Bash)
```bash
python3 scripts/compute_macros.py \
  --macro-ref living_kitchen/global_memory/global_macro_reference.json \
  --ingredients recipes/optimized_short_rib_multi_chile_chili/ingredients_mapping.json \
  --servings 8
```

Options
- `--output <path>` will write a JSON file with totals and per-serving totals.
- Ingredients keys try simple normalization; if your mapping uses other names, add the
  canonical key or match keys by underscore-normalized names.

Next steps you can automate
- Add a small wrapper to update `recipes/<dish>/baseline.md` by inserting the `Macro Estimate` block.
- Add CI job to run the script and fail if macros are missing or differ by >X% from recorded values.
