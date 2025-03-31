from flask import render_template, redirect, url_for
from flask_smorest import Blueprint
from flask.views import MethodView
from flask import request
from marshmallow import ValidationError
from schemas.schedule_schema import ScheduleSchema
from database.connection import db
from models.schedule import ScheduleModel

blp = Blueprint('Schedules', __name__, url_prefix="/schedules", description='Blueprint para agendamentos.')

@blp.route('/')
class SchedulesList(MethodView):
    def get(self):
        return render_template("index.html")
    
    def post(self):
        schema = ScheduleSchema()
        try:
            data = schema.load(request.form)
        except ValidationError as err:
            return {"errors": err.messages}, 400

        schedule = ScheduleModel(
        client=data['cliente'],
        service=data['servico'],
        schedule_date=data['data'],
        schedule_time=data['horario']
        )

        db.session.add(schedule)
        db.session.commit()

        return redirect(url_for('Schedules.SchedulesList'))
    
    
@blp.route('/create')
class SchedulesCreate(MethodView):
    def get(self):
        return render_template("create.html")

    
@blp.route('/update/<int:schedule_id>')
class SchedulesUpdate(MethodView):
    def get(self, schedule_id):
        print('schedule_id', schedule_id)
        return render_template("update.html")
    
    def post(self, schedule_id):
        print('schedule_id', schedule_id)
    
@blp.route('/delete/<int:schedule_id>')
class SchedulesDelete(MethodView):
    def post(self, schedule_id):
        print('schedule_id del', schedule_id)
        return redirect(url_for('Schedules.SchedulesList'))