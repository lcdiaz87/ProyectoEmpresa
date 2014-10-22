__author__ = 'Luis Carlos'

class Empresa():

    def __init__(self, nombreEmpresa, cif, razonSocial):
        self.nombreEmpresa = nombreEmpresa
        self.cif = cif
        self.razonSocial = razonSocial
        self.listaDepartamentos= []

    def anadirDepartamento(self,dept):
        self.listaDepartamentos.append(dept)

