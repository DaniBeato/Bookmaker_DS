from .. import db

class Equipo(db.Model):
    __id = db.Column(db.Integer, primary_key = True)
    __nombre = db.Column(db.String(100), nullable = False)
    __escudo = db.Column(db.String(100), nullable = False)
    __pais = db.Column(db.String(100), nullable = False)



    def __repr__(self):
        return f'< Equipo:  {self.__id} {self.__nombre} {self.__pais}>'



    @property
    def id(self):
        return self.__id


    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def escudo(self):
        return self.__escudo


    @escudo.setter
    def escudo(self, escudo):
        self.__escudo = escudo

    @property
    def pais(self):
        return self.__pais


    @pais.setter
    def pais(self, pais):
        self.__pais = pais

