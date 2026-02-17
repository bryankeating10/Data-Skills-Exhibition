"""
Title:
    Docstring for Database.insert_games

Description:
    Inserts a metadata dataframe into the Meta table in Postgres

Usage:
    from session import session
    insert_games(session, metadata_df, player_id)

Output:
    None
"""

from Database.models import Meta

def insert_games(session, metadata_df, player_id):
    games = []

    print('COLUMNS')
    print(metadata_df.columns)

    for _, row in metadata_df.iterrows():
        game = Meta(
            # Identifier
            game_id=int(row["game_id"]),
            player_id=player_id,

            # Metadata
            event=row.get("Event"),
            site=row.get("Site"),
            date=row.get("Date"),
            variant=row.get("Variant"),
            tournament=row.get("Tournament"),
            round=row.get("Round"),
            white=row.get("White"),
            black=row.get("Black"),
            time_control=row.get("TimeControl"),
            result=row.get("Result"),
            termination=row.get("Termination"),
            link=row.get("Link"),

            # Opening
            eco=row.get("ECO"),
            eco_url=row.get("ECOUrl"),

            # DateTime
            utc_date=row.get("UTCDate"),
            utc_time=row.get("UTCTime"),
            start_time=row.get("StartTime"),
            end_date=row.get("EndDate"),
            end_time=row.get("EndTime"),
            timezone=row.get("Timezone"),

            # Ratings
            white_elo=row.get("WhiteElo"),
            black_elo=row.get("BlackElo")
        )

        # Add game to games list
        games.append(game)

    session.bulk_save_objects(games)
    session.flush()