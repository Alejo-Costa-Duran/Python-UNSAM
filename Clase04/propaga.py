#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:26:36 2021

@author: alejinn
"""

#%%
def propagar(lista):
    n = len(lista)
    i=0
    nueva_lista = []
    while i<n:
        nueva_lista.append(lista[i])
        if lista[i]==1:
            siguiente = i+1
            anterior = i-1
            while (anterior>=0) and nueva_lista[anterior]==0:
                nueva_lista[anterior] = 1
                anterior -=1
            while siguiente<n and lista[siguiente]!=-1:
                nueva_lista.append(1)
                siguiente += 1
            i=siguiente
        else:
            i+=1
    return nueva_lista
#%%