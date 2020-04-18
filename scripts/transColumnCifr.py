"""
El cifrado por transposición consiste en intercambiar la posición de
las letras de un mensaje siguiendo un algoritmo conocido. Los métodos
criptográficos por transposición ya no sustituyen los símbolos de un 
mensaje por otros, sino que los mezclan en un orden que hace que el 
mensaje original ya no sea comprensible. Una técnica de permutación 
muy empleada antiguamente es la conocida como transposición columnar.
https://es.wikipedia.org/wiki/Cifrado_por_transposici%C3%B3n
"""

def salida(criptograma, bloque=5):
    # Divide una cadena en subcadenas del tamaño indicado en el bloque
    texto = ""
    for i in range(len(criptograma)):
        if (i + 1) % bloque != 0:
            texto += criptograma[i]
        else:
            texto += criptograma[i] + " "
    return texto

def cifrar(mensaje, clave):
    # Cada cadena del criptograma es una columna de la lista
    criptograma = [""] * clave

    # Recorremos cada columna de la tabla
    for col in range(clave):
        pos = col

        while pos < len(mensaje):
            criptograma[col] += mensaje[pos]

            pos += clave

    return "".join(criptograma)

if __name__ == "__main__":
    mensaje = input("Introduce el mensaje: ")
    clave = int(input("y la clave numérica: "))

    mensaje = mensaje.replace(" ", "")
    criptograma = salida(cifrar(mensaje, clave))

    print(criptograma.upper())
