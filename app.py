from flask import Flask
from database.connection import db

app = Flask(__name__)

# Env vars
app.config.from_pyfile('settings/env.py')
FLASK_HOST = app.config['FLASK_HOST']
FLASK_PORT = app.config['FLASK_PORT']

# DB
db.init_app(app)

@app.route('/')
def hello_world():
    return "ok!"

print(f'App running on {FLASK_HOST}:{FLASK_PORT} 🚀')