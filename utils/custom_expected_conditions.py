from selenium.common.exceptions import (
    StaleElementReferenceException,
    WebDriverException,
)


def _find_element(driver, by):
    try:
        return driver.find_element(*by)
    except WebDriverException as e:
        raise e


class text_is_not_empty(object):
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            return _find_element(driver, self.locator).text != ""
        except StaleElementReferenceException:
            return False
