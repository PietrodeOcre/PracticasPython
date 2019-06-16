'''
Created on 16 jun. 2019

@author: pietrodeocre
'''
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from numpy.core.defchararray import title


if __name__ == '__main__':
    
    
    def infoAdicional():
        messagebox.showinfo("Ejemplo Menu", "Este es un ejemplo verision 1 de un menu en ventana")
    
    
    def avisoLicencia():
        messagebox.showwarning("Licencia", "Producto bajo licencia GNU")
        
    def salirApp():
        #valor = messagebox.askquestion("Salir", "¿Desea Salir de la Aplicación")
        valor = messagebox.askokcancel("Salir", "¿Desea Salir de la Aplicación?")
        if valor == True:
            raiz.destroy()
    
    def cerrarDocumento():
        valor = messagebox.askretrycancel("Reintentar", "Imposible cerrar, documento bloqueado")
        if valor == False:
            raiz.destroy()
    
    def abrirArchivo():
        archivo = filedialog.askopenfilename(title="Abrir", initialdir="/home/pietrodeocre", filetypes=(("Ficheros Excell", "*.txt"),("Ficheros de texto", "*.rss")))
        print(str(archivo))
    
    
    
    raiz = Tk()
    raiz.title("Menu de prueba")
    
    
    barraMenu = Menu(raiz)
    
    raiz.config(menu=barraMenu)
    
    archivoMenu = Menu(barraMenu, tearoff=0)
    archivoEdifion = Menu(barraMenu, tearoff=0)
    archivoHerramientas = Menu(barraMenu, tearoff=0)
    archivoAyuda = Menu(barraMenu, tearoff=0)
    
    barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
    barraMenu.add_cascade(label="Edición", menu=archivoEdifion)
    barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
    barraMenu.add_cascade(label="ayuda", menu=archivoAyuda)
    
    archivoMenu.add_command(label="Nuevo", command = abrirArchivo)
    archivoMenu.add_command(label="Guardar")
    archivoMenu.add_separator()
    archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
    archivoMenu.add_command(label="Salir", command=salirApp)
    
    
    archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
    archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    raiz.mainloop()
    
    pass