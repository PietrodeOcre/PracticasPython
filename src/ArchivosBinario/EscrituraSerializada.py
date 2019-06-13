'''
Created on 12 jun. 2019

@author: pietrodeocre
'''

import pickle

if __name__ == '__main__':
    
    listaNombre = ["Pedro", "Ana", "Maria", "Isabel"]
    
    ficheroExterno = open("listanombres", "wb")
    
    pickle._dump(listaNombre, ficheroExterno)
    
    ficheroExterno.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pass