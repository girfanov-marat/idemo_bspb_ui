import os
from datetime import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.application import Application


@pytest.fixture(scope="session")
def driver(request):
    driver_path = ChromeDriverManager().install()
    options: Options = Options()
    options.headless = request.config.getoption("--headless")
    driver = webdriver.Chrome(driver_path, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def app(request, driver):
    base_url = request.config.getoption("--base-url")
    fixture = Application(driver, base_url)
    fixture.d.implicitly_wait(10)
    fixture.open_page(base_url)
    fixture.login.auth()
    fixture.wait.until(fixture.ex.url_to_be(fixture.main_url))
    return fixture


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://idemo.bspb.ru/",
        help="enter base_url",
    ),
    parser.addoption(
        "--username", action="store", default="demo", help="enter username",
    ),
    parser.addoption(
        "--password", action="store", default="demo", help="enter password",
    ),
    parser.addoption(
        "--headless",
        action="store",
        default=True,
        help="launching browser without gui",
    ),


PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), "..", p))


@pytest.mark.hookwrapper(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        if "app" in item.fixturenames:
            driver = item.funcargs["app"]
        xfail = hasattr(report, "wasxfail")
        # create file
        add_name = "{}_{}".format(
            report.nodeid.split("::")[1], datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
        )
        file_name = PATH(os.path.abspath(os.curdir) + "/" + add_name + ".png")
        driver.d.get_screenshot_as_file(file_name)
        if (report.skipped and xfail) or (report.failed and not xfail):
            cp_file_name = add_name + ".png"
            # only add additional html on failure
            html = (
                "<div><img src="
                + cp_file_name
                + ' alt="screenshot" style="width:304px;height:228px;" '
            )
            extra.append(pytest_html.extras.html(html))
        report.extra = extra


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        try:
            with open("failures", mode) as f:
                if "app" in item.fixturenames:
                    web_driver = item.funcargs["app"]
                else:
                    print("Fail to take screen-shot")
                    return
            allure.attach(
                web_driver.d.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            print("Fail to take screen-shot: {}".format(e))
