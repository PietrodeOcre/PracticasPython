'''
Created on 11 jun. 2019

@author: pietrodeocre
'''

from Herencia.Moto import Moto
from Herencia.Vehiculo import Vehiculo

class VElectricos(Moto,Vehiculo):
    '''
    classdocs
    '''


    def __init__(self, marca, modelo, velocidad):
        '''
        Constructor
        '''
        super().__init__(marca, modelo)
        self.velocidad=velocidad