#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 23:39:54 2021

@author: alejinn
"""
#%%
import random

def generar_puntos():
    x = random.random()
    y = random.random()
    return x,y

def estimacion_pi(N):
    puntos_dentro = 0
    for i in range(N):
        x,y = generar_puntos()
        dist = x**2+y**2
        puntos_dentro += dist<1
    return 4*puntos_dentro/N