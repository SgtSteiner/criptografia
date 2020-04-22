""" Módulo para detectar si una cadena está en español """

import string

LETRAS = string.ascii_letters + string.digits + string.punctuation


def leer_diccionario():
    with open("./docs/diccionario.txt") as file:
        return dict.fromkeys(file.read().split("\n"))


def limpiar_texto(mensaje):
    letras = [simbolo for simbolo in mensaje if simbolo in LETRAS]
    return "".join(letras)


def es_espanol(mensaje, r_lexica=0.50):
    """ es_espanol(s [,r_lexica]) -> (boolean, float)

    Por defecto, se considera que el mensaje tiene sentido en ese idioma
    si la riqueza léxica >= 0.50

    Devuelve si una cadena está en español en una tupla
    (boolean, coeficiente riqueza léxica)

    """
    mensaje = limpiar_texto(mensaje).upper()
    # crea una lista con las palabras del diccionario que existen en el mensaje
    texto = [palabra for palabra in palabras_espanol if palabra in mensaje]
    # coeficiente = suma de longitudes de las palabras encontradas / longitud del mensaje
    coef = sum(map(len, texto)) / len(mensaje)
    return coef >= r_lexica, coef


palabras_espanol = leer_diccionario()
