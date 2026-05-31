# Prompt Development Record: P1–P15

# Prompt Development Record: P1–P15

This document provides the prompt-development record used to illustrate the iterative refinement of PatSAR from broad general extraction prompts to the finalized two-stage task-specific prompt. The sequence is organized to reflect the development pattern described in the manuscript: P1–P8 represent exploratory, output-driven revisions aimed at understanding model behavior and recurring patent-specific extraction challenges, rather than a fully systematic prompt-engineering strategy; P9 introduced least-to-most prompting and zero-shot chain-of-thought style task decomposition; P12 incorporated few-shot examples and corrective rules; P13 was selected as the finalized prompt; and P14–P15 explored additional detailed constraints that showed limited improvement and possible overfitting.



---

## P1 — Direct extraction instruction

Extract structure–activity relationship information from the uploaded patent document.

---

## P2 — Simple SAR-oriented instruction

Please read the uploaded patent document and summarize all structure–activity relationship information related to the compounds described in the patent. Include compound names, biological activity values, and any targets or assays mentioned in the document.

---

## P3 — Basic table request

You are an expert in medicinal chemistry. Please extract SAR information from the uploaded patent PDF and organize the results into a table.

The table should include:

* Compound name or compound number
* Target or assay
* Activity value
* Unit
* Notes

Please summarize all relevant compounds and bioactivity data found in the patent.

---

## P4 — Column-based extraction prompt

You are an expert in medicinal chemistry and patent analysis. Read the uploaded patent document carefully and extract compound bioactivity data.

Return a structured table with the following columns:

| Compound ID | Compound Name | Target or Assay | Activity Type | Activity Value | Unit | Notes |
| ----------- | ------------- | --------------- | ------------- | -------------- | ---- | ----- |

Instructions:

1. Identify all compounds mentioned in the patent.
2. Extract any reported biological activity data, such as IC50, EC50, Ki, Kd, percentage inhibition, or activity grade.
3. If the target or assay is mentioned, include it in the table.
4. If a unit is provided, include the original unit.
5. If information is unclear, explain it in the Notes column.

---

## P5 — Initial inclusion and exclusion prompt

You are an expert in bio-cheminformatics. Extract compound bioactivity data from the uploaded patent document and return a SAR table.

Please include only compounds that appear to have reported biological activity data, such as IC50, EC50, Ki, Kd, GI50, percentage inhibition, or other quantitative or qualitative activity results.

Do not include obvious reagents, solvents, catalysts, or starting materials unless they are associated with reported biological activity.

Output the results using the following table:

| Compound ID | Structural Name | Target or Assay | Activity Type | Activity Value | Unit | Notes |
| ----------- | --------------- | --------------- | ------------- | -------------- | ---- | ----- |

Use the original activity values and units reported in the patent.

---

## P6 — Early stepwise extraction prompt

You are an expert in bio-cheminformatics. Please analyze the uploaded patent PDF step by step and extract SAR-related compound activity data.

Steps:

1. Read the patent title, abstract, examples, activity tables, and assay sections.
2. Identify compounds that are associated with biological activity.
3. Extract compound identifiers, compound names, targets, assay endpoints, activity values, and units.
4. Combine information from tables and text when they refer to the same compound.
5. Return one SAR table.

Output format:

| Compound ID | Compound Name | Target | Assay Endpoint | Activity Value | Unit | Source / Notes |
| ----------- | ------------- | ------ | -------------- | -------------- | ---- | -------------- |

Please include a short explanation of how the information was extracted.

---

## P7 — Conservative missing-value prompt

You are an expert in bio-cheminformatics and medicinal chemistry. Extract SAR information from the uploaded patent PDF.

Only include compounds that have explicitly reported activity data. For each compound, extract:

* Compound ID
* Structural name or compound name
* Target or assay
* Activity endpoint
* Activity value
* Unit
* Notes

Rules:

