from marshmallow import Schema, fields, validate
from marshmallow.decorators import post_load
from main.models import EmpresaModels

class Empresa(Schema):
    id = fields.Int(dump_only = True)
    razon_social = fields.Str(required = True)
    email = fields.Str(required = True, validate = validate.Email())

    @post_load
    def make_empresa(self, data, **kwargs):
        return EmpresaModels(**data)