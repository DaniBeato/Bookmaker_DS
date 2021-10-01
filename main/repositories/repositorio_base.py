from abc import ABC, abstractmethod

class Crear(ABC):
    @abstractmethod
    def crear(self, objeto):
        pass


class Leer(ABC):
    @abstractmethod
    def obtener_todos(self):
        pass

    @abstractmethod
    def obtener_uno(self, objeto):
        pass

class Modificar(ABC):
    @abstractmethod
    def modificar(self, objeto,id):
        pass


class Eliminar(ABC):
    @abstractmethod
    def eliminar(self, objeto):
        pass


