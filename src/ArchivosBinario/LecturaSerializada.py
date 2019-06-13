'''
Created on 12 jun. 2019

@author: pietrodeocre
'''
import pickle

if __name__ == '__main__':
    
    ficheroExterno = open("listanombres", "rb")
    
    listaNombres = pickle.load(ficheroExterno)
    
    print(listaNombres)
    
    ficheroExterno.close()
    
    pass