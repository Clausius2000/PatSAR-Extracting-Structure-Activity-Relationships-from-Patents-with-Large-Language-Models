This folder contains the code and source data used for metadata extraction and figure reproduction in the PatSAR manuscript.

## Files

- `bigquery_patent_metadata_extraction.sql`: BigQuery SQL script used to extract patent metadata.
- `figure2_plot.py`: Python script used to reproduce Figure 2.
- `figure3_plot.py`: Python script used to reproduce Figure 3.

The scripts were developed with assistance from an AI language model and reviewed by the authors.

## Runtime environment

The main PatSAR extraction workflow was performed through the ChatGPT web interface and did not require local model deployment, model fine-tuning, or a project-specific virtual environment.

The Python environment is only required for reproducing Figure 2 and Figure 3. The figure scripts were tested with Python 3 and require the packages listed in `requirements.txt`.

To install the required Python packages, run:

```bash
pip install -r requirements.txt
