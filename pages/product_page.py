from selenium.common.exceptions import NoSuchElementException

from .base_page import BasePage
from .locators import ProductPageLocators as ppl


class ProductPage(BasePage):
    @property
    def product_title(self):
        title = self.browser.find_element(*ppl.PRODUCT_TITLE).text.strip()
        return title

    @property
    def product_price(self):
        price = self.browser.find_element(*ppl.PRODUCT_PRICE).text.strip()
        return price.split(' ')[0]

    def add_product_to_basket(self):
        assert self.is_element_present(*ppl.ADD_TO_BASKET_BUTTON),\
            "There is no 'add to basket' button on the product page!"
        add_to_basket_button = self.browser.find_element(
            *ppl.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def is_added_to_basket_message_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_added_to_basket_message_correct(self):
        assert self.is_added_to_basket_message_present(*ppl.ADDITION_MESSAGE),\
            "There is no message after adding product into the basket"
        product_title_in_message = self.browser.find_element(
            *ppl.PRODUCT_TITLE_IN_MESSAGE).text.strip()
        product_price_in_message = self.browser.find_element(
            *ppl.PRODUCT_PRICE_IN_MESSAGE).text.strip().split(' ')[0]
        assert product_title_in_message == self.product_title,\
            "Product name in message is different from product title!"
        assert product_price_in_message == self.product_price,\
            "Product price in message is different from product price!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ppl.PRODUCT_TITLE_IN_MESSAGE),\
            "Success message is presented, but should not be"

    def success_message_should_disappering(self):
        assert self.is_element_disappearing(*ppl.ADDITION_MESSAGE),\
            "Success message is not disappering, but should"
