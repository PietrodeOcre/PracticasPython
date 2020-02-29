'''
Created on 17 ene. 2020

@author: pietrodeocre
'''

if __name__ == '__main__':
    
    '''
    Escribir un programa que almacene la cadena de caracteres
     contrasena en una variable, pregunte al usuario por la 
     contrasena e imprima por pantalla si la contrasena introducida 
     por el usuario coincide con la guardada en la variable sin 
     tener en cuenta mayusculas y minusculas.
    '''
    
    contrasena = raw_input("Escribe la contrasena: ")
    
    
    repetida = raw_input("Repite la contrasena: ")
    
    if contrasena.__eq__(repetida):
        print ("Es correcta")
    else:
        print ("es incorrecta")
    
    
    
    
    
    pass