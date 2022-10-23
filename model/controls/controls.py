"""
Controls on the pages
"""
from selene.core.entity import Element
from selene.support.shared import browser
from selenium.webdriver.common.by import By


class Input(object):
    """
    Page object input
    """

    def __init__(self, element: Element):
        self.element = element

    def type(self, value: str):
        self.element.type(value)
