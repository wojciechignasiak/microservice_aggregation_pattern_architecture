
import os
from sqlalchemy.engine import create_engine
from app.models.database_model import Base

postgres_user = os.environ.get("POSTGRES_USER")
postgres_password = os.environ.get("POSTGRES_PASSWORD")

def db_connect_and_init():
        engine = create_engine(f"postgresql+psycopg://{postgres_user}:{postgres_password}@postgres:5432")
        print("Postgres connected")
        Base.metadata.create_all(engine)
        print("Schema initialized")

