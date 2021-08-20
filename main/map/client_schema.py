from marshmallow import Schema, fields, validate
from marshmallow.decorators import post_load
from main.models import ClientModels

class Client(Schema):
    id = fields.Int(dump_only = True)
    nombre = fields.Str(required = True)
    apellido = fields.Str(required = True)
    email = fields.Str(required = True, validate = validate.Email())

    @post_load
    def make_client(self, data, **kwargs):
        return ClientModels(**data)
