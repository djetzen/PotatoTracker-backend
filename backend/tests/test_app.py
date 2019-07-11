import unittest
from pyramid import testing
from pyramid.request import Request
from backend.app import add_all_endpoints, add_endpoint, show_cart_endpoint
from unittest.mock import patch
import backend.json_helpers


class EndpointTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        add_all_endpoints(self.config)

    def tearDown(self):
        testing.tearDown()

    def test_add_endpoint_returns_valid_status(self):
        valid_json = b'{"user_name": "User","name": "lemons","amount": "5"}'
        response = add_endpoint(self.create_add_request(valid_json))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.body, valid_json)

    @patch('backend.json_helpers.valid_request_to_add_endpoint')
    def test_invalid_requests(self, valid_request_to_add_endpoint):

        valid_request_to_add_endpoint.return_value = "False"
        self.check_add_endpoint_status(self.create_add_request(None), 400)

    def test_empty_add_endpoint_returns_error_message(self):
        request = testing.DummyRequest(method="POST")
        self.check_add_endpoint_status(request, 400)

    def test_show_cart_endpoint_is_available(self):
        request = testing.DummyRequest()
        self.assertEqual(show_cart_endpoint(request).status_code, 200)

    def check_add_endpoint_status(self, request, status_code: int):
        self.assertEqual(add_endpoint(request).status_code, status_code)

    def create_add_request(self, json):
        request = Request.blank("/add")
        request.method = "POST"
        request.body = json
        return request
