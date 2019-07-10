import unittest
from pyramid import testing
from sqlalchemy import inspect
from backend.db.repository import Repository
from backend.db.database import create_database
from backend.db.scheme import Purchase, Element


class RepositoryTest(unittest.TestCase):
    user_name = "Karl"

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
        self.assertEqual(1, len(saved_purchases))

    def test_single_purchase_is_found(self):
        self.create_purchases(2, self.user_name)

        single_purchase = self.repository.find_purchase_by_id(1)
        self.assertEqual(
            Purchase(purchase_id=1, user_name=self.user_name), single_purchase
        )

    def test_all_purchases_for_user_are_found(self):
        self.create_purchases(2, self.user_name)

        all_purchases = self.repository.find_all_purchases_for_user(self.user_name)
        self.assertEqual(2, len(all_purchases))

    def test_all_purchases_are_found(self):
        self.create_purchases(4, self.user_name)

        all_purchases = self.repository.find_all_purchases()
        self.assertEqual(4, len(all_purchases))

    def test_element_is_saved(self):
        empty_elements = self.repository.find_all_elements()
        self.repository.create_new_element(
            self.create_element(name="Lemons", amount=5, price=3.5)
        )
        self.repository.create_new_element(
            self.create_element(name="Apples", amount=6, price=2.50)
        )

        saved_elements = self.repository.find_all_elements()
        self.assertEqual(0, len(empty_elements))
        self.assertEqual(2, len(saved_elements))
        self.assertEqual(5, saved_elements[0].amount)
        self.assertEqual(3.50, saved_elements[0].price)

    def test_element_is_found_by_name(self):
        self.repository.create_new_element(self.create_element(name="Lemons"))
        self.repository.create_new_element(self.create_element(name="Lemons"))
        self.repository.create_new_element(self.create_element(name="Apples"))

        saved_lemons = self.repository.find_all_elements_by_name("Lemons")
        self.assertEqual(2, len(saved_lemons))

    def test_find_all_elements_by_user(self):
        self.repository.create_new_element(
            self.create_element(name="Lemons", user_name=self.user_name)
        )
        self.repository.create_new_element(
            self.create_element(name="Lemons", user_name=self.user_name)
        )
        self.repository.create_new_element(
            self.create_element(name="Apples", user_name="Peter")
        )

        karls_elements = self.repository.find_all_elements_for_user(self.user_name)
        self.assertEqual(2, len(karls_elements))

    def test_find_only_bought_elements_by_user(self):
        self.repository.create_new_element(
            self.create_element(name="Lemons", user_name=self.user_name, bought=True)
        )
        self.repository.create_new_element(
            self.create_element(name="Lemons", user_name=self.user_name, bought=True)
        )
        self.repository.create_new_element(
            self.create_element(name="Apples", user_name=self.user_name)
        )

        bought_elements = self.repository.find_only_bought_elements_by_user(
            self.user_name
        )
        self.assertEqual(2, len(bought_elements))

    def test_element_can_be_updated_to_be_bought(self):
        element = self.create_element(name="Lemons", user_name=self.user_name)
        self.repository.create_new_element(element)
        bought_elements_before = self.repository.find_only_bought_elements_by_user(
            self.user_name
        )
        self.repository.mark_as_bought(element)

        bought_elements_after = self.repository.find_only_bought_elements_by_user(
            self.user_name
        )

        self.assertEqual(0, len(bought_elements_before))
        self.assertEqual(1, len(bought_elements_after))

    def test_find_elements_by_purchase_id(self):
        element1 = self.create_element(name="Lemons", purchase_id=1)
        element2 = self.create_element(name="Lemons")
        self.repository.create_new_element(element1)
        self.repository.create_new_element(element2)

        found_elements = self.repository.find_all_elements_by_purchase_id(1)
        self.assertEqual(1, len(found_elements))

    def test_purchase_is_created(self):
        element1 = self.create_element(name="Lemons", user_name=self.user_name)
        element2 = self.create_element(name="Lemons", user_name=self.user_name)
        element3 = self.create_element(name="Apples", user_name=self.user_name)
        self.repository.create_new_element(element1)
        self.repository.create_new_element(element2)
        self.repository.create_new_element(element3)

        self.repository.buy_elements([element1, element2])
        purchased_elements = self.repository.find_all_elements_by_purchase_id(1)
        bought_elements = self.repository.find_only_bought_elements_by_user(
            self.user_name
        )
        self.assertEqual(2, len(bought_elements))
        self.assertEqual(2, len(purchased_elements))

        purchases = self.repository.find_all_purchases()
        self.assertEqual(1, len(purchases))
        self.assertEqual(self.user_name, purchases[0].user_name)
        self.assertEqual(1, purchases[0].purchase_id)

    def create_purchases(self, number_of_times: int, user_name: str):
        for x in range(number_of_times):
            self.repository.create_new_purchase(user_name)

    def create_element(
        self, name="", amount=0, price=0, bought=False, user_name="", purchase_id=1
    ):
        return Element(
            name=name,
            amount=amount,
            price=price,
            bought=bought,
            user_name=user_name,
            purchase_id=purchase_id,
        )

