import time
from .pages.product_page import ProductPage


def test_guest_can_add_product(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.name_of_book_on_page_and_message()
    time.sleep(2)
    page.price_of_book_on_page_amd_message()


