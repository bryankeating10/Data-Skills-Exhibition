"""
Title:
    Database Preview Queries

Description:
    Read-only inspection queries for Player, Meta, and Move tables.

Usage:
    python -m Query.preview
"""

from sqlalchemy import select, func

from Database.session import SessionLocal
from Database.models import Player, Meta, Move

def preview_players(session):
    print("\n--- Players ---")

    stmt = select(Player)
    players = session.scalars(stmt).all()

    for player in players:
        print(
            f"ID: {player.player_id} | "
            f"Username: {player.username} | "
            f"Created: {player.created_at}"
        )

def preview_games(session):
    stmt = select(Meta)
    games = session.scalars(stmt).all()

    for game in games:
        print(
            f'ID: {game.game_id} | '
            f'Between {game.white} and {game.black} | ' 
        )



def main():
    with SessionLocal() as session:
        preview_players(session)

if __name__ == '__main__':
    main()