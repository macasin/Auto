from modules.ui.page_objects.git_sign_in_page import SignInPage
import pytest
import time

@pytest.mark.uigitv2

def test_incorrectUsernameAndPassword():

    sign_in_page=SignInPage() #створюємо обєкт сторінки

    sign_in_page.go_to() #відкриваємо сторінку за посиланням

    sign_in_page.loginInvalidData("ricardoMilos1237@gmail.com", "wrongpassword") #вводимо невалідний логін та пароль

    assert sign_in_page.checkTitle("Sign in to GitHub · GitHub") #перевірка, шо ми залишилися на тій самій сторінці, перехід не відбувся

    time.sleep(5) #пауза 5сек

    sign_in_page.close() #закриваємо браузер




