import pytest


@pytest.fixture(scope='function', autouse=True)
def config():
    """
    Config test
    """
    print("Config")