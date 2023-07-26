def zona_habitable():
    import matplotlib.pyplot as plt
    import numpy as np

    """esta funcion toma en cuenta las temperaturas para que el agua se mantenga en su estado liquido
    siendo 273kelvin y 373kelvin (estas variables deben ser del tipo flotante),
    calculando así la distancia maxima y minima respectivamente, entregando una tupla con dichas distancias"""
    T_estrella= float(input('ingrese la temperatura de la estrella en kelvin: ')) # le pedimos al usuario que ingrese la temperatura en kelvin (este será un parametro flotante)
    radio_estrella = float(input('ingrese el radio de la estrella en kilometros: '))# al igual que t_estrella este también seerá ingresado por el usuario y será flotante
    
    d_interna = (radio_estrella/2)*((T_estrella/373)**2)
    d_externa = (radio_estrella/2)*((T_estrella/273)**2)
    zona_h = [d_interna , d_externa]

    print('la zona de habitabilidad de su estrella se encuentra entre: ', zona_h, 'kilometros')# aqui nos imprime en la terminal los valores de los radios habitables

    centro_x = 0 # definimos la posicion (en coordenadas cartesianas) de la estrella
    centro_y = 0

    radio_ext = zona_h[1]/(15*5**10) # aqui transformamos los kilometros en unidades astronomicas para mayor comprension del lector
    radio_int = zona_h[0]/(15*5**10) 

    angulos = np.linspace(0,2*np.pi,100) # aqui se le asigna el angulo total que va a recorrer el codigo con ayuda de la funcion np.pi de numpy

    x_exterior = centro_x + radio_ext*np.cos(angulos) # en esta parte de aca calculamos la distancia exterior e interior en los ejes x e y respectivamente
    y_exterior = centro_y + radio_ext*np.sin(angulos) # tambien utilizamos la funcion sin y cos de numpy para calcular los radios

    x_interior = centro_x + radio_int*np.cos(angulos)
    y_interior = centro_y + radio_int*np.sin(angulos)

    plt.plot(x_exterior,y_exterior, label = 'exterior') # con ayuda de matplotlib.pyplot graficaremos todo lo que necesitamos, en nuetro caso x exterior e interior e y exterior e interior
    plt.plot(x_interior,y_interior, label = 'interior')

    plt.fill([*x_exterior, *x_interior[::-1]], [*y_exterior, *y_interior[::-1]], color='green', alpha=0.5,label ='zona habitable')  # Rellenar el segmento entre las curvas
    plt.scatter(centro_x,centro_y,color = 'red' ,label = 'star') # creamos un punto en el eje 0,0 el cual será nuestra estrella 
    plt.axis('equal')  
    plt.title('zona habitable')       
    plt.ylabel('y [AU]')
    plt.xlabel('x [AU]')
    plt.legend()
    plt.show()

    return 
print(zona_habitable())