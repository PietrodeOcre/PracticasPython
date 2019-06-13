'''
Created on 11 jun. 2019

@author: pietrodeocre
'''

if __name__ == '__main__':
    
    class Coche():

        def desplazamiento(self):
            print("Me desplazo usando Cuatro ruedas")
            
    class Moto():

        def desplazamiento(self):
            print("Me desplazo usando Dos ruedas")
            
    class Camion():

        def desplazamiento(self):
            print("Me desplazo usando Seis ruedas")
            
    '''
    miVehiculo=Moto()
    
    miVehiculo.desplazamiento()
    
    miVehiculo2=Coche()
    
    miVehiculo2.desplazamiento()
    
    miVehiculo3=Camion()
    
    miVehiculo3.desplazamiento()
    '''
    
    def desplazamientoVehiculo(vehiculo):
        vehiculo.desplazamiento()
    
    miVehiculo = Camion()
    
    desplazamientoVehiculo(miVehiculo)
    
    miVehiculo1 = Moto()
    
    desplazamientoVehiculo(miVehiculo1)
    
    pass
