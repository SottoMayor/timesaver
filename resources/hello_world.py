from flask_smorest import Blueprint
from flask.views import MethodView

blp = Blueprint('hello-world', __name__, url_prefix="/", description='initial blueprint.')

@blp.route('/')
class HelloWorld(MethodView):
    def get(self):
        return '<main><h1>Health Check!</h1> <p>Vá para <a href="/schedules">/schedules</a> para interagir com o app.</p></main>'