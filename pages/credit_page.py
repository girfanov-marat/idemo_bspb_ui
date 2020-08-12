import allure

from locators.credit_page import CreditPageLocators
from pages.base_page import BasePage


class CreditPage(BasePage):
    loan_types = {
        "personal_loan": CreditPageLocators.PERSONAL_LOAN_BUTTON,
        "credit_card": CreditPageLocators.CREDIT_CARD_BUTTON,
        "credit_limit": CreditPageLocators.CREDIT_LIMIT_LOAN_BUTTON,
        "car_loan": CreditPageLocators.CAR_LOAN_BUTTON,
        "mortgage_loan": CreditPageLocators.MORTGAGE_LOAN_BUTTON,
        "refinance_loan": CreditPageLocators.REFINANCE_LOAN_BUTTON,
    }

    @allure.step("Нажатие кнопки 'Заявка на кредит или кредитную карту'")
    def create_loan(self):
        return self.d.find_element(*CreditPageLocators.CREATE_LOAN_BUTTON).click()

    @allure.step("Нажатие кнопки {loan_type}")
    def select_loan(self, loan_type):
        return self.d.find_element(*self.loan_types[loan_type]).click()

    @allure.step("Нажатие кнопки 'Персональный кредит'")
    def personal_loan(self):
        return self.d.find_element(*CreditPageLocators.PERSONAL_LOAN_BUTTON).click()

    def alert_info(self, loan_type):
        if loan_type == "refinance_loan":
            self.wait.until\
                (self.ex.presence_of_element_located(CreditPageLocators.MODAL_WINDOW))
            alert = self.d.find_element(*CreditPageLocators.REFINANCE_ALERT_INFO).text
        else:
            alert = self.d.find_element(*CreditPageLocators.ALERT_INFO).text
        return alert
