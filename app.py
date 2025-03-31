from flask import Flask
from database.connection import db
from flask_migrate import Migrate
from flask_smorest import Api
from resources.hello_world import blp as HelloWorldBlueprint
from resources.schedule import blp as ScheduleBlueprint

app = Flask(__name__)

# Env vars
app.config.from_pyfile('settings/env.py')
FLASK_HOST = app.config['FLASK_HOST']
FLASK_PORT = app.config['FLASK_PORT']

# DB
db.init_app(app)

# Migrations
migrate = Migrate(app, db)

# Blueprints
api = Api(app)
api.register_blueprint(HelloWorldBlueprint)
api.register_blueprint(ScheduleBlueprint)

print(f'App running on {FLASK_HOST}:{FLASK_PORT} 🚀')