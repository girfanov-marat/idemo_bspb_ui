from selenium.webdriver.common.by import By


class CreditPageLocators:
    CREATE_LOAN_BUTTON = (
        By.XPATH,
        '//div[@class="form-actions"]//a[' '@id="loan-application-btn"]',
    )
    PERSONAL_LOAN_BUTTON = (By.XPATH, '//button[@id="personal-loan-apply"]')
    CREDIT_CARD_BUTTON = (By.XPATH, '//button[@id="credit-card-loan-apply"]')
    CREDIT_LIMIT_LOAN_BUTTON = (By.XPATH, '//button[@id="credit-limit-loan-apply"]')
    CAR_LOAN_BUTTON = (By.XPATH, '//button[@id="car-loan-apply"]')
    MORTGAGE_LOAN_BUTTON = (By.XPATH, '//button[@id="mortgage-loan-apply"]')
    REFINANCE_LOAN_BUTTON = (By.XPATH, '//button[@id="refinance-loan-callback"]')
    REFINANCE_ALERT_INFO = (By.XPATH, '//div[@class="alert alert-success"]')
    ALERT_INFO = (By.XPATH, '//div[@class="alert alert-info"]')
    MODAL_WINDOW = (By.XPATH, '//div[@class="modal hidden in"]')
