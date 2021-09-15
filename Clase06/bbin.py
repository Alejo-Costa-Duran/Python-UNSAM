#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 18:38:10 2021

@author: alejinn
"""

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
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
    return pos

def donde_insertar(lista, x):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Si x no está en lista devuelve la posicion donde se podria insertar,
    manteniendo la lista ordenada;
    Si x está en la lista devuelve p tal que lista[p] == x
    '''
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if pos==-1:
        if lista[medio]>x:
            pos = medio
        else:
            pos = medio+1
    return pos

def insertar(lista,x):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Si x no está en lista devuelve la posicion donde se podria insertar,
    manteniendo la lista ordenada y modifica la lista insertando x;
    Si x está en la lista devuelve p tal que lista[p] == x
    '''
    pos = donde_insertar(lista,x)
    if pos==len(lista) or lista[pos]!= x:
        lista.insert(pos,x)
    return pos
