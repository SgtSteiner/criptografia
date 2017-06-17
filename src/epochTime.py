# -*- coding: utf-8 -*-
'''
Created on 17 jun. 2017

@author: Steiner

Programa que lee la hora del meridiano de Greenwich y la 
convierte a días, horas, minutos y segundos.
'''

import time

# Devuelve el tiempo en segundo desde "the epoch",
# según el meridiano de Greenwich
epoca = time.time()

dias = epoca / (60 * 60 * 24)
horas = (epoca / (60 * 60) ) % 24
minutos = (epoca / 60) % 60
segundos = epoca % 60

print("Desde el 1 de enero de 1970 a las 00:00 han transcurrido\n")
print("%d días, %d h %d m %d s" % (dias, horas, minutos, segundos))
    

