"""
Recupera la clave de una cifra César por fuerza bruta
"""
import string

# Símbolos que pueden cifrarse
ALFABETO = (
    f"{string.ascii_uppercase}"
    f"{string.ascii_lowercase}"
    f"{string.digits}"
    f"{string.punctuation}"
)


def hack_cesar(criptograma):
    # Recorre una a una todas las claves (tantas como la longitud del alfabeto)
    result = []
    for clave in range(len(ALFABETO)):

        salida = ""
        for simbolo in criptograma:
            if simbolo in ALFABETO:
                pos = ALFABETO.find(simbolo)
                # descrifra el carácter
                pos = (pos - clave) % len(ALFABETO)
                salida += ALFABETO[pos]

            # No se cifra/descifra si no se encuentra en el ALFABETO
            else:
                salida += simbolo

        result.append(salida)

    return result


if __name__ == "__main__":
    results = hack_cesar(input("Criptograma: "))

    for clave, salida in enumerate(results):
        print(f"Clave {clave}: {salida}")
