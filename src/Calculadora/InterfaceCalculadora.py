'''
Created on 15 jun. 2019

@author: pietrodeocre
'''

from tkinter import *




if __name__ == '__main__':
    
    #-----Raiz-----
    
    raiz = Tk()
    
    raiz.title("Calculadora")
    
    miFrame=Frame(raiz)
    
    miFrame.pack()
    
    #-----Variables-----
    
    numero=StringVar()
    operacion=""
    resultado=0

    #-----Pantalla-----
    
    pantalla= Entry(miFrame, textvariable=numero)
    
    pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=5)
    
    pantalla.config(background="black", fg="#03f943", justify="right")
    

    #-----Botones-----
    
    def numeroPulsado(num):
        
        global operacion
        
        if operacion!="":
            numero.set(num)
            
            operacion=""
            
        else:
            numero.set(numero.get()+num)
        
        
    def division(num):
        global operacion
        
        global resultado
        
        resultado=resultado//float(num)
        operacion = "division"
        
        numero.set(resultado)
        
    def multiplicacion(num):
        global operacion
        
        global resultado
        
        resultado=resultado*float(num)
        operacion = "multiplicacion"
        
        numero.set(resultado)
        
    def resta(num):
        global operacion
        
        global resultado
        
        resultado=resultado-float(num)
        operacion = "resta"
        
        numero.set(+resultado)
        
    def suma(num):
        global operacion
        
        global resultado
        
        resultado+=float(num)
        operacion = "suma"
        
        numero.set(resultado)
        
    def resultadoTotal():
        global resultado
        
        numero.set(resultado+float(numero.get()))
        
        resultado=0
        
    def clean():

        numero.set(0)
        
    
    #-----fila1-----
    
    boton7=Button(miFrame, text="7", command=lambda:numeroPulsado("7"), width=3)
    boton7.grid(row=2, column=1)
    boton8=Button(miFrame, text="8", command=lambda:numeroPulsado("8"),width=3)
    boton8.grid(row=2, column=2)
    boton9=Button(miFrame, text="9", command=lambda:numeroPulsado("9"),width=3)
    boton9.grid(row=2, column=3)
    botonDivision=Button(miFrame, text="/", command=lambda:division(numero.get()) , width=3)
    botonDivision.grid(row=2, column=4)
    
    #-----fila2-----
    
    boton4=Button(miFrame, text="4", command=lambda:numeroPulsado("4"), width=3)
    boton4.grid(row=3, column=1)
    boton5=Button(miFrame, text="5", command=lambda:numeroPulsado("5"), width=3)
    boton5.grid(row=3, column=2)
    boton6=Button(miFrame, text="6", command=lambda:numeroPulsado("6"), width=3)
    boton6.grid(row=3, column=3)
    botonMultiplicacion=Button(miFrame, text="x", command=lambda:multiplicacion(numero.get()) , width=3)
    botonMultiplicacion.grid(row=3, column=4)
    
    #-----fila3-----
    
    boton1=Button(miFrame, text="1", command=lambda:numeroPulsado("1"), width=3)
    boton1.grid(row=4, column=1)
    boton2=Button(miFrame, text="2", command=lambda:numeroPulsado("2"), width=3)
    boton2.grid(row=4, column=2)
    boton3=Button(miFrame, text="3", command=lambda:numeroPulsado("3"), width=3)
    boton3.grid(row=4, column=3)
    botonResta=Button(miFrame, text="-", command=lambda:resta(numero.get()) , width=3)
    botonResta.grid(row=4, column=4)
    botonClean=Button(miFrame, text="clean", command=lambda:clean() , width=3)
    botonClean.grid(row=4, column=5)
    
    #-----fila4-----
    
    boton0=Button(miFrame, text="0", command=lambda:numeroPulsado("0"), width=3)
    boton0.grid(row=5, column=1)
    decimal=Button(miFrame, text=",", command=lambda:numeroPulsado("."), width=3)
    decimal.grid(row=5, column=2)
    igual=Button(miFrame, text="=", command=lambda:resultadoTotal(), width=3)
    igual.grid(row=5, column=3)
    botonSuma=Button(miFrame, text="+", command=lambda:suma(numero.get()) , width=3)
    botonSuma.grid(row=5, column=4)
    botonSalir=Button(miFrame, text="salir", command=raiz.quit, width=3)
    botonSalir.grid(row=5, column=5)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    raiz.mainloop()
    
    pass