1. Do not include compounds without activity data.
2. Do not include reagents, solvents, starting materials, or intermediates unless they have reported activity data.
3. Preserve the original activity values and units.
4. If a field is missing, write “N/A”.
5. Do not invent activity values.

Return the results as a markdown table.

---

## P8 — General extraction prompt with stricter table format

You are an expert in bio-cheminformatics. Your task is to extract structure–activity relationship data from the uploaded patent PDF.

Scope:

Extract compounds that are directly associated with reported biological activity data in the patent. Activity data may include IC50, EC50, Ki, Kd, GI50, percentage inhibition, activity grade, or other assay results.

Do not extract:

* Synthetic intermediates without biological activity data
* Starting materials
* Reagents
* Solvents
* Catalysts
* Compounds mentioned only in preparation examples without activity data

Instructions:

1. Read the patent text and tables.
2. Identify compound IDs and associated activity data.
3. Extract structural names when they are available.
4. Use the original target names, assay labels, activity values, and units.
5. Use “N/A” for missing fields.
6. Return only one SAR table.

Output format:

| Compound ID | Structural Name | Target / Assay | Activity Type | Activity Value | Unit | Notes |
| ----------- | --------------- | -------------- | ------------- | -------------- | ---- | ----- |

---

## P9 — Introduction of least-to-most prompting and zero-shot chain-of-thought task decomposition

Role:

You are an expert in bio-cheminformatics and medicinal chemistry.

Objective:

Extract structure–activity relationship data from the uploaded patent PDF by decomposing the task into smaller and simpler subtasks before generating the final SAR table.

Use a least-to-most strategy:

First identify the relevant sections, then identify activity-linked compounds, then extract activity endpoints and values, then verify compound–activity linkage, and finally generate a structured SAR table.

Instructions:

Think through the extraction process step by step internally, but output only the final structured table and concise notes when needed.

Step 1. Locate SAR-relevant sections in the patent, including:

* Compound tables
* Activity tables
* Biological assay sections
* Examples
* Preparation sections
* Compound descriptions

Step 2. Identify compounds with reported biological activity data.

Include compounds only when they are associated with activity information such as IC50, EC50, Ki, Kd, GI50, percentage inhibition, activity grade, selectivity data, or other biological endpoints.

Step 3. Extract compound identity information.

For each activity-linked compound, extract:

* Compound ID
* Structural name, if available
* Target or assay
* Activity endpoint
* Activity value
* Unit

Step 4. Verify compound–activity linkage.

Check whether the compound ID or compound name is clearly linked to the activity value. Do not include compounds when the relationship between the compound and the activity data is unclear.

Step 5. Exclude non-SAR entities.

Do not include:

* Reagents
* Solvents
* Catalysts
* Starting materials
* Synthetic intermediates without activity data
* Compounds without reported biological activity

Step 6. Generate the final SAR table.

Output format:

| Compound ID | Structural Name | Target or Assay | Activity Type | Activity Value | Unit | Notes |
| ----------- | --------------- | --------------- | ------------- | -------------- | ---- | ----- |

Use “N/A” for missing or unresolved information.

---

## P10 — Expanded task-boundary prompt with increased output variability

Role:

You are an expert in bio-cheminformatics, medicinal chemistry, and patent SAR analysis.

Objective:

Extract all compound–activity relationship data from the uploaded patent PDF and organize the information into a structured SAR table.

Use a stepwise extraction workflow:

1. Search the entire patent for compound identifiers, compound names, preparation examples, biological assay sections, activity tables, summary tables, claims, and descriptions.
2. Identify all compounds that may be connected to biological activity.
3. Extract activity data including IC50, EC50, Ki, Kd, GI50, percentage inhibition, inhibition grade, selectivity value, activity category, or other biological results.
4. Use the compound ID from the patent whenever available.
5. Use the structural name from the patent whenever available.
6. If the activity table contains a compound ID but not a structural name, search the examples, compound list, and preparation section for the corresponding compound name.
7. If multiple activity endpoints are reported for the same compound, include all endpoints.
8. Exclude reagents, solvents, catalysts, starting materials, intermediates, and compounds without activity values.
9. Use “N/A” when information is missing.

