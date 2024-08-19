# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:36:11 2024

@author: Andres Gil
"""
# Utilizando Try - Except 

mi_diccionario = {'nombre': 'Juan', 'edad': 30}

try:
    direccion = mi_diccionario['direccion']
except KeyError:
    print("La clave 'direccion' no existe en el diccionario.")

