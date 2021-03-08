from typing import List


from backend.db.scheme import ElementEntity
from backend.domain.element import Element


class ElementMapper:
    def to_element(self, entity: ElementEntity) -> Element:
        mapped_element = Element()
        mapped_element.user_name = entity.user_name
        mapped_element.purchase_id = entity.purchase_id
        mapped_element.bought = entity.bought
        mapped_element.name = entity.name
        mapped_element.price = entity.price
        mapped_element.amount = entity.amount
        return mapped_element

    def to_element_entity(self, domain: Element) -> ElementEntity:
        mapped_entity = ElementEntity()
        mapped_entity.user_name = domain.user_name
        mapped_entity.purchase_id = domain.purchase_id
        mapped_entity.bought = domain.bought
        mapped_entity.name = domain.name
        mapped_entity.price = domain.price
        mapped_entity.amount = domain.amount
        return mapped_entity

    def to_elements(self, entities: List[ElementEntity]) -> List[Element]:
        results = []

        for entity in entities:
            result = self.to_element(entity)
            results.append(result)

        return results
