from selenium.webdriver.common.by import By


class DepositPageLocators:
    OPEN_DEPOSIT_BUTTON = (By.XPATH, '//a[@class="btn btn-primary"]')

    RUB_CURRENCY = (By.XPATH, '//input[@name="currency" and @value="RUB"]/..')
    EUR_CURRENCY = (By.XPATH, '//input[@name="currency" and @value="EUR"]/..')
    USD_CURRENCY = (By.XPATH, '//input[@name="currency" and @value="USD"]/..')
    MIN_DAYS_TWO_WEEKS = (By.XPATH, '//input[@name="minDays" and @value="15"]/..')
    MIN_DAYS_ONE_MONTH = (By.XPATH, '//input[@name="minDays" and @value="31"]/..')
    MIN_DAYS_THREE_MONTHS = (By.XPATH, '//input[@name="minDays" and @value="91"]/..')
    MIN_DAYS_SIX_MONTHS = (By.XPATH, '//input[@name="minDays" and @value="181"]/..')
    MIN_DAYS_ONE_YEAR = (By.XPATH, '//input[@name="minDays" and @value="367"]/..')
    MIN_DAYS_TWO_YEARS = (By.XPATH, '//input[@name="minDays" and @value="733"]/..')
    MIN_DAYS_FREE_TERM = (By.XPATH, '//input[@name="minDays" and @value="-1"]/..')

    OPEN_DEPOSIT_BUTTONS = (
        By.XPATH,
        '//table[@class="table table-striped '
        'sortable"]//tbody//td[@class="right"]/a['
        '@class="btn btn-mini btn-primary '
        'place-deposit"]',
    )
    DATE_FIELD = (By.XPATH, '//input[@id="endDate"]')
    SUMM_FIELD = (By.XPATH, '//input[@id="amount"]')
    PROLONGATION_CHECKBOX = (By.XPATH, '//input[@type="checkbox"]')
    TERMS_AGREEMENT_CHECKBOX = (
        By.XPATH,
        '//input[@type="checkbox" and ' '@class="immune required condition"]',
    )
    SUBMIT_BUTTON = (By.XPATH, '//button[@id="submit-button"]')
    CONFIRM_BUTTON = (By.XPATH, '//button[@id="confirm"]')
    INTEREST_RATE_VALUE = (By.XPATH, '//span[@id="interest-rate"]')
    INVALID_COMBINATION_SUM_AND_DATE = (
        By.XPATH,
        '//div[@class="tooltip fade right in"]',
    )
    ERROR_MESSAGE = (By.XPATH, '//span[@class="error-message"]')
    RENAME_ACCOUNT_BUTTONS = (By.XPATH, '//i[@class="table-action-link icon-edit"]')
    ACCOUNT_NAME = (By.XPATH, '//tbody/tr/td/a[@class="alias"]')
    INPUT_FIELD = (By.XPATH, '//form[@class="account-alias-edit-form alias-edit-form internal form-inline"]//input[@type="text"]')
    FIRST_ACCOUNT = (By.XPATH, '//table/tbody/tr[1]/td[1]')