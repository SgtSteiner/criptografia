# -*- coding: utf-8 -*-
'''
Created on 14 jun. 2017

@author: Steiner
'''
import pyperclip

# Alfabetos empleados.
CLARO = "abcdefghijklmnopqrstuvwxyz "
CIFRADO = "ZYXWVUTSRQPONMLKJIHGFEDCBA "

# Almacena la forma cifrada / describrada del texto
salida = ""

# Guarda el texto introducido
texto = input("Introduce un texto: ")

# Ejecuta el cifrado/descrifrado letra a letra
for simbolo in texto.lower():
    # Identifica la posición de cada símbolo
    if simbolo in CLARO:
        indice = CLARO.index(simbolo)
        salida = salida + CIFRADO[indice]
        
# Imprime en pantalla el resultado
print(salida)

# Copia el mensaje al portapapeles
# pyperclip.copy(salida)