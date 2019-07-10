import unittest
from pyramid import testing
from pyramid.request import Request
from backend.app import add_all_endpoints, add_endpoint


class BackendTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        add_all_endpoints(self.config)

    def tearDown(self):
        testing.tearDown()

    def test_add_endpoint_returns_valid_status(self):
        valid_json = b'{"user": "User","elementName": "lemons","amount": "5"}'
        response = add_endpoint(self.create_add_request(valid_json))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.body, valid_json)

    def test_invalid_requests(self):
        missing_user = b'{"elementName": "lemons","amount": "5"}'
        missing_elementName = b'{"user": "User","amount": "5"}'
        missing_amount = b'{"user": "User","elementName": "lemons"}'

        self.check_add_endpoint_status(self.create_add_request(missing_user), 400)

        self.check_add_endpoint_status(
            self.create_add_request(missing_elementName), 400
        )

        self.check_add_endpoint_status(self.create_add_request(missing_amount), 400)

    def test_empty_add_endpoint_returns_error_message(self):
        request = testing.DummyRequest(method="POST")
        self.check_add_endpoint_status(request, 400)

    def check_add_endpoint_status(self, request, status_code: int):
        self.assertEqual(add_endpoint(request).status_code, status_code)

    def create_add_request(self, json):
        request = Request.blank("/add")
        request.method = "POST"
        request.body = json
        return request
