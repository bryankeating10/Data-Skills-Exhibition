"""
Title:
    Docstring for Pipelines.ingest

Description:
    Function for download from Chess.com into MetaData and MoveData classes,
    backing up the information in /Data

Usage:
    ingest('bkchessmaster2')
        or
    ingest('bkchessmaster2', start_date='2024-01', end_date='2024-12')

Output:
    Populated MetaData and MoveData classes
"""
# Dependencies
import requests
from pathlib import Path

# Ingestion modules
from Ingestion.download_pgn import download_pgn
from Ingestion.metadata import MetaData
from Ingestion.movedata import MoveData

def ingest(username: str, start_date: str, end_date: str):

    # Download PGN games
    download_pgn(username, start_date, end_date)
    pgn_loc = f'Data/PGN/{username}.pgn'

    # Extract data from PGN file
    meta_parser = MetaData(pgn_loc)
    move_parser = MoveData(pgn_loc)

    # Save as backup
    meta_df = meta_parser.df
    meta_df.to_csv(f'Data/Gold/{username}.csv')
    move_df = move_parser.df
    move_df.to_csv(f'Data/Pre-Eval/{username}.csv')

    return meta_df, move_df

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        ingest(sys.argv[1])
        print("\nIngestion for {username} complete.\n")
    else:
        print("Usage: python -m ingest <username> \nor \n" \
        "ingest('bkchessmaster2', start_date='2024-01', end_date='2024-12')")