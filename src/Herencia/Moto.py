'''
Created on 9 jun. 2019

@author: pietrodeocre
'''
from Herencia.Vehiculo import Vehiculo

class Moto(Vehiculo):
    '''
    classdocs
    '''

    
    def __init__(self, marca, modelo):
   
        super().__init__(marca, modelo)
    
    
    
    hCaballito=""
    def caballito(self):
        self.hCaballito="Hago caballito"
        
       
    def estado(self):
        super().estado()
        print(self.hCaballito, "\n")