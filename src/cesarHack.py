# -*- coding: utf-8 -*-
'''
Created on 16 jun. 2017

@author: Steiner
'''

# Recupera la clave de una cifra César por fuerza bruta
ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
# almacena el criptograma
criptograma = input("Criptograma: ")

# Recorre una a una todas las claves (1 - 25)
for clave in range(1, len(ALFABETO)):
    
    # almacena la cadena descrifrada
    salida = ""
    for simbolo in criptograma:
        if simbolo in ALFABETO:
            pos = ALFABETO.find(simbolo)
            # descrifra el carácter
            pos = (pos - clave) % len(ALFABETO)
            # añade el simbolo descrifrado a la cadena
            salida += ALFABETO[pos]
            
        # si hay un expacio u otro carácter no alfabético
        # lo añade sin más
        else:
            salida += simbolo
        
    print("Clave %d: %s" % (clave, salida))
    