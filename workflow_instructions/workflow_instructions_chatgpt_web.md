# Workflow Instructions: PatSAR Extraction Using the ChatGPT Web or Desktop Interface

This document describes how to reproduce the PatSAR prompt-based workflow using the ChatGPT web or desktop interface. This version is intended for users who perform document-by-document SAR extraction manually through the ChatGPT interface rather than through the API.

## 1. Purpose

PatSAR is a prompt-based workflow for extracting structure–activity relationship (SAR) information from patent PDF documents. The workflow uses two sequential prompts:

* Task 1: Extract compound–activity information and generate an initial SAR table.
* Task 2: Verify and correct missing, unclear, or ambiguous structural names by cross-referencing the patent text.

The workflow is designed for document-level extraction. Each patent PDF should be processed separately.

## 2. Required materials

Before starting, prepare the following files:

1. Patent PDF file to be analyzed.
2. Finalized PatSAR Task 1 prompt.
3. Finalized PatSAR Task 2 prompt.
4. A spreadsheet or text editor for saving the output SAR table.
5. Optional: a record sheet for tracking the patent ID, model used, date of extraction, and notes.

## 3. Recommended extraction record

For transparency and reproducibility, record the following information for each patent:

| Field                | Description                             |
| -------------------- | --------------------------------------- |
| Patent ID            | Publication number or patent identifier |
| Patent PDF filename  | Name of the uploaded PDF file           |
| Target               | Target name, if applicable              |
| Date of extraction   | Date when the extraction was performed  |
| ChatGPT model        | Model used in the interface             |
| Interface            | Web or desktop                          |
| Task 1 completed     | Yes / No                                |
| Task 2 completed     | Yes / No                                |
| Output filename      | Name of the saved SAR table             |
| Manual review status | Not reviewed / Reviewed / Corrected     |
| Notes                | Any issue observed during extraction    |

## 4. Step-by-step workflow

### Step 1. Log in to ChatGPT

Open the ChatGPT web or desktop interface and log in to an account that supports file upload and document analysis.

Use the same model setting as consistently as possible across all patent analyses. If the model changes during the study, record the model used for each extraction.

### Step 2. Start a new chat

Start a new chat session for each patent PDF.

Processing one patent per chat is recommended to reduce cross-document interference and to keep the extraction record clear.

### Step 3. Upload the patent PDF

Upload the patent PDF file using the file attachment function.

After uploading, wait until the file is fully attached and available in the chat interface before entering the prompt.

### Step 4. Enter the Task 1 prompt

Copy the complete Task 1 prompt from the finalized PatSAR prompt file and paste it into the chat.

The Task 1 prompt should instruct the model to:

* Read the patent text and activity table images.
* Identify compounds explicitly linked to reported activity data.
* Extract compound IDs, structural names, targets or assay endpoints, activity values, and units.
* Merge text-derived and table/image-derived information into one SAR table.
* Use `N/A` for unresolved or missing fields.
* Avoid unsupported inference or chemical reconstruction.
* Output the SAR table first.

Submit the prompt and wait for the model to generate the initial SAR table.

### Step 5. Check whether Task 1 output is complete

After Task 1 output is generated, briefly check whether the output contains a SAR table.

The table should generally include:

* Compound ID
* Structural Name
* Activity columns, such as target, metric, value, and unit
* Notes, if necessary

If the model produces a long narrative explanation before the table, repeat the output requirement and ask it to return only the SAR table.

Example corrective instruction:

```text
Please return only the SAR table according to the required output format. Do not provide long narrative analysis before the table.
```

### Step 6. Enter the Task 2 prompt

After Task 1 is complete, copy the complete Task 2 prompt from the finalized PatSAR prompt file and paste it into the same chat.

Task 2 should be performed in the same chat because the model needs access to:

1. The uploaded patent PDF.
2. The SAR table generated in Task 1.
3. The previous extraction context.

The Task 2 prompt should instruct the model to:

* Identify rows where the structural name is missing, unclear, generic, or not explicitly linked to the compound ID.
* Search the patent text, especially preparation examples, synthesis examples, compound lists, and experimental sections.
* Correct structural names only when the patent text clearly supports the assignment.
* Preserve all original rows, compound IDs, row order, activity columns, and activity values.
* Keep `N/A` when the structural name cannot be confidently resolved.
* Output the full updated SAR table first.

### Step 7. Save the final SAR table

After Task 2 output is generated, copy the final SAR table from ChatGPT.

Save the table in one of the following formats:

```text
.csv
.xlsx
.md
.txt
```

Recommended filename format:

```text
[patent_id]_PatSAR_output.csv
```

Example:

```text
WO2020123456A1_PatSAR_output.csv
```

Recommended output folder:

```text
outputs/chatgpt_web/
```

### Step 8. Manual expert review

The PatSAR output should be treated as a structured extraction aid rather than a final expert-curated dataset.

After model extraction, manually review the SAR table against the source patent PDF. Particular attention should be paid to:

* Whether each compound ID is correctly linked to the activity value.
* Whether structural names are explicitly supported by the patent text.
* Whether activity values and units are preserved correctly.
* Whether multiple endpoints for the same compound are represented correctly.
* Whether non-SAR entities, such as intermediates or reagents, were incorrectly included.
* Whether any SAR-relevant compounds were omitted.

Any manual correction should be documented.

## 5. Summary of the web/desktop workflow

The full workflow can be summarized as:

```text
Log in to ChatGPT
→ Start a new chat
→ Upload one patent PDF
→ Enter Task 1 prompt
→ Obtain initial SAR table
→ Enter Task 2 prompt
→ Obtain corrected SAR table
→ Copy or download the table
→ Save output and extraction metadata
→ Perform manual expert review
```
