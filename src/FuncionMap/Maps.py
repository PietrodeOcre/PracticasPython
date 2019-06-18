'''
Created on 18 jun. 2019

@author: pietrodeocre
'''

class Empleado(object):
    '''
    classdocs
    '''


    def __init__(self, nombre, cargo, salario):
        '''
        Constructor
        '''
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        
    '''
    equivalencia al toString
    '''
    def __str__(self):
        return "{} que trabaja como {} tiene salario {} €".format(self.nombre, self.cargo, self.salario) 


if __name__ == '__main__':
    
    '''
    aplicamos una funcion a cada uno de los elementos de una lista
    
    '''
    
    listaEmpleados = [
        Empleado("Juan", "Director", 6700),
        Empleado("Ana", "Presidenta", 7500),
        Empleado("Antonio", "Administrativo", 2100),
        Empleado("Sara", "Secretaria", 2150),
        Empleado("Mario", "Botones", 1800)
        ]
    
    def calculaComision(empleado):
        '''
        con este if podemos filtrar 
        para que solo se aplique la funcion a ciertos 
        empleados
        '''
        if empleado.salario<=3000:
            empleado.salario = empleado.salario * 1.03
        
        return empleado
    
    '''
    la funcion Map lo que hara es aplicar la funcion
    a cada objeto empleado de la lista
    '''
    
    listaEmpleadosComision = map(calculaComision, listaEmpleados)
    
    for empleado in listaEmpleadosComision:
        print(empleado)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pass



















