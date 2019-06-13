'''
Created on 9 jun. 2019

@author: pietrodeocre
'''
from __builtin__ import True, False

class Coche(object):
    '''
    classdocs
    '''
    def __init__(self, largoChasis, anchoChasis, ruedas):
        '''
        Constructor
        '''
        
        #dos guiones bajos significa que es privada
        #las llamadas a la variable dentro de la clase
        #sera tambien con guiones bajos, pero desde fuera 
        #no hay acceso 
        self.__largoChasis = int(largoChasis)
        self.__anchoChasis = int(anchoChasis)
        self.__ruedas = int(ruedas)
        self.__enMarcha = False
        
        
        
        
    def arrancar(self, marcha):
        
        self.__enMarcha = marcha
        
        if(self.__enMarcha):
            chequeo=self.__chequeoInterno()
        
        if(self.__enMarcha and chequeo):
            return "El coche esta arrancado"
        elif self.__enMarcha and chequeo == False:
            return "Algo fue mal en el chequeo."
        else:
            return "El coche esta parado"
        
    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", 
              self.__anchoChasis, " y un largo de ", self.__largoChasis)
    
    def __chequeoInterno(self):
        print("Realizando Chequeo")
        self.gasolina = "ok"
        self.aceite = "mal"
        self.puertas = "cerradas"
        
        if self.gasolina=="ok" and self.aceite == "ok" and self.puertas=="cerradas":
            return True
        else:
            return False
        
        
    
#self es el this de java pero hay 
#que ponerlo como primer parametro en todos los metodos
    
        
        
        
        

miCoche=Coche(250, 120, 4)

print(miCoche.arrancar(True))

miCoche.estado()

print("Segundo Objeto.........................................")

miCoche2=Coche(250, 120, 4)

print(miCoche2.arrancar(False))

miCoche2.estado()























