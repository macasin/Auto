from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class ValidDataLogin(BasePage):
    URL = "https://www.saucedemo.com/"

    def __init__(self):
        super().__init__() #запуск chromium 

    def go_to(self):
        self.driver.get(ValidDataLogin.URL) #переходимо на сторінку сайту

    def validLoginData(self,username,password):
        loginField= self.driver.find_element(By.ID, "user-name") #знаходимо поле логіну
        loginField.send_keys(username) #вводимо Валідні дані

        passwordField= self.driver.find_element(By.NAME, "password") #знаходимо поле паролю
        passwordField.send_keys(password) #вводимо Валідні дані

        loginButton= self.driver.find_element(By.NAME,"login-button") #знаходимо кнопку login
        loginButton.click() #натискаємо на кнопку логін

        time.sleep(3) #пауза 3сек
        
    def checkURL(self,expectedURL):
        return self.driver.current_url == expectedURL


