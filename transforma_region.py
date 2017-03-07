import math
import numpy as np
import random

def generar_complejo_aleatorio():
    """
    generar_complejo_aleatorio() -> a+bi

    Devuelve un número complejo aleatorio donde a y b son números reales
    entre -20 y 20
    """

    return random.uniform(-20, 20) + \
        (random.uniform(-20, 20) ) * 1j

def dist_complejos(z1, z2):
    """
    dist_complejos(z1, z2) -> distancia

    Función matemática para devolver la distancia entre dos números complejos
    en el plano complejo.

    Parámetros:
    z1: Número complejo
    z2: Número complejo
    """
    return math.sqrt( (np.real(z1) - np.real(z2) ) ** 2 + (np.imag(z1) - np.imag(z2)) ** 2)

def trans_reg(z, r):
    """
    trans_reg(z, r) -> (fz, radio)

    Función matemática compleja que transforma una región circular mediante
    la función 

            f(z) = az + b

    donde z es un número complejo, centro de la región circular y a y b son
    dos números complejos al azar. Regresa una región compleja circular con
    su centro y radio.

    Parametros:
    z = número complejo, centro de la región circular.
    r = radio de la región circular
    """
    
    alpha = generar_complejo_aleatorio()
    beta = generar_complejo_aleatorio()

    fz = alpha * z + beta
    fz_c = alpha * (z + r) + beta

    nuevo_radio = dist_complejos(fz, fz_c)
    
    return fz, nuevo_radio