"""
Session util
"""
import json
import allure
import curlify
import requests
from requests import Session


def allure_request_logger(function):
    """
    Allure logger
    """

    def wrapper(*args, **kwargs):
        """
        Wrapper
        """

        response = function(*args, **kwargs)
        message = curlify.to_curl(response.request)
        allure.attach(
            body=message.encode('utf8'),
            name='Request',
            attachment_type=allure.attachment_type.TEXT,
            extension='txt'
        )
        try:
            allure.attach(
                body=str(json.dumps(response.json(),
                                    skipkeys=True,
                                    allow_nan=True,
                                    indent=4)).encode('utf-8'),
                name='Response',
                attachment_type=allure.attachment_type.TEXT,
                extension='txt'
            )
        except requests.exceptions.JSONDecodeError:
            allure.attach(
                body=response.text,
                name='Response',
                attachment_type=allure.attachment_type.TEXT,
                extension='txt'
            )
        return response

    return wrapper


class BaseSession(Session):
    """
    Base session class
    """

    def __init__(self, **kwargs):
        super().__init__()

    @allure_request_logger
    @allure.step('{method} {url}')
    def request(self, method, url, **kwargs):
        response = super().request(method, url, **kwargs)
        return response


def base_session() -> BaseSession:
    """
    Create base session
    """
    session = BaseSession()
    session.verify = False
    return session
