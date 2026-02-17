from models import Player

def create_player(session, username:str):
    player = session.query(Player).filter_by(username=username).first()

    if not player:
        player = Player(username=username)
        session.add(player)
        session.flush()

    return player