"""
Page object: sign up
"""
import allure

from selene import command
from selene.support.shared.jquery_style import s

from model.controls.controls import Input


class SignUp(object):
    """
    Sign up page
    """

    @allure.step('Set username: {name}')
    def set_user_name(self, name: str):
        username_input = Input(s('#registration_username'))
        username_input.type(name)
        return self

    @allure.step('Set user email: {email}')
    def set_user_email(self, email: str):
        emai_input = Input(s('#registration_email'))
        emai_input.type(email)
        return self

    @allure.step('Set user password: {password}')
    def set_user_password(self, password: str):
        password_input = Input(s('#registration_password'))
        password_input.type(password)
        return self

    @allure.step('Submit form')
    def submit_form(self):
        s('#registration_submit').perform(command.js.click)
        return self

    @allure.step('Get password input')
    def get_password_input(self):
        return s('#registration_password')

    @allure.step('Click login button')
    def click_log_in_button(self):
        s('.security-v5-link').click()
        return self
