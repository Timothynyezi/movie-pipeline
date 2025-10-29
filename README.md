# Movie Data Engineering Pipeline

## Project Overview

This project demonstrates an end-to-end data engineering pipeline for movie data. The pipeline covers the main stages of a typical ETL (Extract, Transform, Load) workflow:

1. **Extract**: Load raw movie data from a CSV file.
2. **Transform**: Clean, normalize, and enrich the data.
3. **Load**: Store the processed data into a PostgreSQL database for querying and analysis.

This project is designed for learning purposes and can be extended to include APIs, orchestration tools like Airflow, and visualization dashboards.

---

## Project Structure

movie-pipeline/
│
├── data/
│ ├── raw/ # Raw movie data CSVs
│ └── processed/ # Transformed data ready to load into database
│
├── scripts/
│ ├── extract_movies.py # Script to load raw CSV files
│ ├── transform_movies.py # Script to clean and process data
│ └── load_to_postgres.py # Script to load processed data into PostgreSQL
│
├── .env # Environment variables for database connection
├── requirements.txt # Python dependencies
└── README.md # Project documentation

# Prerequisites

- Docker and Docker Compose (for running PostgreSQL)
- Python 3.9+ and pip
- PostgreSQL database (can be run in Docker)
- Basic familiarity with Python and SQL

---

