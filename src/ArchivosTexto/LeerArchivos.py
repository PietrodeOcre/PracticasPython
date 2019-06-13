'''
Created on 12 jun. 2019

@author: pietrodeocre
'''

from io import open

if __name__ == '__main__':
    '''
    
    #leer el archivo completo
    archivoTexto = open("Archivo.txt","r")
    
    texto = archivoTexto.read()
    
    archivoTexto.close()

    print(texto)
    
    
    
    #devuelve contenido como lista, cada linea un elemento
    archivoTexto = open("Archivo.txt","r")
    
    lineasTexto=archivoTexto.readlines()
    
    archivoTexto.close()
    
    print(lineasTexto)
    
    print(lineasTexto[0])
    
     '''
    
    #Imprime el contenido una vez
    #Mueve el puntero a la posicion 0 y
    #Vuelve a imprimir el contenido 
    #desde la posicion cero
    archivoTexto = open("Archivo.txt","r")
    
    #Leemos desde el caracter 11
    #arcivoTexto.seek(11)
    
    #Lee solo hasta la posicion 11
    print(archivoTexto.read(11))
    
    archivoTexto.seek(0)
    
    #Si se usa python 2.7 o inferior necesario pasar el metodo 
    #frase.decode("utf-8")
    #Ya que si no aparece un error.
    
    #Muestra solo la mitad del contenido del archivo
    #archivoTexto.seek(len(archivoTexto.read())/2)
    
    #Muestra solo el contenido desde el final de la linea
    #archivoTexto.seek(len(archivoTexto.readline()))
    
    print(archivoTexto.read())
    
    archivoTexto.close()

   
    
    
    
    
    
    
    
    
    
    pass