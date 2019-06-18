'''
Created on 18 jun. 2019

@author: pietrodeocre
'''

if __name__ == '__main__':
    
    
    def funcionDecoradora(funcionParametro):
        #con *args decimos a una funcion que puede recivir uno o varios parametros
        def funcionInterna(*args, **kwargs):
            #acciones adicionales
            print("Vamos a hacer un calculo: ")
            funcionParametro(*args, **kwargs)
            print("Hemos terminado el calculo")
        return funcionInterna
    '''
    La funcion decoradora no debe ser llamada 
    puesto que antes de la funcion que decoramos
    ponemos @nombredefunciondecoradora
    y automaticamente al llamar a suma()
    esta llama a la fiuncion decoradora y se 
    pone a si misma como parametro de la funcion
    decoradora  
    '''

    
    @funcionDecoradora
    def suma(num1, num2, num3):
        """
        Calcula la suma de tres numeros pasado por parametro (num1,num2,num3)
        """
        print(num1+num2+num3)
    
    @funcionDecoradora
    def resta(num1, num2):
        print(num1-num2)

    @funcionDecoradora
    def potencia(base, exponente):
        print(pow(base,exponente))
    
    suma(15,20,8)
    resta(30,10)
    potencia(base=5,exponente=3)
    
    help(suma)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pass