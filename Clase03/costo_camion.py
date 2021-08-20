import csv

def costo_camion(nombre_archivo):
    precio_total_pagado = 0
    precio_por_cajon = 0
    cantidad_cajones = 0
    archivo = open(nombre_archivo)
    filas = csv.reader(archivo)
    encabezados = next(filas)
    for nfila,fila in enumerate(filas,start=1):
        record = dict(zip(encabezados,fila))
        try:
            precio_por_cajon = float(record['precio'])
            cantidad_cajones = int(record['cajones'])
            precio_total_pagado += precio_por_cajon*cantidad_cajones
        except:
            print(f'Fila {nfila}: No pude interpretar: {fila}') #Imprime en pantalla la fila donde encontró un error
    archivo.close()
    return precio_total_pagado

costo = costo_camion('../Data/fecha_camion.csv')
print('Costo total:', costo)