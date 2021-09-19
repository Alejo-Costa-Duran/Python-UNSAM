#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:42:17 2021

@author: alejinn
"""
#%% Bloque de funciones y parámetros
import fileparse
import sys



def leer_camion(nombre_archivo): 
    'Funcion que devuelve una lista de diccionarios con nombre, cantidad de cajones y precio por cajón'
    with open(nombre_archivo) as file:
        lista_camion = fileparse.parse_csv(file, select = ['nombre','cajones','precio'], types=[str,int,float])
    return lista_camion

def leer_precios(nombre_archivo):
    'Función que devuelve una tupla que a cada fruta/verdura le asigna un precio'
    with open(nombre_archivo) as file:
        lista_precios = fileparse.parse_csv(file, has_headers = False, types = [str,float])
    return dict(lista_precios)

def hacer_informe(camion,precios):
    lista_informe = []
    for verduras in camion:
        cambio = precios[verduras['nombre']]-verduras['precio']
        lista_informe.append((verduras['nombre'],verduras['cajones'],verduras['precio'],cambio))
    return lista_informe

def imprimir_informe(informe):
    encabezados = ('Nombre','Cajones','Precio', 'Cambio')
    separador = f'{"":->10s} {"":->10s} {"":-<10s} {"":-<10s}'
    print(f'{encabezados[0]:>10s} {encabezados[1]:>10s} {encabezados[2]:>10s} {encabezados[3]:>10s}')
    print(separador)
    for filas in informe:
        precio_pesos  = f'${filas[2]:.2f}'
        fila_formato = f'{filas[0]:>10s} {filas[1]:>10d} {precio_pesos:>10s} {filas[3]:>10.2f}'
        print(fila_formato)

def informe_camion(nombre_archivo_camion,nombre_archivo_precios):
    imprimir_informe(hacer_informe(leer_camion(nombre_archivo_camion),leer_precios(nombre_archivo_precios)))
#%%Ejecucion principal
def f_principal(argumentos):
    informe_camion(argumentos[1],argumentos[2])
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
    f_principal(sys.argv)
