import matplotlib.pyplot as plt
import numpy as np


def zona_habitable(T_estrella,radio_estrella):
    """esta funcion toma en cuenta las temperaturas para que el agua se mantenga en su estado liquido
    siendo 273kelvin y 373kelvin, calculando así la distancia maxima y minima respectivamente"""
    d_interna = (radio_estrella/2)*((T_estrella/373)**2)
    d_externa = (radio_estrella/2)*((T_estrella/273)**2)
    return (d_interna,d_externa)

t_estrella= int(input('ingrese la temperatura de la estrella en kelvin: '))
radio_estrella = int(input('ingrese el radio de la estrella en kilometros: '))
zona_h = zona_habitable(t_estrella,radio_estrella)

print('la zona de habitabilidad de su estrella se encuentra entre: ', zona_h, 'kilometros')

centro_x = 0 # definimos la posicion (en coordenadas cartesianas) de la estrella
centro_y = 0

radio_ext = zona_h[1]/(15*5**10)
radio_int = zona_h[0]/(15*5**10)

angulos = np.linspace(0,2*np.pi,100) # aqui se le asigna el angulo total que va a recorrer el codigo 

x_exterior = centro_x + radio_ext*np.cos(angulos)
y_exterior = centro_y + radio_ext*np.sin(angulos)

x_interior = centro_x + radio_int*np.cos(angulos)
y_interior = centro_y + radio_int*np.sin(angulos)

plt.plot(x_exterior,y_exterior, label = 'exterior')
plt.plot(x_interior,y_interior, label = 'interior')

plt.fill([*x_exterior, *x_interior[::-1]], [*y_exterior, *y_interior[::-1]], color='green', alpha=0.5)  # Rellenar el segmento entre las curvas
plt.scatter(centro_x,centro_y,color = 'red' ,label = 'star')
plt.axis('equal')  
plt.title('zona habitable')       
plt.ylabel('y')
plt.xlabel('x')
plt.legend()
plt.show()