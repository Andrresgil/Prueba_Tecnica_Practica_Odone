# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:40:03 2024

@author: Andres Gil
"""
# Suponiendo que la base de datos esta en SQLite
import sqlite3

conexion = sqlite3.connect('Base_de_datos.db')

cursor = conexion.cursor()

# Consulta
cursor.execute("""
    SELECT order_id, amount_total, customer_name
    FROM ordenes_venta
    WHERE amount_total > 1000;
""")

resultados = cursor.fetchall()

for fila in resultados:
    print(f"Order ID: {fila[0]}, Amount Total: {fila[1]}, Customer Name: {fila[2]}")

#Cierro conexion
conexion.close()
