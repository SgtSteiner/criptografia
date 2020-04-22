"""
Atbash es un método criptográfico de sustitución monoalfabética en el alfabeto hebreo.
También se le conoce como código espejo, pues el alfabeto de sustitución se obtiene 
cambiando la primera letra del alfabeto por la última, la segunda por la penúltima y así sucesivamente
https://es.wikipedia.org/wiki/Atbash
"""

import string

# Alfabetos empleados.
CLARO = f"{string.ascii_lowercase} "
CIFRADO = f"{string.ascii_uppercase[::-1]} "


def cifrado(texto):
    # Ejecuta el cifrado/descrifrado letra a letra
    salida = ""
    for simbolo in texto.lower():
        # Identifica la posición de cada símbolo
        if simbolo in CLARO:
            indice = CLARO.index(simbolo)
            salida += CIFRADO[indice]
    return salida


if __name__ == "__main__":
    texto = input("Introduce un texto a cifrar/descifrar: ")
    print(cifrado(texto))
