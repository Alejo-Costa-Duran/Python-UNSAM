#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 14:16:49 2021

@author: alejinn
"""
#%%
import numpy as np
import random
import matplotlib.pyplot as plt

#%% Funciones definidas para el caso de paquetes con una sola figurita

def crear_album(figus_total):
    return np.zeros(figus_total)

def album_incompleto(A):
    return (0 in A)

def comprar_figu(figus_total):
    return random.randint(0,figus_total-1)

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    while album_incompleto(album):
            album[comprar_figu(figus_total)] +=1
    return np.sum(album)

def experimento_figus(n_repeticiones,figus_total):
    figus_compradas = [cuantas_figus(figus_total) for _ in range(n_repeticiones)]
    return np.mean(figus_compradas)
#%% Funciones definidas para el caso de paquetes con más figuritas

def comprar_paquete(figus_total, figus_paquete):
    return [random.randint(0,figus_total-1) for _ in range(figus_paquete)]

def cuantos_paquetes(figus_total,figus_paquete):
    album = crear_album(figus_total)
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total,figus_paquete)
        for figus in paquete:
            album[figus]+=1
    return sum(album)/figus_paquete

def ejercicio_519(repeticiones,figus_total,figus_paquete):
    compradas = []
    for _ in range(repeticiones):
        compradas.append(cuantos_paquetes(figus_total,figus_paquete))
    return np.mean(compradas)

def grafico_llenado():
    def calcular_historia_figus_pegadas(figus_total, figus_paquete):
        album = crear_album(figus_total)
        historia_figus_pegadas = [0]
        while album_incompleto(album):
            paquete = comprar_paquete(figus_total, figus_paquete)
            while paquete:
                album[paquete.pop()] = 1
                figus_pegadas = (album>0).sum()
                historia_figus_pegadas.append(figus_pegadas)        
        return historia_figus_pegadas
    figus_total = 670
    figus_paquete = 5
    plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
    plt.xlabel("Cantidad de paquetes comprados.")
    plt.ylabel("Cantidad de figuritas pegadas.")
    plt.title("La curva de llenado se desacelera al final")
    plt.show()
    
#%% Funciones definidas para los calculos de los ejercicios opcionales
def probabilidad_npaquetes(n_paquetes,figus_total,figus_paquete,n_repeticiones):
    experimentos = np.array([cuantos_paquetes(figus_total, figus_paquete) for _ in range(n_repeticiones)])
    return (experimentos<n_paquetes).sum()/n_repeticiones

def histograma(figus_total,figus_paquete,n_repeticiones):
    experimentos = np.array([cuantos_paquetes(figus_total, figus_paquete) for _ in range(n_repeticiones)])
    plt.hist(experimentos, bins=20)

