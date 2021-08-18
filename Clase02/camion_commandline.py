import csv
import sys

def costo_camion(nombre_archivo):
	precio_total_pagado = 0
	precio_por_cajon = 0
	cantidad_cajones = 0
	archivo = open(nombre_archivo)
	filas = csv.reader(archivo)
	encabezados = next(filas)
	for fila in filas:
		try:
			precio_por_cajon = float(fila[2])
			cantidad_cajones = int(fila[1])
			precio_total_pagado += precio_por_cajon*cantidad_cajones
		except:
			print("Hay un error en esta fila:", fila) #Imprime en pantalla la fila donde encontró un error
	archivo.close()
	return precio_total_pagado

if len(sys.argv)==2:
	nombre_archivo = sys.argv[1]
else:
	nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)