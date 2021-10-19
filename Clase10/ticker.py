from vigilante import vigilar
import csv
import formato_tabla
import informe_final

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = ([row[index] for index in [0,1,2]] for row in rows)
    rows = ([func(val) for func,val in zip([str,float,int],row)] for row in rows)
    rows = (dict(zip(['nombre','precio','volumen'],row)) for row in rows)
    return rows

def datos_formateador(lines):
    rows = csv.reader(lines)
    rows = ([row[index] for index in [0,1,2]] for row in rows)
    rows = (dict(zip(['nombre','precio','volumen'],row)) for row in rows)
    return rows

def ticker(fname, log, fmt = 'txt'):
    rows = datos_formateador(vigilar(log))
    camion = informe_final.leer_camion(fname)
    rows = (row for row in rows if row['nombre'] in camion)
    formateador = formato_tabla.crear_formateador(fmt)
    formateador.encabezado(['Nombre','Precio','Volumen'])
    for row in rows:
        formateador.fila([row[key] for key in row])


if __name__ == '__main__':
    camion = informe_final.leer_camion('../Data/camion.csv')
    rows = parsear_datos(vigilar('../Data/mercadolog.csv'))
    rows = (row for row in rows if row['nombre'] in camion)
    for row in rows:
        print(row)