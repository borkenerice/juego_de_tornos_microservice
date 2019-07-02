import requests

from flask import abort


def find_all_places():
    raise NotImplementedError


def find_place_by_id(place_id):
    raise NotImplementedError


def create_place():
    raise NotImplementedError


def update_place(place_id, place_data):
    raise NotImplementedError


def delete_place(place_id):
    raise NotImplementedError
