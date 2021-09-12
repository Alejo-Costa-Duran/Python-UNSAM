import csv
import informe_funciones

def costo_camion(nombre_archivo):
    lista_camion = informe_funciones.leer_camion(nombre_archivo)
    precio_total_pagado = 0
    for verduras in lista_camion:
        precio_total_pagado += verduras['precio']*verduras['cajones']
    return precio_total_pagado

costo = costo_camion('../Data/fecha_camion.csv')
print('Costo total:', costo)