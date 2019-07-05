import os

DEBUG = True
TESTING = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SWAGGER_DIR = os.path.join(BASE_DIR, 'api', 'swagger.yml')


# services endpoints
PLACES_API_URL = 'places_api:8081/api'
PLACES_ENDPOINT = f'{PLACES_API_URL}/place'

CHARACTERS_API_URL = 'places_api:8082/api'
CHARACTERS_ENDPOINT = f'{CHARACTERS_API_URL}/character'
CHARACTERS_FIND_BY_PLACE_ENDPOINT = f'{CHARACTERS_ENDPOINT}/findByPlace'


