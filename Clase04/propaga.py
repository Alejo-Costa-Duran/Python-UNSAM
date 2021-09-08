#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:26:36 2021

@author: alejinn
"""

#%%
def propagar(lista):
    '''
    Recibe una lista con 0's, 1's y -1's y devuelve una lista donde los 1 se propagaron hacia
    sus vecinos 0
    '''
    n = len(lista)
    i=0
    nueva_lista = []
    while i<n:
        nueva_lista.append(lista[i])
        if lista[i]==1:
            siguiente = i+1
            anterior = i-1
            while (anterior>=0) and (nueva_lista[anterior]==0):
                #Este while se encarga de la propagacion hacia los vecinos anteriores
                nueva_lista[anterior] = 1
                anterior -=1
            while (siguiente<n) and (lista[siguiente]!=-1):
                #Este while se encarga de la propagacion hacia los vecinos siguientes
                nueva_lista.append(1)
                siguiente += 1
            i=siguiente
        else:
            i+=1
    return nueva_lista
#%%