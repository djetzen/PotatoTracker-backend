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


class Database:
    def __init__(self, db_path):
        self.db_path = db_path

    def create_database(self):
        self.engine = create_engine(self.db_path)
        self.metadata = MetaData(self.engine)

        user_table = Table(
            "user", self.metadata, Column("user_name", String, primary_key=True)
        )

        purchase_table = Table(
            "purchase",
            self.metadata,
            Column("purchase_id", Integer, primary_key=True),
            Column("user_id", Integer, ForeignKey("user.user_name")),
        )
        element_table = Table(
            "element",
            self.metadata,
            Column("element_id", Integer, primary_key=True),
            Column("name", String),
            Column("amount", Float),
            Column("price", Float),
        )

        purchase_element_table = Table(
            "purchase_element",
            self.metadata,
            Column(
                "purchase_id",
                Integer,
                ForeignKey("purchase.purchase_id"),
                primary_key=True,
            ),
            Column(
                "element_id",
                Integer,
                ForeignKey("element.element_id"),
                primary_key=True,
            ),
            Column("already_bought", Boolean),
        )

        self.metadata.create_all()

    def get_table(self, table_name: str):
        return self.metadata.tables[table_name]
