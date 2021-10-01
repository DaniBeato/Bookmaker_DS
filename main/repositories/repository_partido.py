import logging
from flask.scaffold import F
from .. import db
from main.models import PartidoModels
from main.utils import logger


logger = logging.getLogger(__name__)


class Partido_Repositorio(Crear, Modificar, Leer, Eliminar):

    def __init__(self,PartidoModeles):
        self.__modelo = PartidoModeles



    def obtener_todos(self):
        objeto = db.session.query(self.__modelo).all()
        return objeto

    def obtener_por_id(self, id):
        objeto = db.session.query(self.__modelo).get(id)
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

    def eliminar(self, id):
        try:
            objeto = db.session.query(self.__modelo).get(id)
            db.session.delete(objeto)
            db.session.commit()
        except Exception:
            logger.error('No se puede borrar %s', id)
            db.session.rollback()



