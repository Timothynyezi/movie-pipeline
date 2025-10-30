import pandas as pd
from pathlib import Path

RAW_PATH= Path("data/raw/movies.csv")
PROCESSED_DIR = Path("data/processed")
PROCESSED_PATH = PROCESSED_DIR / "movies_processed.csv"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

if RAW_PATH.exists():
    print(f"Found raw file: {RAW_PATH}")
    df = pd . read_csv(RAW_PATH)
    
