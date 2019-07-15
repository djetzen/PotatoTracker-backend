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
)
from backend.db.json_mapper import JSONMapper
import backend.json_helpers

valid_json = b'{"user_name": "User","name": "lemons","amount": "5"}'

mocked_elements = [
    Element(name="Lemons", amount=5, user_name="User"),
    Element(name="Apples", amount=3, user_name="User"),
]


@pytest.fixture(autouse=True)
def run_around_tests(mocker):
    mocker.patch.object(element_service_impl, "create_new_element")
    open_elements_mock = mocker.patch.object(
        element_service_impl, "find_open_elements_by_user"
    )
    open_elements_mock.return_value = mocked_elements

    purchase_id_mock = mocker.patch.object(
        element_service_impl, "find_elements_by_purchase_id"
    )
    purchase_id_mock.return_value = mocked_elements
    yield


def test_add_endpoint_returns_valid_status():
    response = add_endpoint(create_add_request(valid_json))

    assert response.status_code == 201
    assert (
        response.body
        == b'{"name": "lemons", "amount": "5", "price": 0.0, "user_name": "User", "bought": false, "purchase_id": null}'
    )


def test_add_endpoint_with_valid_json_calls_service():
    add_endpoint(create_add_request(valid_json))
    assert element_service_impl.create_new_element.call_count == 1


@patch("backend.json_helpers.valid_request_to_add_endpoint")
def test_invalid_requests(valid_request_to_add_endpoint):

    valid_request_to_add_endpoint.return_value = "False"
    check_add_endpoint_status(request=create_add_request(None), status_code=400)


def test_empty_add_endpoint_returns_error_message():
    request = testing.DummyRequest(method="POST")
    check_add_endpoint_status(request, 400)


def test_cart_endpoint_exists():
    request = testing.DummyRequest()
    request.matchdict["user_name"] = "MyUserName"
    assert cart_endpoint(request).status_code == 200


def test_cart_endpoint_without_parameter_delivers_400():
    request = testing.DummyRequest()
    assert cart_endpoint(request).status_code == 400


def test_cart_endpoint_with_wrong_dict_delivers_400():
    request = testing.DummyRequest()
    request.matchdict["user"] = "MyUserName"
    assert cart_endpoint(request).status_code == 400


def test_cart_endpoint_calls_element_service():
    request = testing.DummyRequest()
    request.matchdict["user_name"] = "MyUserName"
    response = cart_endpoint(request)
    assert response.body == bytearray(
        json.dumps(mocked_elements, cls=JSONMapper), "utf-8"
    )


def test_purchase_id_endpoint_delivers_400_without_id():
    request = testing.DummyRequest()
    response = purchase_id_endpoint(request)

    assert response.status_code == 400


def test_purchase_id_endpoint_delivers_200_with_id():
    request = testing.DummyRequest()
    request.matchdict["id"] = "1"
    response = purchase_id_endpoint(request)

    assert response.status_code == 200
    assert element_service_impl.find_elements_by_purchase_id.call_count == 1
    assert response.body == bytearray(
        json.dumps(mocked_elements, cls=JSONMapper), "utf-8"
    )


def check_add_endpoint_status(request, status_code: int):
    assert add_endpoint(request).status_code == status_code


def create_add_request(json):
    request = Request.blank("/add")
    request.method = "POST"
    request.body = json
    return request
