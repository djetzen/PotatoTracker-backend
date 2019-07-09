import unittest
from pyramid import testing
from sqlalchemy import inspect
from backend.db.database import Database
from backend.db.repository import Repository


class RepositoryTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.database = Database("sqlite://")
        self.database.create_database()
        self.repository = Repository(self.database)

    def tearDown(self):
        testing.tearDown()

    def test_user_can_be_saved(self):
        name = "Dominik"
        user_is_not_saved = self.repository.find_user(name)
        self.repository.save_user(name)

        user_is_saved = self.repository.find_user(name)
        self.assertEqual([], user_is_not_saved)
        self.assertEqual([('Dominik',)], user_is_saved)
