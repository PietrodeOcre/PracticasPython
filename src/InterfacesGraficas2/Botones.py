'''
Created on 15 jun. 2019

@author: pietrodeocre
'''
from tkinter import *

if __name__ == '__main__':

    raiz = Tk()
    
    raiz.title("Mi segunda ventana")
    
    miFrame = Frame(raiz)
    miFrame.config(width=1600, height=1600)
    miFrame.pack()
    
    miNombre=StringVar()
    
    nombreLabel = Label(miFrame, text="Nombre: ")
    nombreLabel.grid(row=0, column = 1,sticky="w",padx=4,pady=4)
    cuadroNombre = Entry(miFrame, textvariable=miNombre)
    cuadroNombre.grid(row = 0, column = 2,padx=4,pady=4)


    def codigoBoton():
        miNombre.set("Juan")   
    
    botonEnvio = Button(raiz, text="Enviar", command=codigoBoton)
    botonEnvio.pack()
    
    Button(miFrame, text="Salir", command=raiz.quit).grid(row=5,column=1,sticky="w",padx=4,pady=4)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    raiz.mainloop()
    
    pass
