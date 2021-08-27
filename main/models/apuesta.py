from .. import db
from sqlalchemy.ext.hybrid import hybrid_property


class Apuesta(db.Model):
    __id = db.Column('id', db.Integer, primary_key = True)
    __fecha = db.Column('fecha', db.String(100), nullable = False)
    __monto = db.Column('monto', db.String(100), nullable = False)
    __equipo_ganador = db.Column('equipo_ganador', db.ForeignKey('equipo.id')), nullable = False)

    def __repr__(self):
        return f'< Cliente:  {self.__id} {self.__probabilidad_local} {self.__probabilidad_empate} {self.__probabilidad_visitante}>'


    @hybrid_property
    def id(self):
        return self.__id


    @id.setter
    def id(self, id):
        self.__id = id


    @id.deleter
    def id(self):
        del self.__id


    @hybrid_property
    def probabilidad_local(self):
        return self.__probabilidad_local


    @probabilidad_local.setter
    def probabilidad_local(self, probabilidad_local):
        self.__probabilidad_local = probabilidad_local


    @hybrid_property
    def probabilidad_empate(self):
        return self.__probabilidad_empate


    @probabilidad_empate.setter
    def probabilidad_empate(self, probabilidad_empate):
        self.__probabilidad_empate = probabilidad_empate


    @hybrid_property
    def probabilidad_visitante(self):
        return self.__probabilidad_visitante


    @probabilidad_visitante.setter
    def probabilidad_visitante(self, probabilidad_visitante):
        self.__probabilidad_visitante = probabilidad_visitante

