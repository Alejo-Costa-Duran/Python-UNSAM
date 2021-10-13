#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:42:17 2021

@author: alejinn
"""
#%% Bloque de funciones y parámetros
import fileparse
import sys
import lote
import formato_tabla



def leer_camion(nombre_archivo): 
    'Funcion que devuelve una lista de lotes con nombre, cantidad de cajones y precio por cajón'
    with open(nombre_archivo) as lineas:
        camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return camion
    
def leer_precios(nombre_archivo):
    'Función que devuelve una tupla que a cada fruta/verdura le asigna un precio'
    with open(nombre_archivo) as file:
        lista_precios = fileparse.parse_csv(file, has_headers = False, types = [str,float])
    return dict(lista_precios)

def hacer_informe(camion,precios):
    lista_informe = []
    for verduras in camion:
        cambio = precios[verduras.nombre]-verduras.precio
        lista_informe.append((verduras.nombre,verduras.cajones,verduras.precio,cambio))
    return lista_informe

def imprimir_informe(informe, formateador):
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

def informe_camion(archivo_camion,archivo_precios, fmt='txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html
    '''
    camion = leer_camion(archivo_camion)
    precios = dict(leer_precios(archivo_precios))

    # Crear los datos para el informe
    data_informe = hacer_informe(camion, precios)

    # Imprimir el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)
    
#%%Ejecucion principal
def f_principal(argumentos):
    parametros = []
    for x in argumentos[1:]:
        parametros.append(x)
    informe_camion(*parametros)
    
if __name__ == '__main__':
    if (len(sys.argv) < 3) or (len(sys.argv) >5) :
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios formato')
    f_principal(sys.argv)
