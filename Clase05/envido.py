#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 21:54:36 2021

@author: alejinn
"""
#%%
import random
def generar_mazo():
    palos = ['espada','oro','copa','basto']
    numeros = [1,2,3,4,5,6,7,10,11,12]
    mazo = [(palo,numero) for palo in palos for numero in numeros]
    return mazo

#%%
from collections import Counter

def envido(cartas):
    '''
    Se calcula los puntos de envido de las cartas en la lista. Asume que son todas del mismo palo
    y que son 2 o 3 cartas. El input cartas es una lista con los números de cada carta
    '''
    envido_cartas = [carta if carta<10 else 0 for carta in cartas]
    envido_cartas.sort()
    puntaje = 20+envido_cartas[-1]+envido_cartas[-2]
    return puntaje

def contar_envido(mano):
    '''
    Se calcula los puntos de envido en una mano de 3 cartas dada como input
    '''
    palos_repetidos = {'espada':[],'oro':[],'copa':[],'basto':[]}
    palos = ['espada','oro','basto','copa']
    ptos_en_mano = 0
    distintos_palos = True
    for carta in mano:
        palos_repetidos[carta[0]] += [carta[1]]
    for repetidos in palos_repetidos:
        n = len(palos_repetidos[repetidos])
        if n>1:
            distintos_palos = False
            ptos_en_mano = envido(palos_repetidos[repetidos])
    if distintos_palos:
        ptos_en_mano = max([palos_repetidos[palo][0] for palo in palos if (palos_repetidos[palo]!=[])])
    return ptos_en_mano

contar_envido([('copa',1),('espada',2),('oro',3)])
def probabilidad_truco(lista,N):
    manos_buenas = 0
    mazo = generar_mazo()
    for i in range(N):
        manos_buenas += contar_envido(random.sample(mazo,3)) in lista
    return manos_buenas/N
