#no of input in paarams  =no. of tc input

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--bname", action="store", default="chrome"
    )


@pytest.fixture(scope='class') #to not to use this line in every file we created a baseclass
def setup(request):
    global driver #this will take the above driver i.e none it set it to global level so the below or next fx can recongnise it
    bname = request.config.getoption('bname')
    if bname == 'chrome':
        driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
    elif bname == 'firefox':
        driver = webdriver.Firefox(executable_path='C:\\geckodriver.exe')
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)



