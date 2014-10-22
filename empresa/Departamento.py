__author__ = 'aulas'


class Departamento():

    def __init__(self, nombreDpto, idDpto):
        self.nombreDpto = nombreDpto
        self.idDpto = idDpto
        self.listaEmpleados= []

    def anadirEmpleado(self,emp):
        self.listaEmpleados.append(emp)

    def getSalarioTotal(self):
        salarioTotal=0
        for empActual in self.listaEmpleados:
            salarioTotal+=empActual.getSalario()
        return salarioTotal