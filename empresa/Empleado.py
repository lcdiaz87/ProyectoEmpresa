__author__ = 'aulas'


class Empleado():
    def __init__(self, nombre, apellidos, dni, direccion, edad, email, salario):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.edad = edad
        self.email = email
        self.salario = salario

    def get_salario(self):
        return self.salario

    def get_dni(self):
        return self.dni

    def get_nombre_apellido(self):
        return self.nombre % " " % self.apellidos

    def get_edad(self):
        return self.edad

    def get_email(self):
        return self.email

    def get_direccion(self):
        return self.direccion

    def get_salario_anual(self):
        return self.salario * 12
