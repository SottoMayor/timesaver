from flask_smorest import Blueprint
from flask.views import MethodView

blp = Blueprint('hello-world', __name__, url_prefix="/", description='initial blueprint.')

@blp.route('/')
class HelloWorld(MethodView):
    def get(self):
        return 'OK'