import re

def tupla_centro(cadena = ""):
    """
    tupla_centro(cadena) -> (h,k)

    Funcion utilitaria para obtener las coordenadas del centro de una circunferencia
    a partir de una cadena de caracteres y usando una expresión regular. La cadena a
    validar puede ser de las formas:

                                    (h,k)     h,k

    Parámetros:
    cadena: cadena que contiene el centro de la región de la forma (h,k)
    """
    er_coor = re.compile("\(?\d*,\d*\)?")

    coincide = er_coor.search(cadena)

    if coincide:
        if cadena[0] == '(':
            cadena = cadena[1:]
        if cadena[len(cadena) - 1] == ')':
            cadena = cadena[:-1]

        separado = False
        indice = 0
        while not separado:
            if cadena[indice] == ',':
                coor_x = float(cadena[:indice])
                coor_y = float(cadena[indice + 1 :])
                separado = True
            else:
                indice += 1

        return (coor_x, coor_y)
    else:
        raise ValueError
# Fin función tupla_centro

def obtener_coordenada_central():
    invalid_input = True

    #Validar centro
    while invalid_input:
        try:
            entrada_centro = input("Introduce coordenada central de la región: ")

            
            centro = tupla_centro(entrada_centro)
            invalid_input = False
            z = centro[0] + centro[1] * 1j

        except ValueError:
            print("\n  ERROR: centro invalido. Debe ser una coordenada de la forma (h,k)," +
                " con o sin paréntesis\n")
        except EOFError:
            exit("\nTerminado\n")
    return z
# Fin obtener_coordenada_central

def obtener_radio():
    invalid_input = True
    while invalid_input:
        try:
            entrada_radio = input("Introduce radio de región: ")
            radio = float(entrada_radio)

            # Verifica que el valor del radio sea mayor a cero.
            if radio < 0:
                raise ValueError

            invalid_input = False
        except ValueError:
            print("\n  ERROR: Entrada inválida. Introduzca un número real mayor a cero.\n")
        except EOFError:
            exit("\nTerminado\n")
    return radio
# Fin funcion radio
