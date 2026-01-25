from Ingestion.download_pgn import download_pgn
from Ingestion.metadata import MetaData
from Ingestion.movedata import MoveData

# USERNAME
username = 'bkchessmaster2'
trunc_usr = username.lower()[:8] # Truncate to 8 characters for filename

# Download PGN games for user 'bkchessmaster2' from Jan 2026 onwards
download_pgn(username, start_date='2026-01')

# Extract metadata from PGN file
bk_meta = MetaData(f'Data/Bronze/{trunc_usr}.pgn')

# Save metadata to CSV
bk_meta.save_csv(f'Data/Silver/{trunc_usr}_metadata.csv')

# Extract move data from PGN file
bk_moves = MoveData(f'Data/Bronze/{trunc_usr}.pgn')

# Save move data to CSV
bk_moves.save_csv(f'Data/Silver/{trunc_usr}_moves.csv')