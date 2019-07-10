from backend.db.repository import repository_impl

class PurchaseService:
    def __init__(self, repository_impl):
        self.__repository = repository_impl

    def save_new_purchase(self, user_name:str):
        self.__repository.create_new_purchase(user_name)

    def find_all_purchases_for_user(self, user_name:str):
        self.__repository.find_all_purchases_for_user(user_name)

    def find_purchase_by_id(self, id:int):
        self.__repository.find_purchase_by_id(id)

    def find_all_purchases(self):
        self.__repository.find_all_purchases()