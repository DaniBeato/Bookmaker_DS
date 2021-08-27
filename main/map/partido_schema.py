from marshmallow import Schema, fields, validate
from marshmallow.decorators import post_load
from main.models import PartidoModels




class Partido(Schema):
    id = fields.Int(dump_only = True)
    fecha = fields.Str(required = True)
    equipo_local = fields.Str(required = True)
    equipo_visitante = fields.Str(required = True)
    finalizado = fields.Bool(required = True)
    ganador = fields.Bool(required = True)

    @post_load
    def make_partido(self, data, **kwargs):
        return PartidoModels(**data)