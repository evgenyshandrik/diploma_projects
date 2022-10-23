"""
Attachment util
"""
import allure
import time
import requests
import os
from selene.support.shared import browser
from allure_commons.types import AttachmentType

FILE_EXTENSION_HTML = '.html'


def take_screenshot(name: str, type_file: AttachmentType):
    """
    Take screenshot
    """
    # for loading page
    time.sleep(0.5)
    allure.attach(browser.driver.get_screenshot_as_png(), name=name, attachment_type=type_file, extension='.png')


def add_logs(browser):
    """
    Add browser logs
    """
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    """
    Add html
    """
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, FILE_EXTENSION_HTML)


def add_video_to_report():
    """
    Add video
    """
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'Steps of test', AttachmentType.HTML, FILE_EXTENSION_HTML)


def get_url_video(session_id: str):
    """
    Get url video from browserstack
    """
    api_browserstack = os.getenv('API_BROWSERSTACK')
    session = requests.Session()
    session.auth = (os.getenv('LOGIN'), os.getenv('KEY'))
    response = session.get(
        f'{api_browserstack}/sessions/{session_id}.json')
    return response.json().get('automation_session').get('video_url')


def add_video_from_browserstack_to_report(session_id: str):
    """
    Add video
    """
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + get_url_video(session_id) \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'Steps of test', AttachmentType.HTML, FILE_EXTENSION_HTML)
