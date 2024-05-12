# MLOps Pipeline with Apache Airflow and DVC

This repository contains a complete MLOps pipeline that automates the process of data extraction from web sources, transformation of the data, storage in a CSV format, and version control using DVC (Data Version Control). Apache Airflow is used to orchestrate and schedule the pipeline.

## Objective

The main goal of this project is to implement a robust MLOps pipeline to automate the extraction of news articles from [Dawn](https://www.dawn.com) and [BBC](https://www.bbc.com), preprocess the text data, and store this data in a version-controlled manner using DVC, with all operations scheduled and managed by Apache Airflow.

## Project Structure

- `data_extraction.py`: Script to scrape the landing pages of Dawn and BBC to extract news articles.
- `data_storage.py`: Script to save the extracted data into a CSV file and manage version control with DVC.
- `airflow_dag.py`: Apache Airflow DAG configuration file to schedule and run the data extraction and storage tasks.
- `README.md`: Documentation providing an overview, setup guide, and usage instructions.

## Setup Instructions

### Prerequisites

- Python 3.6, 3.7, or 3.8
- Apache Airflow 2.x
- DVC
- Access to Google Drive for storage (configured with DVC)

### Installing Dependencies

1. **Python and Pip:**
   Ensure Python and pip are installed. You can download Python from [python.org](https://www.python.org/downloads/) and install pip by running `python -m ensurepip`.

2. **Virtual Environment:**
   It's recommended to use a virtual environment to manage dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
