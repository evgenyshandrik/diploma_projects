"""
Tests mobile application chess.com
"""
import os

import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
from selene import have, be

from util.attachment import add_video_from_browserstack_to_report

SETTING_BUTTON_LOCATOR = "com.chess:id/menu_item_settings_icon"


@pytest.mark.mobile
@allure.description('Test elements on main screen (unauthorized user)')
def test_elements_on_main_screen_unauthorized_user():
    """
    Test elements on main screen (unauthorized user)
    """
    browser.element((AppiumBy.ID, "com.chess:id/log_in")).should(be.visible)
    browser.element((AppiumBy.ID, "com.chess:id/logo")).should(be.visible)
    browser.element((AppiumBy.ID, SETTING_BUTTON_LOCATOR)).should(be.visible)
    browser.element((AppiumBy.ID, "com.chess:id/newGameBtn")).should(be.visible)

    add_video_from_browserstack_to_report(browser.driver.session_id)

    browser.config.driver.quit()


@pytest.mark.mobile
@allure.description('Test successful log in')
def test_successful_log_in():
    """
    Test successful log in
    """
    username = os.getenv('USERNAME_CHESS_COM')
    password = os.getenv('PASSWORD_CHESS_COM')

    browser.element((AppiumBy.ID, "com.chess:id/log_in")).click()
    browser.element((AppiumBy.ID, "com.chess:id/usernameEdit")).type(username)
    browser.element((AppiumBy.ID, "com.chess:id/passwordEdit")).type(password)
    browser.element((AppiumBy.ID, "com.chess:id/loginBtn")).click()
    browser.element((AppiumBy.ID, "com.chess:id/menu_item_avatar")).should(be.visible)

    # add_video_from_browserstack_to_report(browser.driver.session_id)

    browser.config.driver.quit()


@pytest.mark.mobile
@allure.description('Test elements on settings screen')
def test_elements_on_settings_screen():
    """
    Test elements on settings screen
    """
    browser.element((AppiumBy.ID, SETTING_BUTTON_LOCATOR)).click()
    assert len(browser.elements((AppiumBy.ID, "com.chess:id/settingsMenuItem"))) == 7

    # add_video_from_browserstack_to_report(browser.driver.session_id)

    browser.config.driver.quit()


@pytest.mark.mobile
@allure.description('Test version application')
def test_version_application():
    """
    Test version application
    """
    browser.element((AppiumBy.ID, SETTING_BUTTON_LOCATOR)).click()
    browser.element((AppiumBy.ID, "com.chess:id/settingsMenuFooterTxt")).should(have.text('v4.5.3-googleplay-261758'))

    # add_video_from_browserstack_to_report(browser.driver.session_id)

    browser.config.driver.quit()


@pytest.mark.mobile
@allure.description('Test elements on sign up screen')
def test_elements_on_sign_up_screen():
    """
    Test elements on sign up screen
    """
    browser.element((AppiumBy.ID, SETTING_BUTTON_LOCATOR)).click()
    browser.elements((AppiumBy.ID, "com.chess:id/settingsMenuItem"))[0].click()
    browser.element((AppiumBy.ID, "com.chess:id/title")).should(be.clickable)
    browser.element((AppiumBy.ID, "com.chess:id/title")).should(have.text('What is your chess skill level?'))
    browser.element((AppiumBy.ID, "com.chess:id/skillLevelNew")).should(be.visible)
    browser.element((AppiumBy.ID, "com.chess:id/skillLevelBeginner")).should(be.visible)
    browser.element((AppiumBy.ID, "com.chess:id/skillLevelIntermediate")).should(be.visible)
    browser.element((AppiumBy.ID, "com.chess:id/skillLevelAdvanced")).should(be.visible)
    browser.element((AppiumBy.ID, "com.chess:id/continueButton")).should(be.visible)
    browser.element((AppiumBy.ID, "com.chess:id/continueButton")).click()
    browser.element((AppiumBy.ID, "com.chess:id/signup_image")).should(be.visible)
    browser.element((AppiumBy.ID, "com.chess:id/usernameEdit")).should(be.visible)
    browser.element((AppiumBy.ID, "com.chess:id/createUsernameBtn")).should(be.visible)

    # add_video_from_browserstack_to_report(browser.driver.session_id)

    browser.config.driver.quit()
