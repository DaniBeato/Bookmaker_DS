from flask_restful import Resource
from flask import request
from .. import db
from main.models import EquipoModels
from main.map import EquipoSchema



equipo_schema = EquipoSchema()



class Equipos(Resource):
    def get(self):
        equipos = db.session.query(EquipoModels)
        return equipo_schema.dump(equipos.all(), many = True)

    def post(self):
        equipo = equipo_schema.load(request.get_json())
        db.session.add(equipo)
        db.session.commit()
        return equipo_schema.dump(equipo), 201




class Equipo(Resource):
    def get(self,id):
       equipo = db.session.query(EquipoModels).get_or_404(id)
       return equipo_schema.dump(equipo.all(), many = True)



    def put(self, id):
        equipo = db.session.query(EquipoModels).get_or_404(id)
        datos = request.get_json().items()
        for clave, valor in datos:
            setattr(equipo, clave, valor)
        db.session.add(equipo)
        db.session.commit()
        return equipo_schema.dump(equipo)


    def delete(self, id):
        equipo = db.session.query(EquipoModels).get_or_404(id)
        db.session.delete(equipo)
        db.session.commit()
        return '', 204

