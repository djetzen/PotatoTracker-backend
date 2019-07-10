import unittest
from pyramid import testing
from sqlalchemy import inspect
from backend.db.repository import Repository
from backend.db.database import create_database
from backend.db.scheme import Purchase, Element


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
        self.create_purchases(2,self.user_name)

        single_purchase = self.repository.find_purchase_by_id(1)
        self.assertEqual(Purchase(purchase_id=1, user_name=self.user_name), single_purchase)

    def test_all_purchases_for_user_are_found(self):
        self.create_purchases(2,self.user_name)

        all_purchases = self.repository.find_all_purchases_for_user(self.user_name)
        self.assertEqual(2, len(all_purchases))
    
    def test_all_purchases_are_found(self):
        self.create_purchases(4,self.user_name)

        all_purchases = self.repository.find_all_purchases()
        self.assertEqual(4, len(all_purchases))

    def test_element_is_saved(self):
        empty_elements = self.repository.find_all_elements()
        self.repository.create_new_element(Element(name="Lemons", amount=5, price=3.50))
        self.repository.create_new_element(Element(name="Apples", amount=5, price=3.50))

        saved_elements = self.repository.find_all_elements()
        self.assertEqual(0, len(empty_elements))
        self.assertEqual(2,len(saved_elements))
    
    def test_element_is_found_by_name(self):
        self.repository.create_new_element(Element(name="Lemons",amount=5, price=3.50))
        self.repository.create_new_element(Element(name="Lemons",amount=5, price=3.50))
        self.repository.create_new_element(Element(name="Apples",amount=5, price=3.50))

        saved_lemons = self.repository.find_all_elements_by_name("Lemons")
        self.assertEqual(2, len(saved_lemons))

    def test_find_all_elements_by_user(self):
        self.repository.create_new_element(Element(name="Lemons",amount=5, price=3.50, user_name=self.user_name))
        self.repository.create_new_element(Element(name="Lemons",amount=5, price=3.50, user_name=self.user_name))
        self.repository.create_new_element(Element(name="Apples",amount=5, price=3.50, user_name="Peter"))

        karls_elements = self.repository.find_all_elements_for_user(self.user_name)
        self.assertEqual(2,len(karls_elements))


    def create_purchases(self, number_of_times:int, user_name:str):
        for x in range(number_of_times):
            self.repository.create_new_purchase(user_name)