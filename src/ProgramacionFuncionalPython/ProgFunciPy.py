'''
Created on 18 jun. 2019

@author: pietrodeocre
'''
from ProgramacionFuncionalPython.Empleado import Empleado


if __name__ == '__main__':
    
    def numeroPar(num):
        if num%2==0:
            return True

    numeros = [176, 35,56,454,3,56,7,88,32]
    
    
    '''
    En este ejercicio la funcion filter
    se usa como programacion funcional en 
    python para poder ejecutar una 
    funcion sobre una variables en este 
    caso es una lista, y vemos que se lo aplica a 
    todos los elementos de la lista
    '''
    print(list(filter(numeroPar, numeros)))
    
    '''
    Tambien podemos hacer lo mismo con una funcion lambda
    '''
    
    print(list(filter(lambda num: num%2==0, numeros)))
    
    
    listaEmpleados = [
        Empleado("Juan", "Director", 750000),
        Empleado("Ana", "Presidenta", 850000),
        Empleado("Antonio", "Administrativo", 25000),
        Empleado("Sara", "Secretaria", 27000),
        Empleado("Mario", "Botones", 21000)
        ]
    
    
    '''
    ser capaces de filtrar por un dato de un objeto de tipo
    persona con una funcion lambda no es tan dificil
    pero como es una lista, despues iteramos la variable
    donde ponemos el filtro, con un for y 
    los que aparecen son los que pasan dicho filtro.
    '''
    salariosAltos = filter(lambda empleado:empleado.salario>50000, listaEmpleados)
    
    for salario in salariosAltos:
        print(salario)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pass