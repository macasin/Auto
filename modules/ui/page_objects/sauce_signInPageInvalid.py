from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time 

class InvalidSignInPage(BasePage):
    URL= "https://www.saucedemo.com/"

    def __init__(self):
        super().__init__() #запуск chromium

    def go_to(self):
        self.driver.get(InvalidSignInPage.URL) #переходимо на сторінку сайту

    def InvalidLoginData(self,username,password):
        loginField=self.driver.find_element(By.ID, "user-name") #знайти поле логіну
        loginField.send_keys(username) #ввести НЕ валідні дані логін

        passwordField=self.driver.find_element(By.ID, "password") #знайти поле паролю
        passwordField.send_keys(password) #ввести НЕ валідні дані в поле паролю

        loginButton=self.driver.find_element(By.ID, "login-button") #знайти кнопку Login
        loginButton.click() #натиснути на кнопку Login

        time.sleep(3) #пауза 3сек

    def checkURL(self,expectedURL):
        return self.driver.current_url == expectedURL

    def getErrorMessageText(self):
        epicSadface = self.driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3")
        return epicSadface.text

    

