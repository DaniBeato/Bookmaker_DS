from .. import db
from main.models import ClientModels


class Client_Repositorio(Crear, Modificar, Leer, Eliminar):

    def __init__(self,ClientModels):
        self.__modelo = ClientModels



    def obtener_todos(self):
        objeto = db.session.query(self.__modelo).all()
        return objeto

    def obtener_por_id(self, id):
        objeto = db.session.query(self.__modelo).filter(self.__activado == True)
        return objeto

    def crear(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        return objeto

    def modificar(self,objeto,id):
        objeto = db.session.query(self.__modelo).get(id)
        for clave, valor in objeto:
            setattr(objeto, clave, valor)
        db.session.add(objeto)
        db.session.commit()
        return objeto

    def __soft_delete(self, objeto):
        objeto.__activado = False
        self.update(objeto, objeto.id)

    def eliminar(self, id):
        objeto = db.session.query(self.__modelo).get(id)
        #db.session.delete(objeto)
        #db.session.commit()
        self.__soft_delete(objeto)



