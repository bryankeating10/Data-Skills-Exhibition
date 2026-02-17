from sqlalchemy import Column, Integer, Float, \
    String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime, UTC

from base import Base

class Player(Base):
    __tablename__ = "player"

    # Identifier data
    player_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(UTC))

    # Relationship data
    games = relationship("Meta", back_populates="player", cascade="all, delete")

class Meta(Base):
    __tablename__ = "meta"

    # Identifier data
    game_id = Column(Integer, nullable=False)
    player_id = Column(Integer, ForeignKey("player.player_id"),nullable=False)

    # Relationship data
    player = relationship("Player", back_populates="meta")

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
    move_id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey("meta.id"), nullable=False)
    meta = relationship("Meta")

    # Move data
    ply = Column(Integer)
    color = Column(String)
    move = Column(String)
    clock = Column(String)
    eval = Column(String)
    fen = Column(Text)

class MetaDerived(Base):
    __tablename__ = 'meta_derived'

    game_id = Column(
        Integer, 
        ForeignKey("meta.id", ondelete="CASCADE"),
        primary_key=True
    )

    # Rating
    elo_diff = Column(Integer)

    # Relationship
    meta = relationship("Meta")

class MoveDerived(Base):
    __tablename__ = 'move_derived'

    move_id = Column(
        Integer,
        ForeignKey("Move.move_id", ondelete="CASCADE"),
        primary_key=True
    )
    
    # Time
    move_time_self = Column(Float) # Time since last move played by self
    reaction_time = Column(Float) # Reaction time to opponent move

    # Relationship
    move = relationship("Move")