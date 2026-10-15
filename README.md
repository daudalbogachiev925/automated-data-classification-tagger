# Automated Data Classification and Tagging System

This repository provides a lightweight, configurable Python utility that reads a CSV file, classifies each row based on keyword rules, and adds appropriate tags. It is designed for data governance teams that need to automate data discovery and metadata enrichment.

## Features
- **Keyword‑based classification** – Define categories and associated keywords in a YAML config.
- **Automatic tagging** – Tags are appended to a new column `tags` in the output CSV.
- **CLI interface** – Simple command‑line usage.
- **Extensible** – Easily add new classifiers or integrate with other data sources.

## Quick Start
```bash
# Clone the repo
git clone https://github.com/yourusername/automated-data-classification-tagger.git
cd automated-data-classification-tagger

# Install dependencies
pip install -r requirements.txt

# Run the tool on a sample CSV
python -m src.main --input data/sample_data.csv --output data/tagged_output.csv
```

## Configuration
Edit `config.yaml` to define your own categories and keywords:
```yaml
categories:
  Finance:
    - "invoice"
    - "payment"
  HR:
    - "employee"
    - "salary"
  Marketing:
    - "campaign"
    - "lead"
```
The classifier will assign a row to the first matching category.

## Testing
```bash
pytest
```
All tests should pass.

## License
MIT License.
