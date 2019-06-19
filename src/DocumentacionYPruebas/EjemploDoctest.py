'''
Created on 19 jun. 2019

@author: pietrodeocre
'''

import math

def fib(n):
    """ 
    Calculates the n-th Fibonacci number iteratively  

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(10) 
    55
    >>> fib(15)
    611
    >>> 
    
    """
    
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def areaTriang(num1,num2):
    """ 
    Calculates the nth Fibonacci number iteratively  

    >>> areaTriang(3,6)
    0
    >>> 
    >>> areaTriang(3,6)
    9.0
    >>>
    
    """
    
    
    return (num1*num2)/2

def raizCuadrada(listanNumeros):
    """
    Funcion que devuelve las raices cuadradas de una lista
    
    >>> lista=[]
    >>> for i in [4, 9, 16]
    ...     lista.append(i)
    >>> lista=[2.0, 3.0, 4.0]
    >>> raizCuadrada(lista)
        [1.4142135623730951, 1.7320508075688772, 2.0]
    >>>
    
    """
    
    return [math.sqrt(n) for n in listanNumeros]





















if __name__ == "__main__": 
    import doctest
    doctest.testmod()
