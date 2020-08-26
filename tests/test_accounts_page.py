

class TestAccounts:

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
        app.account_page.confirm_button_click()
        assert app.alert_info("success") == CREATE_ACCOUNT_SUCCESS

    def test_close_account(self, app):
        """
        1. Перейти на вкладку "Счета-Текущие"
        2. Выбрать счет с неотрицательным и незарезервирированным балансом
        3. Нажать на шестеренку выбранного счета
        4. Нажать кнопку "Заркыть счет"
        5. Нажать кнопку "Дальше"
        6. Нажать кнопку "Подтвердить"
        """
        app.open_page(app.accounts_url)
        app.account_page.select_account_toggle()
        app.account_page.close_account_button()
        app.account_page.forward_button_click()
        app.account_page.confirm_button_click()
        assert app.alert_info("success") == CLOSE_ACCOUNT_SUCCESS