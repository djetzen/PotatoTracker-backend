from backend.db.repository import repository_impl
from backend.db.scheme import ElementEntity
from backend.domain.element import Element
from backend.mappers.element_mapper import ElementMapper
from typing import List
from backend.db.repository import repository_impl

class ElementService:
    def __init__(self, repository_impl):
        self.__repository = repository_impl
        self.mapper = ElementMapper()

    def get_all_elements(self):
        self.__repository.find_all_elements()

    def create_new_element(self,element: Element):
        self.__repository.create_new_element(element)

    def find_elements_by_name(self,element_name: str):
        self.__repository.find_all_elements_by_name(element_name)

    def find_elements_by_user(self,user_name: str):
        self.__repository.find_all_elements_for_user(user_name)

    def find_bought_elements_by_user(self,user_name: str):
        self.__repository.find_only_bought_elements_by_user(user_name)

    def find_elements_by_purchase_id(self, purchase_id: int):
        self.__repository.find_all_elements_by_purchase_id(purchase_id)

    def buy_elements(self, elements: List[ElementEntity]):
        self.__repository.buy_elements(elements)

element_service_impl = ElementService(repository_impl)