import allure
from selenium.webdriver.android.webdriver import WebDriver
from pages.base_page import BasePage
import logging
from common.logging import setup
from pages.login_page import LoginPage

logger = logging.getLogger()


class Application(BasePage):
    def __init__(self, driver: WebDriver, base_url):
        super().__init__(driver)
        self.base_url = base_url
        self.login = LoginPage(self.d)
        setup("INFO")
        logger.setLevel("INFO")

    @allure.step("Открытие страницы")
    def open_page(self, url):
        logger.info(f"Open page {url}")
        self.driver.get(url)

    @property
    def main_url(self):
        return self.base_url + "welcome"