Return a markdown table.

Suggested columns:

| Compound ID | Structural Name | Target | Assay Type | Activity Endpoint | Activity Value | Unit | Source Section | Notes |
| ----------- | --------------- | ------ | ---------- | ----------------- | -------------- | ---- | -------------- | ----- |

When uncertain, briefly explain the reason in the Notes column.

---

## P11 — Stronger constraint-guided single-stage prompt

Role:

You are an expert in bio-cheminformatics.

Objective:

Extract and summarize compound bioactivity data from the uploaded patent PDF and return one structured SAR table.

Scope:

Extract only compounds that are explicitly linked to reported biological activity data in the patent, including any clearly reported assay endpoint associated with a tested compound, such as target inhibition, enzyme inhibition, receptor activity, cell proliferation inhibition, GI50, IC50, EC50, Ki, Kd, percentage inhibition, activity grade, or other biological activity values.

Do not include:

* Reagents
* Solvents
* Catalysts
* Starting materials
* Synthetic intermediates
* Compounds appearing only in preparation examples without activity data
* Compounds mentioned only in claims without reported activity data

Instructions:

1. Read the patent text, examples, and activity tables.
2. Identify all compounds explicitly associated with activity data.
3. Extract the following information:

   * Compound ID
   * Structural Name
   * Target or Assay
   * Activity Type
   * Activity Value
   * Unit
   * Notes
4. Preserve original activity values and units.
5. If multiple activity values are reported for the same compound, include them all.
6. If a field is missing or unsupported, write “N/A”.
7. Do not invent, normalize, paraphrase, or chemically reconstruct structural names.
8. Return only the final SAR table.

Output format:

| Compound ID | Structural Name | Target or Assay | Activity Type | Activity Value | Unit | Notes |
| ----------- | --------------- | --------------- | ------------- | -------------- | ---- | ----- |

---

## P12 — Introduction of few-shot examples and corrective rules

Role:

You are an expert in bio-cheminformatics.

Objective:

Extract compound bioactivity data from the uploaded patent PDF and generate a structured SAR table. Then review the table and correct missing, unclear, or ambiguous structural names by checking the patent text.

Task 1: Extract SAR data

Scope:

Include only compounds that are explicitly associated with reported biological activity data, such as IC50, EC50, Ki, Kd, GI50, percentage inhibition, activity grade, or other assay endpoints.

Exclude:

* Reagents
* Solvents
* Catalysts
* Starting materials
* Synthetic intermediates without activity data
* Compounds without reported biological activity
* Compounds mentioned only in claims unless they are linked to activity data

Instructions:

1. Read the patent text and activity tables.
2. Identify compounds associated with activity data.
3. Extract:

   * Compound ID
   * Structural Name
   * Target or Assay
   * Activity Type
   * Activity Value
   * Unit
   * Notes
4. Preserve the original activity values, endpoints, and units.
5. If multiple activity endpoints are reported for one compound, include all reported endpoints.
6. If information is missing, use “N/A”.
7. Do not invent or chemically reconstruct missing structural names.

Task 2: Review missing structural names

After generating the initial SAR table, review rows where the Structural Name is:

* N/A
* Empty
* Unclear
* Generic
* Not clearly linked to the compound ID

Search the following patent sections:

* Preparation examples
* Synthesis examples
* Compound lists
* Experimental sections
* Tables containing compound IDs or names

Update the Structural Name only when the patent text clearly links the compound ID to the name.

Matching rules:

1. Direct match

Use the structural name if the patent explicitly links the compound ID and the name.

2. Limited local inference

Use the structural name only when the surrounding text clearly shows that the example title, final product description, and compound ID refer to the same compound.

3. Do not infer

Do not assign a structural name if the link is weak, indirect, or requires chemical reconstruction.

