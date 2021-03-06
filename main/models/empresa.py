from .. import db

class Empresa(db.Model):
    __tablename__ = "empresas"
    __id = db.Column('id', db.Integer, primary_key=True)
    __razon_social = db.Column('razon_social', db.String(50), nullable=False)
    __email = db.Column('email', db.String(120), nullable=False)



    def __repr__(self):
        return f'< Empresa:  {self.__id} {self.__razon_social}>'





    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id


    @property
    def razon_social(self):
        return self.__razon_social


    @razon_social.setter
    def razon_social(self, razon_social):
        self.__razon_social = razon_social


    @property
    def email(self):
        return self.__email


    @email.setter
    def email(self, email):
        self.__email = email