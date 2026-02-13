from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, UTC

from base import Base

class Player(Base):
    __tablename__ = "player"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(UTC))

class Game(Base):
    __tablename__ = "game"

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("player.id"),nullable=False)



    player = relationship("Player", back_populates="games") # player.games returns a list of all games
    

    