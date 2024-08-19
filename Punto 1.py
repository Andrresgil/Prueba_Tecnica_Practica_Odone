# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:37:24 2024

@author: Andres Gil
"""
import json
def agrupar_productos(productos):
    resultado = {}

    for producto in productos:
        fabricante = producto['Fabricante']
        categoria = producto['Categoría']
        genero = producto['Género']
        
        if fabricante not in resultado:
            resultado[fabricante] = {}
        
        if categoria not in resultado[fabricante]:
            resultado[fabricante][categoria] = {'Masculino': [], 'Femenino': []}
        
        resultado[fabricante][categoria][genero].append(producto)
    
    return [resultado]

# Diccionario:
productos = [
    {
        'Nombre': 'Zapatos XYZ',
        'Código de barras': '8569741233658',
        'Fabricante': 'Deportes XYZ',
        'Categoría': 'Zapatos',
        'Género': 'Masculino'
    },
    {
        'Nombre': 'Zapatos ABC',
        'Código de barras': '7452136985471',
        'Fabricante': 'Deportes XYZ',
        'Categoría': 'Zapatos',
        'Género': 'Femenino'
    },
    {
        'Nombre': 'Camisa DEF',
        'Código de barras': '5236412896324',
        'Fabricante': 'Deportes XYZ',
        'Categoría': 'Camisas',
        'Género': 'Masculino'
    },
    {
        'Nombre': 'Bolso KLM',
        'Código de barras': '5863219635478',
        'Fabricante': 'Carteras Hi-Fashion',
        'Categoría': 'Bolsos',
        'Género': 'Femenino'
    }
]

agrupado = agrupar_productos(productos)
print(json.dumps(agrupado, indent=4, ensure_ascii=False)) # Muestro los resultados adecuados 








































