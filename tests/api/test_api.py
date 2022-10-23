"""
Api tests chess.com
"""
import json
import os

import allure
import jsonschema
import pytest

from tests.api.base_session import base_session

URL_CHESS_COM = 'https://www.chess.com'
STATUS_CODE_OK = 'Status code should be OK'


@pytest.mark.api
@allure.description('Test get playlist video')
def test_get_playlist_video():
    """
    Test get playlist video
    """
    response = base_session().get('https://api.chess.com/int/navbar/panels/watch')
    assert response.status_code == 200, STATUS_CODE_OK
    assert len(response.json()['streamers']) > 0, 'Streamers should be more 0'


@pytest.mark.api
@allure.description('Test get events')
def test_get_events():
    """
    Test get events
    """
    response = base_session().post('https://nxt.chessbomb.com/events/api/games/active')
    assert response.status_code == 200, STATUS_CODE_OK
    assert len(response.json()['games']) > 0, 'Games should be more 0'


@pytest.mark.api
@allure.description('Test get news')
def test_get_news():
    """
    Test get news
    """
    response = base_session().get(f'{URL_CHESS_COM}/news')
    assert response.status_code == 200, STATUS_CODE_OK


@pytest.mark.api
@allure.description('Test get board settings')
def test_get_board_settings():
    """
    Test get board settings
    """
    response = base_session().get(f'{URL_CHESS_COM}/callback/board-settings')
    assert response.status_code == 200, STATUS_CODE_OK
    scheme_validation(response, 'board_settings')


@pytest.mark.api
@allure.description('Test get themes')
def test_get_themes():
    """
    Test get themes
    """
    response = base_session().get(f'{URL_CHESS_COM}/callback/themes/data')
    assert response.status_code == 200, STATUS_CODE_OK
    scheme_validation(response, 'themes_settings')


@pytest.mark.api
@allure.description('Test get member statistics')
def test_get_member_statistics():
    """
    Test get member statistics
    """
    username = os.getenv('USERNAME_CHESS_COM')
    response = base_session().get(f'{URL_CHESS_COM}/callback/member/stats/{username}')
    assert response.status_code == 200, STATUS_CODE_OK
    assert len(response.json()['stats']) > 0, 'Statistics should be more 0'


@pytest.mark.api
@allure.description('Test get leagues information not authorized user')
def test_get_leagues_information_not_auth_user():
    """
    Test get leagues information not authorized user
    """
    response = base_session().get(f'{URL_CHESS_COM}/callback/leagues/division-start-check')
    assert response.status_code == 401, 'Status code should be Not Authorized'


@allure.step('Json schemes validation')
def scheme_validation(response, controller_name):
    """
    Json schemes validation
    """
    with open(f'../../resources/schemes/{controller_name}.json', encoding='utf-8') as scheme:
        try:
            jsonschema.validate(response.json(), json.loads(scheme.read()))
        except jsonschema.ValidationError:
            assert False, f'Scheme_name:\n{controller_name}\nResponse.url:\n{response.url}\n' \
                          f'Response.json():\n{response.json()}'
