# Living Kitchen Self-Test Runbook

## Purpose
Validate the framework end-to-end without touching production recipes by using the provided `self_test_recipe.md`.

## Steps
1. Create folder `/recipes/self_test/`.
2. Copy `living_kitchen/self_test_recipe.md` to `/recipes/self_test/original.md`.
3. Initialize `flavor_profile_v1.md` and `ontology_patch_v1.md` per templates using self-test ingredients.
4. Run the pipeline via `/livingkitchen self_test`, following the master prompt phases.
5. Ensure Version Manager creates `/recipes/self_test/version_manifest.json` based on the template.

## Expected Outputs
- `baseline_v1.md`
- `critic_v1.md`
- `weeknight_v1.md`
- `marriage_v1.md`
- `vegetarian_v1.md`
- `vegan_v1.md`
- `dairyfree_v1.md`
- `keto_v1.md`
- `harmonizer_v1.md`
- `audit_v1.md`
- `memory_v1.md`
- `version_manifest.json`

## Compliance Checklist
- Every recipe step includes ingredient quantities with units.
- Each recipe ends with `### Macro Estimate (per serving)` containing all required fields.
- `compliance_agent` reports `compliance_pass: true`.
- Global memory files updated with bounded deltas and conform to schemas.
- `version_manifest.json` records dish name `self_test`, truth source hash, timestamp, and version numbers.

## Troubleshooting
- Missing macro section → rerun relevant agent with macro reference table loaded.
- Compliance failure → review violation list, fix upstream files, rerun affected phases.
- Manifest absent → ensure Version Manager agent executed Phases -1 and 7.
