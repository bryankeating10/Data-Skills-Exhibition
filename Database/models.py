from sqlalchemy import Column, Integer, Float, \
    String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime, UTC

from base import Base

class Player(Base):
    __tablename__ = "player"

    # Identifier data
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(UTC))

    # Relationship data
    games = relationship("Game", back_populates="player", cascade="all, delete")

class Game(Base):
    __tablename__ = "game"

    # Identifier data
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, nullable=False)
    player_id = Column(Integer, ForeignKey("player.id"),nullable=False)

    # Relationship data
    player = relationship("Player", back_populates="games")

    # Game Metadata
    event = Column(String)
    site = Column(String)
    date = Column(String)
    variant = Column(String)
    tournament = Column(String)
    round = Column(String)
    white = Column(String)
    black = Column(String)
    time_control = Column(String)
    result = Column(String)
    termination = Column(String)
    link = Column(String)

    # Opening classification
    eco = Column(String)
    eco_url = Column(String)

    # DateTime
    utc_date = Column(String)
    utc_time = Column(String)
    start_time = Column(String)
    end_date = Column(String)
    end_time = Column(String)
    timezone = Column(String)

    # Ratings
    white_elo = Column(Integer)
    black_elo = Column(Integer)

class Move(Base):
    __tablename__ = "move"

    # Identifier and relationship data
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey("game.id"), nullable=False)
    game = relationship("Game")

    # Move data
    ply = Column(Integer)
    color = Column(String)
    move = Column(String)
    clock = Column(String)
    eval = Column(String)
    fen = Column(Text)

class GameDerived(Base):
    __tablename__ = 'game_derived'

    id = Column(Integer, primary_key = True)

    game_id = Column(
        Integer, 
        ForeignKey("game.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
        index=True
    )

    # Rating
    elo_diff = Column(Integer)

    # Relationship
    game = relationship("Game")

class MoveDerived(Base):
    __tablename__ = 'move_derived'

    id = Column(Integer,primary_key=True)

    move_id = Column(
        Integer,
        ForeignKey("Move.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
        index=True
    )
    
    # Time
    move_time_self = Column(Float) # Time since last move played by self
    reaction_time = Column(Float) # Reaction time to opponent move

    # Relationship
    move = relationship("Move")