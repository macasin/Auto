from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class AddToCart(BasePage):
    URL="https://www.saucedemo.com/"

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(AddToCart.URL)

    def validLoginData(self,username,password):
        loginField= self.driver.find_element(By.ID, "user-name") #знаходимо поле логіну
        loginField.send_keys(username) #вводимо Валідні дані

        passwordField= self.driver.find_element(By.NAME, "password") #знаходимо поле паролю
        passwordField.send_keys(password) #вводимо Валідні дані

        loginButton= self.driver.find_element(By.NAME,"login-button") #знаходимо кнопку login
        loginButton.click() #натискаємо на кнопку логін

        backPackButton=self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack") #find add to the cart button for the backpack
        backPackButton.click()

        bikeLightsButton=self.driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light") ##find add to the cart button for the bike lights
        bikeLightsButton.click()

        time.sleep(2) #пауза 2сек

        cartButton=self.driver.find_element(By.CLASS_NAME,"shopping_cart_link") #find the cart button
        cartButton.click()

        time.sleep(2) #пауза 2сек

    def checkURL(self,expectedURL):
        return self.driver.current_url == expectedURL

    def is_checkout_button_present(self):
        return len(self.driver.find_elements(By.ID, "checkout")) > 0 #check that is more than 0 elements with this ID
