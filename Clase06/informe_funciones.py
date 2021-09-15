#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:42:17 2021

@author: alejinn
"""
import fileparse

def leer_camion(nombre_archivo): 
    'Funcion que devuelve una lista de diccionarios con nombre, cantidad de cajones y precio por cajón'
    lista_camion = fileparse.parse_csv(nombre_archivo, select = ['nombre','cajones','precio'], types=[str,int,float])
    return lista_camion

def leer_precios(nombre_archivo):
    'Función que devuelve una tupla que a cada fruta/verdura le asigna un precio'
    lista_precios = fileparse.parse_csv(nombre_archivo, has_headers = False, select = ['nombre','precio'], types = [str,float])
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