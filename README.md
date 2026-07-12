# PatSAR

This repository provides prompt, workflow, and randomization materials associated with the study "Extracting Structure-Activity Relationships from Patents with Large Language Models".

PatSAR is a prompt-based workflow for extracting structure–activity relationship (SAR) information from patent PDF documents using the ChatGPT web or desktop interface.

## Data availability

The internally constructed PatSAR datasets are deposited in Zenodo:

**DOI:** 10.5281/zenodo.20482853  
**Persistent URL:** https://zenodo.org/records/20482853

All dataset files are deposited in Zenodo. This repository provides the prompt records, workflow instructions, randomization materials, metadata-extraction SQL, and figure-reproduction code associated with the manuscript.

## Repository contents

```text
PatSAR/
├── Code/
│   ├── README.md
│   ├── bigquery_patent_metadata_extraction.sql
│   ├── figure2_plot.py
│   ├── figure3_plot.py
│   └── requirements.txt
├── prompts/
│   └── prompt_development_record.md
├── randomization/
│   ├── search_strategy_GenTest200.md
│   └── random_selection_GenTest200.py
├── workflow_instructions/
│   └── workflow_instructions_chatgpt_web.md
└── README.md
```

The `Code/` folder contains the BigQuery SQL script for patent metadata extraction, Python scripts for reproducing Figure 2 and Figure 3, and the minimal Python dependency file. The `prompts/`, `randomization/`, and `workflow_instructions/` folders provide the prompt-development record, GenTest-200 randomization materials, and practical ChatGPT workflow instructions, respectively.
