"""
Description:
    Testing database insert without evaluating positions

Usage:
    python -m no_eval.py    
"""

from Pipelines.ingest import ingest
from Pipelines.insert import insert

# Chess.com username and time frame
USERNAME = 'bkchessmaster2'
START_DATE = '2026-01'
END_DATE = '2026-02'

# Ingestion
meta_df, move_df = ingest(USERNAME)

# Database insertion
insert(meta_df, move_df, USERNAME)