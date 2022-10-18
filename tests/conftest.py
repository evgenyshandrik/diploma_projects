import pytest
from dotenv import load_dotenv

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
        '--web_browser_size',
        default='1440x800',
        help='web: browser size (1440x800, 1920x1080, 1280x720)'
    )

    parser.addoption(
        '--web_browser_version',
        default='100',
        help='web: browser version (100, 90 and etc.)'
    )


@pytest.fixture(scope='function', autouse=True)
def config(request):
    """
    Config test
    """
    web_remote_driver = request.config.getoption('--web_remote_driver')
    web_remote_driver = web_remote_driver if web_remote_driver != "" else DEFAULT_WEB_REMOTE_DRIVER
    print(web_remote_driver)
    print(request.config.getoption('--web_browser'))
    print("Config")
