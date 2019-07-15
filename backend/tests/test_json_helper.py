import unittest
import json
from pyramid import testing
from backend.json_helpers import (
    create_element_from_json,
    valid_request_to_add_endpoint,
    create_elements,
)


class JsonHelperTests(unittest.TestCase):
    def test_create_element(self):
        valid_json = b'{"user_name": "User","name": "lemons","amount": "5", "price": "3.50", "bought":"true"}'
        element = create_element_from_json(json.loads(valid_json))
        self.assertEqual(
            str(element),
            "Element<name: lemons, amount: 5, price: 3.50, user_name: User, bought: true, purchase_id: None>",
        )

    def test_valid_request_to_add_endpoint(self):
        missing_user = b'{"elementName": "lemons","amount": "5"}'
        missing_elementName = b'{"user": "User","amount": "5"}'
        missing_amount = b'{"user": "User","elementName": "lemons"}'
        valid_json = b'{"user_name": "User","name": "lemons","amount": "5"}'
        self.assertEqual(False, valid_request_to_add_endpoint(missing_user))
        self.assertEqual(False, valid_request_to_add_endpoint(missing_elementName))
        self.assertEqual(False, valid_request_to_add_endpoint(missing_amount))
        self.assertEqual(True, valid_request_to_add_endpoint(valid_json))

    def test_create_elements(self):
        put_json = b'{"elements": [{"user_name": "User","name": "noodles","amount": "5"},{"user_name": "User","name": "rice","amount": "4"}]}'
        elements = create_elements(put_json)
        self.assertEqual(2, len(elements))
        self.assertEqual("User", elements[0].user_name)
        self.assertEqual("noodles", elements[0].name)
        self.assertEqual("5", elements[0].amount)
