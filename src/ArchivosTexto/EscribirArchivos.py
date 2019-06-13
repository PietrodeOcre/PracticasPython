'''
Created on 12 jun. 2019

@author: pietrodeocre
'''

from io import open

if __name__ == '__main__':
    '''
    archivoTexto = open("Archivo.txt","w")
    
    frase="Estupendo dia para estudiar Python \n el Miercoles"
    
    archivoTexto.write(frase.decode('utf-8'))
    
    archivoTexto.close()
    '''
    
    archivoTexto = open("Archivo.txt","a")
    
    frase="\nSiempre es una buena ocasion para estudiar python"
    
    archivoTexto.write(frase)
    
    #Si se usa python 2.7 o inferior necesario pasar el metodo 
    #frase.decode("utf-8")
    #Ya que si no aparece un error.
    
    archivoTexto.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pass