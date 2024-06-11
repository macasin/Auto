from modules.ui.page_objects.sauce_signInValid import ValidDataLogin
import pytest

@pytest.mark.uisauceLoginValid

def test_ValidLogin():
    signInPage=ValidDataLogin() # створюємо обєкт сторінки
    signInPage.go_to() #переходимо на сторінку
    signInPage.validLoginData("standard_user", "secret_sauce") #заповнюємо поле логіну та паролю

    assert signInPage.checkURL("https://www.saucedemo.com/inventory.html")

    signInPage.close() #закриваємо браузер

