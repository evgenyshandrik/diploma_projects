import allure
import time
from selene.support.shared import browser
from allure_commons.types import AttachmentType


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
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video(name: str):
    """
    Add video
    """
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, name, AttachmentType.HTML, '.html')
