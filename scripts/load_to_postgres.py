import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parent[1]
RAW = BASE / "data" / "raw" / "movies.csv"
PROC = BASE / "data" / "processed" / "movies_processed.csv"
PROC.parent.mkdir(parents=True, exist_ok=True)

def categorize_rating(r):
    if pd.isna(r):
        return None
    r = float(r)
    if r >= 8.5:
        return "high"
    if r >= 7.0:
        return "medium"
    return "low"

def main():
    pass