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
        
    def __str__(self):
        return "{} que trabaja como {} tiene salario {} €".format(self.nombre, self.cargo, self.salario) 