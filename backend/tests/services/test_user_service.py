import pytest
from backend.db.repository import Repository
from backend.services.user_service import UserService

repository = Repository(None)
service = UserService(repository)

@pytest.fixture(autouse=True)
def run_around_tests(mocker):
    mocker.patch.object(repository, "save_user")
    mocker.patch.object(repository, "find_user")
    yield

def test_should_call_save_on_repository():
    service.save('')

    assert repository.save_user.call_count == 1

def test_should_call_find_user_on_repository():
    service.find('')
    assert repository.find_user.call_count == 1

