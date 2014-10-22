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

    def getNombreDpto(self):
        return self.nombreDpto

    def getSalarioTotalAnual(self):
        salarioTotalAnual=0
        for empActual in self.listaEmpleados:
            salarioTotalAnual+=empActual.getSalarioAnual()
        return salarioTotalAnual