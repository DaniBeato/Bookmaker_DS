from .. import db
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime


class Partido(db.Model):
    __tablename__ = "partidos"
    __id = db.Column('id', db.Integer, primary_key=True)
    __fecha = db.Column('fecha', db.DateTime, nullable=False)
    __equipo_local = db.Column('equipo_local', db.ForeignKey('equipos.id'), nullable=False)
    __equipo_visitante = db.Column('equipo_visitante', db.ForeignKey('equipos.id'), nullable=False)
    __finalizado = db.Column('finalizado', db.Boolean)
    __ganador = db.Column('ganador', db.String(50))
    __goles_local = db.Column('goles_local', db.Integer, nullable=False)
    __goles_visitante = db.Column('goles_visitante', db.Integer, nullable=False)
    cuota = db.relationship('Cuota', back_populates='partido', uselist=False)


    def __repr__(self):
        return f'< Cliente:  {self.__id} {self.__fecha} {self.__equipo_local}>'



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
    def fecha(self):
        return self.__fecha


    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha




    @hybrid_property
    def equipo_local(self):
        return self.__equipo_local


    @equipo_local.setter
    def equipo_local(self, equipo_local):
        self.__equipo_local = equipo_local




    @hybrid_property
    def equipo_visitante(self):
        return self.__equipo_visitante


    @equipo_visitante.setter
    def equipo_visitante(self, equipo_visitante):
        self.__equipo_visitante = equipo_visitante




    @hybrid_property
    def finalizado(self):
        return self.__finalizado


    @finalizado.setter
    def finalizado(self, finalizado):
        self.__finalizado = finalizado






    @hybrid_property
    def ganador(self):
        return self.__ganador

    @ganador.setter
    def ganador(self, ganador):
        self.__ganador = ganador





    @hybrid_property
    def goles_local(self):
        return self.__goles_local

    @goles_local.setter
    def goles_local(self, goles_local):
        self.__goles_local = goles_local





    @hybrid_property
    def goles_visitante(self):
        return self.__goles_visitante

    @goles_visitante.setter
    def goles_visitante(self, goles_visitante):
        self.__goles_visitante = goles_visitante






