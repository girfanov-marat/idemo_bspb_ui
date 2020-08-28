import logging

import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

from locators.accounts_page import AccountsPageLocators
from pages.base_page import BasePage

logger = logging.getLogger()


class AccountsPage(BasePage):
    ACCOUNT_NAME = None

    @allure.step("Нажатие кнопки 'Открыть вклад' на странице 'Счета-Текущие'")
    def open_account_button_ckick(self):
        logger.info("Нажатие кнопки 'Открыть вклад' на странице 'Счета-Текущие'")
        self.d.find_element(*AccountsPageLocators.OPEN_ACCOUNT_BUTTON).click()

    @allure.step("Проставление чекбокса согласия с правилами")
    def terms_checkbox_click(self):
        logger.info("Проставление чекбокса согласия с правилами")
        self.d.find_element(*AccountsPageLocators.TERMS_CHECKBOX).click()

    @allure.step("Нажатие кнопки 'Открыть счет' на странице открытия счета")
    def submit_button_click(self):
        logger.info("Нажатие кнопки 'Открыть счет' на странице открытия счета")
        self.d.find_element(*AccountsPageLocators.SUBMIT_BUTTON).click()

    def close_modal_window(self):
        self.d.find_element(*AccountsPageLocators.CLOSE_MODAL_WINDOW).click()

    @allure.step("Нажатие кнопки 'Дальше'")
    def forward_button(self):
        logger.info("Нажатие кнопки 'Дальше'")
        self.d.find_element(*AccountsPageLocators.FORWARD_BUTTON).click()

    def account_toggle(self, account: WebElement):
        return account.find_element(*AccountsPageLocators.ACCOUNT_TOGGLE)

    @allure.step("Нажатие шестеренки выбранного аккаунта")
    def select_account_toggle(self, acc: WebElement):
        logger.info("Нажатие шестеренки выбранного аккаунта")
        self.account_toggle(acc).click()

    @allure.step("Нажатие кнопки 'Закрыть счет'")
    def close_account(self, acc: WebElement):
        logger.info("Нажатие кнопки 'Закрыть счет'")
        acc.find_element(*AccountsPageLocators.CLOSE_ACCOUNT).click()

    @allure.step("Поиск аккаунта с не отрицательным и незарезервированным балансом")
    def close_selected_account(self):
        find = False
        logger.info("Поиск аккаунта с не отрицательным и незарезервированным балансом")
        accounts = self.d.find_elements(*AccountsPageLocators.ACCOUNTS)
        for acc in accounts:
            balance = acc.find_element(*AccountsPageLocators.COLUMN_AVAILABLE).text
            logger.info(f"Баланс: {balance}")
            if balance[0] != "-":
                reserved = acc.find_element(*AccountsPageLocators.COLUMN_RESERVED).text
                logger.info(f"Зарезервировано: {reserved}")
                if reserved.__contains__("0.00"):
                    try:
                        self.select_account_toggle(acc)
                        self.close_account(acc)
                        self.forward_button()
                        acc_name = acc.find_element(
                            *AccountsPageLocators.COLUMN_ACCOUNT_NAME
                        ).text
                        self.ACCOUNT_NAME = acc_name
                        logger.info(f"Имя выбранного счета: {acc_name}")
                        find = True
                        break
                    except NoSuchElementException:
                        self.wait.until(
                            self.ex.presence_of_element_located(
                                AccountsPageLocators.CLOSE_MODAL_WINDOW
                            )
                        )
                        self.close_modal_window()
                        continue
        if not find:
            raise Exception("Нет подходящего счета")

    def set_date(self, date_from: str, date_until: str):
        """Заполнение полей периода выписки"""
        logger.info(f"Период: {date_from} - {date_until}")
        from_field = self.d.find_element(*AccountsPageLocators.DATE_FROM_INPUT_FIELD)
        until_field = self.d.find_element(*AccountsPageLocators.DATE_UNTIL_INPUT_FIELD)
        from_field.clear()
        from_field.send_keys(date_from)
        until_field.clear()
        until_field.send_keys(date_until)

    @allure.step("Нажатие кнопки 'Получить'")
    def get_button(self):
        logger.info("Нажатие кнопки 'Получить'")
        self.d.find_element(*AccountsPageLocators.GET_BUTTON).click()

    def date_on_page(self):
        elem = AccountsPageLocators.DATE_ON_PAGE
        self.wait.until(self.ex.presence_of_element_located(elem))
        return self.d.find_element(*elem).text

    @allure.step("Нажатие кнопки 'По емейлу' и выбор формата {file_format}")
    def email_button(self, file_format: str):
        logger.info("Нажатие кнопки 'По емейлу'")
        self.d.find_element(*AccountsPageLocators.ON_EMAIL_BUTTON).click()
        logger.info(f"Выбранный формат: {file_format}")
        if file_format == "PDF":
            self.d.find_element(*AccountsPageLocators.PDF_BUTTON).click()
        elif file_format == "EXCEL":
            self.d.find_element(*AccountsPageLocators.EXCEL_BUTTON).click()
        else:
            raise Exception("Некорректный формат файла")

    @allure.step("Ввод емейла: {email}")
    def insert_email(self, email: str):
        logger.info(f"Введеный емейл: {email}")
        self.d.find_element(*AccountsPageLocators.EMAIL_FIELD).send_keys(email)

    @allure.step("Нажатие кнопки 'Отправить'")
    def send_button(self):
        logger.info("Нажатие кнопки 'Отправить'")
        self.d.find_element(*AccountsPageLocators.SEND_BUTTON).click()

    def email_success_message(self):
        return self.d.find_element(*AccountsPageLocators.EMAIL_SUCCESS_MESSAGE).text
