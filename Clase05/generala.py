#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 15:35:45 2021

@author: alejinn
"""
#%% Ejercicio 5.2: Generala servida
import random

def tirar():
    '''
    Genera una lista con 5 numeros aleatorios entre 1 y 6
    '''
    dados = [random.randint(1,6) for i in range(5)]
    return dados

def es_generala(tirada):
    '''
    Devuelve True si todos los dados son iguales, False si no 
    '''
    generala = (max(tirada) == min(tirada))
    return generala

def nueva_tirada(tirada):
    '''
    Toma como input una tirada de 5 dados, busca el numero que se repite más veces, separa esos dos y genera nuevos numeros para los dados restantes
    '''
    dados = [0]*6
    for e in tirada:
        dados[e-1]+=1
    repeticiones = max(dados)
    dado_repetido = dados.index(max(dados))+1
    resultado = [dado_repetido]*repeticiones
    for nuevos in range(5-repeticiones):
            resultado.append(random.randint(1,6))
    return resultado

def generala_no_servida():
    '''
    Tira los dados hasta 3 veces buscando lograr una generala, devuelve True si lo consigue False si no
    '''
    tirada = tirar()
    tirada = nueva_tirada(tirada)
    tirada = nueva_tirada(tirada)
    return es_generala(tirada)

def prob_generala(N):
    return sum([generala_no_servida() for _ in range(N)])/N
#%%
