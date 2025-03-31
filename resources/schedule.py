from flask_smorest import Blueprint
from flask.views import MethodView

blp = Blueprint('Schedules', __name__, url_prefix="/schedules", description='Blueprint para agendamentos.')

@blp.route('/')
class Schedules(MethodView):
    def get(self):
        return 'GET SCHEDULE'
    
    def post(self):
        return 'POST SCHEDULE'
    
    def patch(self):
        return 'PATCH SCHEDULE'
    
    def delete(self):
        return 'DELETE SCHEDULE'
    