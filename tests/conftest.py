import pytest
from dotenv import load_dotenv

DEFAULT_REMOTE_DRIVER = 'selenoid.autotests.cloud'


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
        '--remote_driver',
        default='selenoid.autotests.cloud'
    )


@pytest.fixture(scope='function', autouse=True)
def config(request):
    """
    Config test
    """
    remote_driver = request.config.getoption('--remote_driver')
    remote_driver = remote_driver if remote_driver != "" else DEFAULT_REMOTE_DRIVER
    print("Config")
