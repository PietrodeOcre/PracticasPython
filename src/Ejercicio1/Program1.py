'''
Created on 7 jun. 2019

@author: pietrodeocre
'''
#  -*- coding: utf-8 -*-
from encodings import undefined
import math
from simplejson.tests.test_pass1 import JSON


if __name__ == '__main__':
    
    '''for i in range(5):
        print (i)
    
    rango = range(5)
    
    for i in rango:
        print (++i)
    
    
    
    numero = input("Digame una cantidad en pesetas: ")
    
    def iteracion(numero):
        #numero2 = range(numero)
        for i in range(numero):
            print("Valor de la variable: ", i)
            
    iteracion(numero)
     
    
    
    Tipos range
    crea matriz de 0 a 4
    range(4)
    
    crea matriz desde el primer numero al segundo
    range(4,7)
    
    crea matriz desde el primer numero al segundo
    pero ademas lo hace en saltos de 5
    range(4,100,5)
    
    #print(len(range(4)))
    
    i = 0
    
    while i<10:
        print("hola5", i)
        i = i + 1
    
    
    edad = int(input("Introduce la edad: "))
    
    while edad<0 or edad>100:
        print("Edad negativa vuelve a interntarlo")
        edad = int(input("Introduce la edad: "))
    
    print("Hola", end=" ")
    print("Hola", end="")
    
    
    
    nombre = "manuel javier"
    
    cont = 0
    
    for i in nombre:
        if 0==" ":
            continue
        cont+=1
    
    print(cont)
    
    class Miclase:
        pass #Implementar mas tarde
    #Pass devuelve un null en bucles
    
    

    import requests
    nombre = "https://google.es/"
    req = requests.put(nombre)
   
    print(req)
    
    print(req.cookies)
    
    print(req.headers)
    
    print(req.headers.keys())
    
    print(req.content)
    
    
    req = requests.post('https://en.wikipedia.org/w/index.php', data = {'search':'Nanotechnology'})
    
    print(req.content)
    
    
    req.raise_for_status()
    with open('Nanotechnology.html', 'wb') as fd:
        for chunk in req.iter_content(chunk_size=50000):
            fd.write(chunk)
    
    
    
    
    #Con funcion normal
    lista = []
    def pares(lista):
        for i in range(0,10):
            if(i%2==0):
                int(i)
                lista.append(i)
        return lista
    
    pares(lista)
    
    print(lista)
    
    for i in lista:
        print(i)
    
    #Generadores
    def pares(limite):
        num = 1
        while num<limite:
            if(num%2==0):
                yield num
            num+=1
    
    for i in pares(10):
        print(i)
    
    par = pares(10)
    
    print(next(par))
    
    print(next(par))
    
    print(next(par))
    
    
    #Generadores con yield from
    def devuelveCiudades(*ciudades):
        for elemento in ciudades:
            #for subElemento in elemento:
                yield from elemento
    
    ciudadesDevueltas = devuelveCiudades("Madrid","Barcelona","Cadiz","bilbao")
    
    print(next(ciudadesDevueltas))
    
    print(next(ciudadesDevueltas))
    
    
    #Captura o control de excepciones
    def divide(num1, num2):
        try:
            return num1/num2
        #Si dividimos entre 0 
        except ZeroDivisionError:
            print("No se puede dividir entre cero")
            return "Operacion errónea"
    
    print(divide(8,0))
    
    print("hola")
    
    #Introducción de letras en lugar de números
    #Captura de exceptión
    try:
        num3 = int(input("Escribe un número.: "))
    except ValueError:
        num3 = ''
        print("Eso no es un número")

    print(num3)
    
    
    #Introducción de números en lugar de letras
    #Captura de exceptión
    try:
        num3 = str(input("Escribe una cadena de text: "))
    except ValueError:
        num3 = ''
        print("Eso no es un texto")

    print(num3)
    
    #TryCatch en python
    while True:
        try:
            op1=int(input("Escribe un número: "))
            op2=int(input("Escribe otro número: "))
            break
        except ValueError:
            print("Error, el valor no es numérico.")
        except ZeroDivisionError:
            print("No se puede dividir por cero.")
        finaly
    
    print("Salí del bucle.")

    #TryCatch en python
    while True:
        try:
            op1=int(input("Escribe un número: "))
            op2=int(input("Escribe otro número: "))
            break
        except:
            print("Se ha producido un error.")
        finally: #Se ejecuta si o si, exista o no error.
            print("Salí del bucle.")
    
    #El try sin except y sin finally devuelve error
    
    
    
    def evaluaEdad(edad):
        
        if edad < 0:
            
            try:
                raise TypeError("Eso es imposible")
            except TypeError as ErrorFeo:
                print(ErrorFeo)
                return "Error"
        
        if edad < 20:
            return "Eres muy joven"
        elif edad < 40:
            return "Eres joven"
        elif edad < 65:
            return "Eres maduro"
        elif edad < 100:
            return "Cuídate..."
    
    print(evaluaEdad(-18))
    
    '''
    
    import Coche
    
    miCoche=Coche()

    print(miCoche.anchoChasis)     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pass
