#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 00:16:59 2021

@author: alejinn
"""
#%%
import random
import numpy as np

def medir_temp(n):
    medidas = np.array([37.5+random.normalvariate(0,0.2) for _ in range(n)])
    np.save('../Data/temperaturas',medidas)
    return medidas

def resumen_temp(n):
    medidas = medir_temp(n)
    medidas.sort()
    mediana = 0
    if n%2==0:
        mediana = (medidas[n//2-1]+medidas[n//2])/2
    else:
        mediana = medidas[n//2]
    return (max(medidas),min(medidas),sum(medidas)/n,mediana)

