'''
Created on 12 jun. 2019

@author: pietrodeocre
'''


from Tkinter import *


if __name__ == '__main__':
    
    raiz = Tk()
    
    raiz.title("Ventana de Pruebas")
    
    #Con esta no deja redimensiona
    #raiz.resizable(0,0)
    
    #cambia icono de menu de ventana
    #raiz.iconbitmap("nombrearchivo.ico")
    
    raiz.geometry("650x350")
    
    raiz.config(bg="blue")
    
    miFrame = Frame() 
    
    #Con esto hanclamos el Frame aun lateral de la ventana
    #miFrame.pack(side = "top",anchor = "s")
    #Con esto otro se rellena la ventana con el frame horizontalmente
    #miFrame.pack(fill="x")
    #Con esto se rellena la ventana verticalmente con el frame
    #miFrame.pack(fill="y", expand = True)
    #PAra rellentar la ventana con el frame automaticamente
    miFrame.pack(fill="both", expand = True)
    
    miImagen=PhotoImage(file="Roberto.png")
    
    #miFrame.config(bg = "red")
    
    miFrame.config(width="650", height = "350")
    
    #miFrame.config(bd="35")
    
    #tipos de bordes para el frame
    #miFrame.config(relief = "groove")
    
    #miFrame.config(relief = "sunken")
    
    #Cambiar el cursor al entrar en el frame
    #miFrame.config(cursor="hand2")
    #miFrame.config(cursor="pirate")
    
    #Todo lo aplicado a los frames puede
    #ser aplicado a la raiz
    
    '''
    miLabel = Label(miFrame, text="Hola",
                     fg="red",
                    font=("Comic Sans MS",18)
                    ).place(x=100,y=200)
    #Adapta el tamanio del frame si no se ha especificado 
    #al tamanio del texto del label
    #miLabel.pack()
    '''
    #Para mostrar la imagen en una ventana
    miLabel = Label(miFrame, image=miImagen).place(x=5,y=5)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    raiz.mainloop()
    
    pass