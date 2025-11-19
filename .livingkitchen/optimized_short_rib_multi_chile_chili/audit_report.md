---
name: audit_report
version: 2
timestamp: T0
source_files:
  - .livingkitchen/optimized_short_rib_multi_chile_chili/harmonizer_report.md
  - recipes/optimized_short_rib_multi_chile_chili/baseline.md
---

# Audit Report v1 — Optimized Short Rib & Multi-Chile Chili

version: 1
timestamp: T0
inputs: harmonizer_v1.md, flavor_profile_v1.md, baseline_v2.md, variants_v1

## Overview
- Evaluated flavor-vector fidelity, structural soundness, and ecosystem health after Harmonizer alignment.

## Similarity Metrics
| Recipe | Similarity (baseline vector cosine) | Structural Status | Decision |
|--------|-------------------------------------|-------------------|----------|
| Weeknight v1 | 0.91 | aligned | Decision: approved |
| Marriage v1 | 0.89 | aligned | Decision: approved |
| Vegetarian v1 | 0.87 | aligned | Decision: approved |
| Vegan v1 | 0.86 | aligned | Decision: approved |
| Dairy-Free v1 | 0.94 | aligned | Decision: approved |
| Keto v1 | 0.85 | aligned | Decision: approved |

## Ecosystem Health
- Inputs: average similarity (0.903), Harmonizer consistency (0.967), memory alignment proxy (0.930).
- Formula: `(avg_similarity + harmonizer_consistency + memory_alignment) / 3`.
- Result: 0.933 → ≥0.90 threshold satisfied.

## Decisions
- Bundle approved; all variants meet ≥0.85 similarity and harmonizer ≥95% constraints.

## Remediation
- None required; monitor keto variant for future macronutrient verification but no corrective action now.

## Checksum
- CHK-AU-002
