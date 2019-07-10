import unittest
from pyramid import testing
from sqlalchemy import inspect
from backend.db.repository import Repository
from backend.db.database import create_database
from backend.db.scheme import User


class RepositoryTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.engine = create_database("sqlite://")
        self.repository = Repository(self.engine)

    def tearDown(self):
        testing.tearDown()

    def test_user_can_be_saved(self):
        name = "Dominik"
        user_is_not_saved = self.repository.find_user(name)
        self.repository.save_user(name)

        user_is_saved = self.repository.find_user(name)
        self.assertEqual(None, user_is_not_saved)
        self.assertEqual(User(user_name='Dominik'), user_is_saved)
