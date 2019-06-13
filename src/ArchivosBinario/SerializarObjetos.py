'''
Created on 12 jun. 2019

@author: pietrodeocre
'''
import pickle

class Vehiculo():
    
    def __init__(self, marca, modelo):
        
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False
        
    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True
        
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
              self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando", self.frena)
        
    def __str__(self):
        return "{} {}".format(self.marca, self.modelo)


        
coche1 = Vehiculo("Mazda", "MX5")
coche2 = Vehiculo("Seat", "Leon")
coche3 = Vehiculo("Renault", "Megane")
coche4 = Vehiculo("Seat", "Lada")
        
coches = [coche1,coche2,coche3,coche4]        
        
        

if __name__ == '__main__':
    
    
    #Desde aqui serializaos los objetos dentro de una lista
    ficheroCoches = open("Coches.dat", "wb")
    
    pickle.dump(coches,ficheroCoches)
    
    ficheroCoches.close()
    
    del(ficheroCoches)
    
    
    #Desde aqui leemos los objetos serializados devolviendo una lista
    ficheroCochesApertura = open("Coches.dat", "rb")
    
    misCoches = pickle.load(ficheroCochesApertura)
    
    for c in misCoches:
        #c.estado()
        print(c)
    
    '''
    
    Si estas dos cosas estan en dos archivos diferentes
    no funcionará por que tendran que estar importada 
    las clase Vehiculo en los dos archivos,
    de manera que python sepa que tipo de objetos esta leyendo
    
    '''
    
    
    #Equivalente a toString en python es el def __str__(self):
    print(misCoches[0])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pass