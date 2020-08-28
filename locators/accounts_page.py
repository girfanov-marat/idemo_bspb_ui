from selenium.webdriver.common.by import By


class AccountsPageLocators:
    OPEN_ACCOUNT_BUTTON = (By.XPATH, '//a[@class="btn btn-primary"]')
    TERMS_CHECKBOX = (By.XPATH, '//input[@type="checkbox"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@id="submit"]')
    ACCOUNTS = (By.XPATH, '//table[@id="accounts"]/tbody/tr')
    COLUMN_AVAILABLE = (By.XPATH, './/td[@class="right"][3]')
    COLUMN_RESERVED = (By.XPATH, './/td[@class="right"][2]')
    COLUMN_ACCOUNT_NAME = (By.XPATH, './/td[@class="account"]//a[@class="alias"]')
    ACCOUNT_TOGGLE = (By.XPATH, './/button[@class="btn btn-mini dropdown-toggle"]')
    CLOSE_ACCOUNT = (By.XPATH, './/a[@class="close-account-link"]')
    FORWARD_BUTTON = (By.XPATH, '//button[@id="#forward"]')
    CLOSE_MODAL_WINDOW = (
        By.XPATH,
        '//div[@id="default-dialog"]/div[@class="modal-header"]/button[@class="close"]',
    )
    DATE_FROM_INPUT_FIELD = (By.XPATH, '//div[@id="from-date"]/input')
    DATE_UNTIL_INPUT_FIELD = (By.XPATH, '//div[@id="until-date"]/input')
    GET_BUTTON = (By.XPATH, '//button[@id="query-button"]')
    DATE_ON_PAGE = (By.XPATH, '//div[@class="statement-header clearfix"]//div[2]')
    ON_EMAIL_BUTTON = (
        By.XPATH,
        '//div[@id="statement-email-send"]//button[@class="btn dropdown-toggle"]',
    )
    PDF_BUTTON = (By.XPATH, '//a[@id="btn-email-pdf"]')
    EXCEL_BUTTON = (By.XPATH, '//a[@id="btn-email-xls"]')
    EMAIL_FIELD = (By.XPATH, '//div[@class="controls"]/input[@type="email"]')
    SEND_BUTTON = (By.XPATH, '//button[@id="send-to-email"]')
    EMAIL_SUCCESS_MESSAGE = (By.XPATH, '//div[@id="email-success-message"]')
