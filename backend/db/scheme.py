from backend.db.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
class Purchase(Base):
    __tablename__ = "purchase"
    purchase_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.user_name"))


class User(Base):
    __tablename__ = "user"
    user_name = Column(String, primary_key=True)

    def __repr__(self):
        return "<User(name='%s')>" % (self.name)

    def __eq__(self, value):
        return self.user_name==value.user_name  


class Element(Base):
    __tablename__ = "element"
    element_id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Float)
    price = Column(Float)

