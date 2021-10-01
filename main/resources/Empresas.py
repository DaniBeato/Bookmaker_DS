from flask_restful import Resource
from flask import request
from .. import db
from main.models import EmpresaModels
from main.map import EmpresaSchema
from main.services import EmpresaServices



empresa_schema = EmpresaSchema()
empresa_service = EmpresaServices()



class Empresas(Resource):
    def get(self):
        return empresa_schema.dump(empresa_service.obtener_empresas(), many = True)

    def post(self):
        empresa = empresa_schema.load(request.get_json())
        db.session.add(empresa)
        db.session.commit()
        return empresa_schema.dump(empresa), 201




class Empresa(Resource):
    def get(self,id):
       empresa = db.session.query(EmpresaModels).get_or_404(id)
       return empresa_schema.dump(empresa.all(), many = True)



    def put(self, id):
        empresa = db.session.query(EmpresaModels).get_or_404(id)
        datos = request.get_json().items()
        for clave, valor in datos:
            setattr(empresa, clave, valor)
        db.session.add(empresa)
        db.session.commit()
        return empresa_schema.dump(empresa)


    def delete(self, id):
        empresa = db.session.query(EmpresaModels).get_or_404(id)
        db.session.delete(empresa)
        db.session.commit()
        return '', 204