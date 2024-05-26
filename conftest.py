import pytest
from modules.api.clients.github import GitHub
class User:

    def __init__(self):
        self.name = None
        self.secondName = None

    def create(self):
        self.name = "Cristiano"
        self.secondName = "Ronaldo"

    def remove(self):
        self.name = ""
        self.secondName = ""

@pytest.fixture
def user():
    user=User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api= GitHub()
    yield api