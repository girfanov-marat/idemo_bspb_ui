import logging

import allure

from locators.base_page import BasePageLocators
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
        logger.info("Нажатие кнопки 'Заявка на кредит или кредитную карту'")
        return self.d.find_element(*CreditPageLocators.CREATE_LOAN_BUTTON).click()

    @allure.step("Нажатие кнопки {loan_type}")
    def select_loan(self, loan_type):
        logger.info(f"Нажатие кнопки '{loan_type}'")
        return self.d.find_element(*self.loan_types[loan_type]).click()

    @allure.step("Нажатие кнопки 'Персональный кредит'")
    def personal_loan(self):
        logger.info("Нажатие кнопки 'Персональный кредит'")
        return self.d.find_element(*CreditPageLocators.PERSONAL_LOAN_BUTTON).click()

    def wait_modal_window(self):
        self.wait.until(
            self.ex.presence_of_element_located(CreditPageLocators.MODAL_WINDOW)
        )

    def submitted_applications(self):
        count = len(self.d.find_elements(*CreditPageLocators.SUBMITTED_APPLICATIONS))
        logger.info(f"Количество доступных к получению кредитов: {count}")
        return count

    @allure.step("Нажатие кнопки 'Получить' на страницу Кредиты")
    def first_submitted_application_receive(self):
        logger.info("Нажатие кнопки 'Получить' на страницу Кредиты")
        locator = CreditPageLocators.SUB_APPLICATIONS_RECEIVE_BUTTONS
        return self.d.find_elements(*locator)[0].click()

    @allure.step("Нажатие кнопки продолжить в окне Параметры договора")
    def first_submitted_application_continue(self):
        logger.info("Нажатие кнопки 'Продолжить' в окне Параметры договора")
        return self.d.find_element(*CreditPageLocators.CONTINIUE_BUTTON).click()

    @allure.step("Нажатие кнопки продолжить в окне Уточнение параметров договора")
    def first_submitted_application_loan_claim_continue(self):
        logger.info("Нажатие кнопки 'Продолжить' в окне Уточнение параметров договора")
        return self.d.find_element(
            *CreditPageLocators.CONTINIUE_LOAN_CLAIM_BUTTON
        ).click()

    @allure.step("Нажатие шестеренки на строке первого договора")
    def first_contract_toggle(self):
        logger.info("Нажатие шестеренки на строке первого договора")
        return self.d.find_elements(*CreditPageLocators.CONTRACT_TOGGLE)[0].click()

    def first_contract_id(self):
        """Вытаскивает id первого договора"""
        first_doc_id = self.d.find_elements(*CreditPageLocators.CONTRACTS)[
            0
        ].get_attribute("data-loan-id")
        logger.info(f"Id первого договора: {first_doc_id}")
        return first_doc_id

    def loan_full_repayment(self):
        """Выбирает первое значение из выпадающего списка действий"""
        logger.info("Выбор первого значения из выпадающего списка действий")
        return self.d.find_elements(*CreditPageLocators.DOCUMENT_ACTIONS)[0].click()

    @allure.step("Выбор второго значения из выпадающего списка офисов")
    def select_first_office(self):
        logger.info("Выбор второго значения из выпадающего списка офисов")
        return self.d.find_elements(*CreditPageLocators.OFFICE_LIST)[1].click()

    @allure.step("Нажатие кнопки 'Отправить'")
    def send_button(self):
        logger.info("Нажатие кнопки 'Отправить'")
        return self.d.find_element(*CreditPageLocators.SEND_BUTTON).click()

    def confirm_button_disabled(self):
        logger.info("Переключение на фрейм")
        self.wait.until(
            self.ex.frame_to_be_available_and_switch_to_it(BasePageLocators.IFRAME)
        )
        button_state = self.d.find_element(
            *CreditPageLocators.CONFIRM_BUTTON
        ).is_enabled()
        logger.info(f"Статус кнопки 'Подтвердить':{button_state}")
        logger.info("Возврат в основное окно")
        self.d.switch_to.default_content()
        return not button_state

    def contract_num(self):
        elem = self.d.find_element(*CreditPageLocators.CONTRACT_NUM)
        self.wait.until(self.ex.visibility_of(elem))
        doc_num = elem.text
        logger.info(f"Номер документа: {doc_num}")
        return doc_num

    def office_field_attribute_class(self):
        attr_value = self.d.find_element(
            *CreditPageLocators.OFFICE_FIELD
        ).get_attribute("class")
        logger.info(f"Значение аттрибута class у поля 'Офис': {attr_value}")
        return attr_value

    @allure.step("Проставление всех чекбоксов на странице")
    def create_contract_set_all_checkboxes(self):
        logger.info("Проставление всех чекбоксов на странице")
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

    def create_new_statement(self):
        self.select_first_office()
        self.send_button()
        self.confirm_with_switch_frame()
