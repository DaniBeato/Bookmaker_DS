from main.models import EmpresaModels
from main.repositories import repositorio_empresa

repositorio = repositorio_empresa()

class EmpresaServices():
    def obtener_empresas(self):
        return repositorio.find_all()

    def obtener_empresa_por_id(self, id):
        return repositorio.find_one(id)
