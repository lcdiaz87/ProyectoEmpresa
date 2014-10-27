__author__ = 'Luis Carlos'


class Empresa():
    def __init__(self, nombre_empresa, cif, razon_social):
        self.nombre_empresa = nombre_empresa
        self.cif = cif
        self.razon_social = razon_social
        self.lista_departamentos = []

    def anadir_departamento(self, dept):
        self.lista_departamentos.append(dept)

