from os import environ

FLASK_APP=environ.get("FLASK_APP")
FLASK_ENV=environ.get("FLASK_ENV")
FLASK_DEBUG=environ.get("FLASK_DEBUG")
FLASK_HOST=environ.get("FLASK_HOST", 'localhost')
FLASK_PORT=environ.get("FLASK_PORT", '5000')