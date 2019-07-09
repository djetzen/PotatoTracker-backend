from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Table,
    create_engine,
    MetaData,
    Float,
    ForeignKey,
)


def create_tables():
    engine = create_engine("sqlite:///database.db")
    metadata = MetaData(engine)

    user_table = Table(
        "user",
        metadata,
        Column("user_id", Integer, primary_key=True),
        Column("name", String),
    )

    purchase_table = Table(
        "purchase",
        metadata,
        Column("purchase_id", Integer, primary_key=True),
        Column("user_id", Integer, ForeignKey("user.user_id")),
    )
    element_table = Table(
        "element",
        metadata,
        Column("element_id", Integer, primary_key=True),
        Column("name", String),
        Column("amount", Float),
        Column("price", Float),
    )

    purchase_element_table = Table(
        "purchase_element",
        metadata,
        Column(
            "purchase_id", Integer, ForeignKey("purchase.purchase_id"), primary_key=True
        ),
        Column(
            "element_id", Integer, ForeignKey("element.element_id"), primary_key=True
        ),
        Column("already_bought", Boolean),
    )

    metadata.create_all()
    return engine
