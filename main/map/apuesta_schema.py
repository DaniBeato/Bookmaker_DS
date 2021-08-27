from marshmallow import Schema, fields, validate
from marshmallow.decorators import post_load
from main.models import ApuestaModels
from DateTime import  datetime




class Apuesta(Schema):
    id = fields.Int(dump_only = True)
    fecha = fields.DateTime(required = True)
    emonto = fields.Str(required = True)
    equipo_ganador = fields.Str(required = True)


    @post_load
    def make_apuesta(self, data, **kwargs):
        return ApuestaModels(**data)