"""
Page object: main
"""
import allure

from selene.support.shared.jquery_style import s


class Main(object):
    """
    Main page
    """

    @allure.step('Click login button')
    def click_login_button(self):
        s('//*[@id="sb"]/div[3]/a[9]').click()
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
        return s('//*[@id="tb"]/div[2]/div/a[2]')
