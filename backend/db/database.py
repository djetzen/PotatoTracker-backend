from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from backend.db.scheme import Purchase, Element


def create_database(db_path) -> engine:
    engine = create_engine(db_path)
    Base.metadata.create_all(engine)
    return engine
