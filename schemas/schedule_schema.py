from marshmallow import Schema, fields, validates, ValidationError
from datetime import datetime

class ScheduleSchema(Schema):
    cliente = fields.String(required=True)
    tuss_codigo = fields.String(required=True)
    data = fields.Date(required=True)
    horario = fields.Time(required=True)
    convenio = fields.String(required=False)

    @validates('data')
    def validate_data(self, value):
        if value < datetime.today().date():
            raise ValidationError("A data não pode estar no passado.")
