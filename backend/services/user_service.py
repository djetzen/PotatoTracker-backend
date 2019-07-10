from backend.db.repository import repository_impl

class UserService:
    def __init__(self, repository_impl):
        self.__repository = repository_impl

    def save(self, user_name:str):
        self.__repository.save_user(user_name)

    def find(self, user_name:str):
        self.__repository.find_user(user_name)

user_service = UserService(repository_impl)
