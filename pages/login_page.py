from .base_page import BasePage
from .locators import LoginPageLocators as lpl


class LoginPage(BasePage):
    def should_be_login_page(self):
        collected_errors = []
        try:
            self.should_be_login_url()
        except AssertionError as err:
            collected_errors.append(str(err))
        try:
            self.should_be_login_form()
        except AssertionError as err:
            collected_errors.append(str(err))
        try:
            self.should_be_register_form()
        except AssertionError as err:
            collected_errors.append(str(err))
        assert not collected_errors,\
            f"It's not login page! There next problems: {' '.join(collected_errors)}"

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url,\
            r"Page hasn't login url!"

    def should_be_login_form(self):
        assert self.is_element_present(*lpl.LOGIN_FORM),\
            "There is no login form on page!"

    def should_be_register_form(self):
        assert self.is_element_present(*lpl.REGISTER_FORM),\
            "There is no register form on page!"

    def register_new_user(self, email, password):
        self.should_be_register_form()
        email_input = self.browser.find_element(*lpl.EMAIL_INPUT_REG)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*lpl.PASSWORD_INPUT_REG)
        password_input.send_keys(password)
        password_confirm = self.browser.find_element(*lpl.PASSWORD_CONFIRM_REG)
        password_confirm.send_keys(password)
        register_button = self.browser.find_element(*lpl.REGISTER_BUTTON)
        register_button.click()
