from backend.db.scheme import Purchase
from sqlalchemy import Table, MetaData
from backend import engine
from sqlalchemy.orm import sessionmaker


class Repository:
    def __init__(self, engine):
        self.__engine = engine

    def create_new_purchase(self, user_name:str):
        session = self.__get_session()
        purchase = Purchase(user_name=user_name)
        self.__add_and_commit(session, purchase)

    def find_all_purchases_for_user(self, user_name:str):
        session = self.__get_session()
        return session.query(Purchase).filter_by(user_name=user_name).all()

    def find_purchase_by_id(self, id: int):
         session = self.__get_session()
         return session.query(Purchase).filter_by(purchase_id=id).first()

    def find_all_purchases(self):
        session = self.__get_session()
        return session.query(Purchase).all()

    def __get_session(self):
        Session = sessionmaker(bind=self.__engine)
        session=Session()
        return session

    def __add_and_commit(self, session, element):
        session.add(element)
        session.commit()    

repository_impl = Repository(engine)
