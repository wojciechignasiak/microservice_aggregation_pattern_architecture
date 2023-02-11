import os
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

postgres_user = os.environ.get("POSTGRES_USER")
postgres_password = os.environ.get("POSTGRES_PASSWORD")

def session_maker():
        engine = create_engine(f"postgresql+psycopg://{postgres_user}:{postgres_password}@postgres:5432")
        print("Postgres connected")
        Session = sessionmaker(engine)
        session = Session()
        return session