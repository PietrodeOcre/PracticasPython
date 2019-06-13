from setuptools import setup

setup(
    name = "modulo2",
    version = "1.0",
    description = "Realiza resta de dos números",
    author = "Pietrodeocre",
    email = "petrodeocre@gmail.com",
    url = "https://www.nuker-labs.com",
    package = ["Modulo","Modulo2","modulos2"]
    )

'''
Despues de crear el paquete
nos vamos en el terminal al 
directorio donde este el 
archivo setup.py 

Escribiremos 
python setup.py

Esto generará un archivo .tar.gz
este será el instalador que se 
creará en el directorio dist

para instalarlo en python normal y 
en python3 usamos uno de estos dos 
comandos 

pip install nombrePaqueteGenerado.tar.gz
pip3 install nombrePaqueteGenerado.tar.gz

-La segunda para python 3.x

Para desinstalar el paquete

pip uninstall nombrePaqueteGenerado.tar.gz
pip3 uninstall nombrePaqueteGenerado.tar.gz

'''