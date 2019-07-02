import os

DEBUG = True
TESTING = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SWAGGER_DIR = os.path.join(BASE_DIR, 'api', 'swagger.yml')
