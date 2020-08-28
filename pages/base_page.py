import logging

import allure
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page import BasePageLocators
from locators.main_page import MainPageLocators
from utils import custom_expected_conditions

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

    @property
    def custom_ex(self):
        return custom_expected_conditions

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
        logger.info(f"Сообщение: {message}")
        return message

    @allure.step("Нажатие кнопки 'Подтвердить'")
    def confirm_button(self):
        logger.info("Нажатие кнопки 'Подтвердить'")
        return self.d.find_element(*BasePageLocators.CONFIRM_BUTTON).click()

    def confirm_with_switch_frame(self):
        logger.info("Переключение на фрейм")
        self.wait.until(
            self.ex.frame_to_be_available_and_switch_to_it(BasePageLocators.IFRAME)
        )
        try:
            self.confirm_button()
        except NoSuchWindowException:
            self.wait.until(
                self.ex.visibility_of(
                    self.d.find_element(*BasePageLocators.CONFIRM_BUTTON)
                )
            )
            self.confirm_button()
        logger.info("Возврат в основное окно")
        self.d.switch_to.default_content()
