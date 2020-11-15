from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    PRICE_OF_BOOK_ON_PAGE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
    NAME_OF_BOOK_ON_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_OF_BOOK_ON_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    NAME_OF_BOOK_ON_MESSAGE = (By.CSS_SELECTOR, "div.alertinner ")