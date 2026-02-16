# Dependencies
from pathlib import Path
import pandas as pd

# Database interaction modules
from Database.session import SessionLocal
from Database.models import Player, Game, Move

# Static path variables
PROJECT_ROOT = Path(__file__).resolve().parents[1]
METADATA_PATH = PROJECT_ROOT / "Data" / "Gold" / "bkchessm_metadata.csv"
MOVEDATA_PATH = PROJECT_ROOT / "Data" / "Gold" / "bkchessm_moves_gold.csv"

