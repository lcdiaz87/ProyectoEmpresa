__author__ = 'aulas'


class Departamento():
    def __init__(self, nombre_dpto, id_dpto):
        self.nombre_dpto = nombre_dpto
        self.id_dpto = id_dpto
        self.lista_empleados = []

    def anadir_empleado(self, emp):
        self.lista_empleados.append(emp)

    def get_salario_total(self):
        salario_total = 0
        for emp_actual in self.lista_empleados:
            salario_total += emp_actual.get_salario()
        return salario_total

    def get_nombre_dpto(self):
        return self.nombre_dpto

    def get_salario_total_anual(self):
        salario_total_anual = 0
        for emp_actual in self.lista_empleados:
            salario_total_anual += emp_actual.get_salario_anual()
        return salario_total_anual