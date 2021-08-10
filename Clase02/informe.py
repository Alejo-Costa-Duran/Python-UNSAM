import csv
from pprint import pprint

def leer_camion(nombre_archivo):
	archivo = open(nombre_archivo,'rt')
	lista_camion = []
	filas = csv.reader(archivo)
	encabezados = next(archivo).split(',')
	for rows in filas:
		try:
			diccionario_fila = {}
			diccionario_fila[encabezados[0]] = rows[0] 
			diccionario_fila[encabezados[1]] = int(rows[1])
			diccionario_fila[encabezados[2][0:-1]] = float(rows[2])
			lista_camion.append(diccionario_fila)
		except:
			print('Error en fila')
	archivo.close()
	return lista_camion

def leer_precios(nombre_archivo):
	archivo = open(nombre_archivo, 'rt')
	precios_frutas = {}
	filas = csv.reader(archivo)
	encabezados = next(archivo)
	for rows in filas:
		try:
			precios_frutas[rows[0]] = float(rows[1])
		except:
			'Oh boy'
	return precios_frutas


pprint(leer_precios('../Data/precios.csv'))