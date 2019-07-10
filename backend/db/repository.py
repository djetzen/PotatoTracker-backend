from backend.db.scheme import Purchase, Element
from sqlalchemy import Table, MetaData
from backend import engine
from sqlalchemy.orm import sessionmaker


class Repository:
    def __init__(self, engine):
        self.__engine = engine
        Session = sessionmaker(bind=self.__engine)
        self.session = Session()

    def create_new_purchase(self, user_name: str):
        purchase = Purchase(user_name=user_name)
        self.__add_and_commit(purchase)

    def find_all_purchases_for_user(self, user_name: str):
        return self.session.query(Purchase).filter_by(user_name=user_name).all()

    def find_purchase_by_id(self, id: int):
        return self.session.query(Purchase).filter_by(purchase_id=id).first()

    def find_all_purchases(self):
        return self.session.query(Purchase).all()

    def find_all_elements(self):
        return self.session.query(Element).all()

    def create_new_element(self, element: Element):
        self.__add_and_commit(element)

    def find_all_elements_by_name(self, element_name:str):
        return self.session.query(Element).filter_by(name=element_name).all()

    def find_all_elements_for_user(self, user_name:str):
        return self.session.query(Element).filter_by(user_name=user_name).all()

    def find_only_bought_elements_by_user(self, user_name:str):
        return self.session.query(Element).filter_by(user_name=user_name).filter_by(bought=True).all()

    def mark_as_bought(self, element:Element):
        element.bought=True
        return self.__add_and_commit(element)

    def __get_session(self):
        return self.session

    def __add_and_commit(self, element):
        self.session.add(element)
        self.session.commit()


repository_impl = Repository(engine)
