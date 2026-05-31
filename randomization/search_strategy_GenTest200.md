# Search Strategy for Constructing PatSAR-GenTest-200

This document describes the Google Patents search strategy used to retrieve candidate patents for constructing PatSAR-GenTest-200.

## 1. Search objective

The purpose of the search was to retrieve recent target-related patent documents containing small-molecule SAR-relevant information. The retrieved candidate patents were then used for eligibility screening and randomized selection.

## 2. Search source

Candidate patents were retrieved from Google Patents.

## 3. Search period

The priority date was restricted to patents with priority dates after January 1, 2020 and before August 1, 2025.

```text
after:priority:20200101 before:priority:20250801
```

## 4. General search template

For each target, the following query structure was used:

```text
AB=("TARGET") (AB=(antagonist) OR AB=(inhibitor)) (IC50) after:priority:20200101 before:priority:20250801
```

In this query, `TARGET` represents the target name used for retrieval.

## 5. Query logic

The search strategy was designed to identify patent documents in which:

* the target name appeared in the abstract;
* the abstract contained activity-related pharmacological terms, including `antagonist` or `inhibitor`;
* the document contained the activity-related term `IC50`;
* the priority date fell within the predefined time window from January 1, 2020 to August 1, 2025.

The intended logical structure was:

```text
Abstract contains TARGET
AND
(Abstract contains antagonist OR Abstract contains inhibitor)
AND
Document contains IC50
AND
Priority date is between 2020-01-01 and 2025-08-01
```

## 6. Target-specific queries

The same search template was applied to each target by replacing `TARGET` with the corresponding target name.

### ALK

```text
AB=("ALK") (AB=(antagonist) OR AB=(inhibitor)) (IC50) after:priority:20200101 before:priority:20250801
```

### BTK

```text
AB=("BTK") (AB=(antagonist) OR AB=(inhibitor)) (IC50) after:priority:20200101 before:priority:20250801
```

### CDK

```text
AB=("CDK") (AB=(antagonist) OR AB=(inhibitor)) (IC50) after:priority:20200101 before:priority:20250801
```

### c-MET

```text
AB=("c-MET") (AB=(antagonist) OR AB=(inhibitor)) (IC50) after:priority:20200101 before:priority:20250801
```

### EGFR

```text
AB=("EGFR") (AB=(antagonist) OR AB=(inhibitor)) (IC50) after:priority:20200101 before:priority:20250801
```

### GLP-1

```text
AB=("GLP-1") (AB=(antagonist) OR AB=(inhibitor)) (IC50) after:priority:20200101 before:priority:20250801
```

### HER2

```text
AB=("HER2") (AB=(antagonist) OR AB=(inhibitor)) (IC50) after:priority:20200101 before:priority:20250801
```

### IL-17A

```text
AB=("IL-17A") (AB=(antagonist) OR AB=(inhibitor)) (IC50) after:priority:20200101 before:priority:20250801
```

### KRAS

```text
AB=("KRAS") (AB=(antagonist) OR AB=(inhibitor)) (IC50) after:priority:20200101 before:priority:20250801
```

### PD-L1

```text
AB=("PD-L1") (AB=(antagonist) OR AB=(inhibitor)) (IC50) after:priority:20200101 before:priority:20250801
```

## 7. Candidate patent export

For each target-specific query, the Google Patents search results were exported as a CSV file.

The exported CSV files were used as the input files for the random-selection script. Only the patent `id` column from each exported CSV file was used for randomization.

## 8. Randomized selection

After retrieval, candidate patent IDs were processed using the random-selection script provided in this repository. For each target-specific candidate pool, patent IDs were assigned random scores using a fixed random seed, ranked in descending order by random score, and the top 20 patents were selected for inclusion in PatSAR-GenTest-200.

The resulting selected patent list is provided as:

```text
selected_patents_GenTest200.csv
```
