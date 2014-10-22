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

    def getSalario(self):
        return self.salario

    def getDni(self):
        return self.dni

    def getNombreApellido(self):
        return self.nombre %" "% self.apellidos
