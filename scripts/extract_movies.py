from pathlib import Path
import shutil
import argparse

RAW_DIR =  Path(__file__).resolve().parents[1] / "data" / "raw"

def main(src=None):
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    if src:
        dest = RAW_DIR / "movies.csv"
        shutil.copy(src, dest)
        print(f"Copied {src} -> {dest}")
    else:
        candidate = RAW_DIR / "movies.csv"
        if candidate.exists():
            print(f"Found raw file: {candidate}")
        else:
            raise SystemExit("No raw movies.csv found. Put one at data/raw/movies.csv or pass --src")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", help="path to csv to copy into raw folder")
    args = parser.parse_args()
    main(args.src)