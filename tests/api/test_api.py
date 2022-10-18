"""
Api tests
"""
import allure
import pytest


@pytest.mark.api
@allure.description('Test sign up form')
@allure.tag('API')
def test_api_one():
    """
    api
    """
    print('test 1 api')


@pytest.mark.api
def test_api_two():
    """
    api
    """
    print('test 2 api')
