from unittest import TestCase
from Empleado import *
from Departamento import *
from mockito import *
__author__ = 'aulas'


class TestDepartamento(TestCase):
    def test_getSalarioTotal(self):
        #creacion de empleados por "mockito-python"
        emp1=mock(Empleado)
        emp2=mock(Empleado)
        emp3=mock(Empleado)
        emp4=mock(Empleado)
        emp5=mock(Empleado)
        #decimos lo que tiene que devolver de la funcion "getSalario()" en cada empleado
        when(emp1).getSalario().thenReturn(100)
        when(emp2).getSalario().thenReturn(200)
        when(emp3).getSalario().thenReturn(300)
        when(emp4).getSalario().thenReturn(400)
        when(emp5).getSalario().thenReturn(500)

        # creamos el departamento y le asignamos los empleados creados
        dept=Departamento("departamento1",1)
        dept.anadirEmpleado(emp1)
        dept.anadirEmpleado(emp2)
        dept.anadirEmpleado(emp3)
        dept.anadirEmpleado(emp4)
        dept.anadirEmpleado(emp5)
        # realizamos la funcion
        res = dept.getSalarioTotal()
        print res
        self.assertEqual(res,1500)

    def test_getSalarioTotalAnual(self):
        #creacion de empleados por "mockito-python"
        emp1=mock(Empleado)
        emp2=mock(Empleado)
        emp3=mock(Empleado)
        emp4=mock(Empleado)
        emp5=mock(Empleado)
        #decimos lo que tiene que devolver de la funcion "getSalario()" en cada empleado
        when(emp1).getSalarioAnual().thenReturn(1000)
        when(emp2).getSalarioAnual().thenReturn(2000)
        when(emp3).getSalarioAnual().thenReturn(3000)
        when(emp4).getSalarioAnual().thenReturn(4000)
        when(emp5).getSalarioAnual().thenReturn(5000)

        # creamos el departamento y le asignamos los empleados creados
        dept=Departamento("departamento2",2)
        dept.anadirEmpleado(emp1)
        dept.anadirEmpleado(emp2)
        dept.anadirEmpleado(emp3)
        dept.anadirEmpleado(emp4)
        dept.anadirEmpleado(emp5)
        # realizamos la funcion
        res = dept.getSalarioTotalAnual()
        print res
        self.assertEqual(res,15000)