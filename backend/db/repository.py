from backend.db.database import Database
from sqlalchemy import Table, MetaData


class Repository:
    def __init__(self, database: Database):
        self.__database = database

    def save_user(self, user_name: str):
        user_table: Table = self.__database.get_table("user")
        insert_stmt = user_table.insert().values(user_name=user_name)
        self.execute_statement(insert_stmt)

    def find_user(self, user_name: str) -> str:
        user_table: Table = self.__database.get_table("user")
        stmt = user_table.select().where(user_table.c.user_name == user_name)
        return self.execute_statement(stmt).fetchall()

    def execute_statement(self, stmt):
        connection = self.__database.engine.connect()
        result = connection.execute(stmt)
        connection.close()
        return result
