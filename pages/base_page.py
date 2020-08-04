from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = self.d = driver

    @property
    def wait(self):
        return WebDriverWait(self.driver, timeout=5)

    @property
    def ex(self):
        return expected_conditions
