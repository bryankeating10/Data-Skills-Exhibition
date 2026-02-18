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

def preview_moves(session, game_id, limit=10):
    print(f"\n--- First {limit} Moves for Game {game_id} ---")

    stmt = (
        select(Move)
        .where(Move.game_id == game_id)
        .order_by(Move.ply)
        .limit(limit)
    )

    moves = session.scalars(stmt).all()

    for move in moves:
        print(
            f"Ply {move.ply} | "
            f"{move.color} played {move.move} | "
            f"Eval: {move.eval}"
        )

def main():
    with SessionLocal() as session:
        preview_players(session)
        preview_games(session)

        # Preview first game's moves
        first_game_id = session.scalar(
            select(Meta.game_id).limit(1)
        )

        if first_game_id:
            preview_moves(session, first_game_id)

if __name__ == '__main__':
    main()