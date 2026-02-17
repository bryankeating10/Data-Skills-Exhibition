"""
Docstring for Pipelines.insert

Insert data from MetaData and MoveData classes into Postgres database.

"""

# Dependencies
from pathlib import Path
import pandas as pd

# Database interaction modules
from Database.session import SessionLocal
from Database.models import Player, Meta, Move

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

def insert_games(session, metadata_df, player_id):
    games = []

    for _, row in metadata_df.iterrows():
        game = Meta(
            # Identifier
            game_id=int(row["game_id"]),
            player_id=player_id,

            # Metadata
            event=row.get("Event"),
            site=row.get("Site"),
            date=row.get("Date"),
            variant=row.get("Variant"),
            tournament=row.get("Tournament"),
            round=row.get("Round"),
            white=row.get("White"),
            black=row.get("Black"),
            time_control=row.get("TimeControl"),
            result=row.get("Result"),
            termination=row.get("Termination"),
            link=row.get("Link"),

            # Opening
            eco=row.get("ECO"),
            eco_url=row.get("ECOUrl"),

            # DateTime
            utc_date=row.get("UTCDate"),
            utc_time=row.get("UTCTime"),
            start_time=row.get("StartTime"),
            end_date=row.get("EndDate"),
            end_time=row.get("EndTime"),
            timezone=row.get("Timezone"),

            # Ratings
            white_elo=row.get("WhiteElo"),
            black_elo=row.get("BlackElo"),
        )

        # Add game to games list
        games.append(game)

    
    session.bulk_save_objects(games)
    session.flush()

    # Build mapping from external game_id → database id
    db_games = session.query(Meta.id, Meta.game_id).filter_by(player_id=player_id).all()
    return {game_id: db_id for db_id, game_id in db_games}

def insert_moves(session, moves_df, game_id_map):
    moves = []

    for _, row in moves_df.iterrows():
        db_game_id = game_id_map.get(int(row['game_id']))

        if not db_game_id:
            continue
        move = Move(
            game_id=db_game_id,
            ply=row.get("Ply"),
            color=row.get("Color"),
            move=row.get("Move"),
            clock=row.get("Clock"),
            eval=row.get("Eval"),
            fen=row.get("FEN"),
        )

        # Add move to moves list
        moves.append(move)

    session.bulk_save_objects(moves)

if __name__ == "__main__":
    session = SessionLocal()

    try:
        metadata_df = pd.read_csv(METADATA_PATH)
        moves_df = pd.read_csv(MOVEDATA_PATH)

        player = create_player(session, "bkchessm")

        game_id_map = insert_games(session, metadata_df, player.id)

        insert_moves(session, moves_df, game_id_map)

        session.commit()
        print("✅ Data inserted successfully.")

    except Exception as e:
        session.rollback()
        print("❌ Insert failed:", e)

    finally:
        session.close()