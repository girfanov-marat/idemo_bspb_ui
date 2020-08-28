import logging

import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from locators.deposit_page import DepositPageLocators
from pages.base_page import BasePage

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

    @allure.step("Нажатие кнопки 'Открыть вклад'")
    def open_deposit(self):
        logger.info("Нажатие кнопки 'Открыть вклад'")
        self.d.find_element(*DepositPageLocators.OPEN_DEPOSIT_BUTTON).click()

    @allure.step("Выбор фильтров: валюта: {currency}, на срок: {min_days}")
    def set_filters(self, currency, min_days):
        logger.info(f"Установка фильтров: валюта - {currency}, срок - {min_days}")
        if currency not in self.deposit_currency.keys():
            logger.error("Некорректная валюта")
            raise Exception("Некорректная валюта")
        if min_days not in self.deposit_min_days.keys():
            logger.error("Некорректный срок")
            raise Exception("Некорректный срок")
        currency_radio = self.deposit_currency[currency]
        min_days_radio = self.deposit_min_days[min_days]
        self.d.find_element(*currency_radio).click()
        self.d.find_element(*min_days_radio).click()

    @allure.step("Нажатие кнопки 'открыть вклад' у первого вклада из списка")
    def open_first_deposit(self) -> bool:
        try:
            logger.info("Нажатие кнопки 'открыть вклад' у первого вклада из списка")
            self.d.find_elements(*DepositPageLocators.OPEN_DEPOSIT_BUTTONS)[0].click()
            return True
        except NoSuchElementException:
            return False

    def add_data(self, end_data, summ, prolongation):
        logger.info(
            f"Проставление данных: дата окончания - {end_data}, сумма - {summ}, "
            f"автоматическое продление - "
            f"{prolongation}"
        )
        self.d.find_element(*DepositPageLocators.DATE_FIELD).clear()
        self.d.find_element(*DepositPageLocators.DATE_FIELD).send_keys(end_data)
        self.d.find_element(*DepositPageLocators.SUMM_FIELD).send_keys(summ)
        if not prolongation:
            self.d.find_element(*DepositPageLocators.PROLONGATION_CHECKBOX).click()

    def add_data_without_end_date(self, summ, prolongation):
        logger.info(
            f"Проставление данных: сумма - {summ}, автоматическое продление "
            f"- {prolongation}"
        )
        self.d.find_element(*DepositPageLocators.SUMM_FIELD).send_keys(summ)
        if not prolongation:
            self.d.find_element(*DepositPageLocators.PROLONGATION_CHECKBOX).click()

    @allure.step("Нажатие кнопки 'Дальше' на странице открытия вклада")
    def submit(self):
        elem = self.d.find_element(*DepositPageLocators.INTEREST_RATE_VALUE)
        self.wait.until(
            self.custom_ex.text_is_not_empty(DepositPageLocators.INTEREST_RATE_VALUE)
        )
        element_text = elem.text
        logger.info(f"Оценочный доход = {element_text}")
        self.d.find_element(*DepositPageLocators.SUBMIT_BUTTON).click()
        logger.info("Нажатие кнопки 'Дальше' на странице открытия вклада")

    @allure.step("Нажатие кнопки 'Дальше' на странице открытия вклада")
    def simple_submit(self):
        logger.info("Нажатие кнопки 'Дальше' на странице открытия вклада")
        self.d.find_element(*DepositPageLocators.SUBMIT_BUTTON).click()

    @allure.step("Проставление чекбокса согласия с правилами")
    def agree_with_terms(self):
        logger.info("Проставление чекбокса согласия с правилами")
        self.d.find_element(*DepositPageLocators.TERMS_AGREEMENT_CHECKBOX).click()

    @allure.step("Нажатие кнопки 'Подтвердить' на странице открытия вклада")
    def confirm(self):
        confirm_button = self.d.find_element(*DepositPageLocators.CONFIRM_BUTTON)
        logger.info(f"Кнопка подтвердить: {confirm_button.is_enabled()}")
        confirm_button.click()
        logger.info("Нажатие кнопки 'Подтвердить' на странице открытия вклада")

    def confirm_is_enabled(self):
        enabled = self.d.find_element(*DepositPageLocators.CONFIRM_BUTTON).is_enabled()
        logger.info(f"Кнопка подтвердить: {enabled}")
        return not enabled

    def alert_info(self, alert=None) -> bool:
        elem = self.d.find_element(
            *DepositPageLocators.INVALID_COMBINATION_SUM_AND_DATE
        )
        logger.info(f"Сообщение об открытии вклада: {elem.text}")
        return elem.is_displayed()

    def error_message(self) -> str:
        elem = self.d.find_element(*DepositPageLocators.ERROR_MESSAGE)
        logger.info(f"Сообщение о недостатке средств: {elem.text}")
        return elem.text

    def get_first_account_id(self):
        attr_name = self.d.find_element(
            *DepositPageLocators.FIRST_ACCOUNT
        ).get_attribute("id")
        logger.info(f"Id первого счета: {attr_name}")
        return attr_name

    @allure.step("Нажатие кнопки переименования счета")
    def rename_button(self):
        logger.info("Нажатие кнопки переименования счета")
        actions = ActionChains(self.d)
        elem = self.d.find_elements(*DepositPageLocators.RENAME_ACCOUNT_BUTTONS)[0]
        actions.move_to_element(elem).perform()
        elem.click()

    def text_to_field(self):
        return self.d.find_element(*DepositPageLocators.INPUT_FIELD)

    @allure.step("Изменение имени счета на {new_name}")
    def rename_account(self, new_name: str):
        self.rename_button()
        self.text_to_field().clear()
        self.text_to_field().send_keys(new_name)
        logger.info(f"Ввод текста '{new_name}' в поле ввода")
        self.text_to_field().send_keys(Keys.ENTER)
        logger.info("Нажатие кнопки 'ENTER'")

    def account_name(self, text):
        element = DepositPageLocators.FIRST_ACCOUNT
        self.wait.until(self.ex.text_to_be_present_in_element(element, text))
        text = self.d.find_element(*element).text
        logger.info(f"Имя первого счета в таблице счетов: {text}")
        return text
