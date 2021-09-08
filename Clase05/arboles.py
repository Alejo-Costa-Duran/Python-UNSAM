#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 09:58:55 2021

@author: alejinn
"""
import csv
import matplotlib.pyplot as plt
import numpy as np
#%% Ej. 4.15: Lectura de todos los árboles

def leer_arboles(nombre_archivo):
    '''
    Dado un nombre de archivo devuelve una lista de diccionarios, cada diccionario tiene
    como claves los nombres de las columnas del archivo y como valores los de las correspondientes filas
    '''
    archivo = open(nombre_archivo)
    rows = csv.reader(archivo)
    encabezados = next(rows)
    #types = [float,float,int,int,int,int,int,str,str,str,str,str,str,str,str,float,float]
    arboleda = [{nom_columna: arbol for nom_columna,arbol in zip(encabezados,row)} for row in rows]
    archivo.close()
    return arboleda


#%% Ej. 4.16: Lista de altos de Jacarandá

def especie_alturas(arboleda,especie):
    '''
    Devuelve una lista con las alturas de todos los árboles de la especie dada en el input "especie"
    que aparezcan en la lista "arboleda"
    '''
    alturas = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']==especie]
    return alturas

#%% Ej. 4.17: Lista de altos y diametros de Jacarandás

def especie_alto_diametro(arboleda, especie):
    '''
    Devuelve una lista con las alturas y diametros de todos los árboles de la especie dada en el input "especie"
    que aparezcan en la lista "arboleda"
    '''
    alt_diam = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie]
    return alt_diam

#%% Ej. 4.18: Diccionario con medidas

def medidas_de_especies(especies, arboleda):
    '''
    Devuelve una lista de diccionarios cuyas claves son las especies dads en "especies" 
     y cuyos valores son una lista con las alturas y diametros de todos los arboles de dicha especie
    '''
    medidas = {especie: especie_alto_diametro(arboleda,especie) for especie in especies }
    return medidas

#%% Pruebas con los ejemplos mencionados

def test_4_16():
    arbolado_porteño = "../Data/arbolado-en-espacios-verdes.csv" 
    alturas = especie_alturas(leer_arboles(arbolado_porteño),'Jacarandá')
    return alturas

def test_4_17():
    arbolado_porteño = "../Data/arbolado-en-espacios-verdes.csv" 
    alturas_y_diam = especie_alto_diametro(leer_arboles(arbolado_porteño),'Jacarandá')
    return alturas_y_diam

def test_4_18():
    arbolado_porteño = "../Data/arbolado-en-espacios-verdes.csv" 
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    diccionarios = medidas_de_especies(especies, leer_arboles(arbolado_porteño))
    return diccionarios

#%%

def histograma_jacaranda():
    arboleda = leer_arboles("../Data/arbolado-en-espacios-verdes.csv")
    altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']
    plt.hist(altos)
    
def scatter_hd(lista_de_pares):
     alt_diam = np.array(lista_de_pares)
     alturas = alt_diam[0:,0]
     diametros = alt_diam[0:,1]
     plt.scatter(diametros,alturas,alpha=0.5)
     plt.xlim(0,160)
     plt.ylim(0,50)
     plt.xlabel("diametro (cm)")
     plt.ylabel("alto (m)")
     plt.title("Relación diámetro-alto para Jacarandás")
     plt.show()
     

def ejercicio_5_27():
    arboleda = leer_arboles("../Data/arbolado-en-espacios-verdes.csv")
    especies = ['Eucalipto','Palo borracho rosado','Jacarandá']
    medidas = medidas_de_especies(especies,arboleda)
    for especie in especies:
        scatter_hd(medidas[especie])