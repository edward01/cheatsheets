# https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/
# To run:               $ pytest -v tests/
#   without warnings:   $ pytest -v --disable-warnings tests/
#   with full logs:     $ pytest -v -s tests/
#
# $ pytest --setup-show tests/unit/
# $ pytest --setup-show tests/functional/test_users.py::test_home_page
# $ pytest --setup-show tests/functional/
# -------------------
# $ pytest -v tests/
# -------------------

ADMIN_USER = 'admin_test'

import pytest

from gridloc.helpers import validate_form, make_hash
from gridloc.vortex.models.admin import Admin

from vortex import admin


@pytest.fixture
def app():
    settings_override = {
        'DEBUG': True,
        'TESTING': True
    }
    app = admin.create_app(settings_override)
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username=ADMIN_USER, password=ADMIN_USER):
        with self._client as c:
            return c.post(
                '/login/',
                data={'username': username, 'password': password}
            )

    def logout(self):
        return self._client.get('/login/exit')


@pytest.fixture
def auth(client):
    test_admin = Admin.collection.insert({'username': ADMIN_USER, 'password': make_hash(ADMIN_USER)})
    yield AuthActions(client) # this is where the testing happens!
    test_admin = Admin.getAdmin(test_admin)
    test_admin.remove()
