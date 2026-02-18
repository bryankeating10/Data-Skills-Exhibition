from sqlalchemy import select
from Database.session import SessionLocal
from Database.models import Meta

def unique_time_controls():
    with SessionLocal() as session:
        stmt = select(Meta.time_control).distinct()
        result = session.execute(stmt)
        return result.scalars().all()
    
if __name__ == '__main__':
    time_controls = unique_time_controls()
    print(time_controls)