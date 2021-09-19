#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%

def valor_absoluto(n):
    '''
    Pre: n debe ser un número real
    Pos: Devuelve el valor absoluto de n
    '''
    if n >= 0:
        return n
    else:
        return -n
    
#%%
def suma_pares(l):
    '''
    Pre: l debe ser una lista no vacía de números reales
    Pos: Devuelve la suma de todos los elementos pares en l
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0
    return res
    #Que res es la suma de los elementos pares
    #ya recorridos es un invariante de ciclo
    
#%%
def veces(a, b):
    '''
    Pre: b debe ser un entero positivo y a un numero real
    Pos: devuelve el producto de a con b
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
    #nb entero positivo y res = a*(b-nb) son invariantes de ciclo
    
#%%
def collatz(n):
    '''
    Pre: n entero positivo
    Pos: Devuelve la cantidad de pasos necesarios para llegar a 1
    desde n siguiendo la sucesión de Collatz
    '''
    res = 1
    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1
    return res
    #Que res es la cantidad de pasos dados hasta ahora es un invariante de ciclo