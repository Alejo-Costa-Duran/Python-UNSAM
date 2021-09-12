#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 19:08:26 2021

@author: alejinn
"""

def incrementar(s):
    carry = 1
    l = len(s)
    incremento = [0]*l
    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            incremento[i] = 0
            carry = 1
        else:
            incremento[i] = s[i] + carry
            carry = 0
    return incremento

def listar_secuencias(n):
    inicial = [0]*n
    secuencias = [inicial]
    actual = incrementar(inicial)
    while actual!=inicial:
        secuencias.append(actual)
        actual = incrementar(actual)
    return secuencias
