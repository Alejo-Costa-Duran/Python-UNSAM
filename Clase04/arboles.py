#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 09:58:55 2021

@author: alejinn
"""
#%% En este bloque están definidas las funciones que operan sobre el archivo de arbolado porteño
import csv
from collections import Counter
arbolado_porteño = "../Data/arbolado-en-espacios-verdes.csv" #Nombre del archivo con la lista de arboles

def leer_arboles(nombre_archivo):
    archivo = open(nombre_archivo)
    rows = csv.reader(archivo)
    encabezados = next(rows)
    types = [float,float,int,int,int,int,int,str,str,str,str,str,str,str,str,float,float]
    arboleda = [{nom_columna: func(arbol) for func,nom_columna,arbol in zip(types,encabezados,row)} for row in rows]
    return arboleda

def leer_parque(nombre_archivo,parque):
    'Devuelve una lista de diccionarios con la informacion de cada arbol en el parque dado como input'
    lista_parque = []
    archivo = open(nombre_archivo)
    filas = csv.reader(archivo)
    encabezados = next(filas)
    for fila in filas:
        record = dict(zip(encabezados,fila))
        record['altura_tot'] = float(record['altura_tot']) #En altura_tot guarda la altura del arbol, la guardo como float
        record['inclinacio'] = float(record['inclinacio']) #En inclinacio guarda la inclinación del arbol, la guardo como un float
        record['long'] = float(record['long'])
        record['lat'] = float(record['lat'])
        if record['espacio_ve'] == parque: #En el archivo de arbolado 'espacio_ve' indica el nombre del parque
            lista_parque.append(record)
    archivo.close()
    return lista_parque

def especies(lista_parque):
    'Devuelve el conjunto de especies de árboles que se encuentran en el parque'
    especies = []
    for arboles in lista_parque:
        especies.append(arboles["nombre_com"]) #Los nombres de las especies están bajo la columna 'nombre_com'
    return set(especies) #La función 'set()' me elimina los repetidos

def contar_ejemplares(lista_parque):
    'Cuenta los ejemplares de cada especie en un parque dado. El input tiene que ser una lista \
    de diccionarios como la que devuelve leer_parque'
    ejemplares = Counter()
    for arbol in lista_parque:
        ejemplares[arbol['nombre_com']] += 1
    return ejemplares

def obtener_alturas(lista_parque,especie):
    'Devuelve una lista con las alturas de todos los árboles de una dada especie en un parque'
    lista_alturas = []
    for arboles in lista_parque:
        if arboles['nombre_com'] == especie:
            lista_alturas.append((arboles['altura_tot']))
    return lista_alturas

def obtener_inclinacion(lista_parque,especie):
    'Devuelve una lista con las inclinaciones de todos los árboles de una dada especie en un parque'
    lista_inclinaciones = []
    for arboles in lista_parque:
        if arboles['nombre_com'] == especie:
            lista_inclinaciones.append(arboles['inclinacio'])
    return lista_inclinaciones

def especimen_mas_inclinado(lista_parque):
    'Devuelve el especimen con la mayor inclinación en un dado parque'
    especies_parque = especies(lista_parque)
    especimen = ('',0) #En esta tupla voy a guardar el especimen con mayor inclinación y su inclinacion, la inicializo vacía
    inclinacion_uniforme = True #Esta variable es por si la inclinación es nula para todas las especies, en ese caso devuelvo el ultimo
    for especie in especies_parque: #Itero sobre las especies en el parque
        inclinaciones = obtener_inclinacion(lista_parque,especie) 
        mayor_inclinacion = max(inclinaciones) #Guardo la mayor inclinacion en la especie que estoy mirando
        print(mayor_inclinacion)
        if mayor_inclinacion>especimen[1]: #La comparo con la inclinación mayor que tengo hasta ahora
            inclinacion_uniforme = False
            especimen = (especie,mayor_inclinacion) #Si la supera actualizo el especimen con mayor inclinacion
    if inclinacion_uniforme:
        print(f"Todas las especies del parque {lista_parque[0]['espacio_ve']} tienen inclinacion 0. Se devuelve el último especimen procesado")
        return (especie,mayor_inclinacion)
    return especimen

def especie_promedio_mas_inclinada(lista_parque):
    'Devuelve la especie con la mayor inclinación en promedio y esta inclinación promedio'
    especies_parque = especies(lista_parque)
    especie_mas_inclinada = ('',0) #En esta tupla voy a guardar el especimen con mayor inclinación y su inclinacion, la inicializo vacía
    inclinacion_uniforme = True
    for especie in especies_parque: #Funciona igual que especimen_mas_inclinado pero comparando promedios en vez de valores maximos
        inclinaciones = obtener_inclinacion(lista_parque,especie)
        inclinacion_prom = sum(inclinaciones)/len(inclinaciones) #El promedio como la suma sobre el total de arboles
        if inclinacion_prom>especie_mas_inclinada[1]:
            especie_mas_inclinada = (especie,inclinacion_prom)
            inclinacion_uniforme = False
    if inclinacion_uniforme:
        return (especie,inclinacion_prom)
    return especie_mas_inclinada

def arbol_mas_alto_mas_inclinado(nombre_archivo):
    'Devuelve el arbol mas alto y el mas inclinado con su latitud, longitud y especie'
    archivo = open(nombre_archivo)
    filas = csv.reader(archivo)
    encabezados = next(filas)
    arbol_mas_alto = ('especie',0,'lat','long') #Variable donde voy a guardar el arbol mas alto, incializo vacia
    arbol_mas_inclinado = ('especie',0,'lat','long')#Variable donde voy a guardar el arbol mas inclinado, la incializo vacia
    for row in filas:
        temp = dict(zip(encabezados,row))
        altura = float(temp['altura_tot'])
        inclinacion =float(temp['inclinacio'])
        if altura>arbol_mas_alto[1]: #Comparo la altura actual con la mas alta que tengo, si es mayor actualizo el arbol mas alto
            arbol_mas_alto = (temp['nombre_com'],altura,float(temp['lat']),float(temp['long']))
        if inclinacion>arbol_mas_inclinado[1]:#Igual que la altura pero con la inclinacion
            arbol_mas_inclinado = (temp['nombre_com'],inclinacion,float(temp['lat']),float(temp['long']))
    archivo.close()
    return [arbol_mas_alto,arbol_mas_inclinado]

