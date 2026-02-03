from sqlalchemy import Column, Integer, String, Float
from database import Base

class Move(Base):
    __tablename__ = 'stak1_game_data'

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer)
    ply = Column(Integer)
    color = Column(String)
    move = Column(String)
    clock = Column(String)
    eval = Column(Float)
    fen = Column(String)


    white = Column(String)
    black = Column(String)
    result = Column(String)

    eco = Column(String)
    eco_url = Column(String)

    utc_date = Column(String)
    white_elo = Column(Integer)
    black_elo = Column(Integer)

    time_control = Column(String)
    termination = Column(String)

    start_time = Column(String)
    end_date = Column(String)
    end_time = Column(String)