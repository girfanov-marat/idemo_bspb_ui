import allure
from pytest import mark

from common.accounts_page import (
    CREATE_ACCOUNT_SUCCESS,
    close_account_message,
    statement_period,
    EMAIL_SUCCESS_MESSAGE,
)
from utils.decorators import decorate_class_methods, start_finish_method_logger


@decorate_class_methods(start_finish_method_logger)
@allure.feature("Проверка блока: Счета")
class TestAccounts:
    @allure.tag("Счета")
    @allure.description("Тест проверяет открытие счета")
    @allure.suite("Открытие счета")
    def test_open_new_account(self, app):
        """
        1. Перейти на вкладку "Счета-Текущие"
        2. Нажать кнопку "Открыть счет"
        3. Проставить чекбокс согласия с правилами
        4. Нажать кнопку "Открыть счет"
        5. Нажать кнопку "Подтвердить"
        :param app:
        :return:
        """
        app.open_page(app.accounts_url)
        app.account_page.open_account_button_ckick()
        app.account_page.terms_checkbox_click()
        app.account_page.submit_button_click()
        app.confirm_with_switch_frame()
        assert app.alert_info("success").__contains__(
            CREATE_ACCOUNT_SUCCESS
        ), "Не удалось открыть новый счет"

    @mark.xfail
    @allure.tag("Счета")
    @allure.description("Тест проверяет закрытие счета")
    @allure.suite("Закрытие счета")
    def test_close_account(self, app):
        """
        1. Перейти на вкладку "Счета-Текущие"
        2. Выбрать счет с неотрицательным и незарезервирированным балансом
        3. Нажать на шестеренку выбранного счета
        4. Нажать кнопку "Закрыть счет"
        5. Нажать кнопку "Дальше"
        6. Нажать кнопку "Подтвердить"
        """
        app.open_page(app.accounts_url)
        app.account_page.close_selected_account()
        acc_name = app.account_page.ACCOUNT_NAME
        app.confirm_with_switch_frame()
        assert app.alert_info("success") == close_account_message(
            acc_name
        ), f"Не удалось закрыть счет {acc_name}"

    @allure.tag("Счета")
    @allure.description("Тест проверяет получение выписки")
    @allure.suite("Выписка")
    def test_create_statement(self, app, date_from="21082020", date_until="28082020"):
        """
        1. Перейти на вкладку "Счета-Выписка"
        2. Выбрать период
        3. Нажать кнопку "Получить"
        """
        app.open_page(app.statement_url)
        app.account_page.set_date(date_from, date_until)
        app.account_page.get_button()
        assert app.account_page.date_on_page() == statement_period(
            date_from, date_until
        ), "Введенный период не совпадает с полученным"

    @allure.tag("Счета")
    @allure.description("Тест проверяет получение выписки на емейл")
    @allure.suite("Выписка")
    def test_get_statement_on_email(self, app, format="PDF", email="test@mail.com"):
        """
        1. Перейти на вкладку "Счета-Выписка"
        2. Выбрать период
        3. Нажать кнопку "На email"
        4. Выбрать формат - "PDF" или "EXCEL"
        5. Нажать кнопку "Отправить"
        """
        app.open_page(app.statement_url)
        app.account_page.email_button(format)
        app.account_page.insert_email(email)
        app.account_page.send_button()
        assert app.account_page.email_success_message() == EMAIL_SUCCESS_MESSAGE
