from selenium.webdriver.common.by import By


class MainPageLocators:
    ALERT_SUCCESS_INFO = (By.XPATH, '//div[@class="alert alert-success"]')
    ALERT_INFO = (By.XPATH, '//div[@class="alert alert-info"]')
    ALERT_ERROR = (By.XPATH, 'div[@class="alert alert-error"')
