'''
Created on 19 jun. 2019

@author: pietrodeocre
'''
import doctest

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
    Calculates the n-th Fibonacci number iteratively  

    >>> areaTriang(3,6)
    0
    >>> 
    >>> areaTriang(3,6)
    9.0
    >>>

    """
    
    
    return (num1*num2)/2

if __name__ == "__main__": 
    doctest.testmod()
