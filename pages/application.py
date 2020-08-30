import allure
from selenium.webdriver.android.webdriver import WebDriver

from pages.accounts_page import AccountsPage
from pages.base_page import BasePage
import logging
from utils.logging import setup
from pages.credit_page import CreditPage
from pages.deposits_page import DepositPage
from pages.login_page import LoginPage

logger = logging.getLogger()


class Application(BasePage):
    def __init__(self, driver: WebDriver, base_url):
        super().__init__(driver)
        self.base_url = base_url
        self.login = LoginPage(self.d)
        self.credit_page = CreditPage(self.d)
        self.deposit_page = DepositPage(self.d)
        self.account_page = AccountsPage(self.d)
        setup("INFO")
        logger.setLevel("INFO")

    @allure.step("Открытие страницы")
    def open_page(self, url):
        logger.info(f"Открытие страницы: {url}")
        self.driver.get(url)

    @property
    def main_url(self):
        return self.base_url + "welcome"

    @property
    def credit_url(self):
        return self.base_url + "loans"

    @property
    def deposit_url(self):
        return self.base_url + "deposits"

    @property
    def accounts_url(self):
        return self.base_url + "accounts"

    @property
    def statement_url(self):
        return self.base_url + "statement"

    def loan_full_repayment_url(self, doc_id):
        return (
            self.base_url + f"messages/form?topic=LOAN_FULL_REPAYMENT&loanId={doc_id}"
        )
