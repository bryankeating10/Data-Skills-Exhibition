from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, UTC

from base import Base

class Player(Base):
    __tablename__ = "player"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(UTC))

    games = relationship("Game", back_populates="player")

class Game(Base):
    __tablename__ = "game"

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, nullable=False)

    player_id = Column(Integer, ForeignKey("player.id"),nullable=False)
    player = relationship("Player", back_populates="games")

    # Game Metadata
    event = Column(String)
    site = Column(String)
    date = Column(String)
    round = Column(String)
    white = Column(String)
    black = Column(String)
    result = Column(String)
    time_control = Column(String)

    # Ratings
    white_elo = Column(Integer)
    black_elo = Column(Integer)
    elo_diff = Column(Integer)

    # DateTime
    utc_date = Column(String)
    utc_time = Column(String)
    start_time = Column(String)
    end_date = Column(String)
    end_time = Column(String)
    timezone = Column(String)

    # Move Data
    ply = Column(Integer)
    color = Column(Integer)

    