import pytest

from api import create_app


@pytest.fixture(scope='module')
def client():
    """
    fixture that initializes the flask app to be used in the tests
    :return: flask app
    """
    app = create_app()
    client = app.test_client()
    with app.app_context():
        yield client
