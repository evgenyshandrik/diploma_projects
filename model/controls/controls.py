"""
Controls on the pages
"""
from selene.core.entity import Element


class Input(object):
    """
    Page object input
    """

    def __init__(self, element: Element):
        self.element = element

    def type(self, value: str):
        self.element.type(value)


class PasswordInput(Input):
    """
    Page object password input
    """

    def show_password(self):
        self.element.element('/html/body/div[1]/div/main/div/div/div[1]/form/div[3]/div/div/span[2]').click()
