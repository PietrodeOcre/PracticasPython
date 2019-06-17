'''
Created on 16 jun. 2019

@author: pietrodeocre
'''

import pymysql

if __name__ == '__main__':
    
    ############### CONFIGURAR ESTO ###################
    # Abre conexion con la base de datos
    #db = pymysql.connect("localhost","root","Mjcg1610pc1.2","python_pruebas")
    #single-priva18.privatednsorg.com:2083
    #192.168.1.89 Desde Casa
    #
    db = pymysql.connect("192.168.1.89","pietro","1234","prueba1")
    ##################################################

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # ejecuta el SQL query usando el metodo execute().
    cursor.execute("SELECT VERSION()")
    #cursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(20))")
    #cursor.execute("INSERT INTO PRODUCTOS VALUES('balon',15,'deportes')")
    
    #cursor.commit() solo si se usa sqlite
    '''
    variosProductos=[
        ("camiseta", 10, "deportes"),
        ("jarron", 10, "ceramica"),
        ("camion", 10, "jugueteria")
        ]
    
    cursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",variosProductos)
    '''
    # procesa una unica linea usando el metodo fetchone().
    #data = cursor.fetchone()
    #print ("Database version : {0}".format(data))
    
    #data = cursor.execute("SELECT * FROM PRODUCTOS")
    #print ("Primera tupla: ", data)
    
    
    query = "SELECT * FROM prueba"
    
    cursor.execute(query)
    
    datos = cursor.fetchall()
    
    for row in datos:
        id = row[0]
        nombre = row[1]
        apellidos = row[2]
        edad = row[3]
        print("id = {0}, nombre = {1}, apellidos = {2}, edad = {3}".format(id,nombre,apellidos,edad))
        


    # desconecta del servidor
    db.close()
    
    
    
    pass