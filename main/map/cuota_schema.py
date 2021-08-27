from marshmallow import Schema, fields, validate
from marshmallow.decorators import post_load
from main.models import CuotaModels




class Cuota(Schema):
    id = fields.Int(dump_only = True)
    probabilidad_local = fields.Str(required = True)
    probabilidad_empate = fields.Str(required = True)
    probabilidad_visitante = fields.Str(required = True)


    @post_load
    def make_cuota(self, data, **kwargs):
        return CuotaModels(**data)