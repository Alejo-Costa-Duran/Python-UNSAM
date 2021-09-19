#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 00:07:57 2021

@author: alejinn
"""
#%%

def sumar_enteros1(desde,hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.
    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    assert (type(desde)==int and type(hasta)==int), 'Los input deben ser enteros'
    suma = 0
    if hasta<= desde:
        suma = 0
    else:
        for i in range(desde,hasta+1):
            suma+=i
    return suma

def numero_triangular(n):
    '''
    Devuelve el número triangular enésimo.
    Pre: n debe ser entero
    '''
    assert (type(n)==int), 'n debe ser entero'
    return int(n*(n+1)/2)

def sumar_enteros2(desde,hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.
    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    assert (type(desde)==int and type(hasta)==int), 'Los input deben ser enteros'
    suma = 0
    if hasta<= desde:
        suma = 0
    else:
        suma+= numero_triangular(hasta)-numero_triangular(desde-1)
    return suma
