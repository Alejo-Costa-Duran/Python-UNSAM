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
            print('Error en fila')
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

def hacer_informe(camion,precios):
    lista_informe = []
    for verduras in camion:
        cambio = precios[verduras['nombre']]-verduras['precios']
        lista_informe.append((verduras['nombre'],verduras['cajones'],verduras['precios'],cambio))
    return lista_informe

camion = leer_camion('../Data/camion.csv')
verduleria = leer_precios('../Data/precios.csv')
informe =hacer_informe(camion, verduleria)
#%%
encabezados = ('Nombre','Cajones','Precio', 'Cambio')
separador = f'{"":->10s} {"":->10s} {"":-<10s} {"":-<10s}'
print(f'{encabezados[0]:>10s} {encabezados[1]:>10s} {encabezados[2]:>10s} {encabezados[3]:>10s}')
print(separador)
for filas in informe:
    precio_pesos  = f'${filas[2]:.2f}'
    fila_formato = f'{filas[0]:>10s} {filas[1]:>10d} {precio_pesos:>10s} {filas[3]:>10.2f}'
    print(fila_formato)
