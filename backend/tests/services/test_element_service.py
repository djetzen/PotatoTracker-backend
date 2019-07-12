import pytest
from backend.db.repository import Repository
from backend.services.element_service import ElementService

repository = Repository(None)
service = ElementService(repository)


@pytest.fixture(autouse=True)
def run_around_tests(mocker):
    mocker.patch.object(repository, "find_all_elements")
    mocker.patch.object(repository, "create_new_element")
    mocker.patch.object(repository, "find_all_elements_by_name")
    mocker.patch.object(repository, "find_all_elements_for_user")
    mocker.patch.object(repository, "find_only_bought_elements_by_user")
    mocker.patch.object(repository, "find_all_elements_by_purchase_id")
    mocker.patch.object(repository, "buy_elements")
    mocker.patch.object(repository, "find_only_unbought_elements_by_user")
    yield


def test_should_call_find_all_element():
    service.get_all_elements()
    assert repository.find_all_elements.call_count == 1


def test_should_call_create_new_element():
    service.create_new_element(None)
    assert repository.create_new_element.call_count == 1


def test_should_call_find_all_elements_by_name():
    service.find_elements_by_name("")
    assert repository.find_all_elements_by_name.call_count == 1


def test_should_call_find_all_elements_for_user():
    service.find_elements_by_user("")
    assert repository.find_all_elements_for_user.call_count == 1


def test_should_call_find_only_bought_elements_by_user():
    service.find_bought_elements_by_user("")
    assert repository.find_only_bought_elements_by_user.call_count == 1


def test_should_call_find_only_unbought_elements_by_user():
    service.find_open_elements_by_user("")
    assert repository.find_only_unbought_elements_by_user.call_count == 1


def test_should_call_find_all_elements_by_purchase_id():
    service.find_elements_by_purchase_id(0)
    assert repository.find_all_elements_by_purchase_id.call_count == 1


def test_should_call_buy_elements():
    service.buy_elements([])
    assert repository.buy_elements.call_count == 1
