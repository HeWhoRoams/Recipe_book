Here’s a direct, strategic breakdown of **B → F** with no fluff.
Everything is actionable. Everything is deterministic.
You're building the DevOps pipeline of food, so the documentation and structural rules must reflect that.

---

# **B. README.md (DROP-IN READY)**

Here is a clean, professional, repo-ready README for your `/recipes/<dish_name>/` folders.
This explains the workflow, the philosophy, the versioning rules, and the CI/CD behavior.

Copy/paste this **exactly**:

---

## **LivingKitchen Recipe Folder README**

### **Overview**

This folder contains the full “recipe-as-code” representation for this dish.
Every file in this directory is part of a deterministic CI/CD pipeline for culinary development powered by the **LivingKitchen Framework**.

The goal:

* Treat recipes like software
* Version every change
* Regenerate variants automatically
* Maintain history
* Continuously improve flavor fidelity and accessibility

---

## **Folder Contents**

Each run of the LivingKitchen pipeline generates or updates:

| File                   | Purpose                                                          |
| ---------------------- | ---------------------------------------------------------------- |
| `original.md`          | The truth-source recipe. Human-written or human-modified.        |
| `baseline_vX.md`       | Canonical baseline recipe built via Chef→Critic loop.            |
| `flavor_profile_vX.md` | Flavor vector model for the dish.                                |
| `ontology_patch_vX.md` | Ingredient substitutions, confidences, cultural notes.           |
| `weeknight_vX.md`      | Time-optimized variant.                                          |
| `marriage_vX.md`       | Michelin-level variant.                                          |
| `vegetarian_vX.md`     | Vegetarian variant.                                              |
| `vegan_vX.md`          | Vegan extension of the vegetarian version.                       |
| `dairyfree_vX.md`      | Dairy-free variant.                                              |
| `keto_vX.md`           | Keto (low-carb) variant.                                         |
| `audit_vX.md`          | Flavor similarity, structural consistency, and ecosystem health. |
| `harmonizer_vX.md`     | Structural normalization across variants.                        |
| `memory_vX.md`         | Per-dish knowledge graph delta and experience notes.             |

All files carry explicit version numbers and timestamps.

---

## **Workflow**

### **1. Creating a new recipe**

```
mkdir recipes/my_new_dish
cp living_kitchen/templates/original.md recipes/my_new_dish/original.md
```

Populate `original.md` with:

* Raw recipe
* Ingredients
* Instructions
* Any notes

Add:

```
truth_source: true
```

Then run:

```
/livingkitchen my_new_dish
```

---

### **2. Cooking and Iterating**

After cooking a recipe:

1. Edit **only one** file (usually `original.md` or `baseline_vX.md`).
2. Add or ensure:

   ```
   truth_source: true
   ```
3. Re-run the pipeline:

   ```
   /livingkitchen my_new_dish
   ```

LivingKitchen detects:

* The changed truth-source
* Rebuilds flavor profile
* Updates ontology if needed
* Regenerates baseline
* Regenerates all variants
* Produces updated audit & memory
* Increments all necessary versions

Commit the results to GitHub.

---

### **3. Versioning Rules**

* No file is ever overwritten.
* New versions are always created (`*_v2.md`, `*_v3.md`, etc.).
* History is preserved for full traceability.
* Memory files capture flavor drift and substitution performance.

---

### **4. Flavor Determinism**

All variants must preserve:

* Core flavor vector
* Cultural integrity rules
* Ingredient ontology structure

If drift is detected, the Auditor reports it.

---

### **5. Support for Dietary Variants**

The pipeline automatically generates:

* Weeknight
* Michelin (“Marriage”)
* Vegetarian
* Vegan
* Dairy-Free
* Keto

Each is a standalone recipe with fully enumerated ingredients and instructions.

---

### **6. Human-in-the-loop cycle**

You cook → you modify → LivingKitchen regenerates → Git stores the history.
This is iterative culinary R&D with software development rigor.

---

# **END README**
