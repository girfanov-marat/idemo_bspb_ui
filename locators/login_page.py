from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME_FIELD = (By.XPATH, '//input[@name="username"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@id="login-button"]')
    LOGIN_OTP_CODE_BUTTON = (By.XPATH, '//button[@id="login-otp-button"]')
