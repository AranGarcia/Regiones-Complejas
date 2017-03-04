import random

def generar_complejo_aleatorio():
    """
    generar_complejo_aleatorio() -> a+bi

    Devuelve un número complejo aleatorio donde a y b son números reales
    entre -20 y 20
    """

    return random.uniform(-20, 20) + \
        (random.uniform(-20, 20) ) * 1j

def trans_reg(z):
    """
    trans_reg(z) -> f(z)

    Función matemática compleja que transforma una región circular mediante
    la función 

            f(z) = az + b

    donde z es un número complejo, centro de la región circular y a y b son
    dos números complejos al azar. Regresa un número complejo.

    Parametros:
    z = número complejo, centro de la región circular.
    """
    
    alpha = generar_complejo_aleatorio()
    beta = generar_complejo_aleatorio()

    fz = alpha * z + beta
    
    return fz