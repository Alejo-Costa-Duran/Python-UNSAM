#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 12:26:49 2021

@author: alejinn
"""
#%%
def buscar_u_elemento(lista,elem):
    pos = -1
    n = len(lista)
    index = 0
    while index<n:
        if lista[index]==elem:
            pos = index
        index+=1
    return pos

def buscar_n_elemento(lista,elem):
    total = 0
    n = len(lista)
    index = 0
    while index<n:
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
    '''Devuelve el maximo de una lista,
    la lista debe ser no vacia.
    '''
    m=lista[0]
    for e in lista:
        if e<m:
            m=e
    return m
#%%