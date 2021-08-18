import csv
from pprint import pprint

def leer_camion(nombre_archivo): #Funcion que devuelve una lista de diccionarios con nombre, cantidad de cajones y precio por cajón
	archivo = open(nombre_archivo,'rt')
	lista_camion = []
	filas = csv.reader(archivo)
	encabezados = next(archivo).split(',')
	for rows in filas:
		try:
			diccionario_fila = {}
			diccionario_fila['nombre'] = rows[0] 
			diccionario_fila['cajones'] = int(rows[1])
			diccionario_fila['precios'] = float(rows[2])
			lista_camion.append(diccionario_fila)
		except:
			print('Error en fila')
	archivo.close()
	return lista_camion

def leer_precios(nombre_archivo): #Función que devuelve un diccionario que a cada fruta/verdura le asigna un precio
	archivo = open(nombre_archivo, 'rt')
	precios_frutas = {}
	filas = csv.reader(archivo)
	for rows in filas:
		try:
			precios_frutas[rows[0]] = float(rows[1])
		except:
			''
	archivo.close()
	return precios_frutas

lista_camion = leer_camion('../Data/camion.csv')
precios_verduleria = leer_precios('../Data/precios.csv')

costo_camion = 0
recaudacion = 0
for verduras in lista_camion: #Itero sobre los diccionarios en lista_camion
	if verduras['nombre'] in precios_verduleria: #Me fijo si la fruta/verdura está en el listado generado por la funcion leer_precios
		recaudacion += verduras['cajones']*precios_verduleria[verduras['nombre']]
		costo_camion += verduras['cajones']*verduras['precios']

print('El balance es:', round(recaudacion - costo_camion,2))
	 

