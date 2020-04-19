""" Descifrado por fuerza bruta del algoritmo de transposición columnar
"""

import detectarEspanol
import transColumnDescifr


def barra_progreso(limite):
    asteriscos = 0
    for numero in range(2, limite):
        if numero % (limite // 40) == 0:
            asteriscos += 1

    print(f"     0% {' ' * asteriscos}100%")
    print(f"      | {'-' * asteriscos}|")
    print("Espere ", end="")


def criptoanalisis(criptograma):
    print("\nPulsa Ctrl-C para abandonar\n")
    print("Probando claves\n")

    limite = len(criptograma)
    barra_progreso(limite)
    razones = []
    textos = []
    claves = []

    # Fuerza bruta. Se prueban todas las claves
    for clave in range(2, limite):
        texto_descrifrado = transColumnDescifr.descifrar(criptograma, clave)
        espanol, coef = detectarEspanol.es_espanol(texto_descrifrado)

        # actualiza barra de progreso
        if clave % (limite // 40) == 0:
            print("*", end="")

        if espanol:
            r_lex = coef
            textos.append(texto_descrifrado)
            razones.append(r_lex)
            claves.append(clave)

    if razones == []:
        return None

    # Seleccionamos el máximo de r_lex
    maximo = razones.index(max(razones))
    solucion = textos[maximo]
    clave = claves[maximo]

    return f"{clave} -> {solucion}"


if __name__ == "__main__":
    criptograma = input("Introduce el criptograma: ")
    criptograma = criptograma.replace(" ", "").lower()
    posible_mensaje = criptoanalisis(criptograma)

    if posible_mensaje:
        print(f"\nPosible mensaje {posible_mensaje}")
    else:
        print("\nNo ha sido posible hallar el texto")
