"""
Page object: main
"""
import allure

from selene.support.shared.jquery_style import s
from selenium.webdriver.common.by import By
from selene.support.shared import browser


class Main(object):
    """
    Main page
    """

    @allure.step('Click login button')
    def click_login_button(self):
        s('.button auth login ui_v5-button-component ui_v5-button-primary').click()
        return self

    @allure.step('Click signup button')
    def click_signup_button(self):
        s('#menu-cta').click()
        return self

    @allure.step('Click cross in modal view')
    def click_cross_in_modal_view(self):
        s('.ui_outside-close-component').click()
        return self

    @allure.step('Get username label')
    def get_username_label(self):
        return browser.config.driver.find_element(By.CSS_SELECTOR, 'home-username-link')
