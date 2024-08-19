# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:48:57 2024

@author: Andres Gil
"""

def calcular_descuento(total_venta):
    if total_venta > 500:
        return 10  # 10% 
    elif 100 <= total_venta <= 500:
        return 5  # 5% 
    else:
        return 0  # 0% 


total = 600
descuento = calcular_descuento(total)
print(f"El descuento para una venta de ${total} es del {descuento}%.")
