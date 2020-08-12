from pytest import mark

from common.credit_page import ALERT_INFO_TEXT, REFINANCE_ALERT_INFO_TEXT


class TestLoanRequest:
    @mark.parametrize(
        "loan_type, alert_info",
        [
            ("personal_loan", ALERT_INFO_TEXT),
            ("credit_card", ALERT_INFO_TEXT),
            ("credit_limit", ALERT_INFO_TEXT),
            ("car_loan", ALERT_INFO_TEXT),
            ("mortgage_loan", ALERT_INFO_TEXT),
            ("refinance_loan", REFINANCE_ALERT_INFO_TEXT),
        ],
    )
    def test_create_loan(self, app, loan_type, alert_info):
        """
        1. Открытие страницы 'Кредиты'
        2. Нажатие кнопки 'Заявка на кредит или кредитную карту'
        3. Выбор типа кредита
        """
        app.open_page(app.credit_url)
        app.credit_page.create_loan()
        app.credit_page.select_loan(loan_type)
        assert app.credit_page.alert_info(loan_type) == alert_info
