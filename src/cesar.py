# -*- coding: utf-8 -*-
'''
Created on 14 jun. 2017

@author: Steiner
'''
from _operator import pos

print("""Este programa cifra o descifra un
mensaje mediante la cifra César\n""")

import pyperclip

# Símbolos que pueden cifrarse
ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Almacena la cadena cifrada/descifrada
salida = ""

# Guarda la opción deseada
modo = input("¿Deseas cifrar o descifrar? (c/d)")

# Se almacena el texto y la clave
texto = input("Introduce el texto: ")
clave = int(input("y la clave (1-25): "))

# Ejecuta el proceso letra a letra
for simbolo in texto.upper():
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
            pos = (pos + clave) % 26
        elif modo == "d":
            pos = (pos - clave) % 26
            
        # Añade el nuevo símbolo a la cadena
        salida += ALFABETO[pos]
        
    # Añade a la cadena el símbolo sin cifrar
    #ni descifrar porque no está en el ALFABETO """
    else:
        salida += simbolo

# Imprime en pantalla el resultado
print(salida)

# Copia el mensaje al portapapeles
# pyperclip.copy(salida)