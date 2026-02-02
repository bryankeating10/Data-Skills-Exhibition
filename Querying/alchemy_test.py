import os
from sqlalchemy import create_engine, Column, Integer, String, Float

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

from sqlalchemy.orm import sessionmaker, declarative_base
from database import Base

class Move(Base):
    __tablename__ = "moves"
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