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