import setuptools

#Si tienes un readme
with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='HABZONEpy',  #nombre del paquete
     version='0.1', #versión
     scripts=['zona_habitable.py'] , #nombre del ejecutable
     author="ignacio solis", #autor
     author_email="ignacio.solis.m@usach.cl", #email
     description="un paquete para encontrar la zona habitable de una estrella", #Breve descripción
     long_description=long_description,
   long_description_content_type="text/markdown", #Incluir el README.md si lo has creado
     url="https://github.com/nachowo21/HABZONEpy.git", #url donde se encuentra tu paquete en Github
     packages=setuptools.find_packages(), #buscamos todas las dependecias necesarias para que tu paquete funcione (por ejemplo numpy, scipy, etc.)
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 ) #aquí añadimos información sobre el lenguaje usado, el tipo de licencia, etc.

