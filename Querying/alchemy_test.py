from database import SessionLocal
from models import Move

db = SessionLocal()

moves = db.query(Move).filter(Move.game_id == 1).all()

for m in moves[:10]:
    print(f"Ply: {m.ply}, Move: {m.move}")