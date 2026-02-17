"""
Title:
    Docstring for Database.insert_games

Description:
    Inserts a move dataframe into the Move table in Postgres

Usage:
    from session import session
    insert_moves(session, move_df)

Output:
    None
"""

from Database.models import Move

def insert_moves(session, moves_df):
    moves = []

    for move_id, row in moves_df.iterrows():
        move = Move(
            # Identifiers
            move_id=int(move_id),
            game_id=int(row["game_id"]),

            # Move data
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