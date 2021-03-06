#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 19:22:40 2021

@author: alejinn
"""
import random
import matplotlib.pyplot as plt
import numpy as np

def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve una tupla cuyo primer elemento es:
    -1 si x no está en lista;
    p tal que lista[p] == x, si x está en lista
    El segundo elemento de la tupla es la cantidad de comparaciones que se hicieron
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    comps = 0
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
        comps +=3
    return pos,comps


def generar_lista(n, m):
    '''
    Genera una lista de n elementos ordenados, cada elemento está entre 0 y m
    '''
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    '''
    Genera un entero aleatorio incluido en [0,m-1]
    '''
    return random.randint(0, m-1)

def experimento_secuencial_promedio(lista, m, k):
    '''
    Realiza k veces la busqueda secuencial de un elemento aleatorio en la lista
    y devuelve la cantidad de comparaciones que tuvo que hacer
    '''
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]
    comps_prom = comps_tot / k
    return comps_prom

def experimento_binario_promedio(lista, m, k):
    '''
    Realiza k veces la busqueda binaria de un elemento aleatorio en la lista
    y devuelve la cantidad de comparaciones que tuvo que hacer
    '''
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[1]
    comps_prom = comps_tot / k
    return comps_prom



def graficar_bbin_vs_bseq(m, k):
    largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
    comps_promedio_secuencial = np.zeros(256)
    comps_promedio_binario = np.zeros(256)  # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
    for i, n in enumerate(largos):
        lista = generar_lista(n, m) # genero lista de largo n
        comps_promedio_secuencial[i] = experimento_secuencial_promedio(lista, m, k)
        comps_promedio_binario[i] = experimento_binario_promedio(lista, m, k)
# ahora grafico largos de listas contra operaciones promedio de búsqueda.
    plt.plot(largos,comps_promedio_secuencial,label = 'Búsqueda Secuencial')
    plt.plot(largos,comps_promedio_binario,label = 'Búsqueda Binaria')
    plt.xlabel("Largo de la lista")
    plt.xlim(0,256)
    plt.ylim(0,256)
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.legend()
    plt.show()