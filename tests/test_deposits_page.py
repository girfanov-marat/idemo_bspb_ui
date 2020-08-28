import allure
from pytest import mark
from selenium.common.exceptions import ElementClickInterceptedException
from common.deposit_page import ALERT_INFO_SUCCESS, ERROR_MESSAGE
from models.deposit_page import DepositData
from utils.decorators import start_finish_method_logger, decorate_class_methods


@decorate_class_methods(start_finish_method_logger)
@allure.feature("Проверка блока: Вклады")
class TestDeposits:
    @allure.tag("Вклады")
    @allure.description("Тест проверяет открытие вклада")
    @allure.suite("Открытие вклада")
    @mark.parametrize(
        "currency, min_days, end_date, summ, prolongation, alert_type, alert_info",
        [("USD", "91", "21092021", "1000", True, "success", ALERT_INFO_SUCCESS)],
    )
    def test_create_deposit(
        self,
        app,
        currency,
        min_days,
        end_date,
        summ,
        prolongation,
        alert_type,
        alert_info,
    ):
        """
        1. Перейти на вкладку "Кредиты"
        2. Нажать кнопку "Открыть вклад"
        3. Установить фильтры
        4. Выбрать первый доступный вклад и нажать кнопку "Открыть вклад"
        5. Ввести дату окончачния, сумму, выбрать/убрать галочку "автоматически
        продлевать на новый срок"
        6. Нажать кнопку "Дальше"
        7. Проставить чекбокс согласия с правилами
        8. Нажать кнопку "Подтвердить"
        """
        deposit = DepositData(end_date, summ, prolongation)
        app.open_page(app.deposit_url)
        app.deposit_page.open_deposit()
        app.deposit_page.set_filters(currency, min_days)
        assert (
            app.deposit_page.open_first_deposit()
        ), "Нет доступных депозитов по выбранным фильтрам"
        app.deposit_page.add_data(deposit.end_date, deposit.summ, deposit.prolongation)
        app.deposit_page.submit()
        app.deposit_page.agree_with_terms()
        app.deposit_page.confirm()
        assert (
            app.alert_info(alert_type) == alert_info
        ), "Некорректное оповещение об успешном создании вклада "

    @allure.tag("Вклады")
    @allure.description(
        "Тест проверяет открытие вклада без проставления чекбокса о "
        "согласии с правилами"
    )
    @allure.suite("Открытие вклада")
    @mark.parametrize(
        "currency, min_days, end_date, summ, prolongation",
        [("USD", "91", "21092021", "1000", True)],
    )
    def test_create_deposit_without_agreemnt(
        self, app, currency, min_days, end_date, summ, prolongation
    ):
        """
        1. Перейти на вкладку "Кредиты"
        2. Нажать кнопку "Открыть вклад"
        3. Установить фильтры
        4. Выбрать первый доступный вклад и нажать кнопку "Открыть вклад"
        5. Ввести дату окончачния, сумму, выбрать/убрать галочку "автоматически
        продлевать на новый срок"
        6. Нажать кнопку "Дальше"
        7. Проставить чекбокс согласия с правилами
        8. Нажать кнопку "Подтвердить"
        """
        deposit = DepositData(end_date, summ, prolongation)
        app.open_page(app.deposit_url)
        app.deposit_page.open_deposit()
        app.deposit_page.set_filters(currency, min_days)
        assert (
            app.deposit_page.open_first_deposit()
        ), "Нет доступных депозитов по выбранным фильтрам"
        app.deposit_page.add_data(deposit.end_date, deposit.summ, deposit.prolongation)
        app.deposit_page.submit()
        try:
            app.deposit_page.confirm()
            assert False
        except ElementClickInterceptedException:
            assert app.deposit_page.confirm_is_enabled(), "Кнопка 'Подтвердить' активна"

    @allure.tag("Вклады")
    @allure.description(
        "Тест проверяет открытие вклада c некорректной датой или суммой"
    )
    @allure.suite("Открытие вклада")
    @mark.parametrize(
        "currency, min_days, end_date, summ, prolongation",
        [("RUB", "-1", "01011969", "1000", True), ("RUB", "-1", "21092021", "0", True)],
    )
    def test_create_deposit_negative_date_sum(
        self, app, currency, min_days, end_date, summ, prolongation
    ):
        """
        1. Перейти на вкладку "Кредиты"
        2. Нажать кнопку "Открыть вклад"
        3. Установить фильтры
        4. Выбрать первый доступный вклад и нажать кнопку "Открыть вклад"
        5. Ввести дату окончачния, сумму, выбрать/убрать галочку "автоматически
        продлевать на новый срок"
        6. Нажать кнопку "Дальше"
        """
        deposit = DepositData(end_date, summ, prolongation)
        app.open_page(app.deposit_url)
        app.deposit_page.open_deposit()
        app.deposit_page.set_filters(currency, min_days)
        assert (
            app.deposit_page.open_first_deposit()
        ), "Нет доступных депозитов по выбранным фильтрам"
        app.deposit_page.add_data(deposit.end_date, deposit.summ, deposit.prolongation)
        app.deposit_page.simple_submit()
        assert (
            app.deposit_page.alert_info()
        ), "Сообщение о некорректной дате или сумме не отобразилось "

    @allure.tag("Вклады")
    @allure.description("Тест проверяет открытие вклада c отрицательного счета")
    @allure.suite("Открытие вклада")
    @mark.parametrize(
        "currency, min_days, summ, prolongation", [("EUR", "91", "1500", True)]
    )
    def test_create_deposit_negative_account_balance(
        self, app, currency, min_days, summ, prolongation
    ):
        """
        1. Перейти на вкладку "Кредиты"
        2. Нажать кнопку "Открыть вклад"
        3. Установить фильтры
        4. Выбрать первый доступный вклад и нажать кнопку "Открыть вклад"
        5. Ввести дату окончачния, сумму, выбрать/убрать галочку "автоматически
        продлевать на новый срок"
        6. Нажать кнопку "Дальше"
        """
        deposit = DepositData(summ=summ, prolongation=prolongation)
        app.open_page(app.deposit_url)
        app.deposit_page.open_deposit()
        app.deposit_page.set_filters(currency, min_days)
        assert (
            app.deposit_page.open_first_deposit()
        ), "Нет доступных депозитов по выбранным фильтрам"
        app.deposit_page.add_data_without_end_date(deposit.summ, deposit.prolongation)
        app.deposit_page.submit()
        assert (
            app.deposit_page.error_message() == ERROR_MESSAGE
        ), "Сообщение 'Недостаточно средств на счёте' не отобразилось "

    @allure.tag("Вклады")
    @allure.description(
        "Тест проверяет переименование первого счета на странице " "вкладов"
    )
    @allure.suite("Переименование счета")
    @mark.xfail
    def test_rename_account(self, app, new_name="new_account_name"):
        """
        1. Перейти на вкладку "Кредиты"
        2. Нажать кнопку переименование счета возле названия счета
        3. Ввести текст
        4. Нажать кнопку "ENTER"
        """
        app.open_page(app.deposit_url)
        app.deposit_page.rename_account(new_name)
        assert app.deposit_page.account_name(new_name)
