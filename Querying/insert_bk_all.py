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

def create_player(session, username:str):
    player = session.query(Player).filter_by(username=username).first()

    if not player:
        player = Player(username=username)
        session.add(player)
        session.flush()

    return player

def insert_games(session,metadata_df, player_id):
    games = []

    for _, row in metadata_df.iterrows():
        game = Game(
            game_id=row['game_id'],
            player_id=player_id
        )