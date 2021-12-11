import pytest
from faker import Faker

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/'\
       'coders-at-work_207/?promo=newYear2019'


@pytest.mark.need_review
@pytest.mark.parametrize('link', [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'\
    '?promo=offer0',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'\
    '?promo=offer1',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'\
    '?promo=offer2',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'\
    '?promo=offer3',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'\
    '?promo=offer4',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'\
    '?promo=offer5',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'\
    '?promo=offer6',
    pytest.param('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'\
    '?promo=offer7', marks=pytest.mark.xfail(reason="Bug that wouldn't be fixed")),
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'\
    '?promo=offer8',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'\
    '?promo=offer9'
    ])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.is_added_to_basket_message_correct()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.success_message_should_disappering()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"\
           "catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"\
           "catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()


@pytest.mark.user_tests
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        login_link = 'https://selenium1py.pythonanywhere.com/accounts/login/'
        login_page = LoginPage(browser, login_link)
        login_page.open()
        email = Faker().email()
        password = Faker().password()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.is_added_to_basket_message_correct()
