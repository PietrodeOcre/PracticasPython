'''
Created on 9 jun. 2019

@author: pietrodeocre
'''


class Vehiculo(object):
    '''
    classdocs
    '''


    def __init__(self, marca, modelo):
        '''
        Constructor
        '''
        self.__marca = marca
        self.__modelo = modelo
        self.__enMarcha = False
        self.__acelera = False
        self.__frena = False
    
    def arrancar(self):
        self.__enMarcha = True
        
    def acelerar(self):
        self.__acelera = True
        
    def frenar(self):
        self.__frena = True
        
    def estado(self):
        print("Marca: ", self.__marca, "\nModelo: ", self.__modelo,
              "\nEn Marcha: ", self.__enMarcha, "\nAcelerado: ", 
              self.__acelera, "\nFrenado: ", self.__frena, "\n")
        
    