from modules.ui.page_objects.sauce_signInValid import ValidDataLogin
from modules.ui.page_objects.sauce_addToTheCart import AddToCart
import pytest


@pytest.mark.addToTheCart
def test_AddToTheCart():
    inventoryPage = AddToCart()
    inventoryPage.go_to()
    inventoryPage.validLoginData("standard_user", "secret_sauce")  # Fill in the login fields
    assert inventoryPage.checkURL("https://www.saucedemo.com/cart.html")
    assert inventoryPage.is_checkout_button_present()
    inventoryPage.close()
