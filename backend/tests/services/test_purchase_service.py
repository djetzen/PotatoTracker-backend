import pytest
from backend.db.repository import Repository
from backend.services.purchase_service import PurchaseService

repository = Repository(None)
service = PurchaseService(repository)

@pytest.fixture(autouse=True)
def run_around_tests(mocker):
    mocker.patch.object(repository, "create_new_purchase")
    mocker.patch.object(repository, "find_all_purchases_for_user")
    mocker.patch.object(repository, "find_purchase_by_id")
    yield

def test_should_call_create_new_purchase():
    service.save_new_purchase('')

    assert repository.create_new_purchase.call_count == 1

def test_should_call_find_all_purchases_for_user():
    service.find_all_purchases_for_user('')
    assert repository.find_all_purchases_for_user.call_count == 1

def test_should_call_find_purchase_by_id():
    service.find_purchase_by_id(1)
    assert repository.find_purchase_by_id.call_count == 1

