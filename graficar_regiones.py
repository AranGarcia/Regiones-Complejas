#!/usr/bin/python3

import entradas
import math
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import transforma_region as tr

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

    coor_escala += (2 * radio_region)

    return (- coor_escala, coor_escala, - coor_escala, coor_escala);
#Fin funcón get_axis

print("Transformación de Regiones\nf(z) = \u03B1z + \u03B2; \u03B1,\u03B2 \u03F5 \u2102\n")

z = entradas.obtener_coordenada_central()
radio = entradas.obtener_radio()

print()
if np.real(z) == 0 and np.imag(z) == 0:
    print("A = {x + iy | x ^ 2 + y ^ 2 <=", radio ** 2, '}')
else:
    print("A = {x + iy | ( x - (", np.real(z),") )\u00b2 + ( y - (", np.imag(z)
        ,") )\u00b2 \u2264", radio ** 2  , '}')


#Prepara la ventana donde se va graficar
figura = plt.figure()
figura.canvas.set_window_title("Transformación de regiones")
plt.ylabel('Imaginarios')
ax = plt.gca()
# Prepara la gráfica
plt.grid()

# Colores para círculos
colores = [ '#000000','#ff0000', '#ff3300', '#ff9900', '#cccc00', '#669900',
    '#009933', '#00cc66', '#009999', '#0099cc', '#0033cc',
    '#0000e6', '#3333cc', '#248f24', '#6600ff', '#9900ff',
    '#990099', '#6600cc', '#660066', '#4d004d', '#33001a']

# Calcula 20 veces la función de transición
fz = [z]
print(fz[0])
for i in range(20):
    fz.append( tr.trans_reg(z) )
    print('f(z) =', fz[ i + 1 ])

plt.axis( get_axis(fz, radio) )

indice = 0

circulo = plt.Circle((np.real(fz[indice]), np.imag(fz[indice])), radio,
    color = colores[indice], label = str(fz[indice]))

# Etiquetas
handles, etiquetas = ax.get_legend_handles_labels()
ax.legend(handles, etiquetas)

def init():
    ax.add_patch(circulo)
    return circulo

def animar(i):
    global indice
    global etiqueta
    if indice == 20:
        indice = 0
    circulo.center = (np.real(fz[indice]), np.imag(fz[indice]))
    L = plt.legend()
    L.get_texts()[0].set_text(fz[indice])
    circulo.set_facecolor( colores[indice] )
    indice += 1
    return circulo

anim = animation.FuncAnimation(figura, animar, init_func = init,
    interval = 500)

plt.show()