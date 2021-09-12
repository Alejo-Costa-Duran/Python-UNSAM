#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 12:26:49 2021

@author: alejinn
"""
#%%
def buscar_u_elemento(lista,elem):
    '''
    Devuelve la posición de la ultima aparición del elemento "elem"
    en la lista "lista"
    '''
    n = len(lista)
    index = 0
    while index<n:
        if lista[index]>elem:
            index = -1
            break
        if lista[index]==elem:
            return index
        index +=1
    return index

def buscar_n_elemento(lista,elem):
    '''
    Devuelve la cantidad de apariciones del elemento "elem"
    en la lista "lista"
    '''
    total = 0
    n = len(lista)
    index = 0
    while index<n:
        if lista[index]>elem:
            break
        if lista[index] == elem:
            total +=1
        index +=1
    return total
#%%
def maximo(lista):
    '''Devuelve el maximo de una lista,
    la lista debe ser no vacia.
    '''
    m=lista[0]
    for e in lista:
        if e>m:
            m=e
    return m

def minimo(lista):
    '''Devuelve el minimo de una lista,
    la lista debe ser no vacia.
    '''
    m=lista[0]
    for e in lista:
        if e<m:
            m=e
    return m
#%%