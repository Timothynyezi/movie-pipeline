from sqlalchemy import create_engine, text
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv
import os


load_dotenv()

PGHOST = os.getenv("PGHOST", "localhost")
PGPORT = os.getenv("PGPORT", "5432")
PGUSER = os.getenv("PGUSER", "postgres")
PGPASSWORD = os.getenv("PASSWORD", "docker")
PGDATABASE = os.getenv("PDGDATABASE", "movies_db")

PROC = Path(__file__).resolve().parents[1] / "data" / "processed" / "movies_processed.csv"

def engine_url():
    return f"postgressql+psycop2://{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}:{PGDATABASE}"

def main():
    if not PROC.exists():
        raise SystemExit(f"Processed file not found: {PROC}")
    df = pd.read_csv(PROC)
    eng = create_engine(engine_url(), echo=False)

    df.to_sql("movies", eng, if_exists="replace", index=False)
    print("Loaded processed data into movies table")


if __name__ == "__main__":
    main()
