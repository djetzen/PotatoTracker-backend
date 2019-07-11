from backend.db.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class Purchase(Base):
    __tablename__ = "purchase"
    purchase_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    elements = relationship("Element", back_populates="purchase")

    def __eq__(self, value):
        return (
            self.purchase_id == value.purchase_id and self.user_name == value.user_name
        )


class Element(Base):
    __tablename__ = "element"
    element_id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Float)
    price = Column(Float)
    user_name = Column(String)
    bought = Column(Boolean)
    purchase_id = Column(Integer, ForeignKey("purchase.purchase_id"))
    purchase = relationship("Purchase", back_populates="elements")

    def __repr__(self):
        return (
            "Element<element_id:"
            + str(self.element_id)
            + ", name: "
            + str(self.name)
            + ", amount: "
            + str(self.amount)
            + ", price:"
            + str(self.price)
            + ", user_name:"
            + str(self.user_name)
            + ", bought: "
            + str(self.bought)
            + ", purchase_id: "
            + str(self.purchase_id)+">"
        )
