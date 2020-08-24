import logging

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page import MainPageLocators

logger = logging.getLogger()


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = self.d = driver

    @property
    def wait(self):
        return WebDriverWait(self.driver, timeout=5)

    @property
    def ex(self):
        return expected_conditions

    def alert_info(self, alert_type: str):
        if alert_type == "success":
            alert_locator = MainPageLocators.ALERT_SUCCESS_INFO
        elif alert_type == "info":
            alert_locator = MainPageLocators.ALERT_INFO
        else:
            return "Incorrect alert type"
        self.wait.until(self.ex.visibility_of_element_located(alert_locator))
        alert = self.d.find_element(*alert_locator)
        message = alert.text
        logger.info(f"Message: {message}")
        return message
