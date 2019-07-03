from tests.config_test import client


def test_find_all_characters(client):
    """
    Check correct response code for a get request to the character endpoint
    :param client: fixture
    :return:
    """
    response = client.get('/api/character')
    assert response.status_code == 200


def test_find_character_by_id(client):
    """
    Check correct response code for a get request for a character identified by its id
    :param client: fixture
    :return:
    """
    response = client.get('/api/character/1')
    assert response.status_code == 200


def test_find_character_by_id_does_not_exists(client):
    """
    Check correct response code for a get request for a character identified by its id if it does not exists
    :param client: fixture
    :return:
    """
    response = client.get('/api/character/90')
    assert response.status_code == 404


def test_create_character(client):
    """
    Check correct response code for a post request to create a character
    :param client: fixture
    :return:
    """
    character = {
        'name': 'Tirria',
        'place_id': "3",
        'king': False,
        'alive': True
    }
    response = client.post('/api/character', json=character)
    assert response.status_code == 201


def test_create_character_same_name(client):
    """
    Check correct response code for a post request to create a character if it has the same name as one that already exists
    :param client: fixture
    :return:
    """
    character = {
        'name': 'Tirria',
        'place_id': "2",
        'king': False,
        'alive': True
    }
    response = client.post('/api/character', json=character)
    assert response.status_code == 400


def test_update_character(client):
    """
    Check correct response code for a put request to update a character
    :param client: fixture
    :return:
    """
    character = {
        'name': 'Manuel',
        'place_id': "4",
        'king': False,
        'alive': True
    }
    response = client.put('/api/character/1', json=character)
    assert response.status_code == 200


def test_update_character_same_name(client):
    """
    Check correct response code for a put request to update a character if it has the same name as one that already exists
    :param client: fixture
    :return:
    """
    character = {
        'name': 'Manuel',
        'place_id': "4",
        'king': False,
        'alive': True
    }
    response = client.put('/api/character/2', json=character)
    assert response.status_code == 400


def test_delete_character_does_not_exists(client):
    """
    Check correct response code for a delete request to delete a character that do not exists
    :param client: fixture
    :return:
    """
    response = client.delete('/api/character/80')
    assert response.status_code == 404
