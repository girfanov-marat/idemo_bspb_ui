from selenium.webdriver.common.by import By


def test_main_page(app):
    assert (
        app.d.find_element(By.XPATH, '//div[@id="user-greeting"]').text
        == "Hello World!"
    )
