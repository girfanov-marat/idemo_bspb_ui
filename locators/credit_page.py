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
    ALERT_SUCCESS_INFO = (By.XPATH, '//div[@class="alert alert-success"]')
    ALERT_INFO = (By.XPATH, '//div[@class="alert alert-info"]')
    MODAL_WINDOW = (By.XPATH, '//div[@class="modal hidden in"]')

    CONTRACTS = (By.XPATH, '//table[@id="loans"]//tbody//tr')
    CONTRACT_TOGGLE = (
        By.XPATH,
        '//table[@id="loans"]//tbody//td//'
        'button[@class="btn btn-mini dropdown-toggle"]',
    )

    DOCUMENT_ACTIONS = (
        By.XPATH,
        '//table[@id="loans"]//div['
        '@class="cogwheel-actions btn-group '
        'pull-right print-hidden open"]//ul['
        '@class="dropdown-menu"]/li',
    )

    OFFICE_LIST = (By.XPATH, '//select[@name="message.branch"]//option')
    SEND_BUTTON = (By.XPATH, '//button[@id="send-button"]')
    CONTINIUE_BUTTON = (
        By.XPATH,
        '//div[@class="form-actions"]//a[@class="btn btn-primary"]',
    )
    CONTINIUE_LOAN_CLAIM_BUTTON = (
        By.XPATH,
        '//div[@class="form-actions"]//button[@class="btn ' 'btn-primary"]',
    )
    SUBMITTED_APPLICATIONS = (
        By.XPATH,
        '//table[@id="pre-approved-applications"]//tbody//tr',
    )
    SUB_APPLICATIONS_RECEIVE_BUTTONS = (
        By.XPATH,
        '//table[@id="pre-approved-applications"]'
        '//tbody//a[@class="btn btn-primary"]',
    )
    ACCOUNTS = (By.XPATH, '//div[@class="controls"]//select[@name="serviceAccountId"]')
    REPAYMENT_DAY = (By.XPATH, '//div[@class="controls"]//select[@name="repaymentDay"]')
    OFFICE_FIELD = (
        By.XPATH,
        '//div[@class="controls"]//select[@name="message.branch"]',
    )
    CONTRACT_SIGNING_CHECKBOXES = (By.XPATH, '//input[@type="checkbox"]')
    PERSONAL_TERMS_MODAL_WINDOW = (By.XPATH, '//div[@id="personal-terms-dialog"]')
    PERSONAL_TERMS_AGREEMENT_BUTTON = (
        By.XPATH,
        '//a[@id="accept-personal-terms-button"]',
    )
    PERSONAL_TERMS = (By.XPATH, '//table[@class="table"]//tr')
    CONTRACT_NUM = (By.XPATH, '//span[@class="uneditable-input input-borderless "]')
    CONFIRM_BUTTON = (By.XPATH, '//button[@id="confirm"]')
