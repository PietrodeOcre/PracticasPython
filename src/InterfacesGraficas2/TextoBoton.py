'''
Created on 13 jun. 2019

@author: pietrodeocre
'''
from tkinter import *


if __name__ == '__main__':
    
    raiz = Tk()#Creamos la ventana
    
    raiz.title("Mi segunda ventana")#Le damos titulo
    
    miFrame = Frame(raiz)#Creamos un frame
    miFrame.config(width=1600, height=1600)#Le damos un tamanio determinado
    miFrame.pack()#se empaqueta

    #creamos un label, texto en ventana
    nombreLabel = Label(miFrame, text="Nombre: ")
    '''
    Le decimos en que celda de una rejilla imaginaria 
    contiene dicho texto
    ''' 
    nombreLabel.grid(row=0, column = 1,sticky="w",padx=4,pady=4)
    
    '''
    Tambien puede indicarse en coordenadas
    pero para formularios es mejor con rejillas
    '''
    #nombreLabel.place(x=100, y=100)
    
    passwLabel = Label(miFrame, text="Password: ")
    passwLabel.grid(row=1, column = 1,sticky="w",padx=4,pady=4)
    
    
    apellidoLabel = Label(miFrame, text="Apellido: ")
    apellidoLabel.grid(row=2, column = 1,sticky="w",padx=4,pady=4)
    '''
    Con la opcion sticky colocamos la alineacion del 
    elemento segun puntos cardinales en ingles
           n
    w            e
           s
    o sus puntos intermedios combinando las letras 
    '''
    direccionLabel = Label(miFrame, text="Direccion: ")
    direccionLabel.grid(row=3, column = 1,sticky="w",padx=4,pady=4)
    
    '''
    Podemos crear cuadros de texto para 
    escribir en ellos
    '''
    cuadroNombre = Entry(miFrame)
    cuadroNombre.grid(row = 0, column = 2,padx=4,pady=4)
    
    cuadroPassw = Entry(miFrame)
    cuadroPassw.grid(row = 1, column = 2,padx=4,pady=4)
    cuadroPassw.config(show="*")
    
    '''
    padx y pady son para anadir padding vertical y horizontal
    '''
    cuadroApellido=Entry(miFrame)
    cuadroApellido.grid(row=2, column=2,padx=4,pady=4)
    
    cuadroDireccion=Entry(miFrame)
    cuadroDireccion.grid(row=3, column=2,padx=4,pady=4)
    
    '''
    Este boton solo cierra la ventana
    '''
    Button(miFrame, text="Salir", command=raiz.quit).grid(row=4,column=1,sticky="w",padx=4,pady=4)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    raiz.mainloop()
    
    pass