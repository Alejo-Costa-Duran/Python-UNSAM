import csv

def leer_camion(nombre_archivo): 
    'Funcion que devuelve una lista de diccionarios con nombre, cantidad de cajones y precio por cajón'
    archivo = open(nombre_archivo,'rt')
    lista_camion = []
    filas = csv.reader(archivo)
    encabezados = next(archivo).split(',')
    for nrows,rows in enumerate(filas,start=1):
        record = dict(zip(encabezados,rows))
        try:
            diccionario_fila = {}
            diccionario_fila['nombre'] = record['nombre'] 
            diccionario_fila['cajones'] = int(record['cajones'])
            diccionario_fila['precios'] = float(record['precio\n'])
            lista_camion.append(diccionario_fila)
        except:
            print(f'Fila {nrows}: No pude interpretar: {rows}')
    archivo.close()
    return lista_camion

def leer_precios(nombre_archivo):
    'Función que devuelve un diccionario que a cada fruta/verdura le asigna un precio'
    archivo = open(nombre_archivo, 'rt')
    precios_frutas = {}
    filas = csv.reader(archivo)
    for nrow,rows in enumerate(filas,start=1):
        try:
            precios_frutas[rows[0]] = float(rows[1])
        except:
            print(f'Fila {nrow}: No pude interpretar: {rows}')
    archivo.close()
    return precios_frutas

lista_camion = leer_camion('../Data/fecha_camion.csv')
precios_verduleria = leer_precios('../Data/precios.csv')

costo_camion = 0
recaudacion = 0
for verduras in lista_camion: #Itero sobre los diccionarios en lista_camion
    if verduras['nombre'] in precios_verduleria: #Me fijo si la fruta/verdura está en el listado generado por la funcion leer_precios
        recaudacion += verduras['cajones']*precios_verduleria[verduras['nombre']]
        costo_camion += verduras['cajones']*verduras['precios']

print('El balance es:', round(recaudacion - costo_camion,2))