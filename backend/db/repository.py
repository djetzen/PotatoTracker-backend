from backend.db.scheme import User
from sqlalchemy import Table, MetaData
from backend import engine
from sqlalchemy.orm import sessionmaker


class Repository:
    def __init__(self, engine):
        self.__engine = engine

    def save_user(self, user_name: str):
        Session = sessionmaker(bind=self.__engine)
        session=Session()
        user = User(user_name=user_name)
        session.add(user)
        session.commit()

    def find_user(self, user_name: str) -> str:
        Session = sessionmaker(bind=self.__engine)
        session=Session()
        user = User(user_name=user_name)
        return session.query(User).filter_by(user_name=user_name).first()


repository_impl = Repository(engine)
