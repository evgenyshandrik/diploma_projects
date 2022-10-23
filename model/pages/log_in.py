"""
Page object: log in
"""
import allure

from selene import command
from selene.support.shared.jquery_style import s
from model.controls.controls import Input


class LogIn(object):
    """
    Log in page
    """

    @allure.step('Set username: {name}')
    def set_user_name(self, name: str):
        username_input = Input(s('#username'))
        username_input.type(name)
        return self

    @allure.step('Set user password: {password}')
    def set_user_password(self, password: str):
        password_input = Input(s('#password'))
        password_input.type(password)
        return self

    @allure.step('Submit form')
    def submit_form(self):
        s('#login').perform(command.js.click)
        return self
