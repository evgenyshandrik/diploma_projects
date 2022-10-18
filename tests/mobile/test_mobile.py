import pytest


@pytest.mark.mobile
def test_mobile_one():
    print('test 1 mobile')


@pytest.mark.mobile
def test_mobile_two():
    print('test 2 mobile')