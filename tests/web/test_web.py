"""
Tests web version chess.com
"""
import allure
import pytest
from allure_commons.types import AttachmentType
from faker import Faker

from selene.support.shared import browser
from model import application_manager
from tests.conftest import open_page
from util.attachment import take_screenshot, add_video

URL_MAIN = 'https://www.chess.com'
URL_SIGN_UP = 'https://www.chess.com/register?returnUrl=https://www.chess.com/'
URL_LOG_IN = 'https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/'


@pytest.mark.web
@allure.description('Test open sign up page')
def test_open_sign_up_page():
    """
    Test open sign up page
    """
    open_page(URL_MAIN)

    application_manager.main_page. \
        click_signup_button()

    take_screenshot(name='Screenshot', type_file=AttachmentType.PNG)
    add_video('Video steps of test')

    assert browser.driver.current_url == URL_SIGN_UP, f'After redirect to sign page url should be {URL_SIGN_UP}'


@pytest.mark.web
@allure.description('Test open log in page')
def test_open_log_in_page():
    """
    Test open log in page
    """
    open_page(URL_MAIN)

    application_manager.main_page. \
        click_login_button()

    take_screenshot(name='Screenshot', type_file=AttachmentType.PNG)
    add_video('Video steps of test')

    assert browser.driver.current_url == URL_LOG_IN, f'After redirect to page login page url should be {URL_LOG_IN}'


@pytest.mark.web
@allure.description('Test show password')
def test_show_password():
    """
    Test show password
    """
    open_page(URL_MAIN)

    application_manager.main_page. \
        click_signup_button()

    password = Faker().password()

    application_manager.sign_up_page \
        .set_user_password(password) \
        .show_password()

    password_from_input = application_manager.sign_up_page \
        .get_password_input() \
        .get_attribute('value')

    take_screenshot(name='Screenshot', type_file=AttachmentType.PNG)
    add_video('Video steps of test')

    assert password == password_from_input, f'Password should be equals {password}'


@pytest.mark.web
@allure.description('Test redirect to log in page from sign up')
def test_redirect_to_log_in_page_from_sign_up():
    """
    Test redirect to log in form
    """
    open_page(URL_MAIN)

    application_manager.main_page. \
        click_signup_button()

    application_manager.sign_up_page \
        .click_log_in_button()

    take_screenshot(name='Screenshot', type_file=AttachmentType.PNG)
    add_video('Video steps of test')

    assert browser.driver.current_url == URL_LOG_IN, f'After redirect to log in page url should be {URL_LOG_IN}'


@pytest.mark.web
@allure.description('Test redirect to sign up page from log in')
def test_redirect_to_sign_up_page_from_log_in():
    # TODO(users) will be fail after too many retries - captcha will turn on
    """
    Test redirect to sign up page from log in
    """
    open_page(URL_MAIN)

    application_manager.main_page. \
        click_signup_button()

    faker = Faker()
    username = (faker.name() + faker.last_name()).replace(' ', '_')

    application_manager.sign_up_page \
        .set_user_name(username) \
        .set_user_email(faker.email()) \
        .set_user_password(faker.password()) \
        .submit_form()

    username_after_sign_up = application_manager.main_page \
        .get_username_label() \
        .get_attribute('value')

    take_screenshot(name='Screenshot', type_file=AttachmentType.PNG)
    add_video('Video steps of test')

    assert username == username_after_sign_up, f'Username after login should be equals before login: {username}'
