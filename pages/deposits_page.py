import time

import allure
from selenium.common.exceptions import NoSuchElementException

from locators.deposit_page import DepositPageLocators
from pages.base_page import BasePage


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
        return self.d.find_element(*DepositPageLocators.OPEN_DEPOSIT_BUTTON).click()

    @allure.step("Выбор фильтров: валюта: {currency}, на срок: {min_days}")
    def set_filters(self, currency, min_days):
        if currency not in self.deposit_currency.keys():
            raise Exception("invalid currency")
        if min_days not in self.deposit_min_days.keys():
            raise Exception("invalid min_days")
        currency_radio = self.deposit_currency[currency]
        min_days_radio = self.deposit_min_days[min_days]
        self.d.find_element(*currency_radio).click()
        self.d.find_element(*min_days_radio).click()

    @allure.step("Нажате кнопки 'открыть вклад' у первого вклада из списка")
    def open_first_deposit(self):
        try:
            self.d.find_elements(*DepositPageLocators.OPEN_DEPOSIT_BUTTONS)[0].click()
            return True
        except NoSuchElementException:
            return False

    def add_data(self, end_data, summ, prolongation):
        self.d.find_element(*DepositPageLocators.DATE_FIELD).clear()
        self.d.find_element(*DepositPageLocators.DATE_FIELD).send_keys(end_data)
        self.d.find_element(*DepositPageLocators.SUMM_FIELD).send_keys(summ)
        time.sleep(1)
        if not prolongation:
            self.d.find_element(*DepositPageLocators.PROLONGATION_CHECKBOX).click()

    @allure.step("Нажатие кнопки 'Дальше' на странице открытия вклада")
    def submit(self):
        return self.d.find_element(*DepositPageLocators.SUBMIT_BUTTON).click()

    @allure.step("Проставление чекбокса")
    def agree_with_terms(self):
        return self.d.find_element(
            *DepositPageLocators.TERMS_AGREEMENT_CHECKBOX
        ).click()

    @allure.step("Нажатие кнопки 'Подтвердить' на странице открытия вклада")
    def confirm(self):
        return self.d.find_element(*DepositPageLocators.CONFIRM_BUTTON).click()
