from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time

class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def name_of_book_on_page_and_message(self):
        book_name_on_page = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK_ON_PAGE).text
        book_name_on_message = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK_ON_MESSAGE).text
        assert book_name_on_page in book_name_on_message, "Name is different"

    def price_of_book_on_page_amd_message(self):
        book_price_on_page = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK_ON_PAGE).text
        book_price_on_message = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK_ON_MESSAGE).text
        assert book_price_on_page in book_price_on_message, "Price is different"







