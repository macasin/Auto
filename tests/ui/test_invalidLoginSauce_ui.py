from modules.ui.page_objects.sauce_signInPageInvalid import InvalidSignInPage
import pytest

@pytest.mark.uisauceLoginInvalid

def test_incorrectUsernameAndPassword():
    
    sign_in_page = InvalidSignInPage() # створюємо обєкт сторінки

    sign_in_page.go_to() #переходимо на сторінку сайту

    sign_in_page.InvalidLoginData("test1","wrongpassword") #заповнюємо не валідними данними поля login та password

    assert sign_in_page.checkURL("https://www.saucedemo.com/") #перевірка чи залишилися ми на цій самій сторінці

    error_message = sign_in_page.getErrorMessageText()
    expected_message = "Epic sadface: Username and password do not match any user in this service"
    assert error_message == expected_message

    sign_in_page.close() #закриваємо браузер
