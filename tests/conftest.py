"""
Tests configuration
"""
import os
import time
from datetime import date

import allure
import pytest
from dotenv import load_dotenv

from selene.support.shared import browser
from selenium import webdriver

DEFAULT_WEB_REMOTE_DRIVER = 'selenoid.autotests.cloud'
DEFAULT_WEB_BROWSER_VERSION = '100'


@pytest.fixture(scope='session', autouse=True)
def load_env():
    """
    Load .env
    """
    load_dotenv()


def pytest_addoption(parser):
    """
    Parser option
    """
    parser.addoption(
        '--web_remote_driver',
        default='selenoid.autotests.cloud',
        help='web: remote driver (local or selenoid)'
    )

    parser.addoption(
        '--web_browser',
        default='chrome',
        help='web: browser (chrome or firefox)'
    )

    parser.addoption(
        '--web_browser_version',
        default='100',
        help='web: browser version (100, 90 and etc.)'
    )

    parser.addoption(
        '--type',
        default='web',
        help='type of tests: web, api, mobile'
    )


@pytest.fixture(scope='function', autouse=True)
@allure.step('Prepare actions before tests')
def config(request):
    """
    Config test
    """
    type_of_test = request.config.getoption('--type')

    if type_of_test == 'web':
        web_remote_driver = request.config.getoption('--web_remote_driver')
        web_remote_driver = web_remote_driver if web_remote_driver != "" else DEFAULT_WEB_REMOTE_DRIVER

        web_browser = request.config.getoption('--web_browser')

        web_browser_version = request.config.getoption('--web_browser_version')
        web_browser_version = web_browser_version if web_browser_version != "" else DEFAULT_WEB_BROWSER_VERSION

        login = os.getenv('LOGIN_SELENOID')
        password = os.getenv('PASSWORD_SELENOID')

        capabilities = {
            "browserName": web_browser,
            "browserVersion": web_browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }

        browser.config.driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@{web_remote_driver}/wd/hub",
            desired_capabilities=capabilities)

        browser.config.browser_name = os.getenv('selene.browser_name', web_browser)
        browser.config.driver.maximize_window()
        browser.config.hold_browser_open = (
                os.getenv('selene.hold_browser_open', 'false').lower() == 'true'
        )
        browser.config.timeout = float(os.getenv('selene.timeout', '3'))

    elif type_of_test == 'mobile':
        create_mobile_driver()
    else:
        pass


def create_mobile_driver() -> webdriver:
    """
    Create mobile driver
    """
    USER = os.getenv('USER_BROWSERSTACK')
    KEY = os.getenv('KEY_BROWSERSTACK')
    APPIUM_BROWSERSTACK = os.getenv('APPIUM_BROWSERSTACK')

    desired_cap = {
        "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
        "deviceName": "Google Pixel 3",
        "os_version": "9.0",
        "platformName": "android",
        "project": "Python project",
        "build": "browserstack-build-" + str(date.today()),
        "name": func.__name__.capitalize().replace('_', ' ')
    }

    return webdriver.Remote(
        command_executor=f"http://{USER}:{KEY}@{APPIUM_BROWSERSTACK}/wd/hub",
        desired_capabilities=desired_cap
    )


@allure.step('Open page: {path}')
def open_page(path: str):
    """
    Open(redirect) pages contains testing form
    """
    browser.open(path)
    time.sleep(1)
