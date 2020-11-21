# conftest.py
#
"""
conftest file call at the beginning and end of every test case.
"""
import os

from common import configuration as conf
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    """
    To enable the environment variable in pytest
    python -m pytest -vs --junitxml=reporting/report.xml --html=reporting/report.html --browser="Chrome"
    Parameters:
        parser: from commandline execution --browser=<browser_name>
    Returns:
        None
    Raises:
        None
    """
    parser.addoption('--browser', help='Use to specify test automation browser environment like: chrome/firefox')

@pytest.yield_fixture(scope="class")
def web_driver(request):
    """
    Create web driver object to perform various action on web elements
    Parameters:
        request: fixture request
    Returns:
        web driver object
    Raises:
        None
    """
    selected = request.config.getoption('browser')
    print("Selected Browser: ", selected)
    # get the path of WebDriverServer
    dir_path = os.path.dirname(__file__)
    driver_path = dir_path + r"\selenium"
    chrome_driver_path = driver_path + r"\Chromedriver.exe"

    if selected is None:
        print("None of the browser is selected so setting default browser as chrome")
        web_driver = webdriver.Chrome(executable_path=chrome_driver_path)
    else:
        # setting run time web driver environment
        if "chrome" in selected.lower():
            web_driver = webdriver.Chrome(executable_path=chrome_driver_path)
        elif "firefox" in selected.lower():
            firefox_driver_path = driver_path + r"\Firefoxdriver.exe"
            web_driver = webdriver.Firefox(executable_path=firefox_driver_path)
        else:
            print("Please enter valid browser like: chrome/firefox")
            return False
    web_driver.get(conf.GOOGLE_URL)
    web_driver.maximize_window()
    request.cls.driver = web_driver
    yield web_driver
    web_driver.close()