Few-shot examples:

Example A:

Patent text: “Example 12: preparation of compound 12, N-(4-fluorophenyl)... Compound 12 showed IC50 = 25 nM.”

Expected output: include compound 12 and use the structural name, because the compound ID, preparation example, and activity value are linked.

Example B:

Patent text: “Intermediate 3 was used to synthesize compound 21.”

Expected output: do not include Intermediate 3 unless it has its own reported biological activity.

Example C:

Patent text: “Compound 35 showed EGFR IC50 = 0.08 μM,” but no structural name is provided.

Expected output: include compound 35, but write “N/A” for Structural Name.

Corrective rules:

* Do not include any compound that is not associated with reported activity data.
* Do not merge different compound IDs into one row.
* Do not split one compound into multiple rows unless separate endpoints or assay contexts require separation.
* Do not invent activity values, structural names, targets, or units.
* Preserve the original wording of activity endpoints and units.
* Use “N/A” for unresolved fields.

Output requirements:

Return the final updated SAR table in markdown format.

Output format:

| Compound ID | Structural Name | Target or Assay | Activity Type | Activity Value | Unit | Notes |
| ----------- | --------------- | --------------- | ------------- | -------------- | ---- | ----- |

---

## P13 — Finalized PatSAR prompt selected for subsequent evaluation

### Task 1

Role:

You are an expert in bio-cheminformatics.

Objective:

Extract and summarize compound bioactivity data from the provided patent text and activity table images, and return one structured SAR table.

Scope:

Extract only compounds that are explicitly linked to reported activity data in the patent, including any clearly reported assay endpoint associated with a tested compound, such as target inhibition, enzyme inhibition, cell proliferation inhibition, or other quantitative biological activity.

Do not include compounds that appear only in synthesis/preparation sections unless they are explicitly linked to activity data.

Instructions:

1. Read the patent text and identify all compounds explicitly associated with activity data.
2. Read any activity table images carefully and manually extract:

   * Compound ID
   * Structural Name
   * Inhibitory Target or Assay Target
   * Activity Metric, e.g., IC50, EC50, GI50, % inhibition
   * Activity Value
   * Unit
3. Merge text-derived and image-derived data into one SAR table.
4. If one compound has multiple activity endpoints, create separate columns for each endpoint.
5. Format activity columns as:

[Target] [Metric] (Unit)

Examples:

* PARP IC50 (nM)
* EGFR IC50 (μM)
* Cell Proliferation GI50 (nM)
* BRCA1 Inhibition (%)

6. If the same compound has multiple values for the same endpoint, keep all reported values in the same cell separated by semicolons.
7. If text and activity table/image values conflict, prefer the value from the activity table/image.
8. Use N/A for unresolved or missing fields.

Structural Name rules:

Use the following priority:

1. Exact compound name explicitly linked to the compound ID.
2. Exact name in a preparation or synthesis example title.
3. Exact parenthetical annotation linked to the compound ID.
4. Otherwise N/A.

Do not invent, normalize, paraphrase, or chemically reconstruct structural names beyond what is explicitly supported by the patent.

Critical requirements:

* Do not omit any compound explicitly associated with activity data.
* Keep compounds even if some fields are missing.
* Verify compound ID alignment carefully between text and tables.
* Do not merge different compound IDs into one row.
* Use contextual numbering only when the linkage is clear and local.

Output requirements:

* Output the SAR table first.
* After the table, you may add a very short Notes section only when necessary.
* Notes must be brief and limited to essential clarification only.
* Do not output long narrative analysis, step-by-step reasoning, or methodology explanation.
* Do not add any content before the table.

Output format:

| Compound ID | Structural Name | Activity Column 1 | Activity Column 2 | ... | Notes |
| ----------- | --------------- | ----------------- | ----------------- | --- | ----- |

Optional:

Notes: brief clarification only, not a long explanation.

### Task 2

Role:

