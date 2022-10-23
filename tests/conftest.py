"""
Tests configuration
"""
import os
import time
import allure
import pytest
import requests
from dotenv import load_dotenv
from datetime import date

from selene.support.shared import browser
from appium import webdriver
from selenium.webdriver.common.by import By

from util.resources import path

DEFAULT_WEB_REMOTE_DRIVER = 'selenoid.autotests.cloud'
DEFAULT_WEB_BROWSER_VERSION = '100'
DEFAULT_MOBILE_APP = 'chess.apk'


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
        help='web: remote driver'
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
        '--mobile_app',
        default='chess.apk',
        help='mobile app: path to app'
    )

    parser.addoption(
        '--mobile_device',
        default='Google Pixel 4',
        help='mobile device'
    )

    parser.addoption(
        '--mobile_device_version',
        default='9.0',
        help='mobile device version'
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
        mobile_app = request.config.getoption('--mobile_app')
        mobile_app = mobile_app if mobile_app != "" else DEFAULT_MOBILE_APP

        mobile_device = request.config.getoption('--mobile_device').replace('_', ' ')

        mobile_device_version = request.config.getoption('--mobile_device_version')

        USER = os.getenv('USER_BROWSERSTACK')
        KEY = os.getenv('KEY_BROWSERSTACK')
        APPIUM_BROWSERSTACK = os.getenv('APPIUM_BROWSERSTACK')
        API_BROWSERSTACK_UPLOAD_FILE = os.getenv('API_BROWSERSTACK_UPLOAD_FILE')

        file_for_upload = [('file', (mobile_app, open(path(mobile_app), 'rb')))]
        response = requests.post(f"https://{USER}:{KEY}@{API_BROWSERSTACK_UPLOAD_FILE}", files=file_for_upload)
        app = response.json()['app_url']

        desired_cap = {
            "app": app,
            "deviceName": mobile_device,
            "os_version": mobile_device_version,
            "platformName": "Android",
            "project": f'Test mobile app: {mobile_app}',
            "build": f'{mobile_device}, {mobile_device_version}'
        }

        print(desired_cap)

        browser.config.driver = webdriver.Remote(
            command_executor=f"http://{USER}:{KEY}@{APPIUM_BROWSERSTACK}/wd/hub",
            desired_capabilities=desired_cap
        )


@allure.step('Open page: {url}')
def open_page(url: str):
    """
    Open(redirect) pages contains testing form
    """
    browser.open(url)
    time.sleep(1)
