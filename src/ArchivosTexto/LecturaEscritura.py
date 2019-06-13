'''
Created on 12 jun. 2019

@author: pietrodeocre
'''

from io import open

if __name__ == '__main__':
    
    
    #Lee un archivo y permite guardar 
    archivoTexto = open("Archivo.txt","r+")
    
    #Si el archivo ya existe solo sobre escribe lo que hay 
    #En las posiciones donde escribimos sin mas, el resto
    #Queda igual
    #archivoTexto.write("Comienzo del texto")
    
    #Si se usa python 2.7 o inferior necesario pasar el metodo 
    #frase.decode("utf-8")
    #Ya que si no aparece un error.
    
    #print(archivoTexto.readlines())
    
    lineasTexto= archivoTexto.readlines()
    
    lineasTexto[1] =  "Esta linea ha sido incluida desde el exterior \n"
    
    #Si se usa python 2.7 o inferior necesario pasar el metodo 
    #frase.decode("utf-8")
    #Ya que si no aparece un error.
    
    archivoTexto.seek(0)
    
    archivoTexto.writelines(lineasTexto)
    
    
    
    print(lineasTexto)
    
    archivoTexto.close()
    
    
    pass