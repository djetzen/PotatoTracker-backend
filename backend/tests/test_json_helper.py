import unittest
from pyramid import testing
from backend.json_helpers import create_element, valid_request_to_add_endpoint

class JsonHelperTests(unittest.TestCase):
    def test_create_element(self):
        valid_json = b'{"user_name": "User","name": "lemons","amount": "5", "price": "3.50", "bought":"true"}'
        element = create_element(valid_json)
        self.assertEqual(str(element),"Element<element_id:None, name: lemons, amount: 5, price:3.50, user_name:User, bought: true, purchase_id: None>")

    def test_valid_request_to_add_endpoint(self):
        missing_user = b'{"elementName": "lemons","amount": "5"}'
        missing_elementName = b'{"user": "User","amount": "5"}'
        missing_amount = b'{"user": "User","elementName": "lemons"}'
        valid_json = b'{"user_name": "User","name": "lemons","amount": "5"}'
        self.assertEqual(False, valid_request_to_add_endpoint(missing_user))
        self.assertEqual(False, valid_request_to_add_endpoint(missing_elementName))
        self.assertEqual(False, valid_request_to_add_endpoint(missing_amount))
        self.assertEqual(True, valid_request_to_add_endpoint(valid_json))