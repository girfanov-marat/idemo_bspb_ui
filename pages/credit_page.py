import logging

import allure
from selenium.common.exceptions import NoSuchWindowException

from locators.credit_page import CreditPageLocators
from pages.base_page import BasePage

logger = logging.getLogger()


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

    def wait_modal_window(self):
        self.wait.until(
            self.ex.presence_of_element_located(CreditPageLocators.MODAL_WINDOW)
        )

    def alert_info(self, alert_type: str):
        if alert_type == "success":
            alert = self.d.find_element(*CreditPageLocators.ALERT_SUCCESS_INFO)
        elif alert_type == "info":
            alert = self.d.find_element(*CreditPageLocators.ALERT_INFO)
        else:
            return "No alert message"
        self.wait.until(self.ex.visibility_of(alert))
        message = alert.text
        logger.info(f"Alert text = {message}")
        return message

    def contracts(self):
        return len(self.d.find_elements(*CreditPageLocators.CONTRACTS))

    def submitted_applications(self):
        return len(self.d.find_elements(*CreditPageLocators.SUBMITTED_APPLICATIONS))

    @allure.step('Нажатие кнопки "Получить" на страницу Кредиты')
    def first_submitted_application_receive(self):
        locator = CreditPageLocators.SUB_APPLICATIONS_RECEIVE_BUTTONS
        return self.d.find_elements(*locator)[0].click()

    @allure.step("Нажатие кнопки продолжить в окне Параметры договора")
    def first_submitted_application_continue(self):
        return self.d.find_element(*CreditPageLocators.CONTINIUE_BUTTON).click()

    @allure.step("Нажатие кнопки продолжить в окне Уточнение параметров договора")
    def first_submitted_application_loan_claim_continue(self):
        return self.d.find_element(
            *CreditPageLocators.CONTINIUE_LOAN_CLAIM_BUTTON
        ).click()

    @allure.step("Нажатие шестеренки на строке первого договора")
    def first_contract_toggle(self):
        """Нажимает на шестеренку первого документа"""
        return self.d.find_elements(*CreditPageLocators.CONTRACT_TOGGLE)[0].click()

    def first_contract_id(self):
        """Вытаскивает id первого документа"""
        return self.d.find_elements(*CreditPageLocators.CONTRACTS)[0].get_attribute(
            "data-loan-id"
        )

    def loan_full_repayment(self):
        """Выбирает первое значение из выпадающего списка действий"""
        return self.d.find_elements(*CreditPageLocators.DOCUMENT_ACTIONS)[0].click()

    @allure.step("Выбор второго значения из выпадающего списка офисов")
    def select_first_office(self):
        """Выбирает второе значение из выпадающего списка офисов"""
        return self.d.find_elements(*CreditPageLocators.OFFICE_LIST)[1].click()

    @allure.step("Нажатие кнопки отправить")
    def send_button(self):
        return self.d.find_element(*CreditPageLocators.SEND_BUTTON).click()

    @allure.step("Нажатие кнопки подтвердить")
    def confirm_button(self):
        return self.d.find_element(*CreditPageLocators.CONFIRM_BUTTON).click()

    def confirm_button_disabled(self):
        return not self.d.find_element(*CreditPageLocators.CONFIRM_BUTTON).is_enabled()

    def contract_num(self):
        return self.d.find_element(*CreditPageLocators.CONTRACT_NUM).text

    def office_field_attribute_class(self):
        return self.d.find_element(*CreditPageLocators.OFFICE_FIELD).get_attribute(
            "class"
        )

    @allure.step("Проставление всех чекбоксов на странице")
    def create_contract_set_all_checkboxes(self):
        """Проставляет все чек боксы на странице 'Подписание договора'."""
        checkboxes = self.d.find_elements(
            *CreditPageLocators.CONTRACT_SIGNING_CHECKBOXES
        )
        for checkbox in checkboxes:
            checkbox.click()
            if checkbox.get_attribute("name") == "condition.personalTerms":
                terms = self.d.find_elements(*CreditPageLocators.PERSONAL_TERMS)
                last_term = terms[len(terms) - 1]
                self.d.execute_script("arguments[0].scrollIntoView();", last_term)
                self.d.find_element(
                    *CreditPageLocators.PERSONAL_TERMS_AGREEMENT_BUTTON
                ).click()

    def confirm_with_switch_frame(self):
        self.wait.until(
            self.ex.frame_to_be_available_and_switch_to_it(CreditPageLocators.IFRAME)
        )
        try:
            self.confirm_button()
        except NoSuchWindowException:
            self.wait.until(
                self.ex.visibility_of(
                    self.d.find_element(*CreditPageLocators.CONFIRM_BUTTON)
                )
            )
            self.confirm_button()
        self.d.switch_to.default_content()

    def create_new_statement(self):
        self.select_first_office()
        self.send_button()
        self.confirm_with_switch_frame()
