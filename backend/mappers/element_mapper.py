from typing import List

from mapper.object_mapper import ObjectMapper

from backend.db.scheme import PurchaseEntity, ElementEntity
from backend.domain.element import Element
from backend.domain.purchase import Purchase


class ElementMapper:
    def __init__(self):
        self.__mapper = ObjectMapper()
        self.__mapper.create_map(ElementEntity, Element)
        self.__mapper.create_map(Element, ElementEntity)

    def to_element(self, entity: ElementEntity) -> Element:
        return self.__mapper.map(entity, Element)

    def to_element_entity(self, domain: Element) -> ElementEntity:
        return self.__mapper.map(domain, ElementEntity)

    def to_elements(self, entities: List[ElementEntity]) -> List[Element]:
        results = []

        for entity in entities:
            result = self.__mapper.map(entity, Element)
            results.append(result)

        return results
