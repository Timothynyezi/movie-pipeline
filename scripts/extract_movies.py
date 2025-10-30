import pandas as pd
from pathlib import Path

RAW = Path("data/raw/movies.csv")
PROCESSED_DIR = Path("data/processed")
PROCESSED_PATH = PROCESSED_DIR / "movies_processed.csv"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

