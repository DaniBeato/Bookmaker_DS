from flask.scaffold import F
from .. import db
from main.models import EmpresaModels
from main.repositories.repositorio_base import Crear, Leer, Modificar, Eliminar


class EmpresaRepositorio(Crear, Leer, Modificar, Eliminar):
    def __init__(self):
        self.__modelo = EmpresaModels

    def find_all(self):
        objetos = db.session.query(self.__modelo).filter(self.__modelo.__activado == True).all()
        return objetos

    def find_one(self, id):
        objeto = db.session.query(self.__modelo).get_or_404(id)
        return objeto

    def create(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        return objeto

    def delete(self, id):
        objeto = db.session.query(self.__modelo).get_or_404(id)
        # db.session.delete(objeto)
        # db.session.commit()
        self.__soft_delete(objeto, id)

    def __soft_delete(self, objeto):
        objeto.__activado = False
        self.update(objeto, id)

    def update(self, data, id):
        objeto = db.session.query(self.__modelo).get_or_404(id)
        for key, value in data:
            setattr(objeto, key, value)
        db.session.add(objeto)
        db.session.commit()
        return objeto