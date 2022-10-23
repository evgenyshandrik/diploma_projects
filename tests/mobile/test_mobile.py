"""
Tests mobile application chess.com
"""

import pytest
from selene.support.shared import browser


@pytest.mark.mobile
def test_mobile_one():
    print(browser.driver.page_source)
    print('test 1 mobile')


@pytest.mark.mobile
def test_mobile_two():
    print('test 2 mobile')
