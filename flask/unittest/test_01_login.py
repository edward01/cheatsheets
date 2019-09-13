import pytest
from flask import session
from tests.conftest import ADMIN_USER
from gridloc.settings import CLOUD_MODE


def test_login_logout(client, auth):
    """
    GIVEN a Flask application
    WHEN the '/login/' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/login/', follow_redirects=True)
    assert response.status_code == 200
    assert b"Admin Login" in response.data  # from login card label
    assert b"Username" in response.data
    assert b"Password" in response.data

    """
    GIVEN a Flask application
    WHEN the '/login/' page is posted to (POST)
    THEN check the session['user'] is valid
    """
    auth.login()
    with client:
        response = client.get('/user_account/', follow_redirects=True)
        assert session['user']['username'] == ADMIN_USER

    """
    GIVEN a Flask application
    WHEN the '/login/exit' page is requested (GET)
    THEN will redirect back the user to the login screen
    """
    auth.logout()
    with client:
        assert 'user' not in session
    response = client.get('/login/', follow_redirects=True)
    assert response.status_code == 200
    assert b"Admin Login" in response.data  # from login card label
    assert b"Username" in response.data
    assert b"Password" in response.data


@pytest.mark.parametrize(('username', 'password', 'message'), (
    (ADMIN_USER, 'test', b'Incorrect username and/or password'),
    ('test', ADMIN_USER, b'Incorrect username and/or password'),
))
def test_login_validate_input(client, auth, username, password, message):
    """
    GIVEN a Flask application
    WHEN the '/login/' page is requested (GET) with invalid credentials
    THEN will return an error message
    """
    auth.login(username, password)
    with client:
        response = client.get('/', follow_redirects=True)
        assert message in response.data


@pytest.mark.parametrize('path', (
    '/networks/',
    '/domains/',
    '/users/',
    '/assets/',
    '/helpdesk/',
))
def test_login_required(client, path):
    """
    GIVEN a Flask application
    WHEN each of the "protected" page is requested (GET) without logging in
    THEN will redirect the user back to the login screen
    """
    response = client.get(path, follow_redirects=True)
    assert response.status_code == 200
    assert b"Admin Login" in response.data  # from login card label
    assert b"Username" in response.data
    assert b"Password" in response.data


def test_login_cloud_mode(client, auth):
    """
    GIVEN a Flask application
    WHEN config is not "CLOUD_MODE"
    THEN the left side protected menus should have "access_points" item
    """
    auth.login()
    with client:
        response = client.get('/networks/', follow_redirects=True)
        if not CLOUD_MODE:
            assert b'data-toggle="popover" data-content="Access Points">' in response.data
        else:
            assert b'data-toggle="popover" data-content="Access Points">' not in response.data
