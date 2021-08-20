from flask_restful import Resource
from flask import request
from .. import db
from main.models import ClientModels
from main.map import ClientSchema
from main.map import ClienteFiltros



client_schema = ClientSchema()



class Clients(Resource):
    def get(self):
        filtros = request.data
        clients = db.session.query(ClientModels)
        client_filter = ClienteFiltros(clients)
        for key, value in request.get_json().items():
            consulta = client_filter.aplicar_filtro(key, value)
        return client_schema.dump(consulta.all(), many = True)

    def post(self):
        client = client_schema.load(request.get_json())
        db.session.add(client)
        db.session.commit()
        return client_schema.dump(client), 201




class Client(Resource):
    def get(self,id):
       client = db.session.query(ClientModels).get_or_404(id)
       return client_schema.dump(client.all(), many = True)



    def put(self, id):
        client = db.session.query(ClientModels).get_or_404(id)
        datos = request.get_json().items()
        for clave, valor in datos:
            setattr(client, clave, valor)
        db.session.add(client)
        db.session.commit()
        return client_schema.dump(client)


    def delete(self, id):
        cliente = db.session.query(ClientModels).get_or_404(id)
        db.session.delete(cliente)
        db.session.commit()
        return '', 204

