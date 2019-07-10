import unittest
from pyramid import testing
from sqlalchemy import inspect
from backend.db.repository import Repository
from backend.db.database import create_database
from backend.db.scheme import Purchase


class RepositoryTest(unittest.TestCase):
    user_name="Karl"
    def setUp(self):
        self.config = testing.setUp()
        self.engine = create_database("sqlite://")
        self.repository = Repository(self.engine)

    def tearDown(self):
        testing.tearDown()

    def test_purchase_can_be_saved(self):
        empty_purchases = self.repository.find_all_purchases_for_user(self.user_name)
        self.repository.create_new_purchase(self.user_name)

        saved_purchases = self.repository.find_all_purchases_for_user(self.user_name)
        self.assertEqual(0, len(empty_purchases))
        self.assertEqual(1,len(saved_purchases))

    def test_single_purchase_is_found(self):
        self.repository.create_new_purchase(self.user_name)
        self.repository.create_new_purchase(self.user_name)

        single_purchase = self.repository.find_purchase_by_id(1)
        self.assertEqual(Purchase(purchase_id=1, user_name=self.user_name), single_purchase)

    def test_all_purchases_for_user_are_found(self):
        self.repository.create_new_purchase(self.user_name)
        self.repository.create_new_purchase(self.user_name)

        all_purchases = self.repository.find_all_purchases_for_user(self.user_name)
        self.assertEqual(2, len(all_purchases))
    
    def test_all_purchases_are_found(self):
        self.repository.create_new_purchase(self.user_name)
        self.repository.create_new_purchase(self.user_name)
        self.repository.create_new_purchase(self.user_name)
        self.repository.create_new_purchase(self.user_name)

        all_purchases = self.repository.find_all_purchases()
        self.assertEqual(4, len(all_purchases))
