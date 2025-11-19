# **LIVINGKITCHEN v5 – PROJECT INSTRUCTION LAYER (FOR COPILOT CHAT)**

You are operating inside the **LivingKitchen Framework v5**, a structured system that treats recipes like code.
You must follow this instruction set whenever the user performs *any* cooking-related request, especially when they use the command:

```
/livingkitchen <recipe_name>
```

This instruction set defines:

* Allowed behaviors
* File structure
* Pipelines
* Agent responsibilities
* Output formatting
* Recipe analysis rules
* Variant generation logic
* Dietary compliance detection
* “Elevation Mode”
* Macro estimation
* Verbose unit inclusion rules

This file **overrides** your default behavior inside this workspace.

---

# ------------------------------------------------------------------------------

# **1. FOLDER STRUCTURE MODEL (CANONICAL, REQUIRED)**

# ------------------------------------------------------------------------------

All recipes must follow this structure:

```
recipes/
  <recipe_name>/
    original.md
    baseline.md
    weeknight.md
    marriage.md
    vegetarian.md
    vegan.md
    dairyfree.md
    keto.md

.livingkitchen/
  <recipe_name>/
    critic_report.md
    audit_report.md
    harmonizer_log.md
    flavor_profile.md
    ingredient_ontology_patch.md
    memory_log.md
```

Rules:

* Only **human-facing recipes** belong inside `recipes/<recipe>/`.
* All system artifacts belong inside `.livingkitchen/<recipe>/`.
* No version numbers in filenames.
* Versioning tracked in **YAML frontmatter** inside each recipe file.
* Copilot must respect this structure when generating output.

---

# ------------------------------------------------------------------------------

# **2. GLOBAL WORKFLOW: /livingkitchen <recipe>**

# ------------------------------------------------------------------------------

Running:

```
/livingkitchen <recipe>
```

triggers the following conceptual pipeline (Copilot must simulate all steps):

### **STEP 1 — Load Recipe Context**

* Read `recipes/<recipe>/original.md` (the user-provided recipe).
* Read any existing variations.
* Read all `.livingkitchen/<recipe>/` artifacts.
* Load global memory files if present.

### **STEP 2 — Perform Baseline Generation or Update**

* Parse the original recipe.
* Normalize structure.
* Produce `baseline.md`.
* Include macro estimates.
* Include repeat-all-units-in-instructions rule.
* Write critic + audit logs to `.livingkitchen/<recipe>/`.

### **STEP 3 — Evaluate Dietary Compliance**

For each variant type:

* vegetarian
* vegan
* dairyfree
* keto

Determine:

```
baseline_meets_constraints: true | false
```

### **STEP 4 — Select Generation Mode**

#### If constraints NOT met:

→ Generate full substitution-based variant.

#### If constraints ARE met:

→ Generate **Elevation Mode** variant:

* No substitutions
* Keep cosine similarity ≥ 0.85 to baseline
* Add domain-specific enhancements
* Add “Compliance Reasoning” section
* Add “Elevation Enhancements” section

### **STEP 5 — Generate All Variants**

Produce (or update):

* weeknight.md
* marriage.md
* vegetarian.md
* vegan.md
* dairyfree.md
* keto.md

Each must be a **full standalone recipe**.

### **STEP 6 — Write System Artifacts**

Update:

* `.livingkitchen/<recipe>/critic_report.md`
* `.livingkitchen/<recipe>/audit_report.md`
* `.livingkitchen/<recipe>/harmonizer_log.md`
* `.livingkitchen/<recipe>/memory_log.md`
* `.livingkitchen/<recipe>/ingredient_ontology_patch.md`
* `.livingkitchen/<recipe>/flavor_profile.md`

### **STEP 7 — Update Frontmatter Version**

Each recipe output must include:

```yaml
version: <int>
timestamp: <ISO8601>
source_files:
  - original.md
  - baseline.md
dependencies:
  - flavor_profile.md
  - ingredient_ontology_patch.md
```

---

# ------------------------------------------------------------------------------

# **3. CORE RULES COPILOT MUST ALWAYS FOLLOW**

# ------------------------------------------------------------------------------

## **3.1 All recipes must include units in every step**

Every step must repeat the exact unit-bearing ingredient amount:

❌ Wrong

> Add the onions.

✔️ Required

> Add the **1.5 cups (1 large)** diced yellow onion.

## **3.2 All recipes must include macro estimates**

Add a section:

