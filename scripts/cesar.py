"""
El cifrado César, también conocido como cifrado por desplazamiento, es una de
las técnicas criptográficas de cifrado más simples y más usadas. Es un tipo 
de cifrado por sustitución monoalfabética en el que una letra en el texto 
original es reemplazada por otra letra que se encuentra un número fijo de
posiciones más adelante en el alfabeto.

https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar
"""

import string

# Símbolos que pueden cifrarse
ALFABETO = (
    f"{string.ascii_uppercase}"
    f"{string.ascii_lowercase}"
    f"{string.digits}"
    f"{string.punctuation}"
)


def cifrado(modo, texto, clave):
    # Ejecuta el proceso letra a letra
    result = ""
    for simbolo in texto:
        if simbolo in ALFABETO:
            # Identifica la posición de cada símbolo
            pos = ALFABETO.find(simbolo)
            """ Ejecuta la operación de cifrado / descifrado 
                Teoría: El proceso de cifrado de un carácter que se 
                encuentra en una posición p con un desplazamiento k
                en una alfabeto de longitud n puede describirse 
                matemáticamente del siguiente modo:
                E(p) = (p + k) mod n
                El proceso de descifrado se describiría como:
                D(p) = (p - k) mod n
            """
            if modo == "c":
                pos = (pos + clave) % len(ALFABETO)
            elif modo == "d":
                pos = (pos - clave) % len(ALFABETO)

            result += ALFABETO[pos]

        # No se cifra/descifra si no se encuentra en el ALFABETO
        else:
            result += simbolo
    return result


if __name__ == "__main__":
    # Guarda la opción deseada
    modo = ""
    while modo.lower() not in ["c", "d"]:
        modo = input("¿Deseas cifrar o descifrar? (c/d)")

    # Se almacena el texto y la clave
    texto = input("Introduce el texto: ")
    clave = int(input(f"y la clave (0-{len(ALFABETO)-1}): "))

    print(cifrado(modo, texto, clave))