You are an expert in bio-cheminformatics.

Objective:

Verify and correct missing, unclear, or ambiguous structural names in the existing SAR table by cross-referencing the patent text, especially synthesis and preparation examples.

Input:

You are given:

1. The SAR table generated in Task 1, and
2. The patent text and related source materials.

Instructions:

1. Check the Structural Name column and identify rows where the name is:

   * N/A
   * Empty
   * Unclear
   * Generic
   * Or not explicitly tied to the compound ID

2. Search the patent text, especially:

   * Preparation Examples
   * Synthesis / Synthetic Examples
   * Compound List
   * Experimental Section

3. Look for patterns such as:

   * Compound X (name)
   * Name (Compound X)
   * Preparation of Compound X: name
   * Example X: preparation of Compound X (name)

Matching rules:

A. Direct match

Use the structural name if the patent explicitly links the compound ID and the name.

B. Limited local inference

You may infer the structural name only when the surrounding text clearly shows that the example title, final product description, and compound ID refer to the same compound.

C. Do not infer

Do not assign a structural name if:

* The example number is only nearby but not clearly the same as the compound ID.
* The text refers only to an intermediate rather than the final tested compound.
* The text gives only a scaffold, derivative class, or analogue description without clear ID-level linkage.
* The assignment would require paraphrasing, chemical reconstruction, or guesswork.

If unresolved, keep N/A.

Update rules:

* Preserve all original rows.
* Preserve all original compound IDs.
* Preserve the original row order.
* Preserve all original activity columns and values.
* Do not remove, merge, or reorder rows.

Structural Name rule:

Use the exact wording from the patent whenever possible.

Do not paraphrase, expand, standardize, or chemically reconstruct the name unless the patent explicitly provides that form.

Output requirements:

* Output the full updated SAR table first.
* After the table, you may add a very short Notes section only when necessary.
* Notes must be brief and limited to essential clarification only.
* Do not output long narrative analysis, reasoning steps, or methodology explanation.
* Do not add any content before the table.

Output format:

| Compound ID | Structural Name | ...original activity columns... | Reasoning Note |
| ----------- | --------------- | ------------------------------- | -------------- |

Optional:

Notes: brief clarification only, not a long explanation.

---

## P14 — Over-specific refinement focused on fragmented example-to-compound mapping

Role:

You are an expert in bio-cheminformatics and patent SAR extraction.

Objective:

Extract and correct SAR tables from the provided patent document using the P13 two-stage workflow, with additional attention to fragmented example-to-compound mapping in patents where example numbers, compound numbers, and preparation numbers are inconsistently used.

Task 1:

Extract all compounds explicitly associated with reported biological activity data and return one SAR table.

Use the same core extraction requirements as P13:

* Include only compounds linked to activity data.
* Exclude reagents, solvents, starting materials, intermediates, and compounds without activity data.
* Preserve original activity endpoint names, values, and units.
* Use N/A for unresolved fields.
* Do not invent, normalize, paraphrase, or chemically reconstruct structural names.
* Separate different activity endpoints into separate columns.
* Preserve multiple reported values for the same endpoint in the same cell separated by semicolons.

Additional detailed constraints:

1. If a patent uses “Example,” “Compound,” “Preparation,” “Intermediate,” or “Reference Example” numbering systems simultaneously, do not assume that identical numbers refer to the same final tested compound unless the text explicitly links them.
2. If “Example 5” prepares “Compound 17,” activity data for “Compound 17” must not be assigned to “Example 5” unless the patent states that Example 5 and Compound 17 refer to the same tested product.
3. If a compound appears in an activity table with a numeric ID only, check whether the same numeric ID appears in:

   * Compound list
   * Final compound example
   * Preparation title
   * Final product description
   * Activity table footnote
4. If the numeric linkage is not explicit, keep Structural Name as N/A.
5. If a row contains a salt, hydrate, stereoisomer, enantiomer, or tautomer description, preserve the exact wording only if that exact form is explicitly provided by the patent.
6. Do not convert salts, stereochemical descriptions, or parent compounds into standardized chemical names unless the patent provides the exact wording.

