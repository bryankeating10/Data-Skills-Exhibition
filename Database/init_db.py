from Database.base import Base
from Database.engine import engine
from Database import models  # VERY IMPORTANT (ensures models are registered)

def init_db():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()
