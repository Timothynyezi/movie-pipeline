from pathlib import Path
import shutil
import argparse

RAW_DIR =  Path(__file__).resolve().parents[1] / "data" / "raw"

def main(src=None):
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    if src:
        pass