'''
Created on 15 ene. 2020

@author: pietrodeocre
'''

if __name__ == '__main__':
    
    
    '''
    Los alumnos de un curso se han dividido en dos grupos A y B 
    de acuerdo al sexo y el nombre. El grupo A esta formado por 
    las mujeres con un nombre anterior a la M y los hombres con 
    un nombre posterior a la N y el grupo B por el resto. 
    Escribir un programa que pregunte al usuario su nombre y 
    sexo, y muestre por pantalla el grupo que le corresponde.
    '''
    nombre = input("¿Como te llamas? ")
    sexo = input("¿Cuál es tu sexo (M o H)? ")
    if (sexo == "M" and nombre.lower() < 'm') or (sexo == "H" and nombre.lower() > 'n'):
        groupo = "A"
    else:
        groupo = "B"
        print("Tu grupo es " + groupo)
    
    
    pass