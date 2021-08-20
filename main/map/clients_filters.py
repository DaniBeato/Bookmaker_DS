from main.models import ClientModels



class ClienteFiltros():


    def __init__(self, clients):
        self.__clients = clients
        self.__dict_filters = {"id": self.__filtro_por_id,
                       "nombre": self.__filtro_por_nombre,
                       "apellido": self.__filtro_por_apellido,
                       "email": self.__filtro_por_email
                       }



    def __filtro_por_id(self, value):
        return self.__clients.filter(ClientModels.id == int(value))


    def __filtro_por_nombre(self, value):
        return self.__clients.filter(ClientModels.nombre.like('%' + value + '%'))



    def __filtro_por_apellido(self, value):
        return self.__clients.filter(ClientModels.apellido.like('%' + value + '%'))


    def __filtro_por_email(self, value):
        return self.__clients.filter(ClientModels.email.like('%' + value + '%'))



    def aplicar_filtro(self, key, value):
        return self.__dict_filters[key](value)

















