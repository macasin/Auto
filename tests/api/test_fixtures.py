import pytest

@pytest.mark.check
def test_changeName(user):
    assert user.name == "Cristiano"

@pytest.mark.check
def test_changeSecondName(user):
    assert user.secondName == "Ronaldo"