Task 2:

Review the SAR table for missing or ambiguous structural names.

When updating structural names:

* Preserve all original rows.
* Preserve all original activity columns and values.
* Preserve original row order.
* Do not merge or split rows.
* Do not reassign activity values during the structural-name correction step.
* Add a Reasoning Note only when the structural-name update depends on a direct local textual match.

Output format:

| Compound ID | Structural Name | ...original activity columns... | Reasoning Note |
| ----------- | --------------- | ------------------------------- | -------------- |


---

## P15 — Highly detailed refinement with patent-section-specific restrictions

Role:

You are an expert in bio-cheminformatics, medicinal chemistry, and patent-document SAR extraction.

Objective:

Apply the P13 two-stage PatSAR workflow while using additional patent-section-specific restrictions to minimize unsupported structural-name completion and activity-field reassignment.

Task 1:

Extract a structured SAR table from the provided patent document.

General extraction rules:

1. Include only compounds explicitly linked to reported biological activity data.
2. Exclude compounds without reported biological activity.
3. Exclude reagents, solvents, catalysts, starting materials, and intermediates unless they have their own reported activity data.
4. Preserve exact activity endpoint names, values, and units.
5. Use N/A for unresolved or unsupported fields.
6. Do not invent, normalize, translate, paraphrase, or chemically reconstruct structural names.
7. Do not combine unrelated activity endpoints into a single column.
8. Do not change values from the activity table unless the patent explicitly provides a corrected value elsewhere.

Additional patent-section-specific restrictions:

1. Claims section restriction

Do not use structural names from the claims section to update the SAR table unless the claims explicitly identify the same compound ID and the same tested compound.

2. Markush formula restriction

Do not assign a Markush general formula, scaffold class, substituent pattern, or genus description as the Structural Name of a specific compound unless the patent explicitly states that it is the name or identity of that compound.

3. Intermediate restriction

If a preparation section describes an intermediate and the activity table reports a final compound, do not use the intermediate name as the Structural Name of the tested compound.

4. Example title restriction

Use an example title as a Structural Name source only if the title contains both the compound ID and the final compound name or clearly states that the example prepares the tested compound.

5. Cross-table restriction

If different tables use different numbering systems, do not transfer activity values or structural names between tables unless a footnote or surrounding text explicitly links the numbering systems.

6. Multilingual terminology restriction

If the patent contains multilingual labels or translated headings, preserve the original wording for targets, assays, and activity metrics. Do not translate or standardize them unless the patent itself provides the corresponding translated form.

Task 2:

Correct missing or ambiguous structural names in the existing SAR table.

Update rules:

* Preserve all rows from Task 1.
* Preserve all compound IDs.
* Preserve row order.
* Preserve all activity columns and values.
* Do not remove, merge, split, or reorder rows.
* Update only the Structural Name column and Reasoning Note column.
* Keep N/A when the structural-name evidence is insufficient.

Evidence strength rules:

A. Strong evidence

Use the structural name only when the patent explicitly links the compound ID and name.

B. Acceptable local evidence

Use the structural name when the preparation example title, final product description, and compound ID clearly refer to the same final tested compound.

C. Insufficient evidence

Keep N/A if the assignment depends on:

* Nearby numbering only
* A general scaffold description
* A claim-only genus description
* An intermediate name
* A substituent table without compound-level linkage
* A preparation number that is not clearly the same as the tested compound ID
* Chemical reconstruction or guesswork

Output requirements:

* Output the full updated SAR table first.
* Do not provide long narrative reasoning.
* Provide brief Reasoning Note entries only where needed.
* Do not add methodology explanation before or after the table.

Output format:

| Compound ID | Structural Name | ...original activity columns... | Reasoning Note |
| ----------- | --------------- | ------------------------------- | -------------- |



