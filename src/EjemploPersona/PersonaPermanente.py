'''
Created on 12 jun. 2019

@author: pietrodeocre
'''
import pickle

class Persona:
    
    def __init__(self, nombre, apellido, genero, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona con este nombre: ", self.nombre)
        
    def __str__(self):
        return "{} {} {} {}".format(self.nombre, self.apellido, self.genero, self.edad)
    
class ListaPersonas:
    
    personas = []
    
    def __init__(self):
        listaPersonas = open("PersonasFichero", "ab+")
        listaPersonas.seek(0)
        
        try:
            self.personas = pickle.load(listaPersonas)
            print("Hay {} personas.".format(len(self.personas)))
        except:
            print("Fichero vacio")
        finally:
            listaPersonas.close()
            del(listaPersonas)
        
    
    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFichero()
        
        
    def mostrarPersnas(self):
        for p in self.personas:
            print(p)
    
    def guardarPersonasEnFichero(self):
        listaPersonas = open("PersonasFichero", "wb")
        pickle.dump(self.personas, listaPersonas)
        listaPersonas.close()
        del(listaPersonas)
        
    def mostrarInfoFicheroExtero(self):
        print("La informacion es: ")
        for p in self.personas:
            print(p)
            
        
        
    
    
    
    
    
    
    
    
    
    
    

if __name__ == '__main__':
    
    miLista=ListaPersonas()
    
    p=Persona("Sandra","Rocha","Femenino", 25)
    miLista.agregarPersonas(p)
    p1=Persona("Pedro","Garcia","Masculino", 42)
    miLista.agregarPersonas(p1)
    p2=Persona("Manuel","Corral","Masculino", 38)
    miLista.agregarPersonas(p2)
    
    miLista.mostrarInfoFicheroExtero()
    
    p3=Persona("Javier","González","Masculino", 38)
    miLista.agregarPersonas(p3)
    
    miLista.mostrarInfoFicheroExtero()
    
    
    '''
    p=Persona("Sandra","Rocha","Femenino", 25)
    
    miLista.agregarPersonas(p)
    
    miLista.mostrarPersnas()
    '''
    
    
    
    
    
    
    pass