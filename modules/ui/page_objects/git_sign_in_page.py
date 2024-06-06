from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage):
    URL="https://github.com/login"

    def __init__(self):
        super().__init__() #запускаємо chromium

    def go_to(self):
        self.driver.get(SignInPage.URL) #відкриваємо вебсайт
    
    def loginInvalidData(self,username,password):
        loginElem=self.driver.find_element(By.ID, "login_field")#знаходимо поле логіну
        loginElem.send_keys(username)#вводимо невалідний логін

        passwordElem=self.driver.find_element(By.ID, "password")#знаходимо поле паролю
        passwordElem.send_keys(password)#вводимо невалідний пароль

        signInButton=self.driver.find_element(By.NAME, "commit")#знаходимо кнопку SignIn
        signInButton.click() #натискаємо на кнопку SignIn

    def checkTitle(self,expectedTitle): #чи відбувся перехід на іншу сторінку
        return self.driver.title == expectedTitle
    
   