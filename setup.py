from setuptools import setup #no es necesario añadirlo como dependencia

with open('README.md', 'r') as fh: #saltarselo si no tienes el README en la carpeta del projecto
    long_description = fh.read()

setup(
      name = 'HABZONEpy', # aqui el nombre de la carpeta donde esta tu modulo/archivo/programa
      version = '1.0.3', # la version correspondiente del programa, VERSION, no commit de github
      license = 'MIT',
      description = 'codigo para visualizar y encontrar la zona habitable', # breve descripcion
      long_description = long_description,
      long_description_content_type = 'text/markdown',
      author = 'Ignacio Solís, Joaquin Lopez, Ignacio Cordova',
      install_requires = ['numpy', 'matplotlib'], #aqui van tus dependecias de tu programa, como numpy, pandas, cosas asi, esto hara que se instalen solos cuando instalen tu modulo si es que no tienen los necesarios
      url = 'https://github.com/nachowo21/HABZONEpy.git', # url de tu github, es opcional pero queda bien
      )
