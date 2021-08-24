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

#%% Resultados de cantidad de especies en los parques General Paz, Los Andes, y Centenario
print('A continuación las 5 especies que más abundan en los parques General Paz, Los Andes, y Centenario: \n \n')

parques_a_mirar = ['GENERAL PAZ','ANDES, LOS','CENTENARIO']
especies_en_parques = {}

for parque in parques_a_mirar:
    especies_en_parques[parque] = contar_ejemplares(leer_parque(arbolado_porteño,parque)).most_common(5)

print(f'{"":-<79}')
print(f'|{"General Paz":^24s} |{"Los Andes":^24s} |{"Centenario":^25s}|')
print(f'{"":-<79}')
for i in range(5):
    fila = ''
    for parque in parques_a_mirar:
        temp = f"{especies_en_parques[parque][i][0]}: {especies_en_parques[parque][i][1]}" #Variable que creo temporalmente para imprimir con el formato adecuado
        fila += f"|{temp:<25s}"
    fila+='|'
    print(fila)
print(f'{"":-<79}')

#%% Mayor altura y altura promedio de Jacarandás en los mismos tres parques
print('\n\nA continuación las alturas promedio y máxima de los Jacarandá en los tres parques anteriores:\n\n')
print(f'{"":-<90s}')
print(f'|{"Medida":10s}|{"General Paz":^24s} |{"Los Andes":^24s} |{"Centenario":^25s}|')
print(f'{"":-<90s}')

alturas_maximas = {}
altura_promedio = {}
for parque in parques_a_mirar:
    lista_alturas = obtener_alturas(leer_parque(arbolado_porteño,parque),'Jacarandá')
    alturas_maximas[parque] = max(lista_alturas)
    altura_promedio[parque] = sum(lista_alturas)/len(lista_alturas)
fila_max = f'|{"max":^10s}'
fila_avg = f'|{"prom":^10s}'
for parque in parques_a_mirar:
    fila_max +=f'|{str(alturas_maximas[parque]):^25s}' 
    fila_avg +=f'|{str(round(altura_promedio[parque],2)):^25s}'
fila_max += '|'
fila_avg += '|'
print(fila_max)
print(fila_avg)
print(f'{"":-<90s}')

#%% Arbol más alto y arbol con mayor inclinación de la ciudad
print('\n\nA continuación el árbol más alto y el más inclinado de la ciudad\n\n')

arboles = arbol_mas_alto_mas_inclinado(arbolado_porteño)

encabezados = f'|{"":20s}|{"Especie":25s}|{"Medida":^18s}|{"Latitud":^10s}|{"Longitud":^10s}|'
separador = f'{"":-<89s}'
mas_alto = f'|{"Arbol más alto":<20s}|{arboles[0][0]:25s}|{"Altura: "+str(arboles[0][1])+"m":^18s}|\
{str(round(arboles[0][2],5)):10s}|{str(round(arboles[0][3],5)):10s}|'
mas_inclinado = f'|{"Arbol más inclinado":<20s}|{arboles[1][0]:25s}|{"Inclinacion: "+str(arboles[1][1])+"°":^18s}|\
{str(round(arboles[1][2],5)):10s}|{str(round(arboles[1][3],5)):10s}|'
print(separador)
print(encabezados)
print(separador)
print(mas_alto)
print(mas_inclinado)
print(separador)