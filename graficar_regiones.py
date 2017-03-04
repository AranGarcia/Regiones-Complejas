import math
import matplotlib.pyplot as plt
import numpy as np

def get_axis(coordenadas, radio_region):
    """
    get_axis() -> (x_min, x_max, y_min, y_max)

    Función auxiliar para conseguir valores de abscisa y coordenadas
    maximos y mínimos adecuada para obtener escala adecuada para pyplot.plot
    y no se vean deformes los círculos
    """
    
    coor_escala = 0
    
    # Iterar a través de todos las coordenadas
    for i in range(1, len(coordenadas)):
        if math.fabs(np.real(coordenadas[i])) > coor_escala:
            coor_escala = np.real(coordenadas[i])
        
        if math.fabs(np.imag(coordenadas[i])) > coor_escala:
            coor_escala = np.imag(coordenadas[i])
    # Fin iteracion

    coor_escala += (radio_region)

    return (- coor_escala, coor_escala, - coor_escala, coor_escala);
#Fin funcón get_axis

def graficar(regiones, radio_region):
    """
    """
    if regiones == None or len(regiones) == 0:
        return
    ejes = get_axis(regiones, radio_region)

    #Prepara la ventana donde se va graficar
    fig = plt.gcf()
    fig.canvas.set_window_title("Transformación de regiones")
    plt.ylabel('Imaginarios')
    print(ejes)
    plt.axis(ejes)
    plt.grid()

    colores = ['#ff0000', '#ff3300', '#ff9900', '#cccc00', '#669900',
        '#009933', '#00cc66', '#009999', '#0099cc', '#0033cc',
        '#0000e6', '#3333cc', '#248f24', '#6600ff', '#9900ff',
        '#990099', '#6600cc', '#660066', '#4d004d', '#33001a']

    #Dibuja  círculo para representar el límite de todas las raíces
    for i in range(len(regiones)):
        circulo = plt.Circle((np.real(regiones[i]), np.imag(regiones[i])),
            radio_region, color = colores[i], fill = True, linestyle = ":")
        ax = plt.gca()
        ax.add_artist(circulo)

    plt.show()
