import logging

import allure
from selenium.common.exceptions import NoSuchElementException

from locators.deposit_page import DepositPageLocators
from pages.base_page import BasePage
from utils.ex import text_is_not_empty

logger = logging.getLogger()


class DepositPage(BasePage):
    deposit_currency = {
        "RUB": DepositPageLocators.RUB_CURRENCY,
        "USD": DepositPageLocators.USD_CURRENCY,
        "EUR": DepositPageLocators.EUR_CURRENCY,
    }

    deposit_min_days = {
        "-1": DepositPageLocators.MIN_DAYS_FREE_TERM,
        "15": DepositPageLocators.MIN_DAYS_TWO_WEEKS,
        "31": DepositPageLocators.MIN_DAYS_ONE_MONTH,
        "91": DepositPageLocators.MIN_DAYS_THREE_MONTHS,
        "181": DepositPageLocators.MIN_DAYS_SIX_MONTHS,
        "367": DepositPageLocators.MIN_DAYS_ONE_YEAR,
        "733": DepositPageLocators.MIN_DAYS_TWO_YEARS,
    }

    @allure.step("Нажатие кнопки 'Открыть вкладку'")
    def open_deposit(self):
        logger.info("'Open deposit' button click")
        self.d.find_element(*DepositPageLocators.OPEN_DEPOSIT_BUTTON).click()

    @allure.step("Выбор фильтров: валюта: {currency}, на срок: {min_days}")
    def set_filters(self, currency, min_days):
        if currency not in self.deposit_currency.keys():
            logger.error("invalid currency")
            raise Exception("invalid currency")
        if min_days not in self.deposit_min_days.keys():
            logger.error("invalid min_days")
            raise Exception("invalid min_days")
        currency_radio = self.deposit_currency[currency]
        min_days_radio = self.deposit_min_days[min_days]
        self.d.find_element(*currency_radio).click()
        self.d.find_element(*min_days_radio).click()
        logger.info(f"Set filters: currency - {currency}, min_days - {min_days}")

    @allure.step("Нажате кнопки 'открыть вклад' у первого вклада из списка")
    def open_first_deposit(self) -> bool:
        try:
            self.d.find_elements(*DepositPageLocators.OPEN_DEPOSIT_BUTTONS)[0].click()
            logger.info("First deposit 'open deposit button' click")
            return True
        except NoSuchElementException:
            return False

    def add_data(self, end_data, summ, prolongation):
        self.d.find_element(*DepositPageLocators.DATE_FIELD).clear()
        self.d.find_element(*DepositPageLocators.DATE_FIELD).send_keys(end_data)
        self.d.find_element(*DepositPageLocators.SUMM_FIELD).send_keys(summ)
        if not prolongation:
            self.d.find_element(*DepositPageLocators.PROLONGATION_CHECKBOX).click()
        logger.info(
            f"Set data: end_data - {end_data}, summ - {summ}, prolongation - "
            f"{prolongation}"
        )

    def add_data_without_end_date(self, summ, prolongation):
        self.d.find_element(*DepositPageLocators.SUMM_FIELD).send_keys(summ)
        if not prolongation:
            self.d.find_element(*DepositPageLocators.PROLONGATION_CHECKBOX).click()
        logger.info(f"Set data: summ - {summ}, prolongation - {prolongation}")

    @allure.step("Нажатие кнопки 'Дальше' на странице открытия вклада")
    def submit(self):
        elem = self.d.find_element(*DepositPageLocators.INTEREST_RATE_VALUE)
        self.wait.until(text_is_not_empty(DepositPageLocators.INTEREST_RATE_VALUE))
        element_text = elem.text
        logger.info(f"Element text = {element_text}")
        self.d.find_element(*DepositPageLocators.SUBMIT_BUTTON).click()
        logger.info("Click submit button")

    @allure.step("Нажатие кнопки 'Дальше' на странице открытия вклада")
    def simple_submit(self):
        self.d.find_element(*DepositPageLocators.SUBMIT_BUTTON).click()
        logger.info("Click submit button")

    @allure.step("Проставление чекбокса")
    def agree_with_terms(self):
        self.d.find_element(*DepositPageLocators.TERMS_AGREEMENT_CHECKBOX).click()
        logger.info("Set checkbox")

    @allure.step("Нажатие кнопки 'Подтвердить' на странице открытия вклада")
    def confirm(self):
        confirm_button = self.d.find_element(*DepositPageLocators.CONFIRM_BUTTON)
        logger.info(f"Confirm button: {confirm_button.is_enabled()}")
        confirm_button.click()
        logger.info("Click confirm button")

    def confirm_is_enabled(self):
        enabled = self.d.find_element(*DepositPageLocators.CONFIRM_BUTTON).is_enabled()
        logger.info(f"Confirm button: {enabled}")
        return not enabled

    def alert_info(self, alert=None) -> bool:
        elem = self.d.find_element(
            *DepositPageLocators.INVALID_COMBINATION_SUM_AND_DATE
        )
        logger.info(f"Message: {elem.text}")
        return elem.is_displayed()

    def error_message(self) -> str:
        elem = self.d.find_element(*DepositPageLocators.ERROR_MESSAGE)
        logger.info(f"Message: {elem.text}")
        return elem.text
