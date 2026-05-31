#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Random selection script for constructing PatSAR-GenTest-200.

This script was developed with assistance from an AI language model and was reviewed
and adapted by the authors.

This script is designed for CSV files exported from Google Patents.

Google Patents CSV structure:
- Row 1: search URL
- Row 2: column headers
- Row 3 onward: patent records

Only the "id" column is used for random selection.

Workflow:
1. Read each target-specific Google Patents CSV file.
2. Skip the first row because it contains the search URL.
3. Extract the "id" column.
4. Remove empty and duplicated patent IDs.
5. Assign a random score to each patent.
6. Rank patents by random score within each target.
7. Select the top 20 patents for each target.
8. Save only the final selected patent list.
"""

from pathlib import Path
import pandas as pd
import numpy as np


INPUT_DIR = Path("randomization/input")
OUTPUT_DIR = Path("randomization/output")

ID_COLUMN = "id"
N_PER_TARGET = 20
RANDOM_SEED = 20250801


def read_google_patents_csv(file_path):
    df = pd.read_csv(file_path, skiprows=1)

    if ID_COLUMN not in df.columns:
        raise ValueError(f"Column '{ID_COLUMN}' not found in file: {file_path}")

    df = df[[ID_COLUMN]].copy()
    df[ID_COLUMN] = df[ID_COLUMN].astype(str).str.strip()

    df = df[
        (df[ID_COLUMN].notna()) &
        (df[ID_COLUMN] != "") &
        (df[ID_COLUMN].str.lower() != "nan")
    ].copy()

    df = df.drop_duplicates(subset=[ID_COLUMN], keep="first")

    return df


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    all_records = []
    csv_files = sorted(INPUT_DIR.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {INPUT_DIR}")

    for file_path in csv_files:
        target = file_path.stem

        df = read_google_patents_csv(file_path)
        df["target"] = target
        all_records.append(df)

    candidate_df = pd.concat(all_records, ignore_index=True)

    candidate_df = candidate_df.sort_values(
        by=["target", ID_COLUMN],
        ascending=[True, True]
    ).reset_index(drop=True)

    rng = np.random.default_rng(RANDOM_SEED)
    candidate_df["random_score"] = rng.random(len(candidate_df))

    candidate_df = candidate_df.sort_values(
        by=["target", "random_score"],
        ascending=[True, False]
    ).reset_index(drop=True)

    candidate_df["random_rank_within_target"] = (
        candidate_df.groupby("target").cumcount() + 1
    )

    selected_df = candidate_df[
        candidate_df["random_rank_within_target"] <= N_PER_TARGET
    ].copy()

    selected_df = selected_df[
        ["target", ID_COLUMN, "random_score", "random_rank_within_target"]
    ]

    selected_output = OUTPUT_DIR / "selected_patents_GenTest200.csv"
    selected_df.to_csv(selected_output, index=False)

    print("Random selection completed.")
    print(f"Random seed: {RANDOM_SEED}")
    print(f"Number selected per target: {N_PER_TARGET}")
    print(f"Selected patent list saved to: {selected_output}")


if __name__ == "__main__":
    main()
