import logging

from locators.login_page import LoginLocators
from pages.base_page import BasePage

logger = logging.getLogger()


class LoginPage(BasePage):
    def login_button(self):
        return self.d.find_element(*LoginLocators.LOGIN_BUTTON)

    def login_otp_code_button(self):
        return self.d.find_element(*LoginLocators.LOGIN_OTP_CODE_BUTTON)

    def auth(self):
        self.login_button().click()
        self.login_otp_code_button().click()
