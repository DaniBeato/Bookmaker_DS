from main.models import EmpresaModels
from main.repositories import Repositorio

repo = Repositorio(EmpresaModels)

class EmpresaServices():
    def obtener_empresas(self):
        return repo.obtener_todos()

    def obtener_empresa_por_id(self, id):
        return repo.obtener_por_id(id)
