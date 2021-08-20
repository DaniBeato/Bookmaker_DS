from marshmallow import Schema, fields, validate
from marshmallow.decorators import post_load
from main.models import EquipoModels

class Equipo(Schema):
    id = fields.Int(dump_only = True)
    nombre = fields.Str(required = True)
    escudo = fields.Str(required = True)
    pais = fields.Str(required = True)

    @post_load
    def make_equipo(self, data, **kwargs):
        return EquipoModels(**data)