# Import dependencies
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import ingestion modules
from Ingestion.download_pgn import download_pgn
from Ingestion.metadata import MetaData
from Ingestion.movedata import MoveData

# Import processing modules
from Processing.unique_fen import unique_fens
from Processing.add_eval import add_eval, repopulate_unique_evals as map_evals
from Processing.merge_game_data import merge_data

# Import database modules
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# Connection string for Docker Compose PostgreSQL service
DATABASE_URL = "postgresql+psycopg://chessuser:chess@db:5432/database"

# Test Postgres connection
def test_connection():
    try:
        engine = create_engine(DATABASE_URL) # Create engine
        with engine.connect() as conn:
            print("✅ Connected to Postgres successfully!")

    except SQLAlchemyError as e:
        print("❌ Failed to connect to Postgres:")
        print(e)

if __name__ == "__main__":
    test_connection()

# USERNAME
username = 'bkchessmaster2'

# Truncate to 8 characters for filenames
trun_usr = username.lower()[:8] 

# Download PGN games for user in specified date range
download_pgn(username)#, start_date='2023-01', end_date='2025-12')

# Extract metadata from PGN file
meta_parser = MetaData(f'Data/Bronze/{trun_usr}.pgn')

# Save metadata to CSV
meta_df = meta_parser.df
meta_df.to_csv(f'Data/Gold/{trun_usr}_metadata.csv')
print(meta_df.head())
print()

# Extract move data from PGN file
move_parser = MoveData(f'Data/Bronze/{trun_usr}.pgn')

# Save move data to CSV
move_df = move_parser.df
move_df.to_csv(f'Data/Silver/{trun_usr}_moves.csv')
print('\nMOVEDATA CHECK')
print(move_df.head())
print()

"""
# Extract unique FENs into a Series to avoid redundant evaluations
unique_fens = unique_fens(move_df)

# Evaluate unique FENs using Stockfish at depth 20
evaluated_fens = add_eval(unique_fens, depth=20)

# Map evaluations back to the original moves dataframe
move_df = map_evals(move_df, evaluated_fens)
"""

# Save final move data without evaluations
move_df.to_csv(f'Data/Gold/{trun_usr}_moves_gold.csv', index=False)

# Merge metadata and move data on 'game_id' and save final game data
game_data = merge_data(meta_df, move_df)
game_data.to_csv(f'Data/Gold/{trun_usr}_game_data_gold.csv', index=False)