```
Macros (per serving):
- Calories:
- Protein:
- Fat:
- Carbohydrates:
- Fiber:
- Net Carbs: (if keto variant)
```

## **3.3 All recipes must be standalone**

No “delta changes.”
No “refer to baseline.”
Every variant must be first-class, complete text.

## **3.4 Marriage variant always maximizes technique + luxury**

Assume unlimited time, skill, and ingredients.

## **3.5 Weeknight version prioritizes speed, shortcuts, and 25–35 minutes total time.**

## **3.6 Vegetarian/Vegan/Dairy-Free/Keto variants must check compliance first**

Baseline-compliance logic is **required**.

If baseline already qualifies → Elevation Mode.

---

# ------------------------------------------------------------------------------

# **4. ELEVATION MODE LOGIC (CRITICAL)**

# ------------------------------------------------------------------------------

For any dietary variant where the baseline qualifies:

* DO NOT substitute
* DO NOT downgrade complexity
* DO NOT produce a carbon copy of the baseline

Instead:

### **Elevation Mode Output Structure**

```
Title
Description
Yields, Prep Time, Cook Time
Compliance Reasoning
Elevation Enhancements
Scientific Rationale (if advanced)
Ingredients (full)
Equipment
Instructions (full; units required)
Macros (full)
```

Enhancement guidelines:

### Vegetarian Elevation

* advanced dairy/egg manipulation
* mushroom umami integration
* browned butter techniques
* cultured dairy for tang/complexity

### Vegan Elevation

* fermentation
* koji/miso
* nut/oil emulsions
* protein completeness (legume + grain optimization)

### Dairy-Free Elevation

* coconut/nut fat structures
* emulsification techniques
* starch-based body

### Keto Elevation

* fat stabilization
* electrolyte balancing
* controlled-carb reductions
* low-carb thickener strategies

---

# ------------------------------------------------------------------------------

# **5. VARIANT AGENTS (SIMULATED BEHAVIOR)**

# ------------------------------------------------------------------------------

Copilot Chat must treat each of these as conceptual subroutines:

* **Chef Agent** → generate baseline
* **Critic Agent** → evaluate and produce critic_report
* **Harmonizer Agent** → enforce formatting and consistency
* **MemoryKeeper Agent** → track changes
* **Auditor Agent** → validate folder structure, unit rules, macros
* **Variant Agents**: weeknight, marriage, vegetarian, vegan, dairyfree, keto

Copilot must **simulate their output**, not create multiple personas.

---

# ------------------------------------------------------------------------------

# **6. OUTPUT FORMATS**

# ------------------------------------------------------------------------------

### Every recipe MUST follow the standard format:

```
---
version: <int>
timestamp: <ISO8601>
source_files: [...]
dependencies: [...]
---

# Title

## Description

## Yields
## Prep Time
## Cook Time

## Scientific Rationale (Baseline + Marriage only)
<optional_or_detailed_text>

## Compliance Reasoning (Elevation Mode only)
## Elevation Enhancements (Elevation Mode only)

## Ingredients
(Use metric + imperial)

## Equipment
(non-standard tools only)

## Instructions
(Numbered + units repeated)

## Macros (per serving)
```

---

# ------------------------------------------------------------------------------

# **7. PERMITTED COMMANDS**

# ------------------------------------------------------------------------------

Copilot Chat must respond to:

### **Generate full pipeline**

```
/livingkitchen <recipe>
```

### **Regenerate only baseline**

```
/livingkitchen baseline <recipe>
```

### **Regenerate variants**

```
/livingkitchen variants <recipe>
```

### **Check structure**

```
/livingkitchen audit <recipe>
```

---

# ------------------------------------------------------------------------------

# **8. NON-PERMITTED BEHAVIORS**

# ------------------------------------------------------------------------------

Copilot Chat must not:

* Create versioned filenames (no `_v1.md`)
* Create delta recipes
* Place files outside defined folders
* Skip units in instructions
* Skip macros
* Skip compliance detection
* Generate partial variants
* Change folder structure
* Invent new agent types
* Ignore flavor profile / ontology
* Output system artifacts into the user-facing folder

---

# ------------------------------------------------------------------------------

# **9. DEFAULT MODE**

# ------------------------------------------------------------------------------

Whenever in doubt:

**Copilot must default to generating the highest-quality, fully compliant LivingKitchen output consistent with v5.0 rules.**

---

# **End of Instructions**

