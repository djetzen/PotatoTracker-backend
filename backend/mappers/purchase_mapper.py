from typing import List

from mapper.object_mapper import ObjectMapper

from backend.db.scheme import PurchaseEntity, ElementEntity
from backend.domain.element import Element
from backend.domain.purchase import Purchase


class PurchaseMapper:
    def __init__(self):
        self.__mapper = ObjectMapper()
        self.__mapper.create_map(PurchaseEntity, Purchase)
        self.__mapper.create_map(Purchase, PurchaseEntity)

    def to_purchase(self, entity: PurchaseEntity) -> Purchase:
        return self.__mapper.map(entity, Purchase)

    def to_purchase_entity(self, domain: Purchase) -> PurchaseEntity:
        return self.__mapper.map(domain, PurchaseEntity)

    def to_purchases(self, entities: List[PurchaseEntity]) -> List[Purchase]:
        results = []

        for entity in entities:
            result = self.__mapper.map(entity, Purchase)
            results.append(result)

        return results