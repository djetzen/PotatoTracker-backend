import unittest
from pyramid import testing
from pyramid.request import Request
from backend.backend import add_all_endpoints, add_endpoint



class BackendTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        add_all_endpoints(self.config)


    def tearDown(self):
        testing.tearDown()

    def test_add_endpoint_returns_valid_status(self):
        add_to_cart_json=b'{"user": "User","elementName": "lemons","amount": "5"}'
        request = Request.blank("/add")
        request.method='POST'
        request.body=add_to_cart_json
        response = add_endpoint(request)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.body,add_to_cart_json)

    
    def test_invalid_requests(self):
        missing_user=b'{"elementName": "lemons","amount": "5"}'
        missing_elementName=b'{"user": "User","amount": "5"}'
        missing_amount=b'{"user": "User","elementName": "lemons"}'
        request = Request.blank("/add")
        request.method='POST'
        request.body=missing_user
        self.assertEqual(add_endpoint(request).status_code, 400)

        request.body=missing_elementName
        self.assertEqual(add_endpoint(request).status_code, 400)

        request.body=missing_amount
        self.assertEqual(add_endpoint(request).status_code, 400)


    def test_empty_add_endpoint_returns_error_message(self):
        request = testing.DummyRequest(method='POST')
        response = add_endpoint(request)

        self.assertEqual(response.status_code, 400)
