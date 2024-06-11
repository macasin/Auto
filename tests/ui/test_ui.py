import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

@pytest.mark.uigitv1

def test_checkIncorrectUserName():
    #Створення обєкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
    
    #відкриваємо сторінку Github Login
    driver.get("https://github.com/login")

    #Знайти поле в яке буде вводити НЕ валідний логін
    loginElement= driver.find_element(By.ID, "login_field")

    #Вводимо неправильне ім'я користувача або адресу
    loginElement.send_keys("gachiMuchi777")

    #Знайти поле в яке вводимо НЕ валідний пароль
    passwordElement=driver.find_element(By.ID,"password")

    #Ввести в поле НЕ валідний пароль
    passwordElement.send_keys("gigachad123@@@11!")

    #Знайти кнопку SignIn та натиснути на неї
    signInButton=driver.find_element(By.NAME, "commit")
    signInButton.click()

    #Перевірка що заголовок сторінки валідний
    assert driver.title == "Sign in to GitHub · GitHub"

    #Пауза на 5сек
    time.sleep(5)

    #закриваємо браузер
    driver.close()
