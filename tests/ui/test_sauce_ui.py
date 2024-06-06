from modules.ui.page_objects.sauce_signInPage import SignInPage
import pytest

@pytest.mark.uisauce

def test_incorrectUsernameAndPassword():
    
    sign_in_page = SignInPage() # створюємо обєкт сторінки

    sign_in_page.go_to #переходимо на сторінку сайту

    sign_in_page.InvalidLoginData("test1","wrongpassword") #заповнюємо не валідними данними поля login та password

    assert sign_in_page.checkURL("https://www.saucedemo.com/") #перевірка чи залишилися ми на цій самій сторінці

    sign_in_page.close() #закриваємо браузер
