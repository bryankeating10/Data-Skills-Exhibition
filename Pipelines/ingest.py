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

# 