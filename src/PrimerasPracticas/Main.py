'''
Created on 9 jun. 2019

@author: pietrodeocre
'''

from Modulo.modulos1 import *
from Modulo.Modulo2.modulos2 import *

# from __future__ import print_function
if __name__ == '__main__':
    
    i = 0
    
    while i < 10:
        print(i, end=' ')
        i = i + 1
    
    import requests   
    
    req = requests.get("http://google.es")
    print("")
    print(req)
    print(req.content)
    
    sumar(2, 4)
    restar(4, 5)
    multiplicar(3, 2)
     
    pass
