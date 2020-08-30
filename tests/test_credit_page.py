import allure
from pytest import mark

from common.credit_page import (
    ALERT_INFO_TEXT,
    REFINANCE_ALERT_INFO_TEXT,
    CREATE_STATEMENT_ALERT_SUCCESS,
    create_credit_success,
)
from utils.decorators import decorate_class_methods, start_finish_method_logger


@decorate_class_methods(start_finish_method_logger)
@allure.feature("Проверка блока: Кредиты")
class TestCredits:
    @allure.tag("Кредиты")
    @allure.description("Тест проверяет создание заявки на кредит или кредитную карту")
    @allure.suite("Заявка на кредит или кредитную карту")
    @mark.parametrize(
        "loan_type, alert_info, alert_type",
        [
            ("personal_loan", ALERT_INFO_TEXT, "info"),
            ("credit_card", ALERT_INFO_TEXT, "info"),
            ("credit_limit", ALERT_INFO_TEXT, "info"),
            ("car_loan", ALERT_INFO_TEXT, "info"),
            ("mortgage_loan", ALERT_INFO_TEXT, "info"),
            ("refinance_loan", REFINANCE_ALERT_INFO_TEXT, "success"),
        ],
    )
    def test_create_loan(self, app, loan_type, alert_info, alert_type):
        """
        1. Открытие страницы 'Кредиты'
        2. Нажатие кнопки 'Заявка на кредит или кредитную карту'
        3. Выбор типа кредита
        """
        app.open_page(app.credit_url)
        app.credit_page.create_loan()
        app.credit_page.select_loan(loan_type)
        assert app.alert_info(alert_type) == alert_info, "Alert invalid"

    @allure.tag("Кредиты")
    @allure.suite("Заявление на досрочное погашение")
    @allure.description("Тест проверяет создание заявления на досрочное погашение")
    def test_create_loan_full_repayment(self, app):
        """
        1. Открыть страницу 'Кредиты'
        2. Нажатие кнопку 'действия' у первого договора в списке
        3. Выборать пункт 'заявление на досрочное погашение'
        4. Выбрать первое значение из выпадающего списка офисов
        5. Нажать кнопку отправить
        6. Нажать кнопку подтвердить
        """
        app.open_page(app.credit_url)
        doc_id = app.credit_page.first_contract_id()
        app.credit_page.first_contract_toggle()
        app.credit_page.loan_full_repayment()
        app.wait.until(app.ex.url_to_be(app.loan_full_repayment_url(doc_id)))
        app.credit_page.create_new_statement()
        assert (
            app.alert_info("success") == CREATE_STATEMENT_ALERT_SUCCESS
        ), "Ошибка при создании заявления"

    @allure.tag("Кредиты")
    @allure.suite("Заявление на досрочное погашение")
    @allure.description(
        "Тест проверяет создание заявления на досрочное погашение, "
        "без выбора конкретного офиса"
    )
    def test_create_loan_full_repayment_without_office(self, app):
        """
        1. Открыть страницу 'Кредиты'
        2. Нажатие кнопку 'действия' у первого договора в списке
        3. Выборать пункт 'заявление на досрочное погашение'
        4. Нажать кнопку отправить
        """
        app.open_page(app.credit_url)
        doc_id = app.credit_page.first_contract_id()
        app.credit_page.first_contract_toggle()
        app.credit_page.loan_full_repayment()
        app.wait.until(app.ex.url_to_be(app.loan_full_repayment_url(doc_id)))
        app.credit_page.send_button()
        assert app.credit_page.office_field_attribute_class() == "span5 required error"

    @allure.tag("Кредиты")
    @allure.suite("Создание договора на получение кредита")
    @allure.description("Тест проверяет создание договора на получение кредита")
    def test_create_credit_contract(self, app):
        """
        1. Открыть страницу 'Кредиты'
        2. Нажать кнопку 'Получить' у первой заявки в списке 'Поданные заявки'
        3. Нажать кнопку 'Продолжить' на странице Параметры договора
        4. Нажать кнопку 'Продолжить' на странице Уточнение параметров договора
        5. Проставить все чек боксы
        6. Нажать кнопку 'Подтвердить'
        """
        app.open_page(app.credit_url)
        assert (
            app.credit_page.submitted_applications() != 0
        ), "Отсутствуют доступные к получению кредиты"
        app.credit_page.first_submitted_application_receive()
        app.credit_page.first_submitted_application_continue()
        app.credit_page.first_submitted_application_loan_claim_continue()
        contract_number = app.credit_page.contract_num()
        app.credit_page.create_contract_set_all_checkboxes()
        app.credit_page.confirm_with_switch_frame()
        assert app.alert_info("success") == create_credit_success(contract_number)

    @mark.xfail
    @allure.tag("Кредиты")
    @allure.suite("Создание договора на получение кредита")
    @allure.description(
        "Тест проверяет создание договора на получение "
        "кредита без проставленных чекбоксов на странице "
        "подписания договора"
    )
    def test_create_credit_contract_without_check_checkboxes(self, app):
        """
        1. Открыть страницу 'Кредиты'
        2. Нажать кнопку 'Получить' у первой заявки в списке 'Поданные заявки'
        3. Нажать кнопку 'Продолжить' на странице Параметры договора
        4. Нажать кнопку 'Продолжить' на странице Уточнение параметров договора
        """
        app.open_page(app.credit_url)
        assert (
            app.credit_page.submitted_applications() != 0
        ), "Отсутствуют доступные к получению кредиты"
        app.credit_page.first_submitted_application_receive()
        app.credit_page.first_submitted_application_continue()
        app.credit_page.first_submitted_application_loan_claim_continue()
        assert app.credit_page.confirm_button_disabled()
