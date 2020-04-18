"""
Descifrado de un cifrado por transposición columnar
"""

import math

def descifrar(criptograma, clave):
    num_cols = math.ceil(len(criptograma)/clave)
    num_filas = clave
    celdas_vacias = (num_cols * num_filas) - len(criptograma)

    texto_plano = [""] * num_cols
    col = 0
    fila = 0

    for simbolo in criptograma:
        texto_plano[col] += simbolo
        col += 1

        if (col == num_cols) or \
            (col == num_cols - 1 and fila >= num_filas - celdas_vacias):
           
           col = 0
           fila += 1

    return "".join(texto_plano)

if __name__ == "__main__":
    criptograma = input("Introduce el criptograma: ")
    clave = int(input("y la clave numérica: "))

    criptograma = criptograma.replace(" ", "").lower()

    texto_plano = descifrar(criptograma, clave)
    print(texto_plano.lower())
