"""
Title:
    Docstring for Pipelines.insert

Description:
    Function for insertion of all meta and move data from a session
    into Postgres database

Usage:
    insert(meta_df,move_df,'bkchessmaster2')

Output:
    None
"""

# Insertion modules
from Database.session import SessionLocal
from Database.init_db import init_db
from Database.create_player import create_player
from Database.insert_games import insert_games
from Database.insert_moves import insert_moves

def insert(meta_df, move_df, username: str):

    # Ensure tables exist
    init_db()

    session = SessionLocal()
    
    # Create player
    player = create_player(session, username)

    # Insert games
    insert_games(session, meta_df, player.player_id)

    # Insert moves
    insert_moves(session, move_df)

    session.commit()
    session.close()
    
    print("✅ Data inserted successfully.")