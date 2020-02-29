'''
Created on 15 ene. 2020

@author: pietrodeocre
'''


if __name__ == '__main__':
     
    peso = input("Escribe tu peso en Kg:")
    
    altura = input("Escribe su altura en metros:")
    
    if altura < 0:
        print("La altura debe ser mayor que 0")
    else:  
        print("MCI: " + str(peso/(altura**2)))  
        
    pass


