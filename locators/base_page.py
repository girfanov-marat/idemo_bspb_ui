from selenium.webdriver.common.by import By


class BasePageLocators:
    CONFIRM_BUTTON = (By.XPATH, '//button[@id="confirm"]')
    IFRAME = (By.XPATH, '//iframe[@id="confirmation-frame"]')
