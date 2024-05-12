import pytest

@pytest.mark.change
def test_remove_name(user):
    user.name= ""
    assert user.name == ""

@pytest.mark.check
def test_check_name(user):
    assert user.name == "Cristiano"

@pytest.mark.check
def test_check_secondName(user):
    assert user.secondName == "Ronaldo"