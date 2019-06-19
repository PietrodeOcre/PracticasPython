'''
Created on 19 jun. 2019

@author: pietrodeocre
'''
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(areaTriangulo(3,6), 9.0)

def areaTriangulo(base,altura):
    """
    Calcula el area de un Triangulo dado
    
    >>>areaTriangulo(3,6)
    8
    
    """
        
    return (base*altura)/2

if __name__ == '__main__':   
    
    
    unittest.main()
    
    
    
    
    
    
    pass