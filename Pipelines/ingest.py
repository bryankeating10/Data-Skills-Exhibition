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

# Dependencies
from Ingestion.metadata import MetaData
from Ingestion.movedata import MoveData

def ingest(username: str, start_date: str, end_date: str):
    username = username.lower()

    # Set output directory
    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    backup_dir = PROJECT_ROOT / 'Data' / 'Bronze'
    backup_dir.mkdir(parents=True, exist_ok=True)

    # Archive URLs
    url = f'https://api.chess.com/pub/player/{username}/games/archives'
    headers = {'User-Agent': 'Mozilla/5.0 (Chess PGN Downloader)'}
    response = requests.get(url, headers=headers)
    archives = response.json()['archives']

