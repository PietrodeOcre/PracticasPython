
'''
Created on 9 jun. 2019

@author: pietrodeocre
'''

from Herencia.Vehiculo import Vehiculo
from Herencia.Moto import Moto
from Herencia.Quad import Quad
from Herencia.VElectricos import VElectricos

if __name__ == '__main__':
    
    miMoto = Moto("Honda", "CBR")
    
    #miMoto.caballito()
    
    miMoto.estado()
    
    miMoto2 = Moto("Suzuki", "Burgman125")
    
    miMoto2.caballito()
    
    miMoto2.estado()
    
    
    
    miQuad = Quad("Goes", "720Max")
    
    miQuad.caballito()
    
    miQuad.estado()
    
    miFurgoneta = Vehiculo("Citroen", "Pickup")
    
    miFurgoneta.estado()
    
    miBici=VElectricos("Orbea", "HBO", 25)
    
    miBici.estado()
    
    print(isinstance(miBici, Vehiculo))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pass