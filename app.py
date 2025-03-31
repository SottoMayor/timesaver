from flask import Flask

app = Flask(__name__)

# Env vars
app.config.from_pyfile('settings/env.py')
FLASK_HOST = app.config['FLASK_HOST']
FLASK_PORT = app.config['FLASK_PORT']

@app.route('/')
def hello_world():
    return "ok!"

print(f'App running on {FLASK_HOST}:{FLASK_PORT} 🚀')