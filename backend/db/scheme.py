from backend.db.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Purchase(Base):
    __tablename__ = "purchase"
    purchase_id = Column(Integer, primary_key=True)
    user_name = Column(String)

    def __eq__(self, value):
        return self.purchase_id==value.purchase_id and self.user_name==value.user_name

class Element(Base):
    __tablename__ = "element"
    element_id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Float)
    price = Column(Float)
    purchase_id = Column(Integer, ForeignKey("purchase.purchase_id"))
