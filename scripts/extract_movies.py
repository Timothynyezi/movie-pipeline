import pandas as pd
from pathlib import Path

RAW_PATH= Path("data/raw/movies.csv")
PROCESSED_DIR = Path("data/processed")
PROCESSED_PATH = PROCESSED_DIR / "movies_processed.csv"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

if RAW_PATH.exists():
    print(f"Found raw file: {RAW_PATH}")
    df = pd . read_csv(RAW_PATH)

    df.dropna(subset=["title"], inplace=True)
    df.to_csv(PROCESSED_PATH, index=False)
    print(f"Saved processed file to: {PROCESSED_PATH}")
else:
    print(f"Raw file not found:  {RAW_PATH}")