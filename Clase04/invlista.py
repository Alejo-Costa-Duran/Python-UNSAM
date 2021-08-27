#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:16:07 2021

@author: alejinn
"""

#%%
def invertir_lista(lista):
    invertida = []
    for e in lista:
        invertida = [e]+invertida
    return invertida
#%%