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