from .. import db
from main.models import ApuestaModels


class Apuesta_Repositorio(Crear, Leer):

    def __init__(self,ApuestaModels):
        self.__modelo = ApuestaModels



    def obtener_todos(self):
        objeto = db.session.query(self.__modelo).all()
        return objeto

    def obtener_por_id(self, id):
        objeto = db.session.query(self.__modelo).all()
        return objeto

    def crear(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        return objeto

