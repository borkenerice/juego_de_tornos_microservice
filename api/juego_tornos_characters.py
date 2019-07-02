import requests

import config
from flask import abort


def find_all_characters():
    try:
        r = requests.get(config.CHARACTERS_ENDPOINT)
        if r.status_code == 200:
            return r.json()
        else:
            return r.status_code
    except requests.ConnectionError:
        abort(500, f'ConnectionError: A connection to the service could not be established')


def create_character(character_data):
    raise NotImplementedError


def find_characters_by_place_id(character_id):
    raise NotImplementedError


def find_character_by_id(character_id):
    raise NotImplementedError


def update_character(character_id, character_data):
    raise NotImplementedError


def delete_character_by_id(character_id, character_data):
    raise NotImplementedError
