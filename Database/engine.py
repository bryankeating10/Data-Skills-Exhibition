import os
from sqlalchemy import create_engine

DATABASE_URL = 'postgres+psycopy://chessuser:chess@db:5432/database'

engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True,
    pool_pre_ping=True
)