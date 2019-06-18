'''
Created on 18 jun. 2019

@author: pietrodeocre
'''
import re


if __name__ == '__main__':
    
    nombre1 = "Sandra Lopez"
    nombre2 = "1Antonio Gomez"
    nombre3 = "sandra Lopez"
    nombre4 = "lara Lopez"
    
    '''
    con el tercer parametro re.IGNORECASE ignora el case sensitive
    '''
    if re.match("Sandra", nombre3, re.IGNORECASE):
        print("Encontrado")
    else:
        print("No encontrado")
        
    if re.match("Sandra", nombre1):
        print("Encontrado")
    else:
        print("No encontrado")
    
    '''
    Se puede usar patrones directamente en la busqueda
    el punto es comodin de un caracter
    '''
    
    if re.match(".ara", nombre4):
        print("Encontrado")
    else:
        print("No encontrado")
    
    '''
    Para buscar por ejemplo si empiezan por un numero
    '''
    
    if re.match("\d", nombre2):
        print("Encontrado")
    else:
        print("No encontrado")
    
    '''
    la funcion match siempre busca solo al principio de la 
    cadena de texto el metodo search busca en todo el texto
    '''
    
    if re.search("\d", nombre2):
        print("Encontrado")
    else:
        print("No encontrado")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pass