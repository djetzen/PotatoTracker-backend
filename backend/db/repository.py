from backend.db.scheme import PurchaseEntity, ElementEntity
from backend.domain.purchase import Purchase
from backend.domain.element import Element
from backend.mappers.element_mapper import ElementMapper
from backend.mappers.purchase_mapper import PurchaseMapper
from sqlalchemy import Table, MetaData
from backend import engine
from sqlalchemy.orm import sessionmaker
from typing import List


class Repository:
    def __init__(self, engine):
        self.__engine = engine
        Session = sessionmaker(bind=self.__engine)
        self.session = Session()
        self.purchase_mapper = PurchaseMapper()
        self.elements_mapper = ElementMapper()

    def create_new_purchase(self, user_name: str):
        purchase_entity = self.__add_and_commit(PurchaseEntity(user_name=user_name))
        return purchase_entity.purchase_id

    def find_all_purchases_for_user(self, user_name: str):
        entities = (
            self.session.query(PurchaseEntity).filter_by(user_name=user_name).all()
        )
        return self.purchase_mapper.to_purchases(entities)

    def find_purchase_by_id(self, id: int):
        first_entity = (
            self.session.query(PurchaseEntity).filter_by(purchase_id=id).first()
        )
        return self.purchase_mapper.to_purchase(first_entity)

    def find_all_purchases(self):
        entities = self.session.query(PurchaseEntity).all()
        return self.purchase_mapper.to_purchases(entities)

    def find_all_elements(self):
        entities = self.session.query(ElementEntity).all()
        return self.elements_mapper.to_elements(entities)

    def create_new_element(self, element: Element):
        element_entity = self.__add_and_commit(
            self.elements_mapper.to_element_entity(element)
        )
        return self.elements_mapper.to_element(element_entity)

    def find_all_elements_by_name(self, element_name: str):
        entities = self.session.query(ElementEntity).filter_by(name=element_name).all()
        return self.elements_mapper.to_elements(entities)

    def find_all_elements_for_user(self, user_name: str):
        entities = (
            self.session.query(ElementEntity).filter_by(user_name=user_name).all()
        )
        return self.elements_mapper.to_elements(entities)

    def find_only_bought_elements_by_user(self, user_name: str):
        entities = (
            self.session.query(ElementEntity)
            .filter_by(user_name=user_name)
            .filter_by(bought=True)
            .all()
        )
        return self.elements_mapper.to_elements(entities)

    def find_only_unbought_elements_by_user(self, user_name: str):
        entities = (
            self.session.query(ElementEntity)
            .filter_by(user_name=user_name)
            .filter_by(bought=False)
            .all()
        )
        return self.elements_mapper.to_elements(entities)

    def find_all_elements_by_purchase_id(self, purchase_id: int):
        entities = (
            self.session.query(ElementEntity).filter_by(purchase_id=purchase_id).all()
        )
        return self.elements_mapper.to_elements(entities)

    def mark_as_bought(self, element: Element):
        element.bought = True
        element_entity = self.__add_and_commit(
            self.elements_mapper.to_element_entity(element)
        )
        return self.elements_mapper.to_element(element_entity)

    def buy_elements(self, elements: List[Element]):
        if not elements:
            return
        purchase_id = self.create_new_purchase(elements[0].user_name)
        entities = []
        for element in elements:
            self.mark_as_bought(element)
            element.purchase_id = purchase_id
            entities.append(
                self.__add_and_commit(self.elements_mapper.to_element_entity(element))
            )
        return self.elements_mapper.to_elements(entities)

    def __get_session(self):
        return self.session

    def __add_and_commit(self, element):
        self.session.add(element)
        self.session.commit()
        return element


repository_impl = Repository(engine)
