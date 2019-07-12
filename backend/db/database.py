from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import SingletonThreadPool

Base = declarative_base()

from backend.db.scheme import PurchaseEntity, ElementEntity


def create_database(db_path) -> engine:
    engine = create_engine(db_path, connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)
    return engine
