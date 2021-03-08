from typing import List


from backend.db.scheme import PurchaseEntity, ElementEntity
from backend.domain.element import Element
from backend.domain.purchase import Purchase


class PurchaseMapper:
    def to_purchase(self, entity: PurchaseEntity) -> Purchase:
        mapped_purchase = Purchase()
        mapped_purchase.purchase_id = entity.purchase_id
        mapped_purchase.user_name = entity.user_name
        return mapped_purchase

    def to_purchase_entity(self, domain: Purchase) -> PurchaseEntity:
        mapped_entity = PurchaseEntity()
        mapped_entity.purchase_id = domain.purchase_id
        mapped_entity.user_name = domain.user_name
        return mapped_entity

    def to_purchases(self, entities: List[PurchaseEntity]) -> List[Purchase]:
        results = []

        for entity in entities:
            result = self.to_purchase(entity)
            results.append(result)

        return results
