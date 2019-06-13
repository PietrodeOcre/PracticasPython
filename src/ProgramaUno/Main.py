'''
Created on 7 jun. 2019

@author: pietrodeocre

def cuentaPalabra(i, texto, cont):
    for i in texto.split(" "):
        #print (i)
        if i == "una":
            cont = cont + 1
        #palabra = ""
    
    return cont

'''

from __future__ import print_function

def cuentaPalabra(i, texto, cont):
    for i in texto.split(" "):
        #print (i)
        if i == "una":
            cont += 1
        #palabra = ""
    
    return cont

if __name__ == '__main__':
    
    print ("Hola Mundo!")
    
    print ("Hola Mundo")
    
    nombre = "Manuel"
    
    print (nombre)
    
    print (45 % 3)
    
    print (2**3 )
    
    print (9//4.6)
    
    #print "" + 5
    
    print ("5" + "")
    
    print (type(nombre))
    
    def programa(boleano):
        
        if(boleano == True):
            print ("hola mundo")
        else:
            print ("Adios mundo cruel")    
        
    
    variable =  False
        
    programa(variable)
    
    
    while (variable):
        print ("ya no mas")
        break
    
    
    def programa2(num, num2):
        resultado = num + num2
        return resultado
    
    res = programa2(3,4)
    
    print (res)
    
    nombres = ["Manuel", "Javier", "Pedro", 5]
    
    print (nombres)
    
    print (nombres[1])
    
    nombres.append("Luis")
    
    print (nombres[2:])
    
    nombres.insert(2, 34)
    
    nombres.extend(["4", "Veintidos", 45, "Pedro"])
    print (nombres)
    
    print (nombres.index("Javier"))
    
    print ("Pedro" in nombres)

    nombres.remove("Javier")

    print (nombres)
    
    nombres.pop()
    
    print (nombres)
    
    nombres2 = ["4", "Veintidos", 45, "Pedro"] * 3
    
    nombres3 = nombres + nombres2
    
    print (nombres3)
    
    nombres4 = ("Manuel", "Padre", 34, "Manuel")
    
    print (nombres4)
    
    print (nombres4.index(34))
    
    print (nombres4[nombres4.index(34)])
    
    nombres5 = list(nombres4)
    
    print (nombres5)
    
    hola = tuple(nombres5)
    
    print (34 in hola)
    
    print (nombres4.count("Manuel"))

    print (len(nombres4))
    
    mitupla = ("juan",)
    
    print (len(mitupla))
    
    print (mitupla.count("juan"))
    
    nombre1, nombre2, num, nombre3 = nombres4
    
    print (nombre1 + nombre2 + nombre3,num) 
    
    nombreDiccionario = {"clave1":"Manuel","clave2":"Manuel2"}
    
    print (nombreDiccionario)
    
    nombreDiccionario["Italia"]="Lisboa"
    
    print (nombreDiccionario)
    
    nombreDiccionario["Portugal"]="Lisboa"
    
    print (nombreDiccionario)
    
    del nombreDiccionario["Italia"]  
    
    print (nombreDiccionario)
    
    mitupla = [1,2,3,4,5,6,7]
    
    nD = {mitupla[0]:"Manuel", mitupla[1]:"Carlos", mitupla[2]:{"Temporada":[2,3,5,4,6,4]}}
    
    print (nD)
    
    print (nD[1])
    
    print (nD[3])
    
    print (nD.keys())
    
    print (nD.values())
    
    print (len(nD))
    
    if nD[1]!="Manuel":
        print ("Igual")
    elif False:
        print ("Si")
    else:
        print ("no")
       
    #num = input("Escribe un numero: ")
    #int (num)
    #print num
    
    edad = -200
    
    if 0<edad<100:
        print ("correcta")
    else:
        print ("Incorrecta")

    for i in [1,3]:
        print(i, end=" ")
    
    num =  range(4)
 
    for i in num:
        print(i)
        
    texto = "Esto es una cadena de textoq ue quiero iterar para ver si tiee una palabra"
    
    palabra = ""
    
    
    cont = 0
   
    print (texto.split(" "))
    
    cont = cuentaPalabra(i, texto, cont)
        
    print ("numero de veces", cont)    
        
    
        
    pass