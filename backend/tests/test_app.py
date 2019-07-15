import unittest
import pytest
import json
from pyramid import testing
from unittest.mock import patch
from pyramid.request import Request
from backend.domain.element import Element
from backend.services.element_service import element_service_impl
from backend.app import (
    add_all_endpoints,
    add_endpoint,
    cart_endpoint,
    purchase_id_endpoint,
    cart_endpoint_put,
)
from backend.db.json_mapper import JSONMapper
import backend.json_helpers
from webtest import TestApp


valid_add_json = b'{"user_name": "User","name": "lemons","amount": "5"}'

mocked_elements = [
    Element(name="Lemons", amount=5, user_name="User"),
    Element(name="Apples", amount=3, user_name="User"),
]
bought_and_mocked_elements = [
    Element(name="Lemons", amount=5, user_name="User", bought=True, purchase_id=1),
    Element(name="Apples", amount=3, user_name="User", bought=True, purchase_id=1),
]


class EndpointTests(unittest.TestCase):
    def setUp(self):
        request = testing.DummyRequest()
        self.config = testing.setUp(request=request)
        add_all_endpoints(self.config)
        app = backend.app.main()
        self.testapp = TestApp(app)

    @pytest.fixture(autouse=True)
    def run_around_tests(self, mocker):
        mocker.patch.object(element_service_impl, "create_new_element")
        mocker.patch.object(element_service_impl, "buy_elements")
        open_elements_mock = mocker.patch.object(
            element_service_impl, "find_open_elements_by_user"
        )
        open_elements_mock.return_value = mocked_elements

        purchase_id_mock = mocker.patch.object(
            element_service_impl, "find_elements_by_purchase_id"
        )
        purchase_id_mock.return_value = mocked_elements

        buy_elements_mock = mocker.patch.object(element_service_impl, "buy_elements")
        buy_elements_mock.return_value = bought_and_mocked_elements
        yield

    def test_add_endpoint_returns_valid_status(self):
        response = self.testapp.post("/add", valid_add_json)

        assert response.status_code == 201
        assert (
            response.body
            == b'{"name": "lemons", "amount": "5", "price": 0.0, "user_name": "User", "bought": false, "purchase_id": null}'
        )

    def test_add_endpoint_with_valid_json_calls_service(self):
        self.testapp.post("/add", valid_add_json)
        assert element_service_impl.create_new_element.call_count == 1

    @patch("backend.json_helpers.valid_request_to_add_endpoint")
    def test_invalid_requests(self, valid_request_to_add_endpoint):

        valid_request_to_add_endpoint.return_value = "False"
        response = self.testapp.post("/add", "", expect_errors=True)
        assert response.status_code == 400

    def test_cart_endpoint_exists(self):
        response = self.testapp.get("/cart/MyUserName")
        assert response.status_code == 200

    def test_cart_endpoint_calls_element_service(self):
        response = self.testapp.get("/cart/MyUserName")
        assert response.body == bytearray(
            json.dumps(mocked_elements, cls=JSONMapper), "utf-8"
        )

    def test_purchase_id_endpoint_delivers_400_without_id(self):
        response = self.testapp.get("/purchase/1")
        assert response.status_code == 200
        assert element_service_impl.find_elements_by_purchase_id.call_count == 1
        assert response.body == bytearray(
            json.dumps(mocked_elements, cls=JSONMapper), "utf-8"
        )

    def test_put_endpoint_for_cart_exists_and_must_not_be_empty(self):
        response = self.testapp.put("/cart/MyUserName", expect_errors=True)
        response2 = self.testapp.put(
            "/cart/MyUserName", valid_add_json, expect_errors=True
        )
        assert response.status_code == 400
        assert response2.status_code == 400

    def test_put_endpoint_for_cart_buys_elements(self):
        put_json = '{"elements": [{"name": "Lemons","amount": 5,"user_name": "User"},{"name": "Apples","amount": 3,"price": 0,"user_name": "User"}]}'
        expected_received_json = b'[{"name": "Lemons", "amount": 5, "price": 0.0, "user_name": "User", "bought": true, "purchase_id": 1}, {"name": "Apples", "amount": 3, "price": 0.0, "user_name": "User", "bought": true, "purchase_id": 1}]'
        response = self.testapp.put("/cart/MyUserName", put_json, expect_errors=True)
        assert response.status_code == 200
        assert element_service_impl.buy_elements.call_count == 1
        assert response.body == expected_received_json

    def create_add_request(self, json):
        request = Request.blank("/add")
        request.method = "POST"
        request.body = json
        return request
