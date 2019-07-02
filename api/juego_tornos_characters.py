import requests

import config
from flask import abort


def find_all_characters():
    try:
        r = requests.get(config.CHARACTERS_ENDPOINT)
        return r.json()
    except requests.ConnectionError:
        abort(500, f'ConnectionError: A connection to the service could not be established')


def create_character(character_data):
    raise NotImplementedError


def find_characters_by_place_id(place_id):
    try:
        r = requests.get(f'{config.CHARACTERS_FIND_BY_PLACE_ENDPOINT}/{place_id}')
        if r.status_code == 200:
            return r.json()
        else:
            abort(r.status_code, r.json())
    except requests.ConnectionError:
        abort(500, f'ConnectionError: A connection to the service could not be established')


def find_character_by_id(character_id):
    raise NotImplementedError


def update_character(character_id, character_data):
    raise NotImplementedError


def delete_character_by_id(character_id, character_data):
    raise NotImplementedError
