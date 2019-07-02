import requests

import config
from flask import abort


def find_all_places():
    try:
        r = requests.get(config.PLACES_ENDPOINT)
        if r.status_code == 200:
            return r.json()
        else:
            return r.status_code
    except requests.ConnectionError:
        abort(500, f'ConnectionError: A connection to the service could not be established')


def find_place_by_id(place_id):
    try:
        r = requests.get(f'{config.PLACES_ENDPOINT}/{place_id}')
        if r.status_code == 200:
            return r.json()
        else:
            return r.json(), r.status_code
    except requests.ConnectionError:
        abort(500, f'ConnectionError: A connection to the service could not be established')


def create_place(place_data):
    try:
        r = requests.post(f'{config.PLACES_ENDPOINT}', json=place_data)
        if r.status_code == 200:
            return r.json()
        else:
            return r.json(), r.status_code
    except requests.ConnectionError:
        abort(500, f'ConnectionError: A connection to the service could not be established')


def update_place(place_id, place_data):
    try:
        r = requests.put(f'{config.PLACES_ENDPOINT}/{place_id}', json=place_data)
        if r.status_code == 200:
            return r.json()
        else:
            return r.json(), r.status_code
    except requests.ConnectionError:
        abort(500, f'ConnectionError: A connection to the service could not be established')


def delete_place(place_id):
    try:
        r = requests.delete(f'{config.PLACES_ENDPOINT}/{place_id}')
        if r.status_code == 200:
            return f'Place {place_id} deleted', r.status_code
        else:
            return r.json(), r.status_code
    except requests.ConnectionError:
        abort(500, f'ConnectionError: A connection to the service could not be established')
