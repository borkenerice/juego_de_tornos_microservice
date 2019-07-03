import requests

import config
from flask import abort
from werkzeug.exceptions import NotFound

from api.juego_tornos_characters import find_characters_by_place_id


def find_all_places():
    try:
        r = requests.get(config.PLACES_ENDPOINT)
        if r.status_code == 200:
            return r.json()
        else:
            abort(r.status_code, r.json())
    except requests.ConnectionError:
        abort(500, f'ConnectionError: A connection to the service could not be established')


def find_place_by_id(place_id):
    try:
        r = requests.get(f'{config.PLACES_ENDPOINT}/{place_id}')
        if r.status_code == 200:
            return r.json()
        else:
            abort(r.status_code, r.json())
    except requests.ConnectionError:
        abort(500, f'ConnectionError: A connection to the service could not be established')


def find_places_and_characters():
    places = find_all_places()
    new_places = []
    for place_position in range(len(places)):
        place = places[place_position]
        place['characters'] = []
        try:
            characters = find_characters_by_place_id(place['place_id'])
            for character_position in range(len(characters)):
                place['characters'].append(characters[character_position])
        # capture the exception raised if no character is found for the place id
        except NotFound:
            pass
        new_places.append(place)
    return new_places


def create_place(place_data):
    try:
        r = requests.post(f'{config.PLACES_ENDPOINT}', json=place_data)
        if r.status_code == 201:
            return r.json(), 201
        else:
            abort(r.status_code, r.json())
    except requests.ConnectionError:
        abort(500, f'ConnectionError: A connection to the service could not be established')


def update_place(place_id, place_data):
    try:
        r = requests.put(f'{config.PLACES_ENDPOINT}/{place_id}', json=place_data)
        if r.status_code == 200:
            return r.json()
        else:
            abort(r.status_code, r.json())
    except requests.ConnectionError:
        abort(500, f'ConnectionError: A connection to the service could not be established')


def delete_place(place_id):
    try:
        r = requests.delete(f'{config.PLACES_ENDPOINT}/{place_id}')
        if r.status_code == 200:
            return f'Place {place_id} deleted'
        else:
            abort(r.status_code, r.json())
    except requests.ConnectionError:
        abort(500, f'ConnectionError: A connection to the service could not be established')
