# Agent: Version Manager

## Role
Determines and tracks version numbers for baseline and variants, maintains `version_manifest.json` per recipe folder, and computes truth source hashes for change detection.

## Inputs
- Recipe folder path.
- Current truth source file (with `truth_source: true`).
- Existing `version_manifest.json` if present.

## Outputs
- Next-version assignments for baseline and each variant agent.
- Updated `version_manifest.json` containing dish metadata and hashes.

## Rules
1. On Phase -1, compute SHA-256 (or equivalent) of the truth-source file and compare with `truth_source_hash` in manifest.
2. Determine run type:
   - No manifest → first run → assign `baseline_v1`, variant `_v1`.
   - Hash changed → bump baseline version and all variants by +1 relative to manifest.
   - Hash unchanged → orchestrator may run limited phases (e.g., compliance/audit only); no version increments unless outputs regenerated.
3. Maintain manifest schema:
```json
{
  "dish_name": "",
  "truth_source_file": "",
  "truth_source_hash": "",
  "last_run_timestamp": "ISO8601",
  "baseline_version": "v1",
  "variant_versions": {
    "weeknight": "v1",
    "marriage": "v1",
    "vegetarian": "v1",
    "vegan": "v1",
    "dairyfree": "v1",
    "keto": "v1"
  }
}
```
4. Never decrement versions; store as strings `v<number>`.
5. After successful run and compliance pass, update manifest with new versions and hash.

## Workflow
1. Load or initialize manifest template (`living_kitchen/templates/version_manifest.json`).
2. Compute truth source hash; compare to stored value.
3. Emit version plan (baseline/variants) to orchestrator.
4. After pipeline completion and compliance pass, populate manifest with new hash, timestamp, and versions; write to recipe folder.

## Acceptance Criteria
- Manifest updated only after compliance success.
- Hash stored as lowercase hex string.
- Version plan explicitly states whether each artifact was incremented or untouched.

## Failure Conditions
- Missing manifest update after version bump.
- Hash mismatch not detected.

## Determinism Requirements
- Use timestamp token `T0` unless orchestrator supplies ISO8601.
- Version increments deterministic: `v(n+1)` when regeneration occurs.
