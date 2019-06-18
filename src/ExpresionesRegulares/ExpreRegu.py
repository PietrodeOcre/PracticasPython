'''
Created on 18 jun. 2019

@author: pietrodeocre
'''

import re
from re import search

if __name__ == '__main__':
    
    '''
    para hacer busquedas los rangos de 
    caracteres y letras y demas.
    '''
    cadena = "Vamos a aprender expresiones regulares"
    
    '''
    equivalente a contains de java
    '''
    objeto =  re.search("aprender", cadena)
    print(objeto)
    
    texto = "aprender"
    
    textoEncontrado = re.search(texto,cadena)
    
    print(textoEncontrado.start())
    
    print(textoEncontrado.end())
    
    print(textoEncontrado.span())
    
    '''
    if re.search(texto, cadena) is not None:
        print( "texto encontrado")
    else:
        print( "texto NO encontrado")
    '''
    
    cadena2 = "Vamos a programar expresiones regulares en Python. Python es un lenguaje de programacion"
    
    textoBuscar = "Python"
    
    
    '''
    Como vemos con findall nos muestra una lista con todas las 
    coincidencias en un texto determinado
    si usamos la funcion len
    podemos ver el numero de veces que un patron se repite en un texto
    '''
    print(len(re.findall(textoBuscar,cadena2)))
    
    
    '''
    realizar busquedas con caracteres  y patrones, rangos, etc
    '''
    
    
    listaNombres = ["http://pildoras.es","http://pildoras.com","http://pildorasespaña.net", "ftp://pildoras.es", "Ana Gomez", "Maria Martin", "Sandra Lopez", "Santiago Martin", "Sandra Fernandez"]
    
    '''
    el caracter ^ es para ver los que comienzan por lo sque siga
    '''
    
    for elemento in listaNombres:
        if re.findall('^Sandra', elemento):
            print(elemento)
    
    for elemento in listaNombres:
        if re.findall('^ftp', elemento):
            print(elemento)
    
    '''
    el caracter ~ es para ver los que finalizan por lo vaya delante del simbolo
    '''
    
    for elemento in listaNombres:
        if re.findall('Martin$', elemento):
            print(elemento)
    
    
    for elemento in listaNombres:
        if re.findall('es$', elemento):
            print(elemento)
    
    
    '''
    patrones de busqueda entre corchetes
    '''
    
    for elemento in listaNombres:
        if re.findall('[ñ]', elemento):
            print(elemento)
    
    '''
    esto es equivalente e igual al metodo que teniamos en java
    para filtrar por vocales consonantes y numeros.
    tambien son llamadas anclas
    '''
    
    otraLista = [
        'hombres',
        'mujeres',
        'mascotas',
        'camion',
        'camión'
        ]
    
    for elemento in otraLista:
        if re.findall('cami[oó]n', elemento):
            print(elemento)
    
    '''
    rangos de patrones de busquedas
    '''
    
    otraLista2 = [
        'Ana',
        'Pedro',
        'Maria',
        'Rosa',
        'Sandra',
        'Celia'
        ]
    
    for elemento in otraLista2:
        #desde la o hasta la t,  distingue mayus y minus
        if re.findall('^[O-T,o-t]', elemento):
            print(elemento)
    '''
    si el ^ esta dentro del [^a-b] indica que esos elementos del rando no 
    deben aparecer para que no aparezcan por ejemplo los que no comiencen en A
    ^[^A] seria asi
    '''
    
    for elemento in otraLista2:
        #desde la o hasta la t,  distingue mayus y minus
        if re.findall('^[^A]', elemento):
            print(elemento)
    
    
    
    
    
    
    
    
    
    
    
    
    pass