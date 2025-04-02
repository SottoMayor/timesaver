from flask import render_template, redirect, url_for
from flask_smorest import Blueprint
from flask.views import MethodView
from flask import request
from marshmallow import ValidationError
from schemas.schedule_schema import ScheduleSchema
from database.connection import db
from models.schedule import ScheduleModel
from datetime import date

blp = Blueprint('Schedules', __name__, url_prefix="/schedules", description='Blueprint para agendamentos.')

@blp.route('/')
class SchedulesList(MethodView):
    def get(self):
        query = ScheduleModel.query

        date = request.args.get("date")
        client = request.args.get("client")
        service = request.args.get("service")

        if date:
            query = query.filter(ScheduleModel.schedule_date == date)
        if client:
            query = query.filter(ScheduleModel.client.ilike(f"%{client}%"))
        if service:
            query = query.filter(ScheduleModel.tuss_description.ilike(f"%{service}%"))

        schedules = query.order_by(ScheduleModel.schedule_date).all()
        
        at_least_one = ScheduleModel.query.first()
        return render_template("index.html", schedules=schedules, at_least_one=at_least_one)
    
    def post(self):
        tuss = [
            {"code": "10101012", "desc": "Consulta médica em consultório"},
            {"code": "20103038", "desc": "Exame de glicemia em jejum"},
            {"code": "30101016", "desc": "Hemograma completo"},
            {"code": "40301033", "desc": "Raio-X de tórax"},
            {"code": "50101018", "desc": "Ultrassonografia do abdome total"},
        ] # como se fosse uma chamada de API
        
        schema = ScheduleSchema()
        try:
            data = schema.load(request.form)
        except ValidationError as err:
            return {"errors": err.messages}, 400
        
        tuss_resul = next((item for item in tuss if item["code"] == data['tuss_codigo']), None)
        if(not tuss_resul):
            return {"errors": err.messages}, 404

        schedule = ScheduleModel(
        client=data['cliente'],
        schedule_date=data['data'],
        schedule_time=data['horario'].strftime('%H:%M:%S'),
        tuss_code=tuss_resul['code'],
        tuss_description=tuss_resul['desc'],
        agreement=(data['convenio'] or None)
        )

        db.session.add(schedule)
        db.session.commit()

        return redirect(url_for('Schedules.SchedulesList'))
    
    
@blp.route('/create')
class SchedulesCreate(MethodView):
    def get(self):
        today = date.today().isoformat()
        agreements = ["Unimed", "Bradesco Saúde", "Amil", "SulAmérica"]
        tuss = [
            {"code": "10101012", "desc": "Consulta médica em consultório"},
            {"code": "20103038", "desc": "Exame de glicemia em jejum"},
            {"code": "30101016", "desc": "Hemograma completo"},
            {"code": "40301033", "desc": "Raio-X de tórax"},
            {"code": "50101018", "desc": "Ultrassonografia do abdome total"},
        ] # como se fosse uma chamada de API
        
        return render_template("create.html", current_date=today, agreements=agreements, tuss=tuss)

    
@blp.route('/update/<int:schedule_id>')
class SchedulesUpdate(MethodView):
    def get(self, schedule_id):
        schedule = ScheduleModel.query.get_or_404(schedule_id)
        today = date.today().isoformat()
        agreements = ["Unimed", "Bradesco Saúde", "Amil", "SulAmérica"]
        tuss = [
            {"code": "10101012", "desc": "Consulta médica em consultório"},
            {"code": "20103038", "desc": "Exame de glicemia em jejum"},
            {"code": "30101016", "desc": "Hemograma completo"},
            {"code": "40301033", "desc": "Raio-X de tórax"},
            {"code": "50101018", "desc": "Ultrassonografia do abdome total"},
        ] # como se fosse uma chamada de API
        
        return render_template("update.html", schedule=schedule, current_date=today, agreements=agreements, tuss=tuss)
    
    def post(self, schedule_id):
        tuss = [
            {"code": "10101012", "desc": "Consulta médica em consultório"},
            {"code": "20103038", "desc": "Exame de glicemia em jejum"},
            {"code": "30101016", "desc": "Hemograma completo"},
            {"code": "40301033", "desc": "Raio-X de tórax"},
            {"code": "50101018", "desc": "Ultrassonografia do abdome total"},
        ]
        
        schedule = ScheduleModel.query.get_or_404(schedule_id)
        
        schema = ScheduleSchema()

        try:
            data = schema.load(request.form)
        except ValidationError as err:
            return {"errors": err.messages}, 400
        
        tuss_resul = next((item for item in tuss if item["code"] == data['tuss_codigo']), None)
        if(not tuss_resul):
            return {"errors": err.messages}, 404
        
        print(request.form, tuss_resul)

        schedule.client = data['cliente']
        schedule.schedule_date = data['data']
        schedule.schedule_time = data['horario'].strftime('%H:%M:%S')
        schedule.tuss_code = tuss_resul['code']
        schedule.tuss_description = tuss_resul['desc']
        schedule.agreement = (data['convenio'] or None)

        db.session.commit()
        return redirect(url_for('Schedules.SchedulesList'))
    

@blp.route('/delete/<int:schedule_id>')
class SchedulesDelete(MethodView):
    def post(self, schedule_id):
        schedule = ScheduleModel.query.get_or_404(schedule_id)
        db.session.delete(schedule)
        db.session.commit()
        return redirect(url_for('Schedules.SchedulesList'))