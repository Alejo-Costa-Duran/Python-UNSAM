#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 22:10:14 2021

@author: alejinn
"""
#%%

def grok():
    raise RuntimeError('Epa!')   # Levanta una excepción acá

def spam():
    grok()                        # Esta llamada va a levantar una excepción

def bar():
    try:
        spam()
    except RuntimeError as e:     # Acá atrapamos la excepción
        print(e)
    
def foo():
    try:
        bar()
    except RuntimeError as e:
        print('Juan Carlos', e)# Por lo tanto la excepción no llega acá

foo()