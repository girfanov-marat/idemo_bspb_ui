import allure
from pytest import mark
from common.deposit_page import ALERT_INFO_SUCCESS
from models.deposit_page import DepositData


@allure.feature("Проверка блока: Вклады")
class TestCredits:
    @allure.tag("Вклады")
    @allure.description("Тест проверяет открытие вклада")
    @allure.suite("Заявка на кредит или кредитную карту")
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
        assert app.alert_info(alert_type) == alert_info, "Alert invalid"
