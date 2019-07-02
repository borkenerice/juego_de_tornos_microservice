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


def test_find_all_places(client):
    """
    Check correct response code for a get request to the place endpoint
    :param client: fixture
    :return:
    """
    response = client.get('/api/place')
    assert response.status_code == 200


def test_find_place_by_id(client):
    """
    Check correct response code for a get request for a place identified by its
    :param client: fixture
    :return:
    """
    response = client.get('/api/place/1')
    assert response.status_code == 200


def test_find_place_by_id_does_not_exists(client):
    """
    Check correct response code for a get request for a place identified by its id if it does not exists
    :param client: fixture
    :return:
    """
    response = client.get('/api/place/90')
    assert response.status_code == 404


def test_create_place(client):
    """
    Check correct response code for a post request to create a place
    :param client: fixture
    :return:
    """
    place = {
        'name': 'Place Create Test'
    }
    response = client.post('/api/place', json=place)
    assert response.status_code == 201


def test_create_place_same_name(client):
    """
    Check correct response code for a post request to create a place if it has the same name as one that already exists
    :param client: fixture
    :return:
    """
    place = {
        'name': 'Place Create Test'
    }
    response = client.post('/api/place', json=place)
    assert response.status_code == 400


def test_update_place(client):
    """
    Check correct response code for a put request to update a place
    :param client: fixture
    :return:
    """
    place = {
        'name': 'Place Update Test',
    }
    response = client.put('/api/place/1', json=place)
    assert response.status_code == 200


def test_update_place_same_name(client):
    """
    Check correct response code for a put request to update a place if it has the same name as one that already exists
    :param client: fixture
    :return:
    """
    place = {
        'name': 'Place Update Test',
    }
    response = client.put('/api/place/2', json=place)
    assert response.status_code == 400


def test_delete_place(client):
    """
    Check correct response code for a delete request to delete a place
    :param client: fixture
    :return:
    """
    response = client.delete('/api/place/1')
    assert response.status_code == 200


def test_delete_place_does_not_exists(client):
    """
    Check correct response code for a delete request to delete a place that do not exists
    :param client: fixture
    :return:
    """
    response = client.delete('/api/place/80')
    assert response.status_code == 404
